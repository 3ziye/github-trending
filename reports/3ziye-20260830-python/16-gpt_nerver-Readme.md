# gpt_nerver

一个用于**批量维护 / 开通 ChatGPT Plus** 的本地 PyQt6 桌面工具。核心能力：

- **注册引擎**：协议 / UI 双模式建号（`vendor/register-protocol`），支持 iCloud/Outlook/xpgmail/CF-Worker 邮箱源、密码 + TOTP + Passkey MFA、手机号注册。
- **登录态维护**：session cookie 刷 AT、AT 吊销自动密码 + TOTP 重登、代理体检 + SID 轮换。
- **卡池 & 开通**：Duola 虚拟卡自动开卡 / 补卡；PH-Link 提链 + Stripe 绑卡 + `checkout/confirm` 全链路开 Plus。
- **CDK 兑换**：外部充值站（`chong.nerver.cc` 同协议）批量兑换，多渠道 CDK 池管理。
- **附加变现链路**：GCash 订阅 / PayPal 批量取链 / 手机号绑定 + Codex PKCE 生成 CPA。

> ⚠️ **本仓库仅用于学习与合规测试**。使用者须自行确保遵守 OpenAI、Stripe、各代理服务商、
> 各地区法律法规的相关条款。作者不对任何滥用行为负责，不承诺代码稳定性或结果可用性。

---

## 目录

