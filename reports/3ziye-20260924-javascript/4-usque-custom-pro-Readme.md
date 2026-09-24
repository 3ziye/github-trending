# Usque MASQUE Pro v6.17 — 动态地区规则 + 完整策略组

> 基于 Cloudflare WARP / MASQUE 的可视化注册、配置生成与多客户端转换工具。  
> 支持 **Cloudflare Pages + Cloudflare Workers 双部署**，浏览器完成 Usque 注册、原生配置保存、MASQUE 多节点生成、Clash/Mihomo 智能分流、Shadowrocket、sing-box、本地 VLESS 桥接，以及可选的 WARP 出口检测。
>
> # YouTube视频教程 [点击查看](https://youtu.be/eRIjgiVHsbs)
> # v6.17 视频教程 [点击查看](https://youtu.be/GREPEjjRQwc)
---

## 目录

- [项目介绍](#项目介绍)
- [核心功能](#核心功能)
- [项目原理](#项目原理)
- [目录结构](#目录结构)
- [部署方式一：Cloudflare Pages（推荐）](#部署方式一cloudflare-pages推荐)
- [部署方式二：Cloudflare Workers](#部署方式二cloudflare-workers)
- [首次使用教程](#首次使用教程)
- [Clash / Mihomo 使用教程](#clash--mihomo-使用教程)
- [ChatGPT / OpenAI 简单模式](#chatgpt--openai-简单模式)
- [节点数量与 H2 扩展池](#节点数量与-h2-扩展池)
- [其它输出格式](#其它输出格式)
- [WARP 出口国家检测（高级）](#warp-出口国家检测高级)
- [升级项目](#升级项目)
- [常见问题](#常见问题)
- [安全与隐私](#安全与隐私)
- [重要说明](#重要说明)

---

# 项目介绍

**Usque MASQUE Pro v6.7** 是一个面向 Cloudflare WARP / MASQUE 的浏览器可视化工具。

它解决的主要问题是：

```text
手动注册 WARP / MASQUE
        ↓
配置字段复杂
        ↓
不同客户端格式不一致
        ↓
需要手工写 Clash / sing-box / VLESS 配置
```

本项目把整个流程整理成：

```text
打开网页
  ↓
一键注册 Usque / WARP MASQUE
  ↓
自动下载原生 config.json
  ↓
按需要设置 Endpoint / Port / SNI / DNS / 节点数量
  ↓
一键生成客户端配置
  ↓
Clash / Mihomo / Shadowrocket / sing-box / VLESS 本地桥接
```

项目重点面向：

- 第一次接触 Usque / MASQUE 的用户
- 不想手工编辑大量 YAML / JSON 的用户
- 需要批量生成 MASQUE 候选节点的用户
- 需要 Clash / Mihomo 智能分流的用户
- 想把原生 Usque 配置长期保存、以后重复使用的用户

---

# 核心功能

## 1. 一键注册 Usque / WARP MASQUE

浏览器中完成：

- WARP 设备注册
- P-256 MASQUE 密钥生成
- MASQUE 公钥 enroll
- 自动整理原生 Usque `config.json`

注册成功后可以立即下载：

```text
usque-config.json
```

以后只需要重新导入这个文件，不必每次重新注册。

---

## 2. 原生配置作为唯一源文件

项目不会要求你每次重新创建账户。

推荐流程：

```text
第一次：注册 → 保存 config.json
以后：导入 config.json → 修改参数 → 重新生成
```

原生配置通常包含：

```text
private_key
endpoint_v4
endpoint_v6
endpoint_h2_v4
endpoint_h2_v6
endpoint_pub_key
license
id
access_token
ipv4
ipv6
```

> `config.json` 包含私钥与设备凭据，请勿上传到 GitHub、网盘、公开群组或公开网页。

---

## 3. 多节点生成

支持：

```text
13 节点
32 节点
64 节点
100 节点
自定义 1～500 节点
```

生成方式包括：

- 精选 Endpoint + Port
- Endpoint × Port 组合
- 均衡分布
- 全排列
- 稳定打散
- 自动去重
- 自定义附加 Endpoint

---

## 4. QUIC / H3 与 H2

支持：

```text
QUIC / H3
H2 / TCP
```

H2 模式提供扩展地址池，适合生成大量候选节点进行测速筛选。

> 节点数量多不代表每个节点都一定可用。不同网络、地区、运营商对不同入口和端口的可达性会不同。

---

## 5. Clash / Mihomo 智能分流

自动生成：

- MASQUE 节点
- 自动测速 `url-test`
- PROXY 策略组
- AI
- YouTube
- Emby
- TikTok
- Netflix
- Disney+
- Spotify
- GitHub
- Telegram
- Google
- Twitter / X
- Instagram
- Facebook
- Apple
- Microsoft
- Steam
- Xbox
- PlayStation
- Nintendo
- Bilibili
- 国外网站
- 漏网之鱼

并使用 MetaCubeX MRS 规则集进行智能分流。

---

## 6. ChatGPT / OpenAI 简单模式

v6.7 默认推荐：

```text
ChatGPT / OpenAI → DIRECT
其它国外流量     → WARP / MASQUE
```

目的是避免某些共享 WARP 出口被 ChatGPT 拒绝时，整个代理配置都不可用。

网页中可以切换：

```text
DIRECT 直连
WARP · AI 自动选择
WARP · 地区优选
WARP · PROXY
AI 策略组
```

---

## 7. 多格式输出

当前支持：

```text
原生 Usque config.json
Clash / Mihomo
Shadowrocket
sing-box
VLESS 本地桥接
```

---

## 8. WARP 出口检测

高级功能可以通过本机 Mihomo API：

- 逐节点切换 MASQUE 节点
- 检测实际出口 IP
- 检测国家 / 地区 / 城市
- 检测 Cloudflare PoP
- 测试延迟
- 测试 ChatGPT HTTP 可达性
- 输出 JSON / CSV 报告
- 根据国家偏好自动选择候选节点

这个功能默认折叠，新手可以完全不使用。

---

# 项目原理

## 整体架构

### Cloudflare Pages 版

```text
浏览器
  │
  ├─ index.html / app.js / usque-register.js
  │
  ├─ 浏览器本地生成 P-256 私钥
  │
  └─ POST /api/warp/*
          ↓
      Pages _worker.js
          ↓
 Cloudflare WARP 注册 API
```

Pages 中：

```text
静态页面 → Pages 直接提供
/api/*   → _worker.js
```

由 `_routes.json` 控制：

```json
{
  "version": 1,
  "include": ["/api/*"],
  "exclude": []
}
```

这样静态页面不会经过 API Worker。

---

### Cloudflare Workers 版

```text
浏览器
   ↓
Workers Static Assets
   ├─ public/index.html
   ├─ public/app.js
   └─ public/style.css

/api/*
   ↓
src/worker.js
   ↓
Cloudflare WARP 注册 API
```

Workers 版通过：

```text
wrangler.jsonc
```

配置：

```jsonc
"assets": {
  "directory": "./public",
  "binding": "ASSETS",
  "run_worker_first": ["/api/*"]
}
```

因此：

```text
普通静态资源 → Static Assets
/api/*       → Worker
```

---

## 注册原理

### 第一步：创建设备

浏览器生成注册所需随机信息，并请求：

```text
/api/warp/register
```

Worker 只把固定格式请求转发到 Cloudflare WARP 注册接口。

---

### 第二步：浏览器生成 P-256 MASQUE 密钥

MASQUE 私钥使用浏览器 WebCrypto：

```text
ECDSA
P-256 / secp256r1
```

生成。

项目会把私钥转换成 Usque 所需的 SEC1 DER Base64 格式。

关键点：

```text
P-256 私钥在浏览器本地生成
```

Worker enroll 时只需要 MASQUE 公钥。

---

### 第三步：Enroll MASQUE

浏览器请求：

```text
/api/warp/enroll
```

Worker 将 P-256 公钥提交给 WARP API，并获取：

```text
MASQUE endpoint
endpoint public key
interface IPv4 / IPv6
设备信息
```

随后浏览器把这些信息与本地私钥组合成：

```text
usque-config.json
```

---

## MASQUE 多节点原理

这里生成的 13 / 32 / 64 / 100 / 500 个节点，并不是注册 500 个账户。

核心逻辑是：

```text
同一套 Usque / WARP 凭据
          +
不同 Endpoint
          +
不同 Port
          ↓
多个 MASQUE 候选连接
```

例如：

```text
Endpoint A : 443
Endpoint A : 500
Endpoint A : 4500
Endpoint B : 443
Endpoint B : 500
...
```

因此：

- 节点数量 ≠ WARP 账号数量
- 节点数量 ≠ 独立出口数量
- 节点数量 ≠ 每个节点都有独立流量额度

大量候选主要用于：

```text
测速
自动选择
寻找当前网络更稳定的入口组合
```

---

## WARP 入口与出口不是一回事

这是本项目最容易误解的地方。

```text
MASQUE Endpoint
      ↓
Cloudflare 入口
      ↓
Cloudflare 网络
      ↓
WARP 出口 