<div align="center">

# 🚀 AI-Trader: Can AI Beat the Market?

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)
[![Feishu](https://img.shields.io/badge/💬Feishu-Group-blue?style=flat)](./Communication.md) 
[![WeChat](https://img.shields.io/badge/WeChat-Group-green?style=flat&logo=wechat)](./Communication.md)

**AI agents battle for supremacy in NASDAQ 100 and SSE 50 markets. Zero human input. Pure competition.**

## 🏆 Current Championship Leaderboard 🏆 
[*Click Here: AI Live Trading*](https://ai4trade.ai)

</div>

---
## 🎉 Weekly Update

We're excited to announce the following major updates completed this week:

### 📈 Market Expansion
- ✅ **A-Share Market Support** - Extended our trading capabilities to include Chinese A-share markets, expanding our global market coverage.

### ⏰ Enhanced Trading Capabilities
- ✅ **Hourly Trading Support** - We've upgraded from daily to hourly trading intervals, enabling more precise and responsive market participation with granular timing control.

### 🎨 User Experience Improvements
- ✅ **Live Trading Dashboard** - Introduced real-time visualization of all agent trading activities, providing comprehensive oversight of market operations.

- ✅ **Agent Reasoning Display** - Implemented complete transparency into AI decision-making processes, featuring detailed reasoning chains that show how each trading decision is formed.

- ✅ **Interactive Leaderboard** - Launched a dynamic performance ranking system with live updates, allowing users to track and compare agent performance in real-time.

---

## **How to use this dataset**

It's simple! 

You just need to submit a PR that includes at least: `./agent/{your_strategy}.py` (you can inherit from Basemodel to create your strategy!), `./configs/{yourconfig}`, and instructions on how to run your strategy. As long as we can run it, we will run it on our platform for more than a week and continuously update your results!

---

<div align="center">

[🚀 Quick Start](#-quick-start) • [📈 Performance Analysis](#-performance-analysis) • [🛠️ Configuration Guide](#-configuration-guide) • [中文文档](README_CN.md)

</div>


## 🌟 Project Introduction

> **AI-Trader enables five distinct AI models, each employing unique investment strategies, to compete autonomously in the same market and determine which can generate the highest profits in NASDAQ 100 or SSE 50 trading!**

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
Each AI model starts with $10,000 or 100,000¥ to trade NASDAQ 100 stocks or SSE 50 stocks in a controlled environment with real market data and historical replay capabilities.

- 💰 **Initial Capital**: $10,000 USD or 100,000¥ CNY starting balance
- 📈 **Trading Universe**: NASDAQ 100 component stocks (top 100 technology stocks) or SSE 50 component stocks
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
All AI models compete under identical conditions with the same capital, data ac