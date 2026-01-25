<p align="center">
    <picture>
        <source srcset="./assets/logo.png" media="(prefers-color-scheme: dark)">
        <img src="./assets/logo.png" width="30%">
    </picture>
    
</p>

<p align="center">
    <a href="https://heartmula.github.io/">Demo 🎶</a> &nbsp;|&nbsp; 📑 <a href="https://arxiv.org/pdf/2601.10547">Paper</a>
    <br>
    <a href="https://huggingface.co/HeartMuLa/HeartMuLa-oss-3B">HeartMuLa-oss-3B 🤗</a> &nbsp;|&nbsp; <a href="https://modelscope.cn/models/HeartMuLa/HeartMuLa-oss-3B">HeartMuLa-oss-3B <picture>
        <source srcset="./assets/badge.svg" media="(prefers-color-scheme: dark)">
        <img src="./assets/badge.svg" width="20px">
    </picture></a>
    <br>
    <a href="https://huggingface.co/HeartMuLa/HeartMuLa-RL-oss-3B-20260123"> HeartMuLa-RL-oss-3B-20260123 🤗</a> &nbsp;|&nbsp; <a href="https://modelscope.cn/models/HeartMuLa/HeartMuLa-RL-oss-3B-20260123">HeartMuLa-RL-oss-3B-20260123 <picture>
        <source srcset="./assets/badge.svg" media="(prefers-color-scheme: dark)">
        <img src="./assets/badge.svg" width="20px">
    </picture></a>
    
</p>

---
# HeartMuLa: A Family of Open Sourced Music Foundation Models

HeartMuLa is a family of open sourced music foundation models including: 
1. HeartMuLa: a music language model that generates music conditioned on lyrics and tags with multilingual support including but not limited to English, Chinese, Japanese, Korean and Spanish.
2. HeartCodec: a 12.5 hz music codec with high reconstruction fidelity;
3. HeartTranscriptor: a whisper-based model specifically tuned for lyrics transcription; Check [this page](./examples/README.md) for its usage.
4. HeartCLAP: an audio–text alignment model that establishes a unified embedding space for music descriptions and cross-modal retrieval.
---


Below shows the experiment result of our oss-3B version compared with other baselines.
<p align="center">
    <picture>
        <source srcset="./assets/exp.png" media="(prefers-color-scheme: dark)">
        <img src="./assets/exp.png" width="90%">
    </picture>
    
</p>

---

## 🔥 Highlight

Our latest internal version of HeartMuLa-7B achieves **comparable performance with Suno** in terms of musicality, fidelity and controllability. If you are interested, welcome to reach us out via heartmula.ai@gmail.com

## 📰 News
Join on Discord! [<img alt="join discord" src="https://img.shields.io/discord/842440537755353128?color=%237289da&logo=discord"/>](https://discord.gg/BKXF5FgH)

- 🚀 **23 Jan. 2026**

    By leveraging Reinforcement Learning, we have continuously refined our model and are proud to officially release **HeartMuLa-RL-oss-3B-20260123**. This version is designed to achieve more precise control over styles and tags. Simultaneously, we are launching **HeartCodec-oss-20260123**, which optimizes audio decoding quality.

- 🫶 **20 Jan. 2026** 
    
    [Benji](https://github.com/benjiyaya) has created a wonderful [ComfyUI custom node](https://github.com/benjiyaya/HeartMuLa_ComfyUI) for HeartMuLa. Thanks Benji!
- ⚖️ **20 Jan. 2026** 

    License update: We update the license of this repo and all related model weights to **Apache 2.0**.
- 🚀 **14 Jan. 2026**  
    The official release of **HeartTranscriptor-oss** and the first **HeartMuLa-oss-3B** version along with our **HeartCodec-oss**.

---
## 🧭 TODOs

- ⏳ Release scripts for inference acceleration and streaming inference. The current inference speed is around RTF $\approx 1.0$.
- ⏳ Support **reference audio conditioning**, **fine-grained controllable music generation**, **hot song generation**.
- ⏳ Release the **HeartMuLa-oss-7B** version.
- ✅ Release inference code and pretrained checkpoints of  
  **HeartCodec-oss, HeartMuLa-oss-3B, and HeartTranscriptor-oss**.

---

## 🛠️ Local Deployment

### ⚙️ Environment Setup

We recommend using `python=3.10` for local deployment.

Clone this repo and install locally.

```
git clone https://github.com/HeartMuLa/heartlib.git
cd heartlib
pip install -e .
```

Download our pretrained checkpoints from huggingface or modelscope using the following command:

```
# if you are using huggingface
hf download --local-dir './ckpt' 'HeartMuLa/HeartMuLaGen'

## To use version released on 20260123 (recommended)
hf download --local-dir './ckpt/HeartMuLa-oss-3B' 'HeartMuLa/HeartMuLa-RL-oss-3B-20260123'
hf download --local-dir './ckpt/HeartCodec-oss' HeartMuLa/HeartCodec-oss-20260123

## To use oss-3B version
hf download --local-dir './ckpt/HeartMuLa-oss-3B' 'HeartMuLa/HeartMuLa-oss-3B'
hf download --local-dir './ckpt/HeartCodec-oss' 'HeartMuLa/HeartCodec-oss'

# if you are using modelscope
modelscope download --model 'HeartMuLa/HeartMuLaGen' --local_dir './ckpt'

## To use version released on 20260123 (recommended)
modelscope download --model 'HeartMuLa/HeartMuLa-RL-oss-3B-20260123' --local_dir './ckpt/HeartMuLa-oss-3B'
modelscope download --model 'HeartMuLa/HeartCodec-oss-20260123' --local_dir './ckpt/HeartCodec-oss'

## To use oss-3B version
modelscope download --m