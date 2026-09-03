# ComfyUI MiniMax H3 Director

基于 **ComfyUI 官方 MiniMax-H3** 的多段音视频导演台插件。仓库地址：[AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director)

**English** → [README_EN.md](README_EN.md)

![MiniMaxH3Director 工作流截图](docs/screenshot.png)

## 功能介绍

**MiniMaxH3Director** 是面向长视频、多段生成的 MiniMax H3 导演台节点，把分段计划、条件编码、采样解码和导出整合在一个节点里。底层走官方 `MiniMaxH3ImageToVideo` / `MiniMaxH3ReferenceToVideo` + `MiniMaxH3SigmaShift` + `KSampler` + AV 分离解码链路，原生输出立体声音频。

### 核心能力

| 功能 | 说明 |
|------|------|
| **多段时间轴** | 节点内上传视频，支持切分、均分、智能分镜分割（PySceneDetect）、追加；分割点可选中删除；可视化时间轴预览每段范围与缩略图 |
| **多任务模式** | `task_type`：`t2v`（文生视频）、`i2v`（图生视频）、`fl2v`（首尾帧生视频）、`r2v`（参考主体生视频 / 素材组）、`v2v`（视频转视频）、`rv2v`（参考素材改视频） |
| **首尾帧 (fl2v)** | 独立首尾帧时间轴：多组关键帧、「添加一组」可只写提示词（文生）、或上传首帧和/或尾帧（官方支持只传尾帧）；开「段间引导」并勾「引用上段」时，空组用上一段末尾 N 帧做运动/音频衔接；拖缘调时长；支持「选择运行」只跑部分组 |
| **参考素材组 (r2v)** | fl2v 式分组 UI：上方「公共参数」共享参考图/音频与公共提示词（与每组提示词拼接）；每组可再挂图片1–9 / 音频1–3 / 视频1–3；提示词用 `<Picture N>` / `<Video K>` / `<Audio J>`（或 `@` 引用）；时间轴预览与选中状态同步 |
| **源视频编辑 (v2v / rv2v)** | Bernini 风格源视频时间轴；每段源画面自动绑定 `<Video 1>`；`rv2v` 另可挂参考图（图片1–9）与参考音频（音频1–3） |
| **选择运行** | 开启后只采样勾选的片段/素材组；未勾选段可用缓存或源画面填充（全部导出时） |
| **外部多组接线** | `Director Group (Image to Video)` / `(Reference to Video)` + `Groups Combine`；连入导演台 `i2v_groups` / `r2v_groups` 后外部优先覆盖 UI 素材，仍支持跑批与选择运行 |
| **原生立体声音频** | 与画面同次采样生成；`v2v`/`rv2v` 可选生成声音 / 使用原声 / 静音 |
| **段间引导** | 默认关闭；多段 `t2v` / `i2v` / `fl2v` / `r2v` / `v2v` / `rv2v` 时可开启，将上一段生成结果的末尾运动（及生成音频）钉入下一段采样再裁掉前缀。上下文帧数：5 / 22 / 39 / 56，**默认推荐为 22**。**感谢 [ComfyUI-H3-Motion-Context](https://github.com/NikoDemon80/ComfyUI-H3-Motion-Context) 提供的实现思路** |
| **二采 / 放大 (Refine)** | 外接 **MiniMax H3 Director Refine** 到导演台 `refine` 口。未接线 = 原来的单次采样。`refine` = 同分辨率精修；`upscale` = 先放大到目标画布再按 SIGMAS 二采（像素插值 / RTX VSR / H3 latent）；`latent_upscale` = 只放大 H3 latent、不二采。`passes` 可多次精修（upscale 只放大一次）。可选接 `refine_model` 换二采 UNET。`images` 为二采后成片，`images_pre_refine` 为一采（放大前）画面 |
| **运行报告** | `report` 口输出分段计划、每段任务摘要 |
| **导演包导入导出** | 工具栏「导入/导出导演包」：zip 内保存时间轴 JSON 与参考图/视频/音频。目录名为英文（`shared_params/`、`asset_groups/01/`、`Picture1`…），与切到 EN 后的界面用语对应，避免路径编码问题 |

参考音频槽可直接选择已有视频，或从本地选择音频/视频；视频会立即提取首条音轨为 FLAC，结果直接保存到 `input/`。本地视频只在临时目录中用于提取，不会作为视频素材保存。音频沿用 ComfyUI 现有上传规则：同名同内容直接复用，同名不同内容自动添加序号且不会覆盖；当前素材组也不会重复添加同一路径。

### 输入 / 输出

**输入：** `model` → `video_vae` → `audio_vae` → `clip`  
**可选：** `i2v_groups`（Image to Video 多组）/ `r2v_groups`（Reference to Video 多组）/ `refine`（`MiniMax H3 Director Refine`）

**输出：** `images` → `audio` → `fps` → `frame_count` → `source_images` → `report` → `images_pre_refine`

> CLIP Loader 的 **type 必须选 `minimax`**（Qwen3-VL）。  
> `t2v` / `i2v` / `fl2v` 用 **fl2va** UNET；`r2v` / `v2v` / `rv2v` 用 **ref2va** UNET。

`输出原片到 source_images` 只填充独立的 `source_images` 输出，不会改变主 `images`。请将 `source_images` 另接预览或视频合成节点查看；解码失败时运行报告会明确说明，并输出灰色占位而不会冒充生成画面。

## 导演包（剧本 + 素材）

工具栏右侧 **导入导演包 / 导出导演包**。导出为 `*.mmxpack.zip`。路径只用 ASCII，与英文界面一致（与当前 UI 语言无关）。

| English UI | Pack path |
|------|------|
| Shared params | `shared_params/` |
| Asset group 1 | `asset_groups/01/` |
| Picture 1–9 | `Picture1.png` … `Picture9.webp` |
| Video 1–3 | `Video1.mp4` |
| Audio 1–3 | `Audio1.wav` |
| start / end (fl2v) | `start.jpg` / `end.jpg` in that group folder |
| Upload video (v2v source) | `source_video/` |

```
pack.json
shared_params/shared_params.json
shared_params/Picture1.png
asset_groups/01/group.json
asset_groups/01/Picture4.png
timeline.json
```

- `timeline.json`：导演台导出时写入，用于无损往返（含其它任务草稿等）。
- 转换工具可以只写 `pack.json` + `shared_params/` + `asset_groups/`，不必手写 `timeline.json`。
- 槽位编号与界面相同：公共参数占用 Picture 1–3 时，组文件夹里从 `Picture4` 续编，不要在组内把第一张改名为 `Picture1`。
- 不含 UNET / CLIP / VAE。导入会覆盖当前节点时间轴（有确认）。媒体落到 ComfyUI `input/minimax_director_packs/`。

## 依赖

请将 **ComfyUI** 升级到 **v0.30.0** 及以上（含官方 MiniMax H3 节点：[PR #15224](https://github.com/comfyanonymous/ComfyUI/pull/15224)、[PR #15228](https://github.com/comfyanonymous/ComfyUI/pull/15228)）。

可选：`scenedetect`（智能分割）、`opencv-python-headless`（源视频解码）、`imageio-ffmpeg`（原声抽取）——见 `requirements.txt`。  
Refine 的 `nvidia_rtx_vsr` 另需 NVIDIA GPU，可 `pip install nvidia-vfx --extra-index-url https://pypi.nvidia.com`（不是硬依赖）。

## 安装

### 方法一：手动安装（标准方式）

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director.git

pip install -r ComfyUI_MiniMaxH3_Director/requirements.txt
```

重启 ComfyUI。

### 方法二：ComfyUI Manager

1. 打开 **ComfyUI Manager**
2. 选择 **Install via Git URL**
3. 填入 `https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director.git` 并安装
4. 重启 ComfyUI

## 模型与工作流下载

完整资源包（**MiniMax H3 模型权重** + **示例 JSON 工作流**）见：

**[Comfyit 搅拌站 · 文章 506：MiniMax H3 模型和工作流](https://comfyit.cn/article/506)**

下载后将 `models/` 合并到 `ComfyUI/models/`，JSON 工作流拖入 ComfyUI 即可。

也可参考：

- **Hugging Face：** [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)
- **ComfyUI 文档：** [MiniMax H3 工作流示例](https://docs.comfy.org/zh/tutorials/video/minimax/minimax-h3)

本仓库自带示例：`example_workflows/`

| 工作流 | task_type | UNET | 说明 |
|--------|-----------|------|------|
| `minimax