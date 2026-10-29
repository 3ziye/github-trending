<div align="center">

# dsh-purge Community

**让 AI 更专注地辅助你的学习与动手实验。**

给 DeepSeek Harness 的自托管控件（俗称「破甲」插件）· 80 条宿主补丁 · 25 层状态自检 · 左侧栏整页设置

[![Release](https://img.shields.io/github/v/release/kingcharleslzy-ai/dsh-purge?label=release)](https://github.com/kingcharleslzy-ai/dsh-purge/releases)
[![Checks](https://github.com/kingcharleslzy-ai/dsh-purge/actions/workflows/community.yml/badge.svg)](https://github.com/kingcharleslzy-ai/dsh-purge/actions/workflows/community.yml)

当前版本 **1.6.60** · 适配 **DSH Desktop 0.2.1-rc.3**（rc.1 / rc.2 同样通过） · [English](docs/README.en.md)

1.6.56 改善状态页卡顿，避免缓存旧宿主证据；读取失败不再误报未安装，并修复深色主题按钮对比度。[发行说明](docs/releases/1.6.56.md) · [市场安装与迁移指南](docs/MARKET-MIGRATION.md)。

**原项目与作者**：基于 [小杨 / YuJunZhiXue 的 dsh-purge](https://github.com/YuJunZhiXue/dsh-purge) 独立维护。原仓库已恢复；保留原作者署名、版权与 MIT 许可证。社区版由本仓库维护，并非原作者官方发行。

</div>

---

## 搭配：本机出图（Qwen Studio）

破甲之后最直接的玩法，是把「生图」也搬到本机——不用网页、不用会员、不把提示词发到别人服务器。

配套插件 **Qwen Studio**（`dsh-qwen-studio`）把 Qwen Image 2.1 接进 DSH：

- **Apple Silicon Mac**：MLX / MFLUX 本机推理，模型用时加载、空闲释放；
- **Windows / Linux + NVIDIA**：连你自己的 GPU 网关（ComfyUI 或 vLLM-Omni 协议），也支持 SSH 按需拉起；
- 支持参考图编辑（按图改画风、换材质）、LoRA、ControlNet、蒙版、整套预设、图库与批量任务；
- 装好之后，会话里直接说「画一张…」或「把这张改成水彩」，Agent 调用 `qwen_generate_image` 并把图返回到对话里。

**组合效果**：破甲让 Agent 不再反复确认「要不要画」，出图插件让它真的画出来，全程在你自己的机器上完成。

**仓库**：[kingcharleslzy-ai/dsh-qwen-studio](https://github.com/kingcharleslzy-ai/dsh-qwen-studio) · **下载**：[最新 Releases](https://github.com/kingcharleslzy-ai/dsh-qwen-studio/releases/latest) · **安装与硬件自查**：[docs/SETUP.md](https://github.com/kingcharleslzy-ai/dsh-qwen-studio/blob/main/docs/SETUP.md)（先看「这台机器能不能跑」再动手）

## 它是什么

dsh-purge Community 是一个跑在你自己机器上的 Harness 附加组件。它把日常使用里最消耗注意力的几件事收敛到一处：

- **看清楚状态**：安装、补丁、注入到底有没有就绪，一条命令或一屏面板给结论；
- **少一些往返**：把反复出现的确认与打断，收敛成一次设置；
- **随时能回去**：应用、回滚、开关都留记录，操作前自动快照；
- **方便做实验**：提示词、规则、预设集中管理，改坏了能撤。

目标很简单：**让助手更连贯地配合你的学习与动手实验**，而不是每做一步都先停下来问一句。

社区里通常把它叫作「破甲」或「无限制模式」插件——指的是它降低了交互层面的摩擦，让 agent 能连续执行任务；它不改模型本身，也不改变你要做的事。

### 下载时报 `fetch failed`？

1.6.39 起，独立安装器会显示失败阶段和错误码，有限重试后可切换系统 curl；两条通道都保留来源、证书和 SHA256 校验。请先重新下载安装脚本再运行 dry-run，仍失败时提交脱敏诊断行即可。见 [下载排查说明](docs/maintenance-issue-52.md)。不会自动修改代理或重启 DSH。

### 让不同预设保留自己的提示词

1.6.40 新增 `excludePresets`：默认空列表，保持原有行为；可将 `roleplay`、`minimal` 等预设排除在 Purge 提示词注入之外，保留命令、面板与工具。切换预设、并行会话和子 Agent 各自判断，宿主兜底也遵守排除。配置示例、升级步骤与边界见 [按预设排除说明](docs/maintenance-issue-53.md)。这不会撤销全局宿主补丁。

## 设计原则

| 原则 | 含义 |
| --- | --- |
| 本机优先 | 全部逻辑在本机运行，不改云端账号、不上传提示词或配置 |
| 可见 | 每个动作都有状态与证据，不靠"应该生效了"这种判断 |
| 可回滚 | 应用 / 安装 / 回滚前自动快照，保留原文件与校验清单 |
| 不替你做决定 | 只减少摩擦，不改变你的目标；改什么、开什么，都由你确认 |

## 适用场景

本机学习、个人项目、自动化实验与维护工作。请在你拥有或已获授权的环境中使用；涉及他人系统时，先取得许可。

## 1.6.39 更新

修复独立安装器只显示 `fetch failed` 的问题：分阶段诊断、有限重试和系统 curl 备用下载，继续严格校验官方来源、证书和 SHA256。下载失败不触碰现有安装。[发行说明](docs/releases/1.6.48.md) · [配置与验收](docs/maintenance-issue-52.md)

## 安装

**DSH 官方入口负责安装插件；下面的社区安装器由本仓库维护，不是 DeepSeek 官方脚本。** 首次安装可用官方界面或 CLI；已经装过 `dsh-purge` / 旧独立面板时，用社区安装器原地迁移，不要先卸载。安装、应用宿主补丁、手动重启是独立动作。

### 方式一：DSH 官方界面（首次安装）

1. 先打开 DSH 完成初始化。按当前官方文档，进入「插件」，点击「实验性插件」旁的「更多」，启用「自定义插件市场」；然后进入「发现 → 添加索引源」。
2. 本项目的**社区索引**：`https://kingcharleslzy-ai.github.io/dsh-purge/index.json`。
3. 选择 dsh-purge Community，核对来源为 `kingcharleslzy-ai/dsh-purge`、包名为 `dsh-purge-community`，确认后安装。

界面和安装协议由 DSH 提供，索引与插件由社区维护。不同 DSH 版本的入口文字可能不同；第三方 `dsh-market` 也可能有额外的筛选与迁移限制。已有旧包时请使用方式三。[官方市场说明](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/plugin-market.zh.md)

### 方式二：DSH 官方 CLI（首次安装）

下面命令适用于**已经安装 `dsh` 命令、且使用 `web` profile 的 CLI/Web 用户**，在 macOS/Linux 终端或 Windows PowerShell 中运行。桌面版用户优先用上面的界面；不要为了安装插件再用 `npx` 下载另一套宿主。

```sh
dsh plugin --profile web add "https://github.com/kingcharleslzy-ai/dsh-purge/releases/download/v1.6.60/dsh-purge-community-1.6.60.tgz"
```

`web` 必须与实际启动的 profile 一致；自定义数据目录需要沿用该实例的 `DSH_HOME`。命令使用本次发行的固定版本 URL；不是 `npm install -g`，也不是安装裸 npm 包名。本项目通过 GitHub 发行，**不要替换成 `add dsh-purge` 或 `add dsh-purge-community`**。官方 CLI 的安装不会额外运行我们安装器的 Release SHA256 比对及迁移快照；需要这些功能时选方式三。[官方 CLI 安装说明](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/develop/basic/publish.zh.md)

### 方式三：社区安装器（备份、旧版迁移、恢复）

先安装并打开一次 DSH，让实际 profile 初始化。以下命令下载**本仓库的脚本**，先校验，再安装；`dry-run` 通过仅代表前置检查、下载和 SHA256 通过，不代表依赖安装、迁移或启动已通过。请先阅读下载的脚本。

#### macOS Desktop

默认应用位置 `/Applications/DeepSeek Harness.app`、数据目录 `~/.dsh`、profile `desktop`。将下面两段放在同一个终端会话中执行：

```sh
PURGE_INSTALL_DIR="$(mktemp -d)"
curl -fSL --connect-timeout 20 --max-time 90 "https://raw.githubusercontent.com/kingcharleslzy-ai/dsh-purge/master/scripts/install.sh" -o "$PURGE_INSTALL_DIR/install.sh"
sh "$PURGE_INSTALL_DIR/install.sh" --dry-run
```

校验成功、核对目标实例后执行：

```sh
sh "$PURGE_INSTALL_DIR/install.sh"
```

自定义应用或 home 时，先设置 `DSH_APP` / `DSH_HOME`；自定义 profile 对两次命令都加 `--profile=实际名称`。不要照抄别人的路径。 macOS 支持从 XML/二进制 plist 读取真实可执行文件名；元数据无效会停止，不会换用其他应用。详见[定位边界](docs/INSTALLATION.md#应用定位边界pr-78)。

#### Windows Desktop · PowerShell 5.1 / 7

脚本会尝试定位唯一的 DSH Desktop，默认 home 为用户的 `.dsh`、profile 为 `desktop`。不要求管理员权限；路径含空格也支持。

```powershell
$PurgeInstaller = 