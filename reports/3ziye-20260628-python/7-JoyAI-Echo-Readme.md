<p align="center">
  <img src="assets/image.png" alt="JoyAI-Echo generated video gallery" width="100%">
</p>

<div align="center">

<h1>JoyAI-Echo</h1>

<p><strong>🎬 Pushing the Frontier of Long Video Generation</strong></p>

<p>Standalone, inference-only release for <strong>minute-level multi-shot audio-video generation</strong> with a distilled DMD generator, paired cross-modal memory, and story-level consistency.</p>

<p>
  <a href="https://www.researchgate.net/publication/405770309_JoyAI-Echo_Pushing_the_Frontier_of_Long_Audio-Visual_Generation"><b>📄 Paper</b></a> |
  <a href="https://echo-team-joy-future-academy-jd.github.io/Echo-LongVideo-Page/"><b>🌐 Project Page</b></a> |
  <a href="#quickstart"><b>🚀 Quickstart</b></a> |
  <a href="https://huggingface.co/jdopensource/JoyAI-Echo"><b>🤗 Hugging Face</b></a> |
  <a href="#results"><b>📊 Results</b></a> |
  <a href="https://github.com/zhuang2002/ComfyUI_JoyAI_Echo"><b>🖥️ ComfyUI</b></a> |
  <a href="#citation"><b>📝 Citation</b></a>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.11">
  <img src="https://img.shields.io/badge/PyTorch-2.8-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch 2.8">
  <img src="https://img.shields.io/badge/CUDA-12.8-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="CUDA 12.8">
  <img src="https://img.shields.io/badge/Release-Inference--Only-black?style=flat-square" alt="Inference">
  <img src="https://img.shields.io/badge/Long%20Video-5%20min-d61f2c?style=flat-square" alt="5 minute long video">
</p>

</div>

## Abstract

Long video generation still suffers from error accumulation, weak temporal coherence, and prohibitive latency, limiting its applicability to interactive scenarios. We present **JoyAI-Echo**, a framework that breaks these barriers through four key advances.
Central to its performance, a cross-modal audio-visual memory bank preserves character appearance and voice timbre consistently over five-minute videos, while a post-training pipeline combines memory-based reinforcement learning with distribution matching distillation for a **7.5× speedup** to substantially boost visual quality and alignment.
Empowered by these two components, **JoyAI-Echo** decisively outperforms *HappyOyster* (directing mode) on long-form generation and even surpasses the short-video specialist *Wan 2.6* on human-centric tasks.
Beyond raw generation quality, an interactive agent enables real-time user editing through conversational instructions, and a lightweight super-resolution module maintains high definition under streaming latency, further elevating the overall experience and delivering instantly editable, conversation-speed video creation.
For the first time, **JoyAI-Echo** simultaneously achieves long-range cross-modal consistency, real-time inference for minute-long video, conversational interactivity, and high-resolution output — without compromise, inaugurating a new era of interactive video generation.
Codes and weights will be open-sourced.

## Highlights

- 🎞️ **Minute-level multi-shot stories**: generate a sequence of coherent shots from one prompt JSON.
- ⚡ **DMD-distilled few-step inference**: ~7.5x faster than the original pipeline.
- 🔊 **Joint audio-video generation**: one pipeline produces synchronized video and audio.
- 🧠 **Paired cross-modal memory bank**: conditions each new shot on prior visual identity and voice context for story-level consistency.


## ComfyUI Integration

Recommended ComfyUI node package: **[ComfyUI_JoyAI_Echo](https://github.com/zhuang2002/ComfyUI_JoyAI_Echo)** — faithful to the official inference pipeline with full bf16 precision (no GGUF quantization), per-shot editable prompts with instant video preview, 3-phase GPU memory hot-swap (48GB VRAM), built-in LLM prompt enhancement, and cross-shot memory chaining for story-level consistency.

## Current Release Scope

JoyAI-Echo currently focuses on **text-to-video (T2V)** and **multi-shot long-video generation with paired audio-video memory**. The memory used in our official pipeline is built from generated T2V shots.

Please note that **image-to-video (I2V)** is **not supported in the current release**.

We are actively working on I2V support and plan to release it in a future version.

## Demo Gallery

Explore long-form and short-form JoyAI-Echo cases on the [Project Page](https://echo-team-joy-future-academy-jd.github.io/Echo-LongVideo-Page/). 🍿

## Results

### Reported Scale

| Item | Value |
| --- | ---: |
| 🎬 Long-form coherent story length | **5 min** |
| ⚡ Generation speedup over the original multi-step pipeline | **7.5x** |
| 📚 Benchmark stories | **100** |
| 🎞️ Generated evaluation shots | **3,000** |
| 🕒 Frames per shot | **241 @ 25 fps** |

### Human Evaluation

GSB user study on long- and short-video generation. The numbers denote the percentage of user preferences.

| Aspect<br>(Long Video) | JoyAI-Echo | Tie | HappyOyster<br> (Di