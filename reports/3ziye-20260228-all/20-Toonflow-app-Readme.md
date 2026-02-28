<p>
  <a href="https://github.com/HBAI-Ltd/Toonflow-app">
    <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" />
  </a>
  &nbsp;|&nbsp;
  <a href="https://gitee.com/HBAI-Ltd/Toonflow-app">
    <img src="https://img.shields.io/badge/Gitee-C71D23?style=flat-square&logo=gitee&logoColor=white" alt="Gitee" />
  </a>
</p>

<p align="center">
  <strong>中文</strong> | 
  <a href="./docs/README.en.md">English</a>
</p>

<div align="center">

<img src="./docs/logo.png" alt="Toonflow Logo" height="120"/>

# Toonflow

  <p align="center">
    <b>
      AI短剧工厂
      <br />
      动动手指，小说秒变剧集！
      <br />
      AI剧本 × AI影像 × 极速生成 🔥
    </b>
  </p>
  <p align="center">
    <a href="https://github.com/HBAI-Ltd/Toonflow-app/stargazers">
      <img src="https://img.shields.io/github/stars/HBAI-Ltd/Toonflow-app?style=for-the-badge&logo=github" alt="Stars Badge" />
    </a>
    <a href="https://www.gnu.org/licenses/agpl-3.0" target="_blank">
      <img src="https://img.shields.io/badge/License-AGPL-blue.svg?style=for-the-badge" alt="AGPL License Badge" />
    </a>
    <a href="https://github.com/HBAI-Ltd/Toonflow-app/releases">
      <img alt="release" src="https://img.shields.io/github/v/release/HBAI-Ltd/Toonflow-app?style=for-the-badge" />
    </a>
  </p>
  
  > 🚀 **一站式短剧工程**：从文本到角色，从分镜到视频，0门槛全流程AI化，创作效率提升10倍+！
</div>

---

# 🌟 主要功能

Toonflow 是一款 AI 工具，能够利用 AI 技术将小说自动转化为剧本，并结合 AI 生成的图片和视频，实现高效的短剧创作。借助 Toonflow，可以轻松完成从文字到影像的全流程，让短剧制作变得更加智能与便捷。

- ✅ **角色生成**  
   自动分析原始小说文本，智能识别并生成角色设定，包括外貌、性格、身份等详细信息，为后续剧本与画面创作提供可靠基础。
- ✅ **剧本生成**  
   基于选定事件和章节，系统自动生成结构化剧本，涵盖对白、场景描述、剧情走向，实现从文学文本到影视剧本的高效转换。
- ✅ **分镜制作**  
   根据剧本内容，智能生成分镜提示词与画面设计，细化前中后景、角色动态、道具设定和场景布局，自动根据剧本生成分镜，为视频制作提供完整路线蓝图。
- ✅ **视频合成**  
   集成 AI 图像与视频技术，可使用 AI 生成视频片段。整合在线编辑，支持个性化调整输出，让影视创作高效协同、快捷落地。

---

# 📦 应用场景

- 短视频内容创作
- 小说影视化实验
- AI 文学改编工具
- 剧本开发与快速原型
- 视频素材生成

---

# 🔰 使用指南

## 📺 视频教程

https://www.bilibili.com/video/BV1na6wB6Ea2
[![Toonflow 8 分钟快速上手 AI 视频](./docs/videoCover.png)](https://www.bilibili.com/video/BV1na6wB6Ea2)

**Toonflow 8 分钟快速上手 AI 视频**
👉 [点击观看](https://www.bilibili.com/video/BV1na6wB6Ea2/?share_source=copy_web&vd_source=5b718c25439a901a34c7bc0c1d35b38e)

📱 手机微信扫码观看

<img src="./docs/videoQR.png" alt="微信扫码观看" width="150"/>

---

# 🚀 安装

## 前置条件

在安装和使用本软件之前，请准备以下内容：

- ✅ 大语言模型 AI 服务接口地址
- ✅ Sora 或豆包视频服务接口地址
- ✅ Nano Banana Pro 图片生成模型服务接口

## 本机安装

### 1. 下载与安装

| 操作系统 | GitHub 下载                                                  | 夸克网盘下载                                    | 说明           |
| :------: | :----------------------------------------------------------- | :---------------------------------------------- | :------------- |
| Windows  | [Release](https://github.com/HBAI-Ltd/Toonflow-app/releases) | [夸克网盘](https://pan.quark.cn/s/94ef07509df0) | 官方发布安装包 |
|  Linux   | ⚙️ 敬请期待                                                  | ⚙️ 敬请期待                                     | 即将发布       |
|  macOS   | ⚙️ 敬请期待                                                  | ⚙️ 敬请期待                                     | 即将发布       |

> 目前仅支持 Windows 版本，其他系统将陆续开放。

> 因 Gitee OS 环境限制及 Release 文件上传大小限制，暂不提供 Gitee Release 下载地址。

### 2. 启动服务

安装完成后，启动程序即可开始使用本服务。

> ⚠️ **首次登录**  
> 账号：`admin`  
> 密码：`admin123`

## Docker 部署

### 前置条件

- 已安装 [Docker](https://docs.docker.com/get-docker/)（版本 20.10+）
- 已安装 [Docker Compose](https://docs.docker.com/compose/install/)（版本 2.0+）

### 方式一：在线部署（推荐）

从 GitHub / Gitee 自动拉取源码并构建镜像：

```shell
docker-compose -f docker/docker-compose.yml up -d --build
```

**支持的构建参数：**

| 参数     | 说明         | 默认值   | 示例               |
| -------- | ------------ | -------- | ------------------ |
| `GIT`    | 代码仓库源   | `github` | `github` / `gitee` |
| `TAG`    | 指定版本标签 | 最新 tag | `v1.0.6`           |
| `BRANCH` | 指定分支     | 默认分支 | `main` / `dev`     |

**版本选择优先级**：指定 TAG > 指定 BRANCH > 自动获取最新 tag > 默认分支

**指定参数示例：**

```shell
# 使用 Gitee 源（国内推荐，速度更快）
GIT=gitee docker-compose -f docker/docker-compose.yml up -d --build

# 指定版本标签
TAG=v1.0.6 docker-compose -f docker/docker-compose.yml up -d --build

# 指定分支 + Gitee 源
GIT=gitee BRANCH=dev docker-compose -f docker/docker-compose.yml up -d --build
```

### 方式二：本地构建

使用本地已有的源码直接构建，适合开发者或已克隆仓库的用户：

```shell
# 先克隆项目（如已有则跳过）
git clone https://github.com/HBAI-Ltd/Toonflow-app.git
cd Toonflow-app

# 使用本地源码构建
docker-compose -f docker/docker-compose.local.yml up -d --build
```

### 服务端口说明

| 端口    | 用途           | 在线部署映射  | 本地构建映射  |
| ------- | -------------- | ------------- | ------------- |
| `80`    | Nginx 前端页面 | 随机端口      | `8080:80`     |
| `60000` | 后端 API 服务  | `60000:60000` | `60000:60000` |

### 数据持久化

默认日志目录会挂载到宿主机 `./logs` 目录。如需持久化上传文件或数据库，可在 `docker-compose.yml` 中添加 volumes：

```yaml
volumes:
  - ./logs:/var/log
  - ./uploads:/app/uploads # 持久化上传文件
  - ./data:/app/data # 持久化数据库（如有）
```

### 常用操作命令

```shell
# 查看容器状态
docker-compose -f docker/docker-compose.yml ps

# 查看实时日志
docker-compose -f docker/docker-compose.yml logs -f

# 停止服务
docker-compose -