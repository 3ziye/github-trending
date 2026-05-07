# Multi-Page Automation

一个用于批量跑通 ChatGPT OAuth 注册/登录流程的 Chrome 扩展。

当前版本基于侧边栏控制，支持单步执行、整套自动执行、停止当前流程、保存常用配置，以及通过 DuckDuckGo / QQ / 163 / 163 VIP / 126 / Inbucket / Hotmail 协助获取验证码。

## 插件效果

一百五十个号，一个401：

<table>
  <tr>
    <td align="center" width="100%">
      <a href="https://apikey.qzz.io/" target="_blank" rel="noreferrer">
        <img src="docs/images/交流群.jpg" alt="QQ交流群，便于大家交流" width="100%" />
      </a><br />
      <strong><a href="https://apikey.qzz.io/" target="_blank" rel="noreferrer">官网 / QQ交流群入口</a></strong><br />
      点击进入官网，查看最新地址与交流入口
    </td>
  </tr>
</table>

## Star History

<a href="https://www.star-history.com/?repos=QLHazyCoder%2Fcodex-oauth-automation-extension&type=timeline&logscale&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=QLHazyCoder/codex-oauth-automation-extension&type=timeline&logscale&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=QLHazyCoder/codex-oauth-automation-extension&type=timeline&logscale&legend=top-left" />
    <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=QLHazyCoder/codex-oauth-automation-extension&type=timeline&logscale&legend=top-left" />
  </picture>
</a>

## 当前能力

- 从 CPA 面板自动获取 OpenAI OAuth 授权链接
- 自动打开 OpenAI 注册页并点击 `Sign up / Register`
- 自动填写邮箱与密码
- 支持自定义密码；留空时自动生成强密码
- 自动显示当前使用中的密码，便于后续保存
- 自动获取注册验证码与登录验证码
- 支持 `Hotmail`：继续使用 `邮箱 + 客户端 ID + 刷新令牌（refresh token）`，并可在远程服务与本地助手两种模式间切换
- 支持 `2925`：新增多账号池、自动登录登出、Step 4 / Step 8 命中“子邮箱已达上限邮箱”后的 24 小时禁用与自动切号
- 支持 `QQ Mail`、`163 Mail`、`163 VIP Mail`、`126 Mail`、`Inbucket mailbox`
- 支持从 DuckDuckGo Email Protection 自动生成新的 `@duck.com` 地址
- 支持基于 Cloudflare 自定义域名自动生成随机邮箱前缀
- Step 5 同时兼容两种页面：
  - 页面要求填写 `birthday`
  - 页面要求填写 `age`
- 支持 `Auto` 多轮运行
- 支持中途 `Stop`
- 支持通过日志区的 `记录` 按钮查看账号记录面板，同一轮的邮箱和手机号会合并显示，按最终状态、时间、失败标签和重试次数筛选
- 支持将账号记录完整快照同步到本地 helper，便于开发者直接查看 `data/account-run-history.json`
- Step 8 会自动寻找 OAuth 同意页的“继续”按钮，并通过 Chrome debugger 输入事件发起点击，然后监听本地回调地址


## 环境要求

- Chrome 浏览器
- 打开扩展开发者模式
- 你自己的 CPA 管理面板，且页面结构与当前脚本适配
- 至少准备一种验证码接收方式：
  - DuckDuckGo `@duck.com` + QQ / 163 / Inbucket 转发
  - Cloudflare 自定义域邮箱前缀 + QQ / 163 / Inbucket 转发
  - 手动填写一个可收信邮箱
- 如果使用 `QQ` / `163` / `163 VIP` / `126` / `Inbucket`，对应页面需要提前能正常打开

## 安装

1. 打开 `chrome://extensions/`
2. 开启“开发者模式”
3. 点击“加载已解压的扩展程序”
4. 选择本项目目录
5. 打开扩展侧边栏

## 2026-04-17 更新补充：Gmail / 2925 别名邮箱

本次版本对 `Gmail` 与 `2925 provide` 的注册邮箱逻辑做了统一整理：

- `Gmail` 与 `2925 provide` 现在都走同一套“别名邮箱”逻辑。
- 两者都不再使用“只填前缀再特殊拼接”的界面交互。
- 两者都要求先填写“基邮箱”：
  - `Gmail`：例如 `name@gmail.com`
  - `2925`（仅 provide 模式）：例如 `name@2925.com`
- 侧边栏里的“注册邮箱”输入框对这两种模式都已开放，可直接手动填写完整邮箱。
- 侧边栏里的 `获取 / 生成` 按钮对这两种模式也可用，行为与 Duck / Cloudflare 一样，都是“可自动生成，也可手动覆盖”。
- 当 `Mail = 2925` 且模式切到 `接收邮箱` 时，不再走别名基邮箱链路，而是回退到普通“邮箱生成 / 手动填写注册邮箱”路线，2925 只负责后续收信。

