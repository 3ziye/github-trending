# OOOSplat

[中文](README.md) | [English](README_EN.md)

<p align="center">
  <img src="assets/readme-logo.svg" alt="OOOSplat Logo" width="180">
</p>

<p align="center">
  <a href="https://github.com/ooolabdev/ooosplat/releases/tag/0.4.0"><strong>⬇️ 下载 OOOSplat 0.4.0（Windows / macOS / Ubuntu）</strong></a>
</p>

OOOSplat 是一款将普通环绕拍摄视频或图片序列一键转换为 3D Gaussian Splatting 的本地桌面应用。选择素材、项目目录和质量档位后，应用会自动完成画面准备、相机重建、训练与 PLY 发布，并可直接预览、调整和导出结果。

Windows 和 Apple Silicon macOS Alpha 均随应用提供 FFmpeg、FFprobe、COLMAP 和 Brush；Linux 支持目前仅作为 Ubuntu 24.04 LTS x86_64 Alpha 提供。整个生成流程使用本机 CPU 和 GPU，输入素材、工程文件、模型与日志无需上传到云端重建或训练服务。React 界面通过 Tauri 直接调用本机 Rust 后端，不需要远程服务或 localhost API。

当前版本：**0.4.0**

查看 [OOOSplat Roadmap](ROADMAP.md) 了解后续规划。

> 0.4.0 新增图片序列输入、透明 MOV/PNG 自动 Mask、阶段级断点续跑，以及矩形、球形和盒形 Gaussian 编辑；原始 `final.ply` 始终保留。

## 核心优势

- **一键生成高斯泼溅**：只需选择输入视频或图片序列、项目目录和质量档位，即可自动完成画面准备、COLMAP 相机重建、Brush 训练和 `final.ply` 发布，无需手动拼接命令或配置引擎。
- **全平台兼容**：支持 Windows、macOS 和 Linux，可在三大主流桌面系统上完成本地高斯泼溅生成；具体系统与处理器要求请参阅下方兼容性说明。
- **安全与隐私保护**：素材、抽帧、相机重建数据、高斯模型和日志默认只保存在用户选择的本地项目目录，核心生成流程在本机完成，无需将原始视频、图像或模型上传到第三方重建与训练平台，从而减少数据在网络传输、云端留存和未经授权访问过程中的泄露风险。
- **完全本地化算力**：重建与训练均在用户自己的电脑上运行，不调用远程计算服务。满足要求时 COLMAP 自动使用本机 NVIDIA GPU 加速，否则回退 CPU，过程和数据始终由用户掌控。

## 界面预览

### 创建与管理任务

![OOOSplat 创建新任务与历史任务界面](assets/screenshots/task-workspace.png)

### 高斯泼溅预览与调整

![OOOSplat 高斯泼溅预览与 Transform 调整界面](assets/screenshots/gaussian-preview.png)

## 主要功能

- 从 MP4、MOV 视频，或包含 JPG、JPEG、PNG 的图片序列文件夹创建 Gaussian Splatting 项目。
- 视频使用均匀抽帧和顺序匹配；图片序列保留全部图片并使用共享相机、穷举匹配和现有增量 Mapper。
- 自动检测透明 MOV 的 Alpha 通道，同步提取 RGBA PNG 画面与 COLMAP Mask；透明区域不会参与特征提取，同时保留给 Brush 训练使用。
- 自动检测透明 PNG，保留 Alpha 供 Brush 使用，并生成 COLMAP Mask 排除完全透明区域。
- Windows 安装包内置 CUDA 版 COLMAP；macOS Alpha 内置 arm64 CPU 版 COLMAP；Ubuntu 使用系统 CPU 版 COLMAP。三个平台均使用固定并校验的 FFmpeg/Brush 方案。
- COLMAP 会自动检查内置 CUDA 运行时、NVIDIA 驱动版本和显卡 Compute Capability，满足要求时使用 GPU 加速特征提取与匹配，否则自动回退到 CPU。
- 实时显示处理阶段、引擎输出、关键计数、累计耗时和最多 500 条界面日志。
- 原始进程输出完整写入项目的 `logs` 目录。
- 支持取消任务，并通过 Windows Job Object 或 Unix process group 终止整个子进程树。
- 支持自定义项目根目录，默认位置为 `Documents\SplatStudio\Projects`。
- 自动记录已完成、失败、中断和取消的历史任务。
- 支持阶段级断点续跑：重新检查抽帧、Mask、COLMAP 数据库、稀疏重建和 PLY 检查点，复用可信阶段，并从最早的不可信阶段安全重跑。
- 根据素材规模、质量档位和本机历史任务估算生成时长；Brush 训练阶段持续更新进度。
- 在“03 预览”中直接加载历史项目的 `.ply`，支持 Orbit、Pan 和 Zoom；“调整 / 动画”双模式切换不会重新加载模型或重置相机。
- 调整模式支持整个 Gaussian 模型的位置、旋转、等比缩放，以及撤销 / 重做。
- 提供矩形、球形和盒形 Gaussian 选择工具：矩形可穿透框选并非破坏式删除点，球形和盒形区域则实时保留区域内的 Gaussian。
- 裁切区域和删除记录会自动保存；点击“保存”时将编辑结果写入唯一的 `edit.ply`，后续保存会安全替换该文件，始终不覆盖原始 `final.ply`。
- 动画模式依次播放 5 秒显现、8 秒冲击波和持续相机环绕，并可导出带 OOOSplat 水印的 1080×1920、30 fps、23 秒 H.264 MP4。
- 可在平台文件管理器中定位 `final.ply`，或将整个项目移入系统回收站。
- 可拖动中央分界线调整左右面板宽度；右下角支持 80%–140% 整体界面缩放。
- 支持中文、空格、长文件名和 UNC 项目路径。

