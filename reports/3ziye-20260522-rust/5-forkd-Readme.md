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

## Fork 100 microVMs in 101 ms.

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

<br/>

## Demo: branch a thinking agent

A 24-second walkthrough of the LangGraph branch-and-fan-out demo —
source agent runs a ReAct loop, gets BRANCHed mid-thought, three
grandchildren each receive a different steering hint, all three
produce divergent itineraries while inheriting the same prior
reasoning state.

![forkd branch-and-fan-out demo](./docs/assets/demo-en.gif)

Headline divergence: the source (no hint) picks Nishiki Market for
Day 1; all three hinted children independently substitute Arashiyama
Bamboo Grove. The cost-focused child also adds "may be pricey"
annotations the others don't. **The model wasn't told to swap places**
— each hint perturbed the next LLM call, the rest of the prior
reasoning came along unchanged.

Full mechanism + numbers + raw transcripts in
[`recipes/langgraph-react/`](./recipes/langgraph-react/) and
[`recipes/langgraph-react/DEMO.md`](./recipes/langgraph-react/DEMO.md).

### And: filesystem state, not just reasoning

For the "but couldn't you just call the LLM 3 times in parallel?"
objection, see [`recipes/coding-agent-fork/`](./recipes/coding-agent-fork/) —
a 50 MiB binary blob travels byte-identically across all 4 sandboxes
through a single BRANCH. Three grandchildren each apply a different
fix to a buggy Python package; their `__pycache__/` and edits stay
isolated, but the 50 MiB inheritance is shared. Bytes can't fit in
a prompt. **3.3 s pause for the BRANCH operation.**

<br/>

## Properties

- **Hardware isolation.** Each child is its own Firecracker microVM
  backed by KVM. Escape requires a hypervisor or kernel vulnerability,
  not a `runc` regression.
- **Warmed runtimes inherit for free.** Imports, JIT compilation, model
  weights, prefetched caches — anything the parent did is already
  resident in the child.
- **Real Linux per child.** Multi-vCPU, full TCP networking, `apt
  install`, outbound HTTPS. Unlike function-level snapshot runtimes
  that trade single-vCPU + serial-I/O for raw spawn speed, forkd
  children can run real Python servers, model inference, or any
  workload that needs a full kernel.
- **Multi-tenant by construction.** Per-child network namespace, per-
  child cgroup v2 memory limit, independent `/dev/urandom` re-seeded
  by `vmgenid` (Linux 5.20+).
- **Built for agent fan-out.** AI agent workloads that fan out into
  many short-lived sandboxes — code-interpreter, tool-use, evaluation
  rollouts — are the design point. The warmed parent collapses the
  per-request `import numpy` / `import torch` cost across the entire
  cohort.
- **Operable.** Daemon process owning state, REST API on Unix or TCP,
  Prometheus `/metrics`, append-only JSON audit log, systemd unit.
- **Open source.** Apache 2.0, no vendor SDK.

<br/>

## Benchmarks

Same Linux host (Ubuntu 24.04, Linux 6.14, 20 vCPU, 30 GiB, KVM).
Workload: spawn 100 sandboxes that each run `import numpy;
numpy.zeros(5).tolist()`.

![Spawn time at N=100](./bench/chart-spawn-100.png)

![Host memory per sandbox](./bench/chart-memory-per.png)

| Backend | Wall-clock at