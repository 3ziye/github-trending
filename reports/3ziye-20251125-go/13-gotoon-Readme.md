# GoTOON - Token-Oriented Object Notation for Go

[![CI](https://github.com/alpkeskin/gotoon/actions/workflows/ci.yml/badge.svg)](https://github.com/alpkeskin/gotoon/actions/workflows/ci.yml)
[![Go Report Card](https://goreportcard.com/badge/github.com/alpkeskin/gotoon)](https://goreportcard.com/report/github.com/alpkeskin/gotoon)
[![codecov](https://codecov.io/gh/alpkeskin/gotoon/branch/main/graph/badge.svg)](https://codecov.io/gh/alpkeskin/gotoon)
[![Go Reference](https://pkg.go.dev/badge/github.com/alpkeskin/gotoon.svg)](https://pkg.go.dev/github.com/alpkeskin/gotoon)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Go Version](https://img.shields.io/github/go-mod/go-version/alpkeskin/gotoon)](https://go.dev/)

**GoTOON** is a Go implementation of [TOON (Token-Oriented Object Notation)](https://github.com/johannschopplich/toon), a compact, human-readable format designed for passing structured data to Large Language Models with significantly reduced token usage.

TOON excels at **uniform complex objects** – multiple fields per row, same structure across items. It achieves **30-60% token reduction** compared to JSON while maintaining high LLM comprehension accuracy.

![Toon](/.github/og.png)

## Why TOON?

LLM tokens cost money, and standard JSON is verbose and token-expensive:

```json
{
  "users": [
    { "id": 1, "name": "Alice", "role": "admin" },
    { "id": 2, "name": "Bob", "role": "user" }
  ]
}
```

TOON conveys the same information with **fewer tokens**:

```
users[2]{id,name,role}:
  1,Alice,admin
  2,Bob,user
```

## Key Features

- 💸 **Token-efficient:** typically 30–60% fewer tokens than JSON
- 🤿 **LLM-friendly guardrails:** explicit lengths and field lists help models validate output
- 🍱 **Minimal syntax:** removes redundant punctuation (braces, brackets, most quotes)
- 📐 **Indentation-based structure:** replaces braces with whitespace for better readability
- 🧺 **Tabular arrays:** declare keys once, then stream rows without repetition
- 🛠️ **Go-idiomatic API:** clean, simple interface with functional options

## Installation

```bash
go get github.com/alpkeskin/gotoon
```

## Quick Start

```go
package main

import (
    "fmt"
    "log"

    "github.com/alpkeskin/gotoon"
)

func main() {
    data := map[string]interface{}{
        "users": []map[string]interface{}{
            {"id": 1, "name": "Alice", "role": "admin"},
            {"id": 2, "name": "Bob", "role": "user"},
        },
    }

    encoded, err := gotoon.Encode(data)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(encoded)
}
```

Output:

```
users[2]{id,name,role}:
  1,Alice,admin
  2,Bob,user
```

## API

### `Encode(input interface{}, opts ...EncodeOption) (string, error)`

Converts any Go value to TOON format string.

**Input normalization:**
- Primitives (bool, int, float, string) are encoded as-is
- Structs are converted to maps using exported fields (respects `json` tags)
- Slices and arrays remain as arrays
- Maps with string keys remain as objects
- `time.Time` is converted to RFC3339Nano format
- `NaN` and `Infinity` become `null`
- `nil`, functions become `null`

**Example:**

```go
type User struct {
    ID   int    `json:"id"`
    Name string `json:"name"`
    Role string `json:"role"`
}

users := []User{
    {ID: 1, Name: "Alice", Role: "admin"},
    {ID: 2, Name: "Bob", Role: "user"},
}

encoded, _ := gotoon.Encode(map[string]interface{}{"users": users})
// Output:
// users[2]{id,name,role}:
//   1,Alice,admin
//   2,Bob,user
```

### Encoding Options

GoTOON supports functional options for customization:

#### `WithIndent(n int)`

Sets the number of spaces per indentation level (default: 2).

```go
gotoon.Encode(data, gotoon.WithIndent(4))
```

#### `WithDelimiter(d string)`

Sets the delimiter for array values and tabular rows. Valid values: `","` (comma, default), `"\t"` (tab), `"|"` (pipe).

```go
// Using tab delimiter
gotoon.Encode(data, gotoon.WithDelimiter("\t"))
// Output:
// users[2	]{id	name	role}:
//   1	Alice	admin
//   2	Bob	user
```

#### `WithLengthMarker()`

Adds `#` prefix to array lengths for clarity (e.g., `[#3]` instead of `[3]`).

```go
gotoon.Encode(data, gotoon.WithLengthMarker())
// Output:
// users[#2]{id,name,role}:
//   1,Alice,admin
//   2,Bob,user
```

### Combining Options

```go
encoded, _ := gotoon.Encode(data,
    gotoon.WithIndent(4),
    gotoon.WithDelimiter("\t"),
    gotoon.WithLengthMarker(),
)
```

## Format Overview

### Objects

Simple objects with primitive values:

```go
data := map[string]interface{}{
    "id":     123,
    "name":   "Ada",
    "active": true,
}
// Output:
// id: 123
// name: Ada
// active: true
```

Nested objects:

```go
data := map[string]interface{}{
    "user": map[string]interface{}{
        "id":   123,
        "name": "Ada",
    },
}
// Output:
// user:
//   id: 123
//   name: Ada
```

### Arrays

#### Primitive Arrays (Inline)

```go
data := map[string]interface{}