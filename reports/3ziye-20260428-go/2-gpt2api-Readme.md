# gpt2api

> 基于逆向 **chatgpt.com** 的 OpenAI 兼容 SaaS 网关 —— 多账号池 / 代理池 / **IMG2 终稿直出** / **批量出图** / **本地 2K/4K 高清放大** / **高并发调度** / 积分计费 / 管理后台一体化。

<p align="center">
  <a href="https://github.com/432539/gpt2api/stargazers"><img alt="stars" src="https://img.shields.io/github/stars/432539/gpt2api?style=flat-square"></a>
  <a href="https://github.com/432539/gpt2api/releases"><img alt="release" src="https://img.shields.io/github/v/release/432539/gpt2api?style=flat-square"></a>
  <a href="https://golang.org/"><img alt="go" src="https://img.shields.io/badge/Go-1.22%2B-00ADD8?style=flat-square&logo=go"></a>
  <a href="https://vuejs.org/"><img alt="vue" src="https://img.shields.io/badge/Vue-3-4FC08D?style=flat-square&logo=vue.js"></a>
  <a href="https://github.com/432539/gpt2api/blob/main/LICENSE"><img alt="license" src="https://img.shields.io/badge/License-MIT-green?style=flat-square"></a>
</p>

- **仓库地址**:<https://github.com/432539/gpt2api>
- **技术交流 QQ 群**:`382446`(入群请注明「gpt2api」)

---

## 目录

