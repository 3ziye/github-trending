# g1-acq

[![Telegram](https://img.shields.io/badge/Telegram-AI羊毛交流群-26A5E4?logo=telegram&logoColor=white)](https://t.me/muihbb)

> 💬 **AI羊毛交流群**:https://t.me/muihbb —— 交流 AI 优惠、订阅羊毛

Google One（iOS）订阅入口的商品 ID 改写与采集工具，适用于 **Shadowrocket / 小火箭**。

**v7.11.0 主模块为 G1 ACQ SKU 管理，新增「1 元开 Pro」预制模板，目标命名空间支持 com.google.gemini.*。** 打开[本地报告页](https://one.google.com/g1-sku-report)，在 **预制映射模板** 中点击 **应用模板**，即可直接合并并保存到手机本地，无需再填源、目标或另点保存。页面继续支持添加、编辑、勾选启用、逐条保存、删除映射和恢复默认；采集列表可预填源，输入框提供已采集 SKU 与模板目标候选。**点击时保存配置，下一次 `/ai?` 响应才使用新规则**，已打开或缓存的方案页需重新进入。

默认模式 `discount75` 保留 20TB / 30TB 三个月 75p 和原始 iOS 2TB → `g1.2tb.ai.12months_ip_90p`；应用模板或保存手动规则后为 `custom`，即使模板目标恰好与默认相同。**75p = 75% off、实付 25%、2.5折**。当前改写运行版本为 `g1-acq-v7.11-mappings`，保留原始 SKU 采集、最近 10 次响应、重复诊断与 JSON 导出，无需另装扫描器；完整步骤见 [SKU 管理、Pro 12个月优惠测试与采集](docs/pro-annual-test.md)。

采集只读取手机实际收到的匹配响应，**不会主动查询全量 SKU**；旧 ID 再次出现时累加次数。字符串改写与 App Store 商品返回分别记录，商品名称、周期、初次与续费金额按收银台实际显示核对，权益按 Google One 账户实际状态记录。

## 主模块安装地址

**G1 ACQ SKU 管理 — 四套预制模板与本地手动映射，保留默认 75p 与 2TB 目标**

```text
https://cdn.jsdelivr.net/gh/crhywun/g1-acq@v7.11.0/g1-acq-ultra-discount.sgmodule
```

| 项目 | 当前主入口 |
|---|---|
| 当前配置 `configuredMode` | 默认 `discount75`；应用模板或保存手动规则后 `custom` |
| 响应脚本 | [g1-acq-discount.js](g1-acq-discount.js)，与 [g1-acq.js](g1-acq.js) 实现相同 |
| 响应运行版本 | `g1-acq-v7.11-mappings` |
| 报告脚本 | [g1-sku-report-discount.js](g1-sku-report-discount.js)，与 [g1-sku-report.js](g1-sku-report.js) 实现相同 |
| 报告版本 | `v7.11.0` |
| 默认 2TB 目标 | `g1.2tb.ai.12months_ip_90p`，无 `.acq` |
| 本地数据 | 沿用 v7.9 的三个 schema 1 键；模板结果仍保存在 `g1.sku.mappings.v1`，无数据迁移 |

首次安装时在小火箭模块管理中添加上方地址并启用。升级顺序为：**关闭旧模块 → 安装新地址 → 只开启 G1 ACQ SKU 管理一个改写入口 → 重新连接小火箭 → 重新打开 Google App 的方案页**。曾安装 **G1 ACQ Ultra 75p**、**G1 ACQ**、**G1 ACQ Ultra 一折**、**G1 ACQ Ultra 试用**、独立 **G1 SKU Scan**、**G1 Pro Annual Test** 或其它改写副本时，停用旧副本，避免重复计数或改写。

安装入口与全部内部脚本固定引用 `@v7.11.0`，无需单独添加脚本。**旧固定链接需换成新地址，不会自动更新。** 当前树保留四个模块，试用模块仍缺席；历史 `v7.10.0` / `v7.9.0` / `v7.8.0` / `v7.7.0` / `v7.6.0` / `v7.5.0` / `v7.4.0` / `v7.3.0` / `v7.2.0` / `v7.1.0` / `v7.0.0` 与 `pro-annual-test-v1` / `pro-annual-test-v2` 标签保持原样，旧试用链接仍指向原内容。

升级沿用 `g1.sku.scan.v1`、`g1.pro.annual.test.v1`、`g1.sku.mappings.v1`，三个键的 `schemaVersion=1` 保持不变，无自动配置迁移；v7.9 已保存的手动规则、累计 SKU、次数、最近 10 次响应和旧执行记录继续保留。当前配置与实际采集、执行记录分别显示，应用模板、保存或恢复规则不重写历史版本、模式、目标与时间。

[g1-acq-v7.sgmodule](g1-acq-v7.sgmodule) 保留名称 **G1 ACQ**；[g1-pro-annual-test.sgmodule](g1-pro-annual-test.sgmodule) 保留名称 **G1 Pro Annual Test** 和仅 `/ai?` 的响应范围，二者使用同一本地映射配置。[g1-sku-scan.sgmodule](g1-sku-scan.sgmodule) 更新下载 pin 并保留报告请求体配置，扫描实现仍为 `pro-annual-test-v2`，保持响应原文，没有模式或响应事件字段；报告保留其真实旧版本、空模式与缺失历史。四个报告 `http-request` 均设置 `requires-body=1,max-size=0`，供本地表单提交使用。

## 四套预制映射模板

报告的 **预制映射模板** 位于手动规则前，按以下顺序展示；点击卡片的 **应用模板** 即提交原生 POST，成功后以 **303** 返回报告，并提示模板已保存到本机、下一次匹配响应读取新配置。

| 模板 | 匹配方式 | 完整源 → 目标 |
|---|---|
| **1 元开 Pro**（`pro-1yuan`） | 精确 `exact` | `g1.ios.20tb.m.v2` → `com.google.gemini.2tb.ai.m.3month_ip_99p` |
| **土区 30TB · 2949.99 里拉记录**（`tr-ultra-30tb`） | 精确 `exact` | `g1.ios.30tb.ai.pro.m` → `g1.ios.30tb.m` |
| **Ultra 20TB / 30TB · 三个月 75p**（`ultra-75p`） | 两条精确 `exact` | `g1.ios.20tb.m.v2` → `g1.20tb.3months_ip_75p.acq`<br>`g1.ios.30tb.ai.pro.m` → `g1.ai.ultra.3months_ip_75p.acq` |
| **2TB / Pro · 12个月 90p**（`pro-12months-90p`） | 前缀 `prefix` | `g1.ios.2tb.` → `g1.2tb.ai.12months_ip_90p` |

土区模板使用旧 iOS 30TB 编号。[公开历史记录](https://github.com/kawhaiyoung/rule/blob/b9ce20bc11a77762216fb9f1ab0f04371f943290/G1_ACQ_Egern_README.md#L75)记载 `g1.ios.30tb.m` 曾调起 **2949.99 TRY** 报价；[土耳其 App Store 公开列表](https://apps.apple.com/tr/app/google/id284815942)列出 **Google AI Ultra (30 TB) ₺2.949,99**，公开列表未给出对应 productId 或周期。这里的“2949”仅指公开历史报价，不保证当前账号价格或周期，也不构成实机购买成功、周期或权益已验证的证据；实际金额、周期与权益分别记录 App Store 面板和 Google One 账户显示。

Ultra 模板同时切换 20TB / 30TB，75p 表示减免 75%、实付 25%；2TB / Pro 模板使用现有 2TB 前缀与独立的 12个月 90p 候选，商品周期按 App Store 面板显示。默认三条保持不变，预制目录没有过期 `trial` 或 Ultra 90p 模板，也不重新开启旧试用或 Ultra 一折模式。

- **合并并启用**：按 `(match, from)` 查找已有规则，更新目标并设为启用，保留该条 `id` 和顺序；缺少时追加新规则。其他手动规则、禁用规则与更窄前缀 / 精确覆盖均保留，仍按精确优先、最长前缀决定实际匹配。
- **重复点击与容量**：重复应用不新增重复规则，但成功保存仍生成新修订。禁用规则也计入 **30 条**上限；已有 30 条时仍可更新同源规则，合并后超过 30 条则整次失败、零写入，不保存部分模板。
- **冲突与存储失败**：旧页面或保存前配置已变化时返回 409，刷新核对再提交；读取、写入或回读失败返回 503，不显示保存成功，刷新后核对实际配置。损坏或不可读取的配置会禁用模板控件；缺少写入接口时也停用模板操作。
- **状态与执行分开**：卡片的 **当前规则一致** 只表示全部模板规则在当前配置中匹配且启用，内建默认也可满足该状态；POST 成功提示才表示本次模板已保存。两者均不证明下一响应已改写，更不证明 App Store 购买或权益；重开方案后核对 `test.mappingRevision`、时间和实际 `to`。
- **与恢复默认的区别**：应用模板保留其他规则并保存为 `custom`；**恢复默认**替换整个规则配置，清除手动差异并回到内建三条 `discount75`。两种操作均保留采集与执行历史，模板不新增持久化字段或 JSON 字段。

## 默认规则与手动映射

主入口先采集 `one.google.com/` 原始文字响应，再仅对 `one.google.com/ai?` 响应中的完整 SKU 执行规则。首次使用或恢复默认时启用以下三条：

| 匹配方式 | 源 | 目标 ID |
|---|---|---|
| 前缀 `prefix` | `g1.ios.2tb.` | `g1.2tb.ai.12months_ip_90p` |
| 精确 `exact` | `g1.ios.20tb.m.v2` | `g1.20tb.3months_ip_75p.acq` |
| 精确 `exact` | `g1.ios.30tb.ai.pro.m` | `g1.ai.ultra.3months_ip_75p.acq` |

编辑时选择**精确或前缀**，填写源与完整目标 ID，勾选“启用”后保存。精确源与目标支持 `g1.*` / `com.google.one.*` / `com.google.gemini.*`，命名空间之后有 1–160 个字母、数字、点、下划线或连字符，完整 ID 不以点结尾；*