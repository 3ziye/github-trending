# AI 角色参考与合成工作台 · 中文版（3合1）

> **姿势库（1,439 张素体白模 + 1,439 张深度图 Depth） + 服装库（3,224 套：ギア写实 1,407 + Shisei 中国历代 57 套/227 视角 + ギア动漫 1,320 + CharaDB 二次元 440） + 人像库（1,499 位） = 6,162 条全中文参考数据 / 12,022 张本地高清图，另有 1,760 张来源站点参考图**，集成 **5 大 AI 图像协议直连工作台** 与 **原生 ComfyUI 自定义节点插件（`custom_nodes`）**。

![画廊总览预览](docs/preview.jpg)

![AI 角色合成台预览](docs/studio.jpg)

<details><summary>手机端预览</summary>

![手机端预览](docs/mobile.jpg)

</details>

**在线演示：** <https://ai-pose-gallery.anhao.app/>
**原始站点：**
- 姿势库（白模）：<https://ai-pose-gallery.pages.dev/>
- 姿势深度图库（Depth）：<https://ai-pose-depth-gallery.pages.dev/>
- 服装库：<https://ai-costume-gallery.pages.dev/>
- 人像库：<https://ai-portrait-gallery.pages.dev/>

**原有图库作者：** ギア（@giaaibusi）；二次元服装作者：たき AI（[@taki_auto](https://x.com/taki_auto) · [CharaDB](https://charadb-2fi.pages.dev/)）。
**中文版维护：** Anhao · [X @anhao_ai](https://x.com/anhao_ai)
**GitHub：** <https://github.com/anhao/ai-pose-gallery-zh>

> ⚠️ **免责声明（必读）**：
> 1. **学习与创作限定**：本项目及配套插件/工作流**仅供个人学习、人体动态研究、合法艺术创作与技术交流使用**，严禁用于任何违反法律法规、生成违法违规/淫秽色情内容或侵害他人合法权益（如未经授权的真人肖像换脸）的用途。
> 2. **NSFW 敏感内容提示**：图库包含部分 18+ 成人向人体素体姿势与内衣/性感穿搭参考，系统默认开启「安全模式 (SFW)」隐藏，**未成年人严禁解锁或访问**。
> 3. **来源与版权声明**：原有姿势、现实服装、人像参考图源自原作者 **ギア（@giaaibusi）** 公开站点；440 套二次元服装源自 **たき AI（@taki_auto）** 的 [CharaDB](https://charadb-2fi.pages.dev/)（详见其 [LICENSE](https://github.com/taki-ttt/charadb/blob/main/LICENSE)），版权归各自原作者所有；本仓库仅为中文翻译整理与工程学习存档，禁止将图库图片打包倒卖。使用者因违规使用产生的一切法律责任由使用者本人独立承担。

---

## 这是什么

原站是ギア（@giaaibusi）发布的三大 AI 绘画参考图库（姿势、服装、人像），元数据全部为日文，且分散在三个独立站点。本仓库（v2.0）完成了**三站合一、全量中文化、AI 角色合成工作台与 ComfyUI 原生插件升级**：

1. **三库四站全量本地镜像（11,568 张图）** —— 完整收录姿势库（素体白模 2,878 张 + 深度图 Depth 2,878 张 WebP）、服装库（2,814 张 WebP）、人像库（2,998 张，全尺寸 `1600×2000` 高清 WebP）的全部缩略图与高清原图，支持纯离线浏览与静态托管。
2. **原有图库全中文元数据** —— 动作体系、姿势分类、服装款式、穿搭标签、人像分区、发长与 51 种细分发型全部译为地道中文，自动组装的生图提示词纯净无日文干扰。
3. **三合一 AI 角色合成工作台（Web Studio）** —— 基于 **React 19 + Tailwind CSS 4 + TypeScript 7 + shadcn/ui + TanStack Router** 构建的响应式多页面应用（兼容 PC / 平板 / 手机）：
   - 从三大图库任意挑选 **人像 + 服装 + 姿势（支持素体白模 / 深度图一键切换）** 组合配方，或一键随机捏人；
   - 支持拖拽、剪贴板粘贴（`Cmd+V` / `Ctrl+V`）或 URL 添加多张自定义附加参考图；
   - 内置 **5 大 AI 图像协议直连**（Google Gemini、OpenAI GPT Image、阿里云百炼 Qwen、字节火山方舟 Doubao、**本地 ComfyUI**），生成记录通过 **IndexedDB** 本地持久化保存。
4. **原生 ComfyUI 自定义节点插件（`custom_nodes`）** —— 本仓库同时是一个即插即用的 ComfyUI 插件！直接 `git clone` 到 `ComfyUI/custom_nodes/` 即可在 ComfyUI 画布内使用 **姿势 / 服装 / 人像 / 三合一角色配方** 4 个自定义节点（姿势与配方节点内置 `use_depth` 深度图切换，可直接接入 ControlNet Depth）与内置的 **6,162 条中文可视化弹窗选图器**。

---

## 核心功能

### 1. 三大参考图库（姿势 / 服装 / 人像）
- **姿势参考库（`/poses`）**：4 大体系（全身单人・标准系 / 全身单人・性感系 / 上半身单人 / 双人缠绵）、26 个动作分类、288 组姿势、5 种视角（正面 / 斜前 / 侧面 / 背面 / 俯视），支持**按姿势分组 / 逐张浏览**双模式、卡片内多角度切换，以及 **`[ 素体白模 | 深度图 (Depth) ]` 一键切换预览与下载**。
- **服装参考库（`/costumes`）**：8 大穿搭分类（春季 / 夏季 / 秋季 / 冬季 / 内衣・睡衣 / 性感穿搭 / 泳装・度假 / 派对・礼服）、86 个中文细节标签与英文 Prompt 关键词。
- **人像参考库（`/portraits`）**：2 大分区（正脸参考 893 / 造型氛围 606）、4 种发长（短发 / 中发 / 中长发 / 长发）、51 种细分发型，支持**精选题集**与**热门榜单**一键筛选。
- **统一交互体验**：中文关键词实时检索、灯箱高清原图预览与下载、一键「加入合成配方」。

### 2. AI 角色合成台（`/studio`）
- **3+N 参考图组合**：3 个核心槽位（人像 / 服装 / 姿势，姿势槽位内置 `[ 白模 | 深度 ]` 实时切换）+ 任意张自定义附加参考图（点击上传、拖拽文件、剪贴板粘贴、填写图片 URL）。
- **参考拼图预览与导出**：弹窗查看三合一高清参考拼图（`1800×1200` Canvas 实时合成），支持一键下载拼图 PNG。
- **12 种画风预设 & 纯中文结构化提示词**：内置「无预设（跟随参考图）」、写实人像写真、日韩杂志画报、复古胶片写真、2.5D 游戏原画立绘、日系二次元插画、新海诚感动画电影、日式黑白漫画网点、3D 次世代角色渲染、3D 潮玩手办质感、赛博朋克霓虹、角色设定集立绘（纯白底）共 12 种画风，根据已选素材自动组装提示词。
- **5 大 AI 图像协议与高级参数**：
  - **Google Gemini**：`gemini-3.1-flash-image-preview`、`gemini-3-pro-image-preview`、`gemini-2.5-flash-image`（支持宽高比 `aspectRatio`、分辨率 `1K/2K/4K`）
  - **OpenAI GPT Image**：`gpt-image-2.5`、`gpt-image-2`、`gpt-image-1.5`、`gpt-image-1`（支持 `/v1/images/edits` JSON URL 直传 / Multipart 上传、尺寸、质量、背景透明度）
  - **阿里云百炼 Qwen**：`qwen-image-3.0-pro`、`qwen-image-2.1-pro`、`qwen-image-2.0-pro`、`qwen-image-edit-plus`（支持 `multimodal-generation` 多图参考输入、智能改写 `prompt_extend`、水印开关）
  - **字节火山方舟 Doubao**：`doubao-seedream-5-0`、`doubao-seedream-4-5-251128`、`doubao-seedream-4-0-250828`、`doubao-seededit-3-0-i2i-250628`（支持多图融合 `image: [...]`、2K/4K 分辨率）
  - **本地 ComfyUI 工作流引擎**：支持自动将三合一拼图及单张人像/服装/姿势图上传至本地 ComfyUI（`/upload/image`），注入自定义 API 工作流占位符或自动识别节点提交 `/prompt` 队列并轮询取回成品图；支持导入/导出通用 `.api.json` 工作流模板。
- **跨页面后台生图 & IndexedDB 历史记录**：切换页面不会中断正在进行的生图请求；生成结果自动存入浏览器 IndexedDB（避免 `localStorage` 容量限制），支持复用提示词与原图下载。

> 本地 ComfyUI 三图合成（Qwen Image Edit 2509）的模型清单、工作流说明和本地运行方法见 [docs/comfyui-local.md](docs/comfyui-local.md)。

> 导入 API 后的动态高级参数、设定集参考上传与可选显示声明见 [ComfyUI 工作流高级参数](docs/comfyui-workflow-parameters.md)。

> WebSocket 实时进度、HTTP 保底与刷新恢复见 [ComfyUI 任务连接与恢复](docs/comfyui-task-tracking.md)。

### 3. ComfyUI 原生自定义节点插件（`comfyui_plugin/`）
将本仓库克隆到 `ComfyUI/custom_nodes/ai-pose-gallery-zh` 后，ComfyUI 画布右键菜单 **「AI角色三合一参考图集」** 下自动提供 4 个节点：
- **AI 姿势参考图 (`PoseGalleryNode`)**：输出 `姿势图 (IMAGE)`、`图片ID`、`姿势提示词`（支持 `use_depth` 开关一键切换输出素体白模或深度图）
- **AI 服装参考图 (`CostumeGalleryNode`)**：输出 `服装图 (IMAGE)`、`图片ID`、`中文服装描述`、`英文服装Prompt`
- **AI 人像参考图 (`PortraitGalleryNode`)**：输出 `人像图 (IMAGE)`、`图片ID`、`人像发型描述`
- **AI 角色三合一合成配方 (`CharacterRecipeNode`)**：单节点同时输出 `人像图`、`服装图`、`姿势图（支持 use_depth 深度图切换）`、`三合一拼图` 以及自动组装的