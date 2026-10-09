<div align="center">

# wx-cli

**从命令行查询本地微信数据**

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)](#安装)
[![Rust](https://img.shields.io/badge/built%20with-Rust-orange.svg)](https://www.rust-lang.org)

会话 · 聊天记录 · 搜索 · 联系人 · 群成员 · 群昵称 · 收藏 · 统计 · 导出

</div>

---

## AI Agent Skill

通过 [skills CLI](https://github.com/vercel-labs/skills) 一键安装到 Claude Code、Cursor、Codex 等 agent：

```bash
npx skills add botiverse/wx-cli
```

或全局安装：

```bash
npx skills add botiverse/wx-cli -g
```

安装后 agent 会自动读取 `SKILL.md`，了解如何安装和调用 wx-cli。

源码与发布仓库：[botiverse/wx-cli](https://github.com/botiverse/wx-cli)。

---

## 特性

- **零依赖安装** — 单一 Rust 二进制，一行命令装完
- **毫秒级响应** — 后台 daemon 持久缓存解密数据库，mtime 不变则复用
- **AI 友好** — `history` / `search` / `sessions` / `new-messages` / `stats` / `attachments` 默认返回 `{..., meta}` wrapper，agent 能直接消费 freshness / source 信息
- **完全本地** — 数据不出本机，实时解密，无需全量预解密

---

## 安装

> **当前仓库 [botiverse/wx-cli](https://github.com/botiverse/wx-cli) 为 private。**  
> 匿名 `curl` / 公开 npm 旧包（`@jackwener/wx-cli@0.3.0`）**拿不到**本仓库最新二进制。  
> 有仓库读权限时，请用下面的 **源码构建**（推荐）。

### 从源码构建（推荐）

```bash
git clone git@github.com:botiverse/wx-cli.git && cd wx-cli
cargo build --release
# 安装到用户 PATH（覆盖旧版）
mkdir -p ~/.local/bin
cp target/release/wx ~/.local/bin/wx
wx --version   # 应显示当前 Cargo.toml 版本，如 0.6.3
```

Windows：

```powershell
git clone git@github.com:botiverse/wx-cli.git
cd wx-cli
cargo build --release
# 将 target\release\wx.exe 放到 PATH 目录
```

### 已有 clone 时升级

```bash
git pull
cargo build --release
cp target/release/wx ~/.local/bin/wx
```

<details>
<summary>其他方式（需仓库权限 / 发布配置）</summary>

**GitHub Release 预编译包**（仓库 private 时仅协作者可见）

从 [Releases](https://github.com/botiverse/wx-cli/releases) 下载：

| 平台 | 文件 |
|------|------|
| macOS Apple Silicon | `wx-macos-arm64` |
| macOS Intel | `wx-macos-x86_64` |
| Linux x86_64 | `wx-linux-x86_64` |
| Linux arm64 | `wx-linux-arm64` |
| Windows x86_64 | `wx-windows-x86_64.exe` |

```bash
chmod +x wx-macos-arm64 && mv wx-macos-arm64 ~/.local/bin/wx
```

**一键脚本**（raw 链接在 private 仓库下对匿名用户 404；有权限时可用 `gh` 下载 release asset）

```bash
# 需已登录 gh 且对 botiverse/wx-cli 有读权限
gh release download -R botiverse/wx-cli -p 'wx-macos-arm64' -O ~/.local/bin/wx
chmod +x ~/.local/bin/wx
```

`install.sh` / `install.ps1` 仍维护在仓库内，仓库公开或 raw 可访问后可再启用：

```bash
curl -fsSL https://raw.githubusercontent.com/botiverse/wx-cli/main/install.sh | bash
```

**npm**

历史包名 `@jackwener/wx-cli` 仍存在于 npm，但公开 registry 上的版本可能严重滞后，**不要**当作当前主安装路径。

</details>

---

## 快速开始

### 新用户要做什么 / 不要做什么

| | macOS 新用户 |
|--|--|
| **需要** | 微信 4.x 已安装并**登录**；从**本机 GUI Terminal**（Terminal.app / iTerm 等，不要用 SSH）执行 `sudo wx init` |
| **不需要** | **关闭 SIP** |
| **不需要** | 预先 `codesign` / ad-hoc **重签微信**（默认路径不会改 WeChat.app） |
| **init 之后** | 日常 `wx sessions` / `history` 等**无需 sudo**，也**不要求微信一直开着** |

### 初始化（只需一次）

保持微信运行并已登录，然后：

**macOS**

```bash
# 必须：本机 GUI Terminal + sudo（系统可能提示授予「开发者工具」权限，请允许）
sudo wx init

# 若提示缺分片密钥 / meta.unknown_shards 非空：加长 hook，等待期间在微信里点开相关聊天
sudo wx key extract --hook-seconds 90
```

`wx init` 两阶段取密钥（**都不依赖关 SIP**）：

1. 进程内存扫描（`x'key+salt'` + salt 邻接）
2. LLDB hook `CCCryptorCreate`，补齐尚未加载进内存的 per-DB AES key

说明：

- 官方 **Hardened Runtime** 包：本机 Terminal + `sudo` 即可；若失败，到「系统设置 → 隐私与安全性 → 开发者工具」里勾选你的终端。
- 部分官网 4.x 本身已是 **ad-hoc**：用户态 LLDB 往往也能工作。
- **不要**默认对 WeChat 做 ad-hoc 重签：会打乱 TCC 权限、公众号/截图可能异常。仅当 SSH 等无 GUI 场景下 `task_for_pid` 仍失败时，才考虑有副作用的重签；详见 [macOS 权限指南](docs/macos-permission-guide.md)。

**Linux**

```bash
sudo wx init
```

**Windows**（以管理员身份运行 PowerShell）

```powershell
wx init
```

### 验证

```bash
wx --version
wx doctor          # 密钥 / 分片 / SQLCipher 健康检查
wx sessions
```

能看到最近会话且 `wx doctor` 关键项通过即表示正常。daemon 在首次查询时自动启动。

若 `doctor` 提示关键分片缺密钥，或 `meta.unknown_shards` 非空：

```bash
sudo wx key extract --hook-seconds 90
# 等待期间在微信里打开相关聊天（冷分片可能需触发加载）
wx doctor
```

---

## 命令

### 诊断与密钥

```bash
wx doctor                                 # 环境 / 密钥 / 分片检查
wx doctor --fix --json                   # JSON + 修复建议
wx key list                               # 已有密钥与缺失覆盖
wx key extract --hook-seconds 90          # 建议：sudo wx key extract --hook-seconds 90
wx key set message/message_1.db <64hex>   # 手动写入并校验
```

补密钥统一用 **`sudo wx key extract --hook-seconds 90`**（不要用裸的 `wx init --force` 当主路径）。  
取钥**不需要关闭 SIP**；需本机 GUI Terminal +（Hardened Runtime 包）sudo。

### 消息

```bash
wx sessions                                      # 最近 20 个会话
wx unread                                        # 有未读消息的会话
wx unread --filter private,group                 # 只看真人未读（过滤公众号/折叠入口）
wx new-messages                                  # 上次检查后的新消息（增量）
wx history "张三"                                # 最近 50 条记录
wx history "张三" -n 2000                        # 拉更多历史消息
wx history "AI群" --since 2026-04-01 --until 2026-04-15
wx search "关键词"                               # 全库搜索
wx search "关键词" -n 500                        # 放宽搜索结果条数
wx s