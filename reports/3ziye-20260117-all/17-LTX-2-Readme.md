# LTX-2

[![Website](https://img.shields.io/badge/Website-LTX-181717?logo=google-chrome)](https://ltx.io)
[![Model](https://img.shields.io/badge/HuggingFace-Model-orange?logo=huggingface)](https://huggingface.co/Lightricks/LTX-2)
[![Demo](https://img.shields.io/badge/Demo-Try%20Now-brightgreen?logo=vercel)](https://app.ltx.studio/ltx-2-playground/i2v)
[![Paper](https://img.shields.io/badge/Paper-PDF-EC1C24?logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/abs/2601.03233)
[![Discord](https://img.shields.io/badge/Join-Discord-5865F2?logo=discord)](https://discord.gg/ltxplatform)

**LTX-2** is the first DiT-based audio-video foundation model that contains all core capabilities of modern video generation in one model: synchronized audio and video, high fidelity, multiple performance modes, production-ready outputs, API access, and open access.

<div align="center">
  <video src="https://github.com/user-attachments/assets/4414adc0-086c-43de-b367-9362eeb20228" width="70%" poster=""> </video>
</div>

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Lightricks/LTX-2.git
cd LTX-2

# Set up the environment
uv sync --frozen
source .venv/bin/activate
```

### Required Models

Download the following models from the [LTX-2 HuggingFace repository](https://huggingface.co/Lightricks/LTX-2):

**LTX-2 Model Checkpoint** (choose and download one of the following)
  * [`ltx-2-19b-dev-fp8.safetensors`](https://huggingface.co/Lightricks/LTX-2/blob/main/ltx-2-19b-dev-fp8.safetensors) - [Download](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-dev-fp8.safetensors)

  * [`ltx-2-19b-dev.safetensors`](https://huggingface.co/Lightricks/LTX-2/blob/main/ltx-2-19b-dev.safetensors) - [Download](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-dev.safetensors)
  * [`ltx-2-19b-distilled.safetensors`](https://huggingface.co/Lightricks/LTX-2/blob/main/ltx-2-19b-distilled.safetensors) - [Download](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled.safetensors)
  * [`ltx-2-19b-distilled-fp8.safetensors`](https://huggingface.co/Lightricks/LTX-2/blob/main/ltx-2-19b-distilled-fp8.safetensors) - [Download](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled-fp8.safetensors)

**Spatial Upscaler** - Required for current two-stage pipeline implementations in this repository
  * [`ltx-2-spatial-upscaler-x2-1.0.safetensors`](https://huggingface.co/Lightricks/LTX-2/blob/main/ltx-2-spatial-upscaler-x2-1.0.safetensors) - [Download](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-spatial-upscaler-x2-1.0.safetensors)

**Temporal Upscaler** - Supported by the model and will be required for future pipeline implementations
  * [`ltx-2-temporal-upscaler-x2-1.0.safetensors`](https://huggingface.co/Lightricks/LTX-2/blob/main/ltx-2-temporal-upscaler-x2-1.0.safetensors) - [Download](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-temporal-upscaler-x2-1.0.safetensors)

**Distilled LoRA** - Required for current two-stage pipeline implementations in this repository (except DistilledPipeline and ICLoraPipeline)
  * [`ltx-2-19b-distilled-lora-384.safetensors`](https://huggingface.co/Lightricks/LTX-2/blob/main/ltx-2-19b-distilled-lora-384.safetensors) - [Download](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled-lora-384.safetensors)

**Gemma Text Encoder** (download all assets from the repository)
  * [`Gemma 3`](https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized/tree/main)

**LoRAs**
  * [`LTX-2-19b-IC-LoRA-Canny-Control`](https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Canny-Control) - [Download](https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Canny-Control/resolve/main/ltx-2-19b-ic-lora-canny-control.safetensors)
  * [`LTX-2-19b-IC-LoRA-Depth-Control`](https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Depth-Control) - [Download](https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Depth-Control/resolve/main/ltx-2-19b-ic-lora-depth-control.safetensors)
  * [`LTX-2-19b-IC-LoRA-Detailer`](https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Detailer) - [Download](https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Detailer/resolve/main/ltx-2-19b-ic-lora-detailer.safetensors)
  * [`LTX-2-19b-IC-LoRA-Pose-Control`](https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Pose-Control) - [Download](https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Pose-Control/resolve/main/ltx-2-19b-ic-lora-pose-control.safetensors)
  * [`LTX-2-19b-LoRA-Camera-Control-Dolly-In`](https://huggingface.co/Lightricks/LTX-2-19b-LoRA-Camera-Control-Dolly-In) - [Download](https://huggingface.co/Lightricks/LTX-2-19b-LoRA-Camera-Control-Dolly-In/resolve/main/ltx-2-19b-lora-camera-control-dolly-in.safetensors)
  * [`LTX-2-19b-LoRA-Camera-Control-Dolly-Left`](https://huggingface.co/Lightricks/LTX-2-19b-LoRA-Camera-Control-Dolly-Left) - [Download](https://huggingface.co/Lightricks/LTX-2-19b-LoRA-Camera-Control-Dolly-Left/resolve/