<div align="center">

```
	____       _ _         __ _
	|  _ \  ___| | |_ __ _ / _(_)_ __
	| | | |/ _ \ | __/ _` | |_| | '_ \
	| |_| |  __/ | || (_| |  _| | | | |
	|____/ \___|_|\__\__,_|_| |_|_| |_|
```

## Run the *full, never-pruned*, 2.8-trillion-parameter [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) on consumer hardware, as "fast" as possible

</div>

Deltafin is a single native binary that runs full Kimi K3. Nothing pruned. Nothing skipped. K3 decides every token.

All 16 experts, every single token. No shortcuts, no "close enough." It's exactly what Moonshot shipped.

The quality rule is simple: **K3 itself decides every token**, and nobody else. Small draft models are allowed to guess ahead (that's where much of the speed comes from), but K3 checks every guess, and nothing reaches you without its official sign-off.

### Latest Benchmarks on an M1 Max laptop

* 0.2901 token/s (3.447 s/token) — 1.9% higher throughput than last update

#### Historical M1 benchmarks:

* 0.2847 token/s (August 2, 2026) — 7.0% higher throughput
* 0.2660 token/s (July 30, 2026) — 102.9% higher throughput
* 0.1311 token/s (July 28, 2026) — 829.8% higher throughput
* 0.0141 token/s (July 27, 2026)


<div align="center">

![model](https://img.shields.io/badge/model-Kimi_K3_·_2.8T_MoE-blueviolet)
![platforms](https://img.shields.io/badge/platforms-macOS_arm64_·_Linux_x86--64%2Faarch64-informational)
![accelerators](https://img.shields.io/badge/accelerators-MPS%2FMetal_·_CUDA_·_CPU-9cf)
![experts](https://img.shields.io/badge/routing-all_16_experts-teal)
![runtime](https://img.shields.io/badge/runtime-one_compiled_binary-brightgreen)
![license](https://img.shields.io/badge/license-MIT-blue)

</div>

---

## Mission Statement

**Pure raw uncut K3 quality, as fast as possible.** Speed must *never come from reducing model quality*. Deltafin keeps all 16 routed experts and the full K3 target as the sole authority for every single token.

Our goal is to squeeze out every last drop of efficiency possible when running a huge model like K3, with all options on the table... *except for reducing quality*.

---

## But Why?!?
Deltafin is not a product pitch. It is an experiment in how far consumer hardware can be pushed, and what we can learn by attempting something so challenging.

Kimi K3 targets infrastructure on the scale of 16 nodes and roughly 4.8 TB of aggregate VRAM. That means the full 2.8T parameters and the 1M-token context window, with the expert bank never pruned. On any home setup, this is an extreme constraint. Every 1% improvement is very hard-won. But each gain can teach something.

**Research and exploration is the point.** *That* is our mission. Not everything has to be a "minimum viable product" to impress venture capitalists. If Deltafin helps make frontier models usable on a $15,000 home setup, instead of a [$2,000,000 infrastructure](https://www.thundercompute.com/blog/nvidia-h200-pricing) like Kimi recommends, we believe that is worthwhile progress on our self-hosted AI journey. Plus everything learned along the way could even benefit other projects in unexpected ways.

> “We choose to run the full 2.8-trillion-parameter model locally, and do the other things, not because they are easy, but because they are hard.”
> — John F. Kennedy probably

Other projects appear to run full K3, somehow faster. But look closer: they've re-encoded K3's expert bank down to ~3 bits. Clever engineering toward a different goal: the smallest K3 that fits and is "close enough." Those weights are no longer the ones Moonshot released, and nobody, including them, has measured what those compromises cost.

Deltafin is the other experiment: every expert byte exactly as Moonshot shipped it, made as fast as physics allows.

---

## 1. New Installation

Deltafin installs almost everything it needs. See [Requirements](docs/REQUIREMENTS.md) if you're missing anything.

```bash
# 1. Get it
git clone https://github.com/gavamedia/deltafin.git
cd deltafin

# 2. Build it
cargo build --locked --release

# 3. Download the FULL 1.7 TB K3 model to disk (optional, but fastest)
./target/release/deltafin setup --full
```

Or, if you don't have enough disk space:
```bash
# 3. Stream K3 as you use it (slower, but 215 GB to start) 
./target/release/deltafin setup --stream
```

`setup --stream` installs the resident model and fetches exact experts on-demand only, initially running far more slowly when routes have no local cache yet. As you build up your cache over time, this can be a way to save space, storing only the parts of the model you use, running entirely off cache on disk.

#### Default DSpark (and optional Qwen)

The normal setup includes [Inferact's Kimi-K3-DSpark](https://huggingface.co/Inferact/Kimi-K3-DSpark). It takes **6.635 GiB on disk** and approximately **4.49 GiB** when admitted at runtime. Deltafin avoids materializing DSpark's redundant copy of K3's embedding. Chat and server requests use DSpark automatically when beneficial; any fa