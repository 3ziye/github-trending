<p align="center">
  <img src="docs/assets/social-preview.png" alt="CSSwitch" width="760">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License">
  <a href="https://github.com/SuperJJ007/CSSwitch/releases/tag/v0.6.0"><img src="https://img.shields.io/badge/release-v0.6.0-2ea44f.svg" alt="CSSwitch v0.6.0"></a>
  <img src="https://img.shields.io/badge/platform-macOS%20Apple%20Silicon-1d1d1f.svg" alt="macOS Apple Silicon">
  <img src="https://img.shields.io/badge/built%20with-Tauri%202-C25A34.svg" alt="Tauri 2">
</p>

<p align="center">
  <a href="./README.md">简体中文</a> ·
  <a href="./README.en.md">English</a>
</p>

# CSSwitch

CSSwitch 是一个给 Claude Science 使用的本地配置转换器。它把 Science 的推理请求转换并接入你自己的模型 API，可配置 DeepSeek、通义千问、Kimi、MiniMax、GLM、OpenRouter、中转站或自定义兼容端点。

它面向的不只是开发者：你只需要准备 Claude Science、一个第三方 API Key，然后在桌面面板里新建配置、设为当前、点击「一键开始」。

> 当前版本主要支持 macOS Apple Silicon。首次打开未公证的 `.dmg` 应用时，macOS 可能需要你右键选择「打开」。

