[English](README.en.md) | [Tiếng Việt](README.md)

<a id="readme-top"></a>

<div align="center">
  <a href="https://lotusinputmethod.github.io/">
    <img src="data/fcitx-lotus-README.svg" alt="Logo" width="80" height="80">
  </a>

<h2 align="center">Fcitx5 Lotus</h2>

<p align="center">
    <b>Bộ gõ tiếng Việt đơn giản, hiệu năng cao cho Linux</b>
    <br />
    <a href="https://lotusinputmethod.github.io/"><strong>Khám phá trang chủ »</strong></a>
    <br />
    <br />
    <a href="https://github.com/LotusInputMethod/fcitx5-lotus/releases">
      <img src="https://img.shields.io/github/v/release/LotusInputMethod/fcitx5-lotus?style=flat&color=success" alt="Release">
    </a>
    <a href="https://github.com/LotusInputMethod/fcitx5-lotus/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/LotusInputMethod/fcitx5-lotus?style=flat&color=blue" alt="License">
    </a>
    <a href="https://lotusinputmethod.github.io/">
      <img src="https://img.shields.io/badge/website-live-brightgreen?style=flat&logo=firefox&logoColor=white" alt="Website">
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
    <a href="https://deepwiki.com/LotusInputMethod/fcitx5-lotus"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
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

<sub>💡 Bấm vào phần bên cạnh badge để mở rộng hướng dẫn.</sub>

<details>
<summary><a href="#cài-đặt"><img src="https://img.shields.io/badge/Arch_Linux-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white" alt="Arch Linux" height="25"></a></summary>
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
<summary><a href="#cài-đặt"><img src="https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white" alt="Debian" height="25"></a></summary>
<br>

```bash
# Tự động nhận diện codename và cài đặt
CODENAME=$(grep '^VERSION_CODENAME=' /etc/os-release | cut -d'=' -f2)
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://fcitx5-lotus.pages.dev/pubkey.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/fcitx5-lotus.gpg
echo "deb [signed-by=/etc/apt/keyrings/fcitx5-lotus.gpg] https://fcitx5-lotus.pages.dev/apt/$CODENAME $CODENAME main" | sudo tee /etc/apt/sources.list.d/fcitx5-lotus.list
sudo apt update && sudo apt install fcitx5-lotus
```

</details>

<details>
<summary><a href="#cài-đặt"><img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" alt="Ubuntu" height="25"></a></summary>
<br>

```bash
# Tự động nhận diện codename và cài đặt
CODENAME=$(grep '^UBUNTU_CODENAME=' /etc/os-release | cut -d'=' -f2)
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://fcitx5-lotus.pages.dev/pubkey.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/fcitx5-lotus.gpg
echo "deb [signed-by=/etc/apt/keyrings/fcitx5-lotus.gpg] https://fcitx5-lotus.pages.dev/apt/$CODENAME $CODENAME main" | sudo tee /etc/apt/sources.list.d/fcitx5-lotus.l