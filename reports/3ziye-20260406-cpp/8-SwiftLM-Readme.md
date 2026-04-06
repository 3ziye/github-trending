# ⚡️ SwiftLM

A blazingly fast, native Swift inference server that serves [MLX](https://github.com/ml-explore/mlx) models with a strict **OpenAI-compatible API**. 

No Python runtime, no Global Interpreter Lock (GIL), no unnecessary memory copies. Just bare-metal Apple Silicon performance compiled to a single binary.

<p align="center">
  <img src="docs/demo.gif" width="320" alt="SwiftLM Chat iOS demo" />
</p>

---

## 📊 Performance: Gemma 4-26B on Apple Silicon

Benchmark results for `gemma-4-26b-a4b-it-4bit` (26B MoE, 4-bit) on M5 Pro 64 GB.

### Headline Numbers

| Configuration | 512 ctx | 40K ctx | 100K ctx |
|---|---|---|---|
| **Dense/Vanilla** | 34 tok/s · 18.8 GB | 17 tok/s · 52.6 GB | 16 tok/s · 52.1 GB |
| **SSD Stream** | 4.5 tok/s · **7.7 GB** | 4.2 tok/s · 52.1 GB | 3.5 tok/s · 52.1 GB |
| **TurboQuant** | 34 tok/s · 18.6 GB | 7.0 tok/s · **35.0 GB** | 4.1 tok/s · **46.7 GB** |
| **SSD + TurboQuant** | 4.7 tok/s · **7.7 GB** | 2.1 tok/s · **22.7 GB** | 1.4 tok/s · **33.3 GB** |

> Values shown as `generation speed · GPU memory allocated`

**Key takeaways:**
- 🖥️ **8 GB Mac Mini**: SSD Stream runs a 26B model at **4.6 GB Active RAM**
- 📄 **40K context on 24 GB MacBook Pro**: SSD + TurboQuant fits in **22.7 GB**
- 📚 **100K context on 32 GB Mac Studio**: SSD + TurboQuant fits in **33.3 GB** — previously required 64 GB

> Run `./run_benchmark.sh` to generate these metrics on your own device. (See **Benchmarks & Testing** below).

---

## 🚀 Features

- 🍎 **100% Native Apple Silicon**: Powered natively by Metal and Swift. 
- 🔌 **OpenAI-compatible**: Drop-in replacement for OpenAI SDKs (`/v1/chat/completions`, streaming, etc).
- 🧠 **Smart Model Routing**: Loads HuggingFace format models directly, with native Safetensors parsing.
- ⚡️ **TurboQuantization Integrated**: Custom low-level MLX Metal primitives that apply extremely fast quantization for KV caching out-of-the-box.
- 💾 **SSD Expert Streaming**: *Experimental* zero-copy streaming that swaps Mixture of Experts (MoE) layers directly from the NVMe SSD to the GPU command buffer without trashing macOS Unified Memory (prevents Watchdog OS kernel panics on 122B+ models).
- 🎛️ **Granular Memory Control**: Integrated Layer Partitioning (`--gpu-layers`) and Wisdom Auto-Calibration for squeezing massive models into RAM.

---

## ⚡️ TurboQuantization: KV Cache Compression

`SwiftLM` implements a **hybrid V2+V3 TurboQuant architecture** for on-the-fly KV cache compression. At roughly ~3.6 bits per coordinate overall, the KV cache is compressed ~3.5× vs FP16 with near-zero accuracy loss.

### By combining V2 Speed with V3 Quality:
Recent reproductions of the TurboQuant algorithm (e.g., `turboquant-mlx`) revealed two distinct paths:
1. **V2 (Hardware-Accelerated)**: Fast, but uses linear affine quantization which degrades quality at 3-bit.
2. **V3 (Paper-Correct)**: Excellent quality using non-linear Lloyd-Max codebooks, but painfully slow due to software dequantization.

**We built the "Holy Grail" hybrid:** We ported the V3 non-linear Lloyd-Max codebooks directly into the native C++ encoding path, and process the dequantization natively in fused Metal (`bggml-metal`) shaders. This achieves **V3 quality at V2 speeds**, completely detached from Python overhead.

### The Algorithm:

**K-Cache (3-bit PolarQuant + 1-bit QJL) = 4.25 bits/dim**
1. Extract L2 norm and normalize: `x̂ = x / ‖x‖`
2. Apply Fast Walsh-Hadamard Transform (WHT) rotation to distribute outliers evenly.
3. Quantize each coordinate using **3-bit non-linear Lloyd-Max centroids**.
4. Compute the residual error between the original vector and the quantized approximation.
5. Project the residual via a random Johnson-Lindenstrauss (QJL) matrix and store the 1-bit signs.
*(Why QJL? QJL acts as an additional regularizer that prevents centroid resolution loss from degrading the attention dot-product.)*

**V-Cache (3-bit PolarQuant) = 3.125 bits/dim**
Because the V-cache matrix is not used for inner-product attention scoring, the QJL error correction provides no benefit. We cleanly disable QJL for the V-cache, extracting an additional 25% memory savings without sacrificing quality.

Reference implementations: [`turboquant-mlx`](https://github.com/sharpner/turboquant-mlx) | [`turboquant_plus`](https://github.com/TheTom/turboquant_plus) | Paper: [TurboQuant, Google 2504.19874](https://arxiv.org/abs/2504.19874)

---

## 💻 Benchmarks & Testing

### Test 1: Automated Extreme Context Benchmark
Run the automated profiling suite on your device to test generation speed and GPU memory allocation across extreme context lengths (up to 100K tokens):
```bash
./run_benchmark.sh
```
> The interactive script lets you pick a model and context sizes. Results are saved to `profiling_results_<hostname>.md` with a rich console visualization.

### Test 2: Prompt Cache & Sliding Window Regression Test
To verify the stability of the prompt cache when interleaving long contexts with sliding window attention (e.g. Gemma 4/Mist