[下载最新版](../../releases/latest) · [项目文档](./docs/README.md) · [更新日志](./CHANGELOG.md) · [报告问题](https://github.com/SuperJJ007/CSSwitch/issues/new?template=bug_report.yml) · [功能建议](https://github.com/SuperJJ007/CSSwitch/issues/new?template=feature_request.yml)

> **0.6.0：** 外部 Skill 安装现在支持准确的公开 GitHub URL 和主面板本地 `.zip` / `.skill` 两条路线；GitHub 慢下载提供单请求进度、终态清理和重启中断恢复。bundle 从任意成员卸载时，必须先返回完整受影响 Skill 列表并由用户确认整包卸载，不做部分物理删除。v0.5.0 的旧 connector 路由会自动迁移，用户 MCP 配置和未知字段保持原样。详见[外部 Skill bridge](./docs/features/external-skill-bridge.md)、[系统 SSH](./docs/features/system-ssh.md)和[架构说明](./docs/architecture/overview.md)。

## 目录

- [为什么需要 CSSwitch](#为什么需要-csswitch)
- [可以做什么](#可以做什么)
- [快速开始](#快速开始)
- [安装和卸载外部 Skill](#安装和卸载外部-skill)
- [从旧版升级](#从旧版升级)
- [支持的模型来源](#支持的模型来源)
- [状态诊断与能力 catalog](#状态诊断与能力-catalog)
- [它如何保护你的真实账号](#它如何保护你的真实账号)
- [哪些能力暂时用不了](#哪些能力暂时用不了)
- [多语言](#多语言)
- [开发与构建](#开发与构建)
- [风险与免责声明](#风险与免责声明)

## 为什么需要 CSSwitch

Claude Science 是 Anthropic 面向科研与分析场景的 AI Agent 应用，可以做文献分析、数据处理、代码执行、图表生成和论文写作等工作。但 Science 默认依赖 Claude 登录和 Anthropic 推理服务。

CSSwitch 做的是本地运行控制：

- 在隔离环境里启动 Claude Science。
- 在独立的本地工作区中运行第三方模型模式，不接管你的真实 Claude 账号。
- 把 Science 的模型请求转发到你选择的第三方 provider。
- 在需要时把 Anthropic Messages API 和 OpenAI 兼容接口互相转换。
- 保留「官方 Claude」模式，可随时切回 Science 的官方服务配置。

简单理解：CSSwitch 之于 Claude Science，类似 CC Switch 之于 Claude Code，并额外管理桌面应用、隔离工作区与本地网关。

```text
Claude Science sandbox
  -> CSSwitch local proxy
  -> DeepSeek / Qwen / Kimi / MiniMax / GLM / OpenRouter / custom endpoint
```

## 可以做什么

**给普通用户**

- 用桌面面板管理多套模型配置，不需要手改环境变量。
- 同一家 provider 可以保存多套配置，例如不同 Key、不同模型、不同中转地址。
- 点击「设为当前」前会先验证 Key；失败不会悄悄切换到坏配置。
- 点击「一键开始」会自动启动代理、准备隔离环境、打开 Science。
- Science 顶部模型选择器会显示你选择的真实模型名，而不是笼统的 `claude` 或 `opus`。
- 可以一键切回「官方 Claude」模式，不干扰你的真实 Claude 登录。
- 复用 Science 的持久化 data-dir；Skill 状态不阻塞 CSSwitch 启动。0.6.0 可从准确的公开 GitHub URL 或本地 `.zip` / `.skill` 安装单 Skill/bundle；bundle 卸载必须整包确认并只隔离 CSSwitch 自己的导入。
- CSSwitch 默认继承 `/Applications/Claude Science.app` 中用户当前安装的 Science，不比较、固定、升级或降级版本；更新 App 后，下次启动继续复用原 data-dir 并使用更新后的 App executable。
- 如果 Science App 缺失，CSSwitch 不会静默启动 data-dir 中的旧缓存。只有缓存可执行且版本可确认时，UI 才允许“仅本次使用缓存版本”；该选择不保存。否则只能打开 [Claude 官方下载页](https://claude.com/download) 安装 / 更新或取消。

**给进阶用户**

- 支持原生 Anthropic 兼容端点、OpenAI Chat Completions 兼容端点、OpenAI Responses 兼容端点。
- 支持自定义 `base_url`、模型名和中转站。
- DeepSeek、Kimi、MiniMax 等原生 Anthropic 端点优先透传，尽量保留工具调用、thinking 和流式响应。
- Qwen 与自定义 OpenAI 端点通过本地代理做协议转换。
- 配置和日志都保存在本机，便于自查和反馈。

## 快速开始

开始之前，请确认你已经安装：

- [Claude Science（Claude 官方下载页）](https://claude.com/download)
- macOS Apple Silicon 设备
- 一个可用的第三方模型 API Key
- CSSwitch 已内置 Rust inference gateway，无需另外安装 Python 运行时

1. 从 [GitHub Releases](../../releases/latest) 下载最新的 `CSSwitch_*.dmg`。
2. 将 CSSwitch 拖入「应用程序」。
3. 第一次打开如果被 Gatekeeper 拦截，请右键应用并选择「打开」。
4. 保持顶部模式为「第三方模型」。
5. 点击「+ 新建」，选择 provider，填写 API Key、模型和必要的 `base_url`。
6. 点击「创建」，再在配置列表中点击「设为当前」。
7. 验证通过后点击「一键开始」。
8. CSSwitch 会启动隔离 Science，并在浏览器中打开入口。

CSSwitch 不替你选择 Science 版本。正常启动使用当前安装的 Claude Science App；如果 App 缺失，面板会据实显示可确认的历史缓存版本并要求你明确选择“仅本次使用”，或打开官方下载页安装 / 更新。缓存选择不会写入配置；以后检测到 App 时会自动恢复使用 App。

如果你想使用 Science 的官方服务配置，切到「官方 Claude」模式即可。CSSwitch 会停止第三方代理链路，再打开真实 Science。

## 安装和卸载外部 Skill

CSSwitch 0.6.0 提供 GitHub 和本地文件两条安装路线。两条路线使用相同的路径、大小、符号链接和保留文件校验，并在安装后把 Skill 原生绑定到 Science 的默认 Agent。安装器不会替你登录 GitHub，也不会读取或接管 Science 凭证。

**从公开 GitHub URL 安装**

1. 在 CSSwitch 中完成「一键开始」，然后打开一个新的 Science 对话。
2. 把准确的公开 GitHub tree URL 发给 Agent，并明确要求使用 CSSwitch 外部 Skill 安装器。例如：

   ```text
   请使用 CSSwitch 外部 Skill 安装器安装这个固定提交，只发起一次请求，不要自动重试：
   https://github.com/<owner>/<repo>/tree/<commit>/<path>
   ```

3. Science 请求访问 CSSwitch bridge 目录时，核对路径后批准本次读写授权。
4. 下载期间等待同一个请求继续推进，不要重复发送安装指令。成功后，单 Skill 会要求在当前会话做一次加载验证；bundle 会报告完整成员数量和绑定结果。

推荐使用固定 commit URL，便于复用和核对。公开仓库的根目录 bundle 也可以使用 `.../tree/<commit>`。私有仓库、名称搜索、覆盖更新和 Skill 发布不在当前范围内。

**从本地文件安装**

1. 保持隔离 Science 正在运行且状态正常。
2. 在 CSSwitch 主面板点击「导入 Skill 包」。
3. 选择 `.zip` 或 `.skill` 文件。支持 archive 根目录直接包含 `SKILL.md`、唯一外层 Skill 目录，以及包含多个直接 Skill 子目录和可选 `_shared` 的 bundle。
4. CSSwitch 校验、原子写入并绑定后，在新的 Science 对话中加载对应 S