### Gaussian 编辑快捷键

- 矩形选择时，左键拖动替换选区，`Shift + 左键拖动`添加，`Ctrl + 左键拖动`移除；中键旋转视角，右键平移，滚轮缩放。
- 黄色高亮表示当前选区；按 `Delete` 或 `Backspace` 删除选中 Gaussian，按 `Esc` 清空临时选区。
- 球形或盒形选择会自动进入正交视图，可切换侧视图、正视图和顶视图，并通过视口控制器或数值面板调整位置与大小。
- `Ctrl + Z` 撤销，`Ctrl + Shift + Z` 或 `Ctrl + Y` 重做。模型变换、裁切和删除共享同一历史记录；相机移动和临时黄色选区不计入历史。

## 处理流程

```text
输入视频或图片序列
  │
  ├─ 视频：FFprobe 分析，FFmpeg 按质量档位均匀抽帧；透明视频同步生成 RGBA 画面与 Mask
  ├─ 图片：按文件名排序并保留全部图片；透明 PNG 自动生成 Mask
  ├─ COLMAP：自动选择 CPU 或 CUDA GPU 提取特征；视频顺序匹配，图片穷举匹配
  ├─ COLMAP：增量重建并验证注册率和三维点
  ├─ Brush：使用可用 GPU 训练 Gaussian Splats
  └─ 校验 PLY 后原子发布为 final.ply
```

只要 COLMAP 生成了至少一张注册图像和有效三维点，任务就会继续进入 Brush；注册率低于 80% 时会给出质量警告，但不再因低于 50% 自动终止。

## 系统要求

- Windows 11，x64。
- 支持 WebView2 Runtime。
- 视频导出需要 WebView2 提供 WebCodecs AVC 编码能力；不支持时仍可在“动画”模式播放效果，但“导出视频”会显示不可用原因。
- Brush 训练需要可用的 GPU 图形后端，建议使用独立显卡。
- COLMAP 的 CUDA 加速需要 NVIDIA 显卡、Windows 驱动 528.33 或更高版本，以及 Compute Capability 5.0 或更高版本；不满足要求时程序会自动使用 CPU，无需用户配置。
- 项目磁盘需要容纳源素材副本、输入图像、COLMAP 数据、Brush 中间文件和最终 PLY。长视频、大型图片序列或精细档位可能占用大量空间。
- 安装模式为整机安装，安装时可能需要管理员权限。

Windows 内置的 COLMAP 使用同时支持 CPU 与 CUDA GPU 的构建，运行前会自动选择可用后端；Brush 训练使用可用图形后端，二者的 GPU 检测与运行机制相互独立。

### macOS 15+ Alpha（仅限 Apple Silicon）

> 当前交付为未签名、未公证的 `.app`/`.dmg` Alpha，仅支持 M1 或更新的 Apple Silicon Mac，不支持 Intel Mac 或 Universal Binary。

- 内置原生 arm64 FFmpeg 8.1.2、独立 FFprobe、COLMAP 4.0.4 CPU CLI-only 和 Brush v0.3.0。
- 用户不需要安装 Homebrew，也不会回退到 Homebrew 或系统 `PATH` 中的同名程序。
- COLMAP 固定使用 CPU；Brush 独立选择可用的 Metal 图形后端，界面会明确显示该原因。
- 首次打开未签名版本时，macOS Gatekeeper 可能阻止启动。请在 Finder 中右键应用并选择“打开”；正式版本将在后续接入 Apple 签名和公证。

### Ubuntu 24.04 Alpha（仅限 x86_64）

> 本 Alpha 交付由 Ubuntu 24.04 构建的 x86_64 `.deb` 安装包；不声明支持 Ubuntu 22.04、其他 Linux 发行版或生产环境部署。

- Ubuntu 24.04 LTS，x86_64。
- Brush 支持的图形后端和对应驱动；Brush 官方支持 AMD、Intel 和 NVIDIA GPU。当前端到端验证使用 NVIDIA GPU，CPU-only 软件图形后端尚未验证，但不会被启动检查人为阻止。
- 从源码构建需要 Node.js 22.12+、Rust stable 和 Tauri 2 的 WebKitGTK 开发依赖；安装 `.deb` 的用户不需要这些开发工具。
- Ubuntu 24.04 系统 `ffmpeg`、`ffprobe` 和 CPU 版 `colmap`（仓库版本为 COLMAP 3.9）。
- Brush v0.3.0 Linux x86_64，由 `npm run setup:engines` 下载并校验。

Ubuntu 依赖安装：

```bash
sudo apt update
sudo apt install -y \
  build-essential curl file ffmpeg colmap \
  libwebkit2gtk-4.1-dev libxdo-dev libssl-dev \
  libayatana-appindicator3-dev librsvg2-dev libdbus-1-dev
```

请为显卡安装可用的 Vulkan 驱动（例如 NVIDIA 专有驱动，或 AMD/Intel 的 Mesa 驱动）。Ubuntu 24.04 仓库