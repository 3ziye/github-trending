<div align="center">
  <img src="https://i.mji.rip/2025/09/27/eedc7b701c0fa5c1f7c175b22f441ad9.jpeg" alt="Clash" width="128" style="border-radius: 16px;" />
</div>

<h2 align="center">
LogVar 弹幕 API 服务器
</h2>

[![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github)](https://github.com/huangxd-/damnu_api)
![GitHub forks](https://img.shields.io/github/forks/huangxd-/danmu_api)
![GitHub Repo stars](https://img.shields.io/github/stars/huangxd-/danmu_api)
![GitHub License](https://img.shields.io/github/license/huangxd-/danmu_api)
![Docker Image Version](https://img.shields.io/docker/v/logvar/danmu-api?sort=semver)
![Docker Pulls](https://img.shields.io/docker/pulls/logvar/danmu-api)
[![telegram](https://img.shields.io/static/v1?label=telegram&message=telegram_channel&color=blue)](https://t.me/logvar_danmu_channel)
[![telegram](https://img.shields.io/static/v1?label=telegram&message=telegram_group&color=blue)](https://t.me/logvar_danmu_group)

---

一个人人都能部署的基于 js 的弹幕 API 服务器，支持爱优腾芒哔人韩弹幕直接获取，兼容弹弹play的搜索、详情查询和弹幕获取接口，并提供日志记录，支持vercel/cloudflare/docker/claw等部署方式，不用提前下载弹幕，没有nas或小鸡也能一键部署。

本项目仅为个人爱好开发，代码开源。如有任何侵权行为，请联系本人删除。

有问题提issue或 [私信机器人](https://t.me/ddjdd_bot) 都ok。

新加了 [tg频道](https://t.me/logvar_danmu_channel) ，方便发送更新通知，以及群组，太多人私信咨询了，索性增加一个 [互助群](https://t.me/logvar_danmu_group) ，大家有问题可以在群里求助。

> 请不要在国内媒体平台宣传本项目！

## 功能
- **API 接口**：
  - `GET /api/v2/search/anime?keyword=${queryTitle}`：根据关键字搜索动漫。
  - `POST /api/v2/match`：根据关键字匹配动漫，用于自动匹配。
  - `GET /api/v2/search/episodes`：根据关键词搜索所有匹配的剧集信息。
  - `GET /api/v2/bangumi/:animeId`：获取指定动漫的详细信息。
  - `GET /api/v2/comment/:commentId?withRelated=true&chConvert=1`：获取指定弹幕评论，支持返回相关评论和字符转换。
  - `GET /api/logs`：获取最近的日志（最多 500 行，格式为 `[时间戳] 级别: 消息`）。
- **日志记录**：捕获 `console.log`（info 级别）和 `console.error`（error 级别），JSON 内容格式化输出。
- **部署支持**：支持本地运行、Docker 容器化、Vercel 一键部署、Cloudflare 一键部署和 Docker 一键启动。

## 前置条件
- Node.js（v18.0.0 或更高版本；理论兼容更低版本，请自行测试）
- npm
- Docker（可选，用于容器化部署）

## 本地运行
1. **克隆仓库**：
   ```bash
   git clone <仓库地址>
   cd <项目目录>
   ```

2. **安装依赖**：
   ```bash
   npm install
   ```

3. **启动服务器**：
   ```bash
   npm start
   ```
   服务器将在 `http://{ip}:9321` 运行，默认token是`87654321`。
   或者使用下面的命令
   ```bash
   # 启动
   node ./danmu_api/server.js
   # 测试
   node --test ./danmu_api/worker.test.js
   ```

4. **测试 API**：
   使用 Postman 或 curl 测试：
   - `GET http://{ip}:9321/87654321`
   - `GET http://{ip}:9321/87654321/api/v2/search/anime?keyword=生万物`
   - `POST http://{ip}:9321/87654321/api/v2/api/v2/match`
   - `GET http://{ip}:9321/87654321/api/v2/search/episodes?anime=生万物`
   - `GET http://{ip}:9321/87654321/api/v2/bangumi/1`
   - `GET http://{ip}:9321/87654321/api/v2/comment/1?withRelated=true&chConvert=1`
   - `GET http://{ip}:9321/87654321/api/logs`

## 使用 Docker 运行
1. **构建 Docker 镜像**：
   ```bash
   docker build -t danmu-api .
   ```

2. **运行容器**：
   ```bash
   docker run -d -p 9321:9321 --name danmu-api -e TOKEN=87654321 danmu-api
   ```
   - 使用`-e TOKEN=87654321`设置`TOKEN`环境变量，覆盖Dockerfile中的默认值。

3. **测试 API**：
   使用 `http://{ip}:9321/{TOKEN}` 访问上述 API 接口。

## Docker 一键启动 【推荐】
1. **拉取镜像**：
   ```bash
   docker pull logvar/danmu-api:latest
   ```

2. **运行容器**：
   ```bash
   docker run -d -p 9321:9321 --name danmu-api -e TOKEN=87654321 logvar/danmu-api:latest
   ```
   - 使用`-e TOKEN=87654321`设置`TOKEN`环境变量。

   ```yaml
   services:
     danmu-api:
       image: logvar/danmu-api:latest
       container_name: danmu-api
       ports:
         - "9321:9321"
       environment:
         - TOKEN=87654321  # 请将 87654321 替换为你想自定义的 Token 值
       restart: unless-stopped    # 可选配置，容器退出时自动重启（非必需，可根据需求删除）
   ```
   - 或使用docker compose部署。
   ```yaml
   services:
     watchtower:
       image: containrrr/watchtower
       container_name: watchtower-gx
       restart: always
       volumes:
         - /var/run/docker.sock:/var/run/docker.sock
       environment:
         - TZ=Asia/Shanghai  # 保持时区正确
       command:
         - --cleanup         # 更新后清理旧镜像
         - --interval        # 间隔参数
         - "12600"           # 30分钟（1800秒），适合测试
         - danmu-api         # 监控的目标容器名
   ```
   - 可以使用watchtower监控有新版本自动更新。

3. **测试 API**：
   使用 `http://{ip}:9321/{TOKEN}` 访问上述 API 接口。

## 部署到 Vercel 【推荐】

### 一键部署
点击以下按钮即可将项目快速部署到 Vercel：

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/huangxd-/danmu_api&project-name=danmu_api&repository-name=danmu_api)

**注意**：请将按钮链接中的 `https://github.com/huangxd-/danmu_api` 替换为你的实际 Git 仓库地址。编辑 `README.md` 并更新链接后，推送到仓库，点击按钮即可自动克隆和部署。
- **设置环境变量**：部署后，在 Vercel 仪表板中：
  1. 转到你的项目设置。
  2. 在“Environment Variables”部分添加 `TOKEN` 变量，输入你的 API 令牌值。
  3. 保存更改并重新部署。
- 示例请求：`https://{your_domian}.vercel.app/87654321/api/v2/search/anime?keyword=子夜归`

### 优化点
Settings > Functions > Advanced Setting > Function Region 切换为 Hong Kong，能提高访问速度，体验更优
> hk有可能访问不了360，也可以尝试切其他region，如新加坡等

## 部署到 腾讯云 edgeone pages

### 一键部署
[![使用 EdgeOne Pages 部署](https://cdnstatic.tencentcs.com/edgeone/pages/deploy.svg)](https://console