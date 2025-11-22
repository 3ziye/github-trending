# deepseek-ocr.rs 🚀

Rust implementation of the DeepSeek-OCR inference stack with a fast CLI and an OpenAI-compatible HTTP server. The workspace packages multiple OCR backends, prompt tooling, and a serving layer so you can build document understanding pipelines that run locally on CPU, Apple Metal, or (alpha) NVIDIA CUDA GPUs.

> 中文文档请看 [README_CN.md](README_CN.md)。  

> Want ready-made binaries? Latest macOS (Metal-enabled) and Windows bundles live in the [build-binaries workflow artifacts](https://github.com/TimmyOVO/deepseek-ocr.rs/actions/workflows/build-binaries.yml). Grab them from the newest green run.

## Choosing a Model 🔬

| Model | Memory footprint* | Best on | When to pick it |
| --- | --- | --- | --- |
| **DeepSeek‑OCR** | **≈6.3GB** FP16 weights, **≈13GB** RAM/VRAM with cache & activations (512-token budget) | Apple Silicon + Metal (FP16), high-VRAM NVIDIA GPUs, 32GB+ RAM desktops | Highest accuracy, SAM+CLIP global/local context, MoE DeepSeek‑V2 decoder (3B params, ~570M active per token). Use when latency is secondary to quality. |
| **PaddleOCR‑VL** | **≈4.7GB** FP16 weights, **≈9GB** RAM/VRAM with cache & activations | 16GB laptops, CPU-only boxes, mid-range GPUs | Dense 0.9B Ernie decoder with SigLIP vision tower. Faster startup, lower memory, great for batch jobs or lightweight deployments. |
| **DotsOCR** | **≈9GB** FP16 weights, but expect **30–50GB** RAM/VRAM for high-res docs due to huge vision tokens | Apple Silicon + Metal BF16, ≥24GB CUDA cards, or 64GB RAM CPU workstations | Unified VLM (DotsVision + Qwen2) that nails layout, reading order, grounding, and multilingual math if you can tolerate the latency and memory bill. |

\*Measured from the default FP16 safetensors. Runtime footprint varies with sequence length.

Guidance:

- **Need maximum fidelity, multi-region reasoning, or already have 16–24GB VRAM?** Use **DeepSeek‑OCR**. The hybrid SAM+CLIP tower plus DeepSeek‑V2 MoE decoder handles complex layouts best, but expect higher memory/latency.
- **Deploying to CPU-only nodes, 16GB laptops, or latency-sensitive services?** Choose **PaddleOCR‑VL**. Its dense Ernie decoder (18 layers, hidden 1024) activates fewer parameters per token and keeps memory under 10GB while staying close in quality on most docs.
- **Chasing reading-order accuracy, layout grounding, or multi-page multilingual PDFs on roomy hardware?** Pick **DotsOCR** with BF16 on Metal/CUDA. Prefill runs around 40–50 tok/s on M-series GPUs but can fall to ~12 tok/s on CPU because of the heavy vision tower.

## Why Rust? 💡

The original DeepSeek-OCR ships as a Python + Transformers stack—powerful, but hefty to deploy and awkward to embed. Rewriting the pipeline in Rust gives us:

- Smaller deployable artifacts with zero Python runtime or conda baggage.
- Memory-safe, thread-friendly infrastructure that blends into native Rust backends.
- Unified tooling (CLI + server) running on Candle + Rocket without the Python GIL overhead.
- Drop-in compatibility with OpenAI-style clients while tuned for single-turn OCR prompts.

## Technical Stack ⚙️

- **Candle** for tensor compute, with Metal and CUDA backends and FlashAttention support.
- **Rocket** + async streaming for OpenAI-compatible `/v1/responses` and `/v1/chat/completions`.
- **tokenizers** (upstream DeepSeek release) wrapped by `crates/assets` for deterministic caching via Hugging Face and ModelScope mirrors.
- **Pure Rust vision/prompt pipeline** shared by CLI and server to avoid duplicated logic.

## Advantages over the Python Release 🥷

- Faster cold-start on Apple Silicon, lower RSS, and native binary distribution.
- Deterministic dual-source (Hugging Face + ModelScope) asset download + verification built into the workspace.
- Automatic single-turn chat compaction so OCR outputs stay stable even when clients send history.
- Ready-to-use OpenAI compatibility for tools like Open WebUI without adapters.

## Highlights ✨

- **One repo, two entrypoints** – a batteries-included CLI for batch jobs and a Rocket-based server that speaks `/v1/responses` and `/v1/chat/completions`.
- **Works out of the box** – pulls model weights, configs, and tokenizer from whichever of Hugging Face or ModelScope responds fastest on first run.
- **Optimised for Apple Silicon** – optional Metal backend with FP16 execution for real-time OCR on laptops.
- **CUDA (alpha)** – experimental support via `--features cuda` + `--device cuda --dtype f16`; expect rough edges while we finish kernel coverage.
- **Intel MKL (preview)** – faster BLAS on x86 via `--features mkl` (install Intel oneMKL beforehand).
- **OpenAI client compatibility** – drop-in replacement for popular SDKs; the server automatically collapses chat history to the latest user turn for OCR-friendly prompts.

## Model Matrix 📦

The workspace exposes three base model IDs plus DSQ-quantized variants for DeepSeek‑OCR, PaddleOCR‑VL, and DotsOCR:

| Model ID | Base Model | Precision | Suggested Use Case |
| --- | --- | --- | --- |
| `deepsee