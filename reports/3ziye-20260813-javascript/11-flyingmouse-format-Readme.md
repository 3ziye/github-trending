# FlyingMouse Format / 飞鼠格式

> A mouse-themed, offline Windows file converter. / 一款鼠鼠主题、可离线使用的 Windows 文件格式转换工具。

[![Release](https://img.shields.io/github/v/release/LaoFeng-mouse/flyingmouse-format?color=e95f6d)](https://github.com/LaoFeng-mouse/flyingmouse-format/releases/latest)
![CI](https://github.com/LaoFeng-mouse/flyingmouse-format/actions/workflows/ci.yml/badge.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS-0078D6)
![License](https://img.shields.io/badge/License-MIT-green)

[下载最新版 / Download](https://github.com/LaoFeng-mouse/flyingmouse-format/releases/latest) · [问题反馈 / Issues](https://github.com/LaoFeng-mouse/flyingmouse-format/issues)

![FlyingMouse Format mouse UI](public/assets/screenshots/home.png)

## 中文

### 主要功能

- 鼠鼠原版界面：鼠鼠会跟随上传、识别、批量、OCR、转换成功或失败切换状态。
- 本地离线转换：内置 FFmpeg、LibreOffice、Poppler、Tesseract 和 AVS3 解码器。
- 支持图片、文本、Word/WPS、Excel/WPS、PPT/WPS、PDF、音频、视频和 ZIP。
- NCM 解密与转码：支持来自 `music.163.com` 对应网易云音乐客户端的常规 NCM，以及 Audio Vivid（AV3A）NCM。
- mflac/mgg 解密：支持 QQ 音乐官方客户端下载的 mflac/mgg（新版 musicex 需 QQ 音乐登录凭据在线换密钥；原档无权限时自动降档下载同一首歌的可用音质档位）。
- 操作记忆：按“源文件格式”分别记住上次选择的目标格式；重新修改后，新选择会成为该源格式的默认值。
- 路径记忆：记住上次保存目录，下次保存时自动从该目录开始。
- 中文/English 界面：首次启动跟随系统语言，手动选择后会记住设置。
- 批量转换：显示逐文件进度、结果和失败原因，并可单独保存或保存全部。
- 转换质量：HTML / Office 转 Markdown 保留标题、列表和代码块；CSV 支持 BOM、转义引号和字段内换行。
- PDF → Excel（智能表格提取）：支持电子文字坐标、扫描页 OCR、有框/无框表格、多表、跨页续接、合并单元格、低置信度批注与 Raw 回退。
- PDF → Word（可编辑内容提取）：电子版 PDF 提取文字与简单表格生成可编辑 DOCX，扫描版自动 OCR 回退。注意：不保留原 PDF 的图片、字体、颜色、页眉页脚与复杂版式，属内容提取而非版式还原。
- 电子书：txt/md/html → EPUB（纯本地生成）；EPUB → TXT/Markdown；MOBI → EPUB/TXT/Markdown（MOBI 解析为实验性，复杂版式可能不完整）。
- 图片合并 PDF 支持调整顺序：多张图片转 PDF 前可在队列中上移/下移，PDF 页序跟随队列顺序。
- HEIC/HEIF 图片可转换为 JPG/PNG/WebP 等（内置 ffmpeg 解码）。
- 相机 RAW 原片（CR2/CR3/NEF/ARW/DNG 等）可转换为 JPG/PNG/WebP/TIFF 等（内置 dcraw 解码，Windows 版，实验性）。
- 资源保护：单图 50MP / 16384px、图片合并 PDF 总计 100MP、批量 2GB、PDF 不限页数（1:1 转换，长文档加载较慢）、OCR 不限页数。

> NCM 说明：仅保证支持 `music.163.com` 对应客户端下载的音乐文件。其他网站或来源虽然扩展名也可能是 `.ncm`，但内部格式不同，不属于本项目的兼容范围。

### 快速开始

1. 在 [Releases](https://github.com/LaoFeng-mouse/flyingmouse-format/releases/latest) 下载 v0.3.5 对应系统的安装包。
2. 安装并启动 FlyingMouse Format。
3. 拖入文件，选择目标格式并开始转换。
4. 选择保存位置；软件会记住目标格式与保存目录。

从源码运行：

> 源码仓库不包含体积较大的 FFmpeg、LibreOffice、Poppler 和 Tesseract 资源；普通用户请直接下载 Release 安装包。开发者从源码运行完整转换功能前，需要自行准备 `bin/` 下的引擎资源。

```powershell
npm install
npm run desktop
```

运行测试与打包：

```powershell
npm test
npm run dist
```

### Windows 版本选择

- **Windows 10 / 11 x64（推荐）**：下载标准资产 `FlyingMouse.Format-Setup-0.3.5-x64.exe`。它使用 Electron 43、Sharp 0.35 和 PDF.js 6 运行时。
- **Windows 7 SP1 x64（兼容版）**：下载 `FlyingMouse.Format-Setup-0.3.5-win7-x64.exe`。它使用同一源码和鼠鼠 UI，但在独立环境固定 Electron 22.3.27、Sharp 0.32.6 与 PDF.js 2.16.105。

Windows 7 兼容版是 Legacy 构建，不会降低标准版依赖。其 Electron 22 已停止上游安全维护，并包含无法在 Windows 7 上直接升级的已知依赖风险；PDF.js 动态代码执行已通过 `isEvalSupported: false` 缓解，但仍只建议离线处理可信文件。v0.3.5 通过 Windows、macOS arm64 和 macOS x64 自动化门禁以及 3 个真实 NCM/AV3A 样本回归；真实 Windows 7 SP1 x64 设备仍待验收。Windows 安装包均未签名，SmartScreen 可能提示。

### macOS 版本选择

- **Apple Silicon（M1 及更新）**：下载 `FlyingMouse.Format-Setup-0.3.5-mac-arm64.dmg`。
- **Intel Mac**：下载 `FlyingMouse.Format-Setup-0.3.5-mac-x64.dmg`。

首批 macOS 包支持 macOS 11 及更新版本，未签名且未公证，可能触发 Gatekeeper。标准 NCM 可用；Audio Vivid（AV3A）NCM 依赖 Windows 专用解码器，不在 macOS 支持范围内。两个架构已在原生 GitHub runner 完成固定引擎、完整转换、包结构和 12 秒启动冒烟；真实 Mac 设备仍待验收。

完整构建只需：

```powershell
npm run dist:win7
```

Win7 staging 使用专用 `win7-package-lock.json` 和 `npm ci` 重建；推荐使用 Node.js 22 LTS（构建脚本接受 18–22，其他主版本会在改动 staging 前拒绝）。构建脚本会绑定子进程到当前 Node、以 Unicode 安全方式复制源码、锁定 staging manifest/lockfile，并校验本地 builder 与打包资源没有越过各自允许的根目录或经过 junction/符号链接。

仅需检查 staging 时可运行 `node scripts/build-win7.js --prepare-only`；它不会打包。完整构建会重新准备 staging。

## English

### Highlights

- Original mouse UI with animated state changes for upload, detection, batch work, OCR, success, and errors.
- Fully local conversion with bundled FFmpeg, LibreOffice, Poppler, Tesseract, and an AVS3 decoder.
- Converts images, text, Word/WPS, Excel/WPS, PPT/WPS, PDF, audio, video, and ZIP files.
- Decrypts and converts standard NCM plus Audio Vivid (AV3A) NCM from the NetEase Cloud Music client associated with `music.163.com`.
- Decrypts mflac/mgg from the official QQ Music client (newer musicex variants require a QQ Music login cookie for online key exchange; when the original quality tier is unauthorized, the app automatically downloads an available tier of the same song).
- Remembers the chosen target separately for each source extension. Changing it replaces that extension's default.
- Remembers the last save directory for the next save dialog.
- Chinese and English UI. The first launch follows the system language; a manual choice is remembered.
- Batch conversion with per-file progress, results, error details, individual save, and Save All.
- Higher-quality text conversion: structural HTML/Office Markdown plus standards-compliant quoted and multiline CSV parsing.
- PDF → Excel smart table extraction for digital text and scanned pages, including multiple tables, continued pages, mer