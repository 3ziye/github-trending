# Qwen3-TTS

<br>

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-TTS-Repo/qwen3_tts_logo.png" width="400"/>
<p>

<p align="center">
&nbsp&nbsp🤗 <a href="https://huggingface.co/collections/Qwen/qwen3-tts">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/collections/Qwen/Qwen3-TTS">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://qwen.ai/blog?id=qwen3tts-0115">Blog</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://arxiv.org/abs/2601.15621">Paper</a>&nbsp&nbsp
<br>
🖥️ <a href="https://huggingface.co/spaces/Qwen/Qwen3-TTS">Hugging Face Demo</a>&nbsp&nbsp | &nbsp&nbsp 🖥️ <a href="https://modelscope.cn/studios/Qwen/Qwen3-TTS">ModelScope Demo</a>&nbsp&nbsp | &nbsp&nbsp💬 <a href="https://github.com/QwenLM/Qwen/blob/main/assets/wechat.png">WeChat (微信)</a>&nbsp&nbsp | &nbsp&nbsp🫨 <a href="https://discord.gg/CV4E9rpNSD">Discord</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://help.aliyun.com/zh/model-studio/qwen-tts-realtime">API</a>

</p>

We release **Qwen3-TTS**, a series of powerful speech generation capabilities developed by Qwen, offering comprehensive support for voice clone, voice design, ultra-high-quality human-like speech generation, and natural language-based voice control. It provides developers and users with the most extensive set of speech generation features available.


## News
* 2026.1.22: 🎉🎉🎉 We have released [Qwen3-TTS](https://huggingface.co/collections/Qwen/qwen3-tts) series (0.6B/1.7B) based on Qwen3-TTS-Tokenizer-12Hz. Please check our [blog](https://qwen.ai/blog?id=qwen3tts-0115)!

## Contents <!-- omit in toc -->

- [Overview](#overview)
  - [Introduction](#introduction)
  - [Model Architecture](#model-architecture)
  - [Released Models Description and Download](#released-models-description-and-download)
- [Quickstart](#quickstart)
  - [Environment Setup](#environment-setup)
  - [Python Package Usage](#python-package-usage)
    - [Custom Voice Generation](#custom-voice-generate)
    - [Voice Design](#voice-design)
    - [Voice Clone](#voice-clone)
    - [Voice Design then Clone](#voice-design-then-clone)
    - [Tokenizer Encode and Decode](#tokenizer-encode-and-decode)
  - [Launch Local Web UI Demo](#launch-local-web-ui-demo)
  - [DashScope API Usage](#dashscope-api-usage)
- [vLLM Usage](#vllm-usage)
- [Fine Tuning](#fine-tuning)
- [Evaluation](#evaluation)
- [Citation](#citation)

## Overview
### Introduction

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-TTS-Repo/qwen3_tts_introduction.png" width="90%"/>
<p>

Qwen3-TTS covers 10 major languages (Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, and Italian) as well as multiple dialectal voice profiles to meet global application needs. In addition, the models feature strong contextual understanding, enabling adaptive control of tone, speaking rate, and emotional expression based on instructions and text semantics, and they show markedly improved robustness to noisy input text. Key features:

* **Powerful Speech Representation**: Powered by the self-developed Qwen3-TTS-Tokenizer-12Hz, it achieves efficient acoustic compression and high-dimensional semantic modeling of speech signals. It fully preserves paralinguistic information and acoustic environmental features, enabling high-speed, high-fidelity speech reconstruction through a lightweight non-DiT architecture.
* **Universal End-to-End Architecture**: Utilizing a discrete multi-codebook LM architecture, it realizes full-information end-to-end speech modeling. This completely bypasses the information bottlenecks and cascading errors inherent in traditional LM+DiT schemes, significantly enhancing the model’s versatility, generation efficiency, and performance ceiling.
* **Extreme Low-Latency Streaming Generation**: Based on the innovative Dual-Track hybrid streaming generation architecture, a single model supports both streaming and non-streaming generation. It can output the first audio packet immediately after a single character is input, with end-to-end synthesis latency as low as 97ms, meeting the rigorous demands of real-time interactive scenarios.
* **Intelligent Text Understanding and Voice Control**: Supports speech generation driven by natural language instructions, allowing for flexible control over multi-dimensional acoustic attributes such as timbre, emotion, and prosody. By deeply integrating text semantic understanding, the model adaptively adjusts tone, rhythm, and emotional expression, achieving lifelike “what you imagine is what you hear” output.


### Model Architecture

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-TTS-Repo/overview.png" width="80%"/>
<p>

### Released Models Description and Download

Below is an introduction and download information for the Qwen3-TTS models that have already been released. Other models mentioned in the technical report will be released in the near future. Please se