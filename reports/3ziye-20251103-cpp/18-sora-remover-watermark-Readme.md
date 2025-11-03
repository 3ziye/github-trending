# 🎬 Sora2 Watermark Remover

**AI-Powered Video Watermark Removal Tool**

![](assets/release.png)

---

## 📋 Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [Quick Start](#quick-start)
- [User Guide](#user-guide)
- [Technical Details](#technical-details)
- [FAQ](#faq)
- [License](#license)
- [Contact & Support](#contact--support)

---

## 🌟 Introduction

**Sora2 Watermark Remover** is an AI-driven desktop and web application that uses advanced computer vision and deep learning models to detect and remove watermarks from Sora-generated videos.  
It provides **professional-grade watermark removal** with a clean, intuitive interface and high-quality, seamless results.

### Why Choose Sora2?

- 🎯 **Accurate AI Detection** – Detects “Made with Sora” and similar watermarks automatically  
- 🖱️ **Manual Control** – Interactive masking editor for precise selection and fine-tuning  
- ⚡ **Fast Processing** – Optimized algorithm pipeline for faster video processing  
- 🎨 **Seamless Results** – AI inpainting ensures smooth, natural-looking output  
- 🔒 **Privacy First** – All processing is local; your videos are never uploaded  

---

## ✨ Key Features

### Core Functions

- 🎭 **AI Watermark Detection** – Automatically detects watermark regions  
- ✏️ **Mask Editing** – Visual editor to manually adjust detected areas  
- 🎬 **Multi-Format Support** – Works with MP4, MOV, MKV, WebM, and more  
- 💾 **Local Saving** – Automatically saves processed results on your device  
- 🌍 **Multi-Language Interface** – Supports English, Chinese, and others  
- 💻 **Responsive UI** – Optimized for desktops and laptops  

### Advanced Options

- 🔍 **Live Preview** – See mask and inpainting results in real time  
- ⚙️ **Batch Processing** – Remove watermarks from multiple videos at once  
- 💡 **Task Queue** – Background task queue for smoother performance  
- 🧩 **Custom Parameters** – Adjust repair strength and algorithm depth  

---

## 🛠️ Tech Stack

### Frontend
- **Framework:** Next.js + TypeScript  
- **UI:** Radix UI + Tailwind CSS  
- **Canvas Editing:** React Konva  
- **State Management:** React Hooks + Context API  
- **Localization:** next-intl  

### Backend
- **Database:** PostgreSQL (via Drizzle ORM)  
- **Authentication:** NextAuth  
- **Storage:** Local filesystem or Cloudflare R2 (optional)  
- **AI Engine:** ComfyUI workflow for frame-by-frame inpainting  

### Infrastructure
- **Deployment:** Local or self-hosted server  
- **Logging:** Built-in runtime logs and error tracking  
- **Monitoring:** Task and performance visualization  

---

## 🔬 How It Works

### Video Processing Pipeline

```

Upload Video → Draw Mask → Generate Mask → Send to AI Model → Inpainting → Export Result

````

### Step-by-Step Workflow

1. **Upload** a video file  
2. **Mark** the watermark area on the interactive canvas  
3. **Generate Mask** – Convert the marked region into a mask image  
4. **AI Repair** – ComfyUI runs AI inpainting frame by frame  
5. **Export** the final watermark-free video  

---

## 🚀 Quick Start

### Requirements

- Node.js 18 or higher  
- PostgreSQL database (optional)  
- ComfyUI processing server (for AI rendering)  

### Installation

### Windows
- Download the latest `.exe` installer or `.zip` archive from [Releases](../../releases)
- Both packages include all dependencies including FFmpeg
- Run the installer or extract the `.zip` and run `SoraRemover.exe`

---

## 📖 User Guide

### For End Users

1. Open the application
2. Click “Upload Video” and select your file
3. Use the editor to mark watermark areas
4. Click “Remove Watermark” to start processing
5. Download the watermark-free video once finished

---

## 🧪 Technical Details

* **AI Detection:** Deep learning models identify watermark positions
* **Inpainting Algorithm:** U-Net based model performs seamless repair
* **Task Queue:** Prevents GPU overload by queuing jobs
* **Performance Optimization:** Lazy loading, caching, and indexed queries

---

## ❓ FAQ

**Q: Is it safe to use?**
A: Yes. All processing is done locally on your machine — no uploads.

**Q: What formats are supported?**
A: MP4, MOV, MKV, WebM, and most common video formats.

**Q: How long does it take?**
A: A 15-second clip usually takes 3–5 minutes depending on GPU speed.

**Q: Does it support 4K videos?**
A: Yes, but higher resolutions require more time. 1080p is recommended.

**Q: Can I process multiple videos at once?**
A: Yes, batch processing is supported.

---

## 📄 License

This project is released under the **MIT License**.
You may use, modify, and distribute it freely with attribution.

---

## 📞 Contact & Support

* **Issue Reporting:** Submit bugs or suggestions via the project’s issue tracker

---

<div align="center">

**Built with ❤️ by the Sora2 Watermark Remover Team**
Thank you to all contributors and testers

[⬆ Back to Top](#sora2-watermark-remover)

</div>
