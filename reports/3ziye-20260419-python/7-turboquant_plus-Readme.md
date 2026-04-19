# TurboQuant+

> ### [Getting Started Guide](docs/getting-started.md) | [Configuration Recommendations](docs/turboquant-recommendations.md) | [llama.cpp Fork](https://github.com/TheTom/llama-cpp-turboquant) | [Swift MLX Fork](https://github.com/ekryski/mlx-swift-lm)

> **🍎 On Apple Silicon and want the fastest path?** Use [ekryski/mlx-swift-lm](https://github.com/ekryski/mlx-swift-lm) — Eric Kryski's Swift MLX implementation that I've been actively collaborating on. Native Swift, ~2.5x faster decode than Python mlx-lm, full TurboQuant+ support including turbo4v2 (4-bit K + 2-bit V). 144 tok/s on Qwen3.5-35B-A3B MoE at 4K on M5 Max. This llama.cpp repo is for cross-platform deployment (CUDA, ROCm, CPU, Metal).

Implementation of [TurboQuant](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) (ICLR 2026) with implementation work, experiments, and follow-on findings beyond the base paper. KV cache compression for local LLM inference.

## Note

This repository is an experimental integration and research workspace for TurboQuant-related work targeting `llama.cpp`. The goal is to make it easier to compare approaches, collect reproducible benchmark and quality data, and share implementation details across hardware and backends. It is not intended as a separate long-term fork or a proposal to merge the branch as a whole.

If individual pieces prove useful and stable, the intent is to upstream them incrementally as small, reviewable patches in line with `llama.cpp`'s normal contribution process.

## What's In This Branch

- Experimental TurboQuant-related integrations for `llama.cpp`
- Benchmark and quality validation across models, contexts, and hardware
- Backend-specific implementation work and performance experiments
- Documentation and writeups intended to make testing and reproduction easier
- Candidate ideas that may be worth upstreaming individually if they prove stable

## Current Findings

Three follow-on findings in this branch have been independently validated by multiple researchers across different hardware and backends:

1. **V compression is free.** Compressing the value cache (even down to 2 bits) has zero measurable effect on attention quality when key precision is maintained. Confirmed on Metal (M5 Max), CUDA RTX 4090 (@sztlink), and CUDA RTX 3090 (@HyperionMS2040). See [asymmetric K/V paper](docs/papers/asymmetric-kv-compression.md).
2. **All quality degradation comes from K compression.** This is why asymmetric configs (q8_0-K + turbo-V) rescue models where symmetric fails. Validated across Qwen, Llama, Mistral, and Command-R+ families. See [M5 Max stress test](docs/papers/m5-max-stress-test.md).
3. **Boundary layers are disproportionately sensitive.** Protecting the first 2 + last 2 layers at higher precision recovers 37-91% of the quality gap. See [Boundary V paper](docs/papers/layer-aware-v-compression.md).

Additional experiments and writeups: [Sparse V dequant](docs/papers/sparse-v-dequant.md) (+22.8% decode), [block size optimization](docs/papers/block-size-experiment.md) (5.12x compression), [turbo4 resurrection](docs/papers/turbo4-resurrection.md) (QJL hurts, PolarQuant works).

Compresses transformer KV cache **3.8-6.4x** using PolarQuant + Walsh-Hadamard rotation. Near q8_0 prefill speed and ~0.9x decode throughput at long context (Apple Silicon). Full format family: turbo2 (2-bit, 6.4x), turbo3 (3-bit, 4.6-5.1x), turbo4 (4-bit, 3.8x). turbo3 compression depends on storage block size; see [block size study](docs/papers/block-size-experiment.md).

**Sparse V:** Attention-gated KV cache decoding that skips low-weight V positions during inference. Up to +22.8% decode speed at 32K context, validated on wikitext-103 (50 chunks, CI +/-0.021) with no measurable PPL change. Not TurboQuant-specific; validated across q8_0, q4_0, and turbo3 KV formats. ~1% perplexity increase vs q8_0 from compression; Sparse V itself introduces no additional degradation (ON/OFF delta = 0.000).

Validated end-to-end from 1.5B to **104B** on M5 Max via llama.cpp Metal. **104B at 128K context on a MacBook** with turbo3 (PPL 4.024, 74 GB peak memory).

## Status: v1 Complete, Speed Optimized, Community-Tested

- 511+ Python tests, 100% code coverage on diagnostics
- C port integrated into llama.cpp with Metal GPU kernels
- `--cache-type-k turbo3 --cache-type-v turbo3` works on Apple Silicon (turbo2/turbo3/turbo4 all supported)
- **turbo2 Metal support**: 2-bit, 6.4x compression, +6.48% PPL — for extreme memory pressure or asymmetric K/V
- **q8_0 prefill speed parity achieved** (2747 vs 2694 tok/s)
- **Norm correction**: PPL beats q8_0 on CUDA (-1.17%), +1.1% on Metal (ported from @spiritbuun)
- **4-mag LUT**: auto-detected on M1/M2/M3/M4, +38-45% decode at long context
- **Layer-adaptive mode 2**: q8_0 quality at 3.5x compression (last 8 layers at q8_0)
- **Temporal decay**: 30-34% memory savings at long context (experiment branch)
- **NIAH retrieval**: 9/9 single needle with 