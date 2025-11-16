# LongCat-Video

<div align="center">
  <img src="assets/longcat-video_logo.svg" width="45%" alt="LongCat-Video" />
</div>
<hr>

<div align="center" style="line-height: 1;">
  <a href='https://meituan-longcat.github.io/LongCat-Video/'><img src='https://img.shields.io/badge/Project-Page-green'></a>
  <a href='https://arxiv.org/abs/2510.22200'><img src='https://img.shields.io/badge/Technique-Report-red'></a>
  <a href='https://huggingface.co/meituan-longcat/LongCat-Video'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-blue'></a>
</div>

<div align="center" style="line-height: 1;">
  <a href='https://github.com/meituan-longcat/LongCat-Flash-Chat/blob/main/figures/wechat_official_accounts.png'><img src='https://img.shields.io/badge/WeChat-LongCat-brightgreen?logo=wechat&logoColor=white'></a>  
  <a href='https://x.com/Meituan_LongCat'><img src='https://img.shields.io/badge/Twitter-LongCat-white?logo=x&logoColor=white'></a>
</div>

<div align="center" style="line-height: 1;">
  <a href='LICENSE'><img src='https://img.shields.io/badge/License-MIT-f5de53?&color=f5de53'></a>
</div>

## Model Introduction
We introduce LongCat-Video, a foundational video generation model with 13.6B parameters, delivering strong performance across *Text-to-Video*, *Image-to-Video*, and *Video-Continuation* generation tasks. It particularly excels in efficient and high-quality long video generation, representing our first step toward world models.

### Key Features
- 🌟 **Unified architecture for multiple tasks**: LongCat-Video unifies *Text-to-Video*, *Image-to-Video*, and *Video-Continuation* tasks within a single video generation framework. It natively supports all these tasks with a single model and consistently delivers strong performance across each individual task.
- 🌟 **Long video generation**: LongCat-Video is natively pretrained on *Video-Continuation* tasks, enabling it to produce minutes-long videos without color drifting or quality degradation.
- 🌟 **Efficient inference**: LongCat-Video generates $720p$, $30fps$ videos within minutes by employing a coarse-to-fine generation strategy along both the temporal and spatial axes. Block Sparse Attention further enhances efficiency, particularly at high resolutions
- 🌟 **Strong performance with multi-reward RLHF**: Powered by multi-reward Group Relative Policy Optimization (GRPO), comprehensive evaluations on both internal and public benchmarks demonstrate that LongCat-Video achieves performance comparable to leading open-source video generation models as well as the latest commercial solutions.

For more detail, please refer to the comprehensive [***LongCat-Video Technical Report***](https://arxiv.org/abs/2510.22200).

## 🎥 Teaser Video

<div align="center">
  <video src="https://github.com/user-attachments/assets/00fa63f0-9c4e-461a-a79e-c662ad596d7d" width="2264" height="384"> </video>
</div>

## Quick Start

### Installation

Clone the repo:

```shell
git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video
cd LongCat-Video
```

Install dependencies:

```shell
# create conda environment
conda create -n longcat-video python=3.10
conda activate longcat-video

# install torch (configure according to your CUDA version)
pip install torch==2.6.0+cu124 torchvision==0.21.0+cu124 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124

# install flash-attn-2
pip install ninja 
pip install psutil 
pip install packaging 
pip install flash_attn==2.7.4.post1

# install other requirements
pip install -r requirements.txt
```

FlashAttention-2 is enabled in the model config by default; you can also change the model config ("./weights/LongCat-Video/dit/config.json") to use FlashAttention-3 or xformers once installed.

### Model Download

| Models | Download Link |
| --- | --- |
| LongCat-Video | 🤗 [Huggingface](https://huggingface.co/meituan-longcat/LongCat-Video) |

Download models using huggingface-cli:
```shell
pip install "huggingface_hub[cli]"
huggingface-cli download meituan-longcat/LongCat-Video --local-dir ./weights/LongCat-Video
```

### Run Text-to-Video

```shell
# Single-GPU inference
torchrun run_demo_text_to_video.py --checkpoint_dir=./weights/LongCat-Video --enable_compile

# Multi-GPU inference
torchrun --nproc_per_node=2 run_demo_text_to_video.py --context_parallel_size=2 --checkpoint_dir=./weights/LongCat-Video --enable_compile
```

### Run Image-to-Video

```shell
# Single-GPU inference
torchrun run_demo_image_to_video.py --checkpoint_dir=./weights/LongCat-Video --enable_compile

# Multi-GPU inference
torchrun --nproc_per_node=2 run_demo_image_to_video.py --context_parallel_size=2 --checkpoint_dir=./weights/LongCat-Video --enable_compile
```

### Run Video-Continuation

```shell
# Single-GPU inference
torchrun run_demo_video_continuation.py --checkpoint_dir=./weights/LongCat-Video --enable_compile

# Multi-GPU inference
torchrun --nproc_per_node=2 run_demo_video_continuation.py --context_parallel_size=2 -