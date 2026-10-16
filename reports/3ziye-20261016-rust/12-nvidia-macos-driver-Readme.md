# NullMoth NVIDIA Driver for macOS

A Metal driver for NVIDIA GeForce cards on macOS 15 Sequoia (Intel Macs and OpenCore PCs). It is open source; the
kernel extensions, the Metal plugin, the shader translator and the Mac app are all in this repository.

Supported cards are Turing and newer: GTX 16, RTX 20, 30, 40 and 50, TITAN RTX, Quadro RTX and the T-series. Most
testing is done on an RTX 5060, so other cards may have problems that haven't been found yet. See
[card support](docs/CARD-SUPPORT.md) for what has been reported working.

- Changes: [CHANGELOG.md](CHANGELOG.md), downloads on the [releases page](https://github.com/nullmoth/nvidia-macos-driver/releases)
- Problems: [troubleshooting](docs/TROUBLESHOOTING.md), then Send logs from the 1401 app
- Installing macOS from Windows: [1401](https://github.com/nullmoth/1401)
- How it works: [docs/HOW-IT-WORKS.md](docs/HOW-IT-WORKS.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)

If your PC doesn't boot macOS with OpenCore yet, set that up first with the
[OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/), then install the driver.

Support the work: https://buymeacoffee.com/nullmoth

| | |
|---|---|
| macOS | 15 Sequoia (tested 15.7.x and 15.8.1), x86_64 |
| GPUs | NVIDIA Turing and later; developed on an RTX 5060 |
| Metal | Metal 3: argument buffers tier 2, ray tracing, mesh shaders, MPS, MetalFX path |
| Also | OpenGL (through Apple's GL-on-Metal), OpenCL, Core Image, Core ML |

## How it works

```
Metal app ─► NVMTLDriver.bundle ─► translator (Apple AIR → SPIR-V) ─► NVK (Mesa Vulkan + NAK compiler) ─► kexts ─► GPU
```

| Component | Path on disk | Source |
|---|---|---|
| Metal driver plugin | `/Library/GPUBundles/NVMTLDriver.bundle` | `plugin/` |
| Shader translator | inside the plugin (`libnvmtl_translate.dylib`) | `translator/` (LGPL-3.0, based on metal2vulkan) |
| Vulkan back end (NVK) | `/Library/GPUBundles/nvmtl/` | `nvk/nvk-macos.patch` on Mesa `17ca6174` |
| Kernel extensions | `/Library/Extensions/NVRM, NVAccel, NVRMFB, NVRMAGDC` | `kexts/` |
| GPU firmware (GSP) | `/Users/Shared/nvfw/nvidia/610.57.04` | NVIDIA, unmodified |

The kernel side runs NVIDIA's own open GPU kernel modules (r610) under macOS. NVRMFB is the display framebuffer,
NVAccel the accelerator WindowServer composites through, NVRMAGDC the display-policy shim.

## Install — by hand

Use the 1401 Mac app below unless you manage your OpenCore config yourself. `install.sh` installs the driver files but
does not change OpenCore, and the driver does not start until OpenCore has these settings:

- `boot-args` include `nvfb=1 nvaccel=1 nvfbheads=4 -nvkmsnosmooth amfi_get_out_of_my_way=0x1 amfi=0x80
  ipc_control_port_options=0`, and not `nv_disable=1` or `-wegnoegpu` (both hide the NVIDIA card)
- `csr-active-config` includes the bits `0x0A43`
- `Misc > Security > SecureBootModel` is `Disabled`
- `Lilu.kext` and `AMFIPass.kext` are in `Kernel > Add` and enabled

Download `nullmoth-nvidia-<version>.tar.gz` from **Releases**, then:

```bash
tar -xzf nullmoth-nvidia-*.tar.gz && cd pkgroot
shasum -a 256 -c SHA256SUMS
sudo ./install.sh
sudo shutdown -r now
```

Every file must say OK in the check. `install.sh` copies the files and rebuilds the Auxiliary Kernel Collection; the
restart is required, because logging out does not load the driver. (Paste the lines without anything after them: the
Terminal on macOS does not treat `#` as a comment, so a pasted comment becomes part of the command.)

macOS asks you to **allow the extensions** in System Settings → Privacy & Security the first time. Allow, then reboot again.

## 1401 Mac app (recommended)

Download the latest `1401-Mac-<version>.dmg` from **Releases**, open it, and run **1401** (the driver package is inside the disk
image, so nothing else to download). Follow its steps. A supported setup must use a verified or explicitly selected OpenCore partition. The app finds the OpenCore that started your Mac (in `EFI/OC` or `EFI/BOOT`, on an
EFI or FAT32 partition), shows every change before making it, backs the config up, installs the driver, and adds
**1401: Remove NVIDIA driver** to the OpenCore boot picker. Choosing that entry removes the driver at the next start and
puts the Mac back exactly as it was before the install, OpenCore config included, then restarts by itself. The app also
maps your USB ports and, if the driver ever crashes the Mac, offers to make a crash report you can upload yourself
(it never sends anything on its own).

If something goes wrong, open 1401 > Crash report > Send logs to NullMoth. It uploads what 1401 did, the driver's
state, crash reports and OpenCore's startup log, with names, serial numbers and addresses removed, and gives you a
report ID to put in your issue or in Discord.

Keep the USB stick or disk that OpenCore started from plugged in while the app runs, and for every restart after:
that is the config the app changes. The app never copies OpenCore to your internal disk. The firs