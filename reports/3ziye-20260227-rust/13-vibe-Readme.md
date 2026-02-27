Vibe is a quick, zero-configuration way to spin up a Linux virtual machine on Mac to sandbox LLM agents:

```
$ cd my-project
$ vibe

░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░
 ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░
 ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓██████▓▒░
  ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░
  ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░
   ░▒▓██▓▒░  ░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░

Host                                      Guest                    Mode
----------------------------------------  -----------------------  ----------
/Users/dev/work/my-project                /root/my-project         read-write
/Users/dev/.cache/vibe/.guest-mise-cache  /root/.local/share/mise  read-write
/Users/dev/.m2                            /root/.m2                read-write
/Users/dev/.cargo/registry                /root/.cargo/registry    read-write
/Users/dev/.codex                         /root/.codex             read-write
/Users/dev/.claude                        /root/.claude            read-write
/Users/dev/.gemini                        /root/.gemini            read-write

root@vibe:~/my-project#
```

On my M1 MacBook Air it takes ~10 seconds to boot.


Dependencies:

- An ARM-based Mac running MacOS 13 (Ventura) or higher.
- A network connection is required on the first run to download and configure the Debian Linux base image.
- That's it!


## Why use Vibe?

- LLM agents are more fun to use with `--yolo`, since they're not always interrupting you to approve their commands.
- Sandboxing the agent in a VM lets it install/remove whatever tools its lil' transformer heart desires, *without* wrecking your actual machine.
- You control what the agent (and thus the upstream LLM provider) can actually see, by controlling exactly what's shared into the VM sandbox.
  (This project was inspired by me running `codex` *without* `--yolo` and seeing it reading files outside of the directory I started it in --- not cool, bro.)

I'm using virtual machines rather than containers because:

- Virtualization is more secure against malicious escapes than containers or the MacOS sandbox framework.
- Containers on MacOS require spinning up a virtual machine anyway.

Finally, as a matter of taste and style:

- The binary is < 1 MB.
- I wrote the entire README myself, 100% with my human brain.
- The entire implementation is in one ~1200 line Rust file.
- The only Rust dependencies are the [Objc2](https://github.com/madsmtm/objc2) interop crates and the [lexopt](https://github.com/blyxxyz/lexopt) argument parser.
- There are no emoji anywhere in this repository.


## Install

Vibe is a single binary built with Rust.

Download [the latest binary built by GitHub actions](https://github.com/lynaghk/vibe/releases/tag/latest) and put it somewhere on your `$PATH`:

    curl -LO https://github.com/lynaghk/vibe/releases/download/latest/vibe-macos-arm64.zip
    unzip vibe-macos-arm64.zip
    mkdir -p ~/.local/bin
    mv vibe ~/.local/bin
    export PATH="$HOME/.local/bin:$PATH"

If you use [mise-en-place](https://mise.jdx.dev/):

    mise use github:lynaghk/vibe@latest

I'm not making formal releases or keeping a change log.
I recommend reading the commit history and pinning to a specific version.

You can also install via `cargo`:

    cargo install --locked --git https://github.com/lynaghk/vibe.git

If you don't have `cargo`, you need to install Rust:

    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh


## Using Vibe


```
vibe [OPTIONS] [disk-image.raw]

Options

  --help                                                    Print this help message.
  --version                                                 Print the version (commit SHA and build date).
  --no-default-mounts                                       Disable all default mounts, including .git and .vibe project subfolder masking.
  --mount host-path:guest-path[:read-only | :read-write]    Mount `host-path` inside VM at `guest-path`.
                                                            Defaults to read-write.
                                                            Errors if host-path does not exist.
  --cpus <count>                                            Number of virtual CPUs (default 2).
  --ram <megabytes>                                         RAM size in megabytes (default 2048).
  --script <path/to/script.sh>                              Run script in VM.
  --send <some-command>                                     Type `some-command` followed by newline into the VM.
  --expect <string> [timeout-seconds]                       Wait for `string` to appear in console output before executing next `--script` or `--send`.
                                                            If `string` does not appear within timeout (default 30 seconds), shutdown VM with error.
```

Invoking vibe without a disk image:

- shares the current directory with the VM
- shares package manager cache directories with the VM, s