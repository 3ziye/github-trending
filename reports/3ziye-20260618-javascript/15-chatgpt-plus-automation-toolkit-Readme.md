# ChatGPT 全流程助手

自动化完成 ChatGPT Plus 账号注册、支付、授权、Session 导出的全链路工具。

## 功能概览

| 编号 | 功能 | 说明 |
|------|------|------|
| 流程一 | 注册账号生成长链接 | 邮箱注册 ChatGPT → 获取 accessToken → 生成 Plus 支付链接 |
| 流程二 | GoPay 支付长链接 | 打开支付链接 → 填写账单 → GoPay 绑定 → OTP → PIN → 支付完成 |
| 流程三 | OAuth 账号授权 | 已支付账号 → OAuth 获取 refresh_token → 落盘 |
| 流程四 | Session 本地导出 | 从浏览器 profile 提取 session → 导出为 sub2api 格式 |
| 流程五 | Free 注册 | 注册免费 ChatGPT 账号（手机号/邮箱方式） |
| PayPal Plus | 注册 + 支付 + 授权 | iCloud 邮箱注册 → PayPal 绑卡支付 → OAuth 授权（独立子流程） |

## 环境要求

- Python 3.10+
- Playwright（自动安装 Chromium）
- Windows / macOS / Linux

## 安装

```bash
# 安装依赖
pip install -r requirements.txt

# 安装 Playwright 浏览器
playwright install chromium
```

## 快速开始

```bash
# 交互式菜单（推荐）
python main.py

# 命令行模式
python main.py --mode register --count 5 --workers 3
python main.py --mode gopay
python main.py --mode authorize
python main.py --mode session-export
python main.py --mode free-register --count 10 --workers 5
```

## 目录结构

```
├── main.py                    # 主入口 + 流程一逻辑
├── authorization_flow.py      # 流程三：OAuth 授权
├── fill_billing_test.py       # 流程二：GoPay 支付
├── config.yaml                # 主配置文件
├── .env                       # 环境变量配置（敏感信息）
├── modules/
│   ├── browser.py             # 浏览器会话管理（指纹、代理）
│   ├── chatgpt_register.py    # ChatGPT 注册核心逻辑
│   ├── checkout.py            # 生成支付长链接
│   ├── free_register.py       # Free 注册流程
│   ├── free_browser_flow.py   # Free 注册浏览器操作
│   ├── paypal_flow.py         # PayPal Plus 主编排
│   ├── paypal_register.py     # PayPal 流程一：注册生成长链接
│   ├── paypal_pay.py          # PayPal 流程二：PayPal 绑卡支付
│   ├── paypal_card_pool.py    # PayPal 虚拟卡池管理
│   ├── paypal_phone_pool.py   # PayPal 手机号池管理
│   ├── billing_provider.py    # 美国地址生成
│   ├── mail_provider.py       # 邮箱验证码获取
│   ├── proxy_pool.py          # 代理池
│   ├── storage.py             # 账号存储管理
│   ├── session_export.py      # Session 导出
│   ├── env_settings.py        # 设置面板
│   ├── utils.py               # 工具函数
│   └── ...
├── data/
│   ├── accounts.txt           # 流程一邮箱账号池
│   ├── mail_pool.txt          # 原始邮箱池
│   ├── proxies/proxies.txt    # 代理列表
│   ├── icloud/                # iCloud 邮箱配置
│   ├── hotmail/               # Hotmail 邮箱配置
│   └── paypal/
│       ├── icloud_accounts.txt  # PayPal 流程 iCloud 账号
│       ├── cards.txt            # 虚拟卡池
│       └── phones.txt           # 手机号池
├── output/
│   ├── 流程1_注册成功长链接.txt
│   ├── 流程2_支付成功待授权.txt
│   ├── 授权输出/              # 流程三输出
│   ├── session导出/           # 流程四输出
│   ├── free成品/              # Free 注册输出
│   └── paypal成品/            # PayPal Plus 输出
│       ├── 长链接账号/
│       ├── 待授权账号/
│       └── 授权成功/
└── profiles/                  # 浏览器 profile 缓存
```

## 配置说明

### .env 环境变量

