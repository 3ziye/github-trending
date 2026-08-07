# reims-vgpu

[![License: LGPL-3.0-or-later](https://img.shields.io/badge/License-LGPL%203.0%20or%20later-blue.svg)](LICENSE)

> **Alpha.** This project is early and under active development. The QEMU device ABI, boot scripts,
> crate layout, backend behavior, and supported host/guest pathways may change without a stable
> compatibility guarantee. Treat it as research-quality: useful for experimentation and bring-up,
> not a frozen virtualization product.

reims-vgpu is an experimental virtual GPU for macOS guests. It aims to let macOS running inside a
VM use accelerated graphics instead of a basic framebuffer, while keeping the guest operating system
unchanged.

macOS already includes a paravirtual GPU driver named `AppleParavirtGPU.kext`.
reims-vgpu provides the QEMU device that driver attaches to, then decodes the guest's GPU command
stream on the host and executes it through Metal (TODO) or Vulkan, with Vulkan translation handled
by [`metal2vulkan`](https://github.com/steelbrain/metal2vulkan). There is no custom macOS kext and
no guest driver to install.

Contributions are welcome. I am especially interested in collaborating with developers who want to
work on correctness, visual glitches, synchronization bugs, command-stream decoding, Metal/Vulkan
translation, and making more host/guest combinations reliable.

![reims-vgpu running an arm64 macOS 13 Ventura guest desktop on an Apple Silicon host](assets/readme/reims-vgpu-macos-arm64-desktop.png)

*arm64 macOS 13 Ventura guest on an Apple Silicon host.*

![reims-vgpu running an x86_64 macOS 13 Ventura guest desktop on a Linux host](assets/readme/reims-vgpu-macos-x86-desktop.png)

*x86_64 macOS 13 Ventura guest on a Linux host.*

## Three pathways

`crates/reims-vgpu` targets the following host/guest/backend combinations. Agents pick the pathway
their unit of work is on.

| Pathway | Host | Guest | Device attach | Backend | Boot |
|---|---|---|---|---|---|
| **x86 macOS / Linux Vulkan** | Linux x86_64 (KVM) | x86_64 macOS Metal guest | PCI `reims-vgpu-pci` | host **Vulkan** via `metal2vulkan` | `vm/boot-x86.sh` |
| **arm64 macOS / macOS Metal** | Apple Silicon macOS (HVF) | arm64 macOS Metal guest (`vmapple`) | sysbus MMIO `reims-vgpu-mmio` | host **Metal** | `vm/boot-arm64.sh` |
| **arm64 macOS / macOS Vulkan** | Apple Silicon macOS (HVF) | arm64 macOS Metal guest (`vmapple`) | sysbus MMIO `reims-vgpu-mmio` | host **Vulkan** via `metal2vulkan` through MoltenVK | `vm/boot-arm64.sh` |

- QEMU device shims: `vendor/qemu` tracks
  [`steelbrain/qemu-reims-vgpu@host-reims-vgpu-vmapple`](https://github.com/steelbrain/qemu-reims-vgpu/tree/host-reims-vgpu-vmapple)
  (thin C — QOM/MMIO/IRQ/console/HostOps only)
- Product logic: `crates/reims-vgpu` (decode + device model + Metal/Vulkan backends)
- Wire layouts: `crates/reims-vgpu-wire` (derived serializer views/parsers; decode uses these as the layout authority for covered records)
- Vulkan translator dependency: public `steelbrain/metal2vulkan` Git crate. On macOS, the Vulkan
  host backend runs through MoltenVK.
- VM lifecycle: `vm/` (snapshot-revert; arm and x86 guest boot scripts)

## Getting started

This tree ships **boot scripts and the device**, not a ready-made macOS disk image. Guest disks,
firmware vars, and OpenCore blobs are private/gitignored under `vm/`. Pick a pathway, provision a
guest once, freeze a golden snapshot, then use the snapshot-revert boots for day-to-day work.
macOS 13 Ventura is the recommended guest release for bring-up.

### x86_64 guest on Linux (KVM)

1. **Host prep.** You need KVM (`/dev/kvm`), a working NVIDIA (or other) Vulkan stack for the product
   backend, and build deps for the in-tree QEMU (`scripts/qemu-build/qemu-build.sh --target x86_64
   --backend vulkan`). KVM must ignore unhandled MSRs or macOS will not boot — e.g. a modprobe conf
   with `options kvm ignore_msrs=1` (reboot or reload the module after).

2. **Generate OpenCore, OVMF, and a guest disk with [OSX-KVM](https://github.com/kholia/OSX-KVM).**
   **macOS 13 is recommended**.Follow that project’s docs to fetch recovery media, build OpenCore,
   and install macOS under QEMU+KVM. The point of this step is only to produce a
   **working, post-Setup-Assistant guest** plus the usual OpenCore/OVMF pieces — not to stay on
   OSX-KVM’s long-term launcher.

3. **Drop the artifacts where this repo expects them** (paths are the defaults in `vm/boot-x86.sh`;
   override with env if you prefer):

   | Artifact | Default location |
   |---|---|
   | Guest system disk | `vm/disks/macos.img` |
   | OpenCore boot disk | `vm/disks/OpenCore.qcow2` |
   | OVMF code | `vm/ovmf/OVMF_CODE_4M.fd` |
   | OVMF vars template | `vm/ovmf/OVMF_VARS-1920x1080.fd` |

   Finish install in the guest: enable Remote Login, install your SSH key, turn off sleep/screensaver
   as you like. Host SSH is typically `localhost:2222` → guest `:22` (see `vm/boot-x86.sh`).

4. **Capture the first immutable snapshot.** From a clean guest state (logged in, 