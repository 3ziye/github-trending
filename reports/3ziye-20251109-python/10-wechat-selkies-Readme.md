# WeChat Selkies

[![GitHub Stars](https://img.shields.io/github/stars/nickrunning/wechat-selkies?style=flat-square&logo=github&color=yellow)](https://github.com/nickrunning/wechat-selkies/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/nickrunning/wechat-selkies?style=flat-square&logo=github&color=blue)](https://github.com/nickrunning/wechat-selkies/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/nickrunning/wechat-selkies?style=flat-square&logo=github&color=red)](https://github.com/nickrunning/wechat-selkies/issues)
[![GitHub License](https://img.shields.io/github/license/nickrunning/wechat-selkies?style=flat-square&color=green)](https://github.com/nickrunning/wechat-selkies/blob/master/LICENSE)
[![Docker Pulls](https://img.shields.io/docker/pulls/nickrunning/wechat-selkies?style=flat-square&logo=docker&color=blue)](https://hub.docker.com/r/nickrunning/wechat-selkies)
[![Docker Image Size](https://img.shields.io/docker/image-size/nickrunning/wechat-selkies?style=flat-square&logo=docker&color=orange)](https://hub.docker.com/r/nickrunning/wechat-selkies)
[![GitHub Release](https://img.shields.io/github/v/release/nickrunning/wechat-selkies?style=flat-square&logo=github&include_prereleases)](https://github.com/nickrunning/wechat-selkies/releases)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/nickrunning/wechat-selkies/docker.yml?style=flat-square&logo=github-actions&label=build)](https://github.com/nickrunning/wechat-selkies/actions)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/nickrunning/wechat-selkies?style=flat-square&logo=github&color=purple)](https://github.com/nickrunning/wechat-selkies/commits)

中文 | [English](README_en.md)

基于 Docker 的微信/QQ Linux 客户端，使用 Selkies WebRTC 技术提供浏览器访问支持。

## 项目简介

本项目将官方微信/QQ Linux 客户端封装在 Docker 容器中，通过 Selkies 技术实现在浏览器中直接使用微信/QQ，无需在本地安装微信/QQ 客户端。适用于服务器部署、远程办公等场景。

## 升级注意事项

> 如果升级后部分功能缺失，请先清空本地挂载目录下的openbox目录(如`./config/.config/openbox`)。

## 功能特性

- 🌐 **浏览器访问**：通过 Web 浏览器直接使用微信，无需本地安装
- 🐳 **Docker化部署**：简单的容器化部署，环境隔离
- 🔒 **数据持久化**：支持配置和聊天记录持久化存储
- 🎨 **中文支持**：完整的中文字体和本地化支持，支持本地中文输入法
- 🖼️ **图片复制**：支持通过侧边栏面板开启图片复制
- 📁 **文件传输**：支持通过侧边栏面板进行文件传输
- 🖥️ **AMD64和ARM64架构支持**：兼容主流CPU架构
- 🔧 **硬件加速**：可选的 GPU 硬件加速支持
- 🪟 **窗口切换器**：左上角增加切换悬浮窗，方便切换到后台窗口，为后续添加其它功能做基础
- 🤖 **自动启动**：可配置自动启动微信和QQ客户端（可选）

## 截图展示
![微信截图](./docs/images/wechat-selkies-1.jpg)
![QQ截图](./docs/images/wechat-selkies-2.jpg)

## 快速开始

### 环境要求

- Docker
- Docker Compose
- 支持WebRTC的现代浏览器（Chrome、Firefox、Safari等）

### 快速部署

1. **直接使用已构建的镜像进行快速部署**

GitHub Container Registry镜像：
```bash
docker run -it -p 3001:3001 -v ./config:/config --device /dev/dri:/dev/dri ghcr.io/nickrunning/wechat-selkies:latest
```

Docker Hub镜像：
```bash
docker run -it -p 3001:3001 -v ./config:/config --device /dev/dri:/dev/dri nickrunning/wechat-selkies:latest
```

2. **访问微信**
   
   在浏览器中访问：`https://localhost:3001` 或 `https://<服务器IP>:3001`
   > **注意：** 映射3000端口用于HTTP访问，3001端口用于HTTPS访问，建议使用HTTPS。

### docker-compose 部署
1. **创建项目目录并进入**
   ```bash
   mkdir wechat-selkies
   cd wechat-selkies
   ```
2. **创建 docker-compose.yml 文件**
   ```yaml
    services:
      wechat-selkies:
        image: nickrunning/wechat-selkies:latest    # or ghcr.io/nickrunning/wechat-selkies:latest
        container_name: wechat-selkies
        ports:
          - "3000:3000"       # http port
          - "3001:3001"       # https port
        restart: unless-stopped
        volumes:
          - ./config:/config
        devices:
          - /dev/dri:/dev/dri # optional, for hardware acceleration
        environment:
          - PUID=1000                    # user ID
          - PGID=100                     # group ID
          - TZ=Asia/Shanghai             # timezone
          - LC_ALL=zh_CN.UTF-8           # locale
          - AUTO_START_WECHAT=true       # default is true
          - AUTO_START_QQ=false          # default is false
          # - CUSTOM_USER=<Your Name>      # recommended to set a custom user name
          # - PASSWORD=<Your Password>     # recommended to set a password for selkies web ui
    ```
3. **启动服务**
   ```bash
   docker-compose up -d
   ```

### 源码部署

1. **克隆项目**
   ```bash
   git clone https://github.com/nickrunning/wechat-selkies.git
   cd wechat-selkies
   ```

2. **启动服务**
   ```bash
   docker-compose up -d
   ```

3. **访问微信**

   在浏览器中访问：`https://localhost:3001` 或 `https://<服务器IP>:3001`

### 配置说明

更多自定义配置请参考 [Selkies Base Images from LinuxServer](https://github.com/linuxserver/docker-baseimage-selkies)。

#### Docker Hub 推送配置

本项目支持同时推送到 GitHub Container Registry 和 Docker Hub。如需启用 Docker Hub 推送功能，请在仓库下添加Environment Secrets和Environment Variables:

**Environment Secrets:**
* DOCKERHUB_USERNAME: 你的 Docker Hub 用户名
* DOCKERHUB_TOKEN: 你的 Docker Hub Access Token
**Environment Variables:**
* ENABLE_DOCKERHUB: 设置为 `true` 来启用 Docker Hub 推送

#### 环境变量配置

在 `docker-compose.yml` 中可以配置以下环境变量：

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| `TITLE` | `WeChat Selkies` |