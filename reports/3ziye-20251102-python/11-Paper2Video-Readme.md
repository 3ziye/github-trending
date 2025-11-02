# Paper2Video

<p align="right">
  <b>English</b> | <a href="./README-CN.md">简体中文</a>
</p>


<p align="center">
  <b>Paper2Video: Automatic Video Generation from Scientific Papers</b>
<br>
从学术论文自动生成演讲视频
</p>

<p align="center">
  <a href="https://zeyu-zhu.github.io/webpage/">Zeyu Zhu*</a>,
  <a href="https://qhlin.me/">Kevin Qinghong Lin*</a>,
  <a href="https://scholar.google.com/citations?user=h1-3lSoAAAAJ&hl=en">Mike Zheng Shou</a> <br>
  Show Lab, National University of Singapore
</p>


<p align="center">
  <a href="https://arxiv.org/abs/2510.05096">📄 Paper</a> &nbsp; | &nbsp;
  <a href="https://huggingface.co/papers/2510.05096">🤗 Daily Paper</a> &nbsp; | &nbsp;
  <a href="https://huggingface.co/datasets/ZaynZhu/Paper2Video">📊 Dataset</a> &nbsp; | &nbsp;
  <a href="https://showlab.github.io/Paper2Video/">🌐 Project Website</a> &nbsp; | &nbsp;
  <a href="https://x.com/KevinQHLin/status/1976105129146257542">💬 X (Twitter)</a>
</p>

- **Input:** a paper ➕ an image ➕ an audio
  
| Paper | Image | Audio |
|--------|--------|--------|
| <img src="https://github.com/showlab/Paper2Video/blob/page/assets/hinton/paper.png" width="180"/><br>[🔗 Paper link](https://arxiv.org/pdf/1509.01626) | <img src="https://github.com/showlab/Paper2Video/blob/page/assets/hinton/hinton_head.jpeg" width="180"/> <br>Hinton's photo| <img src="assets/sound.png" width="180"/><br>[🔗 Audio sample](https://github.com/showlab/Paper2Video/blob/page/assets/hinton/ref_audio_10.wav) |


- **Output:** a presentation video



https://github.com/user-attachments/assets/39221a9a-48cb-4e20-9d1c-080a5d8379c4




Check out more examples at [🌐 project page](https://showlab.github.io/Paper2Video/).

## 🔥 Update
**Any contributions are welcome!**
- [x] [2025.10.15] We update a new version without talking-head for fast generation!
- [x] [2025.10.11] Our work receives attention on [YC Hacker News](https://news.ycombinator.com/item?id=45553701).
- [x] [2025.10.9] Thanks AK for sharing our work on [Twitter](https://x.com/_akhaliq/status/1976099830004072849)!
- [x] [2025.10.9] Our work is reported by [Medium](https://medium.com/@dataism/how-ai-learned-to-make-scientific-videos-from-slides-to-a-talking-head-0d807e491b27).
- [x] [2025.10.8] Check out our demo video below!
- [x] [2025.10.7] We release the [arxiv paper](https://arxiv.org/abs/2510.05096).
- [x] [2025.10.6] We release the [code](https://github.com/showlab/Paper2Video) and [dataset](https://huggingface.co/datasets/ZaynZhu/Paper2Video).
- [x] [2025.9.28] Paper2Video has been accepted to the **Scaling Environments for Agents Workshop([SEA](https://sea-workshop.github.io/)) at NeurIPS 2025**.


https://github.com/user-attachments/assets/a655e3c7-9d76-4c48-b946-1068fdb6cdd9




---

### Table of Contents
- [🌟 Overview](#-overview)
- [🚀 Quick Start: PaperTalker](#-try-papertalker-for-your-paper-)
  - [1. Requirements](#1-requirements)
  - [2. Configure LLMs](#2-configure-llms)
  - [3. Inference](#3-inference)
- [📊 Evaluation: Paper2Video](#-evaluation-paper2video)
- [😼 Fun: Paper2Video for Paper2Video](#-fun-paper2video-for-paper2video)
- [🙏 Acknowledgements](#-acknowledgements)
- [📌 Citation](#-citation)

---

## 🌟 Overview
<p align="center">
  <img src="assets/teaser.png" alt="Overview" width="100%">
</p>

This work solves two core problems for academic presentations:

- **Left: How to create a presentation video from a paper?**  
  *PaperTalker* — an agent that integrates **slides**, **subtitling**, **cursor grounding**, **speech synthesis**, and **talking-head video rendering**.

- **Right: How to evaluate a presentation video?**  
  *Paper2Video* — a benchmark with well-designed metrics to evaluate presentation quality.


---

## 🚀 Try PaperTalker for your Paper!
<p align="center">
  <img src="assets/method.png" alt="Approach" width="100%">
</p>

### 1. Requirements
Prepare the environment:
```bash
cd src
conda create -n p2v python=3.10
conda activate p2v
pip install -r requirements.txt
conda install -c conda-forge tectonic
```
**[Optional] [Skip](#2-configure-llms) this part if you do not need a human presenter.**

Download the dependent code and follow the instructions in **[Hallo2](https://github.com/fudan-generative-vision/hallo2)** to download the model weight.
```bash
git clone https://github.com/fudan-generative-vision/hallo2.git
```
You need to **prepare the environment separately for talking-head generation** to potential avoide package conflicts, please refer to  <a href="git clone https://github.com/fudan-generative-vision/hallo2.git">Hallo2</a>. After installing, use `which python` to get the python environment path.
```bash
cd hallo2
conda create -n hallo python=3.10
conda activate hallo
pip install -r requirements.txt
```

### 2. Configure LLMs
Export your **API credentials**:
```bash
export GEMINI_API_KEY="your_gemini_key_here"
export OPENAI_API_KEY="your_openai_key_here"
```
The best practice is to use **GPT4.1** or **Gemini2.5-Pro** for both LLM and VLMs. We also support locally depl