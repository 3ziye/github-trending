# OOOSplat

[中文](README.md) | [English](README_EN.md)

<p align="center">
  <img src="assets/readme-logo.svg" alt="OOOSplat Logo" width="180">
</p>

OOOSplat 是一款将普通环绕拍摄视频一键转换为 3D Gaussian Splatting 的本地桌面应用。选择视频、项目目录和质量档位后，应用会自动完成抽帧、相机重建、训练与 PLY 发布，并可直接预览、调整和导出结果。

Windows 和 Apple Silicon macOS Alpha 均随应用提供 FFmpeg、FFprobe、COLMAP 和 Brush；Linux 支持目前仅作为 Ubuntu 24.04 LTS x86_64 Alpha 提供。整个生成流程使用本机 CPU 和 GPU，输入素材、工程文件、模型与日志无需上传到云端重建或训练服务。React 界面通过 Tauri 直接调用本机 Rust 后端，不需要远程服务或 localhost API。

当前版本：**0.3.0**

查看 [OOOSplat Roadmap](ROADMAP.md) 了解后续规划。

> 当前版本可从视频生成并管理 `final.ply`，并在应用内完成 Gaussian Splat 预览、整体 Transform 编辑、动画预览以及非破坏式导出。

## 核心优势

- **一键生成高斯泼溅**：只需选择输入视频、项目目录和质量档位，即可自动完成 FFmpeg 抽帧、COLMAP 相机重建、Brush 训练和 `final.ply` 发布，无需手动拼接命令或配置引擎。
- **安全可控**：素材、抽帧、重建数据、模型和日志默认只保存在用户选择的本地项目目录，无需上传云端；Transform 与导出采用非破坏式流程，不覆盖原始 `final.ply`。
- **完全本地化算力**：重建与训练均在用户自己的电脑上运行，不调用远程计算服务。满足要求时 COLMAP 自动使用本机 NVIDIA GPU 加速，否则回退 CPU，过程和数据始终由用户掌控。

## 界面预览

### 创建与管理任务

![OOOSplat 创建新任务与历史任务界面](assets/screenshots/task-workspace.png)

### 高斯泼溅预览与调整

![OOOSplat 高斯泼溅预览与 Transform 调整界面](assets/screenshots/gaussian-preview.png)

## 主要功能

- 从 MP4、MOV 视频创建 Gaussian Splatting 项目。
- 自动完成视频分析、均匀抽帧、特征提取、顺序匹配、相机重建、Brush 训练和 PLY 发布。
- Windows 安装包内置 CUDA 版 COLMAP；macOS Alpha 内置 arm64 CPU 版 COLMAP；Ubuntu 使用系统 CPU 版 COLMAP。三个平台均使用固定并校验的 FFmpeg/Brush 方案。
- COLMAP 会自动检查内置 CUDA 运行时、NVIDIA 驱动版本和显卡 Compute Capability，满足要求时使用 GPU 加速特征提取与匹配，否则自动回退到 CPU。
- 实时显示处理阶段、引擎输出、关键计数、累计耗时和最多 500 条界面日志。
- 原始进程输出完整写入项目的 `logs` 目录。
- 支持取消任务，并通过 Windows Job Object 或 Unix process group 终止整个子进程树。
- 支持自定义项目根目录，默认位置为 `Documents\SplatStudio\Projects`。
- 自动记录已完成、失败、中断和取消的历史任务。
- 在“03 预览”中直接加载历史项目的 `.ply`，支持 Orbit、Pan 和 Zoom；“调整 / 动画”双模式切换不会重新加载模型或重置相机。
- 调整模式支持整个 Gaussian 模型的位置、旋转、等比缩放，以及撤销 / 重做。
- Transform 自动保存到 `project.json`；导出生成 `edited.ply`、`edited-2.ply` 等新文件，不覆盖原始 `final.ply`。
- 动画模式依次播放 5 秒显现、8 秒冲击波和持续相机环绕，并可导出带 OOOSplat 水印的 1080×1920、30 fps、23 秒 H.264 MP4。
- 可在平台文件管理器中定位 `final.ply`，或将整个项目移入系统回收站。
- 可拖动中央分界线调整左右面板宽度；右下角支持 80%–140% 整体界面缩放。
- 支持中文、空格、长文件名和 UNC 项目路径。

