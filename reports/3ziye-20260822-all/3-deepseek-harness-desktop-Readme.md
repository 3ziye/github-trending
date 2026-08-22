<h1 align="center">DSH Desktop</h1>

<p align="center">
  <strong>基于 DeepSeek Harness 构建的 Windows 和 macOS 开源桌面客户端。</strong><br>
  一键下载，开箱即用。<br>
  万物皆「插件」，桌面本身也是「插件」。
</p>

<p align="center"><sub>独立的社区开源项目，与深度求索不存在隶属、合作、授权或背书关系。<br>本仓库目前无深度求索员工或 DeepSeek Harness 上游官方团队成员参与；GitHub Contributors 中显示的上游贡献者来自 fork 继承和同步的提交历史。<br>中文 · <a href="README.en.md">English</a></sub></p>

<p align="center">
  <img src="assets/desktop-hero-zh.png" alt="DSH Desktop：基于 DeepSeek Harness 构建的开源桌面客户端" width="100%">
</p>

<p align="center">
  <a href="https://github.com/anywhere-labs/deepseek-harness-desktop/releases/latest"><img src="https://img.shields.io/github/v/release/anywhere-labs/deepseek-harness-desktop?style=flat&amp;label=release&amp;color=4D6BFE" alt="Latest release"></a>
  <a href="https://github.com/anywhere-labs/deepseek-harness-desktop/releases"><img src="https://img.shields.io/github/downloads/anywhere-labs/deepseek-harness-desktop/total?style=flat&amp;label=downloads&amp;color=4D6BFE" alt="Total downloads"></a>
  <a href="https://github.com/anywhere-labs/deepseek-harness-desktop"><img src="https://img.shields.io/github/stars/anywhere-labs/deepseek-harness-desktop?style=flat&amp;label=%E2%98%85&amp;color=08C" alt="GitHub stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2EA44F?style=flat" alt="MIT License"></a>
  <a href="https://discord.gg/TJeGqKRNM"><img src="https://img.shields.io/badge/Discord-5865F2?style=flat&amp;logo=discord&amp;logoColor=white" alt="Join Discord"></a>
  <img src="https://img.shields.io/badge/macOS%20%7C%20Windows-4493F8?style=flat-square" alt="Supported platforms: macOS and Windows">
</p>

<p align="center">
  <img src="assets/desktop-preview.png" alt="DSH Desktop 界面预览" width="100%">
</p>

DSH Desktop 将 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 的本地 Web UI、Host 服务和插件系统集成到原生桌面应用中。项目固定并原样运行特定上游版本；DSH Desktop 提供窗口、托盘、终端、更新和工作配置，并通过 DeepSeek Harness 提供的插件机制与上游能力组合。

<a id="run"></a>

## 下载与安装

当前正式安装包支持 Windows x64 和 macOS Universal。无需额外环境，下载安装，一键使用。

