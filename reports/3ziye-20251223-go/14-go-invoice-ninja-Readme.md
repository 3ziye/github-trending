<p align="center">
  <img src="assets/banner.svg" alt="Go Invoice Ninja SDK" width="800">
</p>

<h1 align="center">Go Invoice Ninja SDK</h1>

<p align="center">
  <a href="https://pkg.go.dev/github.com/AshkanYarmoradi/go-invoice-ninja"><img src="https://pkg.go.dev/badge/github.com/AshkanYarmoradi/go-invoice-ninja.svg" alt="Go Reference"></a>
  <a href="https://goreportcard.com/report/github.com/AshkanYarmoradi/go-invoice-ninja"><img src="https://goreportcard.com/badge/github.com/AshkanYarmoradi/go-invoice-ninja" alt="Go Report Card"></a>
  <a href="https://github.com/AshkanYarmoradi/go-invoice-ninja/actions/workflows/ci.yml"><img src="https://github.com/AshkanYarmoradi/go-invoice-ninja/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://codecov.io/gh/AshkanYarmoradi/go-invoice-ninja"><img src="https://codecov.io/gh/AshkanYarmoradi/go-invoice-ninja/branch/main/graph/badge.svg" alt="codecov"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
</p>

A professional, idiomatic Go SDK for the [Invoice Ninja](https://invoiceninja.com) API. This SDK provides a clean interface for interacting with Invoice Ninja's comprehensive invoicing and payment platform.

## ✨ Features

- 🔐 **Secure Authentication** - Token-based API authentication
- 💳 **Payment Management** - Full CRUD operations with refund support
- 📄 **Invoice Operations** - Create, send, and manage invoices
- 👥 **Client Management** - Client CRUD with merge capabilities
- 💰 **Credits & Payment Terms** - Complete credit and terms management
- 📥 **File Operations** - Download PDFs and upload documents
- 🔔 **Webhook Handling** - Built-in handler with signature verification
- ⚡ **Rate Limiting** - Client-side limiting with automatic retry
- 🔄 **Retry Logic** - Exponential backoff for transient failures
- 🌐 **Self-hosted Support** - Works with cloud and self-hosted instances
- ✅ **Fully Tested** - 90+ tests with comprehensive coverage

## 📦 Installation

```bash
go get github.com/AshkanYarmoradi/go-invoice-ninja
```

## 📖 Documentation

- [Getting Started](docs/getting-started.md)
- [Authentication](docs/authentication.md)
- [Error Handling](docs/error-handling.md)
- [API Reference](docs/api-reference.md)

## 🏗️ Project Structure

```
go-invoice-ninja/
├── .github/workflows/     # CI/CD pipelines
├── docs/                  # Detailed documentation
├── examples/              # Runnable examples
│   ├── basic/            # Basic usage
│   ├── invoices/         # Invoice operations
│   └── webhooks/         # Webhook handling
├── testdata/              # Test fixtures
│
├── client.go             # Main client
├── clients.go            # Clients service
├── credits.go            # Credits service
├── errors.go             # Error types
├── files.go              # File operations
├── invoices.go           # Invoices service
├── models.go             # Data models
├── payments.go           # Payments service
├── payment_terms.go      # Payment terms
├── retry.go              # Retry & rate limiting
├── webhooks.go           # Webhook handling
│
├── CHANGELOG.md          # Version history
├── CONTRIBUTING.md       # Contribution guide
├── LICENSE               # MIT License
├── Makefile              # Build automation
└── README.md             # This file
```

## 🚀 Quick Start

```go
package main

import (
    "context"
    "fmt"
    "log"

    invoiceninja "github.com/AshkanYarmoradi/go-invoice-ninja"
)

func main() {
    // Create a new client
    client := invoiceninja.NewClient("your-api-token")
    
    // For self-hosted instances:
    // client := invoiceninja.NewClient("your-api-token", 
    //     invoiceninja.WithBaseURL("https://your-instance.com"))

    ctx := context.Background()

    // List payments
    payments, err := client.Payments.List(ctx, &invoiceninja.PaymentListOptions{
        PerPage: 10,
        Page:    1,
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, payment := range payments.Data {
        fmt.Printf("Payment %s: $%.2f\n", payment.Number, payment.Amount)
    }
}
```

## 🔑 Authentication

All API requests require an API token. You can obtain your token from:
**Settings > Account Management > Integrations > API tokens**

```go
client := invoiceninja.NewClient("your-api-token")
```

## ⚙️ Configuration Options

```go
// Custom HTTP client
client := invoiceninja.NewClient("token",
    invoiceninja.WithHTTPClient(customHTTPClient))

// Custom base URL (for self-hosted)
client := invoiceninja.NewClient("token",
    invoiceninja.WithBaseURL("https://your-instance.com"))

// Custom timeout
client := invoiceninja.NewClient("token",
    invoiceninja.WithTimeout(60 * time.Second))
```

## 💳 Payments

### List Payments

```go
payments, err := client.Payments.List(ctx, &invoiceninja.PaymentListOptions{
    PerPage:  20,
    Page:     1,
    ClientID: "client-hash-id",
    Status:   "active",
    Sort:     "amount|desc",
})
```
