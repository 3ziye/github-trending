# CorridorKey


https://github.com/user-attachments/assets/1fb27ea8-bc91-4ebc-818f-5a3b5585af08


When you film something against a green screen, the edges of your subject inevitably blend with the green background. This creates pixels that are a mix of your subject's color and the green screen's color. Traditional keyers struggle to untangle these colors, forcing you to spend hours building complex edge mattes or manually rotoscoping. Even modern "AI Roto" solutions typically output a harsh binary mask, completely destroying the delicate, semi-transparent pixels needed for a realistic composite.

I built CorridorKey to solve this *unmixing* problem. 

You input a raw green screen frame, and the neural network completely separates the foreground object from the green screen. For every single pixel, even the highly transparent ones like motion blur or out-of-focus edges, the model predicts the true, un-multiplied straight color of the foreground element, alongside a clean, linear alpha channel. It doesn't just guess what is opaque and what is transparent; it actively reconstructs the color of the foreground object as if the green screen was never there.

No more fighting with garbage mattes or agonizing over "core" vs "edge" keys. Give CorridorKey a hint of what you want, and it separates the light for you.

## Alert!

This is a brand new release, I'm sure you will discover many ways it can be improved! I invite everyone to help. Join us on the "Corridor Creates" Discord to share ideas, work, forks, etc! https://discord.gg/zvwUrdWXJm

Also, if you are a novice at using python scripts much like I was, consider downloading a smart IDE like Antigravity (from google, it's free), downloading this repository, and then asking Antigravity to help you get up and running. I even made a LLM Handover doc in the docs/ directory. This project uses [uv](https://docs.astral.sh/uv/) to manage dependencies — it handles Python installation, virtual environments, and packages all in one step, so you don't need to worry about any of that.

Naturally, I have not tested everything. If you encounter errors, please consider patching the code as needed and submitting a pull request.

## Features

*   **Physically Accurate Unmixing:** Clean extraction of straight color foreground and linear alpha channels, preserving hair, motion blur, and translucency.
*   **Resolution Independent:** The engine dynamically scales inference to handle 4K plates while predicting using its native 2048x2048 high-fidelity backbone.
*   **VFX Standard Outputs:** Natively reads and writes 16-bit and 32-bit Linear float EXR files, preserving true color math for integration in Nuke, Fusion, or Resolve.
*   **Auto-Cleanup:** Includes a morphological cleanup system to automatically prune any tracking markers or tiny background features that slip through CorridorKey's detection.

## Hardware Requirements

This project was designed and built on a Linux workstation (Puget Systems PC) equipped with an NVIDIA RTX Pro 6000 with 96GB of VRAM. The community is ACTIVELY optimizing it for consumer GPUS.

The most recent build should work on computers with 6-8 gig of VRAM, and it can run on most Mac systems with unified memory. Yes, it might even work on your old Macbook pro. Let us know on the Discord!

*   **Windows Users:** To run GPU acceleration natively on Windows, your system MUST have NVIDIA drivers that support **CUDA 12.8 or higher** installed. If your drivers only support older CUDA versions, the installer will likely fallback to the CPU.
*   **GVM (Optional):** Requires approximately **80 GB of VRAM** and utilizes massive Stable Video Diffusion models.
*   **VideoMaMa (Optional):** Natively requires a massive chunk of VRAM as well (originally 80GB+). While the community has tweaked the architecture to run at less than 24GB, those extreme memory optimizations have not yet been fully implemented in this repository.

Because GVM and VideoMaMa have huge model file sizes and extreme hardware requirements, installing their modules is completely optional. You can always provide your own Alpha Hints generated from other, lighter software.

## Getting Started

### 1. Installation

This project uses **[uv](https://docs.astral.sh/uv/)** to manage Python and all dependencies. uv is a fast, modern replacement for pip that automatically handles Python versions, virtual environments, and package installation in a single step. You do **not** need to install Python yourself — uv does it for you.

**For Windows Users (Automated):**
1.  Clone or download this repository to your local machine.
2.  Double-click `Install_CorridorKey_Windows.bat`. This will automatically install uv (if needed), set up your Python environment, install all dependencies, and download the CorridorKey model.
    > **Note:** If this is the first time installing uv, any terminal windows you already had open won't see it. The installer script handles the current window automatically, but if you open a new te