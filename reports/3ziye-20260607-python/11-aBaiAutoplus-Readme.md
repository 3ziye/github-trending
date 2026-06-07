# aBaiAutoplus

<p align="center">
  <b>多平台 AI 账号自动注册与管理 · 协议化付款一键开通 ChatGPT Plus</b>
</p>

<p align="center">
  <a href="https://github.com/asz798838958/aBaiAutoplus/stargazers"><img src="https://img.shields.io/github/stars/asz798838958/aBaiAutoplus?style=for-the-badge&logo=github&color=FFB003" alt="Stars" /></a>
  <a href="https://github.com/asz798838958/aBaiAutoplus/network/members"><img src="https://img.shields.io/github/forks/asz798838958/aBaiAutoplus?style=for-the-badge&logo=github&color=blue" alt="Forks" /></a>
  <a href="https://github.com/asz798838958/aBaiAutoplus/releases"><img src="https://img.shields.io/github/v/release/asz798838958/aBaiAutoplus?style=for-the-badge&logo=github&color=green" alt="Release" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/asz798838958/aBaiAutoplus?style=for-the-badge&color=orange" alt="License" /></a>
</p>

<p align="center">
  <b>全程vibe coding，代码质量有所欠缺</b><br/>
  <b>ChatGPT plus的AI 平台账号自动注册与管理</b><br/>
  <b>协议 / 浏览器双模式 · PayPal浏览器注册+内置 GoPay 协议付款 ChatGPT Plus </b>
</p>

> ⚠️ **免责声明**：本项目仅供学习和研究使用，不得用于任何商业用途，也不得用于违反目标平台服务条款（ToS）的行为。使用本项目所产生的一切后果由使用者自行承担。

