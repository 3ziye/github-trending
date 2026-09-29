# WorkBuddy Local Gateway

<img width="917" height="754" alt="image" src="https://github.com/user-attachments/assets/7dcfc461-1357-4991-9565-279047687898" />


基于腾讯 **CodeBuddy** 协议开发的**纯 Go、零 CGO 依赖、跨平台单二进制**本地 AI 代理网关。无 Web UI，全部通过命令行（CLI）完成登录、凭据续期与服务控制。

**同时支持两个上游站点**（同一套 `/v2/plugin/*` 协议，凭据按站点隔离，账号池可混挂轮询）：

| 站点 | 上游 | 登录方式 | 登录命令 |
|---|---|---|---|
| 国内站 | `copilot.tencent.com` / `www.codebuddy.cn` | 微信 / 企业微信扫码 | `login` |
| 国际站 | `www.workbuddy.ai` | 浏览器内登录（邮箱 / 验证码 / SSO） | `login -intl` |

---

## 目录

- [核心特性](#核心特性)
- [命令总览](#命令总览)
- [serve](#serve)
- [login](#login)
- [status](#status)
- [refresh](#refresh)
- [monitor](#monitor)
- [probe](#probe)
- [reset](#reset)
- [version / help](#version--help)
- [多账号池](#多账号池)
- [模型列表与倍率](#模型列表与倍率)
- [客户端接入](#客户端接入)
- [各平台部署](#各平台部署)
- [安全提示](#安全提示)
- [从源码构建](#从源码构建)

---

## 核心特性

- **国内 / 国际双站反代**：两个站点走同一套协议，凭据通过 `edition` 字段区分，刷新与对话自动路由到各自上游。
- **模型完全透传**：客户端传什么 `model` 就原样中继到上游，无白名单限制。`/v1/models` 仅用于客户端自动补全，不影响实际转发。
- **模型列表双来源合并**：实时接口 + npm 静态目录，按 ID 去重、接口优先；失败用本地缓存，两边都失败且无缓存时该站点本轮不展示模型（不影响调用）。
- **模型倍率与价格探测**：促销生效时展示 `credits` × factor；促销过期或接口无有效倍率时由余额未耗尽的同站点账号实测（启动即探测、重置后立即探测、每模型 12 小时一轮）。
- **多账号池 + 轮询负载均衡**：`-auth` 逗号分隔或 `-auth-dir` 目录，请求按 round-robin 分发；国内站与国际站账号可混挂。
- **模型级隔离**：`6004` 只冷却触发它的账号 + 模型，`14018` 只阻断该账号的当前收费模型，不再因为一个模型拖垮整个账号。
- **免费站点优先**：同一模型若「一个站点免费、另一个站点收费」，优先使用免费站点账号直至其受限；两个站点都收费（仅倍率不同）时不做倾斜，正常轮询。
- **免费/收费学习**：按「账号 + 模型」从响应 `usage.credit` 学习；`credit=0` 且样本足够（`total_tokens ≥ 100`）才判定免费，避免小样本误判。
- **国内站每日自动签到**：服务启动、凭据热加载时立即补签，之后每天 `UTC+8 09:00` 自动签到；国际站跳过。
- **凭据热加载（免重启）**：默认每 5 秒扫描凭据来源，新增 / 更新 / 删除凭据免重启生效。
- **授权失效自动禁用**：401/403 / `invalid token` / 登录过期时禁止调度、删除凭据文件并写入失效标记，重新 `login` 后自动恢复。
- **后台自动续期**：每 5 分钟检查 Token，距过期不足 15 分钟自动刷新并写回凭据文件。
- **流式分片规范化**：把上游每个分片携带的 `finish_reason:""` 归一化为 `null`，避免 Anthropic 翻译层误判 `stop_reason` 导致工具不执行。
- **工具调用序列自愈**：出站前按 `tool_call_id` 修复并行调用中夹入 message 的历史结构，合并 Responses API 拆散的并行调用，并删除无配对调用、孤儿或重复结果，避免国际站返回 `11148 tool_call_sequence_broken`。
- **OpenAI 兼容协议**：`/v1/chat/completions`（SSE 流式 + 非流式聚合）、`/v1/responses`（Responses API）、`/v1/models`、`/health`。

---

## 命令总览

```text
workbuddy-gateway [command] [options]

命令:
  serve     启动本地网关（默认命令，不带子命令时等同 serve）
  login     登录并获取 / 更新凭据
  status    查看账号池状态
  refresh   手动刷新所有账号访问令牌
  monitor   前台实时监控：账号表格 + 模型统计附表 + 最近日志
  probe     主动探测账号对指定模型的免费 / 收费属性（需 serve 运行中）
  reset     清空除登录凭据外的全部本地数据，并重新拉取模型与倍率
  version   查看版本信息
  help      查看帮助
```

全局选项（对所有命令可用）：

| 选项 | 默认 | 说明 |
|---|---|---|
| `-addr <ip>` | `127.0.0.1` | 网关监听地址 |
| `-port <port>` | `8317` | 网关监听端口 |
| `-auth <path>` | 自动发现 | 凭据文件路径，支持逗号分隔多个 |
| `-auth-dir <dir>` | 空 | 凭据目录，自动加载目录内所有 `workbuddy*.json` |
| `-api-key <key>` | 空 | 设置后调用网关必须携带 `Authorization: Bearer <key>` |
| `-proxy <url>` | 空 | 上游请求代理，如 `http://127.0.0.1:7890`、`socks5://...` |
| `-verbose` | `false` | 输出详细调试日志 |
| `-intl` | `false` | 仅 `login` 生效：登录国际站 |
| `-reload-interval <sec>` | `5` | 凭据热加载扫描间隔，`0` 关闭 |
| `-models-refresh <min>` | `60` | 模型目录刷新间隔，`0` 关闭 |

### JSON 调试日志

工作目录中的 `config.json` 控制结构化调试日志，默认关闭。修改后需要重启网关进程：

```json
{
  "debug": {
    "enabled": true
  }
}
```

开启后，网关把单行 JSON 写入 `logs/debug-YYYY-MM-DD.jsonl`；普通运行日志仍写入原来的 `logs/gateway-YYYY-MM-DD.log`，两者互不替代。可复制 `config.example.json` 作为起点。

### 模型黑白名单

`config.json` 的 `models` 段可按模型名启用黑白名单（大小写与首尾空白不敏感）：

```json
{
  "models": {
    "blocklist": ["deepseek-v4-pro"],
    "allowlist": []
  }
}
```

| 字段 | 说明 |
|---|---|
| `blocklist` | 黑名单，命中即禁用 |
| `allowlist` | 白名单，**非空时**只放行列表内模型，其余一律禁用 |

规则：

- 黑名单优先：命中黑名单直接禁用，即使同时出现在白名单里。
- 两个列表都为空或省略时不做任何限制（默认行为不变）。
- 被禁用的模型会从 `/v1/models`、`/health` 的 `model_count` 和 `monitor` 的模型统计附表中**直接隐藏**。
- 请求被禁用模型时返回 `403` 与中文提示，**不会消耗任何上游账号额度**：

```json
{
  "error": {
    "message": "模型 deepseek-v4-pro 已被网关禁用（命中黑名单），请联系管理员调整 config.json",
    "type": "model_disabled",
    "code": 403
  }
}
```

`serve` 启动横幅会打印当前名单状态，例如 `模型黑白名单: 已启用 (黑名单 1 个 / 白名单 0 个...)`。

### 按模型限制账号文件

`models.accounts` 是**模型专属**的凭据 JSON 文件黑白名单，不是全局账号名单；未配置的模型仍可使用原有账号池。与上面的 `models.allowlist` / `models.blocklist`（控制模型是否可调用）互不替代：

```json
{
  "models": {
    "blocklist": [],
    "allowlist": [],
    "accounts": {
      "deepseek-v4.1-flash": {
        "allowlist": ["intl-a.json", "intl-b.json"],
        "blocklist": ["intl-b.json"]
      },
      "hy3": {
        "blocklist": ["old-account.json"]
      }
    }
  }
}
```

- 同一模型内黑名单优先；账号白名单为空表示不限制，黑名单为空表示不排除。上述示例中 `deepseek-v4.1-flash` 最终只允许 `intl-a.json`，`hy3` 仅排除 `old-account.json`。
- 只接受凭据**文件名**（如 `intl-a.json`），不接受路径或通配符；同名凭据位于多个目录时会拒绝匹配，避免误用。模型名忽略大小写，文件名必须与实际凭据文件一致。
- 请求调度与失败换号都不会绕过账号名单；后台价格探测与本机 `/admin/probe` 也会跳过不允许的账号。若没有匹配的账号，请求返回 `403 model_account_disabled` 中文提示，且不会调用上游。
- 实时运行日志 `logs/gateway-YYYY-MM-DD.log` 在有账号被排除时记录汇总一行（模型、候选账号数、排除明细）；开启调试时 `logs/debug-YYYY-MM-DD.jsonl` 记录每个账号的 `model_account_policy_checked`。`monitor` 模型统计表的“可用账号”列已按名单过滤，只统计符合规则的账号。
- `config.json` 在服务启动时读取，修改后需重启网关；示例中的文件名均为占位值。没有配置 `models.accounts` 时原行为不变。

每条 JSON 调试日志都包含时间、级别、稳定事件名、`trace_id`、`request_id`、服务/实例/版本、路由