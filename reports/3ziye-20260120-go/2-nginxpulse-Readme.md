<p align="center">
  <img src="docs/brand-mark.svg" alt="NginxPulse Logo" width="120" height="120">
</p>

<p align="center">
  <a href="README_EN.md">English</a> | 简体中文
</p>

# NginxPulse

轻量级 Nginx 访问日志分析与可视化面板，提供实时统计、PV 过滤、IP 归属地与客户端解析。

![demo-img-1.png](docs/demo-img-1.png)

![demo-img-2.png](docs/demo-img-2.png)
## 目录
- [项目开发技术栈](#项目开发技术栈)
- [IP 归属地查询策略](#ip-归属地查询策略)
- [如何使用项目](#如何使用项目)
  - [1) Docker](#1-docker)
  - [2) Docker Compose](#2-docker-compose)
  - [3) 手动构建（前端、后端）](#3-手动构建前端后端)
  - [4) 单体部署（单进程）](#4-单体部署单进程)
  - [5) Makefile 常用命令](#5-makefile-常用命令)
- [多个日志文件如何挂载？](#多个日志文件如何挂载)
- [远端日志支持（sources）](#远端日志支持sources)
- [Push Agent（实时推送）](#push-agent实时推送)
- [自定义日志格式](#自定义日志格式)
- [Caddy 日志支持](#caddy-日志支持)
- [访问密钥列表（ACCESS_KEYS）](#访问密钥列表access_keys)
- [常见问题](#常见问题)
- [二次开发注意事项](#二次开发注意事项)
- [目录结构与主要文件](#目录结构与主要文件)

## 项目开发技术栈
- **后端**：`Go 1.23.x` · `Gin` · `Logrus`
- **数据**：`SQLite (modernc.org/sqlite)`
- **IP 归属地**：`ip2region`（本地库） + `ip-api.com`（远程批量）
- **前端**：`Vue 3` · `Vite` · `TypeScript` · `PrimeVue` · `ECharts/Chart.js` · `Scss`
- **容器**：`Docker / Docker Compose` · `Nginx`（前端静态部署）

## IP 归属地查询策略
1. **快速过滤**：空值/本地/回环地址返回“本地”，内网地址返回“内网/本地网络”。
2. **缓存优先**：内存缓存命中直接返回（最多缓存 50,000 条）。
3. **远程优先**：调用 `ip-api.com/batch` 批量查询，超时 1.2s，单批最多 100 个。
4. **本地兜底**：远程失败或结果为“未知”时，IPv4 使用内置 ip2region 数据库本地查询（50ms 超时）。
5. **IPv6 处理**：仅走远程查询，远程失败则返回“未知”。

> 本地数据库 `ip2region.xdb` 内嵌在二进制中，首次启动会自动解压到 `./var/nginxpulse_data/ip2region.xdb`，并尝试加载向量索引提升查询性能。

> 本项目会访问外网 IP 归属地 API（`ip-api.com`），部署环境需放行该域名的出站访问。

## 如何使用项目

### 1) Docker
单镜像（前端 Nginx + 后端服务）：

使用远程镜像（Docker Hub）：

```bash
docker run -d --name nginxpulse \
  -p 8088:8088 \
  -p 8089:8089 \
  -e WEBSITES='[{"name":"主站","logPath":"/share/log/nginx/access.log","domains":["kaisir.cn","www.kaisir.cn"]}]' \
  -v ./nginx_data/logs/all/access.log:/share/log/nginx/access.log:ro \
  -v "$(pwd)/var/nginxpulse_data:/app/var/nginxpulse_data" \
  magiccoders/nginxpulse:latest
```

本地构建运行：

```bash
docker build -t nginxpulse:local .
docker run -d --name nginxpulse \
  -p 8088:8088 \
  -p 8089:8089 \
  -e WEBSITES='[{"name":"主站","logPath":"/share/log/nginx/access.log","domains":["kaisir.cn","www.kaisir.cn"]}]' \
  -v ./nginx_data/logs/all/access.log:/share/log/nginx/access.log:ro \
  -v "$(pwd)/var/nginxpulse_data:/app/var/nginxpulse_data" \
  nginxpulse:local
```

多架构镜像（amd64/arm64）构建与发布：

```bash
./scripts/publish_docker.sh -r <repo> -p linux/amd64,linux/arm64
```

仅本地构建指定架构示例：

```bash
docker buildx build --platform linux/arm64 -t nginxpulse:local --load .
```

GitHub Actions 自动发布（多架构镜像）：
- 在仓库 Secrets 中配置：
  - `DOCKERHUB_USERNAME`
  - `DOCKERHUB_TOKEN`
  - `DOCKERHUB_REPO`（例如：`username/nginxpulse`）
- 推送 `v*` tag 或发布 Release 时触发。

> 如果更偏好配置文件方式，可将 `configs/nginxpulse_config.json` 挂载到容器内的 `/app/configs/nginxpulse_config.json`。

### 2) Docker Compose
使用远程镜像（Docker Hub）：将 `docker-compose.yml` 改为下方远程镜像版本，然后执行：

```bash
docker compose up -d
```

本地构建运行（基于源码构建镜像）：保持仓库自带的 `docker-compose.yml`，执行：

```bash
docker compose up -d --build
```

示例 `docker-compose.yml`（远程镜像）：

```yml
version: "3.8"
services:
  nginxpulse:
    image: magiccoders/nginxpulse:latest
    container_name: nginxpulse
    ports:
      - "8088:8088"
      - "8089:8089"
    environment:
      WEBSITES: '[{"name":"主站","logPath":"/share/log/nginx/access.log","domains":["kaisir.cn","www.kaisir.cn"]}]'
    volumes:
      - ./nginx_data/logs/all/access.log:/share/log/nginx/access.log:ro
      - ./var/nginxpulse_data:/app/var/nginxpulse_data
      - /etc/localtime:/etc/localtime:ro
    restart: unless-stopped
```

示例 `docker-compose.yml`（本地构建）：

```yml
version: "3.8"
services:
  nginxpulse:
    image: nginxpulse:local
    build:
      context: .
    container_name: nginxpulse
    ports:
      - "8088:8088"
      - "8089:8089"
    environment:
      WEBSITES: '[{"name":"主站","logPath":"/share/log/nginx/access.log","domains":["kaisir.cn","www.kaisir.cn"]}]'
    volumes:
      - ./nginx_data/logs/all/access.log:/share/log/nginx/access.log:ro
      - ./var/nginxpulse_data:/app/var/nginxpulse_data
      - /etc/localtime:/etc/localtime:ro
    restart: unless-stopped
```

说明：
- `logPath` 必须是容器内路径，确保与挂载目录一致。
- `var/nginxpulse_data` 挂载用于持久化数据库和解析缓存，推荐保留。

参数说明（环境变量）：
- `WEBSITES`（必填，无配置文件时）
  - 网站列表 JSON 数组，字段：`name`、`logPath`、`sources`、`domains`（可选）。
  - 当配置 `sources` 时将忽略 `logPath`，并以远端来源作为日志输入。
  - `domains` 用于将 referer 归类为“站内访问”，不影响日志解析与 PV 过滤。
- `CONFIG_JSON`（可选）
  - 完整配置 JSON 字符串（等同于 `configs/nginxpulse_config.json` 内容）。
  - 设置后会忽略本地配置文件，其他环境变量仍可覆盖其中字段。
- `LOG_DEST`（可选，默认：`file`）
  - 日志输出位置：`file` 或 `stdout`。
- `TASK_INTERVAL`（可选，默认：`1m`）
  - 扫描间隔，支持 `5m`、`25s` 等 Go duration 格式。
- `LOG_RETENTION_DAYS`（可选，默认：`30`）
  - 日志保留天数，超过天数会清理数据库中的旧日志。
- `DEMO_MODE`（可选，默认：`false`）
  - 开启演示模式，定时生成模拟日志并直接写入数据库（不再解析日志文件）。
- `ACCESS_KEYS`（可选，默认：空）
  - 访问密钥列表（JSON 数组或逗号分隔），配置后将启用访问限制。
- `APP_LANGUAGE`（可选，默认：`zh-CN`）
  - 系统默认语言，支持 `zh-CN` / `en-US`（也接受 `zh`、`en`）。
  - 会同步影响 IP 归属地在线查询返回语言。
- `SERVER_PORT`（可选，默认：`:8089`）
  - 服务监听地址，可传 `: