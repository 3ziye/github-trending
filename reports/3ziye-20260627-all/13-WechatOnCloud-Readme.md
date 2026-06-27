<div align="center">

<img src="doc/img/icon-192.png" width="88" height="88" alt="云微 logo" />

<h1>云微 · WechatOnCloud</h1>

<p><b>在自己的 NAS / 服务器上运行「服务端微信」，多端浏览器共享同一会话</b></p>

<p>不止微信——还能开 <b>Chromium 浏览器实例</b>，登录 Telegram / X / Instagram 等网页版社媒，常驻云端、多端同步</p>

<p>
  <a href="https://github.com/Gloridust/WechatOnCloud/stargazers"><img src="https://img.shields.io/github/stars/Gloridust/WechatOnCloud?style=flat-square&logo=github" alt="stars" /></a>
  <a href="https://github.com/Gloridust/WechatOnCloud/releases"><img src="https://img.shields.io/github/v/release/Gloridust/WechatOnCloud?style=flat-square" alt="release" /></a>
  <a href="https://github.com/Gloridust/WechatOnCloud/issues"><img src="https://img.shields.io/github/issues/Gloridust/WechatOnCloud?style=flat-square" alt="issues" /></a>
  <img src="https://img.shields.io/badge/arch-amd64%20%7C%20arm64-2496ED?style=flat-square&logo=docker&logoColor=white" alt="arch" />
  <img src="https://img.shields.io/badge/PWA-ready-5A0FC8?style=flat-square" alt="pwa" />
  <a href="https://x.com/gloridust1024"><img src="https://img.shields.io/badge/Twitter-@gloridust1024-1DA1F2?style=flat-square&logo=x&logoColor=white" alt="twitter" /></a>
  <a href="https://t.me/WechatOnCloud"><img src="https://img.shields.io/badge/Telegram-WechatOnCloud-26A5E4?style=flat-square&logo=telegram&logoColor=white" alt="telegram" /></a>
</p>

<p>
  <a href="#快速开始">快速开始</a> ·
  <a href="#核心特性">核心特性</a> ·
  <a href="#浏览器实例登录网页版社媒">浏览器实例</a> ·
  <a href="doc/运行原理.md">运行原理</a> ·
  <a href="#安全须知必读">安全须知</a> ·
  <a href="doc/技术方案.md">技术方案</a>
</p>

<table>
  <tr>
    <td width="50%"><img src="doc/img/Screenshot-1.png" alt="云微 · 面板主界面" /></td>
    <td width="50%"><img src="doc/img/Screenshot-2.png" alt="云微 · 实例桌面" /></td>
  </tr>
</table>

</div>

在飞牛 NAS（x86_64 / arm64）或任意 Docker 主机上运行服务端微信：面板可管理**多个**实例，每个实例都是一个独立容器——可以是一个**微信**会话，也可以是一个 **Chromium 浏览器**（用来登录 Telegram / X / Instagram 等网页版应用）。多个 web 用户通过浏览器访问被授权的实例，实现跨设备同步、多端共享。**不修改微信客户端。**

**一句话原理**：每个实例 = 一个容器，里面跑 Xvfb 虚拟显示 + 一个应用（官方原版微信，或 Chromium 浏览器），KasmVNC 把画面串到浏览器；同一实例被多个浏览器连 = 共享同一个会话。前面一层自研**面板**是唯一对外入口，经 docker.sock 按需创建/销毁实例并反向代理。

交流群: [@WechatOnCloud](https://t.me/WechatOnCloud)

---

## 核心特性

- 🗂️ **多实例** — 一个面板管理多个独立实例，每个实例独立容器 + 独立数据卷，互不干扰。
- 🌐 **多应用（微信 + 浏览器）** — 新建实例时可选**微信**或 **Chromium 浏览器**；浏览器实例用来登录 Telegram / X / Instagram 等网页版社媒，登录态写进数据卷、常驻云端、多端共享。
- 👥 **多端共享 + 权限** — 多浏览器 / 设备共享同一会话；子账号体系，按账号分配可访问的实例（RBAC）。
- 🖥️ **PC 式界面** — 左侧实例栏 + 右侧内嵌桌面，侧栏可折叠，移动端自动转抽屉；实例图标可自定义（内置图标 / 上传裁剪）。
- 📦 **微信按需下载 · 浏览器开箱即用** — 镜像不打包微信，面板一键「下载安装 / 更新」带进度条、按架构取包；Chromium 已烤进镜像，创建即用、无需下载。
- 🔁 **实例生命周期** — 启动 / 停止 / 重启 / 升级（拉新镜像重建、保留聊天记录），均在面板内一键完成。
- 📎 **文件传输 + 文本剪贴板** — 拖拽上传 + 下载 + 删除，直达实例桌面 `~/Desktop`；文本可经剪贴板中转送进实例（局域网 http 下也可用）。
- 🧩 **多端协作软锁** — 同一实例多人操作时自动只读 + 申请接管，避免键鼠打架。
- 🔒 **安全优先** — 面板为唯一入口，KasmVNC 凭据服务端注入、永不下发前端；docker.sock 仅管理员可触达。
- 📱 **PWA** — iOS「添加到主屏幕」、桌面 Chrome「安装」当原生 App。
- 🏗️ **多架构** — amd64 / arm64 预构建镜像（Docker Hub + GHCR，GitHub Actions 自动发布）。

---

## 文档

| 文档 | 内容 |
|------|------|
| [运行原理与 Docker 指南](doc/运行原理.md) | 工作原理 + 架构图；面向 Docker 新手的逐步拆解、常用命令、架构自动适配 |
| [部署与运维](doc/部署与运维.md) | 数据持久化、常见问题排查、忘记超管密码的离线找回、目录结构 |
| [设备伪装与风控应对](doc/设备伪装.md) | 唯一 machine-id / 真实 hostname / os-release 伪装；账号被微信强制退出循环时怎么办 |
| [数据卷管理与迁移](doc/数据卷管理.md) | 管理员在面板里备份/恢复整卷、上传 PC 微信数据、浏览管理实例 /config 文件 |
| [发布到 GHCR](doc/发布到GHCR.md) | 用 GitHub Actions 或本机 buildx 把镜像发布到 GHCR |
| [技术方案](doc/技术方案.md) | 完整设计文档与选型权衡 |

---

## 快速开始

> 需已安装 Docker（含 Compose 插件）。x86_64 / arm64 均可。不熟悉 Docker？先读 [运行原理与 Docker 指南](doc/运行原理.md)。

`docker-compose.yml` 默认引用 **Docker Hub** 上的镜像 `docker.io/gloridust/{woc-panel,wechat-on-cloud}`（同时也发布到 GHCR 作为备用源）。
**这两个镜像需先存在**——要么官方已发布（你能直接拉取），要么你在本地自行构建。二选一：

**方式 A · 本地自构建（官方尚未发布镜像时用这个）**

```bash
git clone https://github.com/Gloridust/WechatOnCloud.git WechatOnCloud
cd WechatOnCloud
cp .env.example .env            # 至少改掉默认密码 WOC_PASSWORD
./scripts/build-local.sh        # 构建面板 + 微信实例镜像，打成 compose 用的同名标签
docker compose up -d            # compose 默认优先用本地镜像，不会再去远端拉
```

**方式 B · 拉取官方镜像（推荐，无需 clone 整个仓库）**

部署**只需要 `docker-compose.yml` 这一个文件**——它用 `image:` 直接拉官方镜像，面板数据放在该文件旁自动创建的 `./data-panel` 目录，不依赖仓库里的其它文件。

- **命令行**：丢进一个空目录拉起即可
  ```bash
  mkdir woc && cd woc
  curl -fsSL https://raw.githubusercontent.com/Gloridust/WechatOnCloud/main/docker-compose.yml -o docker-compose.yml
  docker compose up -d            # 默认从 Docker Hub 拉取（公开、amd64/arm64 多架构）
  ```
  > `raw.githubusercontent.com` 拉不动时，在 GitHub 网页打开根目录的 [docker-compose.yml](docker-compose.yml)，复制内容自己建个同名文件即可。

- **飞牛 OS（fnOS）/ 群晖 等 NAS**：在 **Docker → Compose 一键部署** 界面，把根目录 [docker-compose.yml](docker-compose.yml) 的内容**直接粘贴进去**即可部署，无需命令行、无需 clone。

> **改配置（强烈建议至少改密码）**：默认管理员 **admin / wechat**。登录后在「修改密码」里改；或部署前在 `docker-compose.yml` 旁放一个 `.env`（从 [.env.example](.env.example) 下载改名），又或在 NAS 的 Compose 环境变量里填 `WOC_PASSWORD`、`WOC_HTTP_PORT`、`WOC_IMAGE_PREFIX` 等（全部可配置项见 [.env.example](.env.example)）。

> **镜像源**：默认 Docker Hub（国内外通用、免登录，**飞牛等 NAS 还内置了 Docker Hub 加速**，通常比 GHCR 更稳）。