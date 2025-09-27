# Qwen3-Omni

<br>

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com//Qwen3-Omni/qwen3_omni_logo.png" width="400"/>
<p>

<p align="center">
        💜 <a href="https://chat.qwen.ai/"><b>Qwen Chat</b></a>&nbsp&nbsp | &nbsp&nbsp🤗 <a href="https://huggingface.co/collections/Qwen/qwen3-omni-68d100a86cd0906843ceccbe">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/collections/Qwen3-Omni-867aef131e7d4f">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://qwen.ai/blog?id=65f766fc2dcba7905c1cb69cc4cab90e94126bf4&from=research.latest-advancements-list">Blog</a>&nbsp&nbsp | &nbsp&nbsp📚 <a href="https://github.com/QwenLM/Qwen3-Omni/tree/main/cookbooks">Cookbooks</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://arxiv.org/pdf/2509.17765">Paper</a>&nbsp&nbsp
<br>
🖥️ <a href="https://huggingface.co/spaces/Qwen/Qwen3-Omni-Demo">Hugging Face Demo</a>&nbsp&nbsp | &nbsp&nbsp 🖥️ <a href="https://modelscope.cn/studios/Qwen/Qwen3-Omni-Demo">ModelScope Demo</a>&nbsp&nbsp | &nbsp&nbsp💬 <a href="https://github.com/QwenLM/Qwen/blob/main/assets/wechat.png">WeChat (微信)</a>&nbsp&nbsp | &nbsp&nbsp🫨 <a href="https://discord.gg/CV4E9rpNSD">Discord</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://help.aliyun.com/zh/model-studio/user-guide/qwen-omni">API</a>

</p>

We release **Qwen3-Omni**, the natively end-to-end multilingual omni-modal foundation models. It is designed to process diverse inputs including text, images, audio, and video, while delivering real-time streaming responses in both text and natural speech. Click the video below for more information 😃

<details open>
<summary>English Version</summary>
<a href="https://youtu.be/_zdOrPju4_g" target="_blank">
  <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/videocover.png" alt="Open English Video"/>
</a>
</details>

<details>
<summary>Chinese Version</summary>
<a href="https://youtu.be/Wtjsw5deXfQ" target="_blank">
  <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/videocover.png" alt="打开中文视频"/>
</a>
</details>


## News
* 2025.09.26: ⭐️⭐️⭐️ Qwen3-Omni reaches top-1 on Hugging Face Trending! 
* 2025.09.22: 🎉🎉🎉 We have released [Qwen3-Omni](https://huggingface.co/collections/Qwen/qwen3-omni-68d100a86cd0906843ceccbe). For more details, please check our [blog](https://qwen.ai/blog?id=65f766fc2dcba7905c1cb69cc4cab90e94126bf4&from=research.latest-advancements-list)!

## Contents <!-- omit in toc -->

- [Overview](#overview)
  - [Introduction](#introduction)
  - [Model Architecture](#model-architecture)
  - [Cookbooks for Usage Cases](#cookbooks-for-usage-cases)
- [QuickStart](#quickstart)
  - [Model Description and Download](#model-description-and-download)
  - [Transformers Usage](#transformers-usage)
  - [vLLM Usage](#vllm-usage)
  - [DashScope API Usage](#dashscope-api-usage)
  - [Usage Tips (Recommended Reading)](#usage-tips-recommended-reading)
- [Interaction with Qwen3-Omni](#interaction-with-qwen3-omni)
  - [Online Demo](#online-demo)
  - [Real-Time Interaction](#real-time-interaction)
  - [Launch Local Web UI Demo](#launch-local-web-ui-demo)
- [Docker](#-docker)
- [Evaluation](#evaluation)
  - [Performance of Qwen3-Omni](#performance-of-qwen3-omni)
  - [Setting for Evaluation](#setting-for-evaluation)
- [Citation](#citation)

## Overview
### Introduction

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/q3o_introduction.png" width="90%"/>
<p>

Qwen3-Omni is the natively end-to-end multilingual omni-modal foundation models. It processes text, images, audio, and video, and delivers real-time streaming responses in both text and natural speech. We introduce several architectural upgrades to improve performance and efficiency. Key features:

* **State-of-the-art across modalities**: Early text-first pretraining and mixed multimodal training provide native multimodal support. While achieving strong audio and audio-video results, unimodal text and image performance does not regress. Reaches SOTA on 22 of 36 audio/video benchmarks and open-source SOTA on 32 of 36; ASR, audio understanding, and voice conversation performance is comparable to Gemini 2.5 Pro.

* **Multilingual**: Supports 119 text languages, 19 speech input languages, and 10 speech output languages.
  - **Speech Input**: English, Chinese, Korean, Japanese, German, Russian, Italian, French, Spanish, Portuguese, Malay, Dutch, Indonesian, Turkish, Vietnamese, Cantonese, Arabic, Urdu.
  - **Speech Output**: English, Chinese, French, German, Russian, Italian, Spanish, Portuguese, Japanese, Korean.

* **Novel Architecture**: MoE-based Thinker–Talker design with AuT pretraining for strong general representations, plus a multi-codebook design that drives latency to a minimum.

* **Real-time Audio/Video Interaction**: Low-latency streaming with natural turn-taking and immediate text or speech responses.

* **Flexible Control**: Customize behavior via system prompts for fine-grained control and easy 