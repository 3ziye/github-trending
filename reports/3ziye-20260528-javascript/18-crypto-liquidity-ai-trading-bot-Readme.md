# Crypto Liquidity AI Trading Bot

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Node](https://img.shields.io/badge/node-18%2B-green.svg)](https://nodejs.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/python-telegramBot/crypto-liquidity-ai-trading-bot)](https://github.com/python-telegramBot/crypto-liquidity-ai-trading-bot/stargazers)

**Repository:** [github.com/python-telegramBot/crypto-liquidity-ai-trading-bot](https://github.com/python-telegramBot/crypto-liquidity-ai-trading-bot)

A modular, signal-driven trading framework for cryptocurrency markets. Detects order book gaps, hidden liquidity walls, and sweep events across major exchanges in real time—designed for quant researchers, algo traders, and firms building liquidity-aware execution tools.

![Dashboard preview](assets/image.png)

---

## Table of Contents

- [Overview](#overview)
- [Why Liquidity-Based Signals](#why-liquidity-based-signals)
- [Target Users](#target-users)
- [Backtest Results](#backtest-results)
- [Strategy Concept](#strategy-concept)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Capabilities](#capabilities)
- [How Liquidity Detection Works](#how-liquidity-detection-works)
- [Installation](#installation)
- [Supported Exchanges](#supported-exchanges)
- [Project Structure](#project-structure)
- [Use Cases](#use-cases)
- [Related Projects](#related-projects)
- [FAQ](#faq)
- [Contributing](#contributing)

---

## Overview

Most trading bots react to price. This one reads the market differently.

`crypto-liquidity-ai-trading-bot` focuses on **order book structure**—detecting where large passive orders sit, when liquidity walls form or vanish, and when stop-loss clusters are swept. These events often precede sharp price moves, making them higher-quality signals than most lagging technical indicators.

The framework is built to be **modular and extensible**: plug in your own execution engine, risk layer, or research pipeline without rewriting the core.

---

## Why Liquidity-Based Signals

Retail indicators (RSI, MACD, moving averages) describe what price has already done. Order book data describes what is *about* to happen—where passive capital is sitting, where stops are clustered, and which levels the market is likely to test.

Professional traders monitor this continuously. This framework gives independent developers and quant teams the same visibility.

Key signal types detected:

- **Liquidity gaps** — thin order book zones where price may move rapidly
- **Hidden walls** — large resting orders that appear or disappear
- **Stop-loss sweeps** — price reaching stop clusters, triggering momentum
- **Book imbalance** — aggressive bid/ask pressure shifts

---

## Target Users

This project is intended for:

- **Algorithmic trading firms** building in-house liquidity intelligence and execution infrastructure
- **Quantitative researchers** studying order book dynamics and market microstructure
- **Exchanges and surveillance teams** monitoring for liquidity anomalies
- **Developers** building AI trading agents, signal systems, or execution layers

It assumes familiarity with financial markets, order books, and at least one of Node.js or Python.

---

## Backtest Results

The metrics below are from a historical simulation using order-book and liquidity-sweep signals on major spot pairs. These are **not live trading results**.

**Test Configuration**

| Parameter | Value |
|-----------|-------|
| Period | January 2024 – December 2024 |
| Duration | 12 months |
| Asset class | Cryptocurrency (spot) |
| Strategy | Liquidity-sweep + order-book imbalance |
| Trading style | Medium-frequency, signal-driven |
| Pairs | BTC/USDT, ETH/USDT, selected altcoins |
| Execution model | Simulated limit and market fills |

**Performance Metrics**

| Metric | Result |
|--------|--------|
| Win rate | 58.2% |
| Profit factor | 1.42 |
| Max drawdown | −12.4% |
| Sharpe ratio (daily) | 1.18 |

**Interpreting These Numbers**

A win rate above 50% suggests the liquidity signals carry predictive information beyond a random baseline. A profit factor of 1.42 indicates positive expectancy over the tested period. A daily Sharpe above 1.0 reflects reasonable risk-adjusted returns, while max drawdown of −12.4% bounds the observed tail risk.

**Example signal output:**

```json
{
  "symbol": "BTC/USDT",
  "direction": "LONG",
  "strength": 0.61,
  "reason": "liquidity_sweep_detected",
  "ts": "2024-11-15T08:44:02Z"
}
```

> **Disclaimer:** Backtest results do not guarantee future performance. Live results will differ due to fees, slippage, execution latency, and changing market conditions. Conduct independent testing and risk assessment before any live deployment.

---

## Strategy Concept

> Price indicators lag. Liquidity moves first.

Large resting orders and stop-loss clusters sit in the order book *before* price reaches them. W