<div align="center">

<h1>Claude Cage</h1>

**把 Claude 大小姐关起来，为了更好地保护我们的相遇**

<img src="assets/claude-cage-character.png" alt="Claude Cage" width="320" />

[![Release](https://img.shields.io/github/v/release/Lee-xeo/Claude-Cage?include_prereleases)](https://github.com/Lee-xeo/Claude-Cage/releases) [![MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

<a href="https://trendshift.io/repositories/339051#achievements"><img src="https://trendshift.io/api/badge/trendshift/repositories/339051/daily?language=Go" alt="Trendshift — Go Repository of the Day" width="250" height="55" /></a> <a href="https://trendshift.io/repositories/339051#achievements"><img src="https://trendshift.io/api/badge/trendshift/repositories/339051/weekly?language=Go" alt="Trendshift — Go Repository of the Week" width="250" height="55" /></a>

<a href="https://trendshift.io/repositories/339051#achievements"><img src="https://trendshift.io/api/badge/trendshift/repositories/339051/daily" alt="Trendshift — Repository of the Day" width="250" height="55" /></a> <a href="https://trendshift.io/repositories/339051#achievements"><img src="https://trendshift.io/api/badge/trendshift/repositories/339051/weekly" alt="Trendshift — Repository of the Week" width="250" height="55" /></a>

**[项目主页](https://claude-cage.com/) · [下载应用](https://claude-cage.com/#download) · [插件市场](https://claude-cage.com/plugins/) · [使用文档](https://claude-cage.com/docs/) · [常见问题](https://claude-cage.com/docs/troubleshooting/)**

[简体中文](README.md) · [繁體中文](README.zh-TW.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [فارسی](README.fa.md) · [한국어](README.ko.md) · [Español](README.es.md) · [မြန်မာဘာသာ](README.my.md) · [Беларуская](README.be.md) · [پښتو](README.ps.md) · [دری](README.prs.md) · [አማርኛ](README.am.md) · [Soomaali](README.so.md) · [ትግርኛ](README.ti.md) · [Français](README.fr.md)

</div>

## 设计理念

1. **Claude 本身是安全的，但它的运行外壳（harness）及相关程序不是**——包括 Claude Code、Claude Desktop，以及浏览器里接触到的邮件、网页与环境信号。
2. **想要在保证安全的前提下使用 Claude 的能力，通常有两条路线：反向代理，或者远程控制**——要么把 Claude 从远端服务器拉出来直接运行在主机上，要么把 Claude 部署在受控环境里，由它远程操作主机。我们认为后者更安全，也更合规。
3. **因此，Cage 的核心思想是：为 Claude 及相关程序打造一个轻量化的本地隔离环境，再通过标准 MCP 插件，让 Claude 安全、受控地使用本机能力**——每一次越出环境的调用都有明确的权限边界与用户确认，比直接暴露 SSH 更安全。

这样一来，Cage 同时实现了三个目标：

- **把危险的部分关起来，把有用的能力放出来。** Claude 大小姐安心待在 Cage 里，坐在她的小螃蟹上，只需把手伸出来处理外面的工作——不必在 Cage 里重新搭一整间办公室。
- **通过插件市场，与开源社区解耦协作。** 我们开放了[插件市场（cage-plugins）](https://github.com/Lee-xeo/cage-plugins)：**插件 = MCP + 扩展**，分别对应「给 Claude 的能力」与「Cage 工作台的定制化」。开源社区可以在插件市场持续贡献工具、桌面控制与工作流扩展，而不必挤进 Cage 主仓库的 Issue 列表；Cage 核心维护团队也能更聚焦于隔离环境、网络与工作台本身的打磨。
- **合规、安全、轻量化、本地、低成本，一键安装、一键配置、开箱即用。** 我们不再需要维护复杂臃肿的多系统客机，不再担心 Claude 的能力被困在孤岛里，也无需承担高昂的云端成本或数据安全隐患——在自己电脑上就能优雅地实现这一切。

## 受够了 Anthropic

作为一个只是想和 Claude 对话与合作的正常用户，受够了折腾各种 VPS，指纹浏览器，环境检测，面对封号的担惊受怕和财产损失。我们提出 **Claude Cage** 项目：**一个开箱即用的桌面程序，配置好自己的网络代理，集中管理轻量化隔离环境、时区语言、环境检查与插件能力。**

Claude Cage 在一个小型的 Debian 13 环境里运行官方 Claude Code 和 Claude Desktop，macOS、Windows 和 Linux 上都是同一个环境。终端、浏览器、编辑器、官方 Claude Desktop 与插件市场汇集在同一个工作台，项目按需共享，网络独立管理；既可以通过插件安全调用本机能力，也可以连接自己的服务器，或用手机接续电脑上的任务。支持以下几个重点功能：

- 和主机隔离的网络设置，Cage 自己接管和代理内部的所有网络流量
- 和主机隔离的指纹设置，包括时区、语言等，支持自动与代理 IP 同步
- 针对 Claude 使用过程中的全链路适配（浏览器登录，授权，claude code 进程）
- 内置网络与隔离检查，关键检查失败或证据不完整时暂停外网；社区和第三方检测提供补充参考

**使用 Cage 的环境检测结果：**

| 网络与隔离检查 | 浏览器环境检测（社区参考） |
| :---: | :---: |
| <a href="assets/network-checks.png"><img src="assets/network-checks.png" alt="网络与隔离检查" width="400" /></a> | <a href="assets/community-browser-check.png"><img src="assets/community-browser-check-cropped.png" alt="浏览器环境检测（社区参考）" width="400" /></a> |

[FuckClaude](https://fuck-claude.vercel.app/) · [LinXiaoTao / GitHub](https://github.com/LinXiaoTao/FuckClaude)

**Cage 运行主界面：**

![Cage](www/public/workbench-2026-11.jpg)

## 你可以用它做什么

- **在本机终端使用 Claude Code（v0.2.2 功能）。** `cage login` 打开 Cage 浏览器，供你登录 Claude 账号。在项目目录输入 `cage claude` 即可共享当前文件夹并用默认账号打开会话，支持 Claude Code 原生参数和管道。要只在这次调用使用名为 `sarah` 的账号，输入 `cage sarah`。单独输入 `cage` 可查看帮助。`cage start` 可提前在后台启动 Cage 服务和本机虚拟机，等环境就绪后返回。`cage up` 打开或唤回桌面工作台。用 `cage update` 可直接在终端升级 Cage。v0.2.2 的 npm 包发布后，也可用 `npm install -g claude-cage` 安装。 [终端命令与示例](docs/guide/workbench.md#在本机终端使用-claude-code)
- **在一个窗口里完成工作。** 用终端运行 Claude Code，用编辑器查看改动，用 Cage 浏览器预览服务和完成登录。
- **通过插件市场解锁全部能力。** 内置开放的[插件市场（cage-plugins）](https://github.com/Lee-xeo/cage-plugins)，插件 = MCP + 扩展：既能让环境里的 Claude 通过标准 MCP 安全、受控地使用本机能力（如桌面键鼠控制、Office 文档、Blender、命令行工具等），也能通过沙箱页面定制 Cage 工作台。主机插件默认受权限声明与弹窗确认保护。 [插件与插件市场](docs/guide/plugins.md) · [开发规范](docs/plugins.md)
- **三个平台，同一个轻量化环境。** macOS、Windows 和 Linux 上的 Cage 都运行同一个轻量化 Debian 13 环境，无需维护复杂的多系统客机，工具与操作方式一致。 [Debian 环境](docs/guide/guest-systems.md)
- **控制共享范围。** 只共享默认工作区和明确打开的项目文件夹；主机的 Claude 登录、浏览器配置和 SSH 密钥不会自动导入。
- **看清网络状态。** 内置代理管理支持导入订阅、选择节点和检查出口。关键检查未通过时，环境保持离线；代理不可用时没有直连回退。
- **下次继续使用。** 工具、文件和登录状态保存在虚拟磁盘里，关闭窗口可以保留后台任务。
- **管理多个 Claude Code 订阅。** 查看额度、为新会话分配账号，并在明确授权后切换账号接续历史。 [Claude Code](docs/guide/accounts.md)
- **从手机继续处理任务。** Android / iPhone 配对电脑，接续 Claude Code 对话与工具审批，或操作远程浏览器和 Claude Desktop。 [手机连接