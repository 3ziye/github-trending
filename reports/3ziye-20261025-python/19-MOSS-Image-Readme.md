<div align="center">
  <p>
    <img src="assets/lockup-light.svg#gh-light-mode-only" alt="MOSS-Image" width="520">
    <img src="assets/lockup-dark.svg#gh-dark-mode-only" alt="MOSS-Image" width="520">
  </p>
  <p>
    <a href="https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base"><img alt="Hugging Face · MOSS-Image-Base" src="https://img.shields.io/badge/🤗%20Hugging%20Face-MOSS--Image--Base-ffc107?style=flat-square"></a>
    &nbsp;
    <a href="https://huggingface.co/OpenMOSS-Team/MOSS-Image-SFT"><img alt="Hugging Face · MOSS-Image-SFT" src="https://img.shields.io/badge/🤗%20Hugging%20Face-MOSS--Image--SFT-ffc107?style=flat-square"></a>
    &nbsp;
    <a href="https://modelscope.cn/models/openmoss/MOSS-Image-Base"><img alt="ModelScope · MOSS-Image-Base" src="assets/modelscope-base-badge.svg"></a>
    &nbsp;
    <a href="https://modelscope.cn/models/openmoss/MOSS-Image-SFT"><img alt="ModelScope · MOSS-Image-SFT" src="assets/modelscope-sft-badge.svg"></a>
    &nbsp;
    <a href="https://huggingface.co/spaces/OpenMOSS-Team/MOSS-Image"><img alt="Hugging Face Spaces · Demo" src="https://img.shields.io/badge/🤗%20Spaces-Demo-4f46e5?style=flat-square"></a>
    &nbsp;
    <a href="https://platform.mosi.cn/?utm_source=github&amp;utm_medium=readme&amp;utm_campaign=imageapi"><img alt="MOSI API Platform" src="https://img.shields.io/badge/🔌%20MOSI-API%20Platform-0f766e?style=flat-square"></a>
    &nbsp;
    <a href="https://openmoss.github.io/MOSS-Image/"><img alt="Homepage" src="https://img.shields.io/badge/🌐%20Project-Homepage-2563eb?style=flat-square"></a>
    &nbsp;
    <a href="paper/MOSS_Image_Technical_Report.pdf"><img alt="Technical Report" src="https://img.shields.io/badge/📄%20Paper-Technical_Report-b31b1b?style=flat-square"></a>
    &nbsp;
    <a href="https://arxiv.org/abs/2610.23374"><img alt="arXiv: 2610.23374" src="https://img.shields.io/badge/arXiv-2610.23374-b31b1b?style=flat-square&amp;logo=arxiv&amp;logoColor=white"></a>
    &nbsp;
    <a href="https://x.com/Open_MOSS"><img alt="Follow OpenMOSS on X" src="https://img.shields.io/badge/Follow-OpenMOSS-000000?style=flat-square&amp;logo=x&amp;logoColor=white"></a>
    &nbsp;
    <a href="https://qm.qq.com/q/hphM7VhaDu"><img alt="MOSS-Image QQ 交流群：755535143" src="https://img.shields.io/badge/QQ-755535143-12B7F5?style=flat-square&amp;logo=qq&amp;logoColor=white"></a>
    &nbsp;
    <a href="https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=7a3m2007-815f-409b-9c3d-a4129f5c058e"><img alt="MOSS-Builders Feishu Community" src="assets/feishu-builders-badge.svg"></a>
    &nbsp;
    <a href="https://discord.gg/nXFWEyvbb"><img alt="MOSS-Image Discord Community" src="https://img.shields.io/badge/Discord-Community-5865F2?style=flat-square&amp;logo=discord&amp;logoColor=white"></a>
  </p>
  <p>
    <strong>English</strong> &nbsp; | &nbsp; <a href="README_ZH.md">简体中文</a>
  </p>
</div>


## News

- **[2026-10-20]** 🚀 The **MOSS-Image** series is now available on the [MOSI API Platform](https://platform.mosi.cn/?utm_source=github&utm_medium=readme&utm_campaign=imageapi). Try it in the Playground or integrate it through the API.

- **[2026-10-19]** 📄 The [MOSS-Image Technical Report](https://arxiv.org/abs/2610.23374) is now available on arXiv. If you find our work useful, please support us with an [upvote on Hugging Face Papers](https://huggingface.co/papers/2610.23374)! 🤗

- **[2026-10-18]** 🛠️ [KohakuMossTrainer](https://github.com/KohakuBlueleaf/KohakuMossTrainer) has been released, offering full fine-tuning and LyCORIS training (including LoRA) for **MOSS-Image-Base** and **MOSS-Image-SFT**. It features extensive optimizer support, mixed-precision training (BF16/FP16/FP8/MXFP8/INT8), multi-GPU training (DDP/FSDP/pipeline parallelism), optimized kernels, and CPU offloading, enabling adapter training with as little as **6GB VRAM**. It supports Windows, Linux, NVIDIA GPUs (SM70–SM120), and Intel Arc GPUs. See the [GitHub repository](https://github.com/KohakuBlueleaf/KohakuMossTrainer) for details.

- **[2026-10-16]** 🚀 MOSS-Image has day-0 support in [SGLang](https://docs.sglang.io/cookbook/diffusion/OpenMOSS/MOSS-Image), [vLLM-Omni](https://recipes.vllm.ai/OpenMOSS-Team/MOSS-Image-Base), and [ComfyUI](https://huggingface.co/Comfy-Org/MOSS-Image).

- **[2026-10-16]** 🎉 We are introducing **MOSS-Image-Base** and **MOSS-Image-SFT**! Code and model weights are publicly available.

  **Our key highlights:**

  - 📐 **Layout control:** Control the placement of text and visual elements.
  - ✍️ **Strong text rendering:** Generate clear, accurate text within images.
  - 📜 **Long-prompt support:** Accept text prompts of up to 4K tokens.
  - 🎨 **Versatile visual styles:** Create high-quality anime and photorealistic images.
  - 🛠️ **Easy to fine-tune:** Adapt the base model to custom tasks and domains.
  - ⚡ **Compact and efficient:** Efficient image generation with a 5B backbone.
  - 🖥️ **Heterogeneous GPU training**: Trained on alternative GPU platforms.

<a id="c