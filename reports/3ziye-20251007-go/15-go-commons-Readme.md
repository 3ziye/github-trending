# go-commons

<sub><sup>English | [中文 README](README-zh.md)</sup></sub>

[![Go Reference](https://pkg.go.dev/badge/github.com/Rodert/go-commons.svg)](https://pkg.go.dev/github.com/Rodert/go-commons)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](LICENSE)
[![Go Tests](https://github.com/Rodert/go-commons/actions/workflows/go-test.yml/badge.svg)](https://github.com/Rodert/go-commons/actions/workflows/go-test.yml)
[![Go Lint](https://github.com/Rodert/go-commons/actions/workflows/go-lint.yml/badge.svg)](https://github.com/Rodert/go-commons/actions/workflows/go-lint.yml)
[![codecov](https://codecov.io/gh/Rodert/go-commons/branch/main/graph/badge.svg)](https://codecov.io/gh/Rodert/go-commons)

A small collection of Go utility packages focused on string helpers and basic system utilities, with minimal third‑party dependencies.

## Features

- **No third‑party deps**: Prefer using the Go standard library where possible
- **String utilities (`stringutils`)**:
  - Emptiness and whitespace: `IsEmpty`, `IsNotEmpty`, `IsBlank`, `IsNotBlank`, `Trim`, `TrimToEmpty`
  - Substrings and checks: `ContainsAny`, `ContainsAll`, `SubstringBefore`, `SubstringAfter`, `StartsWith`, `EndsWith`
  - Transformations: `Capitalize`, `Uncapitalize`, `ReverseString`, `ToUpperCase`, `ToLowerCase`
  - Replace and join: `Join`, `Split`, `Replace`, `ReplaceAll`, `Repeat`
  - Padding and centering: `PadLeft`, `PadRight`, `Center`
  - Misc: `Truncate`, `TruncateWithSuffix`, `CountMatches`, `DefaultIfEmpty`, `DefaultIfBlank`
- **System utilities (`systemutils`)**:
  - CPU utilities (`cpuutils`): `GetCPUInfo` - retrieve CPU cores, usage percentage, and load averages
  - Memory utilities (`memutils`): `GetMemInfo` - get total, available, and used memory
  - Disk utilities (`diskutils`): `GetDiskInfo` - get disk space information including total, free, used space and usage ratio

## Module

- Module path: `github.com/Rodert/go-commons`
- Go version: `1.24.7`

## Install

```bash
go get github.com/Rodert/go-commons
```

## Development

### Auto-formatting

This project uses Git hooks to automatically format Go code before each commit.

To install the pre-commit hook:

```bash
make hooks
```

### API Documentation

This project includes an interactive API documentation interface using Swagger UI. This allows you to explore and test the library's functions through a web interface.

#### 📌 Online API Documentation

**Visit our API documentation online at: [https://rodert.github.io/go-commons](https://rodert.github.io/go-commons)**

The online documentation is automatically deployed from the main branch and provides the most up-to-date API reference.

![API Documentation Interface](images/api-img.png)

#### Local Development

To start the API documentation server locally:

```bash
./run_apidocs.sh
```

Then open your browser and navigate to [http://localhost:8080](http://localhost:8080) to view the interactive API documentation.

To manually format all Go files:

```bash
make fmt
```

## Usage

### String Utilities

```go
package main

import (
	"fmt"
	"github.com/Rodert/go-commons/stringutils"
)

func main() {
	// Basic string operations
	fmt.Println(stringutils.IsBlank("  \t\n"))         // true
	fmt.Println(stringutils.Trim("  hello  "))        // "hello"
	fmt.Println(stringutils.TruncateWithSuffix("abcdef", 4, "..")) // "ab.."
	fmt.Println(stringutils.PadLeft("42", 5, '0'))     // "00042"
	fmt.Println(stringutils.ContainsAny("gopher", "go", "java")) // true
	
	// String transformations
	fmt.Println(stringutils.Reverse("hello"))         // "olleh"
	fmt.Println(stringutils.SwapCase("Hello World"))  // "hELLO wORLD"
	fmt.Println(stringutils.PadCenter("hello", 9, '*')) // "**hello**"
}
```

### System Utilities

```go
package main

import (
	"fmt"
	"github.com/Rodert/go-commons/systemutils/cpuutils"
	"github.com/Rodert/go-commons/systemutils/memutils"
	"github.com/Rodert/go-commons/systemutils/diskutils"
)

func main() {
	// Get CPU information
	cpuInfo, err := cpuutils.GetCPUInfo()
	if err == nil {
		fmt.Printf("CPU Cores: %d\n", cpuInfo.LogicalCores)
		fmt.Printf("CPU Usage: %.2f%%\n", cpuInfo.UsagePercent)
		fmt.Printf("Load Average: %.2f, %.2f, %.2f\n", 
			cpuInfo.LoadAvg[0], cpuInfo.LoadAvg[1], cpuInfo.LoadAvg[2])
	}
	
	// Get memory information
	memInfo, err := memutils.GetMemInfo()
	if err == nil {
		fmt.Printf("Total Memory: %d bytes\n", memInfo.Total)
		fmt.Printf("Available Memory: %d bytes\n", memInfo.Available)
		fmt.Printf("Used Memory: %d bytes\n", memInfo.Used)
	}
	
	// Get disk information
	diskInfo, err := diskutils.GetDiskInfo("/")
	if err == nil {
		fmt.Printf("Disk Path: %s\n", diskInfo.Path)
		fmt.Printf("Total Space: %d bytes\n", diskInfo.Total)
		fmt.Printf("Free Space: %d bytes\n", diskInfo.Free)
		fmt.Printf("Used Space: %d bytes\n", diskInfo.Used)
		fmt.P