复制 `.env.example` 为 `.env` 并填写：

```bash
cp .env.example .env
```

#### 邮箱源配置

```ini
# 邮箱源选择：moemail / hotmail / icloud_query
MAIL_SOURCE=moemail

# 各流程可单独指定邮箱源（覆盖全局）
FLOW1_MAIL_SOURCE=icloud_query
FREE_MAIL_SOURCE=moemail

# 邮箱账号模式：pool（从文件读取）
MAIL_ACCOUNT_MODE=pool
```

#### MoeMail 自建邮箱池

```ini
MOEMAIL_ENABLED=false
MOEMAIL_BASE_URL=https://your-moemail-server.com
MOEMAIL_API_KEY=your-api-key
MOEMAIL_DOMAIN_WHITELIST=domain1.com,domain2.com
MOEMAIL_CREATE_PREFIX=openai
MOEMAIL_CREATE_MODE=human
```

#### 代理配置

```ini
# 全局代理开关（流程一/Free 注册）
USE_PROXY=false
PROXY_FILE=data/proxies/proxies.txt

# PayPal 流程独立代理开关
PAYPAL_USE_PROXY=false
PAYPAL_PROXY_FILE=data/proxies/proxies.txt
```

代理文件格式（每行一个）：
```
http://user:pass@host:port
socks5://host:port
host:port
```

#### 接码平台配置

支持 HeroSMS / GrizzlySMS / 5sim 三个平台：

```ini
# 全局开关
SMS_ENABLED=true
SMS_PROVIDER=herosms

# HeroSMS
HERO_SMS_API_KEY=your-key
HERO_SMS_SERVICE=dr
HERO_SMS_COUNTRY_TOP_N=10

# GrizzlySMS
GRIZZLY_API_KEY=your-key
GRIZZLY_SERVICE=auto

# 5sim
FIVESIM_API_KEY=your-key
FIVESIM_SERVICE=openai
```

#### 流程二 GoPay 配置

```ini
# GoPay 手机号（支持多线程分别绑定）
GOPAY_PHONE_1=your-phone-1
GOPAY_PHONE_2=your-phone-2
GOPAY_COUNTRY_CODE=+62
GOPAY_PIN=123456

# 账单重试次数
FLOW2_BILLING_RETRIES=5
FLOW2_OTP_TIMEOUT=90

# WhatsApp OTP 自动取码（需要 ADB）
WHATSAPP_OTP_AUTO=false
WHATSAPP_ADB_PATH=tools\adb\adb.exe
```

#### PayPal 流程配置

```ini
# PayPal 虚拟卡和手机号文件
PAYPAL_CARDS_FILE=data/paypal/cards.txt
PAYPAL_PHONES_FILE=data/paypal/phones.txt
PAYPAL_PHONE_MAX_USES=5

# PayPal 注册国家
PAYPAL_BILLING_COUNTRY=US

# PayPal iCloud 账号文件
PAYPAL_ICLOUD_FILE=data/paypal/icloud_accounts.txt
```

#### 人机验证码处理

```ini
# 模式：manual（暂停等手动处理）/ api（打码平台）
PAYPAL_CAPTCHA_MODE=manual
PAYPAL_CAPTCHA_TIMEOUT=180

# 打码平台（api 模式）
CAPTCHA_API_PROVIDER=capsolver
CAPSOLVER_API_KEY=your-key
# 或 2Captcha
# CAPTCHA_API_PROVIDER=twocaptcha
# TWOCAPTCHA_API_KEY=your-key
```

#### 授权服务器上传

```ini
AUTH_SERVER_UPLOAD=false
AUTH_SERVER_URL=http://127.0.0.1:8790
AUTH_SERVER_API_KEY=your-key
```

### config.yaml

主配置文件，包含浏览器参数、ChatGPT 入口、注册 profile 等。一般不需要修改。

### 数据文件格式

#### accounts.txt（流程一邮箱池）

```
email@domain.com----query_code
email2@domain.com----query_code2
```

#### data/paypal/cards.txt（PayPal 虚拟卡）

```
KW-ID----卡号----有效期----CVV----手机号----持卡人----地址----API地址
```

示例：
```
