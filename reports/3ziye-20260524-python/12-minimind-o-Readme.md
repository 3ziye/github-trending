<div align="center">

![logo](./images/logo.png)

</div>


<div align="center">

![visitors](https://visitor-badge.laobi.icu/badge?page_id=jingyaogong/minimind-o)
[![GitHub Repo stars](https://img.shields.io/github/stars/jingyaogong/minimind-o?style=social)](https://github.com/jingyaogong/minimind-o/stargazers)
[![GitHub Code License](https://img.shields.io/github/license/jingyaogong/minimind-o?v=1)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/jingyaogong/minimind-o)](https://github.com/jingyaogong/minimind-o/commits/master)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/jingyaogong/minimind-o/pulls)
[![Collection](https://img.shields.io/badge/🤗-MiniMind--O%20%20Collection-blue)](https://huggingface.co/collections/jingyaogong/minimind-o)
[![Technical Report](https://img.shields.io/badge/Technical%20Report-arXiv-red)](http://arxiv.org/abs/2605.03937)

</div>

<div align="center">
  <h3>"大道至简"</h3>
</div>

<div align="center">

中文 | [English](./README_en.md)

</div>

* 此开源项目旨在从 0 完整实现一个小规模的端到端 Omni 模型，单一权重同时支持文 / 音 / 图三模态输入与文本 / 流式语音输出。
* 其中 `minimind-3o` 仅 ~0.1B，普通个人 GPU 即可完成训练、CPU即可快速推理，是当前公开模型中规模最小的完整 Omni 实现（或之一）。
* 开源 mini 与 full 两套训练数据：mini 单卡 3090 上约 2 小时跑通完整链路，便于入门；full 与发布权重对应。
* 开源 Omni 模型的完整代码与技术报告，覆盖 Thinker–Talker 双路径、流式语音生成、实时打断、近似双工交互、音色克隆与电话模式 WebUI。
* 所有核心算法代码均从 0 使用 PyTorch 原生实现，不依赖三方框架提供的高层抽象。
* MiniMind-O 进一步延续了 [MiniMind](https://github.com/jingyaogong/minimind)（语言）与 [MiniMind-V](https://github.com/jingyaogong/minimind-v)（视觉多模态）的设计范式。

> 注："约 2 小时" 指 mini 数据集在单张 NVIDIA RTX 3090 上跑完 SFT 的实测耗时。

---

<div align="center">

[📄 MiniMind-O Technical Report](http://arxiv.org/abs/2605.03937)

https://github.com/user-attachments/assets/10cbcc5f-4e70-45cf-bdc5-d6361e40bb86

[🔗 在线体验 (Gradio)](https://modelscope.cn/studios/gongjy/MiniMind-O) &nbsp;|&nbsp; [🔗 视频介绍](https://www.bilibili.com/video/BV1V1RsBcEMX)


</div>

---

# 📌 项目介绍

继 [MiniMind](https://github.com/jingyaogong/minimind)（LLM）和 [MiniMind-V](https://github.com/jingyaogong/minimind-v)（VLM）之后，MiniMind-O 是这个系列的第三站。所谓 Omni，就是让一个模型同时具备听、看、说的多模态交互能力：接收文本、语音和视觉信号，输出文本与流式语音。

或许 GPT-4o 让人第一次感受到足够自然的流式语音交互形态，随后 Mini-Omni2、Moshi、GLM-4-Voice、Qwen3-Omni 等开源工作陆续出现。但如果目标不是直接调用这些参数庞大的现成权重，而是从 0 读懂、训练、改动一个完整 Omni 模型，开源社区仍然急缺足够轻量、链路完整的起点。要把语音真正纳入 Omni 模型，一种做法是把 ASR、LLM、TTS 串成级联链路：语音先转文字，LLM 处理后再合成语音。这条路工程上直接，但中间多了一次文本转写，延迟、语气和情绪信息都会受到影响。

MiniMind-O 尝试补上已知的空位：让语音和文本在 hidden state 层面直接连通，在主 backbone 仅 0.1B 的规模下保留端到端 Omni 链路。Talker 侧采用 MTP（Multi-Token Prediction）一次预测多层 Mimi codes，再配合 VAD 支持实时打断与近似双工交互，这是足够实用的工程路线之一。本项目的代码、模型权重、训练数据和技术报告全部完整开源，单张 RTX 3090 上约 2 小时即可跑通 mini 数据集训练。目标依旧：让每个人都能从第一行代码读起，自己动手，从 0 训练一个能听、能看、能思考、能说的模型：

![](images/omni_io_flow.png)

😊 一起感受创造的乐趣吧！

---

#### 🎉 项目包含以下内容

- 提供完整的 MiniMind-O 结构代码：Thinker、独立 Talker、audio / vision projector、Mimi codebook 接口以及 MTP audio head。
- 提供 SFT 全链路训练流程，覆盖 T2A、I2T、A2A 三类数据，支持全参数训练、音频投影层训练、视觉投影层训练与 DDP 多卡训练。
- 提供 mini 与 full 两套训练数据：mini 便于快速入门，单卡 3090 上约 2 小时可跑通；full 与发布权重对应，覆盖中文语音与图像任务。
- 提供多种内置音色、unseen 音色与任意参考音频的音色克隆能力，便于复现音色控制实验。
- 提供完整的推理与 Demo 工具，支持 CLI 推理、Web UI、流式播放、barge-in 打断和电话模式。
- 关键模块均从 0 用 PyTorch 原生实现，不依赖三方高层封装；同时兼容 `transformers` Tokenizer 与原生权重格式。
- 配套技术报告覆盖架构、训练曲线、CER / WER 评估、音色克隆相似度与跨模型对比，链接见顶部 Tech Report 区。

#### 🎉 已发布模型列表

| 模型 | 参数（主干） | Release |
|---|---|---|
| minimind-3o | ~0.1B | 2026.05.05 |
| minimind-3o-moe | ~0.3B-A0.1B | 2026.05.05 |

---

#### 👉 更新日志

<details close>
<summary> <b>🔥 2026-05-05</b> </summary>

- MiniMind-O 首次开源，发布 `minimind-3o`（115M）与 `minimind-3o-moe`（312M-A115M）
- Thinker–Talker 双路径架构，Talker 采用 MTP 预测多层 Mimi codes，支持 24 kHz 流式语音生成与 barge-in 打断
- 音频编解码器采用 Mimi（8 层 codebook，12.5 Hz，24 kHz），Talker 在 codebook 接口上使用共享主体与轻量 adapter
- 语音 / 视觉特征分别由冻结的 SenseVoice-Small 与 SigLIP2 编码，再通过两层 MLP projector 注入 MiniMind 隐空间
- 同步发布 mini 与 full 两套训练数据，mini 单卡 3090 ~2h 即可跑通整条 Thinker–Talker 链路
- 内置 5 个 voice prompt + 7 个 unseen voice prompt，提供音色克隆与电话模式 WebUI

</details>


# 📌 快速开始

<details style="color:rgb(128,128,128)">
<summary>分享本人的软硬件配置（仅供参考）</summary>

* CPU: Intel(R) Core(TM) i9-10980XE CPU @ 3.00GHz
* RAM: 128 GB
* GPU: NVIDIA GeForce RTX 3090(24GB) * 8
* Ubuntu==20.04
* CUDA==12.2
* Python==3.10
* [requirements.txt](./requirements.txt)

</details>

## 第0步（必须）

### 1' 环境准备

```bash
# 克隆仓库代码
git clone --depth 1 https://github.com/jingyaogong/minimind-o
# 安装必要依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 2' 下载资源

```bash
# 下载 SenseVoice-Small 语音编码器到 ./model/SenseVoiceSmall
modelscope download --model gongjy/SenseVoiceSmall --local_dir ./model/SenseVoiceSmall
# 下载 SigLIP2 视觉编码器到 ./model/siglip2-base-p32-256-ve
modelscope download --model gongjy/siglip2-base-p32-256-ve --local_dir ./model/siglip2-base-p32-256-ve
# 下载 Mimi 音频编解码器到 ./model/mimi
modelscope download --model gongjy/mimi --local_dir ./model/mimi
# 下载 CAMPPlus 说话人编码器到 ./model/campplus
modelscope download --model gongjy/campplus --local_dir ./model/campplus
# 下载 MiniMind 语言模型权重到 ./out 目录下（作为