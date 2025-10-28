# GoMem

<div align="center">
  <img src="logo.png" alt="GoMem Logo" width="200"/>
</div>

[![Go Version](https://img.shields.io/badge/Go-1.23+-00ADD8?style=flat-square&logo=go)](https://golang.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Go Report Card](https://goreportcard.com/badge/github.com/langhuihui/gomem?style=flat-square)](https://goreportcard.com/report/github.com/langhuihui/gomem)

> **Language**: [English](README.md) | [中文](README_CN.md)

GoMem is a high-performance memory allocator library for Go, extracted from the Monibuca project.

## Features

- **Multiple Allocation Strategies**: Support for both single-tree and two-tree (AVL) allocation algorithms
- **Buddy Allocator**: Optional buddy system for efficient memory pooling
- **Recyclable Memory**: Memory recycling support with automatic cleanup
- **Scalable Allocator**: Dynamically growing memory allocator
- **Memory Reader**: Efficient multi-buffer reader with zero-copy operations

## Build Tags

The library supports several build tags to customize behavior:

- `twotree`: Use two-tree (AVL) implementation instead of single treap
- `enable_buddy`: Enable buddy allocator for memory pooling
- `disable_rm`: Disable recyclable memory features for reduced overhead
- `enable_mmap`: Enable memory-mapped allocation for improved memory efficiency (Linux/macOS/Windows)
  - **Linux**: Automatically enables Transparent Huge Pages (THP) support, using 2MB huge pages instead of 4KB pages for significantly reduced TLB misses and improved memory access performance

## Installation

```bash
go get github.com/langhuihui/gomem
```

## Usage

### Basic Memory Allocation

```go
package main

import "github.com/langhuihui/gomem"

func main() {
    // Create a scalable memory allocator
    allocator := gomem.NewScalableMemoryAllocator(1024)
    
    // Allocate memory
    buf := allocator.Malloc(256)
    
    // Use the buffer...
    copy(buf, []byte("Hello, World!"))
    
    // Free the memory
    allocator.Free(buf)
}
```

### Partial Memory Deallocation

```go
package main

import "github.com/langhuihui/gomem"

func main() {
    // Create a scalable memory allocator
    allocator := gomem.NewScalableMemoryAllocator(1024)
    
    // Allocate a large block of memory
    buf := allocator.Malloc(1024)
    
    // Use different parts of the memory
    part1 := buf[0:256]    // First 256 bytes
    part2 := buf[256:512]  // Middle 256 bytes  
    part3 := buf[512:1024] // Last 512 bytes
    
    // Fill with data
    copy(part1, []byte("Part 1 data"))
    copy(part2, []byte("Part 2 data"))
    copy(part3, []byte("Part 3 data"))
    
    // Partial deallocation - can free parts of memory
    allocator.Free(part1)  // Free first 256 bytes
    allocator.Free(part2)  // Free middle 256 bytes
    
    // Continue using remaining memory
    copy(part3, []byte("Updated part 3"))
    
    // Finally free remaining memory
    allocator.Free(part3)
}
```

### Recyclable Memory

```go
// Create recyclable memory for batch operations
allocator := gomem.NewScalableMemoryAllocator(1024)
rm := gomem.NewRecyclableMemory(allocator)

// Allocate multiple buffers
buf1 := rm.NextN(128)
buf2 := rm.NextN(256)

// Use the buffers...
copy(buf1, []byte("Buffer 1"))
copy(buf2, []byte("Buffer 2"))

// Recycle all memory at once
rm.Recycle()
```

### Memory Buffer Operations

```go
// Create a memory buffer
mem := gomem.NewMemory([]byte{1, 2, 3, 4, 5})

// Add more data
mem.PushOne([]byte{6, 7, 8})

// Get total size and buffer count
fmt.Printf("Size: %d, Buffers: %d\n", mem.Size, mem.Count())

// Convert to bytes
data := mem.ToBytes()
```

### Memory Reader

```go
// Create a memory reader
reader := gomem.NewReadableBuffersFromBytes([]byte{1, 2, 3}, []byte{4, 5, 6})

// Read data
buf := make([]byte, 6)
n, err := reader.Read(buf)
// buf now contains [1, 2, 3, 4, 5, 6]
```

## Concurrency Safety

⚠️ **Important**: Malloc and Free operations must be called from the same goroutine to avoid race conditions. For more elegant usage, consider using [gotask](https://github.com/langhuihui/gotask), where you can allocate memory in the `Start` method and free it in the `Dispose` method.

```go
// ❌ Wrong: Different goroutines
go func() {
    buf := allocator.Malloc(256)
    // ... use buffer
}()

go func() {
    allocator.Free(buf) // Race condition!
}()

// ✅ Correct: Same goroutine
buf := allocator.Malloc(256)
// ... use buffer
allocator.Free(buf)

// ✅ Elegant: Using gotask
type MyTask struct {
    allocator *gomem.ScalableMemoryAllocator
    buffer []byte
}

func (t *MyTask) Start() {
    t.allocator = gomem.NewScalableMemoryAllocator(1024)
    t.buffer = t.allocator.Malloc(256)
}

func (t *MyTask) Dispose() {
    t.allocator.Free(t.buffer)
}
```

## Performance Considerations

- **Use `enable_mmap` build tag for dramatic performance improvements**: 100-400x faster allocator creation, 99.98% less memory usage
- Use `enable_buddy` build tag for b