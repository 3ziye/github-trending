<h1 align="center">sandboxd</h1>


<p align="center">
  <b>The open-source engine for AI app-builder products.</b><br/>
  Give every user an isolated cloud dev environment, a built-in coding agent,
  and a live preview URL — self-hosted, on one machine, in one command.
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-green.svg"></a>
  <img alt="Runs on Docker" src="https://img.shields.io/badge/runs%20on-Docker-2496ED.svg">
  <img alt="Single binary control plane" src="https://img.shields.io/badge/control%20plane-single%20Go%20binary-00ADD8.svg">
  <img alt="Status: beta" src="https://img.shields.io/badge/status-beta-yellow.svg">
</p>

---

<img width="1100" height="816" alt="sandboxd-demo" src="https://github.com/user-attachments/assets/f794ff9b-8ffe-47e8-bd30-22541f870f09" />


## What is sandboxd? (start here)

Think of the apps where you type *"build me a todo app"* and seconds later a
working website appears at its own link — like Lovable, Bolt, v0, or Replit.
**sandboxd is the open-source backend that makes that possible**, running on
your own server.

Here's what it does, in plain terms. You send it one HTTP request, and it:

1. **Creates a sandbox** — a private, isolated Linux container (its own
   filesystem, its own memory limits), so one user's code can never see or
   break another's.
2. **Runs an AI coding agent inside it** — you give it a prompt, and it writes
   the code into that sandbox. (The OpenCode and Claude Code CLIs come
   pre-installed.)
3. **Gives the app a live URL** — the dev server running inside the sandbox is
   instantly reachable at a shareable preview link.

```
POST /sandbox          → a private, isolated container spins up
POST .../tasks         → an AI agent writes an app inside it
http://<id>.preview... → that app is live at its own URL
```

It's also cheap to run: a sandbox **goes to sleep when nobody's using it**
(freeing memory) and **wakes up the instant someone opens its link again** —
files are saved on disk the whole time. So one ordinary server can hold many
users instead of needing one virtual machine each.

Under the hood it's deliberately small and easy to understand: **one Go program
that tells Docker what to do**, with **Traefik** handling the URLs and
**SQLite** as the database. No Kubernetes, no separate database server, no
message queue — you could read the whole thing in an afternoon.

```
            ┌──────────────── your host (just needs Docker) ────────────────┐
 browser ──▶│  Traefik  ──▶  sandbox  (coding agent + dev server :3000)      │
            │     ▲              ▲   ▲                                        │
 API/CLI ──▶│  sandboxd ─────────┘   └─ workspace dir (persists)             │
            │     │  SQLite (source of truth) · idle→stop · request→wake      │
            └─────┴────────────────────────────────────────────────────────-─┘
```

### Who's it for?

**✅ Use it if** you're running **many sandboxes for other people** — an AI
app-builder ("describe an app → see it live"), an agent platform, a coding
playground, per-user or per-branch preview environments, or multi-app hosting
for a team.

**❌ Skip it if** you just need one or two containers for yourself — a shell
script, `docker run`, or [lxd](https://canonical.com/lxd) is simpler. (More on
that [below](#why-not-just-a-shell-script).)

## Why sandboxd?

If you're building an **AI app-builder, an agent platform, a coding playground,
or a per-user preview product**, the hard part isn't the prompt — it's the
infrastructure underneath it:

- **Multi-tenant isolation** so one user's code can't touch another's.
- **Per-user preview URLs** with automatic routing and TLS.
- **Cost control** — idle environments must release memory, or your bill explodes.
- **Agent orchestration** — run a coding agent against a workspace, stream its
  progress, capture the result.
- **Persistence, wake-on-demand, reconciliation after a crash or reboot.**

That's months of platform work. sandboxd is that platform, distilled to one
command:

- ⚡ **One-command install.** `./install.sh` and you have a working API + previews.
- 🧠 **Agents included.** The OpenCode and Claude Code CLIs ship in every sandbox;
  hand a sandbox a prompt and it builds.
- 💸 **Dense by design.** Stop-on-idle + wake-on-request means dozens of sandboxes
  share one box instead of one VM each — the difference between a $20 server and
  a $2,000 cluster.
- 🔓 **Yours.** Self-hosted, MIT-licensed, no vendor lock-in. Own your data, your
  margins, and your roadmap.
- 🪶 **Boring on purpose.** SQLite + the `docker` CLI + Traefik. A reconciler
  converges Docker back to the database on every boot. You can read the whole
  control plane in an afternoon.

## "Why not just a shell script?"

Fair question — and honestly: **if you need one or two long-lived containers for
yourself, a shell script (or `docker run`, or [lxd](https://canonical.com/lxd))
is simpler. Use that.** We mean i