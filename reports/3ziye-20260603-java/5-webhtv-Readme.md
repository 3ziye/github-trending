# WebHomeTV

WebHomeTV 是基于 FongMi / CatVod 生态二次开发的 Android 影音应用，保留原有点播、直播、Spider、解析、投屏、本地 HTTP 服务等能力，并重点增强了 **WebHome 自定义首页**、**App Native SDK**、**网盘链接检测** 和 **Nostr/TMDB 推荐首页**。

这个项目的核心目标不是替换 CSP/Spider 体系，而是让 CSP 站点首页可以变成一个真正可开发的网页应用：开发者可以用 HTML/CSS/JavaScript 定制首页，再通过 App 暴露的 Native 能力完成搜索、播放、跨域请求、资源代理、最近观看、网盘检测和状态同步。

### 增强功能

- **网盘检测**：对网盘相关能力进行可用性检测，帮助确认当前环境是否支持网盘播放或解析。
- **一键同步**：支持在同一局域网设备间同步配置、站源数据、WebHome 数据、搜索记录、观看历史、收藏和应用设置。
- **站点注入**：支持添加自定义 WebHome 或通用 CSP 站点，并可配置启用状态、插入位置、首页、搜索和换源等行为。
- **APP代理**：支持配置代理地址和域名匹配规则，用于改善特定站点、接口或播放链路的网络访问。
- **调试日志**：提供本机和局域网日志查看入口，便于排查播放、代理、站源和 WebHome 相关问题。

## 效果演示

https://github.com/user-attachments/assets/7249b787-a720-406c-8365-acaa0995cb6a

```
{
  "key": "Nostr",
  "name": "Nostr推荐",
  "type": 3,
  "api": "csp_Nostr",
  "homePage": "https://www.252035.xyz/xs/tvbox/nostr.html"
}
```

## 文档

完整开发说明见：

[**应用完整开发文档.md**](docs/应用完整开发文档.md)


这份文档包含：

- App 配置字段
- Spider 开发
- JS/Python Spider 运行时
- 本地 HTTP 服务
- WebHome SDK 参数和返回值
- 透明背景实现建议
- 网盘检测 API
- PanSou 集成建议
- Nostr 首页实现要点
- 隐藏功能和使用技巧
- Android Intent、DLNA、MediaSession
- CORS、Cookie 和网络策略

## 二开重点

### 1. CSP 站点支持自定义 WebHome 首页

站点配置新增首页字段，切换到该 CSP 站点时可以直接显示自定义网页：

```json
{
  "key": "webhome",
  "name": "WebHome",
  "type": 3,
  "api": "csp_Xxx",
  "homePage": "./nostr.html"
}
```

兼容字段：

- `homePage`
- `home_page`
- `webHome`
- `web_home`

如果配置文件来自在线地址，`./nostr.html` 会按配置文件 URL 做相对路径解析，方便把配置和首页 HTML 放在同一目录。

### 2. WebHome Native SDK

WebHome 页面会注入 `window.fongmi` 和简写 `window.fm`，网页可以直接调用 App 能力。

常用能力包括：

| 能力 | 说明 |
| --- | --- |
| `fm.req(url, options)` | 使用 App 内置 OkHttp 请求接口，绕过浏览器 CORS 限制 |
| `fm.res(url, options)` | 生成本地资源网关地址，给图片、视频、字幕等 DOM 资源使用 |
| `fm.play(url, title, options)` | 播放直链或 `push://` 地址 |
| `fm.vod(siteKey, vodId, title, pic)` | 打开 App 原生 CSP 详情/播放链路 |
| `fm.search(keyword, { direct })` | 调用 App 搜索，支持直接进入搜索结果 |
| `fm.history()` | 读取最近观看记录 |
| `fm.stat()` | 获取当前播放状态、进度、时长等信息 |
| `fm.ctrl(action)` | 控制播放、暂停、停止、上一集、下一集等 |
| `fm.pan.check(items)` | 调用内置网盘链接有效性检测，`fm.check(items)` 是短别名 |
| `fm.pan.play({ type, url, password, title })` | 播放网盘分享、磁力、电驴、thunder 等需要进入 push 链路的地址 |
| `fm.config()` | 获取当前配置和网盘检测开关状态 |
| `fm.site()` | 获取当前站点信息 |
| `fm.device()` | 获取设备信息 |
| `fm.cache` | 提供 WebHome 可用的本地缓存能力 |
| `fm.back()` / `fm.reload()` | 处理网页返回和刷新 |

这套 SDK 的设计目标是让 WebHome 开发者少依赖浏览器私有行为，尽量通过 App 的 Native 能力完成网络、播放和状态管理。

持久化数据建议优先使用 `fm.cache`，不要把账号、页面配置、同步身份等关键数据只放在 `localStorage`。`localStorage` 仍由 Android WebView 提供，并会按页面 origin 保存；但 App 注入 `window.fm` 的时机在页面加载完成后，页面早期脚本应等待 `fmsdk` 事件后再读写 `fm.cache`，或在检测到 `window.fongmiBridge` 但 `window.fm` 尚未就绪时短暂等待，避免误写到浏览器预览 fallback。

