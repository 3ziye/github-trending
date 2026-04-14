# GoProxy

> **智能代理池系统** — 基于 Go 的轻量级、自适应代理池服务，支持免费代理自动抓取 + 付费订阅导入

[![Docker Hub](https://img.shields.io/docker/v/isboyjc/goproxy?label=Docker%20Hub&logo=docker)](https://hub.docker.com/r/isboyjc/goproxy)
[![GitHub Container Registry](https://img.shields.io/badge/GHCR-latest-blue?logo=github)](https://github.com/isboyjc/GoProxy/pkgs/container/goproxy)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Go Version](https://img.shields.io/badge/Go-1.25-00ADD8?logo=go)](https://go.dev/)

GoProxy 从公开代理源自动抓取 HTTP/SOCKS5 代理，同时支持导入 Clash/V2ray 付费订阅，通过出口 IP + 地理位置 + 延迟三重验证后统一入池，对外提供 HTTP 和 SOCKS5 双协议代理服务。

**GitHub**：[github.com/isboyjc/GoProxy](https://github.com/isboyjc/GoProxy)

![](https://cdn.amux.ai/data/1322149f78ab57adb821ce731c11a9e944504649.png)

## 核心特性

### 双池架构

- **免费代理池** — 自动从 20+ 公开源抓取，质量分级（S/A/B/C），智能补充与替换
- **订阅代理池** — 导入 Clash/V2ray 订阅，通过 sing-box 自动转换加密协议（vmess/vless/trojan/ss/hysteria2/anytls 等）为本地 SOCKS5 代理
- **5 种使用模式** — 混合·订阅优先 / 混合·免费优先 / 混合·平等 / 仅订阅 / 仅免费，WebUI 随时切换

### 智能池子管理

- **固定容量 + 动态状态** — Healthy → Warning → Critical → Emergency 四级自适应
- **严格准入** — 出口 IP + 地理位置 + 延迟验证，HTTP 代理额外验证 HTTPS CONNECT 隧道
- **自动优化** — 按需抓取（Emergency/Refill/Optimize 三模式），定时替换慢代理
- **故障自愈** — 请求失败自动切换代理重试（最多 3 次），用户无感知

### 订阅管理

- **格式自动识别** — Clash YAML / V2ray 链接 / Base64 / 纯文本，无需手动选格式
- **sing-box 内置** — Docker 镜像自带 sing-box，加密协议节点自动转为本地 SOCKS5
- **软删除机制** — 订阅代理失败不删除只禁用，定时探测唤醒恢复
- **访客贡献** — 未登录用户可贡献订阅 URL/文件，管理员统一管理
- **自动清理** — 连续 7 天无可用节点的订阅自动移除

### 多端口多协议

| 端口 | 协议 | 模式 | 适用场景 |
|------|------|------|---------|
| 7777 | HTTP | 随机轮换 | 爬虫、数据采集、IP 多样性 |
| 7776 | HTTP | 最低延迟 | 长连接、流媒体、稳定优先 |
| 7779 | SOCKS5 | 随机轮换 | 浏览器、SSH、游戏 |
| 7780 | SOCKS5 | 最低延迟 | 稳定应用、固定连接 |
| 7778 | HTTP | WebUI | 管理面板（双角色权限） |

### WebUI 仪表盘

- 免费池 / 订阅池分离展示，实时状态监控
- 订阅管理：添加 URL / 上传文件 / 刷新 / 暂停 / 删除
- 系统设置：5 种代理模式切换、池子参数、地理过滤
- 双角色权限：访客只读 + 管理员完全控制
- 中英文切换

## 快速开始

### Docker 部署（推荐）

```bash
# 一键启动（自动拉取最新镜像）
docker compose up -d

# 访问 WebUI
# http://localhost:7778（默认密码：goproxy）
```

自定义配置：

```bash
cp .env.example .env
vim .env  # 修改密码、认证、地理过滤等
docker compose up -d
```

### 本地运行

```bash
# 需要 Go 1.25 + CGO（依赖 go-sqlite3）
go run .

# 或编译后运行
go build -o proxygo . && ./proxygo
```

> 如需订阅导入功能，本地需安装 [sing-box](https://sing-box.sagernet.org/)：`brew install sing-box`

## 使用代理

### HTTP 代理

```bash
# 随机轮换（IP 多样性）
curl -x http://localhost:7777 https://httpbin.org/ip

# 最低延迟（稳定优先）
curl -x http://localhost:7776 https://httpbin.org/ip

# 环境变量方式
export http_proxy=http://localhost:7777
export https_proxy=http://localhost:7777
```

### SOCKS5 代理

```bash
# 随机轮换
curl --socks5 localhost:7779 https://httpbin.org/ip

# 最低延迟
curl --socks5 localhost:7780 https://httpbin.org/ip

# 环境变量方式
export ALL_PROXY=socks5://localhost:7779
```

### 带认证使用

```bash
# HTTP
curl -x http://user:pass@your-server:7777 https://httpbin.org/ip

# SOCKS5
curl --socks5 user:pass@your-server:7779 https://httpbin.org/ip

# 环境变量
export http_proxy=http://user:pass@your-server:7777
export ALL_PROXY=socks5://user:pass@your-server:7779
```

### 编程语言示例

**Python**：
```python
import requests

# HTTP 代理
proxies = {'http': 'http://localhost:7777', 'https': 'http://localhost:7777'}
requests.get('https://httpbin.org/ip', proxies=proxies)

# SOCKS5 代理（需 pip install requests[socks]）
proxies = {'http': 'socks5://localhost:7779', 'https': 'socks5://localhost:7779'}
requests.get('https://httpbin.org/ip', proxies=proxies)
```

**Node.js**：
```javascript
// SOCKS5（需 npm install socks-proxy-agent node-fetch）
const { SocksProxyAgent } = require('socks-proxy-agent');
const fetch = require('node-fetch');
const agent = new SocksProxyAgent('socks5://localhost:7779');
fetch('https://httpbin.org/ip', { agent }).then(r => r.json()).then(console.log);
```

**浏览器 / SSH**：
```bash
# 浏览器：设置 → 代理 → SOCKS5 → localhost:7779
# SSH 隧道：
ssh -o ProxyCommand='nc -X 5 -x localhost:7779 %h %p' user@remote-server
```

## 订阅导入

通过 WebUI 管理订阅（管理员登录后）：

1. **订阅 URL** — 填入 Clash/V2ray 订阅地址，自动识别格式并解析
2. **上传文件** — 拖拽或选择 Clash YAML / V2ray 配置文件

支持的节点协议：vmess、vless、trojan、shadowsocks、hysteria2、anytls、http、socks5

订阅代理与免费代理的区别：
- 健康检查失败 → 禁用（不删除），定时探测唤醒
- 不受免费池 slot 容量限制
- 地理过滤 → 禁用（不删除）
- 连续 7 天无可用节点 → 自动移除订阅

访客可通过顶部「贡献订阅」按钮分享自己的订阅 URL 或配置文件。

## Docker 部署详解

### docker run 方式

```bash
docker run -d --name proxygo \
  -p 7776:7776 -p 7777:7777 -p 7778:7778 -p 7779:7779 -p 7780:7780 \
  -e WEBUI_PASSWORD=your_password \
  -e PROXY_AUTH_ENABLED=true \
  -e PROXY_AUTH_USERNAME=myuser \
  -e PROXY_AUTH_PASSWORD=mypass \
  -v goproxy-data:/app/data \
  ghcr.io/isboyjc/goproxy:latest
```

### 数据持久化

- docker-compose 使用 Named Volume `goproxy-data`，容器重启/更新不丢数据
- 数据包含：SQLite 数据库（代理池）、config.json（配置）、sing-box 配置

**备份**：
```bash
docker run --rm -v goproxy-data:/data -v $(pwd):/backup \
  alpine tar czf /backup/goproxy-backup-$(date +%Y%m%d).tar.gz -C /data .
```

**恢复**：
```bash
docker compose down
docker run --rm -v goproxy-data:/data -v $(pwd):/backup \
  alpine sh -c "cd /data && tar xzf /backup