## 处理流程

```text
输入视频
  │
  ├─ FFprobe：读取时长、分辨率、帧率和总帧数
  ├─ FFmpeg：按照质量档位均匀抽取画面
  ├─ COLMAP：自动选择 CPU 或 CUDA GPU 进行特征提取与顺序匹配
  ├─ COLMAP：增量重建并验证注册率和三维点
  ├─ Brush：使用可用 GPU 训练 Gaussian Splats
  └─ 校验 PLY 后原子发布为 final.ply
```

COLMAP 注册图像比例低于 50% 时任务停止；50%–80% 时给出质量警告并继续；达到 80% 时视为正常。

## 系统要求

- Windows 10 或 Windows 11，x64。
- 支持 WebView2 Runtime。
- 视频导出需要 WebView2 提供 WebCodecs AVC 编码能力；不支持时仍可在“动画”模式播放效果，但“导出视频”会显示不可用原因。
- Brush 训练需要可用的 GPU 图形后端，建议使用独立显卡。
- COLMAP 的 CUDA 加速需要 NVIDIA 显卡、Windows 驱动 528.33 或更高版本，以及 Compute Capability 5.0 或更高版本；不满足要求时程序会自动使用 CPU，无需用户配置。
- 项目磁盘需要容纳源视频副本、抽帧图像、COLMAP 数据、Brush 中间文件和最终 PLY。长视频或精细档位可能占用大量空间。
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

请为显卡安装可用的 Vulkan 驱动（例如 NVIDIA 专有驱动，或 AMD/Intel 的 Mesa 驱动）。Ubuntu 24.04 仓库中的无 CUDA COLMAP 构建会自动使用 CPU；Brush 会在运行时选择可用的图形后端。完全 CPU-only 的软件 Vulkan 后端尚未完成端到端验证。

从 GitHub Actions 下载 `OOOSplat-0.3.0-x64-linux` Artifact 后，可执行：

```bash
sudo apt install ./OOOSplat-0.3.0-x64-linux.deb
```

`.deb` 会通过 Ubuntu 包管理器安装 FFmpeg、FFprobe 和 CPU 版 COLMAP；固定版本 Brush 已包含在安装包中。

## 安装与使用

1. Windows 运行 `OOOSplat-0.3.0-x64-windows.exe`；Apple Silicon Mac 打开 `OOOSplat-0.3.0-arm64-macos.dmg` 并将 OOOSplat 拖入“应用程序”；Ubuntu 24.04 使用 `sudo apt install ./OOOSplat-0.3.0-x64-linux.deb`。
2. 启动 OOOSplat，确认顶栏中的内置引擎状态正常。
3. 在“01 创建新任务”中选择输入视频。
4. 选择项目根目录；程序会记住上次使用的位置。
5. 选择“快速”“均衡”或“精细”档位。
6. 查看自动检测到的 COLMAP 加速状态及原因，然后点击“开始生成”。
7. 在左侧查看实时阶段、指标和日志；完成后，在“02 历史任务”中查看项目并点击“预览”。
8. 在“03 预览”的“调整”模式中修改模型，Transform 会自动保存；点击“导出高斯”生成新的 edited PLY。
9. 切换到“动画”可查看竖屏构图并重新播放效果；点击“导出视频”会在项目目录生成 23 秒竖屏 MP4。

使用提示：

- 拖动左右面板之间的分界线可以调整宽度；双击分界线恢复默认比例。
- 点击右下角百分比按钮可缩小、恢复或放大整个界面。
- 任务运行期间不可修改视频、项目目录和质量档位。
- 点击“删除”会回收整个项目目录，包括源视频副本和所有中间文件；如果移入回收站失败，程序不会降级为永久删除。

## 质量档位

| 档位 | 保留画面 | FFmpeg 抽帧率 | Brush iterations | 最大训练分