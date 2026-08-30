<h1 align="center">JoyAI-Video-Edit</h1>
<h3 align="center">Real-Time Open-Ended Video Editing with Autoregressive Diffusion</h3>

<p align="center">
  <a href="https://arxiv.org/abs/2608.03974"><img src="https://img.shields.io/badge/Paper-arXiv-red" alt="Paper"></a>
  <a href="https://huggingface.co/jdopensource/JoyAI-Video-Edit"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Checkpoint-JoyAI--Video--Edit-yellow" alt="Hugging Face"></a>
  <a href="https://huggingface.co/spaces/wxDai/joyai-video-edit"><img src="https://img.shields.io/badge/%F0%9F%9A%80%20Demo-Streaming--V2V-orange" alt="Demo"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License"></a>
</p>

<p align="center">
  <img src="assets/teaser.jpg" width="96%" alt="JoyAI-Video-Edit teaser">
</p>

JoyAI-Video-Edit is a real-time, instruction-guided video editing system for open-ended video streams. Given a live camera stream or uploaded video and a natural-language edit instruction, it edits frames causally as they arrive, without waiting for the full video, requiring a predefined video length, or revisiting future frames. In our deployment benchmark, the full end-to-end pipeline reaches 30 FPS at 720 × 1248, pushing video editing from offline batch processing toward interactive streaming generation.

The system combines an MLLM-based condition encoder, a causal video VAE, and a 16B-parameter multimodal diffusion transformer. It is trained and deployed as an autoregressive diffusion editor, then accelerated with aligned autoregressive distribution matching distillation, long-horizon optimization, bounded KV-state inference, and deployment-oriented scheduling to sustain high-throughput 720p editing while reducing train-inference mismatch and accumulated temporal drift.

## 🔥🔥🔥 News!!

- 2026.08.24: 🎉 Consumer GPU support landed — real-time streaming video editing on a single GeForce RTX 5090 (32 GB): 840 × 480 @ 24 FPS. **[Deployment Guide](DEPLOYMENT.md)**
- 2026.08.15: 🎉 Live demo released — real-time streaming video editing on a single RTX PRO 6000 (Blackwell) GPU: 840 × 480 @ 24 FPS or 720p @ 16 FPS. **[Try HuggingFace Demo](https://huggingface.co/spaces/wxDai/joyai-video-edit)**
- 2026.08.14: 🎉 Released an upgraded checkpoint with significantly stronger reference-image-guided video editing (RV2V), delivering better subject and identity preservation, more faithful reference conditioning, and improved temporal consistency across long streams. Grab the new **[DiT weights](https://huggingface.co/jdopensource/JoyAI-Video-Edit/blob/main/dit/joyai_video_edit_dit_0811.pth)**.
- 2026.08.05: 🎉 We release the deployment code, [technical report](https://arxiv.org/abs/2608.03974), and JoyAI-Video-Edit checkpoints. Please check the links above for details.

## 💎 Highlights

- **Real-time open-ended editing.** Edits live or uploaded videos as frames arrive, without requiring the full sequence upfront.
- **Diverse instruction control.** Supports subject edits, local edits, background changes, style transfer, motion changes, and reference-guided editing.
- **Autoregressive diffusion design.** Combines an MLLM condition encoder, causal video VAE, and MMDiT backbone for streaming video editing.
- **High-throughput 720p deployment.** Reaches 30 FPS end-to-end throughput at 720 × 1248 with bounded KV-state inference and stable per-chunk compute.

## 🕹️ Live Demo

Point your webcam at yourself, type an instruction, and watch the edit stream back in real time — try it in the browser: **[Hugging Face Demo](https://huggingface.co/spaces/wxDai/joyai-video-edit)**. The screenshots below are captured live from it (left: camera source, right: streamed result).

<p align="center">
  <img src="assets/live_demo/live_cartoon_group.jpg" width="96%" alt="Live demo — turn all people into cartoon style">
</p>

<table>
  <tr>
    <td><img src="assets/live_demo/live_optimus_prime.jpg" alt="Live demo — transform into Optimus Prime with background unchanged"></td>
    <td><img src="assets/live_demo/live_gundam.jpg" alt="Live demo — transform into a Gundam via reference-guided editing"></td>
  </tr>
  <tr>
    <td><img src="assets/live_demo/live_hanfu_palace.jpg" alt="Live demo — Ming-style gown outfit change with ancient palace background"></td>
    <td><img src="assets/live_demo/live_cel_anime.jpg" alt="Live demo — add cap and sunglasses, convert to hand-drawn cel animation"></td>
  </tr>
</table>

## 🚧 TODO

- [x] **Stronger model version in progress.** A more powerful version is under active development, with a particular focus on advancing reference-image-guided video editing (RV2V) capabilities.
- [x] **Consumer GPU support.** Optimize deployment for consumer-grade GPUs such as GeForce RTX 5090.
- [ ] **Diffusers support.** Provide a 🤗 Diffusers pipeline for JoyAI-Video-Edit to streamline loading and inference.
- [ ] **LongV2VBench release.** Release LongV2VBench for long-form video-to-video editing evaluation.
- [ ] **Rele