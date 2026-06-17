# WebHomeTV

WebHomeTV 是基于 FongMi / CatVod 生态二次开发的 Android 影音应用,保留原有点播、直播、Spider、解析、投屏、本地 HTTP 服务等能力,并重点增强了 **WebHome 自定义首页**、**App Native SDK**、**管理页面**、**WebHome 扩展**、**登录态学习/同步**、**网盘链接检测**、**站点健康排序**、**观影记录同步** 和 **Nostr/TMDB 推荐首页**。

项目的核心目标不是替换 CSP/Spider 体系,而是让 CSP 站点首页变成一个真正可开发的网页应用:开发者用 HTML/CSS/JavaScript 定制首页,再通过 App 暴露的 Native 能力完成搜索、播放、跨域请求、资源代理、最近观看、网盘检测和状态同步。

### 增强功能

- **网盘检测**:内置网盘分享链接有效性检测,WebHome 和本地 HTTP API 均可调用。
- **站点健康排序**:自动学习站点搜索、详情和播放成功率,搜索与换源优先使用更可用的站点;站点弹窗默认保留用户配置顺序,可在弹窗内单独开启健康排序。
- **管理页面**:在 App 内启动局域网浏览器管理页 `/m`,可管理本机或远端设备文件、登录态、同步目录、站点注入、接口、壳代理、搜索和推送,运行期间通过前台服务保活。
- **一键同步**:在同一局域网设备间同步配置、站源数据(Jar/脚本保存数据)、登录态、WebHome 数据、搜索记录、观看历史、收藏和应用设置,每项可单独勾选。
- **站点注入**:添加自定义 WebHome 或通用 CSP 站点,主列表显示核心摘要和快捷操作,新增/修改在独立表单中维护启用状态、插入位置、首页、搜索和换源行为;顶部“识别”可粘贴单个或多个松散站点 JSON 片段并自动归类追加;WebHome 站点级扩展可直接填写扩展 URL / JSON,也可选择本地 JS/CSS/JSON 自动生成配置。
- **WebHome 扩展**:给真实网页注入用户脚本,主列表显示扩展摘要和状态,新增/修改在独立表单中配置本地文件、远程链接/manifest、直接代码、表单生成或 JSON;匹配范围默认从当前点播配置的 WebHome 站点弹窗多选,也可切换到 CSP key 正则;提供调试工作台用于 Web 预览、Console/Network/Elements 和代码保存预览。
- **观影记录同步**:增强功能中提供独立总览页,包含总开关、本机 API 修改开关、远端同步源和 Webhook 上报。爬虫可通过 `/api/playback/current` 读取当前播放记录,也可在用户开启修改后调用 `/api/playback/progress`、`/api/playback/progress/batch` 或 `/api/playback/progress/delete` 写入/清理本地进度;App 也可从用户配置的远端 API 拉取批量记录合并到本地历史。完整协议见 `webhome-devkit/docs/应用完整开发文档.md` 的“观影记录同步”章节。
- **登录态学习**:用户手动开启后学习 Cookie、Token、接口 Jar 网盘登录文件等登录态路径,待确认项可在管理页查看/编辑,并可参与一键同步。
- **APP 代理**:配置代理地址和域名匹配规则,可按当前站点自动建议代理域名,用于改善特定站点、接口或播放链路的网络访问。
- **调试日志**:本机和局域网日志查看入口,便于排查播放、代理、站源和 WebHome 相关问题。

以上能力集中在设置页的"增强功能"入口,手机端和电视端均为独立设置页。

## 效果演示

https://github.com/user-attachments/assets/7249b787-a720-406c-8365-acaa0995cb6a

演示视频对应的站点配置(Nostr/TMDB 推荐首页):

```json
{
  "key": "Nostr",
  "name": "Nostr推荐",
  "type": 3,
  "api": "csp_Nostr",
  "homePage": "https://www.252035.xyz/xs/tvbox/nostr.html"
}
```

## 文档

完整开发说明见 [**应用完整开发文档.md**](webhome-devkit/docs/应用完整开发文档.md),包含:

- App 配置字段(点播、解析、直播、样式)
- Spider 开发,JS/Python Spider 运行时
- 本地 HTTP 服务端点总览
- WebHome SDK 全部方法的参数和返回值
- 透明背景、电视端遥控器 UX、性能最佳实践
- 网盘检测 API 和站点健康排序
- 观影记录同步、Webhook 上报和爬虫 HTTP API
- 管理页面和局域网 HTTP 能力
- WebHome 扩展脚本开发
- 登录态学习与同步
- PanSou 集成、Nostr 首页实现要点
- 隐藏功能和使用技巧
- Android Intent、DLNA、MediaSession
- CORS、Cookie 和网络策略