具体行为：

- `Gmail` 会基于完整基邮箱生成 `name+tag@gmail.com`
- `2925` 仅在 provide 模式下会基于完整基邮箱生成 `name123456@2925.com`
- 如果当前“注册邮箱”里已经是与当前基邮箱兼容的完整邮箱，流程会优先复用，不会强行重新生成

注意：

- `2925` 旧的“只填前缀”使用方式已经不再推荐，应该改为填写完整基邮箱
- 如果你手动填写了与当前 `Gmail / 2925 provide` 基邮箱不匹配的完整邮箱，侧边栏会在保存或执行 Step 3 时拦截

## 2026-04-23 更新补充：自定义邮箱池

本次版本新增 `自定义邮箱池` 生成方式，用于把一批已经准备好的邮箱按顺序分配给自动流程：

- 在 `邮箱生成` 中选择 `自定义邮箱池`
- 在新出现的 `邮箱池` 文本框里按“每行一个邮箱”填写
- `Auto` 运行次数会自动跟随邮箱池数量，无需再手动对齐轮数
- 同一目标轮次的失败重试会继续复用当前轮邮箱，不会提前跳到下一个
- 实际收码仍然走当前 `Mail` 对应的邮箱服务，因此应保证邮箱池里的地址与当前收码链路匹配

## 2026-04-23 更新补充：自定义邮箱服务号池

当 `Mail = 自定义邮箱` 时，现在也可以直接维护一组“自定义号池”：

- 在 `邮箱服务` 选择 `自定义邮箱`
- 在新出现的 `自定义号池` 文本框里按“每行一个邮箱”填写
- `Auto` 运行次数会自动跟随号池数量
- 只要当前邮箱还没成功认证、也没出现手机号验证，就会持续复用这个邮箱重试
- 只有成功认证，或明确出现 `add-phone / 手机号验证` 时，才会切换到号池中的下一个邮箱
- 这条链路只负责分配注册邮箱；第 `4 / 8` 步仍然保持手动输入验证码，不会改成自动轮询邮箱

## 快速开始

如果你只是想先跑通一套最稳的组合，建议直接按下面三种方案之一配置。

### 方案 A：`CPA + QQ / 163 / 163 VIP / 126`

1. `CPA` 填你的管理面板 OAuth 页面地址
2. `Mail` 选择 `QQ Mail`、`163 Mail`、`163 VIP Mail` 或 `126 Mail`
3. `邮箱生成` 选择 `DuckDuckGo`、`Cloudflare` 或 `自定义邮箱池`
4. 若你选择 `Cloudflare`，先按下文把 Cloudflare Email Routing 配好
5. 若你选择 `自定义邮箱池`，就在 `邮箱池` 中按行填入邮箱；否则点击 `获取` 生成邮箱，或手动粘贴一个你能收信的邮箱
6. 先单步验证 `Step 1 ~ Step 4`
7. 验证没问题后再点右上角 `Auto`

### 方案 B：`SUB2API + QQ / 163 / 163 VIP / 126`

1. `来源` 选择 `SUB2API`
2. 填好 `SUB2API` 地址、登录邮箱、登录密码、分组名
3. `Mail` 与 `邮箱生成` 的配置方式同方案 A
4. Step 1 会直接在 SUB2API 后台生成 OAuth 链接
5. Step 10 会把 localhost 回调提交回 SUB2API，并直接创建 OpenAI 账号

### 方案 C：`Codex2API + QQ / 163 / 163 VIP / 126`

1. `来源` 选择 `Codex2API`
2. 填好 `Codex2API` 后台地址、管理密钥
3. `Mail` 与 `邮箱生成` 的配置方式同方案 A
4. Step 7 会直接通过 Codex2API 协议 `/api/admin/oauth/generate-auth-url` 生成 OAuth 链接
5. Step 10 会把 localhost 回调中的 `code / state` 通过 `/api/admin/oauth/exchange-code` 直接提交给 Codex2API

### 方案 D：`Hotmail 账号池`

1. `Mail` 选择 `Hotmail`
2. 在 `Hotmail 账号池` 中添加 `邮箱 / Client ID / Refresh Token`
3. 先点 `校验`，再点 `测试收信`
4. 通过后再执行步骤或 `Auto`
5. 当前项目中，`Mail = Hotmail` 时会直接使用账号池里的邮箱作为注册邮箱，不再走 `Duck / Cloudflare` 自动生成

### 方案 E：`2925 账号池`

1. `Mail` 选择 `2925`
2. 在 `2925 账号池` 中添加 `邮箱 / 密码`
3. 先根据你的用途选择 `2925 模式`
   - `提供邮箱`：注册邮箱本身就是 2925 别名，会显示“别名基邮箱”输入
   - `接收邮箱`：注册邮箱回退到普通“邮箱生成 / 手动填