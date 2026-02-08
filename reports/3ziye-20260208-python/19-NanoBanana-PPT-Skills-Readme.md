# NanoBanana PPT Skills

> 基于 AI 自动生成高质量 PPT 图片和视频的强大工具，支持智能转场和交互式播放

<div align="center">

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)

**创作者**: [歸藏](https://github.com/op7418)

[效果演示](#-效果演示) • [功能特性](#-功能特性) • [一键安装](#-一键安装) • [作为 Skill 使用](#-作为-claude-code-skill-使用) • [使用指南](#-使用指南) • [视频功能](#-视频功能) • [架构文档](ARCHITECTURE.md) • [常见问题](#-常见问题)

</div>

---

## 🎬 效果演示

<div align="center">

https://github.com/user-attachments/assets/b394de21-2848-489a-8d33-a8e262e60f60

*AI 自动生成 PPT 并添加流畅转场动画 - 从文档分析到视频合成一键完成*

</div>

---

## 📖 简介

NanoBanana PPT Skills 是一个强大的 AI 驱动的 PPT 生成工具，能够：

- 📄 **智能分析文档**，自动提取核心要点并规划 PPT 结构
- 🎨 **生成高质量图片**，使用 Google Nano Banana Pro（Gemini 3 Pro Image Preview）
- 🎬 **自动生成转场视频**，使用可灵 AI 创建流畅的页面过渡动画
- 🎮 **交互式视频播放器**，支持键盘控制、循环预览、智能转场
- 🎥 **完整视频导出**，一键合成包含所有转场的完整 PPT 视频

### 🎨 视觉风格

**渐变毛玻璃卡片风格**
- 高端科技感，Apple Keynote 极简主义
- 3D 玻璃物体 + 霓虹渐变
- 电影级光照效果
- 适合：科技产品、商务演示、数据报告

**矢量插画风格**
- 温暖扁平化设计，复古配色
- 黑色轮廓线 + 几何化处理
- 玩具模型般的可爱感
- 适合：教育培训、创意提案、品牌故事

---

## ✨ 功能特性

### 🎯 核心能力

- 🤖 **智能文档分析** - 自动提取核心要点，规划 PPT 内容结构
- 🎨 **多风格支持** - 内置 2 种专业风格，可无限扩展
- 🖼️ **高质量图片** - 16:9 比例，2K/4K 分辨率可选
- 🎬 **AI 转场视频** - 可灵 AI 生成流畅的页面过渡动画
- 🎮 **交互式播放器** - 视频+图片混合播放，支持键盘导航
- 🎥 **完整视频导出** - FFmpeg 合成包含转场的完整 PPT 视频
- 📊 **智能布局** - 封面页、内容页、数据页自动识别
- ⚡ **快速生成** - 2K 约 30 秒/页

### 🆕 视频功能（v2.0）

- 🎬 **首页循环预览** - 自动生成吸引眼球的循环动画
- 🎞️ **智能转场** - 自动生成页面间的过渡视频
- 🎮 **交互式播放** - 按键翻页时播放转场视频，结束后显示静态图片
- 🎥 **完整视频导出** - 合成包含所有转场和静态页的完整视频
- 🔧 **参数统一** - 自动统一所有视频分辨率和帧率，确保流畅播放

### 🛠️ 技术亮点

- ✅ Google Nano Banana Pro（Gemini 3 Pro Image Preview）图像生成
- ✅ 可灵 AI API 集成（视频生成、数字人、主体库）
- ✅ FFmpeg 视频合成与参数统一
- ✅ 完整的提示词工程和风格管理系统
- ✅ 安全的 .env 环境变量管理
- ✅ 模块化设计，易于扩展

---

## 🚀 一键安装

### 方法一：Claude Code 自动安装（推荐）

**只需复制以下提示词，发送给 Claude Code，它会自动完成全部安装！**

```
请帮我安装 NanoBanana PPT Skills：

1. 克隆项目并进入目录：
   git clone https://github.com/op7418/NanoBanana-PPT-Skills.git
   cd NanoBanana-PPT-Skills

2. 创建 Python 虚拟环境：
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

3. 安装依赖：
   pip install google-genai pillow python-dotenv

4. 配置 API 密钥 - 创建 .env 文件：
   cp .env.example .env

5. 编辑 .env 文件，填入我的 API 密钥：

   GEMINI_API_KEY=YOUR_GEMINI_API_KEY
   KLING_ACCESS_KEY=YOUR_KLING_ACCESS_KEY
   KLING_SECRET_KEY=YOUR_KLING_SECRET_KEY

   注意：
   - GEMINI_API_KEY: Google AI API 密钥（必需，用于生成 PPT 图片）
   - KLING_ACCESS_KEY 和 KLING_SECRET_KEY: 可灵 AI 密钥（可选，用于生成转场视频）

6. 验证安装：
   python3 generate_ppt.py --help

完成后，告诉我安装结果和如何使用。

我的 API 密钥：
- GEMINI_API_KEY: YOUR_GEMINI_API_KEY_HERE
- KLING_ACCESS_KEY: YOUR_KLING_ACCESS_KEY_HERE (可选)
- KLING_SECRET_KEY: YOUR_KLING_SECRET_KEY_HERE (可选)
```

**使用说明**：
1. 先获取 API 密钥：
   - **必需**: [Google AI API 密钥](https://aistudio.google.com/apikey)
   - **可选**: [可灵 AI API 密钥](https://klingai.com)（用于视频转场功能）
2. 复制上面的提示词
3. 将 `YOUR_GEMINI_API_KEY_HERE` 等替换为你的真实 API 密钥
4. 发送给 Claude Code
5. Claude Code 会自动执行所有安装步骤并告知结果

### 方法二：手动安装

如果你想手动安装，按照以下步骤操作：

#### 1. 克隆项目

```bash
git clone https://github.com/op7418/NanoBanana-PPT-Skills.git
cd NanoBanana-PPT-Skills
```

#### 2. 创建虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### 3. 安装依赖

```bash
pip install google-genai pillow
```

如果需要视频功能，还需要安装 FFmpeg：

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg

# Windows
# 下载 FFmpeg 并添加到系统 PATH
```

#### 4. 配置 API 密钥

**推荐方式：.env 文件（已内置支持）**

```bash
# 复制示例文件
cp .env.example .env

# 编辑 .env 文件
nano .env  # 或使用你喜欢的编辑器
```

在 `.env` 文件中填入你的 API 密钥：

```bash
# Google AI API 密钥（必需）
GEMINI_API_KEY=your_gemini_api_key_here

# 可灵 AI API 密钥（可选，用于视频转场功能）
KLING_ACCESS_KEY=your_kling_access_key_here
KLING_SECRET_KEY=your_kling_secret_key_here
```

**替代方式：系统环境变量**

```bash
# zsh 用户 (macOS 默认)
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc

# bash 用户
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

#### 5. 验证安装

```bash
python3 generate_ppt.py --help
```

应该显示帮助信息，表示安装成功。

---

## 🎯 作为 Claude Code Skill 使用

NanoBanana PPT Skills 完全支持 Claude Code Skill 标准，可以直接通过 Claude Code 调用。

### 快速安装为 Skill

**方法一：Claude Code 自动安装为 Skill（最简单）**

**只需复制以下提示词，发送给 Claude Code，它会自动完成 Skill 安装！**

```
请帮我将 NanoBanana PPT Skills 安装为 Claude Code Skill：

1. 创建 Skill 目录：
   mkdir -p ~/.claude/skills/ppt-generator

2. 克隆项目到 Skill 目录：
   git clone https://github.com/op7418/NanoBanana-PPT-Skills.git ~/.claude/skills/ppt-generator

3. 进入目录并安装依赖：
   cd ~/.claude/skills/ppt-generator
   python3 -m venv venv
   source venv/bin/activate
   pip install google-genai pillow python-dotenv

4. 配置 API 密钥：
   cp .env.example .env

   然后编辑 .env 文件，填入我的 API 密钥：
   GEMINI_API_KEY=YOUR_GEMINI_API_KEY
   KLING_ACCESS_KEY=YOUR_KLING_ACCESS_KEY
   KLING_SECRET_KEY=YOUR_KLING_SECRET_KEY

5. 验证安装：
   python3 generate_ppt.py --help

完成后，告诉我如何在 Claude Code 中使用这个 Skill。

我的 API 密钥：
- GEMINI_API