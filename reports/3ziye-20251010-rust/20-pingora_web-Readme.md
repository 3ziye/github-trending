# 🚀 pingora_web

[![CI](https://github.com/pingora-web/pingora_web/actions/workflows/ci.yml/badge.svg)](https://github.com/pingora-web/pingora_web/actions/workflows/ci.yml)
[![Crates.io](https://img.shields.io/crates/v/pingora_web.svg)](https://crates.io/crates/pingora_web)
[![Documentation](https://docs.rs/pingora_web/badge.svg)](https://docs.rs/pingora_web)
[![License](https://img.shields.io/badge/license-MIT%2FApache--2.0-blue.svg)](LICENSE)
[![Downloads](https://img.shields.io/crates/d/pingora_web.svg)](https://crates.io/crates/pingora_web)
[![Stars](https://img.shields.io/github/stars/pingora-web/pingora_web.svg)](https://github.com/pingora-web/pingora_web)

**🔥 Fast setup | Built on Pingora | Beginner friendly** 🦀

[English](README.md) | [中文](README_zh.md)

A web framework built on Cloudflare's Pingora proxy infrastructure, designed to be fast, reliable, and easy to use.

## ✨ Features

### Core Features
- 🛣️ **Path routing** with parameters (`/users/{id}`)
- 🧅 **Middleware system** with onion model (like Express.js)
- 🏷️ **Request ID tracking** (automatic `x-request-id` header)
- 📝 **Structured logging** with tracing integration
- 📦 **JSON support** with automatic serialization
- 📁 **Static file serving** with MIME type detection
- 🌊 **Streaming responses** for large data transfers

### Built on Pingora
- ⚡ **High performance** - leverages Cloudflare's production-tested proxy
- 🗜️ **HTTP compression** - built-in gzip support
- 🛡️ **Request limits** - timeout, body size, and header constraints
- 🚨 **Panic recovery** - automatic error handling
- 🔗 **HTTP/1.1 & HTTP/2** support via Pingora

## 🚀 Quick Start

### 1. Create a new project
```bash
cargo new my_api && cd my_api
```

### 2. Add dependencies to `Cargo.toml`

**Minimal setup (Hello World):**
```toml
[dependencies]
pingora_web = "0.1"
```

**Full setup (with JSON, logging, etc.):**
```toml
[dependencies]
pingora_web = "0.1"
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
tracing-subscriber = { version = "0.3", features = ["env-filter"] }
```

### 3. Hello World (5 lines - like Express/Gin)

```rust
use pingora_web::{App, StatusCode, PingoraWebHttpResponse, WebError, PingoraHttpRequest};

fn main() {
    let mut app = App::default();
    app.get_fn("/", |_req: PingoraHttpRequest| -> Result<PingoraWebHttpResponse, WebError> {
        Ok(PingoraWebHttpResponse::text(StatusCode::OK, "Hello World!"))
    });
    app.listen("0.0.0.0:8080").unwrap();
}
```

### 4. With Parameters (beginner-friendly)

```rust
use pingora_web::{App, StatusCode, PingoraWebHttpResponse, WebError, PingoraHttpRequest};

fn main() {
    let mut app = App::default();
    app.get_fn("/", |_req: PingoraHttpRequest| -> Result<PingoraWebHttpResponse, WebError> {
        Ok(PingoraWebHttpResponse::text(StatusCode::OK, "Hello World!"))
    });
    app.get_fn("/hi/{name}", |req: PingoraHttpRequest| -> Result<PingoraWebHttpResponse, WebError> {
        let name = req.param("name").unwrap_or("world");
        Ok(PingoraWebHttpResponse::text(StatusCode::OK, format!("Hello {}", name)))
    });
    app.listen("0.0.0.0:8080").unwrap();
}
```

### 5. Full-featured example

```rust
use async_trait::async_trait;
use pingora_web::{App, Handler, StatusCode, TracingMiddleware, ResponseCompressionBuilder, WebError, PingoraHttpRequest, PingoraWebHttpResponse};
use std::sync::Arc;

struct Hello;
#[async_trait]
impl Handler for Hello {
    async fn handle(&self, req: PingoraHttpRequest) -> Result<PingoraWebHttpResponse, WebError> {
        let name = req.param("name").unwrap_or("world");
        Ok(PingoraWebHttpResponse::text(StatusCode::OK, format!("Hello {}", name)))
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter("info")
        .init();

    let mut app = App::default();
    app.get("/hi/{name}", Arc::new(Hello));
    app.use_middleware(TracingMiddleware::new());
    app.add_http_module(ResponseCompressionBuilder::enable(6));

    app.listen("0.0.0.0:8080").unwrap();
}
```

### 6. Run the server
```bash
cargo run
```

Visit `http://localhost:8080/` or `http://localhost:8080/hi/world` to see it working!

### Advanced usage (for complex setups)

If you need more control over the server configuration:

```rust
use async_trait::async_trait;
use pingora_web::{App, Handler, StatusCode, WebError, PingoraHttpRequest, PingoraWebHttpResponse};
use pingora::server::Server;
use std::sync::Arc;

struct Hello;
#[async_trait]
impl Handler for Hello {
    async fn handle(&self, req: PingoraHttpRequest) -> Result<PingoraWebHttpResponse, WebError> {
        let name = req.param("name").unwrap_or("world");
        Ok(PingoraWebHttpResponse::text(StatusCode::OK, format!("Hello {}", name)))
    }
}

fn main() {
    let mut app = App::default();
    app.get("/hi/{name}", Arc::new(Hello));
    let app = app;

    // Advanced: Convert to service for more control
    let mut service = app.to_service("my-web-app");
    service.add_tcp("0.0.0.0:8080");
    service.add_tcp