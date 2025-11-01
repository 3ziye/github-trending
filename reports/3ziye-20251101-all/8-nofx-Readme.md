# 🤖 NOFX - AI-Driven Crypto Futures Auto Trading Competition System

[![Go Version](https://img.shields.io/badge/Go-1.21+-00ADD8?style=flat&logo=go)](https://golang.org/)
[![React](https://img.shields.io/badge/React-18+-61DAFB?style=flat&logo=react)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6?style=flat&logo=typescript)](https://www.typescriptlang.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Languages:** [English](README.md) | [中文](README.zh-CN.md) | [Українська](README.uk.md) | [Русский](README.ru.md)

---

An automated crypto futures trading system powered by **DeepSeek/Qwen AI**, supporting **Binance, Hyperliquid, and Aster DEX exchanges**, **multi-AI model live trading competition**, featuring comprehensive market analysis, AI decision-making, **self-learning mechanism**, and professional Web monitoring interface.

> ⚠️ **Risk Warning**: This system is experimental. AI auto-trading carries significant risks. Strongly recommended for learning/research purposes or testing with small amounts only!

## 👥 Developer Community

Join our Telegram developer community to discuss, share ideas, and get support:

**💬 [NOFX Developer Community](https://t.me/nofx_dev_community)**

---

## 🆕 What's New (Latest Update)

### 🚀 Multi-Exchange Support!

NOFX now supports **three major exchanges**: Binance, Hyperliquid, and Aster DEX!

#### **Hyperliquid Exchange**

A high-performance decentralized perpetual futures exchange!

**Key Features:**
- ✅ Full trading support (long/short, leverage, stop-loss/take-profit)
- ✅ Automatic precision handling (order size & price)
- ✅ Unified trader interface (seamless exchange switching)
- ✅ Support for both mainnet and testnet
- ✅ No API keys needed - just your Ethereum private key

**Why Hyperliquid?**
- 🔥 Lower fees than centralized exchanges
- 🔒 Non-custodial - you control your funds
- ⚡ Fast execution with on-chain settlement
- 🌍 No KYC required

**Quick Start:**
1. Get your MetaMask private key (remove `0x` prefix)
2. Set `"exchange": "hyperliquid"` in config.json
3. Add `"hyperliquid_private_key": "your_key"`
4. Start trading!

See [Configuration Guide](#-alternative-using-hyperliquid-exchange) for details.

#### **Aster DEX Exchange** (NEW! v2.0.2)

A Binance-compatible decentralized perpetual futures exchange!

**Key Features:**
- ✅ Binance-style API (easy migration from Binance)
- ✅ Web3 wallet authentication (secure and decentralized)
- ✅ Full trading support with automatic precision handling
- ✅ Lower trading fees than CEX
- ✅ EVM-compatible (Ethereum, BSC, Polygon, etc.)

**Why Aster?**
- 🎯 **Binance-compatible API** - minimal code changes required
- 🔐 **API Wallet System** - separate trading wallet for security
- 💰 **Competitive fees** - lower than most centralized exchanges
- 🌐 **Multi-chain support** - trade on your preferred EVM chain

**Quick Start:**
1. Visit [Aster API Wallet](https://www.asterdex.com/en/api-wallet)
2. Connect your main wallet and create an API wallet
3. Copy the API Signer address and Private Key
4. Set `"exchange": "aster"` in config.json
5. Add `"aster_user"`, `"aster_signer"`, and `"aster_private_key"`

---

## 📸 Screenshots

### 🏆 Competition Mode - Real-time AI Battle
![Competition Page](screenshots/competition-page.png)
*Multi-AI leaderboard with real-time performance comparison charts showing Qwen vs DeepSeek live trading battle*

### 📊 Trader Details - Complete Trading Dashboard
![Details Page](screenshots/details-page.png)
*Professional trading interface with equity curves, live positions, and AI decision logs with expandable input prompts & chain-of-thought reasoning*

---

## ✨ Core Features

### 🏆 Multi-AI Competition Mode
- **Qwen vs DeepSeek** live trading battle
- Independent account management and decision logs
- Real-time performance comparison charts
- ROI PK and win rate statistics

### 🧠 AI Self-Learning Mechanism (NEW!)
- **Historical Feedback**: Analyzes last 20 cycles of trading performance before each decision
- **Smart Optimization**:
  - Identifies best/worst performing coins
  - Calculates win rate, profit/loss ratio, average profit
  - Avoids repeating mistakes (consecutive losing coins)
  - Reinforces successful strategies (high win rate patterns)
- **Dynamic Adjustment**: AI autonomously adjusts trading style based on historical performance

### 📊 Intelligent Market Analysis
- **3-minute K-line**: Real-time price, EMA20, MACD, RSI(7)
- **4-hour K-line**: Long-term trend, EMA20/50, ATR, RSI(14)
- **Open Interest Analysis**: Market sentiment, capital flow judgment
- **OI Top Tracking**: Top 20 coins with fastest growing open interest
- **AI500 Coin Pool**: Automatic high-score coin screening
- **Liquidity Filter**: Auto-filters low liquidity coins (<15M USD position value)

### 🎯 Professional Risk Control
- **Per-Coin Position Limit**:
  - Altcoins ≤ 1.5x account equity
  - BTC/ETH ≤ 10x account equity
- **Configurable Leverage** (v2.0.3+)