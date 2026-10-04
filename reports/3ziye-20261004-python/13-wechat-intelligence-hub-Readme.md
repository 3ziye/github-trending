# WeChat Intelligence Hub

微信个人情报库：把本地微信聊天变成可检索、可核查、可行动的个人情报，包括联系人历史、群聊主题、待回复、承诺、商机、复联线索，以及任意指定时间范围的情报报告。

这不是 Prompt 大礼包，而是一个独立的微信旗舰项目。仓库同时提供只读数据入口和情报工作流，并配有可执行入口、边界、测试和全虚构样例。

当前首发版本为 `v0.9.2-preview.2`。微信相关代码已经具备公开测试条件，但不是“安装后自动读取所有人的完整微信历史”：完整数据库模式需要本人授权的本地数据库和访问材料。Reader 核心不获取密钥、不重签名、不注入、不 Hook 微信；可选的实验性接入助手有独立授权和副作用边界，见下文。

## 一个产品，两个 Skill

| Skill / Project | 作用 | 状态 |
|---|---|---|
| `wechat-cli` | Rion 自有的只读 Reader 入口；v0.9.2-preview.2 已覆盖旧版接口、schema-2 salt-key 授权导入、WCDB 压缩消息，并在维护者已有授权材料的本机完成实读 | 依赖层 / Preview |
| `wechat-intelligence-hub` | 把微信记录转成日报、待回复、承诺、商机和复联线索 | 用户入口 / Flagship |

微信能力在代码中分成四层，方便独立测试和维护；对用户仍是一套产品、一次安装：

- `projects/rion-wechat-reader/`：Rion 自有的 clean-room 只读 Reader 核心。
- `skills/wechat-cli/`：Reader 的统一 Agent 入口，默认只调用 Rion 自有 Reader；只有使用者显式设置 `RION_WECHAT_CLI_BIN` 时才调用兼容后端。
- `skills/wechat-intelligence-hub/`：Agent 的调用入口与判断规则。
- `projects/wechat-intelligence-hub/`：确定性本地引擎、虚构样例和测试。

Rion 的通用 Skill 合集 `rionwu-skills` 只负责收录、发现和链接本项目，不复制微信读取器源码或 Git 历史。

## 安装

**9月22日接入更新：** 已增加材料编码/格式兼容、明确错误码、独立解密计数和`diagnose`诊断。JEV可选辅助分流，但不参与密钥验证；Windows首次获取仍待真机验收。见[更新与排障提示词](docs/access-upgrade-2026-09-22.md)。

向维护者反馈前，让本地Codex运行`access.sh diagnose --support-summary`；Windows用Reader环境的Python运行`rion_wechat_access.py diagnose --support-summary`。它只输出允许分享的版本、状态、计数和错误码，仍请本人检查后再发。只有网页对话、没有本机文件及命令执行能力时，无法直接接入本机微信。另一个工具已能读取时，优先验证已有材料或已解密数据库，不要求重新获取；见[常见卡点处理](docs/access-support.md)。

### 直接让Codex安装和配置

把下面这段发给Codex即可，不需要自己逐条执行命令：

```text
请从 https://github.com/Rion-Wu-tech/wechat-intelligence-hub 安装微信CLI和微信个人情报库，接入这台电脑上我自己的微信。
先读取仓库说明，检查是否已经安装、当前配置是否可用；已有可用配置或key就复用，不覆盖我的个人Profile和数据。
缺少依赖由你处理；确实缺key时，先按操作系统核对是否存在已审核的获取路线。仅在该路线适配本机、说明影响并经我单独确认后执行；没有适配路线就报告缺口，不运行未经审核的工具。我负责登录微信和完成系统授权，不会把密码或key发给你。
完成数据库验证和配置后，告诉我能读取哪些范围、还有什么未就绪；再协助初始化个人情报库。遇到错误请定位并修复，不要把一堆命令交给我，也不要无限重试。
```