- [一、项目定位](#一项目定位)
- [📸 界面预览](#-界面预览)
- [二、核心特性](#二核心特性)
- [三、技术栈](#三技术栈)
- [四、架构概览](#四架构概览)
- [五、快速开始(Docker 一键部署)](#五快速开始docker-一键部署)
- [六、配置说明](#六配置说明)
- [七、API 使用示例](#七api-使用示例)
- [八、重点能力详解](#八重点能力详解)
  - [8.1 IMG2 出图](#81-img2-出图)
  - [8.2 4K / 2K 高清输出(本地 Catmull-Rom 放大)](#82-4k--2k-高清输出本地-catmull-rom-放大)
  - [8.3 批量出图 / 多张聚合](#83-批量出图--多张聚合)
  - [8.4 高性能高并发调度](#84-高性能高并发调度)
- [九、管理后台功能概览](#九管理后台功能概览)
- [十、目录结构](#十目录结构)
- [十一、二次开发 / 定制](#十一二次开发--定制)
- [十二、FAQ](#十二faq)
- [十三、Roadmap](#十三roadmap)
- [十四、参与贡献](#十四参与贡献)
- [十五、免责声明与风险提示](#十五免责声明与风险提示)
- [十六、License](#十六license)

---

## 一、项目定位

`gpt2api` 是一个**自建的 ChatGPT → OpenAI 兼容网关**,把 `chatgpt.com` Plus / Team / Codex 账号的能力,以 **完全兼容 OpenAI API** 的形式(`/v1/chat/completions` / `/v1/images/generations`)开放给下游调用方,同时配套一整套 SaaS 运营后台。

适合的场景:

- 你手头有一批 ChatGPT Plus / Team / Codex 账号,想对外提供稳定的 **GPT Image / DALL·E 3 / IMG2 高清大图**服务;
- 想给公司 / 团队内部开通 OpenAI 风格的代理网关,把所有调用统计、计费、审计集中管理;
- 想低成本搭一个带积分 / 套餐 / 易支付的 AI API 中台,面向 C 端或 B 端开发者售卖。

> 本项目当前版本**聚焦图片模型**(详见 [8.1 IMG2 出图](#81-img2-出图)、[8.2 4K/2K 高清输出](#82-4k--2k-高清输出本地-catmull-rom-放大) 与 [8.3 批量出图](#83-批量出图--多张聚合))。文字通路(`/v1/chat/completions`)代码层完整保留,但因 `chatgpt.com` 新 sentinel 协议存在短期不稳定因素,UI 入口已在当前版本关闭,恢复只需改一行 feature flag,详见 [十一、二次开发](#十一二次开发--定制)。

---

## 📸 界面预览

> 截图来自 **在线体验(Playground)** 页 · `gpt-image-2` / `picture_v2`(IMG2 终稿)· `9:16` 比例 · 单次调用一张 prompt 批量出图。

### 在线体验 · 文生图 / 批量出图

<p align="center">
  <img src="docs/screenshots/playground-batch.png" alt="gpt2api 在线体验 · 文生图 · IMG2 批量出图" width="960">
</p>

- 左侧:模型选择、画面比例(1:1 / 16:9 / **9:16**)、张数、PROMPT 输入、prompt 预设库;
- 右侧:**同一个任务聚合返回多张高清终稿**(IMG2 命中时单次 `/f/conversation` 一次性产出 2 张,再配合"张数 N"即可成批扩图);
- 点击任意一张可进入全屏放大预览 ↓。

### 管理后台 · 单图放大预览

<p align="center">
  <img src="docs/screenshots/playground-preview.png" alt="gpt2api 管理后台 · 图片全屏预览 · 左侧完整菜单" width="960">
</p>

- 左侧:**个人中心 / 后台管理** 双分区菜单 —— API Keys、使用记录、账单与充值、在线体验、接口文档、用户管理、GPT 账号池、代理管理、模型配置、用户分组、用量统计、全局 Keys、审计日志、数据备份、系统设置,一个台子全搞定;
- 中间:全屏放大查看终稿,直接右键"图片另存为"。所有图片 URL 都是内置 `/p/img/:task/:idx` **HMAC 签名代理**,绕过 `chatgpt.com` `estuary/content` 的 403 防盗链。

---

## 二、核心特性

| 分类 | 能力 |
|------|------|
| **上游协议** | 完整逆向 `chatgpt.com` `f/conversation` 两步 sentinel(`/prepare` + `/finalize`)、PoW、`conduit_token`、全套 `oai-*` / `Sec-Ch-Ua-*` 指纹头 |
| **图片生成** | 文生图、**图生图 / 多图参考**、**IMG2 正式版直出**(速度优先,SSE 够数即返回,最长 300s 补齐轮询兜底)、**本地 2K/4K PNG 高清放大**(Catmull-Rom 插值,按需触发 + 进程内 LRU)、轮询 + SSE 直出双通道 |
| **账号池** | JSON / AT / RT / ST 四种方式批量导入,**自动刷新**、**额度探测**、**风控熔断**、按账号稳定绑定 `oai-device-id` / `oai-session-id` |
| **代理池** | 支持 HTTP / SOCKS5,健康分自动探测,按账号强绑定代理,避免 IP 指纹混用 |
| **调度器** | 串行 lease + Redis 分布式锁,`min_interval_sec` 单号最小间隔、`daily_usage_ratio` 日熔断、`cooldown_429_sec` 限速退避 |
| **OpenAI 兼容** | `/v1/chat/completions`(保留)、`/v1/images/generations`、`/v1/images/edits`、`/v1/images/tasks/:id`、`/v1/models` |
| **下游 Key** | 独立于用户账号的 `sk-` Key,支持 **RPM / TPM / 日配额 / IP 白名单 / 模型白名单** |
| **计费** | 积分钱包 + 预扣结算、分组倍率(VIP / 内部 / 渠道)、充值套餐、**易支付(EPay)**接入 |
| **安全** | AES-256-GCM 加密 AT / cookies、JWT 登录、RBAC 权限、**管理员写操作全链路审计**、高危操作 `X-Admin-Confirm` 二次确认 |
| **运维** | 数据库一键备份 / 恢复(`mysqldump` + gzip)、上传单文件限额、备份保留策略 |
| **图片防盗链** | 内置签名代理 `/p/img/:task/:idx`,HMAC 签名 + 过期时间,绕过 `chatgpt.com` `estuary/content` 的 403 |
| **前端** | Vue 3 + Element Plus 单页控制台,账户池 / 代理池 / 模型 / 用户 / 积分 / 审计 / 备份 / 系统设置全覆盖 |

---

## 三、技术栈

**后端**

- Go 1.22+
- Gin(HTTP 框架) / sqlx(MySQL 访问) / Viper(配置) / Zap(日志)
- MySQL 8.0(业务数据 + 审计 + 账变) / Redis 7(分布式锁 / 限流 / 缓存)
- `refraction-networking/utls`(TLS 指纹,用于规避 `chatgpt.com` JA3 检测)
- `golang-jwt/jwt` / `golang.org/x/crypto`(鉴权 + 密码学)
- Goose(数据库迁移)

**前端**

- Vue 3 + Vite 5 + TypeScript 5
- Element Plus 2.7(组件库)
- Pinia(状态管理) / `pinia-plugin-persistedstate`
- Vue Router 4
- Axios

**部署**

- Docker Compose(MySQL + Redis + server,可选 nginx)
- 默认单机;水平扩展见 [`deploy/README.md`](deploy/README.md)

---

## 四、架构概览

```mermaid
flowchart LR
  subgraph Client["下游调用方"]
    SDK["OpenAI SDK / curl / 自家业务"]
  end

  subgraph Gateway["gpt2api Server :8080"]
    