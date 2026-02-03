<p align="center">
  <img src="https://raw.githubusercontent.com/likaia/nginxpulse/main/docs/brand-mark.svg" alt="NginxPulse Logo" width="120" height="120">
</p>

<p align="center">
  <a href="https://github.com/likaia/nginxpulse/blob/main/README_EN.md">English</a> | 简体中文
</p>

# NginxPulse

轻量级 Nginx 访问日志分析与可视化面板，提供实时统计、PV 过滤、IP 归属地与客户端解析。

源码仓库：https://github.com/likaia/nginxpulse

> ⚠️注意：此文档只讲解了如何使用这个项目，详细文档与示例配置请移步Wiki：https://github.com/likaia/nginxpulse/wiki

![demo-img-1.png](https://raw.githubusercontent.com/likaia/nginxpulse/main/docs/demo-img-1.png)

![demo-img-2.png](https://raw.githubusercontent.com/likaia/nginxpulse/main/docs/demo-img-2.png)
## 目录
- [项目开发技术栈](#项目开发技术栈)
- [IP 归属地查询策略](#ip-归属地查询策略)
- [如何使用项目](#如何使用项目)
  - [1) Docker](#1-docker)
  - [2) Docker Compose](#2-docker-compose)
  - [时区设置（重要）](#时区设置重要)
  - [3) 手动构建（前端、后端）](#3-手动构建前端后端)
  - [4) 单体部署（单进程）](#4-单体部署单进程)
  - [5) Makefile 常用命令](#5-makefile-常用命令)
- [Docker 部署权限说明](#docker-部署权限说明)
- [常见问题](#常见问题)
- [目录结构与主要文件](#目录结构与主要文件)
- [致谢](#致谢)

## 项目开发技术栈
**重要提示（版本 > 1.5.3）**：已完全弃用 SQLite；单体部署必须自备 PostgreSQL 并配置 `DB_DSN`（或 `database.dsn`）。
- **后端**：`Go 1.24.x` · `Gin` · `Logrus`
- **数据**：`PostgreSQL (pgx)`
- **IP 归属地**：`ip2region`（本地库） + `ip-api.com`（远程批量）
- **前端**：`Vue 3` · `Vite` · `TypeScript` · `PrimeVue` · `ECharts/Chart.js` · `Scss`
- **容器**：`Docker / Docker Compose` · `Nginx`（前端静态部署）

### IP 归属地查询策略
1. **快速过滤**：空值/本地/回环地址返回“本地”，内网地址返回“内网/本地网络”。
2. **解析解耦**：日志解析阶段仅入库并标记“待解析”，IP 归属地由后台任务异步补齐并回填。
3. **缓存优先**：持久化缓存 + 内存缓存命中直接返回（默认上限 1,000,000 条）。
4. **本地优先（IPv4/IPv6）**：优先查 ip2region，本地结果可用时直接使用。
5. **远程补齐**：本地返回“未知”或解析失败时，调用远端 API（默认 `ip-api.com/batch`，可配置）批量查询（超时 1.2s，单批最多 100 个）。
6. **远程失败**：返回“未知”。

> 归属地解析未完成时，页面会显示“待解析”，地域统计可能不完整。

> 本地数据库 `ip2region_v4.xdb` 与 `ip2region_v6.xdb` 内嵌在二进制中，首次启动会自动解压到 `./var/nginxpulse_data/`，并尝试加载向量索引提升查询性能。

> 本项目会访问外网 IP 归属地 API（默认 `ip-api.com`），部署环境需放行该域名的出站访问。同时也支持自己搭建IP归属地查询服务，详见下文。

## 如何使用项目

### 1) Docker
单镜像（前端 Nginx + 后端服务）：
> 镜像内置 PostgreSQL，启动时会自动初始化数据库（未自备数据库时）。**必须挂载数据目录**：`/app/var/nginxpulse_data` 与 `/app/var/pgdata`。未挂载时容器会直接退出并报错。

一键启动（极简配置，首次启动进入初始化向导）：

```bash
docker run -d --name nginxpulse \
  -p 8088:8088 \
  -v ./docker_local/logs:/share/logs:ro \
  -v ./docker_local/nginxpulse_data:/app/var/nginxpulse_data \
  -v ./docker_local/pgdata:/app/var/pgdata \
  -v ./docker_local/configs:/app/configs \
  -v /etc/localtime:/etc/localtime:ro \
  magiccoders/nginxpulse:latest
```

> 注意：docker_local请替换为你宿主机存在的目录，确保文件权限设置正确，能被容器正常访问，否则会出现无日志的情况。


> 如果更偏好配置文件方式，可将 `configs/nginxpulse_config.json` 挂载到容器内的 `/app/configs/nginxpulse_config.json`。
> 若未提供配置文件/环境变量，首次启动会进入“初始化配置向导”。保存后会写入 `configs/nginxpulse_config.json`，需重启容器生效（建议挂载 `/app/configs` 以持久化）。

### 2) Docker Compose
使用远程镜像（Docker Hub）：
```yaml
services:
  nginxpulse:
    image: magiccoders/nginxpulse:latest
    container_name: local_nginxpulse
    ports:
      - "8088:8088"
      - "8089:8089"
    volumes:
      - ./docker_local/logs:/share/logs
      - ./docker_local/nginxpulse_data:/app/var/nginxpulse_data
      - ./docker_local/pgdata:/app/var/pgdata
      - ./docker_local/configs:/app/configs
      - /etc/localtime:/etc/localtime
    restart: unless-stopped
```

```bash
docker compose up -d
```

### 时区设置（重要）
本项目使用**系统时区**进行日志时间解析与统计，请确保运行环境时区正确。

**Docker / Docker Compose**
- 推荐挂载宿主机时区：`-v /etc/localtime:/etc/localtime:ro`（Linux）
- 若宿主机提供 `/etc/timezone`，可额外挂载：`-v /etc/timezone:/etc/timezone:ro`
- 若你只想指定时区，可设置 `TZ=Asia/Shanghai`，但需保证容器内有时区数据（例如安装 `tzdata` 或挂载 `/usr/share/zoneinfo`）

**单体部署（单进程）**
- 默认使用当前系统时区
- 可通过环境变量临时指定：`TZ=Asia/Shanghai ./nginxpulse`

### 移动端访问（/m）
- 入口地址：`http://<host>:8088/m`
- 移动端仅提供 **概览 / 日报 / 实时 / 日志** 四个页面
- **首次初始化必须在电脑端完成**，移动端会提示在电脑打开

### 3) 手动构建（前端、后端）
前端构建：

```bash
cd webapp
npm install
npm run build
```

移动端构建（/m）：

```bash
cd webapp_mobile
npm install
npm run build
```

后端构建：

```bash
go mod download
go build -o bin/nginxpulse ./cmd/nginxpulse/main.go
```

本地开发（前后端一起跑）：

```bash
./scripts/dev_local.sh
```

> 前端开发服务默认端口 8088，并会将 `/api` 代理到 `http://127.0.0.1:8089`。
> 本地开发前请准备好日志文件，放在 `var/log/` 下（或确保 `configs/nginxpulse_config.json` 的 `logPath` 指向对应文件）。

### 4) 单体部署（单进程）
**重要提示（版本 > 1.5.3）**：已彻底弃用 SQLite。单体部署必须自备 PostgreSQL 并配置 `DB_DSN`（或在 `configs/nginxpulse_config.json` 填好 `database.dsn`）。  
从仓库的releases下载对应平台的二进制文件，执行即可。

执行后会生成单体可执行文件（已内置前端静态资源），启动后即可同时提供前后端服务：
- 前端：`http://localhost:8088`
- 后端：`http://localhost:8088/api/...`

#### 单体部署的配置方式
单体运行时读取配置有两种方式（任选其一）：

**方式 A：配置文件（默认）**
1. 在运行目录创建 `configs/`
2. 放入 `configs/nginxpulse_config.json`
3. 启动：`./nginxpulse`

**方式 B：环境变量注入（无需文件）**
```bash
CONFIG_JSON="$(cat /path/to/nginxpulse_config.json)" ./nginxpulse
```

注意事项：
- 配置文件路径为相对路径 `./configs/nginxpulse_config.json`，请确保运行时工作目录正确。
- 如果使用 systemd，请设置 `WorkingDirectory`，或改用 `CONFIG_JSON` 注入。
- 数据目录 `./var/nginxpulse_data` 也是相对路径；找不到目录时请先确认当前进程的工作目录。

### 5) Makefile 构建
此项目也支持了通过Makefile来构建相关资源，命令如下：
```bash
make frontend   # 构建前端（含移动端）webapp/dist + webapp_mobile/dist
make frontend-mobile # 仅构建