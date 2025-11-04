# Sa-Token-Go

**English** | **[中文](README_zh.md)**

[![Go Version](https://img.shields.io/badge/Go-%3E%3D1.21-blue)](https://img.shields.io)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)

A lightweight, high-performance Go authentication and authorization framework, inspired by [sa-token](https://github.com/dromara/sa-token).

## ✨ Core Features

- 🔐 **Authentication** - Multi-device login, Token management
- 🛡️ **Authorization** - Fine-grained permission control, wildcard support (`*`, `user:*`, `user:*:view`)
- 👥 **Role Management** - Flexible role authorization mechanism
- 🚫 **Account Ban** - Temporary/permanent account disabling
- 👢 **Kickout** - Force user logout, multi-device mutual exclusion
- 💾 **Session Management** - Complete Session management
- ⏰ **Active Detection** - Automatic token activity detection
- 🔄 **Auto Renewal** - Asynchronous token auto-renewal (400% performance improvement)
- 🎨 **Annotation Support** - `@SaCheckLogin`, `@SaCheckRole`, `@SaCheckPermission`
- 🎧 **Event System** - Powerful event system with priority and async execution
- 📦 **Modular Design** - Import only what you need, minimal dependencies
- 🔒 **Nonce Anti-Replay** - Prevent replay attacks with one-time tokens
- 🔄 **Refresh Token** - Refresh token mechanism with seamless refresh
- 🔐 **OAuth2** - Complete OAuth2 authorization code flow implementation

## 🚀 Quick Start

### 📥 Installation

#### Option 1: Simplified Import (Recommended) ✨

**Import only one framework integration package, which automatically includes core and stputil!**

```bash
# Import only the framework integration (includes core + stputil automatically)
go get github.com/click33/sa-token-go/integrations/gin@v0.1.2    # Gin framework
# or
go get github.com/click33/sa-token-go/integrations/echo@v0.1.2   # Echo framework
# or
go get github.com/click33/sa-token-go/integrations/fiber@v0.1.2  # Fiber framework
# or
go get github.com/click33/sa-token-go/integrations/chi@v0.1.2    # Chi framework
# or
go get github.com/click33/sa-token-go/integrations/gf@v0.1.2     # GoFrame framework

# Storage module (choose one)
go get github.com/click33/sa-token-go/storage/memory@v0.1.2  # Memory storage (dev)
go get github.com/click33/sa-token-go/storage/redis@v0.1.2   # Redis storage (prod)
```

#### Option 2: Separate Import

```bash
# Core modules
go get github.com/click33/sa-token-go/core@v0.1.2
go get github.com/click33/sa-token-go/stputil@v0.1.2

# Storage module (choose one)
go get github.com/click33/sa-token-go/storage/memory@v0.1.2  # Memory storage (dev)
go get github.com/click33/sa-token-go/storage/redis@v0.1.2   # Redis storage (prod)

# Framework integration (optional)
go get github.com/click33/sa-token-go/integrations/gin@v0.1.2    # Gin framework
go get github.com/click33/sa-token-go/integrations/echo@v0.1.2   # Echo framework
go get github.com/click33/sa-token-go/integrations/fiber@v0.1.2  # Fiber framework
go get github.com/click33/sa-token-go/integrations/chi@v0.1.2    # Chi framework
```

### ⚡ Minimal Usage (One-line Initialization)

```go
package main

import (
    "github.com/click33/sa-token-go/core"
    "github.com/click33/sa-token-go/stputil"
    "github.com/click33/sa-token-go/storage/memory"
)

func init() {
    // One-line initialization! Shows startup banner
    stputil.SetManager(
        core.NewBuilder().
            Storage(memory.NewStorage()).
            TokenName("Authorization").
            Timeout(86400).                      // 24 hours
            TokenStyle(core.TokenStyleRandom64). // Token style
            IsPrintBanner(true).                 // Show startup banner
            Build(),
    )
}
```

**Startup banner will be displayed:**

```
   _____         ______      __                  ______     
  / ___/____ _  /_  __/___  / /_____  ____      / ____/____ 
  \__ \/ __  |   / / / __ \/ //_/ _ \/ __ \_____/ / __/ __ \
 ___/ / /_/ /   / / / /_/ / ,< /  __/ / / /_____/ /_/ / /_/ /
/____/\__,_/   /_/  \____/_/|_|\___/_/ /_/      \____/\____/ 
                                                             
:: Sa-Token-Go ::                                    (v0.1.2)
:: Go Version ::                                     go1.21.0
:: GOOS/GOARCH ::                                    linux/amd64

┌─────────────────────────────────────────────────────────┐
│ Token Style     : random64                              │
│ Token Timeout   : 86400                      seconds    │
│ Auto Renew      : true                                  │
└─────────────────────────────────────────────────────────┘
```

```go
func main() {
    // Use StpUtil directly without passing manager
    token, _ := stputil.Login(1000)
    println("Login successful, Token:", token)
    
    // Set permissions
    stputil.SetPermissions(1000, []string{"user:read", "user:write"})
    
    // Check permissions
    if stputil.HasPermission(1000, "user:read") {
        println("Has permission!")
    