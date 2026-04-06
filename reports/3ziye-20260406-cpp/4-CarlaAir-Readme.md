<h1 align="center">CARLA-Air: Fly Drones Inside a CARLA World</h1>
<h3 align="center">A Unified Infrastructure for Air-Ground Embodied Intelligence</h3>

<p align="center">
  <a href="https://youtu.be/a0fZG2dmT1Q">
    <img src="docs/images/teaser_video.gif" alt="CARLA-Air Teaser — click to watch the full demo" width="100%"/>
  </a>
</p>

**CARLA-Air** is an open-source infrastructure that unifies high-fidelity urban driving and physics-accurate multirotor flight within a single Unreal Engine process, providing a practical simulation foundation for air-ground embodied intelligence research.  

👉 **Get started instantly with our pre-built executable (no compilation required):**  
[Baidu Pan](https://pan.baidu.com/s/1RguWqwKrN-3KEgyKvWiiug?pwd=d5ai) | [Hugging Face](https://huggingface.co/tianlezeng/CarlaAIr-v0.1.7)

<div align="center">
  <a href="https://huggingface.co/papers/2603.28032"><img src="https://img.shields.io/badge/%F0%9F%8F%86%20HF%20Daily%20Papers-%231%20Paper%20of%20the%20Day-FFD700" alt="#1 Paper of the Day"/></a>
  <a href="https://arxiv.org/abs/2603.28032"><img src="https://img.shields.io/badge/Paper-PDF-red" alt="Paper PDF"/></a>
  <a href="https://arxiv.org/abs/2603.28032"><img src="https://img.shields.io/badge/arXiv-2603.28032-b31b1b?logo=arxiv&logoColor=white" alt="arXiv"/></a>
  <a href="https://github.com/louiszengCN/CarlaAir/stargazers"><img src="https://img.shields.io/github/stars/louiszengCN/CarlaAir?style=social" alt="GitHub Stars"/></a>
  <a href="https://github.com/louiszengCN/CarlaAir/releases/tag/v0.1.7"><img src="https://img.shields.io/badge/version-v0.1.7-blue" alt="Version"/></a>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"/>
  <img src="https://img.shields.io/badge/python-3.8+-blue" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/CARLA-0.9.16-green" alt="CARLA 0.9.16"/>
  <img src="https://img.shields.io/badge/AirSim-1.8.1-orange" alt="AirSim 1.8.1"/>
  <img src="https://img.shields.io/badge/platform-Ubuntu%2020.04%20%7C%2022.04-lightgrey" alt="Platform"/>
</div>

<br>

<p align="center">
  <a href="README.md">English</a> | <a href="README_CN.md">简体中文</a> &nbsp;&nbsp;|&nbsp;&nbsp;
  📄 <a href="https://arxiv.org/abs/2603.28032"><b>Paper</b></a> &nbsp;|&nbsp;
  🌐 <a href="#"><b>Project Page</b></a> <i>(coming soon)</i> &nbsp;|&nbsp;
  📖 <a href="CarlaAir_Release/guide/Quick-Start.md"><b>Docs</b></a> &nbsp;|&nbsp;
  🎬 <a href="https://youtu.be/a0fZG2dmT1Q"><b>Video</b></a>
</p>

<p align="center">
  <a href="https://pan.baidu.com/s/1RguWqwKrN-3KEgyKvWiiug?pwd=d5ai"><img src="https://img.shields.io/badge/Baidu%20Pan-Download-2932E1?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyczQuNDggMTAgMTAgMTAgMTAtNC40OCAxMC0xMFMxNy41MiAyIDEyIDJ6Ii8+PC9zdmc+" alt="Baidu Pan"/></a>
  <a href="https://huggingface.co/tianlezeng/CarlaAIr-v0.1.7"><img src="https://img.shields.io/badge/HuggingFace-Download-FFD21E?logo=huggingface&logoColor=black" alt="HuggingFace"/></a>
  <a href="docs/images/wxg.jpg"><img src="https://img.shields.io/badge/WeChat-Group-07C160?logo=wechat&logoColor=white" alt="WeChat Group"/></a>
</p>

## 📌 Table of Contents

- [🔥 News](#news)
- [✨ Highlights](#highlights)
- [🏆 Platform Comparison](#platform-comparison) — 15 simulators, side-by-side
- [🎮 Quick Start](#quick-start) — up and running in 4 steps
- [🐍 One Script, Two Worlds](#one-script-two-worlds) — dual API code examples
- [🔬 Research Directions & Workflows](#research-directions--workflows) — W1–W5 validated workflows
- [⌨️ Flight Controls](#flight-controls)
- [📚 Documentation & Tutorials](#documentation--tutorials) — 8 step-by-step tutorials
- [🗺️ Roadmap](#roadmap)
- [📝 Citation](#citation)
- [📜 License & Acknowledgments](#license--acknowledgments)
- [⭐ Star History](#star-history)

<a id="news"></a>

## 🔥 News

- **[2026-04-01]** 🏆 $\color{red}{\textbf{\\#1 Paper of the Day}}$ **on [Hugging Face Daily Papers](https://huggingface.co/papers/2603.28032)!**
- **[2026-03-30]** 📄 Technical report released -- [Read the paper](https://arxiv.org/abs/2603.28032)
- **[2026-03]** `v0.1.7` released -- VSync fix, stable traffic, one-click env setup, drone recording toolkit, coordinate docs
- **[2026-03]** `v0.1.6` released -- Auto traffic spawn, UE4 native Sweep collision, ground clamping
- **[2026-03]** `v0.1.5` released -- 12-direction collision system, bilingual help overlay (`H`)
- **[2026-03]** `v0.1.4` released -- ROS2 validation (63 topics), first official binary release

---

<a id="highlights"></a>

## ✨ Highlights

| | |
|---|---|
| 🏗️ **Single-Process Composition** | `CARLAAirGameMode` inherits CARLA and composes AirSim. Only 3 upstream files modified (~35 lines). No bridge, no latency. |
| 🎯 **Absolute Coordinate Alignment** | Exact `0.0000 m` error between CARLA (left-handed) and AirSim (NED) coordinate frames