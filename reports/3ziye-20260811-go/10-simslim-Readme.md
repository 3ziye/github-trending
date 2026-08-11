# simslim

Run a lot more iOS simulators on one Mac by turning off the background daemons a simulator doesn't need.

A freshly booted iOS simulator starts around 180 background services: Siri, Spotlight indexing, photo analysis, News, wallpaper posters, iCloud sync, and so on. None of it matters when you're using the simulator for development, testing, or CI. simslim switches those services off, which cuts each simulator's memory roughly 4x. On the same laptop you go from a handful of simulators to a screenful.

![19 iOS simulators running at once on a 16 GB Mac](docs/simslim-19-sims.png)

*19 iOS simulators, all under automation, on a 16 GB MacBook Pro. Stock simulators start thrashing at around 5.*

## Numbers

One simulator, booted stock and then slimmed, same device and settle time (M1 Pro, 16 GB):

| | Stock | Slim |
|---|---|---|
| Processes | 258 | 70 |
| Memory | 4.0 GB | 0.9 GB |

Memory here is phys_footprint, the figure Activity Monitor shows, which counts compressed and swapped pages. That's what decides how many simulators fit before the machine starts swapping. Run `simslim measure <udid>` to see it for any booted simulator.

## Install

```sh
brew install mobai-app/tap/simslim
```

or

```sh
go install github.com/mobai-app/simslim/cmd/simslim@latest
```

macOS only, and you need Xcode with an iOS Simulator runtime, since simslim
drives simulators through `xcrun simctl`.

## macOS app

The SwiftUI app bundles the CLI and adds:

- Searchable simulator status, disk-size, and live RAM columns.
- Searchable service profiles with per-daemon controls and purpose summaries.
- Read-only disk analysis plus confirmed cleanup of allowlisted data.
- Clone, rename, erase, delete, and Finder shortcuts.

Build it locally with Go and Xcode:

```sh
make app
open build/SimSlim.app
```

Memory estimates are guidance rather than additive savings; see the
[measurement method](docs/category-memory.md). SimSlim recommends cloning before
service or disk changes so the copy can serve as a backup.

## Usage

```sh
simslim list             # simulators and their slim status (--booted to filter)
simslim profiles         # what a slim boot turns off
simslim profiles <id>    # the daemons in one category
simslim on <udid>        # slim a simulator and reboot it slim
simslim off <udid>       # put it back to stock
simslim status <udid>    # how slim a booted simulator is
simslim verify <udid> --profile ci.json   # exact profile match; non-zero on drift
simslim doctor <udid> --requires push,storekit,universal-links
simslim measure <udid>   # a booted simulator's memory footprint
simslim top              # live fleet monitor; enter a sim for per-daemon RAM/CPU
simslim size <udid>      # total allocated simulator size
simslim disk-plan <udid> # measure reclaimable data; read-only
simslim disk-clean --categories caches,logs --confirm <udid>
simslim clone <udid> <name>
simslim rename <udid> <name>
simslim boot <udid>      # boot a simulator and wait for its services
simslim shutdown <udid>  # shut down a booted simulator
simslim erase <udid>     # erase apps, data, settings, and slimming overrides
simslim delete <udid>    # permanently delete a simulator
```

Read-only and simulator-management commands accept `--json` for integrations
and the macOS app.

### Slow CI runners

`simslim on` boots the simulator, disables ~170 daemons one `launchctl` call at a
time, then reboots — all under a single 10-minute deadline. Shared CI runners (like
GitHub-hosted macOS runners) are slower and less predictable, and can blow that
deadline mid-reconfigure with `context deadline exceeded` errors. Raise it with the
global `--boot-timeout` flag or the `SIMSLIM_BOOT_TIMEOUT` environment variable:

```sh
simslim on <udid> --boot-timeout 15m
# or, for the whole job:
export SIMSLIM_BOOT_TIMEOUT=15m
```

Each individual `launchctl` transition is also bounded by its own 2-minute
timeout, and the first transitions after a cold boot can exceed that on slow
hosts (failed ones are retried automatically). Raise it with the global
`--spawn-timeout` flag or the `SIMSLIM_SPAWN_TIMEOUT` environment variable:

```sh
simslim on <udid> --spawn-timeout 5m
# or, for the whole job:
export SIMSLIM_SPAWN_TIMEOUT=5m
```

## Disk cleanup

Disk cleanup is permanent and separate from service slimming. `disk-plan` is
read-only. `disk-clean` shuts down the exact simulator, clears only allowlisted
per-device directories, and refuses to run without `--confirm`.

```sh
simslim disk-categories
simslim disk-plan <udid>
simslim disk-clean --categories caches,logs,temporary --confirm <udid>
# Optional: also remove on-demand language models
simslim disk-clean --categories linguistic-data --confirm <udid>
```

Built-in apps and core OS language resources are part of a signed iOS runtime
shared by every simulator using that version, so simslim never modifies them.
Required Siri assets are measured only because iOS restores them on launch;
on-demand language data is opt-in and may down