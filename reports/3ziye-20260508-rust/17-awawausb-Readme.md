# WebUSB extension for Firefox

This extension adds WebUSB functionality to Firefox by making use of [native messaging](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Native_messaging).

In order to use this, you need to _both_ install the extension in your browser and install a small program (separate from the browser) on your computer. This extra program is called the "native stub".

## Feature support

This extension is supposed to be compatible with Chrome's implementation. Please report any differences you encounter that result in software not working.

However, unlike Chrome, this API is only exposed on the main page and is not available in [Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers).

Android cannot be supported, because it does not have native messaging capabilities.

## WebUSB vs other interfaces

This extension only supports WebUSB. WebUSB is only one of several ways for web pages to access physical devices (even if the device is physically plugged in to your computer using _USB connectors_).

Please read [this document](Documentation/what-is-webusb.md) for a detailed explanation.

## Installation instructions

You can install this extension by downloading binaries from the GitHub "Releases" section (in the right-hand column), or you can build from source.

### Installing the extension

To install a signed version of the extension, download the .xpi file and open it in Firefox.

To load a _testing_ version of the extension in Firefox Developer Edition, open `about:debugging`, select "This Firefox" in the left-hand list, then "Load Temporary Add-on…", and then browse to the `manifest.json` inside the `extension/` directory.

### Installing the native stub

If you are using prebuilt binaries, unzip _all_ of the files and then run either `./install.sh` (on Linux or macOS) or `install.bat` (on Windows). These installers will try to automatically copy the appropriate files into a sensible location and then configure a [native manifest](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Native_manifests) so that the browser can find it.

Prebuilt binaries are available for the following platforms:

- macOS x86_64 and ARM64
- Linux x86_64 and aarch64
- Windows AMD64 and ARM64

If you are not using prebuilt binaries, see [below](#compiling-from-source).

### "Unusual" configurations

The default installer is known to have problems with uncommon configurations such as:

- sharing a \*nix home directory across different computers with different CPU architectures
- Windows roaming user profiles across computers with different CPU architectures

The root cause of this is because the "native manifest" mechanism was not designed well to take these situations into account (for example, through its use of absolute paths). If you are in one of these situations, you will unfortunately need to invent an ad-hoc workaround.

## System requirements

This native stub tries to avoid doing anything too "exciting", but, due to development and testing resource constraints, it focuses on "reasonably modern" desktop platforms.

### macOS

macOS 10.15 or later is required, matching Firefox's system requirements. However, older systems are not very well-tested. Expect macOS 12 to be a much more reasonable baseline.

### Windows

Windows 10 or later is required, due to the requirements of the Rust platform support. This also matches Firefox system requirements. Backporting to Windows 8/8.1 might theoretically be possible, but any older is not expected to work (due to limitations in WinUSB).

### Linux

Linux kernel version 4.8 or later is required. (More specifically, a kernel containing commit `5cce438` and `USBDEVFS_CAP_REAP_AFTER_DISCONNECT` is _strongly_ recommended, and a kernel supporting `USBDEVFS_DISCONNECT_CLAIM` is required.)

Your system must have `/dev` and `/sys` mounted.

In order to detect USB devices being connected, a userspace with [udev](https://man7.org/linux/man-pages/man7/udev.7.html) or a compatible daemon is required. Specifically, a daemon which broadcasts `0xfeedcafe`-format messages on `NETLINK_KOBJECT_UEVENT` group `2` is required.

## Compiling from source

In general, this native stub is written entirely in Rust and can be built using `cargo build` in the `native-stub` directory. Cross-compiling _is_ supported and is configured by default for the supported platforms.

If this does not "just work", the following notes might help:

### macOS

This _really_ should just work. The repository contains a vendored copy of all the `.tbd` files needed to link the final binary. If that is somehow causing problems, disable the appropriate entries in `.cargo/config.toml` (which will then require you to have a macOS SDK installed).

### Linux

Linux prebuilt binaries are set up to use [musl libc](https://www.musl-libc.org/) with Rust's default of static linking. The goal of this is to produce binaries which work acro