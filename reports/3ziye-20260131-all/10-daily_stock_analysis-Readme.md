<div align="center">

# 📈 股票智能分析系统

[![GitHub stars](https://img.shields.io/github/stars/ZhuLinsen/daily_stock_analysis?style=social)](https://github.com/ZhuLinsen/daily_stock_analysis/stargazers)
[![CI](https://github.com/ZhuLinsen/daily_stock_analysis/actions/workflows/ci.yml/badge.svg)](https://github.com/ZhuLinsen/daily_stock_analysis/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Ready-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)

> 🤖 基于 AI 大模型的 A股/港股/美股自选股智能分析系统，每日自动分析并推送「决策仪表盘」到企业微信/飞书/Telegram/邮箱

[**功能特性**](#-功能特性) • [**部署指南**](docs/DEPLOY.md) • [**推送效果**](#-推送效果) • [**使用指南**](docs/full-guide.md) • [**更新日志**](docs/CHANGELOG.md)

[English](docs/README_EN.md) | 简体中文 | [繁體中文](docs/README_CHT.md)

</div>

## 💖 赞助商 (Sponsors)
<div align="center">
  <a href="https://serpapi.com/baidu-search-api?utm_source=github_daily_stock_analysis" target="_blank">
    <img src="./sources/serpapi_banner_zh.png" alt="轻松抓取搜索引擎上的实时金融新闻数据 - SerpApi" height="160">
  </a>
</div>
<br>


## ✨ 功能特性

### 🎯 核心功能
- **AI 决策仪表盘** - 一句话核心结论 + 精确买卖点位 + 检查清单
- **多维度分析** - 技术面 + 筹码分布 + 舆情情报 + 实时行情
- **大盘复盘** - 每日市场概览、板块涨跌、北向资金
- **多渠道推送** - 支持企业微信、飞书、Telegram、邮件（自动识别）
- **零成本部署** - GitHub Actions 免费运行，无需服务器
- **💰 白嫖 Gemini API** - Google AI Studio 提供免费额度，个人使用完全够用
- **🔄 多模型支持** - 支持 OpenAI 兼容 API（DeepSeek、通义千问等）作为备选

### 📊 数据来源
- **行情数据**: AkShare（免费）、Tushare、Pytdx（通达信）、Baostock、YFinance
- **新闻搜索**: Tavily、SerpAPI、Bocha
- **AI 分析**: 
  - 主力：Google Gemini（gemini-3-flash-preview）—— [免费获取](https://aistudio.google.com/)
  - 备选：应大家要求，也支持了OpenAI 兼容 API（DeepSeek、通义千问、Moonshot 等）

### 🛡️ 交易理念内置
- ❌ **严禁追高** - 乖离率 > 5% 自动标记「危险」
- ✅ **趋势交易** - MA5 > MA10 > MA20 多头排列
- 📍 **精确点位** - 买入价、止损价、目标价
- 📋 **检查清单** - 每项条件用 ✅⚠️❌ 标记

## 🚀 快速开始

### 方式一：GitHub Actions（推荐，零成本）

**无需服务器，每天自动运行！**

#### 1. Fork 本仓库(顺便点下⭐呀)

点击右上角 `Fork` 按钮

#### 2. 配置 Secrets

进入你 Fork 的仓库 → `Settings` → `Secrets and variables` → `Actions` → `New repository secret`

**AI 模型配置（二选一）**

| Secret 名称 | 说明 | 必填 |
|------------|------|:----:|
| `GEMINI_API_KEY` | [Google AI Studio](https://aistudio.google.com/) 获取免费 Key | ✅* |
| `OPENAI_API_KEY` | OpenAI 兼容 API Key（支持 DeepSeek、通义千问等） | 可选 |
| `OPENAI_BASE_URL` | OpenAI 兼容 API 地址（如 `https://api.deepseek.com/v1`） | 可选 |
| `OPENAI_MODEL` | 模型名称（如 `deepseek-chat`） | 可选 |

> *注：`GEMINI_API_KEY` 和 `OPENAI_API_KEY` 至少配置一个

**通知渠道配置（可同时配置多个，全部推送）**

| Secret 名称 | 说明 | 必填 |
|------------|------|:----:|
| `WECHAT_WEBHOOK_URL` | 企业微信 Webhook URL | 可选 |
| `FEISHU_WEBHOOK_URL` | 飞书 Webhook URL | 可选 |
| `TELEGRAM_BOT_TOKEN` | Telegram Bot Token（@BotFather 获取） | 可选 |
| `TELEGRAM_CHAT_ID` | Telegram Chat ID | 可选 |
| `EMAIL_SENDER` | 发件人邮箱（如 `xxx@qq.com`） | 可选 |
| `EMAIL_PASSWORD` | 邮箱授权码（非登录密码） | 可选 |
| `EMAIL_RECEIVERS` | 收件人邮箱（多个用逗号分隔，留空则发给自己） | 可选 |
| `PUSHPLUS_TOKEN` | PushPlus Token（[获取地址](https://www.pushplus.plus)，国内推送服务） | 可选 |
| `CUSTOM_WEBHOOK_URLS` | 自定义 Webhook（支持钉钉等，多个用逗号分隔） | 可选 |
| `CUSTOM_WEBHOOK_BEARER_TOKEN` | 自定义 Webhook 的 Bearer Token（用于需要认证的 Webhook） | 可选 |
| `SINGLE_STOCK_NOTIFY` | 单股推送模式：设为 `true` 则每分析完一只股票立即推送 | 可选 |
| `REPORT_TYPE` | 报告类型：`simple`(精简) 或 `full`(完整)，Docker环境推荐设为 `full` | 可选 |
| `ANALYSIS_DELAY` | 个股分析和大盘分析之间的延迟（秒），避免API限流，如 `10` | 可选 |

> *注：至少配置一个渠道，配置多个则同时推送
>
> 📖 更多配置（Pushover 手机推送、飞书云文档等）请参考 [完整配置指南](docs/full-guide.md)

**其他配置**

| Secret 名称 | 说明 | 必填 |
|------------|------|:----:|
| `STOCK_LIST` | 自选股代码，如 `600519,hk00700,AAPL,TSLA` | ✅ |
| `TAVILY_API_KEYS` | [Tavily](https://tavily.com/) 搜索 API（新闻搜索） | 推荐 |
| `BOCHA_API_KEYS` | [博查搜索](https://open.bocha.cn/) Web Search API（中文搜索优化，支持AI摘要，多个key用逗号分隔） | 可选 |
| `SERPAPI_API_KEYS` | [SerpAPI](https://serpapi.com/baidu-search-api?utm_source=github_daily_stock_analysis) 备用搜索 | 可选 |
| `TUSHARE_TOKEN` | [Tushare Pro](https://tushare.pro/) Token | 可选 |
| `WECHAT_MSG_TYPE` | 企微消息类型，默认 markdown，支持配置 text 类型，发送纯 markdown 文本 | 可选 |

#### 3. 启用 Actions

进入 `Actions` 标签 → 点击 `I understand my workflows, go ahead and enable them`

#### 4. 手动测试

`Actions` → `每日股票分析` → `Run workflow` → 选择模式 → `Run workflow`

#### 5. 完成！

默认每个工作日 **18:00（北京时间）** 自动执行

### 方式二：本地运行 / Docker 部署

> 📖 本地运行、Docker 部署详细步骤请参考 [完整配置指南](docs/full-guide.md)

## 📱 推送效果

![运行效果演示](./sources/all_2026-01-13_221547.gif)

### 决策仪表盘
```
📊 2026-01-10 决策仪表盘
3只股票 | 🟢买入:1 🟡观望:2 🔴卖出:0

🟢 买入 | 贵州茅台(600519)
📌 缩量回踩MA5支撑，乖离率1.2%处于最佳买点
💰 狙击: 买入1800 | 止损1750 | 目标1900
✅多头排列 ✅乖离安全 ✅量能配合

🟡 观望 | 宁德时代(300750)
📌 乖离率7.8%超过5%警戒线，严禁追高
⚠️ 等待回调至MA5附近再考虑

---
生成时间: 18:00
```

### 大盘复盘

![大盘复盘推送效果](./sources/dapan_2026-01-13_22-14-52.png)

```
🎯 2026-01-10 大盘复盘

📊 主要指数
- 上证指数: 3250.12 (🟢+0.85%)
- 深证成指: 10521.36 (🟢+1.02%)
- 创业板指: 2156.78 (🟢+1.35%)

📈 市场概况
上涨: 3920 | 下跌: 1349 | 涨停: 155 | 跌停: 3

🔥 板块表现
领涨: 互联网服务、文化传媒、小金属
领跌: 保险、航空机场、光伏设备
```

## ⚙