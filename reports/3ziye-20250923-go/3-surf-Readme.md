<p align="center">
  <img src="https://user-images.githubusercontent.com/65846651/233453773-33f38b64-0adc-41b4-8e13-a49c89bf9db6.png">
</p>

<h1>Surf - Advanced HTTP Client for Go</h1>

[![Go Reference](https://pkg.go.dev/badge/github.com/enetx/surf.svg)](https://pkg.go.dev/github.com/enetx/surf)
[![Go Report Card](https://goreportcard.com/badge/github.com/enetx/surf)](https://goreportcard.com/report/github.com/enetx/surf)
[![Coverage Status](https://coveralls.io/repos/github/enetx/surf/badge.svg?branch=main&service=github)](https://coveralls.io/github/enetx/surf?branch=main)
[![Go](https://github.com/enetx/surf/actions/workflows/go.yml/badge.svg)](https://github.com/enetx/surf/actions/workflows/go.yml)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/enetx/surf)

<p>Surf is a powerful, feature-rich HTTP client library for Go that makes working with HTTP requests intuitive and enjoyable. With advanced features like browser impersonation, JA3/JA4 fingerprinting, and comprehensive middleware support, Surf provides everything you need for modern web interactions.</p>

## ✨ Key Features

### 🎭 **Browser Impersonation**
- **Chrome & Firefox Support**: Accurately mimic Chrome v131 and Firefox v143 browser fingerprints
- **Platform Diversity**: Impersonate Windows, macOS, Linux, Android, and iOS devices
- **TLS Fingerprinting**: Full JA3/JA4 fingerprint customization for enhanced privacy
- **Automatic Headers**: Proper header ordering and browser-specific values
- **WebKit Form Boundaries**: Accurate multipart form boundary generation matching real browsers

### 🔒 **Advanced TLS & Security**
- **Custom JA3/JA4**: Configure precise TLS fingerprints with `HelloID` and `HelloSpec`
- **HTTP/3 Support**: Full HTTP/3 over QUIC with complete browser-specific QUIC fingerprinting
- **JA4QUIC Fingerprinting**: Complete QUIC transport parameter fingerprinting for Chrome and Firefox
- **HTTP/2 & HTTP/3**: Full HTTP/2 support with customizable settings (SETTINGS frame, window size, priority)
- **Ordered Headers**: Browser-accurate header ordering for perfect fingerprint evasion
- **Certificate Pinning**: Custom TLS certificate validation
- **DNS-over-TLS**: Enhanced privacy with DoT support
- **Proxy Support**: HTTP, HTTPS, and SOCKS5 proxy configurations with UDP support for HTTP/3

### 🚀 **Performance & Reliability**
- **Connection Pooling**: Efficient connection reuse with singleton pattern
- **Automatic Retries**: Configurable retry logic with custom status codes
- **Response Caching**: Built-in body caching for repeated access
- **Streaming Support**: Efficient handling of large responses and SSE
- **Compression**: Automatic decompression of gzip, deflate, brotli, and zstd responses
- **Keep-Alive**: Persistent connections with configurable parameters

### 🛠️ **Developer Experience**
- **Standard Library Compatible**: Convert to `net/http.Client` for third-party library integration
- **Fluent API**: Chainable methods for elegant code
- **Middleware System**: Extensible request/response/client middleware with priority support
- **Type Safety**: Strong typing with generics support via [enetx/g](https://github.com/enetx/g)
- **Debug Mode**: Comprehensive request/response debugging
- **Error Handling**: Result type pattern for better error management
- **Context Support**: Full context.Context integration for cancellation and timeouts

## 📦 Installation

```bash
go get -u github.com/enetx/surf
```

**Required Go version:** 1.24+

## 🔄 Standard Library Compatibility

Surf provides seamless integration with Go's standard `net/http` package, allowing you to use Surf's advanced features with any library that expects a standard `*http.Client`.

```go
// Create a Surf client with advanced features
surfClient := surf.NewClient().
    Builder().
    Impersonate().Chrome().
    Session().
    Build()

// Convert to standard net/http.Client
stdClient := surfClient.Std()

// Use with any third-party library
// Example: AWS SDK, Google APIs, OpenAI client, etc.
resp, err := stdClient.Get("https://api.example.com")
```

**Preserved Features When Using Std():**
- ✅ JA3/TLS fingerprinting
- ✅ HTTP/2 settings
- ✅ HTTP/3 & QUIC fingerprinting
- ✅ Browser impersonation headers
- ✅ Ordered headers
- ✅ Cookies and sessions
- ✅ Proxy configuration
- ✅ Custom headers and User-Agent
- ✅ Timeout settings
- ✅ Redirect policies
- ✅ Request/Response middleware

**Limitations with Std():**
- ❌ Retry logic (implement at application level)
- ❌ Response body caching
- ❌ Remote address tracking
- ❌ Request timing information

## 🚀 Quick Start

### Basic GET Request

```go
package main

import (
    "fmt"
    "log"
    "github.com/enetx/surf"
)

func main() {
    resp := surf.NewClient().Get("https://api.github.com/users/github").Do()
    if resp.IsErr() {
        log.Fatal(resp.Err())
    }

    fmt.Println(resp.Ok().Body.String())
}
```

### JSON Response Handling

```go
type User struct {
    Name     string `json:"name"`
    Company