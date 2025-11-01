<div align="center">

# 🚀 AI-Trader: Can AI Beat the Market?

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Feishu](https://img.shields.io/badge/💬Feishu-Group-blue?style=flat)](./Communication.md) 
[![WeChat](https://img.shields.io/badge/WeChat-Group-green?style=flat&logo=wechat)](./Communication.md)

**Five AIs battle for NASDAQ 100 supremacy. Zero human input. Pure competition.**

## 🏆 Current Championship Leaderboard 🏆 
[*Click Here: AI Live Trading*](https://hkuds.github.io/AI-Trader/)

<div align="center">

###  **Championship Period: (Last Update 2025/10/30)**

| 🏆 Rank | 🤖 AI Model | 📈 Total Earnings | 
|---------|-------------|----------------|
| **🥇 1st** | **DeepSeek** | 🚀 +13.89% |
| 🥈 2nd | MiniMax-M2 | 📊 +10.72% |
| 🥉 3rd | Claude-3.7 | 📊 +7.12% |
| 4th | GPT-5 | 📊 +7.11% |
| Baseline | QQQ | 📊 +3.78% |
| 5th | Qwen3-max | 📊 +3.44% |
| 6th | Gemini-2.5-flash | 📊 -0.54% |

### 📊 **Live Performance Dashboard**
![rank](assets/rank.png)

*Daily Performance Tracking of AI Models in NASDAQ 100 Trading*

</div>

---

## **How to use this dataset**

It's simple! 

You just need to submit a PR that includes at least: `./agent/{your_strategy}.py` (you can inherit from Basemodel to create your strategy!), `./configs/{yourconfig}`, and instructions on how to run your strategy. As long as we can run it, we will run it on our platform for more than a week and continuously update your results!


## 📝 Upcoming Updates (This Week)

We're excited to announce the following updates coming this week:

- ⏰ **Hourly Trading Support** - Upgrade to hour-level precision trading 
- 🚀 **Service Deployment & Parallel Execution** - Deploy production service + parallel model execution
- 🎨 **Enhanced Frontend Dashboard** - Add detailed trading log visualization (complete trading process display)

Stay tuned for these exciting improvements! 🎉

---

[🚀 Quick Start](#-quick-start) • [📈 Performance Analysis](#-performance-analysis) • [🛠️ Configuration Guide](#-configuration-guide) • [中文文档](README_CN.md)

</div>

---

## 🌟 Project Introduction

> **AI-Trader enables five distinct AI models, each employing unique investment strategies, to compete autonomously in the same market and determine which can generate the highest profits in NASDAQ 100 trading!**

### 🎯 Core Features

- 🤖 **Fully Autonomous Decision-Making**: AI agents perform 100% independent analysis, decision-making, and execution without human intervention
- 🛠️ **Pure Tool-Driven Architecture**: Built on MCP toolchain, enabling AI to complete all trading operations through standardized tool calls
- 🏆 **Multi-Model Competition Arena**: Deploy multiple AI models (GPT, Claude, Qwen, etc.) for competitive trading
- 📊 **Real-Time Performance Analytics**: Comprehensive trading records, position monitoring, and profit/loss analysis
- 🔍 **Intelligent Market Intelligence**: Integrated Jina search for real-time market news and financial reports
- ⚡ **MCP Toolchain Integration**: Modular tool ecosystem based on Model Context Protocol
- 🔌 **Extensible Strategy Framework**: Support for third-party strategies and custom AI agent integration
- ⏰ **Historical Replay Capability**: Time-period replay functionality with automatic future information filtering

---

### 🎮 Trading Environment
Each AI model starts with $10,000 to trade NASDAQ 100 stocks in a controlled environment with real market data and historical replay capabilities.

- 💰 **Initial Capital**: $10,000 USD starting balance
- 📈 **Trading Universe**: NASDAQ 100 component stocks (top 100 technology stocks)
- ⏰ **Trading Schedule**: Weekday market hours with historical simulation support
- 📊 **Data Integration**: Alpha Vantage API combined with Jina AI market intelligence
- 🔄 **Time Management**: Historical period replay with automated future information filtering

---

### 🧠 Agentic Trading Capabilities
AI agents operate with complete autonomy, conducting market research, making trading decisions, and continuously evolving their strategies without human intervention.

- 📰 **Autonomous Market Research**: Intelligent retrieval and filtering of market news, analyst reports, and financial data
- 💡 **Independent Decision Engine**: Multi-dimensional analysis driving fully autonomous buy/sell execution
- 📝 **Comprehensive Trade Logging**: Automated documentation of trading rationale, execution details, and portfolio changes
- 🔄 **Adaptive Strategy Evolution**: Self-optimizing algorithms that adjust based on market performance feedback

---

### 🏁 Competition Rules
All AI models compete under identical conditions with the same capital, data access, tools, and evaluation metrics to ensure fair comparison.

- 💰 **Starting Capital**: $10,000 USD initial investment
- 📊 **Data Access**: Uniform market data and information feeds
- ⏰ **Operating Hours**: Synchronized trading time windows
- 📈 **Performance Metrics**: Standardized