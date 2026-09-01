# opencode2api

`opencode2api` 是一个使用 Go 编写的 OpenCode Zen / Zen Go 协议代理。它对外提供标准 OpenAI 与 Anthropic API，并自动添加 OpenCode 客户端请求头。

主要功能：

- 支持 OpenAI Chat Completions、Responses 和 Models API
- 支持 Anthropic Messages API
- 支持普通响应和 SSE 流式响应
- 支持文本、图片、thinking/reasoning、工具定义、工具调用和工具结果转换
- 分离配置 Zen key 池与 Zen Go key 池
- 支持无需上游 key 的 Zen 匿名模式，免费模型先走匿名通道，失败后按 `prefer` 顺序回退 Zen/Go key
- 按配置周期同步 Zen/Go `/v1/models`，并从 OpenCode `models.opencode.ai/api.json` 自动同步每个 Tier 的原生协议与不支持模型；不把模型 ID 硬编码在程序中
- 每 24 小时从 models.dev 更新 OpenCode 成本与弃用信息；models.dev 零成本或名称含 `free` 任一条件即可判定免费
- 模型同时存在于两个上游时按 `prefer` 配置排列 Go/Zen key 的首选与回退顺序（默认 Go）
- 支持直连、HTTP、HTTPS、SOCKS5 和 SOCKS5H 代理
- 支持从文本文件读取代理池，并与配置内的代理合并、去重
- `config.json` 支持 `//` 和 `/* ... */` 注释
- 将 key 自动均衡绑定到代理，保持连接亲和性
- 使用稳定会话哈希保持同一会话的 key/proxy 亲和性，并在节点故障时自动回退
- 代理失败后自动迁移绑定，key 失败后进行短时冷却
- 根据真实上游流量识别代理故障，并每 15 分钟通过 Cloudflare trace 并行复查异常代理
- 为不同会话生成不同的 OpenCode 会话 ID，并支持 `x-opencode-session`、`x-session-id` 和 `conversation-id` 显式指定会话
- 内置独立端口 Field Manual WebUI，可管理配置、查看 Token/上游指标、诊断路由、运行三协议 Playground 与订阅实时日志
- WebUI 使用账号密码、服务端 session、HttpOnly Cookie、CSRF 与登录限速保护
- WebUI 保存后原子写入配置并热切换 Gateway；无效配置不会影响当前流量
- stdout 输出结构化 JSON 日志；请求、Token、上游尝试与最近一小时滚动指标仅保存在进程内存中

## API 路径

| 方法 | 路径 | 协议 |
| --- | --- | --- |
| `GET` | `/v1/models` | OpenAI 模型列表 |
| `POST` | `/v1/chat/completions` | OpenAI Chat Completions |
| `POST` | `/v1/responses` | OpenAI Responses |
| `POST` | `/v1/messages` | Anthropic Messages |
| `GET` | `/healthz` | 健康检查 |

`/healthz` 无需 API key，返回服务版本以及模型目录、Zen/Go key、匿名开关和代理池的汇总状态，不会暴露 key 或代理地址。模型目录尚未完成首次刷新、已经过期、没有可暴露模型或没有健康代理时返回 HTTP `503`；其余情况返回 `200`。

模型目录的过期阈值为 `models.refresh_seconds` 的两倍，且不低于 60 秒。刚启动时短暂返回 `503 starting` 属于正常现象，模型列表首次刷新成功后会变为 `200 ok`。

健康检查不会计入请求指标。它也不会触发 models.dev 刷新或写入任何监控记录。

## WebUI

示例配置会在独立的 `8081` 端口启动管理界面：

```text
http://服务器地址:8081
```

首次账号为 `admin`，密码来自 `webui.password`。服务第一次成功启动时会使用 Argon2id 将密码转换为带盐哈希，写入 `webui.password_hash`，并从配置中删除明文密码。请在首次登录后立即修改示例密码。

Field Manual WebUI 包含运行桌面、六步首次运行检查、接入手册、Token 用量、三协议 Playground、路由诊断、配置、事件日志和账号安全页面。接入手册会生成 Chat、Responses、Anthropic、Python 和 JavaScript 示例，但始终使用 `YOUR_API_KEY` 占位符，不把真实 Server Key 写入页面。

Token 页面展示用量覆盖率、每分钟趋势、模型排行与 Zen/Go Tier 分布。诊断页展示 models.dev 状态、模型原生协议与匿名判断来源、Key/代理状态、逐次上游尝试以及最近一次 Playground 追踪；实时日志通过 SSE 推送。所有动态管理数据都以 DOM 文本节点渲染。

