# agit

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Built with Rust](https://img.shields.io/badge/built%20with-Rust-orange?logo=rust&logoColor=white)](https://www.rust-lang.org)

Lossless version control for every agent session: publishable, resumable.
Works with Claude Code, Codex, OpenCode, and Cursor.

On disk, sessions are just JSONL files that get overwritten, compacted, and
cleaned up at any moment. `agit` puts snapshots and versions on top of them,
so "that conversation last Wednesday that finally cracked the bug" becomes
something you can find, continue, and hand to a teammate.

```text
agit                              choose a session to continue
agit new                          choose a repo and name a fresh conversation
agit import                       choose an existing runtime conversation to adopt
agit log                          choose a session and browse its history
agit push                         choose a saved session to publish
agit share                        choose a session and review link settings
agit run owner/repo@ref           open a saved source, forking when needed
```

These bare commands open their interfaces in a human terminal. `agit resume`
continues the same session and never forks; `agit run` can start a new writable
session from a tag, historical point or another author's source.

Inside an adopted agent session, `agit commit` saves completed turns and
`agit push` publishes that session. For scripts, pass the target explicitly,
for example `agit push owner/repo@branch --json`. Directory branch pins do not
choose targets for `commit`, `push` or `share`.

On user-facing startup, `agit` checks for a newer release at most once a day and prints a
reminder to stderr; it never upgrades automatically. JSON/quiet/CI and internal hook/MCP paths
skip this reminder.

Adopting and recording the first version are one command — the in-between
state ("linked, but unversioned") means nothing to anyone. To mark a session
without versioning it (e.g. offline), pass `--link-only`.

Use a full native session ID and an explicit runtime and destination for lineage discovery.
The terminal offers verified local bases, independent import, or cancellation. Noninteractive
calls return choices without writing; pass `--onto <ref>` or `--independent` to select a path.
`--propose-lineage` prints a read-only report without adopting the session.
Inspecting lineage in an existing repository requires NUL-framed Git worktree output,
normally available in Git 2.36 or newer. An unsupported Git reports `git_worktree_format`;
explicit `--onto`, `--independent`, and `--link-only` imports retain their ordinary checks.

`agit clone` fetches repository history locally. Use `agit run` or `agit resume`
to start a runtime. A clone is **read-only by default** on the Hub: nothing is
created in your name and `origin` points at the source. `agit clone --mine`
creates your copy, repoints `origin` and remembers the source as `upstream`.

The full command list is in `agit --help`.

## Install

### Users: npm

```sh
npx -y create-agit                 # one-shot: installs agit + wires skills/hooks/MCP
# or as a global package:
npm install -g @einsia/agent-git   # pnpm add -g @einsia/agent-git works too
agit --version
```

Both routes install a prebuilt binary — no Rust toolchain required. npm
picks the platform sub-package matching your `os`/`cpu`; on platforms with no
prebuilt binary (e.g. FreeBSD) running `agit` prints the source-build recipe.
Details and environment variables: [`npm/README.md`](npm/README.md).

Windows x64 packages include the native peer RC daemon. On Windows, Linux and macOS, run
`agit login` followed by `agit rc start --detach` to register the device and allow your own
account to control it from Workspaces. Windows owner RPC uses a local named pipe restricted
to the current user. RC state requires a private, user-owned directory.

pnpm (v10+) does not run dependency install scripts by default, so the
automatic `agit setup` is skipped there — run `agit setup` once yourself
after installing.

The Linux artifact is **musl static-linked**, so no minimum glibc — the
release pipeline runs every Linux binary inside an Alpine / Amazon Linux /
Debian / Ubuntu container matrix before publishing.

Prebuilt binaries include Git and Git LFS, extracted into a private cache on first
use. Your shell PATH and global Git configuration stay unchanged. Source builds
use system Git; `AGIT_USE_SYSTEM_GIT=1` selects it in a prebuilt binary too.
See [runtime configuration and source prerequisites](docs/01_setup.md).

> Do not install `@einsia/agentgit` (no hyphen) — that is the pre-rewrite
> CLI; its protocol does not match this branch and it will not work.

### Contributors / eager users: from source

```sh
git clone https://github.com/Einsia/agent-git
cd agent-git
./setup.sh
```

`setup.sh` checks the toolchain (rustc, a C compiler), builds, and installs
the binary to `~/.local/bin/