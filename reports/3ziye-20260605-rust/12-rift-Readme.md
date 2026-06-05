> **Warning: Experimental repository**
>
> This repository is experimental and is not ready for use. We are exploring a variety of ideas here, and behavior, interfaces, and implementation details may change without notice.

rift: better alternative to git worktrees

- copy on write (saves space)
- instant (< 0.1s on 10gb folder)
- fast cli
- use as FFI lib with bun or node

mac and linux with btrfs or native reflinks for now
more support soon

## Install

```bash
npm install -g rift-snapshot
# or
bun add -g rift-snapshot
```

Release archives are available from [GitHub Releases](https://github.com/anomalyco/rift/releases/latest).

## Platforms

| Platform          | Backend                             | Behavior                                                           |
| ----------------- | ----------------------------------- | ------------------------------------------------------------------ |
| Linux x64         | Writable btrfs snapshots            | `rift init` converts an ordinary directory into a btrfs subvolume. |
| Linux x64         | Native per-file reflinks            | `rift init` verifies reflink support and registers the directory.  |
| macOS arm64 / x64 | APFS `clonefile`                    | `rift init` registers the source directory.                        |
| Windows x64       | None                                | The package is published; workspace creation is not implemented.   |

## CLI

### Initialize

```bash
cd ~/code/app
rift init
```

`rift init` selects an existing Rift root above the current directory, or the nearest Git root when no Rift root exists. Use `--here` to initialize exactly the selected directory.

On Linux, first initialization of an ordinary btrfs directory performs a reflink import into a new btrfs subvolume and swaps it into the same path. On other Linux filesystems, initialization verifies native reflink support and registers the directory in place. This includes XFS and other filesystems when their `FICLONE` support succeeds. If the selected root is registered already, no conversion occurs. If its `.rift` marker is missing, `rift init` restores it and completes any required setup.

### Create

```bash
rift create
rift create --name parser-fix
rift create --into /fast/rifts
rift create --copy-all
rift create --no-hooks
```

`rift create` searches upward for `.rift`, copies that managed workspace, records the immediate parent, and prints the new workspace path to stdout.

By default, creation omits heavyweight regenerable dependency and build artifacts such as `node_modules`, `target`, virtualenvs, framework caches, `dist`, `build`, and `coverage`. Manifests and lockfiles are preserved. Use `--copy-all` to keep the previous exact-copy behavior.

On btrfs, exact copies use writable subvolume snapshots and filtered copies use a reflink import into a new subvolume. On other reflink-capable Linux filesystems, Rift reflink-clones the selected directory tree. On macOS, exact copies use APFS `clonefile`, and filtered copies clone included entries.

When the workspace is a Git repository, the new workspace has detached `HEAD` and retains index and working-tree state.

If the source contains `.rift.toml`, `rift create` runs configured postcreate hooks after the workspace is created, registered, and prepared. Use `--no-hooks` to skip them.

```toml
version = 1

[[hooks.postcreate]]
run = "pnpm install --frozen-lockfile"

[[hooks.postcreate]]
run = "pnpm run codegen"
```

Postcreate commands run in the new workspace root. If a hook fails, the workspace remains registered and `rift create` exits with an error.

### List And Ancestors

```bash
rift list
rift ancestors
```

`list` prints direct active child workspaces. `ancestors` prints parent workspaces, nearest first.

### Remove And Garbage Collection

```bash
rift remove                         # trash the current created rift subtree
rift remove -f ~/code/app           # unregister a source root
rift remove --children ~/code/app   # trash descendants, preserve the selected workspace
rift gc                             # physically delete trash and prune missing entries
```

Removing a created rift moves its active subtree into adjacent `.trash` storage. `rift gc` deletes that storage later.

Removing a source root requires `-f` in the CLI. The source directory remains on disk. Its `.rift` marker is removed. Existing registered descendants are moved into trash. Missing descendants are removed from the registry.

### Shell Integration

```bash
eval "$(rift shell-init zsh)" # or bash
```

```nushell
rift shell-init nushell | save -f (($nu.user-autoload-dirs | first) | path join "rift.nu")
```

The shell wrapper changes directory after `init` conversion, `create`, or removal of the current created rift.

## Storage

Each managed workspace has a `.rift` marker containing its identifier. An SQLite registry stores paths, parent identifiers, and trash entries.

Default created-workspace storage is adjacent to the registered s