### 3. CORS 和资源加载增强

普通网页 `fetch()` 会受浏览器 CORS 限制。WebHomeTV 提供两种内置能力：

- `fm.req()`：用于接口请求，返回 JSON、文本、二进制等数据。
- `fm.res()` / `/webResource`：用于图片、视频、字幕、CSS 背景等资源加载。

这可以处理常见跨域、Header、Cookie、资源防盗链等问题。WebHome 页面不需要要求用户安装浏览器插件或关闭系统 WebView 的安全策略。

### 4. 透明背景 WebHome

App WebView 已支持透明背景，WebHome 页面可以让 App 壁纸透出，适合做沉浸式影视首页。

开发时建议：

- `html`、`body` 和主容器保持透明。
- 卡片、按钮、输入框、Tab、弹层使用半透明中性背景。
- 详情页、剧情页等全屏浮层打开时隐藏底层页面，避免多层内容叠在一起。
- 电脑浏览器调试可以保留兜底背景，App 内使用透明背景。

### 5. WebHome 路由、返回、刷新和恢复

WebHome 支持多层网页状态：

- 使用 History API 管理详情页、搜索页、弹层等路由。
- App 返回键会优先让网页内部回退，再退出 WebHome。
- `fm.reload()` 可以刷新当前 WebHome，而不要求用户重启 App。
- App 从后台或锁屏恢复时会派发 `fmresume` 事件，网页可以保留当前页面状态并补偿刷新数据。
- 正常冷启动应默认回到 WebHome 主页；详情页、弹层等 UI 快照只建议用于后台恢复或 App 明确带 `_fm_restore=1` 的 WebView 进程恢复场景。

电视端 WebHome 要按遥控器模型单独设计焦点：默认焦点不要放在文本框；搜索建议、状态面板、网盘结果列表等打开后要限制方向键在当前区域内；文本框默认 `readonly`，只有 OK/点击后进入编辑态；动态列表刷新要恢复原焦点和滚动位置。完整经验见 [应用完整开发文档.md](docs/应用完整开发文档.md) 的“电视端遥控器 UX 最佳实践”。

### 6. 内置网盘链接检测和播放

设置页新增“增强功能”入口，网盘检测开关放在增强功能页中，默认开启。开启后，WebHome 或自定义工具可以调用 App 内置检测能力。

WebHome SDK：

```js
const config = await fm.config();
if (config.driveCheck) {
  const result = await fm.pan.check([
    { type: "aliyun", url: "https://www.aliyundrive.com/s/xxx" },
    { type: "quark", url: "https://pan.quark.cn/s/xxx" }
  ]);
}
```

本地 HTTP API：

```http
POST http://127.0.0.1:{port}/pan/check
Content-Type: application/json

{
  "items": [
    { "type": "quark", "url": "https://pan.quark.cn/s/xxx" }
  ]
}
```

检测接口支持批量提交，内部每批最多 10 条并发检测，超过 10 条会自动分批处理。WebHome 开发时建议只检测用户当前可见范围内的资源，并且只检测 App 支持的网盘类型，避免无意义请求和界面跳动。

`fm.pan.play({ type, url, password, title })` 是 WebHome 的网盘播放语义入口，当前内部复用 App 已有的 `push_agent/pvideo` 播放链路。因为底层进入 `SiteApi.PUSH`，磁力、电驴、thunder、jianpian 等地址也可以走这个入口。它的性能和直接推送 `push://` 基本一致，但对 WebHome 开发者更清晰，也方便后续 App 内部调整播放策略。`password` 参数会保留在 API 形态中，当前播放链路主要依赖 App/JAR/pvideo 自身处理。

### 6.1 调试日志

调试日志入口也在“增强功能”页中，默认关闭。开启后，App 会记录 WebHome SDK 调用、`fm.req`/资源网关、`pan.check`、`pan.play`、本地 HTTP 服务、爬虫请求、push/pvideo 和播放状态等链路日志。

行为说明：

- 关闭调试日志时不弹 toast，并自动清空当前进程内日志。
- 日志保存在当前 App 进程内，不限制 2000 条；关闭或进程结束后不保留。
- 开启后会打开 `/debug/logs` 页面，可刷新、下载、清空，也可以通过同局域网地址查看。

### 7. PanSou 网盘搜索集成示例

`demo/nostr.html` 的详情页集成了 PanSou 类搜索能力，支持：

- 自定义盘搜服务地址。
- 账号密码认证。
- 自定义 TG 频道。
- 按网盘类型分 Tab 展示。
- 对支持的网盘类型调用 App 内置检测。
- 只检测可见范围内的结果。
- 检测结果用状态圆点表达。
- 点击资源后调用 `fm.pan.play({ type, url, password, title })` 交给 App 播放