这是有人确认关键操作的接入工作流，不是无条件、无人值守的解密。已有安装如何升级、微信升级后如何排障，见[配置与排障提示词](docs/USAGE.md#让codex处理配置与排障)。

### 手动安装入口

**先确认接入条件：安装成功不等于已能读取聊天。** 已有本机访问材料可直接验证、导入；没有key时，由Codex按[五步首次接入工作流](skills/wechat-cli/references/access-onboarding.md)核对平台与候选工具。仅对已审核且适配的候选，经明确确认后尝试获取；macOS候选可能重启微信和重签名副本，Windows获取尚未合入。仓库不捆绑获取工具，安装和日常日报均不会触发获取；macOS新机器获取路径尚未实测，不保证所有版本可用。请勿向维护者、社群或Issue发送key、密码和数据库。

克隆仓库：

```bash
git clone https://github.com/Rion-Wu-tech/wechat-intelligence-hub.git
cd wechat-intelligence-hub
```

安装完整产品：

```bash
./scripts/install.sh --with-sqlcipher --with-html
```

不传 Skill 名称时会安装 `wechat-cli`、`wechat-intelligence-hub` 及其本地引擎。即使只指定 `wechat-intelligence-hub`，安装器也会自动补齐它依赖的 `wechat-cli`；用户不需要手工拼装两套组件。

`--with-html` 在 Hub 自己的 `.venv` 安装固定版本的 HTML 净化依赖 `nh3`，不修改全局 Python；HTML 还需要本机 Pandoc。没有该依赖时，HTML 生成会明确报错，不降级为未净化页面；纯 Markdown/检索仍可用。已有安装请让 Codex 先确认实际引擎路径、备份代码再升级，保留 Profile、数据库和 key。安装器不会覆盖已有目录。安全改动、影响和回归方法见[升级说明](docs/upgrade-2026-09-14.md)。

安装后可以直接对Codex说：

> 用 $wechat-cli 帮我接入这台电脑上我自己的微信。已有配置或key就复用；没有就帮我准备工具，说明影响并确认后获取，再完成验证和配置。

安装 `wechat-cli` Skill 时会同时安装 Rion 自有的 `rion-wechat-reader` 核心。新用户无需第三方二进制即可检查本机覆盖范围，并在 macOS 上读取系统实际保留的微信通知预览；该模式只覆盖入站预览，不能代表完整聊天记录。v0.9.2-preview.2 的公开接口已与旧 `wechat-cli 1.6.19` 的 29 项只读工具、266 个输入字段对齐，可读取用户显式提供的 schema-2 salt-key 授权材料，并安装隔离 SQLCipher 与 Zstandard 运行依赖。维护者在已有授权材料的本机完成了新旧 CLI 真实数据对照、当前 macOS 图片/视频/文件路径验证和微信个人情报库端到端索引验证；这不证明新机器首次取钥或其他微信版本可用。其他版本仍按能力矩阵逐项积累。

需要独立命令行入口时只安装一个 CLI：

```bash
projects/rion-wechat-reader/install.sh --with-sqlcipher
rion-wechat-cli self-test
rion-wechat-cli self-test --require-sqlcipher
rion-wechat-cli access-plan --pretty
```

`ready` 表示复用已有配置；`ready_to_configure` 才继续用相同输入运行 `setup`；`needs_access` 表示缺少访问材料，不要重复运行setup。JSON顶层 `ok: true` 仅表示诊断完成，请查看 `data.state`。部分覆盖、驱动缺失、多账号和权限问题会分别给出下一步。

**卡在找key、反复退出微信？** 先让Codex运行`access.sh status`，根据失败阶段继续处理。新助手支持账号目录自动适配、相对路径材料转换、Reader `salt_keys`复用，以及获取前的文件/调试器检查。不要上传原始日志或key。具体见[接入排障表](skills/wechat-cli/references/access-troubleshooting.md)和[本轮接入升级及仍未解决的兼容项](docs/access-upgrade-2026-09-14.md)。这些改动不代表任意Mac/Windows版本都能自动取得key。

维护者和兼容测试用户可查看[macOS接入候选补丁](providers/wxkey/README.md)：包含上游Intel修复、进程身份核验、等待超时与清理改进。仓库只附补丁和准备脚本，不附可执行获取工具；它尚未通过新机器真实微信获取验收，不是默认安装步骤。

候选路线要成为默认安装能力，必须先通过[真实首次接入验收](docs/first-access-pilot.md)：数据库可读、目标聊天抽检及官方微信恢复都要分别确认。模拟测试通过不等于真实取钥成功。

**Windows接入状态：** Reader 的 Windows 原生 CI 已验证虚构材料导入、SQLCipher 读取、ACL 和路径兼容；社区报告过特定微信版本和外接工具组合的个人成功案例，但主仓库未合入 Windows 首次获取，也未完成新电脑上的取钥到日报验收。具体边界与已有方案见[Windows接入指引](skills/wechat-cli/references/windows-access.md)。

接入助手还会提示复用已存在的wxcli材料，并在启动获取工具前检查LLDB关键接口。数据库验证成功后仍需确认微信恢复；`finish-recovery`只在用户事后确认和进程检查通过后移除恢复锁，正常查询不受该锁影响。

完整历史和实时数据库读取要求有权访问的本地数据库与访问材料，且仅覆盖已同步到本机的数据。只读 Reader 与可选接入助手的边界见 [Reader 说明](projects/rion-wechat-reader/README.md)。没有数据库读取条件时，仍可运行全虚构 Demo，验证索引、判断与报告链路。

安装 `wechat-intelligence-hub` 时，脚本会同时把经过隐私扫描的本地引擎放进 Codex 目录，正常调用无需再配置 `WECHAT_HUB_HOME`。先用虚构数据运行 Demo：

```bash
bash projects/wechat-intelligence-hub/scripts/run_demo.sh
```

只有在开发或调试仓库源码时，才需要临时指定引擎路径：

```bash
export WECHAT_HUB_HOME="$PWD/projects/wechat-intelligence-hub"
```

安装 `wechat-cli` 和 `wechat-intelligence-hub` 后，建议先做一次个性化初始化。它会把你正在做的事、个人背景和关系标签变成日报的排序依据：

```bash
cd projects/wechat-intelligence-hub
p