> 🙏 **致谢**：本项目基于 [`lxf746/any-auto-register`](https://github.com/lxf746/any-auto-register) 二次开发，在其插件化注册框架之上扩展了**PayPal 浏览器注册ChatGPT Plus** **GoPay 协议注册ChatGPT Plus** 等能力。感谢原作者的开源工作。本仓库与上游各自独立维护。

多平台账号自动注册与管理系统，支持插件化扩展，内置 Web UI 与桌面客户端。

## 目录

- [相比上游的新增能力](#相比上游的新增能力)
- [功能特性](#功能特性)
- [支持的平台](#支持的平台)
- [界面预览](#界面预览)
- [技术栈](#技术栈)
- [快速开始](#快速开始)
- [桌面版下载](#桌面版下载)
- [Docker 部署](#docker-部署)
- [GoPay 付款 ChatGPT Plus](#gopay-付款-chatgpt-plus)
- [邮箱服务配置](#邮箱服务配置)
- [验证码服务配置](#验证码服务配置)
- [代理池配置](#代理池配置)
- [接码服务配置](#接码服务配置)
- [账号生命周期管理](#账号生命周期管理)
- [注册成功率仪表盘](#注册成功率仪表盘)
- [Any2API 联动](#any2api-联动)
- [项目结构](#项目结构)
- [插件开发](#插件开发)
- [安全说明](#安全说明)
- [常见问题](#常见问题)
- [参与贡献](#参与贡献)
- [License](#license)

## 相比上游的新增能力

本项目在 [`any-auto-register`](https://github.com/lxf746/any-auto-register) 基础上重点扩展：

| 新增能力                       | 说明                                                                          |
| ------------------------------ | ----------------------------------------------------------------------------- |
| � **PayPal日区/美区 付款 ChatGPT Plus** | PayPal浏览器多线程付款，自动完成 ChatGPT Plus 订阅全链路 |
| � **GoPay 付款 ChatGPT Plus** | 印尼 GoPay 协议化付款，自动完成 ChatGPT Plus 订阅的「生成支付链接 → Midtrans 收银台 → GoPay 14 步 API 付款」全链路 |
| � **GoPay 账号自动注册**      | 印尼手机号 + PIN 协议注册 GoPay 账号，支持接码渠道轮换                         |
| 🧾 **接码渠道扩展**            | 在原有 SMS-Activate / HeroSMS 之外，新增 SMSPool、SMSBower 渠道                |
| 🌐 **C 端 / 管理端独立 API**   | `customer_portal_api/` 提供可独立部署的多租户门户后端                          |

> 其余平台注册、邮箱 / 验证码 / 代理 provider、生命周期管理、成功率仪表盘等能力沿用并兼容上游框架。

## 功能特性

- **多平台支持**：ChatGPT、Cursor、Kiro、Trae.ai、Tavily、Grok、Blink、Cerebras、OpenBlockLabs、Windsurf、GoPay，支持自定义插件扩展（Anything 通用适配器）
- **多邮箱服务**：MoeMail（自建）、Laoudo、DuckMail、Testmail、outlookEmail、Cloudflare Worker 自建邮箱、Freemail、TempMail.lol、Temp-Mail Web、DuckDuckGo Email
- **多执行模式**：API 协议（无浏览器）、无头浏览器、有头浏览器（各平台按需支持）
- **验证码服务**：YesCaptcha、2Captcha、本地 Solver（Camoufox）
- **接码服务**：SMS-Activate、HeroSMS、SMSPool、SMSBower
- **代理池管理**：静态代理轮询 + 动态代理 API 提取 + 旋转网关代理，成功率统计、自动禁用失效代理
- **账号生命周期**：定时有效性检测、token 自动续期、trial 过期预警
- **注册成功率仪表盘**：按平台、按天、按代理的成功率统计，错误聚合分析
- **并发注册**：可配置并发数
- **实时日志**：SSE 实时推送注册日志到前端
- **账号导出**：支持 JSON、CSV、CPA、Sub2API、Kiro-Go、Any2API 多种格式
- **Any2API 联动**：注册完成后自动推送账号到 Any2API 网关，注册即可用
- **平台扩展操作**：各平台可自定义操作（如 Kiro 账号切换、Trae Pro 升级链接生成、GoPay 付款 Plus）

## 支持的平台

| 平台          | 协议模式 | 浏览器模式 | OAuth | 备注                         |
| ------------- | :------: | :--------: | :---: | ---------------------------- |
| ChatGPT       |    ✅    |    ✅     |  ✅   | Plus 支付链接 / PayPal 结账  |
| Cursor        |    -    |     ✅     |  -   | 需手机验证                   |
| Kiro          |    -    |     ✅     |  -   | 支持账号切换                 |
| Trae.ai       |    -    |     ✅     |  -   | Pro 升级链接生成             |
| Grok          |    -    |     ✅     |  -   |                              |
| Windsurf      |    -    |     ✅     |  -   | Trial 链接生成               |
| Tavily        |    -    |     ✅     |  -   |                              |
| Blink         |    -    |     ✅     |  -   |                              |
| Cerebras      |    -    |     ✅     |  -   |                              |
| OpenBlockLabs |    -    |     ✅     |  -   |                              |
| GoPay         |    ✅    |     —      |  —    | 印尼 GoPay，手机 + PIN，付款 Plus |
| Anything      |    -    |     ✅     |  —    | 通用适配器，配置即接入新平台 |

> 各平台实际支持的执行器以插件 `supported_executors` 声明为准，可在 Web UI「平台能力」页查看与覆盖。

## 界面预览

> 📸 _截图将随版本迭代持续更新。_
### 交流联系方式

![联系方式](assets/screenshots/QQ群交流.jpg)

### gopay注册生成gptplus

![gopay注册生成gptplus](assets/screenshots/gopay注册生成gptplus.png)

### PayPal注册gptplus

![PayPal注册gptplus](assets/screenshots/PayPal注册gptplus.png)

### PayPal注册gptplus

![PayPal注册gptplus](assets/screenshots/PayPal注册gptplus2.png)

### 设置

![设置](assets/screenshots/设置2.png)
![设置](assets/screenshots/设置.png)

##