<h3 align="center">
    <img src="assets/uso.webp" alt="Logo" style="vertical-align: middle; width: 95px; height: auto;">
    </br>
    Unified Style and Subject-Driven Generation via Disentangled and Reward Learning
</h3>

<p align="center"> 
<a href="https://bytedance.github.io/USO/"><img alt="Build" src="https://img.shields.io/badge/Project%20Page-USO-blue"></a> 
<a href="https://arxiv.org/abs/2508.18966"><img alt="Build" src="https://img.shields.io/badge/Tech%20Report-USO-b31b1b.svg"></a>
<a href="https://huggingface.co/bytedance-research/USO"><img src="https://img.shields.io/static/v1?label=%F0%9F%A4%97%20Hugging%20Face&message=Model&color=green"></a>
<a href="https://huggingface.co/spaces/bytedance-research/USO"><img src="https://img.shields.io/static/v1?label=%F0%9F%A4%97%20Hugging%20Face&message=demo&color=orange"></a>
</p>
</p>

><p align="center"> <span style="color:#137cf3; font-family: Gill Sans">Shaojin Wu,</span><sup></sup></a>  <span style="color:#137cf3; font-family: Gill Sans">Mengqi Huang,</span></a> <span style="color:#137cf3; font-family: Gill Sans">Yufeng Cheng,</span><sup></sup></a>  <span style="color:#137cf3; font-family: Gill Sans">Wenxu Wu,</span><sup></sup> </a> <span style="color:#137cf3; font-family: Gill Sans">Jiahe Tian,</span><sup></sup></a> <span style="color:#137cf3; font-family: Gill Sans">Yiming Luo,</span><sup></sup></a> <span style="color:#137cf3; font-family: Gill Sans">Fei Ding,</span></a> <span style="color:#137cf3; font-family: Gill Sans">Qian He</span></a> <br> 
><span style="font-size: 13.5px">UXO Team</span><br> 
><span style="font-size: 12px">Intelligent Creation Lab, Bytedance</span></p>

### 🚩 Updates
* **2025.09.12** 🔥 Our new family member [UMO](https://github.com/bytedance/UMO) is here! It focuses on multiple identities and subject-driven generation. You can visit the <a href="https://bytedance.github.io/UMO/" target="_blank">UMO project page</a> for more examples.

* **2025.09.03** 🎉 USO is now natively supported in ComfyUI, see official tutorial [USO in ComfyUI](https://docs.comfy.org/tutorials/flux/flux-1-uso) and our provided examples in `./workflow`. More tips are available in the [README below](https://github.com/bytedance/USO#%EF%B8%8F-comfyui-examples).
<p align="center">
<img src="assets/usoxcomfyui_official.jpeg" width=1024 height="auto">
</p>

* **2025.08.28** 🔥 The [demo](https://huggingface.co/spaces/bytedance-research/USO) of USO is released. Try it Now! ⚡️
* **2025.08.28** 🔥 Update fp8 mode as a primary low vmemory usage support (please scroll down). Gift for consumer-grade GPU users. The peak Vmemory usage is ~16GB now.
* **2025.08.27** 🔥 The [inference code](https://github.com/bytedance/USO) and [model](https://huggingface.co/bytedance-research/USO) of USO are released.
* **2025.08.27** 🔥 The [project page](https://bytedance.github.io/USO) of USO is created.
* **2025.08.27** 🔥 The [technical report](https://arxiv.org/abs/2508.18966) of USO is released.

## 📖 Introduction
Existing literature typically treats style-driven and subject-driven generation as two disjoint tasks: the former prioritizes stylistic similarity, whereas the latter insists on subject consistency, resulting in an apparent antagonism. We argue that both objectives can be unified under a single framework because they ultimately concern the disentanglement and re-composition of “content” and “style”, a long-standing theme in style-driven research. To this end, we present USO, a Unified framework for Style driven and subject-driven GeneratiOn. First, we construct a large-scale triplet dataset consisting of content images, style images, and their corresponding stylized content images. Second, we introduce a disentangled learning scheme that simultaneously aligns style features and disentangles content from style through two complementary objectives, style-alignment training and content–style disentanglement training. Third, we incorporate a style reward-learning paradigm to further enhance the model’s performance.
<p align="center">
    <img src="assets/teaser.webp" width="1024"/>
</p>

## ⚡️ Quick Start

### 🔧 Requirements and Installation

Install the requirements
```bash
## create a virtual environment with python >= 3.10 <= 3.12, like
python -m venv uso_env
source uso_env/bin/activate
## or
conda create -n uso_env python=3.10 -y
conda activate uso_env

## install torch
## recommended version:
pip install torch==2.4.0 torchvision==0.19.0 --index-url https://download.pytorch.org/whl/cu124 

## then install the requirements by you need
pip install -r requirements.txt # legacy installation command
```

Then download checkpoints:
```bash
# 1. set up .env file
cp example.env .env

# 2. set your huggingface token in .env (open the file and change this value to your token)
HF_TOKEN=your_huggingface_token_here

#3. download the necessary weights (comment any weights you don't need)
pip install huggingface_hub
python ./weights/downloader.py
```
- **IF YOU HAVE WEIGHTS, COMMENT OUT W