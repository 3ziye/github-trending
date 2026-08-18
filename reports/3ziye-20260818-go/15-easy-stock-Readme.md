<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/jundizhou/easy-stock@main/desktop/assets/easy-stock.png" width="112" height="112" alt="easy-stock Logo" />
</p>

<h1 align="center">easy-stock</h1>

<p align="center"><strong>AI 时代的 A 股行情分析与智能投研工作台</strong></p>

<p align="center">
  让 AI 看懂市场，让每一次判断都有证据。<br />
  把盘中观察、盘后复盘和长期认知，沉淀为一套持续进化的研究系统。
</p>

<p align="center">
  <img alt="Go" src="https://img.shields.io/badge/Backend-Go-00ADD8?logo=go&logoColor=white" />
  <img alt="React" src="https://img.shields.io/badge/Frontend-React%20%2B%20TypeScript-3178C6?logo=react&logoColor=white" />
  <img alt="Electron" src="https://img.shields.io/badge/Desktop-Electron-47848F?logo=electron&logoColor=white" />
  <img alt="Hermes" src="https://img.shields.io/badge/AI-Hermes-6D5BD0" />
  <img alt="Local First" src="https://img.shields.io/badge/Data-Local%20First-159A80" />
  <img alt="License" src="https://img.shields.io/badge/License-Non--Commercial-EA580C" />
</p>

<p align="center">
  <a href="#为什么要做-easy-stock">为什么</a> ·
  <a href="#核心产品能力">核心能力</a> ·
  <a href="#ai-如何赋能-a-股研究">AI 研究方式</a> ·
  <a href="#ai-原生架构">系统架构</a> ·
  <a href="#快速开始">快速开始</a> ·
  <a href="#许可与商业使用">许可</a>
</p>

---

## 为什么要做 easy-stock

AI 时代的炒股软件，不应该只是在传统行情终端旁边多放一个聊天框。

传统行情软件擅长展示价格、涨跌幅和成交额，但 A 股交易真正困难的是理解价格背后的结构：今天的主线是什么、题材是否扩散、连板高度是否打开、昨日强势股是否获得溢价、趋势是否仍然成立、情绪处于修复还是退潮。

easy-stock 希望构建一套真正理解 A 股语境的 AI 原生工作台：

| AI 原生能力 | easy-stock 的实现方式 |
| --- | --- |
| **感知市场** | 聚合开盘啦、东方财富、新浪、财联社等来源，统一行情、K 线、题材、涨停与资讯数据 |
| **理解结构** | 将趋势、题材、连板、情绪、量价和相对强度整理成可计算的领域模型 |
| **执行任务** | 通过定时调度、内置浏览器和 Agent 自动发现文章、去重、归档并提炼观点 |
| **形成记忆** | 将文章、摘要、情绪历史、分析记录、模型会话和研究缓存保存在本机 |
| **验证结论** | 保留评分维度、题材来源、原文地址、更新时间、延迟与降级状态，让结论可以回到证据层核验 |

> easy-stock 的目标不是替你做决定，而是让你在 AI 时代拥有更完整的感知、更高效的研究和更可复用的判断体系。

---

## 核心产品能力

### 01 · 大 V 自动复盘

#### 兼听则明，客观则赢：让 AI 自动收集和整理多位市场作者的观点

大 V 的盘后复盘通常分散在雪球、淘股吧和微信公众号中，手工逐个打开主页、筛选当天文章、复制正文并整理观点非常耗时。easy-stock 将这些内容组织为统一的复盘时间流：

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/jundizhou/easy-stock@main/docs/assets/easy-stock-auto-review.png" width="2560" height="1692" alt="easy-stock 大 V 自动复盘与每日同步工作台" />
</p>

文章收集完成后，可以一键生成「今日大 V 观点共识」，从文章集合中提炼共同关注方向、主要分歧、盘面事实与下一交易日需要验证的条件。

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/jundizhou/easy-stock@main/docs/assets/easy-stock-ai-daily-consensus.png" width="2560" height="1692" alt="easy-stock AI 今日大 V 观点共识与明日预期" />
</p>

这套能力希望解决的不是“让 AI 猜明天涨什么”，而是把几十篇非结构化文章转化为一份可阅读、可核验、可在次日继续跟踪的观点地图。

