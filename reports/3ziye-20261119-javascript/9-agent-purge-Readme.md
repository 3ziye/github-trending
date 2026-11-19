<div align="center">

<p>
  <img src="web/assets/logo.svg" width="72" height="72" alt="agent-purge logo" />
</p>

# agent-purge

**一份人设，统一接管本机多个 coding agent。**

[English](README.en.md) | [日本語](README.ja.md) | 简体中文

[![npm](https://img.shields.io/npm/v/agent-purge)](https://www.npmjs.com/package/agent-purge)
[![stars](https://img.shields.io/github/stars/ZiChuanLan/agent-purge)](https://github.com/ZiChuanLan/agent-purge/stargazers)
[![license](https://img.shields.io/npm/l/agent-purge)](LICENSE)

<p>
  <a href="https://trendshift.io/repositories/321425?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-321425" target="_blank" rel="noopener noreferrer">
    <img src="https://trendshift.io/api/badge/trendshift/repositories/321425/daily?language=JavaScript" alt="ZiChuanLan/agent-purge | Trendshift" width="250" height="55"/>
  </a>
</p>

[文档站](https://zichuanlan.github.io/agent-purge/) · [快速开始](#快速开始) · [界面一览](#界面一览) · [人设与模式](#人设与模式) · [应用范围](#应用范围) · [支持情况](#支持情况) · [暂停与卸载](#暂停与卸载) · [免责与合规声明](#免责与合规声明)

</div>

agent-purge 是一个本地提示词与人设编排控制台，为 Pi、Codex、Claude Code、OpenCode、Qwen Code、Kiro CLI 等执行器提供统一的人设管理入口。你可以在浏览器控制台中点击切换，也可以直接用命令行启动；每个宿主仍完整保留自己的模型、工具与工作流。

## 核心能力

- **一份人设，多端入口**：CLI 与 Web 共用同一份人设库与账本，支持单次启动、常驻配置、会话内 `/purge` 热切与按目录写入项目规则。
- **能力诚实、分家自治**：默认跟随全局人设与改写力度，也可按工具单独覆写；界面严格按各家实测支持度展示可用通道与力度，不摆假开关。
- **支持热切，也明示边界**：Pi / omp / OpenCode / dsh 等具备每轮回调的动态通道下一轮即生效；静态配置或启动参数入口明示需新开会话。
- **文件共享与原子可逆**：项目规则按 `AGENTS.md` / `CLAUDE.md` / `QWEN.md` 文件共享托管，支持写入前 diff 预览与 SHA 冲突检测；每次写入均保留原字节 `stash` 快照，随时可逐位撤回。
- **零生产依赖、本地优先**：无外部后端、不上传配置，数据保存在独立目录（默认 `~/.agent-purge/`），升级不覆盖用户人设。

## 快速开始

需要 **Node.js 20+**，并先在本机安装你要管理的 coding agent。

```bash
npm install -g agent-purge
agent-purge web
```

也可以直接运行 `npx agent-purge web`，无需全局安装。

1. 在 **「人设库」** 编辑起步模板或新建人设（支持从 GitHub 仓库或本地目录批量拉取）。
2. 回到 **「控制台」** 选择人设与默认力度、保存设置，打开目标工具开关或点开右侧详情工作区调优通道。
3. 在 **「规则文件」** 为指定项目目录或全局配置目录追加规则块（默认在原文件末尾 append，随时可无损移除）。

控制台默认监听 `http://127.0.0.1:7788`；若端口被系统保留或占用，会自动顺延至 `7890–7909` 空闲端口并打开独立桌面窗口。桌面端是单例：重复双击只会把已打开的窗口叫到前台，不会再开第二个服务或第二个页面；关窗行为（退出/留在后台、是否需要确认）与 WebDAV 备份在「设置」页调整，改完立即生效。首次启动不会自动接管任何工具。

## 界面一览

![agent-purge 控制台总览](docs/images/console-desktop.png)

![agent-purge 工具详情与安全试跑](docs/images/console-detail.png)

系统提示词接管在 **「控制台」**；项目目录及各家全局规则文件（`AGENTS.md` / `CLAUDE.md` / `QWEN.md` / `CRUSH.md` / `.clinerules` / `.roorules`）统一在 **「规则文件」** 页按作用范围与指定人设写入。

![agent-purge 规则文件](docs/images/project-rules.png)

[查看移动端窄屏布局](docs/images/console-mobile.png)

<details>
<summary>其他安装方式：Windows 安装器、便携包与无桌面环境</summary>

| 形式 | 运行要求 | 适用场景 |
|---|---|---|
| npm | Node.js 20+ | 用 npm 安装与升级 |
| `agent-purge-<版本>-setup.exe` | Windows，外部 Node.js 20+ | 图形安装和卸载 |
| `agent-purge-<版本>.zip` | Windows，外部 Node.js 20+ | 解压后使用 |
| `agent-purge.exe` | Windows x64，自带运行时 | 无需另装 Node 的独立便携版 |
| `agent-purge-<版本>-darwin-arm64.dmg` / `x64.dmg` | macOS 12+（Apple Silicon / Intel，自带运行时） | 未签名 `.app` 磁盘镜像，拖入 `/Applications` 后首次需右键「打开」或 `xattr -cr` 放行 |
| `agent-purge-<版本>-linux-x64` / `-linux-arm64` | 主流 Linux 发行版（自带运行时） | 单文件二进制，`chmod +x` 后直接运行 |
| `agent-purge-<版本>-linux-<架构>.tar.gz` | 主流 Linux 发行版 | 便携包，含 `.desktop`、图标与免 root 的 `install.sh` |
| `agent-purge-<版本>-linux-<架构>.deb` | Debian / Ubuntu 及衍生版 | `sudo apt install ./*.deb`，注册 `/usr/bin/agent-purge` 与桌面入口 |
| `agent-purge-<版本>-linux-<架构>.AppImage` | 主流 Linux 发行版（存在时才有） | 双击或用 `--appimage-extract-and-run` 直接启动控制台 |

下载附件以实际 [GitHub Releases](https://github.com/ZiChuanLan/agent-purge/releases) 为准；未发布的版本没有附件。请核对 SHA-256 和签名状态，未签名程序可能出现系统提示。ZIP 中的 EXE 是薄启动器，不是自带运行时的独立版。

SSH / WSL 等无桌面环境使用 `agent-purge web --no-open`。Web 仅监听本机；Linux 可用 npm / 源码入口或 Release 里的二进制、`.tar.gz`、`.deb`（AppImage 随 runner 能力可选生成），macOS 可用 npm / 源码或 `.dmg` 镜像（`.dmg` 未经 Apple 签名与公证）。平台验证范围见[兼容性说明](docs/reference/compatibility.md)。

控制台右上角的版本角标点开就是升级入口，按安装形态自动选路：独立 EXE 下载并就地热替换、npm 全局安装调 `npm install -g`、**源码检出（`git clone` 后直接 `node bin/agent-purge.mjs`）在安装目录执行 `git pull --ff-only`**，不下载任何发布产物。源码检出的「有没有更新」按上游提交算，版本号没变也会提示；工作区有未提交改动、处于游离 HEAD 或分支没有上游时一律拒绝并说明原因。

</details>

## 人设与模式

人设正文决定要提供给执行器的提示词；名称和说明只用于管理。首次运行会生成 `neutral` 起步模板，你可以在 Web 中直接编辑，也可以创建自己的 Markdown 文件。

```bash
agent-purge ls                       # 查看人设
agent-purge use <id>                 # 切换并同步已选范围
agent-purge mode append              # 修改全局模式
agent-purge use <id> --for codex     # 只给 Codex 指定人设
agent-purge use follow --for codex   # 恢复跟随全局
```

### 四种处理模式

| 模式 | 行为 | 注意 |
|---|---|---|
| `replace`（默认） | 优先替换宿主身份行，尽量保留其他说明 | 身份识别是近似处理；无法读取宿主文本的启动入口按 strict 执行 |
| `strict` | 用人设替换可控入口中的宿主文本 | 该入口原有说明也会移除；宿主仍可能添加额外文本 |
| `append` | 保留宿主说明，另加一份人设 | 不替换原身份，需注意规则冲突 |
| `off` | 停止相应入口注入 | 全局暂停与单次启动参数的作用范围不同 |

**strict 不等于“模型只收到人设”。** 实际角色可能是 `system`、`developer` 或项目上下文，取决于宿主和通道。希望保留宿主说明时，可先试 `append`。

<details>
<summary>手写人设示例与存储位置</summary>

将以下内容保存为 `~/.agent-purge/personas/concise.md`，然后执行 `agent-purge use concise`：

```markdown
---
id: concise
name: 简洁协作
description: 中文、先结论、修改前先读代码
---

用简体中文协作。先给结论，再给依据。
修改代码前先阅读现有实现；不确定时明确说明。
```

只有正