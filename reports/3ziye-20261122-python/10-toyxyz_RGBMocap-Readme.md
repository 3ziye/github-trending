# RGB MoCap

![RGB MoCap workspace showing video tracking and a 3D motion preview](docs/images/rgbmocap-workspace.png)

A native Windows app that turns video into editable human animation. Review and
export motion with AI processing running locally.

## Sample videos

### Motion capture

https://github.com/user-attachments/assets/b948dd8c-43b9-493a-9d7f-2fae0317695e

[Download original sample](docs/samples/motion-capture.mp4)

### Character retargeting

https://github.com/user-attachments/assets/1759f1bf-a0d0-409f-84d8-dde9409cfe6f

[Download original sample](docs/samples/character-retargeting.mp4)

### Multi Cam MoCap

https://github.com/user-attachments/assets/4c0b290b-4a65-4287-8d22-c63c96b3d080

[Download original sample](docs/samples/multi-cam-mocap.mp4)

### Streaming to Blender

https://github.com/user-attachments/assets/cc0e79bb-ecce-4752-ae14-3b6cea30c810

[Download original sample](docs/samples/streaming-to-blender.mp4)

### Unreal Engine MetaHuman live streaming

https://github.com/user-attachments/assets/3353f5ca-6393-40af-822f-210a77f51003

## Install and run

The steps below cover Windows. For the experimental x86-64 Linux AppImage and
source installation, see the [Linux guide](https://github.com/toyxyz/toyxyz_RGBMocap/blob/linux_support/docs/LINUX.md#test-the-appimage-on-linux-mint).
The AppImage was tested on WSL 2. Native Linux Mint testing is welcome.

> [!IMPORTANT]
> On Windows 11, Smart App Control in **On** mode may block the unsigned private
> Python runtime used by RGB MoCap. This can stop installation or launch.
> See [Smart App Control troubleshooting](docs/USER_GUIDE.md#smart-app-control-on-windows-11).

1. Install [Git for Windows](https://git-scm.com/download/win). Use a short, writable
   installation path such as `C:\RGBMoCap`. Open **Command Prompt** to clone
   the repository. Adjust the path if you need a different folder.

   ```cmd
   git clone https://github.com/toyxyz/toyxyz_RGBMocap.git C:\RGBMoCap
   cd /d C:\RGBMoCap
   ```

2. Prepare the runtimes for ExMR, FlowHMR and GVHMR with their supported add-ons,
   plus PEAR live-preview support,
   Blender, FFmpeg and native motion correction. AI weights and registered body
   files are downloaded separately in Model Manager:

   ```cmd
   install.cmd
   ```

3. Start the app:

   ```cmd
   RGBMoCap.cmd
   ```

   Keep the console open while the app runs. Prepare the AI model files separately
   using **Model Manager**; some require account registration and manual download.

If setup fails with `WinError 3` or `WinError 206` and the error shows a long
path, see [Windows path length troubleshooting](docs/USER_GUIDE.md#windows-path-length-during-installation).

To update, close the app and run `update.cmd` from the same folder. See the
[installation guide](docs/USER_GUIDE.md#install) for disk space, prerequisites
and recovery.

Updates reuse recently verified, unchanged runtimes. If PEAR or camera-alignment
support preparation fails after the base installation succeeds, the base app
remains usable; rerun `install.cmd` to retry the unavailable support. See
[verification and repair](docs/USER_GUIDE.md#installation-verification-and-repair).

### Optional model runtimes

`install.cmd` prepares ExMR, FlowHMR, GVHMR and the small shared-runtime support
for [PEAR live preview](docs/models/PEAR.md). Install the following only if
you use them, after the base installation:

| Model | Separate setup command | Installation and usage |
| --- | --- | --- |
| MAMMA | `Setup_MAMMA.cmd` | [MAMMA guide](docs/MAMMA.md) |
| PromptHMR | `Setup_PromptHMR.cmd` | [PromptHMR guide](docs/models/PROMPTHMR.md) |
| GEM-X | `Setup_GEMX.cmd` | [GEM-X guide](docs/models/GEMX.md) |

MAMMA and PromptHMR require **Visual Studio 2022 C++ Build Tools**, the Windows SDK and
**CUDA Toolkit 12.8** for local native builds. Close the app and review the
provider terms before setup. Then reopen it and prepare the selected model's
files in **Model Manager**. Their optional runtimes do not require each other;
`install.cmd` and `update.cmd` do not install them.

GEM-X uses the existing ExMR Python base with its own pinned inference packages.
Run its separate setup after `install.cmd`, then prepare its public files in
**Model Manager**. It does not require the C++ build tools or CUDA Toolkit.

PEAR reuses the base shared runtime with a small support overlay prepared by
`install.cmd` and `update.cmd`. No separate setup or compiler is required.
Model files are prepared separately.

For optional text-prompt and click-guided **Find person** tracking on Windows,
run `Setup_SAM31.cmd` after the base setup. Then choose **SAM 3.1** next to
**Find person** and use **Auto Download** on its 1.75 GB checkpoint row in
**Model Manager**. SAM 3.1 uses more VRAM than **Default** tracking.
**Resource Mode > Automatic** can offload tracking state and masks to system
RAM when VRAM is tight and retry once after CUDA runs out of memory.
See the [SAM 3.1 tracker guide](docs/models/SAM31.md#vra