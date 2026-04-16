# Multi-Page Automation

一个用于批量跑通 ChatGPT OAuth 注册/登录流程的 Chrome 扩展。

当前版本基于侧边栏控制，支持单步执行、整套自动执行、停止当前流程、保存常用配置，以及通过 DuckDuckGo / QQ / 163 / Inbucket / Hotmail 协助获取验证码。

## 插件效果

一百五十个号，一个401：

<table>
  <tr>
    <td align="center" width="50%">
      <img src="docs/images/交流群.jpg" alt="QQ交流群，便于大家交流" width="100%" />
    </td>
    <td align="center" width="50%">
      <img src="docs/images/十轮自动.png" alt="最新版本运行日志" width="100%" />
    </td>
  </tr>
</table>

## 打赏一下

佬们觉得好用的话，也可以打赏小弟一杯奶茶哦

<table>
  <tr>
    <td align="center" width="50%">
      <img src="docs/images/支付宝.jpg" alt="支付宝收款码" width="100%" />
    </td>
    <td align="center" width="50%">
      <img src="docs/images/微信.png" alt="微信收款码" width="100%" />
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
- 支持 `QQ Mail`、`163 Mail`、`Inbucket mailbox`
- 支持从 DuckDuckGo Email Protection 自动生成新的 `@duck.com` 地址
- 支持基于 Cloudflare 自定义域名自动生成随机邮箱前缀
- Step 5 同时兼容两种页面：
  - 页面要求填写 `birthday`
  - 页面要求填写 `age`
- 支持 `Auto` 多轮运行
- 支持中途 `Stop`
- Step 8 会自动寻找 OAuth 同意页的“继续”按钮，并通过 Chrome debugger 输入事件发起点击，然后监听本地回调地址


## 环境要求

- Chrome 浏览器
- 打开扩展开发者模式
- 你自己的 CPA 管理面板，且页面结构与当前脚本适配
- 至少准备一种验证码接收方式：
  - DuckDuckGo `@duck.com` + QQ / 163 / Inbucket 转发
  - Cloudflare 自定义域邮箱前缀 + QQ / 163 / Inbucket 转发
  - 手动填写一个可收信邮箱
- 如果使用 `QQ` / `163` / `Inbucket`，对应页面需要提前能正常打开

## 安装

1. 打开 `chrome://extensions/`
2. 开启“开发者模式”
3. 点击“加载已解压的扩展程序”
4. 选择本项目目录
5. 打开扩展侧边栏

## 快速开始

如果你只是想先跑通一套最稳的组合，建议直接按下面三种方案之一配置。

### 方案 A：`CPA + QQ / 163 / 163 VIP`

1. `CPA` 填你的管理面板 OAuth 页面地址
2. `Mail` 选择 `QQ Mail`、`163 Mail` 或 `163 VIP Mail`
3. `邮箱生成` 选择 `DuckDuckGo` 或 `Cloudflare`
4. 若你选择 `Cloudflare`，先按下文把 Cloudflare Email Routing 配好
5. 点击 `获取` 生成邮箱，或手动粘贴一个你能收信的邮箱
6. 先单步验证 `Step 1 ~ Step 4`
7. 验证没问题后再点右上角 `Auto`

### 方案 B：`SUB2API + QQ / 163 / 163 VIP`

1. `来源` 选择 `SUB2API`
2. 填好 `SUB2API` 地址、登录邮箱、登录密码、分组名
3. `Mail` 与 `邮箱生成` 的配置方式同方案 A
4. Step 1 会直接在 SUB2API 后台生成 OAuth 链接
5. Step 9 会把 localhost 回调提交回 SUB2API，并直接创建 OpenAI 账号

### 方案 C：`Hotmail 账号池`

1. `Mail` 选择 `Hotmail`
2. 在 `Hotmail 账号池` 中添加 `邮箱 / Client ID / Refresh Token`
3. 先点 `校验`，再点 `测试收信`
4. 通过后再执行步骤或 `Auto`
5. 当前项目中，`Mail = Hotmail` 时会直接使用账号池里的邮箱作为注册邮箱，不再走 `Duck / Cloudflare` 自动生成

## 侧边栏配置说明

### `CPA`

你的管理面板 OAuth 页面地址，例如：

```txt
http(s)://<your-host>/management.html#/oauth
```

Step 1 和 Step 9 都依赖这个地址。

### `Mail`

支持五种验证码来源：

- `Hotmail`
- `163 Mail`
- `163 VIP Mail`
- `QQ Mail`
- `Inbucket`

说明：

- `Hotmail` 通过侧边栏里的 Hotmail 账号池选择账号，可切换为远程服务模式或本地助手模式
- `QQ`、`163`、`163 VIP` 用于直接轮询网页邮箱
- `Inbucket` 通过你在侧边栏里配置的 host 访问 `mailbox` 页面：`https://<your-inbucket-host>/m/<mailbox>/`

### `Hotmail 账号池`

仅当 `Mail = Hotmail` 时使用。

可配置项：

- `接码模式`
- `远程服务地址`
- `本地助手地址`

每条账号支持保存：

- `email`
- `clientId`
- `refreshToken`
- 可选邮箱密码备注

使用方式：

- 先选择 Hotmail 接码模式
- 远程模式下填写你自己的远程服务地址
- 本地模式下填写本地助手地址（默认 `http://127.0.0.1:17373`）
- Windows 运行仓库根目录的 `start-hotmail-helper.bat`
- macOS 运行仓库根目录的 `start-hotmail-helper.command`
- 本地 helper 当前仅依赖 Python 标准库，无需额外安装第三方 Python 包
- 再新增账号
- 点击 `校验`
- 校验通过后，可点击 `测试收信`
- Auto 模式每轮会自动选用一个可用账号

#### 本地 helper 启动命令

Windows：

```powershell
.\start-hotmail-helper.bat
```

macOS：

```bash
chmod +x ./start-hotmail-helper.command
./start-hotmail-helper.command
```

如果你不想走启动脚本，也可以直接运行 Python 程序本体：

```bash
python scripts/hotmail_helper.py
```

如果你的环境里命令是 `python3`：

```bash
python3 scripts/hotmail_helper.py
```

#### 启动成功标志

本地 helper 启动成功后，终端会输出：

```text
Hotmail helper listening on http://127.0.0.1:17373
```

看到这行再回到扩展里点 `校验` 或 `复制最新验证码`。

#### 最小排错说明

- 如果提示 `Python 3 not found`，先安装 Python 3.10+
- 如果 helper 已启动但扩展仍报连接失败，先确认模式切到了 `本地助手`
- 确认本地助手地址与终端输出一致，默认应为 `http://127.0.0.1:17373`
- 如果地址一致仍失败，再检查是否有端口占用或终端里是否已经抛出异常

### `Mailbox`

仅当 `Mail = Inbucket` 时显示。

填写 Inbucket mailbox 名称，例如：

```txt
tmp-mailbox
```

脚本会自动打开：

```txt
https://<your-inbucket-host>/m/<mailbox>/
```

并且只检索未读邮件：

- 只匹配 `.message-list-entry.unseen`
- 第 2 次轮询开始会自动点击 mailbox 页面上的刷新按钮
- 识别到验证码后会尝试删除当前邮件，减少重复命中

### `Inbucket`

仅当 `Mail = Inbucket` 时显示。

这里填写 Inbucket host，支持两种格式：

- `your-inbucket-host`
- `https://your-inbucket-host`

脚本会自动规范化成 ori