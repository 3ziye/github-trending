[English](README.en.md) | [Tiếng Việt](README.md)

<a id="readme-top"></a>

<div align="center">
  <a href="https://github.com/LotusInputMethod/fcitx5-lotus">
    <img src="data/fcitx-lotus-README.svg" alt="Logo" width="80" height="80">
  </a>

<h2 align="center">Fcitx5 Lotus</h2>

<p align="center">
    <b>Bộ gõ tiếng Việt đơn giản, hiệu năng cao cho Linux</b>
    <br />
    <br />
    <a href="https://github.com/LotusInputMethod/fcitx5-lotus/releases">
      <img src="https://img.shields.io/github/v/release/LotusInputMethod/fcitx5-lotus?style=flat&color=success" alt="Release">
    </a>
    <a href="https://github.com/LotusInputMethod/fcitx5-lotus/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/LotusInputMethod/fcitx5-lotus?style=flat&color=blue" alt="License">
    </a>
    <a href="https://github.com/LotusInputMethod/fcitx5-lotus/stargazers">
      <img src="https://img.shields.io/github/stars/LotusInputMethod/fcitx5-lotus?style=flat&color=yellow" alt="Stars">
    </a>
    <a href="https://github.com/LotusInputMethod/fcitx5-lotus/network/members">
      <img src="https://img.shields.io/github/forks/LotusInputMethod/fcitx5-lotus?style=flat&color=orange" alt="Forks">
    </a>
    <a href="https://github.com/LotusInputMethod/fcitx5-lotus/issues">
      <img src="https://img.shields.io/github/issues/LotusInputMethod/fcitx5-lotus?style=flat&color=red" alt="Issues">
    </a>
    <a href="#contributors-">
      <img src="https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square" alt="All Contributors">
    </a>
  </p>

<p align="center">
    <a href="#cài-đặt"><strong>Cài đặt »</strong></a>
    <br />
    <br />
    <a href="https://github.com/LotusInputMethod/fcitx5-lotus/issues/new?template=bug_report.yml">Báo lỗi</a>
    ·
    <a href="https://github.com/LotusInputMethod/fcitx5-lotus/issues/new?template=feature_request.yml">Yêu cầu tính năng</a>
  </p>
</div>

<br />

Dự án này là bản fork được tối ưu hóa từ [bộ gõ VMK](https://github.com/thanhpy2009/VMK). Chân thành cảm ơn tác giả Thành đã đặt nền móng cho bộ gõ này.

> **Lưu ý:** Gỡ và xoá cấu hình `fcitx5-vmk` trước khi cài đặt `fcitx5-lotus` để tránh phát sinh lỗi.
>
> <details>
> <summary><b>Gỡ và xoá cấu hình <code>fcitx5-vmk</code></b></summary>
>
> <details>
> <summary><b>Arch / Arch-based - AUR</b></summary>
> <br>
>
> Bạn có thể dùng `pacman` (khuyên dùng), `yay` hoặc `paru` để gỡ cài đặt:
>
> ```bash
> sudo pacman -Rns fcitx5-vmk
> ```
>
> ```bash
> yay -Rns fcitx5-vmk
> ```
>
> ```bash
> paru -Rns fcitx5-vmk
> ```
>
> > **Lưu ý:** Các file config ở `$HOME` sẽ được giữ lại.
>
> </details>
>
> <details>
> <summary><b>Debian / Ubuntu / Fedora / openSUSE</b></summary>
> <br>
>
> - <b>Debian/Ubuntu</b>
>
> ```bash
> sudo apt remove fcitx5-vmk
> ```
>
> - <b>Fedora</b>
>
> ```bash
> sudo dnf remove fcitx5-vmk
> ```
>
> - <b>openSUSE</b>
>
> ```bash
> sudo zypper remove fcitx5-vmk
> ```
>
> </details>
>
> <details>
> <summary><b>NixOS</b></summary>
> <br>
>
> Xóa (hoặc comment) dòng `services.fcitx5-vmk` và `inputs` trong file config, sau đó rebuild lại system. NixOS sẽ tự dọn dẹp.
>
> </details>
>
> <details>
> <summary><b>Biên dịch từ nguồn</b></summary>
> <br>
>
> Vào lại thư mục source code đã build và chạy:
>
> ```bash
> sudo make uninstall
> ```
>
> </details>
>
> ---
>
> Xóa cấu hình `vmk` không tương thích:
>
> ```bash
> rm ~/.config/fcitx5/conf/vmk-*.conf
> ```
>
> </details>

<details>
  <summary><b>Mục lục</b></summary>
  <ol>
    <li><a href="#cài-đặt">Cài đặt</a></li>
    <li><a href="#bật-bộ-gõ">Bật bộ gõ</a></li>
    <li><a href="#hướng-dẫn-sử-dụng">Hướng dẫn sử dụng</a></li>
    <li><a href="#gỡ-cài-đặt">Gỡ cài đặt</a></li>
    <li><a href="#đóng-góp">Đóng góp</a></li>
    <li><a href="#giấy-phép">Giấy phép</a></li>
  </ol>
</details>

---

<a id="cài-đặt"></a>

## 📦 Cài đặt

<details>
<summary><b>Arch / Arch-based - AUR</b></summary>
<br>

Hiện tại AUR có 3 gói cài đặt để bạn lựa chọn:

| Gói                | Mô tả                              |
| ------------------ | ---------------------------------- |
| `fcitx5-lotus`     | Build từ mã nguồn release ổn định  |
| `fcitx5-lotus-bin` | Dùng binary đã build sẵn           |
| `fcitx5-lotus-git` | Build từ danh sách commit mới nhất |

Cài đặt bằng `yay`:

```bash
# Cú pháp: yay -S <tên-gói>
yay -S fcitx5-lotus
```

Hoặc `paru`:

```bash
# Cú pháp: paru -S <tên-gói>
paru -S fcitx5-lotus
```

</details>

<details>
<summary><b>Debian / Ubuntu / Fedora / openSUSE</b></summary>
<br>

Bạn có thể xem cách cài của từng distro [tại đây](INSTALL.md).

</details>

<details>
<summary><b>NixOS</b></summary>
<br>

Thêm input của fcitx5-lotus vào `flake.nix`:

```nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    fcitx5-lotus = {
      url = "github:LotusInputMethod/fcitx5-lotus";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {
    self,
  ...
}
```

Bật fcitx5-lotus service trong `configuration.nix`:

```nix
{