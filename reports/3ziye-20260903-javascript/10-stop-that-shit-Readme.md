<p align="center">
  <img src="assets/stop-stamp.svg" alt="Stop That Shit（别再造史了）AI Agent 任务边界 Guard 的红色 STOP 印章" width="240">
</p>

<h1 align="center">Stop That Shit（别再造史了）</h1>

<p align="center">
  <a href="https://github.com/lennney/stop-that-shit/releases"><img src="https://img.shields.io/github/v/release/lennney/stop-that-shit?include_prereleases&sort=semver&style=flat-square&color=111111&label=release" alt="最新版本"></a>
  <a href="https://github.com/lennney/stop-that-shit/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/lennney/stop-that-shit/ci.yml?branch=main&style=flat-square&label=build" alt="构建状态"></a>
  <img src="https://img.shields.io/github/license/lennney/stop-that-shit?style=flat-square&color=111111" alt="MIT 许可证">
</p>

<p align="center">
  <strong>你只让 Agent 导出一个结果文件。它顺手又生成一份 SHA-256 校验和，但后面没有任何命令会读取它。Stop That Shit。</strong><br>
  Stop That Shit（别再造史了）处理 AI coding agent 自己加出来的防御性工作和任务越界。<br>
  支持 <a href="INSTALL.md#codex-skill--guard">Codex</a>、<a href="INSTALL.md#claude-code-skill--guard">Claude Code</a>、<a href="INSTALL.md#opencode-install-from-github">OpenCode</a>、<a href="INSTALL.md#hermes-agent-cli">Hermes Agent CLI</a> 和 <a href="INSTALL.md#pi-coding-agent">Pi</a>。<br>
  <a href="#快速安装">安装</a> ·
  <a href="#bad-case--good-case">Bad / Good Case</a> ·
  <a href="cases/README.md">案例库</a> ·
  <a href="#020从多做一步到多说一句">0.2.0</a> ·
  <a href="CONTRIBUTING.md">参与贡献</a> ·
  <a href="README_EN.md">English</a>
</p>

这份校验和生成了，任务却没有少做一步，后面的流程也完全一样。换个任务，多出来的可能是 guard、兼容层、全量测试或额外流程。Codex、Claude Code、OpenCode、Hermes Agent CLI 和 Pi 都可能这么做：每一步单看都有理由，但用户没要求，当前任务也用不上。

我也试过不断往 `AGENTS.md` 里补「不要乱改」「别过度设计」「没让我做的先别做」。规则越补越长，`AGENTS.md` 自己也开始造史。Stop That Shit 把其中能明确判断的边界做成 Skill 和可执行 Guard。

你用 `review`、`change` 等模式写明授权，再按需限制文件、依赖、hash 和 subagent
预算。Stop That Shit 在受覆盖的 Hook 路径上检查这些明确边界。Agent 仍然可以读
仓库，也必须处理真正受影响的调用方。Guard 确认某个动作越界时，会返回一枚红章：

```text
STOP / INTENT
Guard 返回 permission deny。
Reason: MODE_FORBIDS_MUTATION
State: ARMED / review
Event: evt_...
```

## 0.2.0：从多做一步，到多说一句

0.1.x 先处理 SHIT 的动作面：没人读取的 `.sha256`、为想象中未来准备的兼容层、Review 时顺手开始改代码。

0.2.0 把同一套判断带到表达里。Agent 写提案时也会替不存在的批评者辩护：这不是完整研究，没有覆盖所有情况，也不保证适用于每个人。这些话消耗 Token，却不改变任何决定。

多做一步，是用动作自保；多说一句，是用文字自保。一个没人读取的 checksum，和一句不改变任何决定的免责声明，都没有消费者。

Stop Ladder 继续判断一个动作该不该做。新增的 **Stop That Shit Slop（别再废话）** 用 Sentence Consumer Test 判断一句防御性表达该删、该收紧，还是必须保留。

> 为什么 Agent 总在替不存在的批评者辩护？
>
> “这不是完整研究。”“没有覆盖所有情况。”“不保证适用于每个人。”
>
> 我没有问这些。
>
> 写给想象中批评者的防御性废话，就别再浪费我的 Token 了。
>
> Stop That Shit 0.2.0 新增 Stop That Shit Slop：判断一句话该删、该收紧，还是必须留下。

