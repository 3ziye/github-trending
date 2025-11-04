# getk · 美股K线数据抓取 / US Stock K-Line Fetcher

<p align="center">
  <a href="#简体中文">简体中文</a> · <a href="#english">English</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Go-1.21%2B-00ADD8?logo=go" alt="Go" />
  <img src="https://img.shields.io/badge/PostgreSQL-12%2B-336791?logo=postgresql" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/LongPort-OpenAPI-ff6d00" alt="LongPort OpenAPI" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-2ea44f" alt="Platform" />
</p>

---

## 简体中文

一个基于长桥证券接口（LongPort OpenAPI）的抓取工具，按配置批量抓取指定股票在指定日期的历史 K 线并写入 PostgreSQL。支持多只股票、多日期、去重插入、进度显示。

### 功能特性
- 批量多线程抓取指定标的的历史 K 线（分钟级）
- 多日期批处理，自动去重（`ON CONFLICT DO NOTHING`）
- 自动根据标的生成数据表（如 `AAPL.US` → `aapl_us`）
- 支持 `go run` 与二进制部署两种运行方式

### 环境要求
- Go 1.20+（建议 1.21 或更高）
- PostgreSQL 12+
- LongPort OpenAPI 凭证（App Key、App Secret、Access Token）

### 如果没有 LongPort OpenAPI 凭证？

> 必须要在长桥证券开户，才能够开通 LongPort OpenAPI。

（一）长桥证券香港  
开户链接：[https://app.longbridgehk.com/ac/oa?account_channel=lb&channel=HB100036&invite-code=1OZ6MT](https://app.longbridgehk.com/ac/oa?account_channel=lb&channel=HB100036&invite-code=1OZ6MT)

优势：配合香港银行卡出入无损，账户功能更加完善  
福利：
1. 入金等值 1W 港币得港股终身免佣金；
2. 入金 2 万港币或等值美金得 400 港币股票现金卡 + 5 美元现金卡 + 5% 收益货币基金购买资格；
3. 支持日内 10 倍融资，新加坡不支持。

（二）长桥证券新加坡  
开户链接：[https://activity.lbmkt.ing/pages/longbridge/7415/index.html?app_id=longbridge&org_id=1&account_channel=lb&lang=zh-CN&channel=HB100036&invite-code=1OZ6MT](https://activity.lbmkt.ing/pages/longbridge/7415/index.html?app_id=longbridge&org_id=1&account_channel=lb&lang=zh-CN&channel=HB100036&invite-code=1OZ6MT)

优势：配合新加坡银行卡新币出入无损，有护照即可办理；  
福利：
1. 入金 1800 新币可得港美股终生免佣；
2. 入金满 3400 新币得 72 新币股票现金卡 + 5 美元期权现金卡；
另外：用我链接开户的，再赠送 100 HKD 现金或者 18 新币。

- 开户成功后注册 LongPort OpenAPI 账号：[https://open.longportapp.com/](https://open.longportapp.com/)
- 创建应用并获取凭证（App Key、App Secret、Access Token）
- 配置 `config/longport.yaml` 或环境变量

### 快速运行（Windows 示例）
```powershell
# 直接运行（读取项目根的 config/）
go run .\main.go

# 或构建后运行（读取 exe 同级的 config/）
go build -o getk.exe .
.\getk.exe
```

### 配置文件示例
#### 1) `config/config.yaml`
```yaml
symbols:
  - "AAPL.US"
  - "TSLA.US"
  - "NVDA.US"

dates:
  - "2025-10-15"
  - "2025-10-16"
  - "2025-10-17"

settings:
  period: "OneMinute"      # 可选：OneMinute, FiveMinute, FifteenMinute, ThirtyMinute
  adjust_type: "No"        # 可选：No, ForwardAdjust
```

#### 2) `config/db.yaml`
```yaml
db:
  host: "127.0.0.1"
  port: 5432
  user: "postgres"
  password: "your_password"
  name: "your_database"
  sslmode: "disable"
```

#### 3) `config/longport.yaml`
```yaml
longport:
  app_key: "xxxxx"
  app_secret: "xxxxx"
  access_token: "xxxxx"
  region: "cn"
  threads: 5
  rps: 10
```
也可用环境变量（PowerShell）：
```powershell
setx LONGPORT_APP_KEY "your-app-key"
setx LONGPORT_APP_SECRET "your-app-secret"
setx LONGPORT_ACCESS_TOKEN "your-access-token"
```

### 数据库表结构与写入规则
- 表名：取股票代码点号前部分并转小写，加上下划线分隔符。例如 `AAPL.US` → `aapl_us`。
- 去重：以 `timestamp` 为唯一键，`ON CONFLICT (timestamp) DO NOTHING` 跳过重复。

示例表结构（以 `aapl_us` 为例）：
```sql
CREATE TABLE IF NOT EXISTS aapl_us (
  timestamp   TIMESTAMPTZ PRIMARY KEY,
  open        DOUBLE PRECISION,
  close       DOUBLE PRECISION,
  high        DOUBLE PRECISION,
  low         DOUBLE PRECISION,
  volume      BIGINT,
  turnover    DOUBLE PRECISION
);
```

### 常见问题
- 读取配置失败：确认实际生效的配置目录内存在 `config.yaml / db.yaml / longport.yaml`。
- LongPort 鉴权错误：检查 `app_key/app_secret/access_token` 是否有效，并确保账户具有行情权限。

### LongPort 接口频率限制
- 每个账号同时只能建立一个长连接，最多同时订阅 500 个标的。
- 1 秒内不超过 10 次调用，并发请求数不超过 5。
- OpenAPI SDK 内部已经做了有效的频率控制：
  - 行情类：`QuoteContext` 下的接口，SDK 会按照服务端频率限制自动控制；请求过快时会自动延迟。
  - 交易类：`TradeContext` 下的接口，SDK 没有做限制，需要用户自行处理。

### LongPort 使用费用
LongPort 不针对接口服务额外收取开通或使用费用，只需开通 LongPort 账户及 OpenAPI 服务权限后即可免费使用。实际交易费率请咨询您开通证券账户的券商。

### 说明
- 本项目使用 `github.com/longportapp/openapi-go/quote` 拉取历史 K 线。
- 路径解析已优化以兼容 `go run` 与二进制部署场景。

---

## English

A data fetcher powered by LongPort OpenAPI. It batches historical K-line (candlestick) data for specified symbols and dates, and writes into PostgreSQL. Supports multiple symbols, multiple dates, de-dup insert, and progress display.

### Features
- Batch multi-thread fetch minute-level historical K-line for selected symbols
- Multi-date processing with de-dup (`ON CONFLICT DO NOTHING`)
- Auto-create table per symbol (e.g. `AAPL.US` → `aapl_us`)
- Works with both `go run` and compiled binary deployments

### Requirements
- Go 1.20+ (recommend 1.21+)
- PostgreSQL 12+
- LongPort OpenAPI credentials (App Key, App Secret, Access Token)

### Don’t have LongPort OpenAPI credentials?

> LongBridge currently does not support customers from the United States and Canada due to licensing. You need a LongBridge brokerage account to enable OpenAPI.

(1) LongBridge Hong Kong  
Signup: [https://app.longbridgehk.com/ac/oa?account_channel=lb&channel=HB100036&invite-code=1OZ6MT](https://app.longbridgehk.com/ac/oa?account_channel=lb&channel=HB100036&invite-code=1OZ6MT)

Pros: seamless HKD in/out with HK