# Any Auto Register

<p align="center">
  <a href="https://linux.do" target="_blank">
    <img src="https://img.shields.io/badge/LINUX-DO-FFB003?style=for-the-badge&logo=linux&logoColor=white" alt="LINUX DO" />
  </a>
</p>

> ⚠️ 免责声明：本项目仅供学习与研究使用，不得用于任何商业用途。使用本项目所产生的一切后果由使用者自行承担。

多平台账号自动注册与管理系统，支持插件化扩展、Web UI 管理、批量注册、状态同步，以及本地 Turnstile Solver 自动拉起。

## 目录

- [项目简介](#项目简介)
- [当前界面与实际平台展示](#当前界面与实际平台展示)
- [功能特性](#功能特性)
- [界面预览](#界面预览)
- [技术栈](#技术栈)
- [环境要求](#环境要求)
- [ChatGPT 专项能力](#chatgpt-专项能力)
- [邮箱服务支持](#邮箱服务支持)
- [快速开始](#快速开始)
- [Docker 部署](#docker-部署)
- [插件与外部依赖](#插件与外部依赖)
- [常见问题排查](#常见问题排查)
- [项目结构](#项目结构)
- [Electron 开发说明](#electron-开发说明)
- [License](#license)
- [用户讨论群](#用户讨论群)
- [打赏博主](#赞助支持)
- [Star History](#star-history)

## 项目简介

本仓库当前直接维护在 [Cong0707/any-auto-register](https://github.com/Cong0707/any-auto-register)。

代码基线主要同步自 [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register)，更早的历史来源追溯到 [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register.git)。

### 项目沿袭与改动来源

- 基础框架、平台插件体系、Web UI 与任务调度能力，沿袭自 `lxf746/any-auto-register` 和后续的 `zc-zhangchen/any-auto-register` 历史演进。
- Cloudflare Worker 临时邮箱接入思路，来源于 [dreamhunter2333/cloudflare_temp_email](https://github.com/dreamhunter2333/cloudflare_temp_email)。
- 当前分支上的 ChatGPT 注册链路修复，主要来自对 `dsclca12/auto_reg` 在 `2026-04-03` 的相关提交对比后手工缝合，而不是直接整体搬运。对应参考包括：
- `1b94a1f`：提交前预热页面、补 Cloudflare Cookie、增加自然延迟、修正 headless 行为。
- `663d39a`：验证码校验前的人类行为模拟，以及 `add_phone` / OTP 阶段的重试思路。
- `6d64389`：`about_you` 页面访问补 Cookie、workspace 获取补链路、验证码等待时间调整。
- 本仓库在此基础上另外加入了本地改动：`Browser -> VM` 的 Sentinel 重试顺序、`user_already_exists` 后切换验证码登录、上一枚 OTP 优先复用、consent HTML 中的 workspace 抽取日志与回退逻辑。

## 当前界面与实际平台展示

根据当前前端代码与界面，**左侧“平台管理”菜单默认显示的平台**为：

- ChatGPT
- Grok
- Kiro (AWS Builder ID)
- OpenBlockLabs
- Trae.ai



## 功能特性

- **多平台账号注册与管理**：统一的账号列表、详情、导入、导出、删除、批量操作
- **多执行器模式**：纯协议、无头浏览器、有头浏览器
- **多邮箱服务接入**：支持内置、第三方、自建 Worker 邮箱等多种方案
- **验证码支持**：YesCaptcha、本地 Turnstile Solver（Camoufox）
- **代理能力**：代理池轮询、代理状态维护、注册过程代理接入
- **批量注册**：支持注册数量、并发数、每个账号启动延迟设置
- **实时日志**：前端实时查看注册日志
- **任务历史管理**：支持历史记录查看与批量删除
- **插件化扩展**：可按需接入外部服务和独立管理端

## 界面预览

### 仪表盘

![仪表盘](docs/images/dashboard.png)

### 全局配置 / 插件管理

![全局配置 / 插件管理](docs/images/settings-integrations.png)

## 技术栈

| 层级 | 技术 |
| --- | --- |
| 后端 | FastAPI + SQLite（SQLModel） |
| 前端 | React + TypeScript + Vite |
| HTTP | curl_cffi |
| 浏览器自动化 | Playwright / Camoufox |

## 环境要求

- Python 3.12+
- Node.js 18+
- Conda（推荐）
- Windows（推荐直接使用仓库内启动脚本）

## ChatGPT 专项能力

当前版本里，**ChatGPT 是功能最完整的平台之一**，不仅支持注册，还支持 Token 生命周期管理、状态探测和外部系统同步。

### 1. ChatGPT Token 方案切换

前端当前提供两种 ChatGPT 注册模式：

- **有 RT**（默认推荐）
  - 走新 PR 链路
  - 产出 **Access Token + Refresh Token**
- **无 RT**（兼容旧方案）
  - 走旧链路
  - 仅产出 **Access Token / Session**
  - 依赖 RT 的后续能力可能不可用

这项切换在以下位置都能看到：

- 注册任务页
- ChatGPT 平台注册弹窗



### 4. ChatGPT 批量状态同步与补传

在 ChatGPT 平台列表顶部，当前还有两类批量能力：

- **状态同步**
  - 同步所选账号本地状态
  - 同步所选账号 CLIProxyAPI 状态
  - 或对当前筛选结果批量执行
- **补传远端未发现**
  - 补传远端未发现的 auth-file
  - 支持“当前筛选范围”或“当前所选账号”两种作用范围

## 邮箱服务支持

根据当前注册页实际配置项，项目支持以下邮箱服务：

| 服务名称 | 标识 | 说明 |
| --- | --- | --- |
| LuckMail | `luckmail` | 可免费领取 **125 个邮箱**用于测试，且**每天签到还能继续领取邮箱**；可通过 [https://mails.luckyous.com/9331211B](https://mails.luckyous.com/9331211B) 进入，支持博主获得少量赏金，用于维持开源测试 |
| MoeMail | `moemail` | 默认常用方案，自动注册账号并生成邮箱 |
| TempMail.lol | `tempmail_lol` | 临时邮箱方案，部分地区可能需要代理 |
| SkyMail (CloudMail) | `skymail` | 通过 API / Token / 域名使用 |
| CloudMail (genToken) | `cloudmail` | 通过管理员邮箱/口令获取 token，直接轮询 `emailList` |
| YYDS Mail / MaliAPI | `maliapi` | 支持域名与自动域名策略 |
| GPTMail | `gptmail` | 基于 GPTMail API 生成临时邮箱并轮询邮件，支持已知域名时本地拼装随机地址 |
| OpenTrashMail | `opentrashmail` | 对接自建 OpenTrashMail 服务，支持 `/api/random` 自动取号，也支持配置域名后本地拼装随机地址 |
| DuckMail | `duckmail` | 临时邮箱方案 |
| Freemail | `freemail` | 自建邮箱服务，支持指定域名生成 |
| Laoudo | `laoudo` | 固定邮箱方案 |
| CF Worker | `cfworker` | Cloudflare Worker 自建邮箱 |

### Kiro 邮箱说明

Kiro 当前风控较严格，邮箱方案会显著影响成功率。当前项目内也保留了这条重点提示：

- **自建邮箱成功率：100%**
- **项目内置临时邮箱成功率：0%**

因此进行 **Kiro (AWS Builder ID)** 注册时，建议优先使用**自建邮箱**。

## 快速开始

### 1. 创建并激活 Conda 环境

```bash
conda create -n any-auto-register python=3.12 -y
conda activate any-auto-register
```

### 2. 安装后端依赖

```bash
pip install -r requirements.txt
```

### 3. 安装浏览器相关依赖

```bash
python -m playwright install chromium
python -m camoufox fetch
```

### 4. 安装并构建前端

```bash
cd frontend
npm install
npm run build
cd ..
```

构建完成后，静态资源输出到：

```text
./static
```

### 5. 启动项目

#### Windows 推荐方式

PowerShell：

```powershell
.\start_backend.ps1
```

CMD：

```bat
start_backend.bat
```

#### 手动启动

```bash
conda activate any-auto-register
python main.py
```

启动后默认访问：

```text
http://localhost:8000
```

> 如果你已经执行过 `npm run build`，前端会由 FastAPI 直接托管，因此访问的是 `8000`，不是 `5173`。

## Windows 启动脚本说明

仓库内已提供以下脚本：

- `start_backend.bat`
- `start_backend.ps1`
- `stop_backend.bat`
- `stop_backend.ps1`

这些脚本会强制使用 `any-auto-register` 环境启动/停止后端，可避免以下常见问题：

- 后端能启动，但 Solver 没有拉起
- `ModuleNotFoundError: quart`
- 前端中 Turnstile Solver 一直显示“未运行”

停止服务时可执