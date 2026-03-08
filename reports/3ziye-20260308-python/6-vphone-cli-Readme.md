<div align="right"><strong><a href="./docs/README_ko.md">🇰🇷한국어</a></strong> | <strong><a href="./docs/README_ja.md">🇯🇵日本語</a></strong> | <strong><a href="./docs/README_zh.md">🇨🇳中文</a></strong> | <strong>🇬🇧English</strong></div>

# vphone-cli

Boot a virtual iPhone (iOS 26) via Apple's Virtualization.framework using PCC research VM infrastructure.

![poc](./docs/demo.jpeg)

## Tested Environments

| Host          | iPhone             | CloudOS       |
| ------------- | ------------------ | ------------- |
| Mac16,12 26.3 | `17,3_26.1_23B85`  | `26.1-23B85`  |
| Mac16,12 26.3 | `17,3_26.3_23D127` | `26.1-23B85`  |
| Mac16,12 26.3 | `17,3_26.3_23D127` | `26.3-23D128` |

## Firmware Variants

Three patch variants are available with increasing levels of security bypass:

| Variant         |   Boot Chain    |    CFW    | Make Targets                                                 |
| --------------- | :-------------: | :-------: | ------------------------------------------------------------ |
| **Regular**     |   41 patches    | 10 phases | `fw_patch` + `cfw_install`                                   |
| **Development** |   52 patches    | 12 phases | `fw_patch_dev` + `cfw_install_dev`                           |
| **Jailbreak**   | 66 / 78 patches | 14 phases | `fw_patch_jb` + `cfw_install_jb` + `cfw_install_jb_finalize` |

> `cfw_install_jb_finalize` requires booting into the full system, not the ramdisk.

See [research/0_binary_patch_comparison.md](./research/0_binary_patch_comparison.md) for the detailed per-component breakdown.

## Prerequisites

**Host OS:** macOS 15+ (Sequoia) is required for PV=3 virtualization.

**Configure SIP/AMFI** — required for private Virtualization.framework entitlements and unsigned binary workflows.

Boot into Recovery (long press power button), open Terminal, then choose one setup path:

- **Option 1: Fully disable SIP + AMFI boot-arg (most permissive)**

  In Recovery:

  ```bash
  csrutil disable
  csrutil allow-research-guests enable
  ```

  After restarting into macOS:

  ```bash
  sudo nvram boot-args="amfi_get_out_of_my_way=1 -v"
  ```

  Restart once more.

- **Option 2: Keep SIP mostly enabled, disable only debug restrictions, use [`amfidont`](https://github.com/zqxwce/amfidont)**

  In Recovery:

  ```bash
  csrutil enable --without debug
  csrutil allow-research-guests enable
  ```

  After restarting into macOS:

  ```bash
  xcrun python3 -m pip install amfidont
  sudo amfidont --path [PATH_TO_VPHONE_DIR]
  ```

**Install dependencies:**

```bash
brew install ideviceinstaller wget gnu-tar openssl@3 ldid-procursus sshpass keystone autoconf automake pkg-config libtool cmake
```

**Submodules** — this repo uses a git submodule for resource archives. Clone with:

```bash
git clone --recurse-submodules https://github.com/Lakr233/vphone-cli.git
```

## Quick Start

```bash
make setup_machine            # full automation through "First Boot" (includes restore/ramdisk/CFW)
# options: NONE_INTERACTIVE=1 SUDO_PASSWORD=...
```

## Manual Setup

```bash
make setup_tools              # install brew deps, build trustcache, clone insert_dylib, build libimobiledevice, create Python venv
make build                    # build + sign vphone-cli
make vm_new                   # create vm/ directory (ROMs, disk, SEP storage)
make fw_prepare               # download IPSWs, extract, merge, generate manifest
make fw_patch                 # patch boot chain (regular variant)
# or: make fw_patch_dev       # dev variant (+ TXM entitlement/debug bypasses)
# or: make fw_patch_jb        # jailbreak variant (+ full security bypass)
```

## Restore

You'll need **two terminals** for the restore process. Keep terminal 1 running while using terminal 2.

```bash
# terminal 1
make boot_dfu                 # boot VM in DFU mode (keep running)
```

```bash
# terminal 2
make restore_get_shsh         # fetch SHSH blob
make restore                  # flash firmware via idevicerestore
```

## Install Custom Firmware

Stop the DFU boot in terminal 1 (Ctrl+C), then boot into DFU again for the ramdisk:

```bash
# terminal 1
make boot_dfu                 # keep running
```

```bash
# terminal 2
sudo make ramdisk_build       # build signed SSH ramdisk
make ramdisk_send             # send to device
```

Once the ramdisk is running (you should see `Running server` in the output), open a **third terminal** for the iproxy tunnel, then install CFW from terminal 2:

```bash
# terminal 3 — keep running
iproxy 2222 22
```

```bash
# terminal 2
make cfw_install
# or: make cfw_install_jb        # jailbreak variant
```

## First Boot

Stop the DFU boot in terminal 1 (Ctrl+C), then:

```bash
make boot
```

This gives you a **direct console** on the VM. When you see `bash-4.4#`, press Enter and run these commands to initialize the shell environment and generate SSH host keys:

```bash
export PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/X11:/usr/games:/iosbinpack64/usr/local/sbin:/iosbinpack64/