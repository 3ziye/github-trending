<h1 align="center">iLab GPT Conjure</h1>

<p align="center">
  <sub>GPT-image-2 WebUI 工作台 · Codex Image / OpenAI 兼容 API · 图库、模板、历史库与并发任务</sub>
</p>

<p align="center">
  <a href="https://github.com/kadevin/ilab-gpt-conjure/releases"><img alt="release" src="https://img.shields.io/github/v/release/kadevin/ilab-gpt-conjure?style=flat-square&logo=github&label=release&color=0EA5E9"></a>
  <a href="https://github.com/kadevin/ilab-gpt-conjure/actions/workflows/ci.yml"><img alt="CI status" src="https://github.com/kadevin/ilab-gpt-conjure/actions/workflows/ci.yml/badge.svg?branch=main&event=push"></a>
  <a href="https://github.com/kadevin/ilab-gpt-conjure/commits/main"><img alt="last commit" src="https://img.shields.io/github/last-commit/kadevin/ilab-gpt-conjure?style=flat-square&logo=github&label=last%20commit&color=10B981"></a>
  <a href="https://github.com/kadevin/ilab-gpt-conjure/stargazers"><img alt="stars" src="https://img.shields.io/github/stars/kadevin/ilab-gpt-conjure?style=flat-square&logo=github&label=stars&color=0284C7"></a>
  <a href="https://github.com/kadevin/ilab-gpt-conjure/network/members"><img alt="forks" src="https://img.shields.io/github/forks/kadevin/ilab-gpt-conjure?style=flat-square&logo=github&label=forks&color=0369A1"></a>
</p>

<p align="center">
  <img alt="license AGPL-3.0-only" src="https://img.shields.io/badge/license-AGPL--3.0--only-22C55E?style=flat-square">
  <img alt="Python 3.11+" src="https://img.shields.io/badge/python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="FastAPI WebUI" src="https://img.shields.io/badge/WebUI-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white">
  <img alt="CLI" src="https://img.shields.io/badge/CLI-enabled-334155?style=flat-square">
  <img alt="OpenAI-Compatible API" src="https://img.shields.io/badge/OpenAI--Compatible-API-111827?style=flat-square">
  <img alt="Advanced OAuth mode" src="https://img.shields.io/badge/local%20OAuth-advanced%20mode-B45309?style=flat-square">
</p>


<p align="center">
  中文 · <a href="README.en.md">English</a> · <a href="RELEASES.md">下载 / Releases</a>
</p>

<p align="center">
  <img src="assets/UI_cn.png" alt="iLab GPT Conjure WebUI 截图" width="960" />
</p>

## 简介

iLab GPT Conjure 是面向 GPT-image-2 的 AI 图片生成 WebUI 工作台，同时
提供 CLI 便于本地自动化。它支持默认 Codex Image 通道、Codex Responses
兼容通道与 OpenAI 兼容 API 接入，并内置公用图库、多类型 chip 快捷引用、
提示词模板、多任务并发、分页历史库和本地队列管理。

公开版推荐优先使用 OpenAI-compatible API 模式，通过你配置的供应商使用
Images API 或 Responses API 形态。

免安装一键包下载见 [下载 / Releases](RELEASES.md)。

## 功能

- 面向 GPT-image-2 的文生图、参考图生成和图像编辑工作流。
- 支持 Codex Image、Codex Responses 和 OpenAI 兼容 API 接入；公开或共享使用优先选择 API 模式。
- 多任务并发、本地队列状态、分页历史库、缩略图和结果归档。
- 独立 `/history` 页面支持 SQLite 分页、搜索、筛选、网格/列表视图和懒加载详情。
- Codex Responses 和 API Responses 生图可选启用联网搜索；生成页和历史库搜索支持提示词与任务 ID，并可命中历史任务。
- 单任务多图输出、部分失败处理和失败重试。
- 公用图库、最近参考图、颜色 chip、提示词片段 chip 和提示词模板。
- 图像编辑器支持插入输入框里的其他图片、多图层组合、默认锁定比例变换、
  Shift 自由变换、局部擦除和真实图层缩略图。