`0.2.0` 保留原有 Stop Ladder、Guard、五套 Adapter 和成对案例，并新增可独立使用的 Stop That Shit Slop。

| 从哪里开始 | 提供什么 | 使用成本 |
| --- | --- | --- |
| **Skill + Guard** | 同一份 Skill，加上机器可执行边界 | 默认；检查宿主 Hook 配置后启用 |
| **只装 Skill** | Stop Ladder 和任务模式引导 | 可选；没有执行拦截 |

## 从 Codex + GPT-5.6 开始，现在覆盖多种 Agent

项目从 Codex 起步：公开记录保留了 Codex CLI `0.145.0` + `gpt-5.6-sol` 的探索运行，以及 Codex CLI `0.147.0` + `gpt-5.6-luna` 的定向 pilot。现在五个 Adapter 共用同一套任务边界核心；Codex 安装方式、GPT-5.6 记录和 paired eval 见 [EVIDENCE.md](EVIDENCE.md) 与 [Codex 对照测试](evals/codex-paired/README.md)。

## 快速安装

一般宿主需要 Node.js 18+；Pi 0.84.4 自身要求 Node.js 22.19+。完整安装说明见 [INSTALL.md](INSTALL.md)。

### Claude Code

解压后，在仓库根目录执行：

```bash
claude plugin validate .
claude plugin marketplace add ./
claude plugin install stop-that-shit@stop-that-shit
```

重启 Claude Code 或执行 `/reload-plugins`，然后使用：

```text
/stop-that-shit:stop-that-shit review -- Review 这个 diff，只报告问题，不要修改。
```

### Codex

```bash
codex plugin marketplace add lennney/stop-that-shit --ref 0.2.0
codex plugin add stop-that-shit@stop-that-shit
```

`--ref 0.2.0` 把安装固定到版本 tag，不跟随可变的 `main`。重启 Codex。在新的 CLI TUI 中输入 `/hooks`，检查命令后信任 `UserPromptSubmit` 和 `PreToolUse`。也可以把 [`INSTALL_FOR_AGENTS.md`](INSTALL_FOR_AGENTS.md) 交给 Codex，让它完成非交互步骤。

### OpenCode 从 GitHub 安装

OpenCode 1.18.18 或更高版本可以全局安装这个仓库，无需 clone：

```bash
opencode plugin github:lennney/stop-that-shit -g
```

重启 OpenCode 后用 `$stop-that-shit review -- ...` 设置契约。该命令安装 Guard；内置 Skill 和可选 `/sts` 别名不会自动注册。详见 [INSTALL.md](INSTALL.md#opencode-install-from-github)。

### Hermes Agent CLI

需要 Node.js 18+。

```fish
hermes plugins install lennney/stop-that-shit/.hermes-plugin --no-enable
hermes plugins enable stop-that-shit
hermes plugins list
```

启用后，CLI 用户需要启动新的 Hermes CLI 进程或会话；Gateway 用户需要执行：

```fish
hermes gateway restart
```

这些操作不需要每次使用插件时重复。只有启用、禁用、更新、回滚或重装插件后，
才需要重启对应的 Hermes 进程。

### Pi Coding Agent

当前适配固定验证 `@earendil-works/pi-coding-agent` `0.84.4`。从包含该
Adapter 的本地 checkout 安装：

```bash
pi install /absolute/path/to/stop-that-shit
```

启动新的 Pi 进程，或修改资源后在 TUI 执行 `/reload`。然后使用：

```text
/skill:stop-that-shit review -- Review 这个 diff，只报告问题，不要修改。
```

从 `0.2.0` tag 安装即可获得 Pi Adapter 和两个 Skill。详见 [INSTALL.md](INSTALL.md#pi-coding-agent)。

## Bad Case / Good Case

```text
BAD CASE
用户   Review 这个 diff，不要修改。
Codex  调用 apply_patch。
STS    STOP / INTENT：Review 不等于允许修改。

GOOD CASE
用户   只修 P1 问题。
Codex  提交一个窄补丁，运行受影响的检查。
STS    ALLOWED：完成请求确实需要这个动作。
```

Good Case 和拦