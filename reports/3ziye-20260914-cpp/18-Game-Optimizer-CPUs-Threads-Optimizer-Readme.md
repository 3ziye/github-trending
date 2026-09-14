# Game Optimizer

**CPU threads optimizer.**

![Game Optimizer in use](video/gameoptimizer.gif)

Per-game CPU Set isolation for split-topology CPUs — the isolation of BIOS "Turbo Game Mode",
applied only to the game you chose, and only while it is running.

Please turn off
- Turbo Game Mode, optimize CCD Parking services in BIOS.
- Game Mode and AMD's 3D V-Cache optimizer in OS.

On a dual-CCD AMD part (7950X3D, 7900X3D, 9950X3D) one CCD carries 3D V-Cache and the other
clocks higher. Some games run better pinned to the cache CCD with nothing else on it. The
existing ways to arrange that — a BIOS game mode, or letting Windows and AMD's driver decide —
are session-wide: they cost you half the machine for Discord, OBS, browsers and compilers too.

Game Optimizer applies the isolation to one process tree, keeps the other CCD free for everything
else, and clears every mask the moment the game exits.

- **CPU Sets only.** `SetProcessDefaultCpuSets`, never `SetProcessAffinityMask`.
- **Child processes included.** A worker spawned twenty minutes into a session is picked up
  within one poll period. This is not optional — CPU sets are *not* inherited by children.
- **Nothing global by default.** No CCD parking, no system policy, no driver, no reboot. The one
  exception is opt-in: the AMD 3D V-Cache setting described below, which changes a driver's start
  type and needs a restart.
- **No injection, no overlay.** One native exe, no .NET runtime. Nothing needs elevation except
  the optional AMD 3D V-Cache setting, which asks for it once.
- **Local config only.** No account, no telemetry, and the app itself makes no network
  requests.
- **One optional runtime dependency: WebView2.** It renders the sponsor strip at the
  bottom of the Settings window and nothing else. If it is absent the strip is drawn
  with GDI instead and nothing else changes — the app always starts. It is never
  touched while the app sits in the tray. See `NOTICE.md` and the file table below.

**Runs on:** Windows 10 or 11, x64. The manifest declares no older Windows, and there is no
32-bit or ARM build.

## Which CPUs this helps

The app works this out for itself. On first run it asks Windows for the machine's core and cache
layout, classifies it, and tells you on screen which of the cases below you are in, along with a
confidence level and a map of which logical processors are in each group. There is no list of CPU
models anywhere in the app — the decision comes from what Windows reports, so nothing here goes
stale. Run it and read the first-run screen; that answer is authoritative for your machine and this
table is only a guide. The first matching row wins, so a machine reporting more than one core type
is classified by core type and never by cache size.

| What Windows reports | Shown as | Masks you get | How much it helps |
|---|---|---|---|
| More than one distinct efficiency class | Intel hybrid (P/E cores) | `P-cores`, `E-cores`, `All`, plus `no SMT` variants where they differ | A real split. Game on P-cores, background apps on E-cores. High confidence |
| Two or more last-level-cache domains, sizes differ | AMD asymmetric cache (X3D) | `Cache`, `Freq`, `Freq 2`, …, `All` | A real split. Game on the largest-L3 domain, background apps on the rest. High confidence |
| Two or more last-level-cache domains, same size | Multi-CCD symmetric | `CCD0`, `CCD1`, …, `All` | A real split, but which domain gets called `CCD0` is an ordering choice, not a measurement. Medium confidence — check the core map |
| Exactly one last-level-cache domain | Single cache domain | `All`, and `All no SMT` if the CPU has SMT | Very little. There is no second group to move background work onto |
| No cache domains reported at all | Unknown | the same as a single domain | Very little, and the first-run screen says so |

Most CPUs are a single cache domain, and on those this app can only give the game one thread per
physical core. That is the whole of it — no isolated cores, no background separation. If the CPU has
no SMT either, `All no SMT` is not offered at all, both defaults fall back to `All` — every
processor — and the app changes nothing on that machine.

The multi-domain cases are the ones worth installing for: parts such as AMD's dual-chiplet X3D
desktop processors, where 3D V-Cache sits on one chiplet only, and Intel's hybrid parts with both
performance and efficient cores. Those are examples rather than a specification — a single-chiplet
X3D part is one cache domain, some chips in Intel's hybrid generations ship with no efficient cores
at all, and a dual-chiplet part with V-Cache on both chiplets reports two equal domains and lands in
the symmetric row instead. The group names borrow vendor vocabulary but the tests do not: no branch
anywhere checks who made the CPU, so any processor Windows reports with two efficiency classes is
shown under the Intel name whoever built it.

If Windows cannot describe the topology at all, the app says so at startup and gover