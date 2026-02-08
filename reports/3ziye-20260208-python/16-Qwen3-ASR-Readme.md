# Qwen3-ASR

<br>

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-ASR-Repo/logo.png" width="400"/>
<p>

<p align="center">
&nbsp&nbsp🤗 <a href="https://huggingface.co/collections/Qwen/qwen3-asr">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/collections/Qwen/Qwen3-ASR">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://qwen.ai/blog?id=qwen3asr">Blog</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://arxiv.org/abs/2601.21337">Paper</a>&nbsp&nbsp
<br>
🖥️ <a href="https://huggingface.co/spaces/Qwen/Qwen3-ASR">Hugging Face Demo</a>&nbsp&nbsp | &nbsp&nbsp 🖥️ <a href="https://modelscope.cn/studios/Qwen/Qwen3-ASR">ModelScope Demo</a>&nbsp&nbsp | &nbsp&nbsp💬 <a href="https://github.com/QwenLM/Qwen/blob/main/assets/wechat.png">WeChat (微信)</a>&nbsp&nbsp | &nbsp&nbsp🫨 <a href="https://discord.gg/CV4E9rpNSD">Discord</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://help.aliyun.com/zh/model-studio/qwen-speech-recognition">API</a>

</p>

We release **Qwen3-ASR**, a family that includes two powerful all-in-one speech recognition models that support language identification and ASR for 52 languages and dialects, as well as a novel non-autoregressive speech forced-alignment model that can align text–speech pairs in 11 languages.


## News
* 2026.1.29: 🎉🎉🎉 We have released the [Qwen3-ASR](https://huggingface.co/collections/Qwen/qwen3-asr) series (0.6B/1.7B) and the Qwen3-ForcedAligner-0.6B model. Please check out our [blog](https://qwen.ai/blog?id=qwen3asr)!


## Contents <!-- omit in toc -->

- [Overview](#overview)
  - [Introduction](#introduction)
  - [Model Architecture](#model-architecture)
  - [Released Models Description and Download](#released-models-description-and-download)
- [Quickstart](#quickstart)
  - [Environment Setup](#environment-setup)
  - [Python Package Usage](#python-package-usage)
    - [Quick Inference](#quick-inference)
    - [vLLM Backend](#vllm-backend)
    - [Streaming Inference](#streaming-inference)
    - [ForcedAligner Usage](#forcedaligner-usage)
  - [DashScope API Usage](#dashscope-api-usage)
- [Launch Local Web UI Demo](#launch-local-web-ui-demo)
  - [Gradio Demo](#gradio-demo)
  - [Streaming Demo](#streaming-demo)
- [Deployment with vLLM](#deployment-with-vllm)
- [Fine Tuning](#fine-tuning)
- [Docker](#docker)
- [Evaluation](#evaluation)
- [Citation](#citation)


## Overview

### Introduction

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-ASR-Repo/qwen3_asr_introduction.png" width="90%"/>
<p>

The Qwen3-ASR family includes Qwen3-ASR-1.7B and Qwen3-ASR-0.6B, which support language identification and ASR for 52 languages and dialects. Both leverage large-scale speech training data and the strong audio understanding capability of their foundation model, Qwen3-Omni. Experiments show that the 1.7B version achieves state-of-the-art performance among open-source ASR models and is competitive with the strongest proprietary commercial APIs. Here are the main features:

* **All-in-one**: Qwen3-ASR-1.7B and Qwen3-ASR-0.6B support language identification and speech recognition for 30 languages and 22 Chinese dialects, so as to English accents from multiple countries and regions.

* **Excellent and Fast**: The Qwen3-ASR family ASR models maintains high-quality and robust recognition under complex acoustic environments and challenging text patterns. Qwen3-ASR-1.7B achieves strong performance on both open-sourced and internal benchmarks. While the 0.6B version achieves accuracy-efficient trade-off, it reaches 2000 times throughput at a concurrency of 128. They both achieve streaming / offline unified inference with single model and support transcribe long audio.

* **Novel and strong forced alignment Solution**: We introduce Qwen3-ForcedAligner-0.6B, which supports timestamp prediction for arbitrary units within up to 5 minutes of speech in 11 languages. Evaluations show its timestamp accuracy surpasses E2E based forced-alignment models.

* **Comprehensive inference toolkit**: In addition to open-sourcing the architectures and weights of the Qwen3-ASR series, we also release a powerful, full-featured inference framework that supports vLLM-based batch inference, asynchronous serving, streaming inference, timestamp prediction, and more.

### Model Architecture

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-ASR-Repo/overview.jpg" width="100%"/>
<p>


### Released Models Description and Download

Below is an introduction and download information for the Qwen3-ASR models. Please select and download the model that fits your needs.

| Model | Supported Languages | Supported Dialects | Inference Mode | Audio Types |
|---|---|---|---|---|
| Qwen3-ASR-1.7B & Qwen3-ASR-0.6B | Chinese (zh), English (en), Cantonese (yue), Arabic (ar), German (de), French (fr), Spanish (es), Portuguese (pt), Indonesian (id), Italian (it), Korean (ko), Russian (ru), Thai (th), Vietnamese (vi), Japan