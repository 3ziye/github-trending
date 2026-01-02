<h1 align="center">
  <img src="assets/logo.png" alt="Gõ Nhanh Logo" width="128" height="128"><br>
  Gõ Nhanh
</h1>

<p align="center">
  <img src="https://img.shields.io/github/downloads/khaphanspace/gonhanh.org/total?label=Downloads" />
  <img src="https://img.shields.io/github/contributors/khaphanspace/gonhanh.org" />
  <img src="https://img.shields.io/github/last-commit/khaphanspace/gonhanh.org" />
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Platform-macOS-000000?logo=apple&logoColor=white" />
  <img src="https://img.shields.io/badge/Platform-Linux-FCC624?logo=linux&logoColor=black" />
  <img src="https://img.shields.io/badge/License-BSD--3--Clause-blue.svg" alt="License: BSD-3-Clause">
  <img src="https://github.com/khaphanspace/gonhanh.org/actions/workflows/ci.yml/badge.svg" alt="CI">
</p>

<p align="center">
  <strong>Bộ gõ tiếng Việt miễn phí, nhanh, ổn định cho macOS.</strong><br>
  Cài là dùng. Không quảng cáo. Không thu thập dữ liệu.
</p>

<p align="center">
  <img src="assets/screenshot.png" alt="Gõ Nhanh Light Mode" width="100%">
</p>

---

## 📥 Tải về & Cài đặt

### 🍺 Homebrew (macOS - Khuyến nghị)

```bash
brew install --cask gonhanh
```

> **Cập nhật:** App tự động kiểm tra phiên bản mới mỗi 24h. Hoặc dùng `brew upgrade --cask gonhanh`.

### 📦 Tải thủ công

| Nền tảng | Trạng thái | Tải xuống | Hướng dẫn |
|:--------:|:----------:|:---------:|:----------|
| **macOS** | ✅ Sẵn sàng | [📥 Tải GoNhanh.dmg](https://github.com/khaphanspace/gonhanh.org/releases/latest/download/GoNhanh.dmg) | [Xem hướng dẫn](docs/install-macos.md) |
| **Linux** | 🧪 Beta | — | [Xem hướng dẫn](docs/install-linux.md) |
| **Windows** | 🧪 Beta | — | [Xem hướng dẫn](docs/install-windows.md) |

<details>
<summary><strong>⚠️ macOS: App không mở được?</strong></summary>

```bash
# Chạy lệnh này trong Terminal sau khi kéo app vào Applications
xattr -cr /Applications/GoNhanh.app
```

Sau đó: **System Settings → Privacy & Security → Accessibility → Bật GoNhanh**

</details>

## ✨ Tính năng

### 🔥 Highlight

- 🔍 **Fix lỗi Chrome/Spotlight/Arc/Claude Code/JetBrains** - Tự động sửa dính chữ trong address bar, thanh tìm kiếm, Arc history
- 🔤 **Auto-restore tiếng Anh** — Gõ `text` `expect` `user` `push` `sort` → tự khôi phục khi nhấn space. [Xem chi tiết ↓](#-auto-restore-tiếng-anh)
- ⎋ **Gõ ESC tự khôi phục** — Gõ `user` → `úẻ` → nhấn **ESC** → `user`. Không cần tắt bộ gõ khi gõ tiếng Anh!
- 🧠 **Chuyển chế độ thông minh** — Tự nhớ ON/OFF cho từng app. Code trên VS Code (tắt) → Chat trên Slack (bật) → tự chuyển
- 🔄 **Tự động theo input source** — Dùng tiếng Nhật, Hàn, Trung... → Gõ Nhanh tự tắt. Chuyển về tiếng Anh → tự bật lại
- ⚡ **Siêu nhanh** — <1ms latency · ~5MB RAM. Hỗ trợ đa nền tảng trên cùng một engine


<p align="center">
  <video src="https://github.com/user-attachments/assets/957ec6c6-d6df-4ca9-9161-0a1bb6cf98ce" width="100%"></video>
</p>

### 📋 Đầy đủ

- ⌨️ **Telex & VNI** — Chọn kiểu gõ quen thuộc
- 🎯 **Đặt dấu chuẩn** — Tự động theo [quy tắc mới](https://vi.wikipedia.org/wiki/Quy_t%E1%BA%AFc_%C4%91%E1%BA%B7t_d%E1%BA%A5u_thanh_c%E1%BB%A7a_ch%E1%BB%AF_Qu%E1%BB%91c_ng%E1%BB%AF): `hoà`, `khoẻ`, `thuỷ`
- 🔠 **Tự viết hoa đầu câu** — Gõ `ok.` Space `b` → `B` hoa. Hỗ trợ `.` `!` `?` và Enter
- ✂️ **Gõ tắt** — `vn` → `Việt Nam`, `ko` → `không`
- 🔌 **Mọi app** — VS Code, Zed, Chrome, Notion, Terminal, Ghostty...
- 🌗 **Dark/Light** — Theo hệ thống
- 💻 **Đa nền tảng** — macOS, Linux, Windows (beta)

### 🛡️ Cam kết "Ba Không"

- 🚫 **Không thu phí** — Miễn phí mãi mãi, không bản Pro
- 🚫 **Không quảng cáo** — Không popup, không làm phiền
- 🚫 **Không theo dõi** — Offline 100%, mã nguồn mở

---

## 🔤 Auto-restore tiếng Anh

Khi gõ tiếng Anh bằng Telex, một số chữ cái bị nhận nhầm thành modifier tiếng Việt:
- `s` → sắc, `f` → huyền, `r` → hỏi, `x` → ngã, `j` → nặng
- `w` → dấu móc (ư, ơ)

**Gõ Nhanh tự động khôi phục** khi nhấn **Space** nếu phát hiện pattern tiếng Anh.

### ✅ Các pattern được nhận diện

| Pattern | Ví dụ | Giải thích |
|:--------|:------|:-----------|
| **Modifier + phụ âm** | `text` `next` `test` `expect` `express` | x/s theo sau bởi phụ âm (t, p, c...) |
| **EI + modifier** | `their` `weird` | Cặp nguyên âm "ei" + r/s/f... |
| **P + AI + modifier** | `pair` | P đầu (hiếm trong tiếng Việt) + ai |
| **Nguyên âm + modifier + nguyên âm** | `use` `user` | Không có phụ âm đầu |
| **W đầu + phụ âm** | `window` `water` `write` `what` | W không phải phụ âm đầu tiếng Việt |
| **W + nguyên + W** | `wow` | Pattern "wow" đặc trưng tiếng Anh |
| **F đầu** | `file` `fix` `function` `firebase` | F không tồn tại trong tiếng Việt |

### 📝 So sánh: macOS Telex vs Gõ Nhanh

| Gõ | macOS Telex | Gõ Nhanh |
|:---|:------------|:---------|
| `text ` | `têt ` ❌ | `text ` ✅ |
| `expect ` | `ễpct ` ❌ | `expect ` ✅ |
| `perfect ` | `pềct ` ❌ | `perfect ` ✅ |
| `window ` | `ưindow ` ❌ | `window ` ✅ |
| `with ` | `ưith ` ❌ | `with ` ✅ |
| `tesla ` | `téla ` ❌ | `tesla ` ✅ |
| `luxury ` | `lủuy ` ❌ | `luxury ` ✅ |
| `case `