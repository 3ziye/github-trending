<div align="center">
  <img src="figure/LOGO2.png" width="70%" style="vertical-align:-7px;" />


[![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/pdf/2509.09372) [![Hugging Face Collection](https://img.shields.io/badge/Models-fcd022?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/VLA-Adapter) [![Twitter](https://img.shields.io/badge/AK-%23000000.svg?style=for-the-badge&logo=x&logoColor=white)](https://x.com/_akhaliq/status/1966610780838621241) [![WeChat](https://img.shields.io/badge/WeChat--Group-07C160?style=for-the-badge&logo=wechat&logoColor=white)](https://github.com/OpenHelix-Team/VLA-Adapter/issues/1)

</div>

### The official implementation of **VLA-Adapter**.
<br/>

<div id="top" align="center">
<p align="center">
<img src=figure/Framework.png width=90% />
</p>
</div>

> **📝 Paper: https://arxiv.org/abs/2509.09372**<br/>
> **🌍 Project page: https://vla-adapter.github.io/**<br/>
> **🤗 HuggingFace: https://huggingface.co/VLA-Adapter**<br/>
> **Github: https://github.com/OpenHelix-Team/VLA-Adapter**

<br/>

## :loudspeaker: News!
- **[2025/09/22]** We released our codes! An enhanced **Pro** version is also released (this version conforms to the pipeline in the original paper, but is optimized in implementation). Everyone is welcome to use it!🎉
- **[2025/09/13]** Our paper won the 🥇**first place** in the [daily list](https://huggingface.co/papers/date/2025-09-12), the 🥈**second place** in the [weekly list](https://huggingface.co/papers/week/2025-W37), and 🥉**third place** in the [Monthly list](https://huggingface.co/papers/month/2025-09) in HF! ⭐
- **[2025/09/13]** Our paper listed in the [Trending Paper](https://huggingface.co/papers/trending) in HF! ⭐
- **[2025/09/12]** We released the original version of the VLA-Adapter for four LIBERO models on [HuggingFace](https://huggingface.co/VLA-Adapter).
- **[2025/09/11]** We released our paper on [ArXiv](https://arxiv.org/abs/2509.09372).

<br/>

## :black_nib: TODO List<a name="todo"></a>

- [x]  Release **checkpoints** for reproduction.
- [x]  Release [VLA-Adapter v2 paper](https://arxiv.org/abs/2509.09372).
- [ ]  A more **powerful version**, **VLA-Adapter++**, and a detailed **technical report** 📝 will be released soon.<br/>
- [ ]  Continue to update the code to adapt to various **real-world systems** deployments, including the configuration of our paper, Franka, UR-5, and AGILE Piper.<br/>
- [ ]  It will soon be compatible with **various foundation models**, including but not limited to [VPP](https://arxiv.org/abs/2412.14803), [π0.5](https://arxiv.org/abs/2504.16054).<br/>
- [ ]  We will update the **diffusion transformers** and **flow matching** policy networks in the future, and the results will be updated in the subsequent VLA-Adapter++ technical report.
- [ ]  We will also update and give more experiments on **Frozen backbone**.
- [ ]  We will expand its **generalization** further in the future. Work is in progress! So please stay tuned!
- [ ]  **RL post-training** is also in progress. Interested researchers are welcome to join us in building this foundation!
- [ ]  **The dual-system compatibility** of VLA-Adapter is under exploration!


<br/>

## 🌟 Table of Contents

- [:rocket: Quick Start](#rocket-quick-start) 
  - [Conda Environment of VLA-Adapter](#conda-environment-of-vla-adapter)
  - [Install Dependencies](#install-dependencies)
- [:pencil: Data Preparation](#pencil-data-preparation) 
  - [LIBERO Benchmark](#libero-benchmark)
  - [CALVIN Benchmark](#calvin-benchmark)
  - [:video_game: Our Dependencies](#video_game-our-dependencies)
  - [:pushpin: Benchmark Location](#pushpin-benchmark-location)
- [⚓ VLM backbone](#vlm)
- [:fire: Training for Different Configurations](#fire-training-for-different-configurations) &emsp; => Provides **training configurations** for GPUs ranging from **10GB** to **80GB** of VRAM.
  - [:books: Related File for Training](#books-related-file-for-training)
  - [:ledger: How to Train on Extremely Limited VRAM GPUs](#ledger-how-to-train-on-extremely-limited-vram-gpus) &emsp; => A card with 10GB-12GB *(e.g. NVIDIA GeForce RTX 2080Ti, 3060, 3080, 4070, 4080, and 5070)*
  - [:ledger: How to Train on Low VRAM GPUs](#ledger-how-to-train-on-low-vram-gpus) &emsp; => A card with 24GB *(e.g. NVIDIA GeForce RTX 3090 and 4090)*
  - [:ledger: How to Train on Larger VRAM GPUs](#ledger-how-to-train-on-larger-vram-gpus) &emsp; => A Consumer GPU with 32GB *(e.g. NVIDIA GeForce RTX 5090)* &emsp; A Professional-Grade GPU with 40GB-48GB *(e.g. NVIDIA A100-40GB, A800-40GB, L20, and RTX A6000).*
  - [:ledger: How to Train on Sufficient VRAM GPUs](#ledger-how-to-train-on-sufficient-vram-gpus) &emsp; => Professional-Grade GPUs with ≥80GB *(e.g. NVIDIA A100-80GB, A800-80GB, H100, H800, H20-NVLink, and GB200).*
- [:mechanical_arm: Inference](#mechanical_arm-inference)
  - [:books: Related File for Inference](#books-related-file-for-inference)
  -