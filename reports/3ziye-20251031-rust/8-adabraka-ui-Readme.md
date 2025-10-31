# adabraka-ui

[![Crates.io](https://img.shields.io/crates/v/adabraka-ui.svg)](https://crates.io/crates/adabraka-ui)
[![Downloads](https://img.shields.io/crates/d/adabraka-ui.svg)](https://crates.io/crates/adabraka-ui)
[![Documentation](https://docs.rs/adabraka-ui/badge.svg)](https://docs.rs/adabraka-ui)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Rust](https://img.shields.io/badge/rust-nightly-orange.svg)](https://www.rust-lang.org/)
[![GitHub Stars](https://img.shields.io/github/stars/Augani/adabraka-ui?style=social)](https://github.com/Augani/adabraka-ui)

A comprehensive, professional UI component library for [GPUI](https://github.com/zed-industries/zed), the GPU-accelerated UI framework powering the Zed editor. Inspired by [shadcn/ui](https://ui.shadcn.com/), adabraka-ui provides 73+ polished, accessible components for building beautiful desktop applications in Rust.

**[📖 Documentation](https://augani.github.io/adabraka-ui/)** · **[🚀 Getting Started](#installation)** · **[📦 Components](#components)** · **[💡 Examples](#examples)**

## ✨ Features

- 🎨 **Complete Theme System** - Built-in light/dark themes with semantic color tokens
- 🧩 **73+ Components** - Comprehensive library covering all UI needs from buttons to data tables
- 📱 **Responsive Layout** - Flexible layout utilities (VStack, HStack, Grid)
- 🎭 **Professional Animations** - Smooth transitions with cubic-bezier easing and spring physics
- ✍️ **Typography System** - Built-in Text component with semantic variants
- 💻 **Code Editor** - Multi-line editor with syntax highlighting and full keyboard support
- ♿ **Accessibility** - Full keyboard navigation, ARIA labels, and screen reader support
- 🎯 **Type-Safe** - Leverages Rust's type system for compile-time guarantees
- 🚀 **High Performance** - Optimized for GPUI's retained-mode rendering with virtual scrolling
- 📚 **Well Documented** - Extensive examples and comprehensive API documentation

## 🎬 Showcase

See adabraka-ui in action in real applications:

### Desktop Music Player
![Music Player App](docs/assets/images/music-player.png)

A beautiful desktop music player with offline playing capabilities. Features smooth animations, responsive UI, and a polished user experience built entirely with adabraka-ui components.

### Project Task Manager
![Task Manager App](docs/assets/images/task-manager.png)

A powerful task management application used to track the development of this UI library. Features drag-and-drop task organization with smooth animations, showcasing the library's advanced capabilities.

## 🚀 Installation

> **Note:** Currently requires Rust nightly due to GPUI dependencies. Install with: `rustup toolchain install nightly`

Add adabraka-ui to your `Cargo.toml`:

```toml
[dependencies]
adabraka-ui = "0.2.2"
gpui = "0.2.0"
```

Build your project with nightly:
```bash
cargo +nightly build
```

## ✨ What's New in v0.2.2

**Latest Release (October 28, 2025)** - Improved form usability and documentation!

### 🔐 Password Input Fixed
The password input eye icon now properly toggles between masked (••••) and visible text with immediate state updates. Click the eye icon to reveal or hide your password.

```rust
Input::new(password_input, cx)
    .password(true)  // Enables eye icon toggle
    .placeholder("Enter password")
```

### ⌨️ Tab Navigation
Added full keyboard navigation support between form inputs. Press Tab to move to the next input, Shift-Tab to go back. Works automatically with proper FocusHandle configuration.

```rust
// Tab navigation works automatically
Input::new(&email_input, cx).placeholder("Email")
Input::new(&password_input, cx).password(true).placeholder("Password")
// Press Tab to move between inputs!
```

### 🗺️ Comprehensive Roadmap
New [ROADMAP.md](ROADMAP.md) with complete component inventory (73+ components), phase-based development plan, and prioritized quick wins for desktop integration features.

### 🧹 Code Quality
Removed 13 unnecessary inline comments across 6 files for a cleaner, more production-ready codebase.

---

## Quick Start

```rust
use adabraka_ui::prelude::*;
use gpui::*;

fn main() {
    Application::new().run(|cx| {
        // Initialize the UI library
        adabraka_ui::init(cx);

        // Install a theme
        install_theme(cx, Theme::dark());

        cx.open_window(
            WindowOptions {
                titlebar: Some(TitlebarOptions {
                    title: Some("My App".into()),
                    ..Default::default()
                }),
                ..Default::default()
            },
            |_, cx| cx.new(|_| MyApp::new()),
        ).unwrap();
    });
}

struct MyApp;

impl MyApp {
    fn new() -> Self {
        Self
    }
}

impl Render for MyApp {
    fn render(&mut self, _window: &mut Window, cx: &mut Context<Self>) -> impl IntoElement {
        VStack::new()
            .p(px(32.0))
            .gap(px(16.0))
            .child(
                d