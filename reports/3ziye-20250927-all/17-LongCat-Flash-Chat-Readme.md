# LongCat-Flash-Chat

<div align="center">
  <img src="figures/longcat_logo.svg" width="45%" alt="LongCat-Flash" />
</div>
<hr>

<div align="center" style="line-height: 1;">
  <a href="https://longcat.ai/" target="_blank" style="margin: 2px;">
    <img alt="Chat" src="https://img.shields.io/badge/🤖%20Chat-LongCat--Flash--Chat-ADFF2F?color=29E154&logoColor=white"  fill-opacity="1" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://huggingface.co/meituan-longcat" target="_blank" style="margin: 2px;">
    <img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-LongCat-ffc107?color=ffc107&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<div align="center" style="line-height: 1;">
  <a href="https://github.com/meituan-longcat/LongCat-Flash-Chat/blob/main/figures/wechat_official_accounts.png" target="_blank" style="margin: 2px;">
    <img alt="Wechat" src="https://img.shields.io/badge/WeChat-LongCat-brightgreen?logo=wechat&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://x.com/Meituan_LongCat" target="_blank" style="margin: 2px;">
    <img alt="Twitter Follow" src="https://img.shields.io/badge/Twitter-LongCat-white?logo=x&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<div align="center" style="line-height: 1;">
  <a href="LICENSE" style="margin: 2px;">
    <img alt="License" src="https://img.shields.io/badge/License-MIT-f5de53?&color=f5de53" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<p align="center">
  <a href="https://arxiv.org/abs/2509.01322"><b>Tech Report</b>&nbsp;📄</a>
</p>

## Model Introduction
We introduce LongCat-Flash, a powerful and efficient language model with 560 billion total parameters, featuring an innovative Mixture-of-Experts (MoE) architecture. The model incorporates a dynamic computation mechanism that activates 18.6B∼31.3B parameters (averaging∼27B) based on contextual demands, optimizing both computational efficiency and performance. To achieve advanced training and inference efficiency, we employ a shortcut-connected architecture that expands computation-communication overlap window, achieving over 100 tokens per second (TPS) for inference cost-effectively. Our comprehensive training and scaling strategies ensure stable, efficient training, while tailored data strategies enhance model performance.

Now we release LongCat-Flash-Chat, a non-thinking foundation model that delivers highly competitive performance among leading models, with exceptional strengths in agentic tasks.


### Key Features

#### 🌟 Scalable Architectural Design for Computational Efficiency

LongCat-Flash is designed and optimized under two key principles: efficient computation utilization, as well as  efficient training and inference. Specifically, (1) As not all tokens are equal, we introduce the zero-computation experts mechanism in MoE blocks to allocate a dynamic computation budget to important tokens based on their significance, i.e., activating 18.6 to 31.3 billion parameters (out of 560 billion total) based on contextual demands. To ensure consistent computation load, we employ expert bias adjusted by a PID-controller, maintaining an average of∼27 billion activated parameters per token. (2) As communication overhead becomes a bottleneck during MoE model scaling, we incorporate the Shortcut-connected MoE (ScMoE) design to expand the computation-communication overlap window. Combined with customized infrastructure optimizations, this design enables training at a massive scale of over tens of thousands accelerators and inference with high throughput and low latency.


#### 🌟 Effective Model Scaling Strategy

Effectively and efficiently scaling model size remains a key challenge in strategy design. To this end, we develop a comprehensive stability-and-scaling framework for robustly training large-scale models: (1) We successfully apply a hyperparameter transfer strategy to such a large model, predicting optimal hyperparameter configurations by leveraging results from smaller proxy models with theoretical guarantees. (2) We initialize the model using a model-growth mechanism based on a refined half-scale checkpoint, achieving improved performance compared to conventional initialization methods. (3) A multi-pronged stability suite incorporates principled router-gradient balancing, a hidden z-loss to suppress massive activations, and fine-tuned optimizer configurations. (4) To enhance the reliability of large-scale cluster training, we introduce deterministic computation. This guarantees the exact reproducibility of experiments and enables the detection of SDC (Silent Data Corruption) during the training process. These interventions ensure that LongCat-Flash ’s training remains stable, with no irrecoverable loss spikes.

#### 🌟 Multi-Stage Training Pipeline for Agentic Capability
Through a metic