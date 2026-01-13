<p align="center">
  <img src="./docs/images/logo.png?v=2" width="400" alt="str logo">
</p>

<p align="center">
    A fluent, Laravel-inspired string toolkit for Go, focused on rune-safe helpers,
    expressive transformations, and predictable behavior beyond the standard library.
</p>

<p align="center">
    <a href="https://pkg.go.dev/github.com/goforj/str"><img src="https://pkg.go.dev/badge/github.com/goforj/str.svg" alt="Go Reference"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
    <a href="https://github.com/goforj/str/actions"><img src="https://github.com/goforj/str/actions/workflows/test.yml/badge.svg" alt="Go Test"></a>
    <a href="https://golang.org"><img src="https://img.shields.io/badge/go-1.18+-blue?logo=go" alt="Go version"></a>
    <img src="https://img.shields.io/github/v/tag/goforj/str?label=version&sort=semver" alt="Latest tag">
    <a href="https://codecov.io/gh/goforj/str" ><img src="https://codecov.io/github/goforj/str/graph/badge.svg?token=9KT46ZORP3"/></a>
<!-- test-count:embed:start -->
    <img src="https://img.shields.io/badge/tests-196-brightgreen" alt="Tests">
<!-- test-count:embed:end -->
    <a href="https://goreportcard.com/report/github.com/goforj/str"><img src="https://goreportcard.com/badge/github.com/goforj/str" alt="Go Report Card"></a>
</p>

## Installation

```sh
go get github.com/goforj/str
```

## Runnable examples

Every function has a corresponding runnable example under [`./examples`](./examples).

These examples are **generated directly from the documentation blocks** of each function, ensuring the docs and code never drift. These are the same examples you see here in the README and GoDoc.

An automated test executes **every example** to verify it builds and runs successfully.

This guarantees all examples are valid, up-to-date, and remain functional as the API evolves.

<!-- api:embed:start -->

## API Index

| Group | Functions |
|------:|-----------|
| **Affixes** | [ChopEnd](#chopend) [ChopStart](#chopstart) [EnsurePrefix](#ensureprefix) [EnsureSuffix](#ensuresuffix) [Unwrap](#unwrap) [Wrap](#wrap) |
| **Case** | [Camel](#camel) [Headline](#headline) [Kebab](#kebab) [LcFirst](#lcfirst) [Pascal](#pascal) [Snake](#snake) [Title](#title) [ToLower](#tolower) [ToTitle](#totitle) [ToUpper](#toupper) [UcFirst](#ucfirst) [UcWords](#ucwords) |
| **Checks** | [IsASCII](#isascii) [IsBlank](#isblank) [IsEmpty](#isempty) |
| **Cleanup** | [Deduplicate](#deduplicate) [NormalizeNewlines](#normalizenewlines) [NormalizeSpace](#normalizespace) [Squish](#squish) [Trim](#trim) [TrimLeft](#trimleft) [TrimRight](#trimright) [TrimSpace](#trimspace) |
| **Comparison** | [Equals](#equals) [EqualsFold](#equalsfold) |
| **Compose** | [Append](#append) [NewLine](#newline) [Prepend](#prepend) |
| **Constructor** | [Of](#of) |
| **Encoding** | [FromBase64](#frombase64) [ToBase64](#tobase64) |
| **Fluent** | [GoString](#gostring) [String](#string) |
| **Length** | [Len](#len) [RuneCount](#runecount) |
| **Masking** | [Mask](#mask) |
| **Match** | [Is](#is) [IsMatch](#ismatch) [Match](#match) [MatchAll](#matchall) |
| **Padding** | [PadBoth](#padboth) [PadLeft](#padleft) [PadRight](#padright) |
| **Pluralize** | [Plural](#plural) [Singular](#singular) |
| **Replace** | [Remove](#remove) [ReplaceAll](#replaceall) [ReplaceArray](#replacearray) [ReplaceEnd](#replaceend) [ReplaceFirst](#replacefirst) [ReplaceFirstFold](#replacefirstfold) [ReplaceFold](#replacefold) [ReplaceLast](#replacelast) [ReplaceLastFold](#replacelastfold) [ReplaceMatches](#replacematches) [ReplaceStart](#replacestart) [Swap](#swap) |
| **Search** | [Contains](#contains) [ContainsAll](#containsall) [ContainsAllFold](#containsallfold) [ContainsFold](#containsfold) [Count](#count) [EndsWith](#endswith) [EndsWithFold](#endswithfold) [Index](#index) [LastIndex](#lastindex) [StartsWith](#startswith) [StartsWithFold](#startswithfold) |
| **Slug** | [Slug](#slug) |
| **Snippet** | [Excerpt](#excerpt) |
| **Split** | [Lines](#lines) [Split](#split) [UcSplit](#ucsplit) |
| **Substrings** | [After](#after) [AfterLast](#afterlast) [Before](#before) [BeforeLast](#beforelast) [Between](#between) [BetweenFirst](#betweenfirst) [CharAt](#charat) [Limit](#limit) [Slice](#slice) [SubstrReplace](#substrreplace) [Take](#take) [TakeLast](#takelast) |
| **Transform** | [Repeat](#repeat) [Reverse](#reverse) [Transliterate](#transliterate) |
| **Words** | [FirstWord](#firstword) [Join](#join) [LastWord](#lastword) [SplitWords](#splitwords) [WordCount](#wordcount) [Words](#words) [WrapWords](#wrapwords) |


## Affixes

### <a id="chopend"></a>ChopEnd

ChopEnd removes the first matching suffix if present.

```go
v := str.Of("file.txt").ChopEnd(".txt", ".md").String()
println(v)
// #string file
```

### <a id="chopstart"></a>ChopStart

ChopStart removes the first matching prefix if present.

```go
v := str.Of("https://goforj.dev").ChopStart("https://", "http://").String()
println(v)
