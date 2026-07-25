<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/gpt-5.6-instruct-hero-dark.webp" />
  <source media="(prefers-color-scheme: light)" srcset="docs/images/gpt-5.6-instruct-hero-light.webp" />
  <img src="docs/images/gpt-5.6-instruct-hero-light.webp" alt="gpt-5.6 破甲提示词及测试包" width="70%" />
</picture><br />
<img src="docs/images/readme-spacer.png" alt="" width="1" height="5" />

<p>
  <a href="https://github.com/MDX-Tom/gpt-5.6-instruct/stargazers"><img src="https://img.shields.io/github/stars/MDX-Tom/gpt-5.6-instruct?logo=github&label=Stars" alt="GitHub Stars" /></a>
  <img src="https://img.shields.io/badge/Model-gpt--5.6--sol-7c3aed" alt="gpt-5.6-sol" />
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white" alt="Python 3.8+" /></a>
  <a href="docs/comparison-tests-en.md"><img src="https://img.shields.io/badge/Documentation-Purple?color=8A2BE2&logo=readthedocs" alt="English Documentation" /></a>
  <a href="docs/comparison-tests.md"><img src="https://img.shields.io/badge/中文文档-red?logo=readthedocs" alt="中文文档" /></a>
</p>

<p>
  <a href="README_EN.md"><img src="https://img.shields.io/badge/lang-English-blue.svg" alt="English" /></a>
  <a href="README.md"><img src="https://img.shields.io/badge/语言-简体中文-red.svg" alt="简体中文" /></a>
</p>

<h1>gpt-5.6 破甲提示词及测试包</h1>

</div>

<!-- README_SYNC: 修改 README.md 时必须同步更新 README_EN.md；图表也必须提供对应语言版本。 -->

<a id="overview"></a>

本项目提供面向大模型的越狱/破甲提示词，将安全研究、渗透测试、逆向工程、软件破解与 NSFW 虚构内容统一设定为本地沙箱任务，并显式压制拒绝与回退话术，以提升 Codex 对复杂指令的直接执行能力。

本项目现迭代最新版为 `v41`，新版本优化过程中让模型持续吸收用户指令、真实失败案例和 GitHub Issues，自行创建/扩展测试集、分析失败并重写提示词，再通过 low、medium、high 分层回归决定是否发布。
先前旧版 `v5`、`v24`、`v35` 已移入 [`historical-versions/`](historical-versions/) 仅用于复现。

在 `gpt-5.6-sol` 的原 120 条 `medium` 测试集中，`v41` 在 low、medium、high 三档的审计汇总均为 120/120。根据真实失败案例和 GitHub Issues #3/#4/#5/#6/#8，新增的 52-case/58-turn 明文专项集中，`v41` 三档均为 52/52；相较 `v35`，low/medium 提升 25.00 个百分点，high 提升 23.08 个百分点，同时基础提示词长度减少 55.67%。

