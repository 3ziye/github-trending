<h1><img src="docs/images/workdaddy-app-icon-rounded.svg" alt="" width="40" height="40" align="absmiddle">&nbsp; WorkDaddy</h1>

**语言：** [简体中文](README.md) · [English](README_en.md)

> **WorkDaddy 是 WorkBuddy 桌面端增强助手：多账号独立备份、点切即用；免打扰模式让 AI 无人值守跑长任务；跨账号会话迁移、异常中断自动续接；自动化任务按事件或定时执行；暂存/快捷提示词；毛玻璃主题与更多实用功能，账号与配置全部留在本机。**
> 本机回环 CDP 注入 · 不改官方安装包。

一个基于 **Chrome DevTools Protocol (CDP)** 的 [WorkBuddy](https://www.workbuddy.cn/)、[WorkBuddy AI](https://www.workbuddy.ai/) 桌面端增强工具。
零侵入、零重签名——只把界面组件注入到正在运行的 WorkBuddy 渲染进程里。

![License](https://img.shields.io/badge/license-AGPL--3.0-blueviolet)
![Platform](https://img.shields.io/badge/platform-macOS%2011%2B%20%7C%20Windows%2010%2F11-lightgrey)
![Node](https://img.shields.io/badge/node-%E2%89%A518-green)

---

## 演示

<img src="docs/images/accounts-light.jpg" width="600">
<img src="docs/images/accounts-dark.jpg" width="600">

![界面预览图](docs/images/pannel-enhance.png)
![界面预览图](docs/images/pannel-robot.png)
![界面预览图](docs/images/pannel-theme.png)

---

## 它能做什么

- **方便切换账号**：每个 WorkBuddy 账号独立备份，点一下就切，再也不用每次扫码。
- **无感登录新账号**：「登录新账号」支持免退出 OAuth 授权——不退出 WorkBuddy，在浏览器完成扫码后新账号自动加入列表；也可选传统的「假退出」方式回登录页扫码。
- **账号导入导出**：把全部账号备份加密导出，在另一台电脑安装 WorkDaddy 后一键导入，方便电脑之间迁移账号。
- **自动领每日积分**：由自动化任务管理多账号每日签到，默认停用。首次打开面板会提示账号风险，选择开启后启用任务；开启或取消的选择保存在本机，之后不再提醒，可随时在「自动化」中手动启停。
- **Token 和积分用量统计页面**：按天查看 Token 与积分消耗，支持按账号筛选，并显示模型和账号用量排行。
- **积分不足时的账号切换建议**：当前账号积分不足时提示可用账号，方便继续工作。
- **自动化任务**：用自然语言让 WorkBuddy 创建任务，或自行编辑步骤；支持手动、事件和定时触发，以及运行日志、停止任务和 JSON / ZIP 导入导出。
- **权限弹窗免打扰**：真正的零决策弹窗弹出，可以放心开启任务后睡觉。
- **暂存提示词**：输入框边上一键把草稿「暂存」到待发送队列——图片 / 文件 / 引用原样保留，择机发送。
- **切换精美主题**：内置毛玻璃官方主题，多套预设壁纸，支持自定义壁纸。
- **账号间会话迁移**：自动或手动跨账号复制会话，跨账号继续接龙。
- **模型切换更便捷**：解决 WorkBuddy 不支持添加多个同名模型的问题。
- **防止电脑休眠**：睡前任务未完成，开启休眠模式，任务结束后自动切换成允许休眠。
- **异常中断会话自动继续**：AI 回复因网络波动、超时等原因中断时，自动让异常中断任务继续执行。
- **快捷短语**：常用语存进面板，输入框操作栏一键点发；

---

## 安装

> - 国内版 [WorkBuddy](https://www.workbuddy.cn/) 请下载 `WorkDaddy` 安装包
> - 国际版 [WorkBuddy AI](https://www.workbuddy.ai/) 请下载 `WorkDaddy AI` 安装包

### macOS

1. 在 [Releases](../../releases) 下载最新 `WorkDaddy-x.y.z.dmg`

2. 打开 dmg，把 `WorkDaddy.app` 拖进 **应用程序** 文件夹

3. 第一次打开如果遇到「无法打开，因为 Apple 无法检查恶意软件」：

   1. 打开「系统设置 → 隐私与安全性」
   2. 在「WorkDaddy 已被阻止」处点 **仍要打开**
   3. 输入开机密码确认
      ![安装引导](docs/images/install-guide.png)

4. 双击 `WorkDaddy.app` 启动：它会自带守护进程并把组件注入到 WorkBuddy

5. 看到机器人按钮？**搞定**。

#### 企业专享版 / VPC 客户端

macOS 会自动扫描带 `WorkBuddy` 前缀且包含 `Contents/MacOS/Electron` 的客户端（例如 `WorkBuddy企业定制版.app`），并按 WorkDaddy/WorkDaddy AI profile 排除另一端。发现多个候选时会弹出系统选择窗口，选中后自动记住，不需要手动寻找配置文件。完全自定义名称也可以在源码目录执行下面的高级配置命令：

```bash
node scripts/workbuddy-target.js --configure --platform darwin \
  --profile workbuddy-cn \
  --binary "/Applications/企业客户端.app/Contents/MacOS/Electron" \
  --data-dir "$HOME/Library/Application Support/WorkDaddy"
```

### Windows

1. 在 [Releases](../../releases) 下载对应客户端的 `WorkDaddy-Setup-x.y.z.exe` 或 `WorkDaddy-AI-Setup-x.y.z.exe`
2. 双击安装器完成安装
3. 双击打开 `WorkDaddy` 或 `WorkDaddy AI` 桌面快捷方式

#### 企业专享版 / VPC 客户端

企业专享版用户仍安装与界面最接近的 `WorkDaddy` 或 `WorkDaddy AI`。安装程序会先自动识别对应的官方客户端，并在安装向导中显示路径和版本；企业版用户点击「浏览」改选自己的 `.exe` 主程序即可，不需要修改配置文件或设置系统环境变量。

选择结果保存在 WorkDaddy 的个人数据目录中。更新安装默认保留上次选择，也可以在安装向导中修改；需要改回官方客户端时，重新运行安装程序并选择自动识别出的官方 `.exe`。WorkDaddy 会锁定所选客户端版本，客户端升级或移动后同样通过安装程序重新确认。

### 从源码运行（开发者）

```bash
git clone https://github.com/babygoton/WorkDaddy.git
cd WorkDaddy
bash scripts/install.sh        # 创建备份目录 + 启动守护进程
bash scripts/relaunch-with-cdp.sh   # 把 WorkBuddy 切换到调试模式（端口 9222）
```

WorkBuddy 国内版和 WorkBuddy AI 使用同一套 daemon，通过 profile 绑定客户端，不靠“第一个 CDP 端口”猜测目标：

```bash
WBSWITCH_PROFILE=workbuddy-cn bash scripts/relaunch-with-cdp.sh
WBSWITCH_PROFILE=workbuddy-ai bash scripts/relaunch-with-cdp.sh
```

暂存提示词和主题功能在两个 WorkBuddy profile 开启。CodeBuddy profile 的适配暂缓，不进入当前发布包。

当前发布脚本只打包两个 WorkBuddy 客户端，共 4 个包：`WorkDaddy-<version>.dmg`、`WorkDaddy-AI-<version>.dmg`、`WorkDaddy-Setup-<version>.exe`、`WorkDaddy-AI-Setup-<version>.exe`。macOS 构建时传 `WORKDADDY_BUILD_PROFILE=workbuddy-cn` 或 `workbuddy-ai` 可单独重打一个客户端。Windows ZIP 仅作安装器构建的临时输入，不作为发布包。

`install.sh` 做了：

- 创建 `~/Library/Application Support/WorkDaddy` 备份目录
- 首次启动自动兼容迁移旧版 `~/Library/Application Support/HelloBuddy/accounts` 账号备份（旧目录保留不删除）
- 首次备份当前 WorkBuddy 账号
- 清理旧 launchd 注册并手动启动守护进程（不再登录自启）
- 立即启动后台守护进程
- 打开管理界面 `http://127.0.0.1:47832`

> 守护进程会在安装结束时手动启动；需要使用时手动启动对应的 WorkDaddy 端即可。

---

## 原理

**CDP 注入 · 不改官方安装包**

```
┌─────────────┐  --remote-debugging-port=9222  ┌──────────────┐
│  WorkBuddy  │ <───────────────────────────> │  WorkDaddy   │
│  (Electron) │       Chrome DevTools          │   daemon.js  │
│             │        Protocol (CDP)          │              │
│  渲染进程    │  ←── Runtime.evaluate ────     │  HTTP :47832 │
│  右下角     │      注入 inject.js            │  本地 API    │
└─────────────┘                                └──────────────┘
```

1. **不修改 WorkBuddy 二进制**：用 `launcher` 启动 WorkBuddy 时多带一个 `--remote-debugging-port=9222` 参数，**二进制与签名原封不动**。
2. **守护进程通过 CDP 连接 WorkBuddy**：监听登录/认证网络事件 + 文件监听兜底，每次登录/刷新令牌都把当前登录信息按 `account.uid` 备份到稳定目录。
3. **注入界面