<p align="center">
  <img src="assets/colibri.svg" width="500" alt="colibrì — tiny engine, immense model">
</p>

<p align="center">
  <a href="https://justvugg.github.io/colibri"><img src="https://img.shields.io/badge/website-justvugg.github.io%2Fcolibri-1f6feb" alt="Website"></a>
  <a href="https://github.com/JustVugg/colibri/releases"><img src="https://img.shields.io/github/v/release/JustVugg/colibri?color=2ea043" alt="Latest release"></a>
</p>

<p align="center">
  <a href="https://justvugg.github.io/colibri"><b>Website</b></a> ·
  English · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.it.md">Italiano</a>
</p>

**Tiny engine, immense model.** Run **GLM-5.2 (744B-parameter MoE)** on a consumer machine with ~25 GB of RAM — in pure C, with zero dependencies, by streaming experts from disk.

Colibrì is a lightweight, quality-preserving MoE runtime that treats VRAM, RAM,
and storage as one managed memory hierarchy. Insufficient fast memory may reduce
speed, but the default policy **never silently changes model precision or router
semantics**.

```
$ ./coli chat
  🐦 colibri v1.1.0 — GLM-5.2 · 744B MoE · int4 · streaming CPU
  ✓ ready in 32s · resident 9.9 GB
  › ciao!
  ◆ Ciao! 😊 Come posso aiutarti oggi?
```

## See it running

<p align="center">
  <img src="docs/media/colibri-dashboard.png" width="900" alt="colibrì web dashboard — live metrics, hardware panel, expert tiers">
</p>
<p align="center"><em>The web dashboard (<code>./coli web</code>): a 744B model at <strong>4 tok/s, TTFT 1.6 s, disk 0</strong> —
full expert residency on 6× RTX 5090, with live token metrics, the per-turn time breakdown,
the VRAM/RAM/disk tier bar and the live mini-brain in the corner.</em></p>

<p align="center">
  <img src="docs/media/colibri-brain.png" width="900" alt="the Brain page — 19,456 experts as a live cortex">
</p>
<p align="center"><em>The <strong>Brain</strong> page: all 19,456 experts as a living cortex — colour is the storage tier,
brightness is routing heat, and every expert routed in a turn flashes white. Hovering shows the expert's
<a href="https://github.com/JustVugg/colibri/issues/175">measured topic affinity</a>.</em></p>

<p align="center">
  <img src="docs/media/colibri-atlas.png" width="900" alt="the Atlas page — the measured expert atlas as a 3-D galaxy">
</p>
<p align="center"><em>The <strong>Atlas</strong> page: the <a href="https://github.com/JustVugg/colibri/issues/175">measured expert atlas</a>
as a 3-D galaxy — 13,260 characterised experts, 1,041 replicated specialists clustering by topic
(poetry, law, Chinese, SQL…). Position is measured routing affinity, not a learned embedding. Drag to spin.</em></p>

## The vision

Frontier models should not be sealed inside datacenters. colibrì exists so that
**anyone curious enough can open one up**: run a 744B-parameter mind on hardware
you already own, watch every expert fire in real time, and change the code that
does it. Not renting intelligence behind an API — *holding* it: probing it,
measuring it, improving it. Every optimisation in this project started with
someone measuring something on their own machine; the engine is deliberately
small enough that the next one can come from you.

## The idea

A 744B Mixture-of-Experts model activates only ~40B parameters per token — and
only ~11 GB of those change from token to token (the routed experts):

<p align="center">
  <img src="docs/media/sparse.png" width="880" alt="only ~5.4% of parameters are active per token">
</p>

So the model doesn't need to *fit* in fast memory — it needs to be **placed**:

- the **dense part** (attention, shared experts, embeddings — ~17B params) stays
  **resident in RAM at int4** (~9.9 GB);
- the **19,456 routed experts** (75 MoE layers × 256 + the MTP head, ~19 MB each
  at int4) live **on disk** (~370 GB) and are **streamed on demand**, with a
  per-layer LRU cache, a learned pinned hot-store, and an optional VRAM tier.

Think of the core algorithm as **a JIT, but for weights**. A compiler JIT never
compiles the whole program — it watches what actually runs and compiles the hot
paths, just in time. colibrì makes the same bet about a 744B parameter space:
parameters are not resident state to be held, they are **data to be staged**
across a heterogeneous storage hierarchy (VRAM / RAM / NVMe), exactly when the
router proves they are needed. Measured routing heat decides which experts earn
which tier, the router runs a layer ahead so prefetch hides the staging latency,
and — like a JIT — the engine learns your workload: the more you run, the hotter
the right experts get. It works because routing has measurable structure (see
the [expert atlas](https://github.com/JustVugg/colibri/issues/175)) — and
structure is cacheable.

The engine is a single C file (`c/glm.c`) plus small headers. No BLAS, no Python
at runtime, no GPU required.

## How it works

### The per-token path

<p align="center">
  <img src="docs/media/token-path.png" width="880