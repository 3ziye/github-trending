This is the first part of a series introducing Bash programmers to Go. This part goes through the language building blocks that will be used in later parts.

# Ok but why?

> A language that doesn't affect the way you think about programming is not worth knowing. - Alan J. Perlis

You might be wondering along these lines - I already kind of know Bash (or a similar language) and can do all I need in it. It's easy and fast. Why should I learn Go? That's a good question. Always ask why because the answer to a why question provides a reason and thus understanding and motivation. In our case I think the answer has to do with the difference between programming and software engineering.

Programming means writing a program that works and does something useful. Software engineering is programming plus time and other people. It's the initial writing of a program and its being modified by you or other people over time. Programming alone is hard enough. First you need to understand the domain and the concrete problem to solve within the domain. Then you design a solution and implement it in a programming language whose syntax and idioms you should know well. This process can, and *should*, take multiple iterations. When you are done you go work on other stuff. Then you might be asked to modify something in the program (to fix a bug or add new functionality) or to hand over the program to someone else (people come and go).

The most important thing to do when doing the software engineering is to reduce the cognitive load; to reduce the system's complexity. This requires hard work, attention to detail and using good tools. I think Go is a good tool for software engineering because it includes "a cultural agenda of radical simplicity". See https://github.com/go-monk/from-bash-to-go for a practical example of how and why migrate a script from Bash to Go.

# Building blocks

In this section I swiftly introduce some of the language building blocks that I hope will help you start understanding the Go syntax, semantics and idioms. I recommend actually writing (copying) the code below in your favorite editor. And then running it. And maybe changing it a bit and running again. If you break the code be happy, that's a way to learn :-).

## Writing and running Go code

Packages are Go's way of organizing and (re)using code.

Bash is organized mostly via files - each program usually lives in a file:

```
+------------+
| script1.sh |
+------------+
+------------+
| script2.sh |
+------------+
+------------+
| script3.sh |
+------------+
```

Go code lives in one or more *packages* that are contained in one or more .go files within a single directory. Packages can be grouped into *modules* for versioning and sharing.

It can be visualized like this:

```
+--------------------------+
| module example.net/hello |
|                          |
|  +-------------------+   |
|  |   package main    |   |
|  |                   |   |
|  |  +-------------+  |   |
|  |  | greeting.go |  |   |
|  |  +-------------+  |   |
|  |  +-------------+  |   |
|  |  | hello.go    |  |   |
|  |  +-------------+  |   |
|  |                   |   |
|  +-------------------+   |
|                          |
+--------------------------+
```

Go identifiers - constants, variables, types and functions - are visible (exported) outside of a package when their name starts with an uppercase letter. Otherwise they are confined to the current package.

Let's create our first package. In case you want to run your code (as opposed to using it as an importable library) you need at least the `main` package.

First create a directory and change to it:

```
$ mkdir hello
$ cd hello
```

Then create `hello.go` file with the following content:

```go
package main

import "fmt"

func main() {
	fmt.Println("hello")
}
```

The `main` function is where the program's execution starts.

The easiest way to run a Go program is:

```sh
$ go run hello.go # build the binary and run it
hello
```

As mentioned above, you can spread package code into multiple files within the same directory:

```go
// hello.go
package main

import "fmt"

func main() {
        fmt.Println(greeting)
}
```

```go
// greeting.go
package main

const greeting = "hello"
```

Now we need to include both package files:

```sh
$ go run hello.go greeting.go
hello
```

Module is a group of packages that is versioned as a unit. To create a module:

```sh
$ go mod init github.com/jsmith/hello
$ go mod tidy # download dependencies
```

To build for a different OS and/or CPU architecture than the one you are running:

```sh
macOS$ GOOS=linux GOARCH=amd64 go build
```

To see the list of all supported OS/ARCH combinations:

```sh
$ go tool dist list
```

See https://go.dev/doc/tutorial/getting-started for more.

## Variables and types

In Bash all simple variables are strings:

```sh
name=Jack
age=40
active=true

# this is not a problem in Bash, since there are no types
age=forty
```

Go is a statically typed language. It