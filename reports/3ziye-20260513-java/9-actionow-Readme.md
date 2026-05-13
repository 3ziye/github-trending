<div align="center">

<img src="assets/full-logo.png#gh-light-mode-only" alt="Actionow" width="520" />
<img src="assets/full-logo-dark.png#gh-dark-mode-only" alt="Actionow" width="520" />

<h3><i>Action! Now!</i> &nbsp;The open-source AI studio for screenwriting and storyboard production.</h3>

<p>从剧本到分镜，从角色到成片，Actionow 把"Action! Now!"的创作冲动<br/>
落到一个工程化工作台——智能体驱动、开箱即接最新模型、支持代码级控制与私有化部署。</p>

<p><a href="https://www.actionow.ai"><b>actionow.ai</b></a></p>

<p>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0%20with%20additional%20conditions-blue.svg" alt="License"></a>
  <a href="https://t.me/+m1saPHQZlTIxZDg1"><img src="https://img.shields.io/badge/Telegram-加入群组-2CA5E0.svg?logo=telegram" alt="Telegram"></a>
  <a href="https://openjdk.org/projects/jdk/21/"><img src="https://img.shields.io/badge/Java-21-orange.svg" alt="Java 21"></a>
  <a href="https://spring.io/projects/spring-boot"><img src="https://img.shields.io/badge/Spring%20Boot-3.4.1-6DB33F.svg" alt="Spring Boot"></a>
  <a href="https://spring.io/projects/spring-ai"><img src="https://img.shields.io/badge/Spring%20AI-1.1.2-6E4AFF.svg" alt="Spring AI"></a>
  <a href="https://nextjs.org/"><img src="https://img.shields.io/badge/Next.js-16-black.svg" alt="Next.js 16"></a>
  <a href="https://react.dev/"><img src="https://img.shields.io/badge/React-19-61DAFB.svg" alt="React 19"></a>
  <a href="https://www.docker.com/"><img src="https://img.shields.io/badge/Docker-Compose%20v2-2496ED.svg" alt="Docker Compose"></a>
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</p>

<p>
  <strong>中文</strong> ·
  <a href="README_EN.md">English</a>
</p>

<p>
  <a href="#产品定位">产品定位</a> ·
  <a href="#在线演示">在线演示</a> ·
  <a href="#核心能力">核心能力</a> ·
  <a href="#架构总览">架构总览</a> ·
  <a href="#快速开始">快速开始</a> ·
  <a href="#文档">文档</a> ·
  <a href="#roadmap">Roadmap</a>
</p>

</div>

---

## 产品定位

Actionow 面向剧本创编、分镜协作与 AIGC 成片这一完整生产链，提供一个由智能体驱动、可私有化部署的开源工作台。

平台围绕 **剧本 → 剧集 → 场次 → 分镜 → 角色、场景、道具、风格、素材** 的内容图谱组织所有创作行为，所有实体均带版本控制与血缘追踪，所有交互均可被智能体观察、复用与回放。

| 适用对象 | 如何受益 |
|----------|----------|
| 影视、广告、动画团队 | 用智能体串联编剧、美术、制片，把分镜与素材沉淀为可复用资产 |
| AIGC 工作室 | 将多模态模型能力以 Skill 形式封装，按角色与场景组合调用 |
| 企业 AI 平台团队 | 以本项目为参考实现，构建自有的 Agent 中台与计费闭环 |
| AI 工程开发者 | 研究 Spring AI Alibaba Agent Framework 在多租户生产环境下的工程化落地 |

---

## 在线演示

线上体验：**[actionow.ai](https://actionow.ai)**

<div align="center">

<table>
  <tr>
    <td width="50%" align="center">
      <img src="assets/demo/screenshot-chat.png" alt="Agent Chat" width="100%" /><br/>
      <sub><b>Agent Chat</b></sub>
    </td>
    <td width="50%" align="center">
      <img src="assets/demo/screenshot-model.png" alt="Model Config" width="100%" /><br/>
      <sub><b>Model Config</b></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <img src="assets/demo/screenshot-mission.png" alt="Mission Console" width="100%" /><br/>
      <sub><b>Mission Console</b></sub>
    </td>
    <td width="50%" align="center">
      <img src="assets/demo/screenshot-inspiration.png" alt="Inspiration" width="100%" /><br/>
      <sub><b>Inspiration</b></sub>
    </td>
  </tr>
</table>

</div>

---

## 核心能力

<table>
<tr>
<td width="50%" valign="top">

### 多 Agent 与自定义 Skill
基于 Spring AI Alibaba 的智能体编排，内置影视创作 Skill 库

- Mission 分步追踪 · SSE 实时进度
- JSON Schema 输出校验
- 三级 Skill 作用域：系统 / 工作空间 / 用户

</td>
<td width="50%" valign="top">

### 团队实时协作
WebSocket 多人协同，虚拟线程承载广播扇出

- Presence 在线感知 + 实体排他编辑锁
- 完整协作生命周期事件
- 多浏览器标签页协同

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 细粒度权限控制
工作空间 + 剧本两级权限模型

- Workspace：Creator / Admin / Member / Guest
- Script：VIEW / EDIT / ADMIN
- 临时授权 + 过期时间 + 来源追踪

</td>
<td width="50%" valign="top">

### 多租户架构
PostgreSQL Schema 级隔离

- 每工作空间独立 Schema
- 基于 TransmittableThreadLocal 跨异步链路传递租户上下文
- 跨租户公共数据共享

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 积分与计费系统
工作空间钱包 + 动态支付通道闭环

- 充值 / 消费 / 退款 / 转账 / 冻结全流水
- 成员配额 + 周期重置（日 / 周 / 月）
- 支付 Provider 运行时可切换 · 礼品码兑换 · Free / Basic / Pro / Enterprise

</td>
<td width="50%" valign="top">

### AI 模型插件化网关
Groovy 沙箱驱动的企业级实现

- **接入新模型无需发版**，写脚本即上线
- 四种响应模式：BLOCKING / STREAMING / CALLBACK / POLLING
- 重试 / 限流 / 熔断 / 超时（Resilience4j 运行时可配）
- Provider 自动 fallback · 灰度白名单 · Bearer / API Key / AK-SK

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 异步任务编排
图片 / 视频 / 音频 / 文本统一异步执行框架

- 优先级队列 + BatchJob + Pipeline
- 超时 / 重试 / Compensation 回滚
- 全程关联积分扣费

</td>
<td width="50%" valign="top">

### 多 Provider 邮件网关
统一邮件抽象 + 运行时热切换

- Resend / SMTP（AWS SES）/ Cloudflare
- DynamicMailService 路由分发
- 验证码 / 重置 / 欢迎 / 安全告警模板

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 内容图谱与版本管理
剧本 / 分镜 / 角色 / 素材统一建模

- 全量实体版本控制
- `t_asset_lineage` 资产血缘追踪
- 画布节点与三种布局引擎已在后端建模，前端集成中

</td>
<td width="50%" valign="top">

### 多云对象存储抽象
一套接口，五家 Provider

- MinIO / AWS S3 / 阿里云 OSS
- Cloudflare R2 / 火山 TOS
- 配置驱动切换

</td>
</tr>
</table>

---

## 架构总览

```mermaid
flowchart LR
    Client["Web · Desktop · Mobile"] --> Web["Next.js · 3000"] --> Gateway["Gateway · 8080"]

