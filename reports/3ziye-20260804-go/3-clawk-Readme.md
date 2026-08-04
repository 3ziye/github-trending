<div align="center">

<img src="assets/clawk-lockup-orange-transparent.png" alt="clawk" width="400">

*Give a coding agent its own disposable Linux machine, not yours.*

[![CI](https://github.com/clawkwork/clawk/actions/workflows/ci.yml/badge.svg)](https://github.com/clawkwork/clawk/actions/workflows/ci.yml)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Go 1.26+](https://img.shields.io/badge/Go-1.26%2B-00ADD8?logo=go&logoColor=white)](go.mod)
![Platform: macOS · Linux (experimental)](https://img.shields.io/badge/platform-macOS%20%C2%B7%20Linux%20(experimental)-lightgrey)

**[Install](#install)** · **[Quickstart](#quickstart)** ·
**[Why a VM?](#why-a-vm)** · **[How it works](#how-it-works)** ·
**[Compared to](#compared-to)** · **[FAQ](#faq)** · **[Docs](docs/)**

</div>

A coding agent is only useful when you let it actually *do* things: install
packages, run the code it writes, start servers, use the network. On your own
machine that leaves two bad options. You approve every command (and babysit a
prompt every few seconds), or you run `--dangerously-skip-permissions` and hope
nothing important is one `rm -rf` or one leaked token away.

clawk is a third option. `cd` into a repo, type `clawk`, and Claude Code (or
Codex, or a shell) is working inside a disposable Linux VM (your code mounted
in, root in the guest, no permission prompts) while your files, your keychain,
and the rest of your machine stay out of reach. **The agent gets its own
machine instead of yours.**

<p align="center">
  <img src="assets/demo.gif" alt="clawk demo: clawk boots a VM and attaches claude; a blocked attempt to send data to an unknown server shows up in clawk network denials; clawk attach resumes the sandbox later" width="760">
  <br>
  <sub><i>One command to a working agent; an attempt to send data to an
  unknown server, blocked by the network allow-list; <code>clawk attach</code>
  resumes the session later.</i></sub>
</p>

The boundary isn't a rule in a prompt the agent could be talked out of. It's
a separate machine, and the only openings are the ones you mounted. From a
shell inside a sandbox:

```console
$ curl https://tracker.evil.example   # not on the allow-list: blocked
curl: (7) Failed to connect to tracker.evil.example port 443 after 2 ms: Connection refused

$ cat ~/.ssh/id_rsa                   # your keys never entered the VM
cat: /home/agent/.ssh/id_rsa: No such file or directory

$ git push                            # ...yet this works: ssh-agent is forwarded
Enumerating objects: 5, done.
```

To be honest about the limits, the allow-list blocks connections to *unknown*
servers, not to ones you've allowed: github.com is pre-allowed and the
forwarded ssh-agent can push, so treat anything the agent can read as
something it could publish. The
[security model](#security-model-and-its-limits) spells this out.

And if the agent wrecks the VM, run `clawk destroy && clawk`: a fresh VM, same
repo, and `--resume` restores the conversation.

> [!IMPORTANT]
> **Pre-1.0 and moving fast.** Expect breaking changes between releases and
> the occasional rough edge; things can and will break. Please file issues;
> that feedback is shaping 1.0.

## Highlights

- **Let the agent do anything.** It runs in a disposable VM with a restricted
  network, so `rm -rf`, package installs, and untrusted code can't reach your
  host, your files, or anything you didn't explicitly share.
- **Working in one command.** `cd` into a repo and run `clawk`. No
  Dockerfile, devcontainer, or setup file. First boot builds a rootfs from
  your image; every boot after takes seconds.
- **Break it without losing anything.** Destroy and recreate freely; your
  code and the agent's conversations live on the host. Only the disposable
  VM disk is lost.
- **A real Linux box, your toolchain.** Any OCI image is the rootfs: a full
  OS with exactly the tools your project needs. No Docker daemon required.
- **Secrets stay on your machine.** Outbound traffic is allow-listed and your
  ssh-agent is forwarded, so `git push` works without keys entering the VM.
- **A sandbox per project or ticket.** Run several at once; multi-repo
  tickets get a git worktree per repo with coordinated PRs. Idle VMs
  automatically release memory and suspend to disk, so a forgotten sandbox
  costs (almost) nothing.

## Why a VM?

clawk is a general-purpose local environment for autonomous coding agents.
The VM is the point: it's a whole machine the agent can own, not a process
wrapped in policy on the one you're using.

- **A separate kernel.** The guest runs its own Linux kernel, so the host
  filesystem isn't hidden behind deny rules; it was never mounted.
- **A conventional Linux environment.** Standard kernel, standard userland,
  `/dev/kvm`-shaped expectations, so tools behave the way their docs say,
  without a syscall-filter surprise.
- **Root in the guest.** Install system packages, edit `/etc`, load a module,
  bind a privileged po