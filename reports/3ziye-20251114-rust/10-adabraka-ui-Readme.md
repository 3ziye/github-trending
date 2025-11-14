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
adabraka-ui = "0.2.3"
gpui = "0.2.0"
```

Build your project with nightly:
```bash
cargo +nightly build
```

## ✨ What's New in v0.2.3

**Latest Release (November 13, 2025)** - Enhanced slider component with vertical orientation support!

### 📊 Vertical Slider Support
The Slider component now supports both horizontal and vertical orientations. Perfect for volume controls, brightness adjustments, and other vertical UI patterns.

```rust
// Horizontal slider (default)
Slider::new(slider_state.clone())
    .show_value(true)

// Vertical slider
Slider::new(slider_state.clone())
    .vertical()
    .size(SliderSize::Lg)
    .show_value(true)
    .on_change(|value, _, _| {
        println!("Value: {}", value);
    })
```

### 🐛 Slider Thumb Centering Fixed
The slider thumb is now perfectly centered on the track line, providing a more polished and professional appearance across all size variants (Sm, Md, Lg).

### 🎨 Improved Component Architecture
- Separate `render_horizontal()` and `render_vertical()` methods for cleaner code
- Adaptive thumb shape: horizontal oval for horizontal sliders, vertical oval for vertical sliders
- Better positioning logic using container dimensions matching thumb dimensions

### 📚 Enhanced Examples
Updated `slider_styled_demo.rs` with 10 comprehensive examples showcasing horizontal and vertical sliders with various styling options.

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
        VSt