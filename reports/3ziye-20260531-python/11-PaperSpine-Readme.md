# PaperSpine

[English](README.en.md) | [中文](README.md)


[**PaperSpine 使用讲解视频（Bilibili）**](https://www.bilibili.com/video/BV1rjVa6ZEYu)


> PaperSpine 是一个面向 Codex、Claude Code 和 OpenClaw 的、以 motivation 为主线的论文与报告写作 skill suite。

它适合目标格式很重要的写作任务：期刊论文、会议论文、课程或技术报告、综述、竞赛论文。它要求 agent 在写作前先学习目标场景和优秀样例，再记录每一个写作单元为什么这样规划或修改。

## 仓库结构

```text
PaperSpine/
  dist/
    codex/
      skills/                   # Codex 扁平 skill suite
      paper-spine/              # 旧版 Codex 自包含兼容包
    claude/
      skills/                   # Claude Code 扁平 skill suite
        paper-spine/
        paper-spine-ui/
        paper-spine-intake/
        paper-spine-research/
        paper-spine-citation/
        paper-spine-rewrite/
        paper-spine-build/
        paper-spine-latex/
        paper-spine-audit/
        paper-spine-translate/
        paper-spine-humanize/
        paper-spine-update/
      commands/                 # Claude Code slash-command 辅助入口
        paperspine.md
        paper-spine.md
        paperspine-legacy.md
    openclaw/
      skills/                   # OpenClaw 扁平 skill suite
  src/
    scripts/                    # 共享的确定性辅助脚本
    references/                 # 共享工作流参考文档
    agents/                     # 共享 agent 元数据源
  .claude-plugin/               # Claude Code 插件元数据
  install.ps1                   # Windows 安装脚本
  install.sh                    # macOS / Linux 安装脚本
  README.md
  README.en.md
```

`dist/` 是真正用于安装的内容。`src/` 保留共享脚本和参考文档，便于开发与维护。

## 快速安装

Windows PowerShell:

```powershell
git clone https://github.com/WUBING2023/PaperSpine.git
cd PaperSpine
.\install.ps1 -Target all
```

也可以只安装某一端：

```powershell
.\install.ps1 -Target codex
.\install.ps1 -Target claude
.\install.ps1 -Target openclaw
.\install.ps1 -Target all -CleanLegacy
```

`-CleanLegacy` 会清理常见的旧 PaperSpine 目录，例如嵌套的 `PaperSpine`、`PaperSpineV2` 和旧的 `paper-spine-*` 副本，避免重复发现或找不到 skill。

安装到 Codex 后：**Restart Codex**。然后用 `$paper-spine` 启动全流程，或单独调用 `$paper-spine-research`、`$paper-spine-citation`、`$paper-spine-latex` 等分支 skill。

安装到 Claude Code 后：重启或 reload Claude Code，然后使用 `/paperspine`。

安装到 OpenClaw 后：重启或 reload OpenClaw，然后用 `paper-spine` 启动全流程，或调用任意 `paper-spine-*` 分支 skill。

安装脚本会把当前版本记录到 `~/.paperspine/install_state.json`，并保留 `~/.paperspine/config.json`，包括 UI 语言等全局配置。

## 手动安装

Codex 现在推荐使用扁平 suite，这样每个分支都可以被单独调用：

```text
dist/codex/skills/*
```

复制到：

```text
~/.codex/skills/
```

最终 Codex 布局应该是：

```text
~/.codex/skills/paper-spine/SKILL.md
~/.codex/skills/paper-spine-research/SKILL.md
~/.codex/skills/paper-spine-citation/SKILL.md
~/.codex/skills/paper-spine-latex/SKILL.md
~/.codex/skills/paper-spine-update/SKILL.md
```

`dist/codex/paper-spine` 仍保留为旧版自包含兼容包，但推荐的新安装方式是 `dist/codex/skills/*`。

Claude Code 需要扁平 skill 文件夹和可选 slash commands：

```text
dist/claude/skills/*
dist/claude/commands/*.md
```

复制到：

```text
~/.claude/skills/
~/.claude/commands/
```

最终 Claude Code 布局应该包含：

```text
~/.claude/skills/paper-spine/SKILL.md
~/.claude/skills/paper-spine-ui/SKILL.md
~/.claude/skills/paper-spine-intake/SKILL.md
~/.claude/skills/paper-spine-research/SKILL.md
~/.claude/skills/paper-spine-citation/SKILL.md
~/.claude/skills/paper-spine-update/SKILL.md
~/.claude/commands/paperspine.md
```

OpenClaw 需要包含 `SKILL.md` 的 skill 文件夹：

```text
dist/openclaw/skills/*
```

复制到：

```text
~/.openclaw/skills/
```

最终 OpenClaw 布局应该包含：

```text
~/.openclaw/skills/paper-spine/SKILL.md
~/.openclaw/skills/paper-spine-research/SKILL.md
~/.openclaw/skills/paper-spine-citation/SKILL.md
~/.openclaw/skills/paper-spine-update/SKILL.md
```

## Claude Code 插件安装

Claude Code 也可以使用 `.claude-plugin` 中的插件元数据：

```text
/plugin marketplace add https://github.com/WUBING2023/PaperSpine
/plugin install paper-spine
/reload-plugins
```

插件 manifest 指向 `dist/claude/skills` 下的扁平 suite，而不是 Codex 的单 skill 目录。

## Codex、Claude Code 与 OpenClaw 的差异

| 宿主 | 安装单元 | 常用入口 | 原因 |
| --- | --- | --- | --- |
| Codex | `dist/codex/skills/*` | `$paper-spine` 或 `$paper-spine-*` | Codex 可以发现扁平 skill 文件夹，因此全流程和子 skill 都能调用。 |
| Claude Code | `dist/claude/skills/*` 加 `dist/claude/commands/*` | `/paperspine` | Claude Code 按扁平文件夹发现 skills，并支持 slash-command 辅助入口。 |
| OpenClaw | `dist/openclaw/skills/*` | `paper-spine` 或 `paper-spine-*` | OpenClaw skill 也是包含 `SKILL.md` 的目录，因此使用同一套扁平 suite。 |

不要把整个仓库直接复制进 `skills` 文件夹。这是重复或缺失 skill 的主要原因。

## 主工作流

PaperSpine 有两条平级主流程：

1. **Rewrite Existing**：改进已有论文或报告，但不把任务降级成简单润色。
2. **Build From Materials**：从素材文件夹构筑论文或报告，素材可以包括说明文档、图片、PDF、数据摘要、部分初稿和实验描述。

支持四类目标场景：

- `journal`：期刊论文
- `conference`：会议论文
- `report/review`：课程报告、技术报告或综述
- `competition`：竞赛论文或竞赛报告

研究深度：

- `flash`：3 篇目标场景样例、3 篇近期/高质量同领域论文和官方要求。
- `pro`：6 篇目标场景样例、6 篇近期/高质量同领域论文和官方要求。

输出语言：

- `English`
- `Chinese`

选择英文输出时，PaperSpine 还可以生成 `translation_package`，把中间产物和最终 Markdown 产物翻译为中文。

## 主控与分支 Skill

PaperSpine 由一个主控 skill 加多个分支 skill 组成。主控 `paper-spine` 不直接修补句子，而是逐阶段路由：

1. `paper-spine-ui`：打开外部终端配置 UI。
2. `paper-spine-intake`：校验 `paper_spine_config.json`。
3. `paper-spine-research`：学习目标场景、本地/指定参考资料和优秀样例。
4.