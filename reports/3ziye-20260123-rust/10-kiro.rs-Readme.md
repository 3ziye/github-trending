# kiro-rs

一个用 Rust 编写的 Anthropic Claude API 兼容代理服务，将 Anthropic API 请求转换为 Kiro API 请求。

## 免责声明
本项目仅供研究使用, Use at your own risk, 使用本项目所导致的任何后果由使用人承担, 与本项目无关。
本项目与 AWS/KIRO/Anthropic/Claude 等官方无关, 本项目不代表官方立场。

## 注意！
因 TLS 默认从 native-tls 切换至 rustls，你可能需要专门安装证书后才能配置 HTTP 代理。可通过 `config.json` 的 `tlsBackend` 切回 `native-tls`。
如果遇到请求报错, 尤其是无法刷新 token, 或者是直接返回 error request, 请尝试切换 tls 后端为 `native-tls`, 一般即可解决。

**Write Failed/会话卡死**: 如果遇到持续的 Write File / Write Failed 并导致会话不可用，参考 Issue [#22](https://github.com/hank9999/kiro.rs/issues/22) 和 [#49](https://github.com/hank9999/kiro.rs/issues/49) 的说明与临时解决方案（通常与输出过长被截断有关，可尝试调低输出相关 token 上限）

## 功能特性

- **Anthropic API 兼容**: 完整支持 Anthropic Claude API 格式
- **流式响应**: 支持 SSE (Server-Sent Events) 流式输出
- **Token 自动刷新**: 自动管理和刷新 OAuth Token
- **多凭据支持**: 支持配置多个凭据，按优先级自动故障转移
- **智能重试**: 单凭据最多重试 3 次，单请求最多重试 9 次
- **凭据回写**: 多凭据格式下自动回写刷新后的 Token
- **Thinking 模式**: 支持 Claude 的 extended thinking 功能
- **工具调用**: 完整支持 function calling / tool use
- **多模型支持**: 支持 Sonnet、Opus、Haiku 系列模型

## 支持的 API 端点

| 端点 | 方法 | 描述          |
|------|------|-------------|
| `/v1/models` | GET | 获取可用模型列表    |
| `/v1/messages` | POST | 创建消息（对话）    |
| `/v1/messages/count_tokens` | POST | 估算 Token 数量 |

## 快速开始

> **前置步骤**：编译前需要先构建前端 Admin UI（用于嵌入到二进制中）：
> ```bash
> cd admin-ui && pnpm install && pnpm build
> ```

### 1. 编译项目

```bash
cargo build --release
```

### 2. 配置文件

创建 `config.json` 配置文件：

```json
{
   "host": "127.0.0.1",   // 必配, 监听地址
   "port": 8990,  // 必配, 监听端口
   "apiKey": "sk-kiro-rs-qazWSXedcRFV123456",  // 必配, 请求的鉴权 token
   "region": "us-east-1",  // 必配, 区域, 一般保持默认即可
   "tlsBackend": "rustls", // 可选, TLS 后端: rustls / native-tls
   "kiroVersion": "0.8.0",  // 可选, 用于自定义请求特征, 不需要请删除: kiro ide 版本
   "machineId": "如果你需要自定义机器码请将64位机器码填到这里", // 可选, 用于自定义请求特征, 不需要请删除: 机器码
   "systemVersion": "darwin#24.6.0",  // 可选, 用于自定义请求特征, 不需要请删除: 系统版本
   "nodeVersion": "22.21.1",  // 可选, 用于自定义请求特征, 不需要请删除: node 版本
   "countTokensApiUrl": "https://api.example.com/v1/messages/count_tokens", // 可选, 用于自定义token统计API, 不需要请删除
   "countTokensApiKey": "sk-your-count-tokens-api-key",  // 可选, 用于自定义token统计API, 不需要请删除
   "countTokensAuthType": "x-api-key",  // 可选, 用于自定义token统计API, 不需要请删除
   "proxyUrl": "http://127.0.0.1:7890", // 可选, HTTP/SOCK5代理, 不需要请删除
   "proxyUsername": "user",  // 可选, HTTP/SOCK5代理用户名, 不需要请删除
   "proxyPassword": "pass",  // 可选, HTTP/SOCK5代理密码, 不需要请删除
   "adminApiKey": "sk-admin-your-secret-key"  // 可选, Admin API 密钥, 用于启用凭据管理 API, 填写后才会启用web管理， 不需要请删除
}
```
最小启动配置为: 
```json
{
   "host": "127.0.0.1",
   "port": 8990,
   "apiKey": "sk-kiro-rs-qazWSXedcRFV123456",
   "region": "us-east-1",
   "tlsBackend": "rustls"
}
```
### 3. 凭证文件

创建 `credentials.json` 凭证文件（从 Kiro IDE 获取）。支持两种格式：

#### 单凭据格式（旧格式，向后兼容）

```json
{
   "accessToken": "这里是请求token 一般有效期一小时",  // 可选, 不需要请删除, 可以自动刷新
   "refreshToken": "这里是刷新token 一般有效期7-30天不等",  // 必配, 根据实际填写
   "profileArn": "这是profileArn, 如果没有请你删除该字段， 配置应该像这个 arn:aws:codewhisperer:us-east-1:111112222233:profile/QWER1QAZSDFGH",  // 可选, 不需要请删除
   "expiresAt": "这里是请求token过期时间, 一般格式是这样2025-12-31T02:32:45.144Z, 在过期前 kirors 不会请求刷新请求token",  // 必配, 不确定你需要写一个已经过期的UTC时间
   "authMethod": "这里是认证方式 social / idc",  // 必配, IdC/Builder-ID/IAM 三类用户统一填写 idc
   "clientId": "如果你是 IdC 登录 需要配置这个",  // 可选, 不需要请删除
   "clientSecret": "如果你是 IdC 登录 需要配置这个"  // 可选, 不需要请删除
}
```

#### 多凭据格式（新格式，支持故障转移和自动回写）

```json
[
   {
      "refreshToken": "第一个凭据的刷新token",
      "expiresAt": "2025-12-31T02:32:45.144Z",
      "authMethod": "social",
      "priority": 0
   },
   {
      "refreshToken": "第二个凭据的刷新token",
      "expiresAt": "2025-12-31T02:32:45.144Z",
      "authMethod": "idc",
      "clientId": "xxxxxxxxx",
      "clientSecret": "xxxxxxxxx",
      "region": "us-east-2",
      "priority": 1
   }
]
```

> **多凭据特性说明**：
> - 按 `priority` 字段排序，数字越小优先级越高（默认为 0）
> - 单凭据最多重试 3 次，单请求最多重试 9 次
> - 自动故障转移到下一个可用凭据
> - 多凭据格式下 Token 刷新后自动回写到源文件
> - 可选的 `region` 字段：用于 OIDC token 刷新时指定 endpoint 区域，未配置时回退到 config.json 的 region
> - 可选的 `machineId` 字段：凭据级机器码；未配置时回退到 config.json 的 machineId；都未配置时由 refreshToken 派生

最小启动配置(social):
```json
{
   "refreshToken": "XXXXXXXXXXXXXXXX",
   "expiresAt": "2025-12-31T02:32:45.144Z",
   "authMethod": "social"
}
```

最小启动配置(idc):
```json
{
   "refreshToken": "XXXXXXXXXXXXXXXX",
   "expiresAt": "2025-12-31T02:32:45.144Z",
   "authMethod": "idc",
   "clientId": "xxxxxxxxx",
   "clientSecret": "xxxxxxxxx"
}
```
### 4. 启动服务

```bash
./target/release/kiro-rs
```

或指定配置文件路径：

```bash
./target/release/kiro-rs -c /path/to/config.json --credentials /path/to/credentials.json
```

### 5. 使用 API

```bash
curl http://127.0.0.1:8990/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: sk-your-custom-api-key" \
  -d '{
    "model": "claude-sonnet-4-20250514",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "Hello, Claude!"}
    ]
  }'
```

## 配置说明

### config.json

| 字段 | 类型 | 默认值 | 描述                      |
|------|------|--------|------------------------