![](assets/teaser.webp)

# Native and Compact Structured Latents for 3D Generation

<a href="https://arxiv.org/abs/2512.14692"><img src="https://img.shields.io/badge/Paper-Arxiv-b31b1b.svg" alt="Paper"></a>
<a href="https://huggingface.co/microsoft/TRELLIS.2-4B"><img src="https://img.shields.io/badge/Hugging%20Face-Model-yellow" alt="Hugging Face"></a>
<a href="https://huggingface.co/spaces/microsoft/TRELLIS.2"><img src="https://img.shields.io/badge/Hugging%20Face-Demo-blueviolet"></a>
<a href="https://microsoft.github.io/TRELLIS.2"><img src="https://img.shields.io/badge/Project-Website-blue" alt="Project Page"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green" alt="License"></a>

https://github.com/user-attachments/assets/63b43a7e-acc7-4c81-a900-6da450527d8f

*(Compressed version due to GitHub size limits. See the full-quality video on our project page!)*

**TRELLIS.2** is a state-of-the-art large 3D generative model (4B parameters) designed for high-fidelity **image-to-3D** generation. It leverages a novel "field-free" sparse voxel structure termed **O-Voxel** to reconstruct and generate arbitrary 3D assets with complex topologies, sharp features, and full PBR materials.


## ✨ Features

### 1. High Quality, Resolution & Efficiency
Our 4B-parameter model generates high-resolution fully textured assets with exceptional fidelity and efficiency using vanilla DiTs. It utilizes a Sparse 3D VAE with 16× spatial downsampling to encode assets into a compact latent space.

| Resolution | Total Time* | Breakdown (Shape + Mat) |
| :--- | :--- | :--- |
| **512³** | **~3s** | 2s + 1s |
| **1024³** | **~17s** | 10s + 7s |
| **1536³** | **~60s** | 35s + 25s |

<small>*Tested on NVIDIA H100 GPU.</small>

### 2. Arbitrary Topology Handling
The **O-Voxel** representation breaks the limits of iso-surface fields. It robustly handles complex structures without lossy conversion:
*   ✅ **Open Surfaces** (e.g., clothing, leaves)
*   ✅ **Non-manifold Geometry**
*   ✅ **Internal Enclosed Structures**

### 3. Rich Texture Modeling
Beyond basic colors, TRELLIS.2 models arbitrary surface attributes including **Base Color, Roughness, Metallic, and Opacity**, enabling photorealistic rendering and transparency support.

### 4. Minimalist Processing
Data processing is streamlined for instant conversions that are fully **rendering-free** and **optimization-free**.
*   **< 10s** (Single CPU): Textured Mesh → O-Voxel
*   **< 100ms** (CUDA): O-Voxel → Textured Mesh


## 🗺️ Roadmap

- [x] Paper release
- [x] Release image-to-3D inference code
- [x] Release pretrained checkpoints (4B)
- [x] Hugging Face Spaces demo
- [ ] Release shape-conditioned texture generation inference code (Current schdule: before 12/24/2025)
- [ ] Release training code (Current schdule: before 12/31/2025)


## 🛠️ Installation

### Prerequisites
- **System**: The code is currently tested only on **Linux**.
- **Hardware**: An NVIDIA GPU with at least 24GB of memory is necessary. The code has been verified on NVIDIA A100 and H100 GPUs.  
- **Software**:   
  - The [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive) is needed to compile certain packages. Recommended version is 12.4.  
  - [Conda](https://docs.anaconda.com/miniconda/install/#quick-command-line-install) is recommended for managing dependencies.  
  - Python version 3.8 or higher is required. 

### Installation Steps
1. Clone the repo:
    ```sh
    git clone -b main https://github.com/microsoft/TRELLIS.2.git --recursive
    cd TRELLIS.2
    ```

2. Install the dependencies:
    
    **Before running the following command there are somethings to note:**
    - By adding `--new-env`, a new conda environment named `trellis2` will be created. If you want to use an existing conda environment, please remove this flag.
    - By default the `trellis2` environment will use pytorch 2.6.0 with CUDA 12.4. If you want to use a different version of CUDA, you can remove the `--new-env` flag and manually install the required dependencies. Refer to [PyTorch](https://pytorch.org/get-started/previous-versions/) for the installation command.
    - If you have multiple CUDA Toolkit versions installed, `CUDA_HOME` should be set to the correct version before running the command. For example, if you have CUDA Toolkit 12.4 and 13.0 installed, you can run `export CUDA_HOME=/usr/local/cuda-12.4` before running the command.
    - By default, the code uses the `flash-attn` backend for attention. For GPUs do not support `flash-attn` (e.g., NVIDIA V100), you can install `xformers` manually and set the `ATTN_BACKEND` environment variable to `xformers` before running the code. See the [Minimal Example](#minimal-example) for more details.
    - The installation may take a while due to the large number of dependencies. Please be patient. If you encounter any issues, you can try to install the dependencies one by one, specifying one flag at a time.
    - If you encounter any issues during the installa