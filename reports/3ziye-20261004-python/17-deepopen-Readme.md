
# DeepOpen:    [中文](https://github.com/deepopen-com/deepopen/blob/main/readme-cn.md)

Open-Source Multilingual System 1 Decision Engine Technical Whitepaper

## Introduction
DeepOpen is a fully open-source non-autoregressive System 1 decision engine built on Laya, purpose-built for structured decision-making scenarios. It breaks away from the conventional token-by-token text generation paradigm of large language models, completing multi-dimensional classification across over 100 languages in a single forward pass. Tested on NVIDIA T4 GPUs, it achieves latency as low as 33ms per single request and only 7.2ms for batch processing. Trained with the strictly correct reward rule RLCD reinforcement learning framework, and equipped with a built-in intelligent router that automatically matches the optimal checkpoint for every incoming request, DeepOpen thoroughly solves the longstanding pain points of traditional LLMs in classification, routing, and scoring scenarios: slow inference speed, high deployment cost, and vulnerability to hallucinations.

## Benchmark Reproduction & Leaderboard Results
We provide fully reproducible training and evaluation pipelines for two widely recognized intent classification benchmarks, allowing users to replicate our state-of-the-art results with one click:
- Banking77: Full reproduction scripts, dataset configurations and pre-trained checkpoints are available at  
  https://github.com/deepopen-com/deepopen/tree/main/banking77
- CLINC150: Complete end-to-end benchmark implementation for intent classification tasks can be accessed at  
  https://github.com/deepopen-com/deepopen/tree/main/clinc150

Core Advantages
- Ultra-Low Latency: Non-autoregressive architecture eliminates iterative token generation, delivering millisecond-level inference for real-time decision services.
- Native Multilingual Support: Out-of-the-box classification capability for 100+ languages without additional fine-tuning for most common scenarios.
- Hallucination-Free Decision Making: The deterministic classification design ensures no arbitrary generated content, making outputs fully reliable for production routing and scoring use cases.
- Optimized GPU Efficiency: Far higher throughput than equivalent autoregressive LLMs on the same hardware, drastically reducing inference cost at scale.

Quick Start

  https://github.com/deepopen-com/deepopen/tree/main/banking77

  benchmark
  
  https://github.com/deepopen-com/deepopen/tree/main/clinc150
  
 
You can then directly run the provided benchmark scripts under the `banking77` and `clinc150` directories to verify performance, or deploy the engine as a local decision service for your own structured scenarios.

License & Contribution
DeepOpen is released under a permissive open-source license, welcoming developers, researchers and enterprise users to contribute improvements, extend supported languages, and adapt the engine for more domain-specific decision workflows.

 


# DeepOpen：开源多语言System 1决策引擎 技术白皮书

DeepOpen 是基于laya的一款完全开源的非自回归System 1决策引擎，专为结构化类型决策场景设计。

## 复现 打榜  banking77

https://github.com/deepopen-com/deepopen/tree/main/banking77


## 复现 打榜  clinc150

https://github.com/deepopen-com/deepopen/tree/main/clinc150


它摒弃了传统大模型逐Token生成文本的模式，在单次前向传递中即可完成100+种语言的多维度类型判断，单请求延迟低至33毫秒、批量处理仅7.2毫秒（T4显卡实测），依托严格正确评分规则RLCD完成强化学习训练，通过内置智能路由器自动为每个请求匹配最优检查点，彻底解决了传统大模型在分类、路由、打分场景下速度慢、成本高、易产生幻觉的痛点。


# 打榜表现

DeepOpen 在两个榜单打榜的初步结果：
模型： Deepopen（改进后的 Laya）
榜单： CLINC150 和 Banking77

![](https://github.com/deepopen-com/deepopen/blob/main/%E6%89%93%E6%A6%9C.png?raw=true)

本地测试： 对照参考成绩，分别位于第 2 位和第 5 位；





## 核心架构与三大检查点

DeepOpen 基于三大独立优化的检查点构建，内置的智能路由器可在亚毫秒内完成输入内容的脚本、语言识别，自动调度对应最优模型，无需开发者手动配置切换规则：
- DeepOpen 英文检查点：基于ModernBERT-large 421M参数训练，支持512上下文窗口，在英文单语种任务中实现39.5毫秒单请求延迟，在英文意图分类、XNLI等基准测试中准确率达到0.783-0.860，专为纯英文高并发决策场景优化。
- DeepOpen-multilingual 多语言检查点：基于mmBERT-base 322M参数训练，支持1024上下文窗口，推理速度比英文模型快2倍，覆盖100+种语言，其中45种语言的准确率超过3倍随机基线，在非拉丁语种下性能远超纯英文模型，13种非英文语言的意图分类准确率达到0.451，是英文检查点的1.47倍。
- DeepOpen-typed-decisions 类型决策检查点：基于ModernBERT-large 421M参数训练，支持1024上下文窗口，专门针对结构化类型决策场景微调，在2000个决策样本的基准测试中，准确率达到0.766，超过TypeSafe Jev 1.13.0的0.727，同时Brier分数低至0.062，是目前开源决策模型中精度领先的方案。

## 核心技术特性

1. 零幻觉非自回归设计：全程不生成任何文本内容，所有输出均为开发者预先定义的结构化类型结果，无需后续解析处理，从根源上杜绝了传统大模型的幻觉问题，输出结果100%符合预设的类型边界。
2. 全链路智能路由机制：在模型前向推理前，通过纯Python实现的语言检测模块，在<0.5毫秒内识别输入内容的脚本类型和所属语言，自动匹配最优检查点，彻底避免了英文模型在非拉丁语种下“高置信度错误”的致命问题——此前纯英文检查点在高棉语任务中准确率为0，却给出95.2%的错误置信度，仅靠置信度阈值完全无法规避风险。
3. 严格校准的概率输出：依托RLCD强化学习框架训练，所有输出的置信度分数具备严格的统计意义，经过域温度校准后，ECE（预期校准误差）低至0.081，远优于同类方案，可直接用于生产环境的自动置信门控流程，高置信度请求直接自动处理，低置信度请求自动流转人工审核。
4. 极致的性能表现：在特斯拉T4显卡上实测，单请求推理仅需32.8毫秒，10题批量处理仅72.3毫秒，单T4显卡最高支持每秒103-332个问题的吞吐量，实测速度是TypeSafe Jev的7.8倍。
5. 完全开源零成本部署：采用Apache 2.0开源许可，所有权重完全开放，支持本地自托管，无需调用任何付费API，不存在按Token计费的额外成本，对比TypeSafe Jev每百万Token 0.042美元的定价，长期大规模部署可节省近100%的推理成本。

快速上手部署流程
1. 安装依赖包
直接通过PyPI一键安装最新版本：
```bash
pip install deepopen
```

2. 推荐路由模式（开箱即用）
通过内置Router入口点，自动完成语言检测和模型调度，预加载所有检查点后即可实现亚毫秒级路由切换：
```python
import deepopen
from deepopen import Router

将所有检