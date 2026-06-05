<br/>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/logo-dark.svg">
    <img alt="forkd" src="docs/logo.svg" width="220">
  </picture>
</div>

<br/>
<br/>

<p align="center">
  <a href="https://github.com/deeplethe/forkd/actions"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/deeplethe/forkd/ci.yml?branch=main&style=flat-square&label=ci"></a>
  <a href="https://github.com/deeplethe/forkd/releases"><img alt="Release" src="https://img.shields.io/github/v/release/deeplethe/forkd?style=flat-square&color=4c956c"></a>
  <a href="https://pypi.org/project/forkd/"><img alt="PyPI" src="https://img.shields.io/pypi/v/forkd?style=flat-square&color=3776ab&logo=pypi&logoColor=white"></a>
  <a href="./LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-blue?style=flat-square"></a>
  <a href="./README-zh.md"><img alt="中文 README" src="https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87-red?style=flat-square"></a>
  <a href="https://github.com/deeplethe/forkd/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/deeplethe/forkd?style=flat-square&color=eab308&logo=github"></a>
</p>

<br/>

## Fork 100 microVMs in 101 ms. BRANCH a live VM in 56 ms (v0.4 live mode).

A microVM sandbox runtime for **AI agent fan-out**. Children fork
from a warmed parent snapshot, inheriting its address space
copy-on-write instead of cold-booting their own kernel.

forkd is built on Firecracker. The parent VM boots once, imports
your runtime (Python + your dependencies, a JIT-warmed JVM, an
already-loaded ML model) and is paused to disk. Each child is a
separate Firecracker process that `mmap`s the parent's memory image
with `MAP_PRIVATE`; the kernel implements copy-on-write at the page
level, so children share the parent's resident memory until they
diverge.

The result is two properties at once: per-child KVM isolation, and a
spawn cost that's closer to `fork(2)` than to a cold-boot VM.

forkd also supports **BRANCH**: pause a running sandbox, snapshot its
in-flight state, and resume — all in ~150 ms — so an agent can fork
mid-thought, not only at warm-up. v0.3.4 fixed a slow-path regression
where repeated BRANCHes on the same parent ballooned from 150 ms to
2.7 s ([#146](https://github.com/deeplethe/forkd/issues/146)); the
chain now stays flat (17.6× faster on the 6th consecutive BRANCH).

**v0.4 live BRANCH** collapses the source-pause window from ~200 ms
(Diff) to **56 ms p50 / 64 ms p90** on a 1.5 GiB source — measured
on a real BRANCH workload, [`bench/live-fork-pause-window/RESULTS-v0.4.md`](./bench/live-fork-pause-window/RESULTS-v0.4.md).
**3.6× faster pause** vs v0.3 Diff at p50, and the gap *widens* on
slower storage because Live's pause is disk-independent (memory
copy runs after resume, not during). With `wait: false` the caller
returns in ~70 ms while the background copy completes asynchronously
— a **200×** RT improvement for fire-and-forget BRANCH from agent
code. Pass `--live` / `--no-wait` on the CLI, `mode: "live"` /
`wait: false` on REST, or the same on the Python / TypeScript / MCP
SDKs.

```python
from forkd import Controller
c = Controller()
# Source must boot with live_fork=True (memfd-backed RAM, the prereq
# for UFFD_WP to see writes from the running parent).
parent = c.spawn_sandboxes("pyagent", n=1, live_fork=True)[0]
# ... drive parent ... then BRANCH live + fire-and-forget:
branch = c.branch_sandbox(parent["id"], mode="live", wait=False)
# Returns after ~10 ms with status="writing"; poll list_snapshots
# until status="ready" for the background copy to finish.
```

```bash
# CLI: spawn live-fork-capable children locally, then live-BRANCH the
# daemon-tracked one. The two paths don't compose yet — daemon-side
# spawn from the CLI is the next gap (see issue #209 for status).
sudo -E forkd fork --tag pyagent -n 1 --per-child-netns --live-fork
sudo -E forkd snapshot --from-sandbox <sb-id> --live --no-wait
```

Requires Linux ≥ 5.7, `vm.unprivileged_userfaultfd=1` (or
`CAP_SYS_PTRACE`), and the vendored Firecracker fork from
[deeplethe/firecracker:forkd-v0.4-mem-backend-shared-v1.12](https://github.com/deeplethe/firecracker/tree/forkd-v0.4-mem-backend-shared-v1.12)
— `forkd doctor` probes both. Full design:
[`DESIGN-v0.4.md`](./DESIGN-v0.4.md). Empirical PoC data:
[`experiments/v0.4-*-poc/`](./experiments/). Tracking issue
[#101](https://github.com/deeplethe/forkd/issues/101).

<br/>

## v0.5: stacking diff snapshots into a chain

Once an agent starts caching `pip install numpy`, `pip install pandas`,
`pip install scikit-learn` as separate snapshots, you want them
**stacked** — not three copies of the same 1.5 GiB base. v0.5 ships
**diff-snapshot chains**: each layer records a `parent_tag` +
content-hash edge to the layer below; the daemon walks the chain at
spawn time and assembles the memory image in one pass.

```bash
# Build a 3-layer chain off a python:3.12-slim base
forkd snapshot-diff --from py