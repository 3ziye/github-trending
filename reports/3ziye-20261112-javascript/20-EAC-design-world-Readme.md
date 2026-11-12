<div align="center">

<img src="docs/assets/logo.jpg" alt="EAC design world 插件 Logo" width="112" height="112" />

# EAC design world

**让创作，自成世界。**

DeepSeek Harness 的本地视频制作与设计工作室

[![Release](https://img.shields.io/github/v/release/Ebony-Vinyl/EAC-design-world?include_prereleases&style=for-the-badge&color=227b70)](https://github.com/Ebony-Vinyl/EAC-design-world/releases)
[![License](https://img.shields.io/badge/license-AGPL--3.0-227b70?style=for-the-badge)](LICENSE)
[![Node](https://img.shields.io/badge/Node.js-22%2B-43853d?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/)
[![Stars](https://img.shields.io/github/stars/Ebony-Vinyl/EAC-design-world?style=for-the-badge&color=d77b66)](https://github.com/Ebony-Vinyl/EAC-design-world/stargazers)

[下载发布包](https://github.com/Ebony-Vinyl/EAC-design-world/releases) · [快速开始](#快速开始) · [功能一览](#功能一览) · [设计与架构](#设计与架构) · [问题反馈](https://github.com/Ebony-Vinyl/EAC-design-world/issues)

</div>

**把模板、素材、剪辑和设计工程连在一起，让 AI 与你共同完成一件可预览、可修订、可导出的作品。**

EAC design world 为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 提供原生创作模式、模板选择和右侧作品画布，同时拥有可独立运行的本地工作台。视频录制、配音、配乐、字幕、编码与检查产生真实文件；网站、幻灯片、SVG 和文档保留源文件及版本历史。

当前版本为 **v0.6.1 开发预览版**。本版修正时间线拖拽的素材入点累积、越界与拖拽后滚动等缺陷，并沿用 0.6.0 的参数化调色、变速运镜、网络素材与人工续剪工程导出，详见 [发布说明](docs/release-v0.6.1.md)。保留 150 个 Shotcraft 镜头、设计库、签名更新与回滚、草稿恢复和隔离预览。独立 MCP 入口支持 macOS 与 Windows，自动发现 Chrome / Edge；旁白支持 macOS say、Windows SAPI 和本地 GPT-SoVITS 曼波中文音色，桌面录制支持 Windows gdigrab 与 macOS avfoundation。模板数量代表可检索内容，不代表每个模板均可离线直接渲染。

<p align="center"><b>以下两条宣传片均为 deepseek harness + EAC design world + deepseek v4.1 flash（非 1017）一轮出的结果</b></p>

<p align="center"><b>AI 全程自己录制素材和制作音乐</b></p>

<p align="center"><b>EAC design world · RUSH 60s</b></p>

https://github.com/user-attachments/assets/3f6641e0-e803-48cf-b61a-2baa57f2c088

<p align="center"><b>Our Free Model · 65s</b></p>

https://github.com/user-attachments/assets/ca081273-1061-4656-a1b7-41d50af0aec7

顶部“音频模板”提供默认音色和曼波中文，可试听、设为默认，并将曼波模型下载到本机。本地曼波中文配音的安装、默认音色和验收方式见 [配音接入说明](docs/local-mambo-voice.md)。

## 目录

| 开始使用 | 创作能力 | 开发与来源 |
| :--- | :--- | :--- |
| [下载与安装](#下载与安装)<br />[环境要求](#环境要求)<br />[快速开始](#快速开始) | [功能一览](#功能一览)<br />[设计内容库](#设计内容库)<br />[AI 与 MCP](#ai-与-mcp) | [设计与架构](#设计与架构)<br />[开发与验证](#开发与验证)<br />[许可证与致谢](#许可证与致谢) |

## 功能一览

| 你想完成的工作 | 插件提供的能力 |
| --- | --- |
| 从对话开始创作 | 正常、剪辑、Design 三种模式；模板区独立铺开，选择状态不覆盖正文；重复点击或标签上的 × 可取消 |
| 找到合适的视觉风格 | 152 套设计体系与 517 个 OpenDesign 模板条目，另有原有 17 个视频选项；按类型搜索、分类和分页 |
| 浏览与挑选动效镜头 | Shotcraft 本地快照含 150 个镜头、10 类动效、59 个精选；可见视频预览、选片单、名单复制与下载、导入项目素材 |
| 录下真实产品 | Edge / Chrome 网页操作录制；Windows gdigrab 或 macOS avfoundation 桌面录制；原素材不被改写 |
| 编排实际镜头 | 多轨时间线；拖动片段移动、拖两端裁剪，也可直接输入开始时间、素材入点、时长、音量和轨道；带修订号保存 |
| 找网络风景素材与配乐 | `stock_search`/`stock-download`：Pexels、Pixabay（免费 API Key）、维基共享 Commons（免 Key）风景视频与 Jamendo CC 配乐；作者与许可随素材持久化 |
| 参数化调色与迭代 | 曲线（主/RGB）、HSL 二级、色相曲线、分区轮、静态局部蒙版与相机输入 LUT；全局色彩调整可导出 `.cube`，空间蒙版在原生渲染生效、续剪时需重建；`grade-preview` 对比帧、`scopes` 示波器与 `color_workflow` 调色版本/曝光匹配建议辅助 AI 迭代 |
| 卡点变速与运镜 | `beats` 节拍分析驱动音乐卡点剪辑；`clip.speed` 变速、`clip.motion` 数字运镜（推拉摇移）、片尾淡出/锐化/暗角；大时间线自动分块多 Pass 渲染防内存溢出 |
| 交付人工续剪 | 导出面板选择剪映草稿、Premiere/达芬奇 FCP7 XML、SRT 与 LUT；下载交接文件并保留人工修改的已有草稿；交换格式的效果保留以交接说明为准 |
| 处理语音与字幕 | 本地语音转录、去停顿初稿、SRT、时间线字幕与 ASS 烧录；转录需自行准备本地模型 |
| 完成声音与编码 | Windows SAPI 或 macOS `say` 旁白、本地确定性器乐、源音轨混音、H.264 输出与技术检查 |
| 制作图形动效 | `renderAt(t)` / `__seek(t)`、CSS 动画和 GSAP 时间线的确定性驱动与抽帧审查；可选接入 Motion Web 交互案例和 Onetake 函数库 |
| 创建网站和演示稿 | HTML、SVG、Markdown 编辑、隔离预览、不可变修订与源文件下载 |
| 检查与导出作品 | Harness 原生右侧作品画布、HTML 幻灯片分页、PDF / PNG / PPTX 整页图像导出 |
| 维护插件 | 顶部导航中的独立维护中心：运行/安装版本、签名更新、本地更新、备份回滚、宿主热重载、公告与已读记录 |

剪辑、调色和渲染由插件自身执行，不需要安装达芬奇或 Premiere。当前覆盖范围与尚未实现的能力见[专业能力说明](docs/professional-capabilities.md)，不宣称包含这两款软件的所有功能。

<p align="center"><img src="docs/assets/templates.png" alt="EAC design world 两行模板推荐与真实页面封面" width="960" /><br /><sub>按创作类型推荐模板，保留真实封面与可移除的选择标签。</sub></p>

### 设计内容库

从 [OpenDesign](https://github.com/nexu-io/open-design) 导入并建立本地索引的 **865 项内容**：

| 内容 | 数量 |
| --- | ---: |
| 设计体系 | 152 |
| 模板条目 | 517 |
| 创作技能 | 169 |
| 基础组件 | 13 |
| 场景 | 14 |

517 个模板条目包含 188 个示例、115 个设计模板、63 个视频模板、45 个图片模板、58 个视频提示词和 48 个图片提示词。部分来自同一视觉主题的不同上游目录，保留独立条目与来源。**205 项需要外部生成服务**；模板中的素材占位符或 HyperFrames 子合成依赖会单独标示。

<p align="center"><img src="docs/assets/design-systems.png" alt="设计体系的真实色板、字体与令牌" width="960" /></p>

### Shotcraft 镜头库

视觉模板页提供 Shotcraft 来源入口、分类与用途搜索、精选筛选和持久化选片单。预览只加载正在浏览的镜头，同时最多播放 3 个；离屏、切换到后台或打开详情时暂停。详情支持真实视频播放，以及可驱动 HTML 模板的播放、暂停、重播和时间进度。

在独立工作台创建项目后，可从选片单将 Shotcraft 镜头导入项目素材，继续使用时间线剪辑和视频导出。Harness 中仍通过模板选择附加当前创作参考，输入正文不受影响。

Shotcraft 的 124 张配方、React/TSX 实现及共享素材可以通过 `library_read` 和 `template_read` 读取。原始 TSX 需要在 Remotion 项目中注册或定制成 HTML 时间线，当前不直接交给 HTML 渲染器运行。导入、来源和复现步骤见 [Shotcraft 接入说明](docs/shotcraft-library.md)。

### 可选动效来源：Motion Web / Onetake

支持从已取得的本地仓库导入 [motion-web](https://github.com/feitangyuan/motion-web) 的 7 个交互案例及制作指南，以及 [onetake](https://github.com/feitangyuan/onetake) 的 OM 动效函数库与制作指南。模板统一进入搜索、源码读取和隔离预览；Onetake 示例可逐帧导出，Motion Web 实时页面可录制