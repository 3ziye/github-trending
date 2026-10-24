<div align="center">
  <img src="icon.svg" alt="Our Free Model — DeepSeek Harness 免费模型插件" width="120">

# dsh-our-free-model

**简体中文** | [English](README_EN.md)

  <img alt="许可证" src="https://img.shields.io/badge/license-MIT-263146?style=flat-square">
  <img alt="零依赖" src="https://img.shields.io/badge/dependencies-zero-4b6fff?style=flat-square">
  <img alt="无构建步骤" src="https://img.shields.io/badge/build%20step-none-7da1de?style=flat-square">
  <img alt="适配内核" src="https://img.shields.io/badge/dsh-0.1.5--0.1.7--rc.2-2f6f4f?style=flat-square">
  <img alt="状态" src="https://img.shields.io/badge/status-beta-f0a441?style=flat-square">
  <br>
  <a href="https://trendshift.io/repositories/261203"><img alt="GITHUB TRENDING 第 1 名，日榜仓库" src="docs/images/trendshift-daily-laurel-gold.svg" width="250" height="55"></a>
  <a href="https://trendshift.io/weekly?language=JavaScript"><img alt="Trendshift JavaScript 周榜第 1 名（2026-10-05 至 2026-10-11，更新中）" src="docs/images/trendshift-weekly-2026-10-11-first-gold.svg" width="250" height="55"></a>
  <br>
  <sub>Trendshift JavaScript 周榜第 1 · 2026-10-05 至 2026-10-11 · 更新中，截至 2026-10-11</sub>

</div>

<div align="center">

> 你只需在 dsh 里装上这个插件，无需登录、注册、填 API Key 或任何其它操作，
> 就能用上包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。
>
> *All you do is install this plugin in dsh: no login, no sign-up, no API key, nothing
> else. The frontier models are just there — DeepSeek V4.1 Flash, Kimi K3 and the rest.
> Free, with no usage cap.*
>
> 模型清单跟随上游刷新，可用性由**你自己这台机器的网络出口**实测得出，
> 思考强度下发的是真实预算而不是提示词，另附一个 OpenAI 兼容的本地转发端口。
>
> 纯插件挂载：不改内核、无构建步骤、零依赖。

</div>

---

## 交流群

<div align="center">
  <img src="docs/images/qq-group-883073874.jpg" alt="ai技术交流群8 入群二维码（群号：883073874）" width="300">
  <br>
  <b>QQ 群：883073874（ai技术交流群8）</b>
  <br>
  扫码或搜索群号加入群聊，一起交流插件使用心得、反馈问题与分享玩法。
</div>

---

## 亮点

