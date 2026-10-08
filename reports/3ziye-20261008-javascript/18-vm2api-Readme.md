<div align="center">

# vm2api

### 完全隔离的虚拟机级 AI 订阅转 API 生产网关
**Next-Generation Fully Isolated VM-Level AI Subscription-to-API Gateway**

[![Release](https://img.shields.io/badge/Release-v1.3.105-blue.svg?style=for-the-badge&logo=github)](https://github.com/dofastted/vm2api/releases)
[![License](https://img.shields.io/badge/License-Noncommercial-amber.svg?style=for-the-badge)](LICENSE)
[![Benchmarks](https://img.shields.io/badge/Benchmarks-Clean%20Verified-00C853?style=for-the-badge&logo=shield)](docs/benchmarks/README.md)
[![Cluster](https://img.shields.io/badge/Cluster-Multi--VPS%20Ready-7928CA?style=for-the-badge&logo=docker)](docs/DEPLOY.md)

<p align="center">
  <a href="#-简体中文"><b>🇨🇳 简体中文</b></a> •
  <a href="#-english"><b>🇬🇧 English</b></a> •
  <a href="docs/技术路线.md"><b>🗺️ 技术路线</b></a> •
  <a href="docs/DEPLOY.md"><b>🚀 部署指南</b></a> •
  <a href="docs/benchmarks/README.md"><b>📊 干净度基准</b></a> •
  <a href="#-交流与赞助支持--community--sponsorship"><b>☕ 支持捐赠</b></a>
</p>

---

<img src="docs/images/brand-hero.png" alt="vm2api Hero Banner" width="100%" style="border-radius: 12px; box-shadow: 0 8px 32px rgba(0,0,0,0.4);" />

</div>

<br/>

> [!NOTE]
> **vm2api** 专为高可靠 AI 订阅转化为生产级标准 API 设计。摒弃传统的简单 HTTP 逆向与易被封禁的公用代理方案，采用**全隔离虚拟机/容器环境 + 官方真实客户端进程常驻 + 真实硬件指纹拟真 + 单槽单独立网络出口 + 智能前置蒸馏拦截**，实现真正稳定、长效、高并发的订阅转 API 基础设施。

---

# 🇨🇳 简体中文

## 目录
- [💡 项目概览](#-项目概览)
- [🛡️ 九大核心特性（特色防封与拟真矩阵）](#️-九大核心特性特色防封与拟真矩阵)
  - [0️⃣ 独家 0 提示词注入机制 & 改写引擎](#0️⃣-独家-0-提示词注入机制--改写引擎)
  - [1️⃣ 真实拟真物理机环境](#1️⃣-真实拟真物理机环境)
  - [2️⃣ 官方 Claude Code 真实进程转发](#2️⃣-官方-claude-code-真实进程转发)
  - [3️⃣ 智能前置拦截与“蒸馏拦截”](#3️⃣-智能前置拦截与蒸馏拦截)
  - [4️⃣ 完整的隔离网络环境（1 VM = 1 独立网络出口）](#4️⃣-完整的隔离网络环境1-vm--1-独立网络出口)
  - [5️⃣ 前置协议清洗与多协议统一结构化](#5️⃣-前置协议清洗与多协议统一结构化)
  - [6️⃣ 官方遥测（Telemetry）可控开关](#6️⃣-官方遥测telemetry可控开关)
  - [7️⃣ 分布式集群系统（多 VPS 跨机舰队管理）](#7️⃣-分布式集群系统多-vps-跨机舰队管理)
  - [8️⃣ 完整的企业级 API 密钥与配额管理](#8️⃣-完整的企业级-api-密钥与配额管理)
- [📊 干净度基准评测（Benchmarks）](#-干净度基准评测benchmarks)
- [🚀 快速开始（生产部署）](#-快速开始生产部署)
- [🔌 接口与协议兼容](#-接口与协议兼容)
- [💬 交流与赞助支持](#-交流与赞助支持--community--sponsorship)
- [📜 许可证与免责声明](#-许可证与免责声明--license)

---

## 💡 项目概览

在当今大模型服务中，直接使用第三方逆向脚本或共享代理极易触发风控导致封号、降权与服务中断。**vm2api** 是业界领先的虚拟机级 API 转换中继系统：

- **支持平台**：全面支持 **Anthropic (Claude Pro / Team / Enterprise / Max)** 以及 **OpenAI (ChatGPT / Codex)** 订阅转标准 API。
- **真实载体**：Anthropic 采用官方客户端在隔离 VM / 容器内运行**真实系统进程**，而非第三方伪造 HTTP 模拟。
- **全链路拟真**：从物理机硬件指纹（SMBIOS、MAC、Machine-ID）到独立 SOCKS5 / 本地网络出口，全方位还原真实开发者电脑环境。
- **极简集成**：向上游输出标准 OpenAI `/v1/chat/completions`、`/v1/responses` 与 Anthropic `/v1/messages` 兼容接口，任何支持标准 API 的前端、Agent 或应用均可无缝接入。

---

## 🛡️ 九大核心特性（特色防封与拟真矩阵）

<div align="center">
  <img src="docs/images/vm2api-security-distill.jpg" alt="Security & Distillation Protection" width="95%" style="border-radius: 10px; margin: 12px 0;" />
</div>

### 0️⃣ 独家 0 提示词注入机制 & 改写引擎
- **无感透传，告别 System 篡改**：传统中继依赖向 Prompt 注入大段系统人设与假装指令，不仅消耗高昂 Token，还极易引发模型“自我认知混乱”并被上游识别封号。vm2api 身份在凭证层即对齐官方形态，**做到真正 0 提示词注入（Zero Prompt Injection）**。
- **改写引擎与模板定制**：提供从 `zero`（完全零注入）、`official`、`official_full` 到自定义改写模板的灵活切换，满足特殊上下文场景需求。
- **提供公开 Benchmarks**：随仓库公开提供干净度测试套件与判定报告，杜绝官方内置工具及泄露痕迹，供所有人测试与对比检验。

### 1️⃣ 真实拟真物理机环境
- **消除云主机与多开痕迹**：不仅是普通 Docker 容器，更可支持真虚拟机（KVM / QEMU）。
- **全套物理硬件指纹拟真**：针对上游平台的设备探测，深度拟真真实物理机的硬件特征，涵盖独立 SMBIOS 信息、网卡 MAC 地址、CPU 拓扑、系统序列号、时区与真实的 `/etc/machine-id`。

### 2️⃣ 官方 Claude Code 真实进程转发 & 槽位管理
- **官方原版二进制常驻守护**：每一个 VM / 容器槽位内部均运行 Anthropic 原版 Claude Code 二进制程序，通过内核级 Unix Domain Socket 与协议路由总线通信，完全继承官方客户端签名与合规信誉，杜绝第三方逆向 HTTP 模拟带来的指纹泄露与封禁风险。
- **原生多路 Subagent 高并发调度**：单槽位原生支持多达 **20 路 Subagent 会话并发交互**。会话上下文在槽位内部原生隔离与状态持久化，享受官方客户端热缓存（Prompt Caching）加速与极致响应速度。
- **5h / 7d 官方用量窗口智能对齐**：控制面实时对齐 Anthropic 官方 5 小时滚动窗口与 7 天硬限消耗，精确计算重置倒计时（精确到分钟级）。支持设置水位报警阈值，额度逼近硬限时自动熔断并将流量平滑降级调度至空闲槽位。
- **全生命周期槽位状态机与健康监控**：实时追踪槽位调度状态（在池调度、5h/7d 冷却保护、调用关闭、凭证失效）。支持优先级分级路由（高优先级 VIP 槽位专属调度）、单槽独立成本流水统计与一键额度全槽健康探测。

<div align="center">
  <img src="docs/images/console-vms.png" alt="vm2api 虚拟机槽位管理与官方进程运行实机看板" width="95%" style="border-radius: 10px; border: 1px solid rgba(255,255,255,0.12); box-shadow: 0 6px 24px rgba(0,0,0,0.4);" />
  <br/>
  <sub><i>线上生产环境实机运行脱敏截图：Claude / GPT 多槽位舰队状态、20 路并发承载、5h/7d 官方配额窗口追踪与实时成本流水</i></sub>
</div>

---

<div align="center">
  <img src="docs/images/vm2api-vm-hardware-network.jpg" alt="VM Hardware & Network Isolation" width="95%" style="border-radius: 10px; margin: 12px 0;" />
</div>

### 3️⃣ 智能前置拦截与“蒸馏拦截”
- **反逆向与蒸馏提权拦截**：自动识别并拦截针对大模型的知识蒸馏（Model Distillation）、思维链逆向抓取（CoT Extraction）及恶意提示词攻击，不消耗官方额度。
- **上游 AUP / Refusal 智能阻断卫士**：
  - 实时捕获并分析官方请求与响应中的违规特征（Anthropic AUP 政策风险 / `stop_reason=refusal` / `content_filter`）。
  - 违规特征落库形成智能防护指纹，在网关入口处直接予以拦截，**彻底阻断违规请求触碰官方账号**，从根本上杜绝因敏感 Prompt 导致的账号封禁。

### 4️⃣ 完整的隔离网络环境（1 VM = 1 独立网络出口）
- **绝不共享 IP 资源**：系统严格要求**每一个 VM / KVM 槽位必须且只能绑定一条独立的网络出口**才能启动运行（支持专用独立 SOCKS5 代理、高匿出口池或独立本地出站网络）。
- **彻底告别关联连带封号**：账号之间绝对网络物理隔离，即便单条代理波动或单个账号受限，绝不殃及集群内的其它账号。
- **安全自定义 DoH 解析**：支持配置企业级自定义 HTTPS DoH（DNS-over-HTTPS）上游解析，全程代理加密传输，防止 DNS 劫持与 ISP 侧特征分析。

### 5️⃣ 前置协议清洗与多协议统一结构化
- **入站多协议通吃**：客户端可以使用 Anthropic 原生协