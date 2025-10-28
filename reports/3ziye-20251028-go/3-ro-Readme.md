
# ro - Reactive programming for Go

[![tag](https://img.shields.io/github/tag/samber/ro.svg)](https://github.com/samber/ro/releases)
![Go Version](https://img.shields.io/badge/Go-%3E%3D%201.18-%23007d9c)
[![GoDoc](https://godoc.org/github.com/samber/ro?status.svg)](https://pkg.go.dev/github.com/samber/ro)
![Build Status](https://github.com/samber/ro/actions/workflows/test.yml/badge.svg)
[![Go report](https://goreportcard.com/badge/github.com/samber/ro)](https://goreportcard.com/report/github.com/samber/ro)
[![Coverage](https://img.shields.io/codecov/c/github/samber/ro)](https://app.codecov.io/gh/samber/ro)
[![Contributors](https://img.shields.io/github/contributors/samber/ro)](https://github.com/samber/ro/graphs/contributors)

> A *Go* implementation of the [ReactiveX](https://reactivex.io/) spec.

The purpose of Reactive Programming is to simplify the development of event-driven and asynchronous applications by providing a declarative and composable way to handle streams of data or events.

----

<h3 align="center">💖 Support This Project</h3>

<p align="center">
	I’m going all-in on open-source for the coming months.
	<br>
	Help sustain development: Become an <a href="http://github.com/sponsors/samber">individual sponsor</a> or join as a <a href="mailto:hey@samuel-berthe.fr">corporate sponsor</a>.
</p>

----

![cover](/docs/static/img/cover.png)

**See also:**

- [samber/lo](https://github.com/samber/lo): A Lodash-style Go library based on Go 1.18+ Generics
- [samber/do](https://github.com/samber/do): A dependency injection toolkit based on Go 1.18+ Generics
- [samber/mo](https://github.com/samber/mo): Monads based on Go 1.18+ Generics (Option, Result, Either...)

What makes it different from **samber/lo**?
- lo: synchronous helpers across finite sequences (maps, slices...)
- ro: processing of infinite data streams for event-driven scenarios

## The Reactive Programming paradigm

Reactive Programming is focused on handling asynchronous data streams where values (like user input, API responses, or sensor data) are emitted over time. Instead of pulling data or waiting for events manually, you react to changes as they occur using `Observable`, `Observer`, and `Operator`. This approach simplifies building systems that are responsive, resilient, and scalable, especially in event-driven or real-time applications.

```go
observable := ro.Pipe(
    ro.RangeWithInterval(0, 10, 1*time.Second),
    ro.Filter(func(x int) bool {
        return x%2 == 0
    }),
    ro.Map(func(x int) string {
        return fmt.Sprintf("even-%d", x)
    }),
)

// Start consuming on subscription
observable.Subscribe(ro.OnNext(func(s string) {
    fmt.Println(s)
}))

// Output:
//   "even-0"
//   "even-2"
//   "even-4"
//   "even-6"
//   "even-8"
```

Now you discovered the paradigm, follow the documentation and turn reactive: [🚀 Getting started](https://ro.samber.dev/docs/getting-started)

## Core package

[Full documentation here](https://ro.samber.dev/docs/operator).

The `ro` library provides all basic operators:
- **Creation operators**: The data source, usually the first argument of `ro.Pipe`
- **Chainable operators**: They filter, validate, transform, enrich... messages
  - **Transforming operators**: They transform items emitted by an `Observable`
  - **Filtering operators**: They selectively emit items from a source `Observable`
  - **Conditional operators**: Boolean operators
  - **Math and aggregation operators**: They perform basic math operations
  - **Error handling operators**: They help to recover from error notifications from an `Observable`
  - **Combining operators**: Combine multiple `Observable` into one
  - **Connectable operators**: Convert cold into hot `Observable`
  - **Other**: manipulation of context, utility, async scheduling...
- **Plugins**: External operators (mostly IOs and library wrappers)

## Plugins

The `ro` library provides a rich ecosystem of plugins for various use cases:

[Full documentation here](https://ro.samber.dev/docs/plugins).

### Data Manipulation
- **Bytes** (`plugins/bytes`) - String and byte slice manipulation operators
- **Strings** (`plugins/strings`) - String manipulation operators
- **Sort** (`plugins/sort`) - Sorting operators
- **Type Conversion** (`plugins/strconv`) - String conversion operators

### Encoding & Serialization
- **JSON** (`plugins/encoding/json`) - JSON marshaling and unmarshaling
- **CSV** (`plugins/encoding/csv`) - CSV reading and writing
- **Base64** (`plugins/encoding/base64`) - Base64 encoding and decoding
- **Gob** (`plugins/encoding/gob`) - Go binary serialization

### Scheduling & Timing
- **Cron** (`plugins/cron`) - Schedule jobs using cron expressions or duration intervals
- **ICS** (`plugins/ics`) - Read and parse ICS/iCal calendars

### Network & I/O
- **HTTP** (`plugins/http`) - HTTP request operators
- **I/O** (`plugins/io`) - File and stream I/O operators
- **File System** (`plugins/fsnotify`) - File system monitoring operators

### Observability &