WebHome 主页、扩展、模板、示例和 AI skills 统一放在 [webhome-devkit/](webhome-devkit/) （附 [独立CNB仓库](https://cnb.cool/fish2018/ext)）：

- 扩展脚本开发指南见 [webhome-devkit/README.md](webhome-devkit/README.md)。
- 扩展示例见 [webhome-devkit/examples/extensions/](webhome-devkit/examples/extensions/)。
- 主页示例见 [webhome-devkit/examples/homepages/](webhome-devkit/examples/homepages/)。
- 模板见 [webhome-devkit/templates/](webhome-devkit/templates/)。
- AI 编程客户端如何接入和复用 Skills,见 [webhome-devkit/skills/](webhome-devkit/skills/)。


## 二开重点

### 1. CSP 站点支持自定义 WebHome 首页

站点配置新增首页字段,切换到该 CSP 站点时直接显示自定义网页:

```json
{
  "key": "webhome",
  "name": "WebHome",
  "type": 3,
  "api": "csp_Xxx",
  "homePage": "./nostr.html"
}
```

兼容字段:`homePage`、`home_page`、`webHome`、`web_home`。

如果配置文件来自在线地址,`./nostr.html` 会按配置文件 URL 做相对路径解析,方便把配置和首页 HTML 放在同一目录。

### 2. WebHome Native SDK

WebHome 页面会注入 `window.fongmi` 和简写 `window.fm`,网页可以直接调用 App 能力:

| 能力 | 说明 |
| --- | --- |
| `fm.req(url, options)` | 使用 App 内置 OkHttp 请求接口,绕过浏览器 CORS 限制 |
| `fm.res(url, options)` | 生成本地资源网关地址(`/webResource`),给图片、视频、字幕等 DOM 资源使用 |
| `fm.play(url, title, options)` | 播放直链或 `push://` 地址,`options` 可带 `pic` 和 `wallPic` |
| `fm.vod(siteKey, vodId, title, pic, options)` | 打开 App 原生 CSP 详情/播放链路,`options.wallPic` 可指定播放页背景图 |
| `fm.vodInline(payload)` | 从 WebHome 传入临时 VOD,支持多集直链或按集即时解析,打开 App 原生播放页 |
| `fm.preloadArtwork(pic, wallPic)` | 后台预热播放页海报和背景图,不阻塞后续播放跳转 |
| `fm.search(keyword, { direct, pic, wallPic })` | 调用 App 搜索,支持直接进入搜索结果,可把详情页图片带入后续播放 |
| `fm.openLive()` / `fm.openKeep()` / `fm.openSetting()` | 打开 App 原生直播、收藏和设置入口 |
| `fm.history()` | 读取最近观看记录 |
| `fm.stat()` | 获取当前播放状态、进度、时长等信息 |
| `fm.ctrl(action)` | 控制播放、暂停、停止、上一集、下一集等 |
| `fm.pan.check(items)` | 调用内置网盘链接有效性检测,`fm.check(items)` 是短别名 |
| `fm.pan.play({ type, url, password, title, pic, wallPic })` | 播放网盘分享、磁力、电驴、thunder 等需要进入 push 链路的地址,可带播放页图片 |
| `fm.config()` | 获取当前配置和网盘检测开关状态 |
| `fm.site()` | 获取当前站点信息 |
| `fm.device()` | 获取设备信息 |
| `fm.cache` | WebHome 可用的本地缓存(get/set/del) |
| `fm.ext` | 扩展脚本辅助能力(info/log/toast) |
| `fm.ui.setToolbar(visible)` | 控制 App 工具栏显示 |
| `fm.back()` / `fm.reload()` | 处理网页返回和刷新 |

播放页图片语义:`pic` 是海报/播放器默认图,`wallPic` 是播放页背景图。App 不会自动判断横竖屏,WebHome 应把竖版海报放在 `pic`,把横屏剧照/背景图放在 `wallPic`;播放背景只使用 `wallPic`,没有 `wallPic` 时显示 App 默认背景/壁纸,不会再用 `pic` 兜底。`fm.play`、`fm.vod`、`fm.vodInline`、`fm.pan.play` 共用这套语义;`fm.search(keyword, { direct: true, pic, wallPic })` 可把详情页图片带到原生搜索结果后续播放链路。详情页拿到图片后可先调用 `fm.preloadArtwork(pic, wallPic)` 预热原生 Glide 缓存,点击继续观看、搜索播放或播放时仍应直接调用对应入口,不要在点击后等待预热。

SDK 相关事件:

- `fmsdk`:SDK 注入完成,页面早期脚本应等待该事件后再调用 `fm.*`。
- `fmresume`:App 从后台或锁屏恢复,detail 携带暂停时长,可用于补偿刷新数据。
- `fmurlchange`:History API 路由变化。
- `fmviewport`:WebView 尺寸变化,同时更新 `--fm-web-width/--fm-web-height` CSS 变量。

持久化数据建议优先使用 `fm.cache`,不要把