监控、上游尝试、最近 Playground 结果和日志仅保存在内存。**进程重启会清空全部监控与诊断历史，包括 lifetime 累计。** stdout 日志仍可由 Docker 或日志平台收集；models.dev 价格快取是独立的磁盘兼容资料，不属于监控历史。

### 监控字段

登录 WebUI 后，`GET /api/monitor` 返回以下顶层字段；该管理 API 只在 `webui.listen` 上提供，并受 Session 保护：

| 字段 | 内容 |
| --- | --- |
| `version` | 当前程序版本。 |
| `metrics` | 原有请求统计：进程启动时间、活跃请求/流、lifetime 与最近一小时成功率/延迟、端点/模型/Tier/状态码聚合，以及 60 个每分钟序列点。 |
| `usage` | Token 的 `lifetime` 与 `last_hour` 统计。包含 `requests`、`reported`、`coverage`、总 Token 和按模型/Tier 聚合。 |
| `upstream` | 上游请求级路由 `requests`、尝试级 `lifetime`、`last_hour` 与 `recent`。按 Tier、匿名/Key 通道、Key 尾码聚合。 |
| `resources` | 模型目录、Key 冷却、脱敏代理节点、匿名开关和 models.dev metadata 状态。 |

`usage.*.tokens` 与模型/Tier 项均包含 `input_tokens`、`output_tokens`、`cached_tokens`、`reasoning_tokens`、`total_tokens`。其中 `input_tokens` 统一表示包含缓存读写的总输入，`cached_tokens` 单独表示缓存读取量。`metrics.series` 的每分钟点也包含这些 Token 字段和 `usage_reported`。普通 JSON、同协议 SSE 与跨协议 SSE 响应都会解析上游 usage；`coverage` 是收到 usage 的推理请求数除以已建立上游路由的推理请求数。上游未提供 usage 时不会估算 Token。

每个 `upstream.requests` 项对应一个已完成的推理请求，包含最终实际使用的 Tier、通道、Key 尾码（或 `anonymous`）、尝试次数、HTTP 状态、耗时、成功标记和结果分类。每个 `upstream.recent` 项则对应一次上游尝试，包含时间、Request ID、模型、Tier、尝试序号、匿名标记、通道、Key 尾码、`proxy_node`、HTTP 状态、耗时、成功标记和结果分类。真实 Key 在日志和 WebUI 中只显示最后 5 个字符；配置接口的内部 secret ID 仍使用 SHA-256 稳定指纹。代理 URL 的认证信息会被移除，字段名称明确为代理节点而非出口 IP。

lifetime 从当前进程启动开始；last hour 使用 60 个一分钟 Bucket。管理响应最多返回最近 500 个请求路由和 500 次上游尝试，WebUI 默认各显示最后 100 条。数据不会写入配置、metadata 快取或其他数据库。

### Playground 与诊断 API

以下接口受管理 Session 保护；POST 还要求当前 CSRF Token，并按客户端每分钟最多 12 次限制：

| 方法 | 路径 | 用途 |
| --- | --- | --- |
| `GET` | `/api/debug/models` | 模型路由、原生协议、协议来源、Zen/Go 可用性、匿名资格/来源、成本与 metadata 状态。 |
| `POST` | `/api/debug/inference` | 通过真实 Gateway 发起 Chat、Responses 或 Anthropic 非流式诊断请求。 |

请求格式：

```json
{
  "protocol": "chat",
  "request": {
    "model": "example-model",
    "messages": [{"role": "user", "content": "Hello"}]
  }
}
```

`protocol` 可为 `chat`、`responses` 或 `anthropic`。服务端无条件把内层 `stream` 改为 `false`。诊断结果统一包含 `ok`、真实 `http_status`、`duration_ms`、`request_id`、`route` 和原始协议 `response`。一旦诊断调用已执行，管理接口本身返回 HTTP `200`，即使上游结果是 4xx/5xx；因此错误正文、路由和 Request ID 仍可一起查看。外层请求格式、Session、CSRF 或限速错误仍使用相应管理 HTTP 状态。

诊断响应不会包含本地 Server Key、上游 Key、Cookie、密码、Authorization 或代理凭据；响应中同名敏感字段及已配置敏感值会在返回浏览器前清除。最近一次结果只保存在当前管理进程内。

## 编译

需要 Go 1.24 或更高版本。

```bash
go build -o opencode2api ./
```

## 下载

预编译的 Windows、Linux 和 macOS 可执行文件可从 [GitHub Releases](https://github.com/jasonxu114514/opencode2api/releases) 下载。

## GHCR / Docker Compose 部署

正式镜像发布在 `ghcr.io/jasonxu114514/opencode2api`


```bash
git clone https://github.com/jasonxu114514/opencode2api.git
cd opencode2api
cp config.example.json config.json
# 编辑 server_keys、zen_keys/go_keys，并修改 webui.pas