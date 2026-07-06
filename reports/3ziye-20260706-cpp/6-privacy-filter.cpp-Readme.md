# privacy-filter.cpp

Minimal [GGML](https://github.com/ggml-org/ggml) inference engine for the
`openai-privacy-filter` token-classification model family
([openai/privacy-filter](https://huggingface.co/openai/privacy-filter),
[OpenMed/privacy-filter-multilingual](https://huggingface.co/OpenMed/privacy-filter-multilingual),
[OpenMed/privacy-filter-nemotron](https://huggingface.co/OpenMed/privacy-filter-nemotron)):
PII/NER entity spans with exact UTF-8 byte offsets. Stock upstream ggml — no
patches; the model's YaRN `truncate=false` frequencies are computed at load
time and fed to `ggml_rope_ext` as `freq_factors`.

Pre-converted GGUFs (arch `openai-privacy-filter`):
[`LocalAI-io/privacy-filter-multilingual-GGUF`](https://huggingface.co/LocalAI-io/privacy-filter-multilingual-GGUF),
[`LocalAI-io/privacy-filter-GGUF`](https://huggingface.co/LocalAI-io/privacy-filter-GGUF),
and [`LocalAI-io/privacy-filter-nemotron-GGUF`](https://huggingface.co/LocalAI-io/privacy-filter-nemotron-GGUF).
Convert your own from a HF checkpoint with
[`scripts/convert.py`](scripts/convert.py) — self-contained, no llama.cpp
dependency (see [Convert](#convert)).

## Bench

A "redaction race" against stock HF Transformers on the same hardware:

**CPU — 8k-token document, real time.** Both finish; ours is 7.7× faster.

![CPU redaction race: privacy-filter.cpp vs HF Transformers on an 8k-token document](demo/out/pii_duel_cpu.gif)

**GPU — 132k-token document (4× slow-mo).** Ours runs flat to 131k tokens; HF
hits the 16 GiB memory wall and OOMs at ~16k.

![GPU redaction race: privacy-filter.cpp runs to 131k tokens while HF OOMs](demo/out/pii_duel_gpu.gif)

Full-quality MP4s: [CPU](demo/out/pii_duel_cpu_final.mp4) · [GPU](demo/out/pii_duel_gpu_final.mp4).

**Raspberry Pi 5 — on-device, real time.** The same engine, no GPU: 1,360 tokens
of mixed PII classified in 3.8 s (360 tok/s) on a Cortex-A76 @ 1.5 GHz with q8
weights. The right pane is the live NER feed — 107 spans across 22 categories,
each with its category and byte range (q8 output is span-for-span identical to
f16 here).

![Raspberry Pi 5 on-device PII scan: 1,360 tokens, 107 PII spans across 22 categories in 3.8 s](demo/out/pii_scan.gif)

Full-quality MP4: [Pi 5 scan](demo/out/pii_scan_final.mp4).

Single forward-pass latency and throughput vs stock HF Transformers (transformers
5.9, eager), Ryzen 9 7900 (12 threads) + RTX 5070 Ti, f16/fp16, matched token
counts ([scripts/bench_torch.py](scripts/bench_torch.py)). `tokens` is the input
sequence length classified in one forward pass (the whole document at once, not
generation); latency is `tokens ÷ tok/s`.

GPU — ours (Vulkan) vs HF (CUDA):

| tokens | HF (tok/s) | HF (ms) | ours (tok/s) | ours (ms) | speedup |
|-------:|-----------:|--------:|-------------:|----------:|--------:|
|    512 |      5 526 |      93 |      100 503 |         5 |     18× |
|  2 048 |     16 427 |     125 |      145 481 |        14 |    8.9× |
|  8 192 |     14 154 |     579 |      105 034 |        78 |    7.4× |
| 32 768 |        OOM |     OOM |       83 519 |       392 |       — |
| 131072 |        OOM |     OOM |       81 105 |     1 616 |       — |

CPU — ours vs HF (fp32):

| tokens | HF (tok/s) | HF (s) | ours (tok/s) | ours (s) | speedup |
|-------:|-----------:|-------:|-------------:|---------:|--------:|
|    512 |      2 171 |   0.24 |        3 564 |     0.14 |    1.6× |
|  2 048 |        978 |   2.09 |        3 490 |     0.59 |    3.6× |
|  8 192 |        304 |  26.95 |        2 332 |     3.51 |    7.7× |

The speedup widens with length because HF's full self-attention is O(n²) while
ours is banded/near-linear, so our tok/s stays roughly flat as HF's collapses.
Memory is flat ~2.8 GiB VRAM on a 16
GiB GPU. `release-portable` runtime-dispatches the best ggml-cpu ISA (AVX-512
without `-march=native`); flash + banded attention default on. See
[docs/cpu-perf.md](docs/cpu-perf.md).

Reproduce the numbers:

```sh
cmake --preset release-portable && cmake --build --preset release-portable -j
build/release-portable/bin/pf-bench model.gguf [cpu|vulkan] [iters] [lengths]
```

## Build

```sh
git clone --recursive <repo>
cmake --preset release && cmake --build --preset release -j
```

Presets: `release`, `debug` (ASan+UBSan), `profile`, `fuzz` (clang libFuzzer).
GPU backends layer onto any preset:
- Vulkan: `-DPF_VULKAN=ON` (needs Vulkan headers/loader + glslc).
- CUDA: `-DPF_CUDA=ON` (needs the CUDA toolkit). ggml picks sensible
  `CMAKE_CUDA_ARCHITECTURES`; for a bleeding-edge GPU whose features ptxas
  rejects under the generic arch (e.g. Blackwell sm_120 → `sm_120a`), pass
  `-DCMAKE_CUDA_ARCHITECTURES=120a`.

## Run

```sh
build/release/pf-cli --info model.gguf
echo "Contact John Doe at jdoe@example.com" | \
  build/release/pf-cli --classify model.gguf 0.5       # [cpu|cuda|vulkan]
```

## Convert

Pre-converted GGUFs are linked above. To convert an `OpenAIPrivacyFilter` HF
checkpoint yourself:

```sh
pip install -r scripts/requirements.txt   # torch + s