| 平台 | 下载 | 安装方式 |
| --- | --- | --- |
| Windows x64 | [下载安装程序](https://www.dshdesktop.cn/api/downloads/windows) | 运行 NSIS 安装程序并按提示完成安装 |
| macOS Universal | [下载 DMG](https://www.dshdesktop.cn/api/downloads/mac) | 打开 DMG，将 DSH Desktop 拖入 Applications |

详细步骤、插件命令和故障排查见[用户指南](docs/user-guide.md)与[常见问题](docs/faq.md)。

我们希望和所有插件作者一起，构建一个开放、可组合、可持续的 DSH 插件生态，让每个插件都能与其他插件共同进步：[DSH 插件生态倡议书](docs/plugin-ecosystem.md)。

## 文档

普通用户从[用户指南](docs/user-guide.md)开始即可；开发者文档只在需要扩展或维护时才需要阅读。

### 用户文档

| 目标 | 入口 |
| --- | --- |
| 安装和日常使用 | [用户指南](docs/user-guide.md) |
| 快速确认平台、环境和使用边界 | [常见问题](docs/faq.md) |
| 了解项目为什么存在 | [为什么做 DSH Desktop](docs/why-desktop.md) |
| 查看全部文档与 README 分工 | [文档索引](docs/README.md) |

### 开发者与维护者文档

| 目标 | 入口 |
| --- | --- |
| 阅读插件生态倡议书 | [插件生态倡议书](docs/plugin-ecosystem.md) |
| 编写普通或 Desktop 插件 | [插件开发](docs/plugin-development.md) |
| 参与统一插件 contract 讨论 | [DSH Community Fabric Draft](dsh-community-fabric/README.zh.md) |
| 了解统一插件框架为什么这样设计 | [成熟框架与真实插件调研](dsh-community-fabric/docs/research/mature-plugin-frameworks.zh.md) |
| 查看插件市场的产品与安全设计 | [DSH Community Market](dsh-community-market/README.zh.md) |
| 了解桌面插件可以使用的能力 | [桌面插件接口说明](dsh-plugin-desktop/docs/plugin-services.zh.md) |
| 了解桌面应用如何工作 | [架构说明](docs/architecture.md) |
| 查阅包级构建与发布细节 | [`dsh-plugin-desktop/README.md`](dsh-plugin-desktop/README.md) |

## 主要功能

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Desktop</h3>
      <p>把上游 DeepSeek Harness 的本地 Web UI 带到原生桌面。应用自动启动和管理本地 Harness 服务，集成系统托盘与桌面窗口，无需安装 Node.js 或执行命令。</p>
    </td>
    <td width="50%" valign="top">
      <h3>手机远程控制 <img src="https://img.shields.io/badge/%E5%8D%B3%E5%B0%86%E6%8E%A8%E5%87%BA-F59E0B?style=flat-square" alt="即将推出"></h3>
      <p>通过 iOS 和 Android 远程连接 Desktop，在手机上发起任务、查看 Agent 进度，并在需要时继续跟进。</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="dsh-community-market/README.zh.md">插件市场</a> <img src="https://img.shields.io/badge/%E5%B7%B2%E5%86%85%E7%BD%AE-2EA44F?style=flat-square" alt="已内置"></h3>
      <p>DSH Community Market 已完成并内置，提供插件发现、详情、安装与管理。市场以开放方式连接各种插件数据源：任何人都可以提供、接入和使用符合公开 Schema 的来源，已有 API 也可以通过受审 adapter 加入合作数据源。</p>
    </td>
    <td width="50%" valign="top">
      <h3>共建插件生态</h3>
      <p>DSH 的插件生态由社区共同建设。上游插件、DSH Desktop 插件和其他社区插件遵循统一的约定，可以通过相同的组合机制共同工作；欢迎加入共建，详见 <a href="docs/plugin-ecosystem.md">DSH 插件生态倡议书</a>。</p>
    </td>
  </tr>
</table>

## 插件生态

插件是给 DSH 添加能力的扩展包——模型、工具、界面、工作流都可以做成插件，像搭积木一样自由组合。

DSH Desktop 没有修改上游源码，也不是一个固定写死的外壳。固定版本的上游 DeepSeek Harness 原样运行；桌面壳本身——窗口、托盘、终端、更新、工作配置——作为 DSH 插件接入，并通过 DeepSeek Harness 提供的插件机制与上游能力组合进同一个运行时。从核心 agent 到桌面外壳，整个产品遵守同一条"一切皆插件"的规则：与所固定上游版本兼容的插件可以使用，桌面能力也按插件的方式组合、替换和演进。

我们希望插件生态像手机应用一样：每个插件按同一套规则开发，装在一起也能一起工作、互不干扰。

### 给开发者

与许多其他项目不同，这个项目本身就是一个 DSH [插件](docs/plugin-development.md)：桌面壳与第三方插件使用相同的插件组合机制。Desktop 的插件能力已经可以使用。我们提供了 Desktop 服务，让插件开发者能够把插件与桌面能力集成起来：例如查看和切换工作配置，或在当前配置中安装、更新和移除插件。完整用法见[桌面插件接口说明](dsh-plugin-desktop/docs/plugin-services.zh