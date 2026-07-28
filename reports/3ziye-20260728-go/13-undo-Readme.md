# undo

**Revert what the last shell command did to the filesystem.**

[![CI](https://github.com/edaywalid/undo/actions/workflows/ci.yml/badge.svg)](https://github.com/edaywalid/undo/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/edaywalid/undo?sort=semver)](https://github.com/edaywalid/undo/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Website: [undo.edaywalid.com](https://undo.edaywalid.com)

![undo reverting an accidental rm -rf](assets/demo.gif)

Works for the classic mistakes: `rm` / `rm -rf`, `mv` over a file you
needed, truncating with `>`, an accidental `chmod -R`, files and
directories created by a script that ran amok. Changed your mind again?
`undo redo` re-applies. Undo never deletes anything permanently, only
parks it in the session store, so a session toggles between undone and
applied as many times as you like.

**Contents**

- [Why](#why)
- [How it works](#how-it-works)
- [Install](#install)
- [Usage](#usage)
- [Storage and disk space](#storage-and-disk-space) - what it keeps, for
  how long, and what it costs you
- [Ignoring build noise](#ignoring-build-noise)
- [Configuration](#configuration) - every environment variable
- [What it cannot catch](#what-it-cannot-catch)
- [Secure deletion](#secure-deletion) - read this before `shred`
- [Platform support](#platform-support)
- [Upgrading](#upgrading) and [Uninstalling](#uninstalling)
- [Development](#development)

## Why

The shell has never had an undo, and the usual advice is that once data
is overwritten it is gone. The tools that do exist ask you to change
your habits first: alias `rm` to a trash command, or set up btrfs/zfs
snapshots before the accident. undo asks for nothing. You keep typing
`rm`, and the safety net is already under you, even when the deletion
happens three processes deep inside a build tool where no alias could
reach.

It is command-granular, not time-granular: it reverts exactly what *that
one command* touched, on any filesystem, without root. That is the
difference from a snapshot, which rolls the whole tree back to a point in
time and takes your good work with it.

## How it works

There is no snapshotting and no daemon. Nothing runs between your
commands.

1. **Hook.** A shell hook (zsh, bash, fish) arms a small `LD_PRELOAD`
   library, `libundo.so`, around every command you run.
2. **Journal.** While armed, the library intercepts destructive libc
   calls (`unlink`, `rename`, `open` with write flags, `rmdir`, `mkdir`,
   `chmod`, ...). Before each one goes through, it saves the affected
   file into a per-command session and appends a line to a journal.
   Deletions are saved by **hardlink**, so `rm -rf` on gigabytes copies
   no data and costs almost nothing.
3. **Replay.** `undo` reads the last session's journal and replays it in
   reverse: relink deleted files, move renames back, swap truncated
   files with their backups, remove accidental creations, recreate
   directories with their original modes.

Each command that changed something gets one session directory. The
whole storage format is plain files you can inspect:

```
~/.local/share/undo/sessions/        (mode 0700)
└── 1784718280691946/
    ├── cmd        rm -rf thesis/          the command line, for `undo list`
    ├── journal    one line per change     replayed in reverse
    ├── pid, done  liveness markers        so undo won't touch a running command
    └── data/
        ├── 48211-1   = thesis/draft.md    (hardlink, no data copied)
        └── 48211-2   = thesis/refs.bib
```

The last 30 sessions are kept, within a 1 GiB budget; both are
configurable, and `undo purge` wipes the store. The most recent session
is always kept, even if it alone exceeds the budget, since that is the
one `undo` reverts.

## Install

### 1. Get the binary

Any distro, no root, nothing to configure:

```sh
curl -fsSL https://undo.edaywalid.com/install.sh | sh
```

That installs into `~/.local`, then **asks** whether to add the hook line
to your shell rc, showing you the exact line first. Say no and it prints
the instructions instead; it never edits anything when there is no
terminal to ask at (a CI run, a piped install). `UNDO_MODIFY_RC=1`
answers yes for scripted installs, `UNDO_NO_MODIFY_RC=1` answers no.

Prefer a package manager?

| Channel | Command |
| --- | --- |
| Homebrew (Linux) | `brew install edaywalid/tap/undo` |
| Debian / Ubuntu | `.deb` from [releases](https://github.com/edaywalid/undo/releases), then `sudo dpkg -i undo_*.deb` |
| Fedora / openSUSE | `.rpm` from [releases](https://github.com/edaywalid/undo/releases), then `sudo rpm -i undo_*.rpm` |
| Arch | `yay -S undo-cli-bin` (AUR), or `.pkg.tar.zst` from [releases](https://github.com/edaywalid/undo/releases) |
| Nix | `nix run github:edaywalid/undo` (flake, experimental) |
| From source | `make install` (needs gcc + go, installs to `~/.local`) |

### 2. Turn it on

If you let the installer do it, open a new terminal and skip to st