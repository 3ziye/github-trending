<p align="center">
  <img src="app-icon.svg" width="88" height="88" alt="HGhub 图标" />
</p>

<h1 align="center">HGhub</h1>

<p align="center">一个通过插件连接内容的通用视频播放器。</p>

<p align="center">
  <a href="#开始使用">开始使用</a> ·
  <a href="https://minireel.github.io/HGhub/">在线文档</a> ·
  <a href="docs/developers/index.md">插件开发</a> ·
  <a href="docs/DEVELOPMENT.md">参与开发</a> ·
  <a href="https://github.com/Minireel/HGhub/issues">反馈问题</a>
</p>

HGhub 将浏览、搜索、播放和个人片库放在同一个应用中。通过导入 JavaScript 插件，你可以接入不同内容来源，并使用统一的界面观看与管理内容。

**应用不内置内容源，不分发第三方插件，也不提供官方源列表。** 首次使用需自行导入插件，无需注册 HGhub 账号；来源要求登录时，由对应插件提供登录入口。

## 核心体验

- **沉浸式播放**：桌面与移动端界面，配合手势和播放控制，在面板中查看详情、选集与评论。
- **多来源浏览与搜索**：推荐、分类筛选和聚合搜索，支持按来源查看结果，并保留本地搜索历史。
- **灵活的播放选择**：支持 HLS 与普通视频，切换线路、清晰度和解析器，也可搜索其他来源继续观看。
- **自己的片库**：管理本地收藏、观看历史与续播进度；支持追更，以及将插件提供的云端列表导入本地收藏。
- **按需扩展**：通过文件、网址或插件列表导入内容源与解析器，检查更新，并在更新失败时恢复上一可用版本。
- **更多内容形式**：除点播外，还可通过插件接入直播、信息流和图文内容。

具体内容、账号、评论与互动能力取决于所安装的插件。

## 开始使用

插件版处于早期开发阶段，目前可[从源码运行或构建](docs/DEVELOPMENT.md)。当前重点完善 Windows 与 Android，其他平台仍在适配和验证；详见[支持状态](docs/developers/status.md)。

1. 打开 **插件中心 → 导入与订阅**。移动端从“我的”进入插件中心。
2. 选择插件文件、粘贴代码，或输入插件／列表网址；确认安装并启用。
3. 从首页、搜索或分类找到内容，开始播放。需要切换首页来源时，可在设置中选择。

HGhub 维护播放器与插件接口，第三方内容的可用性由相应来源决定。

## 文档

**[打开在线文档站 →](https://minireel.github.io/HGhub/)**

| 我想…… | 从这里开始 |
| --- | --- |
| 制作一个内容源或解析器插件 | [插件开发教程](docs/developers/index.md) |
| 了解插件文件、宿主 API 与内容模型 | [HPP 插件协议](docs/plugin-protocol/README.md) |
| 让 Agent 协助开发插件 | [Agent 开发指南](docs/developers/agent.md) |
| 修改客户端或自行构建 | [客户端开发指南](docs/DEVELOPMENT.md) |
| 查看已支持与待完善的能力 | [支持状态](docs/developers/status.md) |

客户端使用 **Rust · Tauri 2 · React · TypeScript** 构建。HPP 插件协议仍在演进，编写插件前请阅读当前支持状态。

## 参与、交流、贡献

欢迎通过 [Issues](https://github.com/Minireel/HGhub/issues) 反馈问题、提出想法，或提交 [Pull Request](https://github.com/Minireel/HGhub/pulls) 参与改进。报告问题时，请附上应用版本、操作系统和复现步骤。

项目本身由我独立维护，维护者会根据时间与精力处理反馈，不承诺第三方插件或站点持续可用。维护范围与权益反馈方式见[项目声明](docs/PROJECT_POLICY.md)。

HGhub 欢迎您的贡献，任何一个协议都需要大量、长久的踩坑、试错、经验总结，使它变的越来越完善。您的任何 Issues 与 PR 都对 HGhub 帮助良多！

社区交流：[Linux.DO](https://linux.do/)。

## 许可证与非商业立场

本项目源码公开，采用 [PolyForm Noncommercial 1.0.0](LICENSE)。**禁止商业用途**，包括销售、广告变现、卡密、VIP、付费解锁，以及作为收费产品或服务的一部分使用；具体以许可证全文为准。

维护者**不提供商业授权，不接受广告、推广或商务合作**，也未授权任何人以本项目名义收费。社区技术贡献与问题反馈不属于商务合作。

项目不运营内容托管服务，与外部内容提供者无官方隶属或背书关系。完整责任边界、维护政策与权益反馈说明见[项目声明](docs/PROJECT_POLICY.md)。