- 系统设置提供语言下拉菜单，支持简体中文、正體中文、繁体中文、日语、韩语、English、西班牙语、葡萄牙语、法语、德语、俄语、意大利语和印地语；首次启动自动跟随浏览器语言，手动选择后偏好保存在当前浏览器。
- 系统设置整合 API 设置、Codex 通道、语言 / Language、存储与通知四个 Tab；API 设置默认第一位。
- API 供应商以卡片快速选择，默认只读详情，支持显式编辑、复制、删除确认和多供应商排序。
- 免安装一键包启动脚本只负责本地启动；更新脚本需手动运行，会校验 SHA256、保留 `data/`，并把被替换文件备份到 `.backup/`。
- 高级本机 OAuth 工作流支持个人本地 Codex 使用，并明确提示接口风险。
- API 供应商配置，支持 Base URL、API Key、图像模型、调用方式和并发上限。
- CLI 支持生成、参考图、图像编辑、mask 和 dry-run。

## 认证模式

### 推荐：OpenAI-compatible API

稳定集成、团队使用、共享工作站或可能公开提供服务的场景，应使用 API 模式。
你可以在 WebUI 中配置 Base URL、API Key、模型名和调用方式。

### 高级本机模式：Codex / ChatGPT OAuth

本项目可选复用本机 Codex / ChatGPT OAuth 登录态，调用 ChatGPT 内部后端接口。
Codex 模式默认使用 Image 通道生成和编辑，也可在系统设置的 Codex 通道 Tab 切换到 Responses
兼容通道。该模式只面向个人本机工作流。

这不是 OpenAI 官方推荐的 API 集成方式。接口可能随时变更、失效，也可能受到
账号、产品或用量规则影响。生产环境、团队部署、公开服务或需要稳定性的场景，
应优先使用 OpenAI-compatible API 模式。

不要提交 OAuth 文件、API key、本地输入图、生成结果、任务 metadata、SQLite
数据库或调试日志。

## 环境要求

- Python 3.11 或更高版本。
- WebUI 依赖见 `requirements-webui.txt`。
- 修改 TypeScript 或 CSS 时需要 `package.json` 中的前端工具。

## 安装

```bash
git clone https://github.com/kadevin/ilab-gpt-conjure.git
cd ilab-gpt-conjure
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-webui.txt
```

## 启动 WebUI

macOS：

```bash
open "Start WebUI.command"
```

Windows：

```text
Start WebUI.bat
```

手动启动：

```bash
.venv/bin/python -m uvicorn codex_image.webui.app:app --host 127.0.0.1 --port 8787 --no-access-log
```

然后打开：

```text
http://127.0.0.1:8787/
```

## 免安装一键包

当前可用的一键包见 [下载 / Releases](RELEASES.md)，也可以直接打开
[GitHub Release v0.5.2](https://github.com/kadevin/ilab-gpt-conjure/releases/tag/v0.5.2)。

这些包面向希望像 ComfyUI 一样“解压即用”的用户：

1. 从下载页选择对应平台的 portable zip。
2. 解压到普通用户目录。
3. Windows 双击 `Start WebUI Portable.bat`；macOS 双击
   `Start WebUI Portable.command`。
4. 如果浏览器没有自动打开，手动访问 `http://127.0.0.1:8787/`。

一键包内包含打包好的 CPython、已安装的 WebUI 依赖、预构建的 WebUI 静态资源、
用于源码复构的前端 package 元数据和构建配置、应用源码、许可证文件，以及本地
`data/` 目录。设置、公用图库、输入图、输出图、任务数据库和日志都会写入 `data/`。

一键包启动脚本不会运行 `npm install`，也不会重建前端资源。只有你主动修改
TypeScript 或 CSS 并从源码重新生成 `codex_image/webui/static/app.js` 时，才需要
本机安装 Node.js。