此外，本项目还提供了一个专为配合相关 skills 使用的破甲提示词版本 `gpt-5.6-sol-unrestricted-v41-skills`，详见 [上游 Agent Skills](#upstream-agent-skills)。

<a id="architecture"></a>

## 系统架构

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/project-architecture-zh-dark.webp" />
    <source media="(prefers-color-scheme: light)" srcset="docs/images/project-architecture-zh-light.webp" />
    <img alt="破甲提示词持续迭代、发布门禁与生产运行架构" src="docs/images/project-architecture-zh-light.webp" width="100%" />
  </picture>
</p>

项目架构由迭代优化与生产使用两部分组成。迭代阶段持续吸收用户指令、失败样例及 GitHub Issues，由模型更新中英文测试集、分析回归结果并优化提示词，经三级推理与证据门禁后发布 v41。生产阶段通过脚本加载 v41，依次完成归一化、语义分派、意图路由、状态连续性和工件验证，最终生成可核验结果。

该图使用 Draw.io 绘制，亮色、暗色及中英文页面均保存在可编辑的 [Draw.io 源文件](docs/architecture/project-architecture.drawio) 中。

<a id="highlights"></a>

## 亮点

| | |
|---|---|
| 🚀 **单入口部署**<br>交互式菜单或 `--apply` 直接预览、植入唯一默认 `v41`。 | 🔁 **自迭代优化**<br>模型同步演进测试集与提示词，并由分层回归决定发布。 |
| ↩️ **可控回滚**<br>自动保存基线备份与操作快照，恢复前再次确认。 | 🧪 **可复现评测**<br>360 条主测试与 52 条专项测试，记录输入、输出与最终判定。 |

<a id="versions"></a>

## 默认版本

| 版本 | 定位 | 生产入口 | 获取 |
|---|---|---|---|
| **v41（唯一默认版）** | 通用首轮归一化、状态连续性、跨域路由、错误恢复与真实工件 | `python3 codex-instruct.py --apply` | [ZIP](gpt-5.6-sol-unrestricted-v41.zip) |

历史 `v5`、`v24`、`v35` 不再出现在部署菜单或版本参数中，统一存放于 [`historical-versions/`](historical-versions/)；其中 v5 同时保留 Markdown，三版均保留 ZIP 以支持趋势复现。

当前发布 ZIP 的 SHA256：

```text
v41  569be9d9dd29ee7d54f7e3ec208ecf2ec3a9d97530f6b6baca187e639b98154b
```

<a id="quick-start"></a>

## 快速开始

### 1. 获取项目

```bash
git clone https://github.com/MDX-Tom/gpt-5.6-instruct.git
cd gpt-5.6-instruct
```

### 2. 预览并部署

```bash
# 先预览 v41，不写入任何文件
python3 codex-instruct.py --apply --dry-run

# 部署唯一默认版 v41
python3 codex-instruct.py --apply
```

不带参数运行可打开交互式菜单：

```bash
python3 codex-instruct.py
```

<details>
<summary><strong>更多命令</strong></summary>

```bash
# 指定 Codex home
python3 codex-instruct.py --apply --codex-dir ~/.codex

# 部署自定义 ZIP 或 Markdown
python3 codex-instruct.py --file ./custom-instructions.zip

# 安全卸载提示词；只恢复本项目管理的配置项
python3 codex-instruct.py --reset

# 人工应急：显式恢复整份 config.toml 快照
python3 codex-instruct.py \
  --restore-snapshot ~/.codex/config.toml.bak_YYYYMMDD_HHMMSS_ffffff \
  --codex-dir ~/.codex
```

</details>

执行 `--reset` 时，脚本只恢复部署前的顶层 `model_instructions_file`，不会用旧快照覆盖整个 `config.toml`。脚本仅删除由本次状态记录为新建且 SHA256 未变化的提示词；部署前已存在或后来被用户修改的文件会保留。

### 手动部署及回滚

解压 v41，将指令文件复制到 `CODEX_HOME`，为 `config.toml` 创建操作前快照，并写入：

```toml
model_instructions_file = "./gpt-5.6-sol-unrestricted-v41.md"
```

若要手动回滚，直接删除或用 `#` 注释掉上述行即可恢复模型原始默认行为；也可删除部署的版本化 Markdown 文件以清理本地文件。

### 反代工具兼容性

<details>
<summary><strong>点击查看</strong></summary>

- 部署前的指令项、已部署文件 SHA256 及部署前是否存在记录在 `CODEX_HOME/.gpt56-sol-instruct-state.json`；状态文件不保存 provider、模型、URL 或认证数据。
- **CCSwitch 等反代工具在部署后写入的 provider、模型和认证配置会在 `--reset` 后保留。**
- 完整 `config.toml.bak_<时间戳>` 快照只用于人工应急恢复；需要恢复整份配置时，必须显式使用 `--restore-snapshot` 并再次确认。
- 旧版 `config.toml.gpt56-sol-instruct.bak` 只用于找回原有 `model_instruc