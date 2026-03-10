# gotreesitter

Pure-Go [tree-sitter](https://tree-sitter.github.io/) runtime. No CGo, no C toolchain. Cross-compiles to any `GOOS`/`GOARCH` target Go supports, including `wasip1`.

```sh
go get github.com/odvcencio/gotreesitter
```

gotreesitter loads the same parse-table format that tree-sitter's C runtime uses. Grammar tables are extracted from upstream `parser.c` files by `ts2go`, compressed into binary blobs, and deserialized on first use. 206 grammars ship in the registry.

## Motivation

Every Go tree-sitter binding in the ecosystem depends on CGo:

- Cross-compilation requires a C cross-toolchain per target. `GOOS=wasip1`, `GOARCH=arm64` from a Linux host, or any Windows build without MSYS2/MinGW, will not link.
- CI images must carry `gcc` and the grammar's C sources. `go install` fails for downstream users who don't have a C compiler.
- The Go race detector, coverage instrumentation, and fuzzer cannot see across the CGo boundary. Bugs in the C runtime or in FFI marshaling are invisible to `go test -race`.

gotreesitter eliminates the C dependency entirely. The parser, lexer, query engine, incremental reparsing, arena allocator, external scanners, and tree cursor are all implemented in Go. The only input is the grammar blob.

## Quick start

```go
import (
    "fmt"

    "github.com/odvcencio/gotreesitter"
    "github.com/odvcencio/gotreesitter/grammars"
)

func main() {
    src := []byte(`package main

func main() {}
`)

    lang := grammars.GoLanguage()
    parser := gotreesitter.NewParser(lang)

    tree, _ := parser.Parse(src)
    fmt.Println(tree.RootNode())
}
```

`grammars.DetectLanguage("main.go")` resolves a filename to the appropriate `LangEntry`.

### Queries

```go
q, _ := gotreesitter.NewQuery(`(function_declaration name: (identifier) @fn)`, lang)
cursor := q.Exec(tree.RootNode(), lang, src)

for {
    match, ok := cursor.NextMatch()
    if !ok {
        break
    }
    for _, cap := range match.Captures {
        fmt.Println(cap.Node.Text(src))
    }
}
```

The query engine supports the full S-expression pattern language: structural quantifiers (`?`, `*`, `+`), alternation (`[...]`), field constraints, negated fields, anchor (`!`), and all standard predicates. See [Query API](#query-api).

### Typed query codegen

Generate type-safe Go wrappers from `.scm` query files:

```sh
go run ./cmd/tsquery -input queries/go_functions.scm -lang go -output go_functions_query.go -package queries
```

Given a query like `(function_declaration name: (identifier) @name body: (block) @body)`, `tsquery` generates:

```go
type FunctionDeclarationMatch struct {
    Name *gotreesitter.Node
    Body *gotreesitter.Node
}

q, _ := queries.NewGoFunctionsQuery(lang)
cursor := q.Exec(tree.RootNode(), lang, src)
for {
    match, ok := cursor.Next()
    if !ok { break }
    fmt.Println(match.Name.Text(src))
}
```

Multi-pattern queries generate one struct per pattern with `MatchPatternN` conversion helpers.

### Multi-language documents (injection parsing)

Parse documents with embedded languages (HTML+JS+CSS, Markdown+code fences, Vue/Svelte templates):

```go
ip := gotreesitter.NewInjectionParser()
ip.RegisterLanguage("html", htmlLang)
ip.RegisterLanguage("javascript", jsLang)
ip.RegisterLanguage("css", cssLang)
ip.RegisterInjectionQuery("html", injectionQuery)

result, _ := ip.Parse(source, "html")

for _, inj := range result.Injections {
    fmt.Printf("%s: %d ranges\n", inj.Language, len(inj.Ranges))
    // inj.Tree is the child language's parse tree
}
```

Supports static (`#set! injection.language "javascript"`) and dynamic (`@injection.language` capture) language detection, recursive nested injections, and incremental reparse with child tree reuse.

### Source rewriting

Collect source-level edits and apply atomically, producing `InputEdit` records for incremental reparse:

```go
rw := gotreesitter.NewRewriter(src)
rw.Replace(funcNameNode, []byte("newName"))
rw.InsertBefore(bodyNode, []byte("// added\n"))
rw.Delete(unusedNode)

newSrc, _ := rw.ApplyToTree(tree)
newTree, _ := parser.ParseIncremental(newSrc, tree)
```

`Apply()` returns both the new source bytes and the `[]InputEdit` records. `ApplyToTree()` is a convenience that calls `tree.Edit()` for each edit and returns source ready for `ParseIncremental`.

### Incremental reparsing

```go
tree, _ := parser.Parse(src)

// User types "x" at byte offset 42
src = append(src[:42], append([]byte("x"), src[42:]...)...)

tree.Edit(gotreesitter.InputEdit{
    StartByte:   42,
    OldEndByte:  42,
    NewEndByte:  43,
    StartPoint:  gotreesitter.Point{Row: 3, Column: 10},
    OldEndPoint: gotreesitter.Point{Row: 3, Column: 10},
    NewEndPoint: gotreesitter.Point{Row: 3, Column: 11},
})

tree2, _ := parser.ParseIncremental(src, tree)
```

`ParseIncremental` walks the old tree's spine, identifies the edit region, and reuses unchanged subtrees by reference. Only the invalidated span is re-lexed and re-parsed. Both leaf and non-leaf subtrees are eligible for reu