- [快速开始](#快速开始)
- [能跑什么 / 不能跑什么](#能跑什么--不能跑什么)
- [目录结构](#目录结构)
- [十个 Tab 一览](#十个-tab-一览)
- [外部服务接入](#外部服务接入)
- [常见工作流](#常见工作流)
- [开发与测试](#开发与测试)
- [进一步阅读](#进一步阅读)
- [免责声明](#免责声明)

---

## 快速开始

### 环境要求

- Python **3.10+**（推荐 3.11 / 3.12；已在 3.14 上过 smoke）
- Windows / macOS 均可；部分远端浏览器功能依赖 AdsPower 本地 API
- 首次运行会自动下载并解压 Chromium（Playwright）

### 安装

```bash
git clone https://github.com/<你的用户名>/gpt_nerver.git
cd gpt_nerver
python -m pip install -r requirements.txt
python -m playwright install chromium
```

### 首次启动

```bash
python -m src.main
```

首次启动会：

1. 复制 `config.example.json` → `config.json`（本地文件，不进 git）
2. 在仓库根目录建 `gpt_nerver.db`（SQLite，全部账号 / 卡 / CDK / 手机号池数据存这里）
3. 建 `logs/`、`data/`、`output/` 三个目录
4. 弹出 GUI（10 个 Tab）

---

## 能跑什么 / 不能跑什么

诚实矩阵。别人 clone 后立刻能用的、需要自己配一层的、必须联接外部 SaaS 才能跑的，分三档：

### ✅ 开箱即用（零外部服务）

| 场景 | 说明 |
| --- | --- |
| GUI 启动 | `python -m src.main` |
| 手动导入 session-token / 邮箱-密码-TOTP-session-AT 多段格式 | 「账户列表」→ 粘贴导入 |
| 「完善 SESSION」刷新 → 输出完整 JSON | 只依赖 `chatgpt.com/api/auth/session?refresh=true` |
| 「查订阅」批量查 plan | 只依赖 chatgpt.com API |
| SQLite 账户 / 卡 / CDK / 手机号池管理、CSV 导入导出 | 纯本地 |
| 单元测试 | `python tests/test_cdk_pool_and_geo.py` / `python tests/test_relogin_proxy_rotate.py` |

### 🔧 需要自己配一层（免费 / 自建）

| 依赖 | 用在哪 | 起步成本 |
| --- | --- | --- |
| **住宅或数据中心代理** | 没代理 CF 直接 403 | 任意 socks5/http 都行，`config.json.proxies` 或"代理"Tab 粘一行 |
| **AdsPower**（远端浏览器）| UI 建号模式；协议模式不需要 | 免费版够用，默认 `http://127.0.0.1:50325` |
| **CF Email Worker 邮箱域** | 「随机邮箱」注册模式收 OTP | 自建 CF Worker，改 `config.mail.email_domain`，见 [`docs/SETUP.md`](docs/SETUP.md) |
| **hCaptcha 求解器**（可选）| 注册风控高时 | nonecap / yescaptcha 之类，付费 |

### 💰 必须联外部 SaaS 才能跑（硬依赖）

| 服务 | 用在哪 | 没有 key 会怎样 |
| --- | --- | --- |
| `cha.nerver.cc` API | PH-Link 提链、优惠预检、PayPal 取链、GCash、订阅查询、UPI/PIX/iDEAL/Kakao 出码 | 直接失败，需 `config.cha.api_key` |
| `chong.nerver.cc` API | CDK 兑换充值 | 走不通 CDK 开通模式 |
| Duola 虚拟卡商 | 自动开卡 / 补卡 | 只能手动导入卡池 |
| HeroSMS / SMSBower | 手机号注册 + 手机号绑定 CPA | 走不到这条路，转为纯 email 注册 |
| IPWEB / IPRoyal 住宅代理 | 高抗封成功率 | 可换任意代理，但成功率显著下降 |
| iCloud 邮箱池后台 | `icloud_mail_provider.py` 客户端连的后台服务 | 只能改用 outlook / imap 模式手动导入 |

> **注意**：`cha.nerver.cc` / `chong.nerver.cc` 是本仓库作者维护的 SaaS 服务，需自行联系拿 key 或
> 按其公开 API 协议（`docs/*.md` 有部分描述）自建同协议后端。

---

## 目录结构

```
gpt_nerver/
├── src/
│   ├── main.py                 # 启动入口: python -m src.main
│   ├── ui/                     # PyQt6 桌面 UI
│   │   ├── main_window.py      # 10 个 Tab 挂载
│   │   ├── tabs/               # 每个 Tab 的实现
│   │   │   ├── sessions_tab.py       # 账户列表主 Tab（含右键批量动作）
│   │   │   ├── sessions/             # 从 sessions_tab.py 拆出的子模块
│   │   │   │   ├── workers.py        #   完善SESSION / 查订阅 / GCash 硬查 workers
│   │   │   │   ├── actions.py        #   右键批量操作 Mixin
│   │   │   │   ├── dialogs.py        #   详情 / 粘贴导入 / 出库对话框
│   │   │   │   └── ...
│   │   │   ├── emails_tab.py
│   │   │   ├── cards_tab.py
│   │   │   ├── cdk_tab.py
│   │   │   ├── phone_pool_tab.py
│   │   │   ├── proxy_tab.py
│   │   │   ├── billing_tab.py
│   │   │   ├── ads_tab.py
│   │   │   ├── run_tab.py
│   │   │   └── log_tab.py
│   │   └── *_dialog.py         # PayPal 批量 / 手机号绑定 / GCash 订阅 / QR 出码
│   ├── modules/                # 业务模块（一个模块 = 一条业务链路）
│   │   ├── register_account.py       # 注册主流程
│   │   ├── register_rpc.py           # 调 vendor/register-protocol RPC
│   │   ├── ads_ui_signup*.py         # AdsPower UI 建号
│   │   ├── open_plus.py              # 卡池开通 Plus
│   │   ├── refresh_at.py             # AT 刷新 / SID 轮换
│   │   ├── discount_eligibility.py   # 开通前优惠预检
│   │   ├── duola_cards.py            # Duola 卡商 SDK
│   │   ├── external_open.py          # CDK 开通（chong SaaS）
│   │   ├── external_redeem.py        # CDK 兑换（chong SaaS）
│   │   ├── paypal_links.py           # PayPal 批量取链
│   │   ├── gcash_*.py                # GCash 资格 / 订阅
│   │   ├── phone_bind.py             # 手机号绑定 + CPA
│   │   ├── cpa_pack.py               # CPA JSON 打包
│   │   └── cha_qr_test.py            # QR 出码测试
│   ├── workflow/               # 编排层
│   │   ├── account_workflow.py       # 单账户完整链路
│   │   ├── pool_runner.py            # 单池调度（注册 or 开通）
│   │   ├── dual_pool_runner.py       # 双池并发（注册补水位 + 开通消费）
│   │   ├── batch_runner.py           # 通用批量执行器
│   │   └── batch_opener.py           # 批量开通
│   └── shared/                 # 通用层
│       ├── db.py                     # SQLite 单写线程池
│       ├── config.py                 # config.json 读写
│       ├── logger.py 