- **开箱即用，无配置环节**——不需要账号、不需要 Key、不需要在后台申请配额。
- **上游来源公开透明**——免费车道来源为 [OpenCode 的 Zen 网关](https://opencode.ai)，Kilo 渠道来源为 [Kilo AI 的公共网关](https://kilo.ai)，均直连、不经任何第三方中转。请求由谁处理、数据发往何处，见「上游是哪些源」与「免责声明」。
- **清单跟随上游**——模型集合、上下文长度与能力在每次刷新时向上游重新拉取，插件内不保存静态快照。
- **选择器只广播可用的模型**——上游清单已声明但网关明确拒绝路由的模型（返回 `Model is unavailable`、或 404 找不到该 id）从下拉框移除，仅在设置页保留记录并注明拒因；网关自身故障（5xx）、配额限制（429）、超时与断网不属于对模型的判定，一律保持可达；被地区策略拦截的模型归入 region-limited 分组。整轮探测全部被拒时同样保留，选择器不会为空。
- **公告中心 + 实时推送**——仓库维护者在仓库中编辑 JSON 并推送后，所有已安装实例最迟在一个轮询周期内收到；正文为白名单约束下的 HTML，支持图文排版；`urgent` 级别触发全屏弹窗；可选系统级通知。
- **应用内升级**——设置页一键升级：下载 → SHA-256 校验 → 备份 → 原子替换 → 校验回读 → 热重载，任一步失败自动回滚至上一版本。
- **热重载**——升级与代码变更即时生效，无需重启应用；也可在设置页手动触发，或启用文件监视自动重载。
- **按响应体形状判定流式响应**——网关在高负载下会以 `application/json` 的 content-type 返回完整的 SSE 帧序列。插件按响应体形状判定，并将已嗅探的字节重新注入流，既不会导致整轮失败，也不会因 header 与实际内容不符而将可用模型判为不可用。
- **思考强度实际生效**——两类模型两种控制：声明了思考档位的模型（如 DeepSeek V4.1 Flash、GLM 5.3 Flash）给出它自己的档位菜单（Off / Low / High / Max 等），选中值按原值下发到上游 `reasoning_effort`，上游会校验该字段、集合外的取值直接 400；没有档位菜单的模型（MiMo V2.6 等）走预算阶梯——Light / Balanced / Deep 对应输出 token 预算 2 048 / 8 192 / 模型上限，思考不可关闭的模型三档整体翻倍为 4 096 / 16 384 / 模型上限，因为思考与正文共享同一输出额度。两者都逐次调用留痕，设置页每张模型卡均标注档位或该档实际下发的上限（详见「思考强度：档位菜单与预算阶梯」）。
- **不依赖浏览器界面**——插件仅将 llm 作为硬依赖，在没有 web server 的 composition（如 dsh-tui）中同样完成启动并输出模型；看板模块挂载在独立的 fiber 上，待 webServer 就绪后再注册路由，因此既不会阻塞模型车道，也不会因插件先于 web 服务加载而永久丢失设置页。
- **用量看板，数据全部留在本机**——Token 热力图、总量曲线（支持总计与单模型视图）、输出速度与首字延迟逐次采样。不上传任何数据。
- **OpenAI 兼容转发端口**——本机其它工具通过 base URL 与 Key 即可调用这些模型。Chat 历史中 assistant 的字符串 `reasoning_content` 会随工具后续请求保留，包括显式空字符串；缺失字段不会被补造。
- **EAC 渠道（桌面端专属）**——在 DeepSeek Harness 桌面端与 DSHEAC AIO 桌面端中自动解锁一条协付通道，模型以 EAC 前缀显示（如 EAC DeepSeek V4.1 Flash）；凭据加密密封，由宿主指纹闸门把守；该渠道在服务器侧校验 GitHub 授权（登录并 star 本仓库）后才放行对话；在命令行及其它宿主中该通道完全不存在。详见「EAC 渠道」。
- **Kilo 渠道（免密免费池）**——内置 Kilo AI 公共网关的免费模型池（`isFree` 清单实时拉取，含 `kilo-auto/free` 自动路由），无需任何账号或 Key；模型卡带 Kilo 徽章。思考强度与 EAC 渠道同款：模型自身的档位菜单（Off / Low / Medium / High，默认 High），经网关统一的 `reasoning` 参数真实下发——Off 已逐家族实测将思考归零（nemotron、ling、dots、poolside、apodex、cohere）；stepfun 与 liquid 端点强制思考（对关闭请求返回 400）、两个自动路由不透传关闭，这些模型的菜单不含 Off 档。该池由上游免费提供，上游会在其模型卡中声明 prompt 可能被记录用于改进服务——请勿发送敏感内容，详见「免责声明」。
- **聚合渠道，自带 Key**——设置页新增一页，把第三方端点接进同一条模型清单：注册表内置 76 家提供商（NVIDIA NIM、OpenRouter、Groq、Cerebras、SambaNova、Gemini、DeepSeek、Mistral、Together、Fireworks、SiliconFlow、Nebius、Chutes、Hugging Face、Cloudflare、Z.ai、Kimi、MiniMax、QwenCloud/Alibaba、Bedrock、Vertex、Vercel AI Gateway、Azure OpenAI、FleetRelay Gateway，以及无需账号的 Ollama、LM Studio、llama.cpp），写入 Key（本机免账号的提供商不需要）后其模型即以 `provider/model` 出现在选择器里，也可经本地网关调用。Key 只写入本机 0600 的 settings.json，API 只回显 `hasKey` 与 `…abcd` 指纹；每家可单独启停、测试（列表探测，不花一次生成）、发现模型、覆盖 Base URL 与模型清单。OAuth 与 ADC 认证的提供商照常列出，但标注为不可驱动。
- **省 Token**——三件事：工具输出压缩（RTK）在请求发出前就地重写 `tool_result`（git diff / status / log、grep、find、ls、tree、构建日志、编号转储、搜索清单、重复日志行），实测 40 KB 的 `git diff` 移除 90% 的字节且模型仍能就它作答；提示词瘦身有 caveman 与 ponytail 两族、默认全关；另有五个不占用上游请求的本地应答。设置页用与用量图表同一批统计行显示压缩前后字节、节省比例、压缩块数与统计调用数。
- **路由（降级链）**——把任意车道的模型串成一条命名链，以 `combo:<name>` 作为虚拟模型出现在选择器与网关上；`fallback` 固定从链首开始，`round-robin` 轮换起点并连续 N 轮粘滞。链接在输出任何正文之前失败会被整段丢弃，切换对调用方不可见；思考增量不算正文，因此「想了很久才撞上配额墙」正是降级最有价值的场景。
- **本地网关原生说 Anthropic**——新增 `POST /v1/messages`（流式与非流式，含 thinking 