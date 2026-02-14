<div align="center">
  <img src="assets/logo.jpg" alt="PicoClaw" width="512">

  <h1>PicoClaw: Ultra-Efficient AI Assistant in Go</h1>

  <h3>$10 Hardware · 10MB RAM · 1s Boot · 皮皮虾，我们走！</h3>

  <p>
    <img src="https://img.shields.io/badge/Go-1.21+-00ADD8?style=flat&logo=go&logoColor=white" alt="Go">
    <img src="https://img.shields.io/badge/Arch-x86__64%2C%20ARM64%2C%20RISC--V-blue" alt="Hardware">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
    <br>
    <a href="https://picoclaw.io"><img src="https://img.shields.io/badge/Website-picoclaw.io-blue?style=flat&logo=google-chrome&logoColor=white" alt="Website"></a>
    <a href="https://x.com/SipeedIO"><img src="https://img.shields.io/badge/X_(Twitter)-SipeedIO-black?style=flat&logo=x&logoColor=white" alt="Twitter"></a>
  </p>

 [中文](README.zh.md) | [日本語](README.ja.md) | **English**
</div>


---

🦐 PicoClaw is an ultra-lightweight personal AI Assistant inspired by [nanobot](https://github.com/HKUDS/nanobot), refactored from the ground up in Go through a self-bootstrapping process, where the AI agent itself drove the entire architectural migration and code optimization.

⚡️ Runs on $10 hardware with <10MB RAM: That's 99% less memory than OpenClaw and 98% cheaper than a Mac mini!


<table align="center">
  <tr align="center">
    <td align="center" valign="top">
      <p align="center">
        <img src="assets/picoclaw_mem.gif" width="360" height="240">
      </p>
    </td>
    <td align="center" valign="top">
      <p align="center">
        <img src="assets/licheervnano.png" width="400" height="240">
      </p>
    </td>
  </tr>
</table>


> [!CAUTION]
> **🚨 SECURITY & OFFICIAL CHANNELS / 安全声明**
>
> * **NO CRYPTO:** PicoClaw has **NO** official token/coin. All claims on `pump.fun` or other trading platforms are **SCAMS**.
> * **OFFICIAL DOMAIN:** The **ONLY** official website is **[picoclaw.io](https://picoclaw.io)**, and company website is **[sipeed.com](https://sipeed.com)**
> * **Warning:** Many `.ai/.org/.com/.net/...` domains are registered by third parties. 
>

## 📢 News
2026-02-13 🎉 PicoClaw hit 5000 stars in 4days! Thank you for the community! There are so many PRs&issues come in (during Chinese New Year holidays), we are finalizing the Project Roadmap and setting up the Developer Group to accelerate PicoClaw's development.  
🚀 Call to Action: Please submit your feature requests in GitHub Discussions. We will review and prioritize them during our upcoming weekly meeting.


2026-02-09 🎉 PicoClaw Launched! Built in 1 day to bring AI Agents to $10 hardware with <10MB RAM. 🦐 PicoClaw，Let's Go！

## ✨ Features

🪶 **Ultra-Lightweight**: <10MB Memory footprint — 99% smaller than Clawdbot - core functionality.

💰 **Minimal Cost**: Efficient enough to run on $10 Hardware — 98% cheaper than a Mac mini.

⚡️ **Lightning Fast**: 400X Faster startup time, boot in 1 second even in 0.6GHz single core.

🌍 **True Portability**: Single self-contained binary across RISC-V, ARM, and x86, One-click to Go!

🤖 **AI-Bootstrapped**: Autonomous Go-native implementation — 95% Agent-generated core with human-in-the-loop refinement.

|                               | OpenClaw      | NanoBot                  | **PicoClaw**                              |
| ----------------------------- | ------------- | ------------------------ | ----------------------------------------- |
| **Language**                  | TypeScript    | Python                   | **Go**                                    |
| **RAM**                       | >1GB          | >100MB                   | **< 10MB**                                |
| **Startup**</br>(0.8GHz core) | >500s         | >30s                     | **<1s**                                   |
| **Cost**                      | Mac Mini 599$ | Most Linux SBC </br>~50$ | **Any Linux Board**</br>**As low as 10$** |

<img src="assets/compare.jpg" alt="PicoClaw" width="512">

## 🦾 Demonstration

### 🛠️ Standard Assistant Workflows

<table align="center">
  <tr align="center">
    <th><p align="center">🧩 Full-Stack Engineer</p></th>
    <th><p align="center">🗂️ Logging & Planning Management</p></th>
    <th><p align="center">🔎 Web Search & Learning</p></th>
  </tr>
  <tr>
    <td align="center"><p align="center"><img src="assets/picoclaw_code.gif" width="240" height="180"></p></td>
    <td align="center"><p align="center"><img src="assets/picoclaw_memory.gif" width="240" height="180"></p></td>
    <td align="center"><p align="center"><img src="assets/picoclaw_search.gif" width="240" height="180"></p></td>
  </tr>
  <tr>
    <td align="center">Develop • Deploy • Scale</td>
    <td align="center">Schedule • Automate • Memory</td>
    <td align="center">Discovery • Insights • Trends</td>
  </tr>
</table>

### 🐜 Innovative Low-Footprint Deploy

PicoClaw can be deployed on almost any Linux device!

- $9.9 [LicheeRV-Nano](https://www.aliexpress.com/item/1005006519668532.html) E(Ethernet) or W(WiFi6) version, for Minimal Home 