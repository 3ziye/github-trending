# deepseek-ocr.rs 🚀

Rust implementation of the DeepSeek-OCR inference stack with a fast CLI and an OpenAI-compatible HTTP server. The workspace packages the vision-language model, prompt tooling, and serving layer so you can build document understanding pipelines that run locally on CPU, Apple Metal, or (alpha) NVIDIA CUDA GPUs.

> 中文文档请看 [README_CN.md](README_CN.md)。  

> Want ready-made binaries? Latest macOS (Metal-enabled) and Windows bundles live in the [build-binaries workflow artifacts](https://github.com/TimmyOVO/deepseek-ocr.rs/actions/workflows/build-binaries.yml). Grab them from the newest green run.

## Inside `crates/core` 🔬

- **Vision preprocessing** – `prepare_vision_input_from_image` builds a square global canvas with letterboxing (`build_global_view`) and, when crop mode is enabled, applies `dynamic_preprocess` tiling to produce high-resolution local crops plus optional thumbnails.
- **SAM + CLIP fusion** – each view is normalised via `image_to_tensor`, pushed through the Candle ports of SAM (`SamBackbone`) and CLIP-L (`ClipVisionModel`), then flattened with `build_clip_sam_tokens` so the features stay spatially aligned.
- **Projector & layout tokens** – the custom `ImageProjector` linearly maps concatenated SAM/CLIP channels into the language hidden size while injecting learned `image_newline`/`view_separator` tokens to preserve grid structure, yielding the multimodal embeddings used during decoding.
- **Tokenizer alignment** – `build_prompt_tokens` synthesises `<image>` spans whose length exactly matches the projected token count (global + local grids), ensuring OpenAI-style prompts remain consistent even after chat history pruning.
- **Decoder & caching** – the text stack is a Candle reimplementation of DeepSeek-V2 (`DeepseekLanguageModel`) with optional FlashAttention, rotary position embeddings, and `DynamicCache` guards so both the CLI and server can stream tokens efficiently.
- **Observability & parity** – debug builds expose CLIP/SAM traces (`VisionDebugFeatures`) so we can diff intermediate tensors against the PyTorch reference; most stages are already numerically aligned, and the few remaining deltas (mainly projector normalisation + vision tiling) are tracked on the roadmap for upcoming releases.

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

## Quick Start 🏁

### Prerequisites

- Rust 1.78+ (edition 2024 support)
- Git
- Optional: Apple Silicon running macOS 13+ for Metal acceleration
- Optional: CUDA 12.2+ toolkit + driver for experimental NVIDIA GPU acceleration on Linux/Windows
- Optional: Intel oneAPI MKL for preview x86 acceleration (see below)
- (Recommended) Hugging Face account with `HF_TOKEN` when pulling from the `deepseek-ai/DeepSeek-OCR` repo (ModelScope is used automatically when it’s faster/reachable).

### Clone the Worksp