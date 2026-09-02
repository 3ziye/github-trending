# JT Vehicle Platform

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![JDK](https://img.shields.io/badge/JDK-25-orange.svg)](https://adoptium.net/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-4.1-brightgreen.svg)](https://spring.io/projects/spring-boot)
[![Vue](https://img.shields.io/badge/Vue-3-42b883.svg)](https://vuejs.org/)

[English](README.en.md)

**开箱即用的部标车联网平台**。终端按 JT/T 808 接入，视频按 JT/T 1078 推流，
浏览器里直接看实时地图、实时视频和历史轨迹——**不依赖 Redis、消息队列或任何外部业务系统**。

> 一条命令跑起全栈：
> ```bash
> docker compose up -d --build     # 然后打开 http://localhost
> ```

### AI 助手：一句话运维，答案直接画出来

用中文问平台上的任何数据，也可以让它帮你建档、建围栏、处置告警。
**答案不只是文字——位置、路线、趋势会直接渲染在对话里**，输入框始终可用，可以边看边追问。

问「这台车在哪」，除了中文地址，地图直接长在回答下面：

![AI 对话内嵌实时位置](docs/images/ai-live-map.png)

问「看看昨天的轨迹」，折线、起终点、里程与最高速一并给出：

![AI 对话内嵌行驶轨迹](docs/images/ai-track-map.png)

要看画面时给一张卡片而不是直接开流——**开流会向路上那台车下发指令，这种事由人点一下**。
点开后在右侧面板播放，对话区照常可以继续输入：

![AI 对话中的实时视频](docs/images/ai-live-video.png)

改动数据一律走确认卡片：AI 只能**提议**，执行由前端用当前用户自己的令牌调既有接口完成，
因此权限、数据范围与审计全部沿用既有通道，AI 侧没有任何特权。

### 轨迹回放

按车辆和时间段查询历史轨迹，地图上绘制行驶路线并支持 1x–16x 倍速回放，
同时给出里程、最高速、平均速与轨迹点数。设备上报的是 WGS-84 坐标，入库时转换为
GCJ-02 后再渲染，因此不会出现整体偏移。

![轨迹回放](docs/images/track-playback.png)

### 运营看板

聚合建档车辆、在线/行驶、静止/离线、未建档在线、未关闭告警与当日里程，
并展示近七日运营趋势、告警分级分布和最近告警动态。

![运营看板](docs/images/dashboard.png)

## 它解决什么问题

做部标车辆监控，通常要自己啃 JT/T 808 的分包与转义、1078 的裸流重组、终端 ID 与手机号的映射、
浏览器端的 H.264 解码……这些坑本项目都已经趟过并且有对应的代码和文档。

拿到手就是一套能跑的完整链路：

```
车载终端 ──JT/T 808/1078──▶ 协议网关 ──HTTP 投递──▶ 业务后端 ──REST/WS──▶ 控制台前端
                              │                      (SQLite)                 │
                              └────────── 裸流 WebSocket ──────────────────────┘
```

| 模块 | 职责 | 默认端口 |
|---|---|---|
| `jt-platform` | JT/T 808 信令、JT/T 1078 媒体、开流调度与事件投递 | `7100`、`7101`、`7810-7815`、`8100`、`8109` |
| `jt-console` | 认证、车辆/轨迹/状态、运营统计、告警/围栏、实时广播与开流代理 | `8300` |
| `jt-console-ui` | 运营看板、实时监控、告警处置、电子围栏、轨迹回放与视频播放 | `9527`（开发）/ `443`（部署） |
| `packages/jt-player` | 零运行时依赖的浏览器裸流播放器 SDK（含 Vue3、React 适配） | — |
| `jt-terminal-simulator` | 用电脑摄像头模拟 808 终端与 1078 推流，无真车也能验证 | 桌面客户端 |

技术基线：JDK 25 · Spring Boot 4.1 · Netty · Vue 3 · SQLite。

## 核心能力

- JT/T 808 2011、2013、2019 终端接入，兼容 JT/T 1078、苏标主动安全相关消息。
- H.264、H.265、AAC、G.711A 媒体接入，按主码流、子码流、历史回放和对讲分端口监听。
- 两步式开流与一次性媒体 token，客户端直连被调度的媒体节点。
- 裸流 WebSocket 播放、独占或混音对讲、裸流分片录像、检索、回放和离线 MP4 导出；
  控制台提供录像检索与回放页面。
- API 与 RocketMQ 可独立或同时启用的协议消息投递。
- 车队运营看板聚合建档、在线、行驶、静止、未处理告警和当日里程，并展示近七日趋势、告警分布和最近动态。
- JT/T 808 协议告警和围栏告警持久化、去重、组合筛选、分级及确认/关闭处置。
- GCJ-02 电子围栏（圆形/矩形/多边形/路线）创建、启停、车辆分配、进出边界与围栏内限速判定。
- 自定义告警规则引擎：超速阈值、怠速超时、疲劳驾驶时长，按位置流持续判定并去重。
- 运营报表：按车辆与时间范围聚合里程、活跃天数与告警，支持 CSV 导出。
- OTA 升级包管理：上传、版本管理、按车下发（8108）与升级包查询。
- 车辆运营详情聚合档案、最新状态、当日/近七日指标和最近告警，并提供监控、轨迹和视频快捷入口。
- 设备日志中心：上行报文、下行指令、上下线三类记录统一入库，留存原始帧 hex 与解析 JSON，
  按设备与时间段检索，页面可展开逐条比对，独立日志库与业务库物理隔离。
- 终端管理：连接过网关的终端自动入册，展示终端自报的编号、制造商、型号与车牌，
  标注是否已建档，未建档终端可一键转为车辆档案。
- AI 助手用自然语言查询与运维平台：流式对话、跨会话留存，改动数据一律经确认卡片由用户执行。
- AI 回答内嵌实时位置、行驶轨迹、统计图表与实时视频；有副作用的视图（开流）必须用户显式点击。
- 同一个可执行 JAR 支持 `standalone` 单进程和 `api`、`signal`、`media` 分进程部署。

## 快速开始（Docker，推荐）

只需要装了 Docker，不用准备 JDK、Maven 和 Node：

```bash
git clone https://github.com/liuxiaoyan199701-coder/jt-vehicle-platform.git
cd jt-vehicle-platform
docker compose up -d --build
```

首次构建要下载 Maven 与 npm 依赖，耗时较长；之后会命中缓存。启动完成后：

```bash
# 取管理员账号（本地模式下每次启动随机生成，不使用默认口令）
docker compose logs console | grep "jt-console] 用户名\|jt-console] 密码"
```

浏览器打开 **http://localhost** 登录即可。

终端接入地址是宿主机的 `7100/TCP`（或 `7101/UDP`），视频推流端口 `7811-7814`。
没有真实车机时，用 [终端推流模拟器](docs/terminal-simulator.md) 就能跑通整条链路。

> **必须用 `localhost` 访问**：视频播放依赖浏览器的 WebCodecs，而它只在安全上下文中可用。
> `http://localhost` 属于安全上下文，换成 IP 或域名访问就必须配 HTTPS，否则视频无法解码。
>
> 接入**真实车机**时还要设置宿主机可达地址，否则终端收到开流指令也连不上：
> ```bash
> MEDIA_REACHABLE_ADDRESS=192.168.1.10 docker compose up -d
> ```
>
> 这套编排面向本地体验：设备鉴权为 `allow-all`、开流鉴权关闭、走明文 HTTP。
> 生产部署请用 `deploy/` 下的脚本，它带证书校验、蓝绿发布与失败自动回滚。

## 从源码启动

### 1. 准备环境

- JDK 25 或更高版本，确认 `java -version` 指向正确的 JDK。
- Maven 3.9 或更高版本。
- 空闲端口：`7100/TCP`、`7101/UDP`、`7810-7815/TCP`、`8100/TCP`、`8109/TCP`。

网关本身不依赖 `ffmpeg` 完成启动、终端接入、录像、检索或裸流回放；只有离线 MP4 导出需要它。
Windows 摄像头推流模拟器需要用户另外安装带 `dshow`、`libx264` 和 `pcm_alaw` 的 FFmpeg，详见
[终端推流模拟器](docs/terminal-simulator.md)。仓库和便携包都不会捆绑 `ffmpeg.exe`。

### 2. 构建

```bash
cd jt-platform
mvn -B -ntp clean package
```

构建产物为：

```text
jt-boot-all/target/jt-boot-all-0.1.0-SNAPSHOT.jar
```

### 3. 启动

```bash
java -jar jt-boot-all/target/jt-boot-all-0.1.0-SNAPSHOT.jar
```

未指定 profile 或角色时默认以 `standalone` 启动，信令、媒体与 API 位于同一进程。

### 4. 检查健康状态

```bash
curl --fail http://127.0.0.1:8109/actuator/health
curl --fail http://127.0.0.1:7810/health
```

两个请求都应返回包含 `"status":"UP"` 的 JSON。此时 JT/T 808 终端可接入 `7100/TCP` 或
`7101/UDP`，业务侧 REST API 位于 `8100/TCP`。

## 安全启动业务控制台

本地开发允许控制台在未配置管理员哈希时生成本次进程有效的一次性密码，并只在启动终端显示。
投递密钥必须由控制台和网关共同使用，不能复用管理员密码或浏览器 token。先在两个启动终端中设置
同一个随机值，例如自行生成至少 32 字节随机密钥后设置：

```powershell
$env:JT_CONSOLE_INGEST_KEY = "<same-random-ingest-key>"
```

启动控制台后端：

```powershell
$env:JAVA_HOME = "D:\path\to\jdk