This is the second part of a series introducing Bash programmers to Go. This part is about basics of writing CLI tools in Go. See the [first](https://github.com/go-monk/from-bash-to-go-part-i) part for the language building blocks.

# Our first CLI tool

Bash is often used to write small CLI tools and automation. Let's start with an example CLI tool that prints "hello" to terminal. The Bash version is pretty simple:

```bash
#!/bin/bash
echo hello
```

Now, let's implement a Go version. We start by creating a directory where the first version of our program will live. We also initialize a module in there:

```sh
$ mkdir -p hello/1
$ cd hello/1
$ go mod init hello
```

Since the program is not complex we don't have to think a lot about its design and can easily start with a test:

```go
// hello/1/hello_test.go
package hello_test

import (
	"hello"
	"testing"
)

func TestPrintExists(t *testing.T) {
	hello.Print()
}
```

We named the package `hello_test` instead of `hello`. This is possible and it allows for writing tests that use only the public API (identifiers starting with a capital letter) of the tested package as a real user would. Note that `*_test` packages are the sole exception to Go's standard rule that each source directory can contain only one package. In this test we just call the `Print` function from the `hello` package. Let's try and run the test:

```sh
$ go test
hello: no non-test Go files in ~/github.com/go-monk/from-bash-to-go-series/part-ii-cli-tools/hello/1
FAIL    hello [build failed]
```

Yes, we have not yet written the code we want to test. So let's do it:

```go
// hello/1/hello.go
package hello

func Print() {}
```

If we re-run the test

```sh
$ go test
PASS
ok      hello   0.570s
```

we can see that all is good now. Or is it? Well, something must be wrong because an empty function that does nothing at all (except that it exists) passes the test. So the *test* is obviously wrong. Now we need to start thinking a bit. What should be actually tested? 

## Making it testable

Okay, we want the function to print the string "hello" to terminal. How to test it except by looking at the terminal? In Bash the terminal is the standard output, i.e. the place where the stuff is written to by default. But we can redirect the standard output to a file or store it in a variable:

```bash
$ echo hello > /tmp/hello.txt
$ HELLO=$(echo hello)
```

In Go you can achieve similar functionality by using the standard library interface called [io.Writer](https://pkg.go.dev/io#Writer) (that is the `Writer` from the `io` package):

```go
// hello/2/hello.go
func PrintTo(w io.Writer) {
	s := "hello"
	w.Write([]byte(s))
}
```

We write (print) the string "hello" to `w` supplied as the function's argument. And since the argument (parameter more precisely) is an interface it can be multiple kinds of things. Or more precisely it can be any type that implements the `io.Writer` interface, i.e. has a function with the `Write(p []byte) (int, error)` signature attached.

There are many implementations of `io.Writer` in the standard library. Two of them are `bytes.Buffer` and `os.Stdout`. We can write to a bytes buffer in the test

```go
// hello/2/hello_test.go
func TestPrintToPrintsHelloToWriter(t *testing.T) {
	buf := new(bytes.Buffer)
	hello.PrintTo(buf) // writing to buffer
	want := "hello"
	got := buf.String()
	if want != got {
		t.Errorf("want %q, got %q", want, got)
	}
}
```

and to the standard output in the main function

```go
// hello/2/cmd/hello/main.go
func main() {
	hello.PrintTo(os.Stdout) // writing to STDOUT
}
```

Now we have a real test that we can rely on:

```sh
$ cd hello/2
$ go test
PASS
ok      hello   0.183s
```

As an exercise try to break the test so it doesn't pass.

We also added the `cmd` folder that holds the binary (command) to be used by the end user like this:

```sh
$ go install ./cmd/hello
$ hello
hello
```

## Decreasing complexity

Talking about the end user and looking at how the `PrintTo` function is called in `main`

```go
hello.PrintTo(os.Stdout)
```

we might think this is not ideal. Why should a user tell the function to print to standard output? Isn't it what most users want most of the time? Shouldn't it be the default behavior?

### Nil argument

But the `PrintTo` function *must* have an argument when called. So maybe we can use the approach that's used by the `http.ListenAndServe` standard library function; we use `nil` to indicate we want the default behaviour:

```go
// hello/3/hello.go
func PrintTo(w io.Writer) {
	if w == nil {
		w = os.Stdout
	}
	s := "hello"
	w.Write([]byte(s))
}
```

```go
// hello/3/cmd/hello/main.go
hello.PrintTo(nil)
```

Hmm, this works but still seems unnecessary complex.

### Global variable

We could remove the need for an argument altogether by using a global variable that would define where to write:

```go
// hello/4/hello.go
var Output io.Writer = os.Stdout
```

To change the default, you change the global variable:

```go
// hello/4/h