<a name="readme-top"></a>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/img/logo.png">
    <img alt="AgentFlow" src="assets/img/logo.png" width=31%>
  </picture>
</p>

<h3 align="center">
AgentFlow: In-the-Flow Agentic System Optimization
</h3>


<!--- BADGES: START --->
<p align="center">
    <a href="https://arxiv.org/abs/2510.05592"><img src="https://img.shields.io/badge/arXiv-2510.05592-B31B1B.svg?logo=arxiv" alt="Arxiv"></a>
    <a href="https://huggingface.co/spaces/AgentFlow/agentflow"><img src="https://img.shields.io/badge/Gradio-Demo-F97316.svg?logo=gradio" alt="Gradio Demo"></a>
    <a href="https://huggingface.co/papers/2510.05592"><img src="https://img.shields.io/badge/Huggingface-Paper-FFD21E.svg?logo=huggingface" alt="Huggingface Paper"></a>
    <a href="https://huggingface.co/AgentFlow"><img src="https://img.shields.io/badge/Huggingface-Model-FFD21E.svg?logo=huggingface" alt="Huggingface Model"></a>
    <a href="https://agentflow.stanford.edu/"><img src="https://img.shields.io/badge/Website-AgentFlow-E5426E?logo=kashflow" alt="Website"></a>
    <a href="https://x.com/lupantech/status/1976016000345919803"><img src="https://img.shields.io/badge/Coverage-AgentFlow-2176BC.svg?logo=x" alt="X"></a>
    <a href="https://www.youtube.com/watch?v=kIQbCQIH1SI"><img src="https://img.shields.io/badge/YouTube-Tutorial-FF0000?logo=youtube" alt="Youtube"></a>
    <a href="https://join.slack.com/t/agentflow-co/shared_invite/zt-3f712xngl-LfxS4gmftAeKvcxR3nSkWQ"><img src="https://img.shields.io/badge/Slack-AgentFlow-D41544.svg?logo=slack" alt="Slack"></a>
    <a href="https://github.com/lupantech/AgentFlow/blob/main/assets/img/wechat_group.jpg">
  <img src="https://img.shields.io/badge/Wechat-AgentFlow-07C160.svg?logo=wechat" alt="Wechat AgentFlow">
</a>
  
  </p>
<!--- BADGES: END --->


## 📣 News
- **[2025.10.16]** 🏆 Our paper has been accepted by [**NeurIPS 2025 Efficient Reasoning Workshop**](https://efficient-reasoning.github.io/)!
- **[2025.10.13]** 📸 Excited to have a tutorial video for AgentFlow covered by Discover AI on **[YouTube](https://www.youtube.com/watch?v=kIQbCQIH1SI)**!
- **[2025.10.10]** 🚀 Our X [post](https://x.com/lupantech/status/1976016000345919803) received **1K+ likes**! Feel free to check out the post and join the discussion! 💬
- **[2025.10.08]** 🔥 We are honored to be featured as 🤗 HuggingFace **[Daily Paper #2](https://huggingface.co/papers/2510.05592)**.

## 🌟 Why AgentFlow?
AgentFlow is a **trainable, tool-integrated agentic framework** designed to overcome the **scalability** and **generalization limits** of today’s tool-augmented reasoning approaches. 

Unlike prevailing approaches such as [Search-R1](https://github.com/PeterGriffinJin/Search-R1) which train a **single LLM** to interleave reasoning steps with tool calls, **AgentFlow** introduces a **modular agentic system** with four specialized modules: 🧭 **Planner**, 🛠 **Executor**, ✅ **Verifier**, and ✍️ **Generator**.

![framework_overall](assets/img/framework.png)

For effective planning and tool use, the framework directly **optimizes planner agent within the system** in an **online fashion** using **Flow-based Group Refined Policy Optimization (Flow-GRPO)**, achieving superior performance across diverse domains with improved tool-calling reliability and long-horizon reasoning capabilities.

![flow_grpo](assets/img/flow_grpo.png)

## 📺 YouTube Tutorial
Excited to have a tutorial video for AgentFlow covered by [Discover AI](https://www.youtube.com/@code4AI) on YouTube!

<!-- [![AgentFlow Tutorial](https://img.youtube.com/vi/kIQbCQIH1SI/0.jpg)](https://www.youtube.com/watch?v=kIQbCQIH1SI) -->

<div align="center">
  <a href="https://www.youtube.com/watch?v=kIQbCQIH1SI">
    <img src="https://img.youtube.com/vi/kIQbCQIH1SI/maxresdefault.jpg" alt="AgentFlow Tutorial" width="100%">
  </a>
</div>


## 🚀 Key Features

- 🧩 **Modular Agentic System** – Four specialized agent modules (**Planner**, **Executor**, **Verifier**, **Generator**) that coordinate via evolving memory and integrated tools across multiple turns.  
- 🔗 **Multi-Tool Integration** – Seamlessly connect with diverse tool ecosystems, including `base_generator`, `python_coder`, `google_search`, `wikipedia_search`, `web_search`, and more.  
- 🎯 **Flow-GRPO Algorithm** – Enables **in-the-flow agent optimization** for **long-horizon reasoning tasks** with sparse rewards.
- 📈 **Proven Results** – **AgentFlow (7B Backbone)** beats top baselines on 10 benchmarks, with **+14.9% search**, **+14.0% agentic**, **+14.5% math**, **+4.1% science**, even outperforming ~200B-parameter **GPT-4o**.

## 🏆 Experiments

### 📊 Main Results
**AgentFlow (Qwen-2.5-7B-Instruct Backbone)** outperforms top baselines on 10 benchmarks:  
- **+14.9%** on search  
- **+14.0%** on agentic reasoning  
- **+14.5%** on math  
- **+4.1%** on science  

💡 Even surpasses larger proprietary models like **GPT-4o (~200B)**.

![main_table1](assets/img/maintabl