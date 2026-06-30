# ainovel-cli — Bản tiếng Việt

> **Fork tiếng Việt** của [voocel/ainovel-cli](https://github.com/voocel/ainovel-cli) — toàn bộ giao diện, prompt hệ thống và tài liệu đã được Việt hoá.

Công cụ CLI sáng tác tiểu thuyết dài kỳ hoàn toàn tự động bằng AI. Từ **một câu yêu cầu** đến **tiểu thuyết hoàn chỉnh** — không cần can thiệp thủ công trong quá trình viết.

<p align="center">
  <img src="scripts/sample.gif" alt="ainovel-cli demo" width="800">
</p>

---

## Mục lục

1. [Tính năng nổi bật](#tính-năng-nổi-bật)
2. [Kiến trúc hệ thống](#kiến-trúc-hệ-thống)
3. [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
4. [Cài đặt nhanh](#cài-đặt-nhanh)
   - [Docker (khuyến nghị)](#docker-khuyến-nghị)
   - [Build từ source](#build-từ-source)
5. [Cấu hình](#cấu-hình)
   - [Ollama (local, miễn phí)](#ollama-local-miễn-phí)
   - [OpenRouter](#openrouter)
   - [Anthropic / OpenAI](#anthropic--openai)
   - [Cấu hình nhiều model theo vai trò](#cấu-hình-nhiều-model-theo-vai-trò)
6. [Bắt đầu viết](#bắt-đầu-viết)
7. [Lệnh TUI](#lệnh-tui)
8. [Can thiệp thời gian thực](#can-thiệp-thời-gian-thực)
9. [Phong cách và quy tắc tuỳ chỉnh](#phong-cách-và-quy-tắc-tuỳ-chỉnh)
10. [Khôi phục sau gián đoạn](#khôi-phục-sau-gián-đoạn)
11. [Cấu trúc thư mục output](#cấu-trúc-thư-mục-output)
12. [Xuất truyện](#xuất-truyện)
13. [Troubleshooting](#troubleshooting)

---

## Tính năng nổi bật

| Tính năng | Mô tả |
|---|---|
| **Đa agent tự chủ** | Điều phối viên điều phối Kiến trúc sư → Người viết → Biên tập viên trong một vòng lặp LLM duy nhất |
| **Viết hoàn chỉnh không cần trực** | Nhập một câu, hệ thống tự xây dựng thế giới, lập đề cương, viết và đánh giá toàn bộ |
| **Hỗ trợ 500+ chương** | Quản lý ngữ cảnh 3 tầng (chương → cung → tập), tự động nén khi đầy |
| **Kế hoạch cuộn** | Không lập kế hoạch toàn bộ một lần. Cung/tập sau mở rộng dần khi cần, tránh đề cương rỗng tuếch |
| **Khôi phục cấp step** | Checkpoint sau mỗi lần gọi công cụ thành công — crash/mất mạng/Ctrl+C đều khôi phục chính xác |
| **Can thiệp thời gian thực** | Nhập ý kiến chỉnh sửa bất cứ lúc nào, không cần dừng, hệ thống tự đánh giá phạm vi ảnh hưởng |
| **Đánh giá 7 chiều** | Biên tập viên đánh giá: tính nhất quán, nhân vật, nhịp truyện, mạch kể, phục bút, điểm móc, thẩm mỹ |
| **Chống văn phong AI** | Bộ tiêu chí cơ học + ngữ nghĩa tích hợp sẵn, tự động kiểm tra khi lưu chương |
| **Nhiều nhà cung cấp LLM** | OpenRouter, Anthropic, Gemini, OpenAI, Deepseek, Ollama (local), và proxy tuỳ chỉnh |

---

## Kiến trúc hệ thống

```
┌──────────────────────────────────────────────────┐
│                  Host (vỏ mỏng)                   │
│   Khởi động / Khôi phục / Quan sát / Can thiệp    │
└───────────────────────┬──────────────────────────┘
                        │ Một lần Prompt
┌───────────────────────▼──────────────────────────┐
│          Coordinator (vòng lặp dài LLM)           │
│  Đọc ngữ cảnh → Gọi agent phụ → Đọc kết quả → Tiếp tục │
└────┬───────────┬──────────┬──────────────────────┘
     │           │          │
┌────▼───┐  ┌───▼───┐  ┌───▼────┐
│Architect│  │Writer │  │ Editor │
└────┬───┘  └───┬───┘  └───┬────┘
     └──────────┼───────────┘
                │ Gọi công cụ (IO + checkpoint)
┌───────────────▼──────────────────────────────────┐
│                    Store                          │
│  Progress / Checkpoint / Outline / Drafts / ...  │
└──────────────────────────────────────────────────┘
```

**Nguyên tắc cốt lõi**: LLM quyết định mọi thứ về nội dung và luồng sáng tác. Host chỉ khởi động, quan sát và cung cấp dữ liệu sự thật. Càng ít code, càng ít chỗ hỏng.

---

## Yêu cầu hệ thống

| Phương pháp | Yêu cầu |
|---|---|
| **Docker** (khuyến nghị) | Docker Desktop ≥ 24, 4 GB RAM trống |
| **Build từ source** | Go ≥ 1.21 |
| **Model AI** | API key từ nhà cung cấp, hoặc Ollama chạy local |

> **Windows**: Khuyến nghị dùng Docker. Không cần cài Go.

---

## Cài đặt nhanh

### Docker (khuyến nghị)

**Bước 1** — Tải source và chuẩn bị thư mục:

```bash
git clone https://github.com/<your-username>/ainovel-cli.git
cd ainovel-cli
mkdir config workspace
```

**Bước 2** — Build Docker image:

```bash
docker build -t ainovel-cli-vi .
```

> Lần đầu mất 2–5 phút do tải Go dependencies. Các lần sau dùng cache, rất nhanh.

**Bước 3** — Tạo file cấu hình `config/config.json` (xem [phần Cấu hình bên dưới](#cấu-hình)).

**Bước 4** — Chạy TUI:

```bash
# Linux / macOS
docker run --rm -it \
  -v "$PWD/config:/root/.ainovel" \
  -v "$PWD/workspace:/workspace" \
  -e TERM=xterm-256color \
  ainovel-cli-vi

# Windows (PowerShell)
docker run --rm -it `
  -v "${PWD}\config:/root/.ainovel" `
  -v "${PWD}\workspace:/workspace" `
  -e TERM=xterm-256color `
  ainovel-cli-vi

# Windows (Command Prompt)
docker run --rm -it -v "%CD%\config:/root/.ainovel" -v "%CD%\workspace:/workspace" -e TERM=xterm-256color ainovel-cli-vi
```

> **Windows Terminal**: Mở tab mới tự động —
> ```powershell
> Start-Process "wt.exe" -ArgumentList "new-tab", "cmd", "/k", 'docker run --rm -it -v "%CD%\config:/root/.ainovel"