### 02 · 超短连板分析

#### 看清梯队、晋级和情绪周期，寻找真正的超短节点

系统将涨停池、连板梯队、昨日反馈、晋级率和情绪历史放在同一视图中,并设计一套算法分析情绪周期：

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/jundizhou/easy-stock@main/docs/assets/easy-stock-short-term-analysis.png" width="2560" height="1692" alt="easy-stock 超短连板、市场情绪与晋级结构分析" />
</p>

### 03 · 趋势题材雷达

#### 从板块涨跌中识别真正的市场主线：牛市进程分歧研究，熊市进程分歧防守
聚合题材排名、涨跌强度、资金流、上涨宽度和持续天数，通过题材地图拆解产业链、概念节点和细分方向。结合 AI 分析市场趋势、题材阶段和趋势股的条件化介入点

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/jundizhou/easy-stock@main/docs/assets/easy-stock-theme-radar.png" width="2560" height="1696" alt="easy-stock 趋势题材雷达、主线热度与个股梯队分析" />
</p>

### 04 · 行情总览

#### 把指数、资金、榜单和研究信号组织成一张可追溯的市场地图

行情总览将市场核心指数、新闻快讯、行业趋势强度、行业资金、题材概念、个股资金流入流出、龙虎榜、公告雷达、机构观点与产业透视统一到同一个研究入口。每个页面保留数据来源与抓取时间，并可将当前上下文直接交给 AI 解读，减少在多个行情终端和资讯页面之间来回切换。

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/jundizhou/easy-stock@main/docs/assets/easy-stock-market-overview-indices.png" width="2560" height="1696" alt="easy-stock 行情总览、市场核心指数与跨市场走势分析" />
</p>

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/jundizhou/easy-stock@main/docs/assets/easy-stock-market-overview-research.png" width="2560" height="1696" alt="easy-stock 行情总览、机构观点与研报证据检索" />
</p>

### 05 · 个股 AI 分析

#### 把趋势股与情绪股放进同一套可解释决策系统

个股 AI 分析会系统判断个股更接近情绪连板、趋势容量、趋势成长、震荡观察还是弱势风险路径，再为不同路径分配不同权重，结合你的个人操作经验，复盘文章，游资心得等差异化内容让ai定制你的专属个股报告。

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/jundizhou/easy-stock@main/docs/assets/easy-stock-stock-ai-analysis-overview.png" width="2560" height="1696" alt="easy-stock 个股 AI 分析总览、多维评分与题材定位" />
</p>

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/jundizhou/easy-stock@main/docs/assets/easy-stock-stock-ai-analysis-evidence.png" width="2560" height="1696" alt="easy-stock 个股 AI 分析条件决策、事实链与风险边界" />
</p>

<p align="center"><sub>截图用于展示页面结构；股票状态、题材标签、评分和风险参数会随交易日、缓存快照与数据源可用性动态变化。</sub></p>

### 06 · 游资心法与 AI Copilot

#### 把经验材料变成可持续研读的知识，让 AI 越用越懂你的研究方式

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/jundizhou/easy-stock@main/docs/assets/easy-stock-trading-mastery.png" width="2560" height="1696" alt="easy-stock 游资心法库、人物资料与 Hermes 深度研读" />
</p>

### 每日研究闭环

| 阶段 | easy-stock 提供的能力 |
| --- | --- |
| **盘中发现** | 行情总览、趋势题材、实时行情、题材地图、涨停梯队和数据源状态 |
| **个股研判** | 路径识别、多周期趋势、相对强度、题材归因、隔日情景和风险边界 |
| **收盘复盘** | 情绪时间轴、昨日反馈、晋级结构和连板梯队分析 |
| **信息收集** | 大 V 主页自动同步、文章导入、正文清洗和本地归档 |
| **AI 提炼** | 单篇摘要、作者归纳、跨作者共识、分歧和明日观察条件 |
| **长期积累** | 文章资料库、游资心法、个股分析记录、AI 会话和本地研究记忆 |

---

## AI 如何赋能 A 股研究

### 1. 从“看数据”升级为“理解市场结构”

easy-stock 先通过