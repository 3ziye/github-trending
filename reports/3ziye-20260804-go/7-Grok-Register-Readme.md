# Grok-Register

Grok 免费号 **注册 → OAuth → CPA 可用 JSON** 二合一 CLI（Go）。

一条命令后台跑完，产物可直接导入 CPA / cliproxy 类网关。

```bash
grok start                 # 交互：数量 + 线程(1–8)
grok start -t 10 --thread 2
grok status
grok logs -f
grok stop
grok config                # 编辑 ~/.grok/config.env
grok upload                # 手动上传 CPA JSON 到 Management API
```

---

## 近期特性

| 特性 | 说明 |
|------|------|
| **协议优先 + TLS 指纹** | Go `tls-client`（默认 `chrome_131`）过 CF；`CLEARANCE_MODE=auto` 失败再拉 WARP/FS |
| **Turnstile 屏外有头** | 默认 `TURNSTILE_MODE=offscreen`（非真 headless，降低 600010） |
| **Castle 空 token** | 当前 `castleRequestToken=""`；风控收紧后再补 offline |
| **testmail** | `EMAIL_MODE=testmail`，GitHub Student Pack 等 |
| **cf_temp_email** | 对接 [cloudflare_temp_email](https://github.com/dreamhunter2333/cloudflare_temp_email) 自建 Worker |
| **全局座位上限** | `done + reserved ≤ target` |
| **CPA 上传 wait** | 结束前等待 Management 上传，避免进程先退出 |
| **一键安装** | 路径/命令名/WARP/结束停容器交互；安全同步（不再误删非空目录） |
| **`grok stop` 停清障** | `CLEARANCE_AUTO_STOP=1` 时手动 stop 也会 `docker compose stop` |
| **grok2api 导出** | `outputs/<run>/grok2api/tokens.txt` 仅 SSO token（一行一个） |
| **OAuth 限速** | 全局间隔 + discovery 缓存 + rate_limited 重试 |

### 架构三腿

```text
协议腿  gRPC 发/验码 → Server Action → SSO hop → OAuth → 探活/CPA
边缘腿  chrome_131 TLS 优先 → CF 拦再 clearance（auto）
挑战腿  Turnstile 仅 Chromium（offscreen 池 / one-shot）
```

冒烟（不注册账号）:

```bash
go run scripts/smoke_protocol.go
REGISTER_PROXY=http://127.0.0.1:7890 go run scripts/smoke_protocol.go
```

---

## 一键安装（推荐）

`scripts/install.sh` 自动识别平台：

| 平台 | 前提 | 默认安装位置 |
|------|------|----------------|
| **Linux**（Debian/Ubuntu） | root / sudo | 源码 `/opt/Grok-Register`；数据优先 **`SUDO_USER` 的 `~/.grok`**（非 `/root`） |
| **macOS** | 已装 **Homebrew** + **Docker Desktop**（缺则提示安装命令后退出） | `~/Grok-Register`，数据 `~/.grok`，CLI `~/.local/bin` |

会拉源码、编译 CLI、装 Playwright/CloakBrowser、起 clearance，并写入**分区中文注释**的 `config.env`（与 `config.env.example` 同模板）。

### 交互询问

有真实 TTY 时会依次提示：

1. CLI 命令名 / 源码目录 / 数据目录 / 二进制 / venv  
2. **是否启用 WARP 清障栈？** `[Y]`  
   - **Y（默认）**：起 Docker 清障，`REGISTER_PROXY=http://127.0.0.1:40080`  
   - **N**：不装清障；再问 **本机 HTTP 代理端口**  
     - 输入如 `7890` → `REGISTER_PROXY=http://127.0.0.1:7890`，`CLEARANCE_ENABLED=0`  
     - **直接回车** → 直连（无代理，适合能访问 x.ai 的境外 VPS）  
3. **（WARP 时）运行结束后是否自动关闭清障容器？** `[Y]`  
   - **Y（默认）**：`CLEARANCE_AUTO_STOP=1`，结束/中断后 `docker compose stop`  
   - **N**：容器常开；每次 `grok start` 仍会检测并自动拉起未运行的栈
无 TTY 的 `curl|sudo bash` 可能无法提问，此时：

```bash
# WARP 清障（默认）
curl -fsSL .../install.sh | sudo bash -s -- --with-warp

# 本机 Clash 等代理
curl -fsSL .../install.sh | sudo bash -s -- --no-warp --proxy-port 7890

# 境外 VPS 直连
curl -fsSL .../install.sh | sudo bash -s -- --no-warp

# 强制全默认（WARP）
curl -fsSL .../install.sh | sudo NONINTERACTIVE=1 bash
```

### Linux 一行

```bash
curl -fsSL https://raw.githubusercontent.com/Charles-0509/Grok-Register/main/scripts/install.sh | sudo bash
```

| 项 | 默认 |
|----|------|
| 命令 | `/usr/local/bin/grok` |
| 源码 | `/opt/Grok-Register`（软链 `/opt/Grok-Reg`） |
| 数据 | `sudo` 时为 **`/home/<SUDO_USER>/.grok`**，纯 root 为 `/root/.grok` |
| Python | `/opt/cloakbrowser-venv/bin/python` |
| mint | `/usr/local/share/grok-reg/turnstile_{mint,pool}.py` |
### macOS 一行

**先**确认：

```bash
# 1) Homebrew — 若无:
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2) Docker Desktop — 若无:
# brew install --cask docker
# 打开 Docker 应用，等引擎就绪: docker info
```

然后（**不要 sudo**）：

```bash
curl -fsSL https://raw.githubusercontent.com/Charles-0509/Grok-Register/main/scripts/install.sh | bash
```

| 项 | 默认 |
|----|------|
| 命令 | `~/.local/bin/grok` |
| 源码 | `~/Grok-Register` |
| 数据 | `~/.grok` |
| Python | `~/.local/share/cloakbrowser-venv/bin/python` |
| mint | `~/.local/share/grok-reg/turnstile_{mint,pool}.py` |
| 环境 | 写入 `~/.zprofile` / `~/.zshrc` |

缺 brew 或 Docker 时脚本会打印安装命令并退出，装好后重跑同一行即可。

### 自定义命令名 / 目录

```bash
# Linux：改命令名
curl -fsSL .../install.sh | sudo bash -s -- --command grok-reg

# Linux：自定义目录
curl -fsSL .../install.sh | sudo bash -s -- \
  --install-dir /data/Grok-Register --home /data/grok-data

# macOS：改命令名 / 把二进制装到 brew 前缀
curl -fsSL .../install.sh | bash -s -- --command grok-reg
curl -fsSL .../install.sh | bash -s -- --bin-dir "$(brew --prefix)/bin"
```

### 常用选项

| 选项 / 环境变量 | Linux 默认 | macOS 默认 | 说明 |
|-----------------|------------|------------|------|
| `--command` | `grok` | 同左 | CLI 命令名 |
| `--install-dir` | `/opt/Grok-Register` | `~/Grok-Register` | 源码 |
| `--home` | `/root/.grok` | `~/.grok` | 数据 |
| `--bin-dir` | `/usr/local/bin` | `~/.local/bin` | 二进制 |
| `--share-dir` | `/usr/local/share/grok-reg` | `~/.local/share/grok-reg` | mint 脚本 |
| `--venv-dir` | `/opt/cloakbrowser-venv` | `~/.local/share/cloakbrowser-venv` | Python venv |
| `--skip-docker` | off | off | 不检查/不装 Docker |
| `--skip-clearance` | off | off | 不起清障 |
| `--skip-browser` | off | off | 不装 Playwright |
| `--skip-go` | off | off | 不自动装 Go |
| `--no-start-clearance` | off | off | 不 `compose up` |

本地已 clone：

```bash
# 