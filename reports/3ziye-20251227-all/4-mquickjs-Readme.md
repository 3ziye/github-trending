MicroQuickJS
============

## Introduction

MicroQuickJS (aka. MQuickJS) is a JavaScript engine targetted at
embedded systems. It compiles and runs JavaScript programs using as little
as 10 kB of RAM. The whole engine requires about 100 kB of ROM (ARM
Thumb-2 code) including the C library. The speed is comparable to
QuickJS.

MQuickJS only supports a [subset](#javascript-subset-reference) of JavaScript close to ES5. It
implements a **stricter mode** where some error prone or inefficient
JavaScript constructs are forbidden.

Although MQuickJS shares much code with QuickJS, it internals are
different in order to consume less memory. In particular, it relies on
a tracing garbage collector, the VM does not use the CPU stack and
strings are stored in UTF-8.

## REPL

The REPL is `mqjs`. Usage:

```
usage: mqjs [options] [file [args]]
-h  --help            list options
-e  --eval EXPR       evaluate EXPR
-i  --interactive     go to interactive mode
-I  --include file    include an additional file
-d  --dump            dump the memory usage stats
    --memory-limit n  limit the memory usage to 'n' bytes
--no-column           no column number in debug information
-o FILE               save the bytecode to FILE
-m32                  force 32 bit bytecode output (use with -o)
-b  --allow-bytecode  allow bytecode in input file
```

Compile and run a program using 10 kB of RAM:

```sh
./mqjs --memory-limit 10k tests/mandelbrot.js
```


In addition to normal script execution, `mqjs` can output the compiled
bytecode to a persistent storage (file or ROM):

```sh
./mqjs -o mandelbrot.bin tests/mandelbrot.js
```

Then you can run the compiled bytecode as a normal script:

```sh
./mqjs -b mandelbrot.bin
```

The bytecode format depends on the endianness and word length (32 or
64 bit) of the CPU. On a 64 bit CPU, it is possible to use the option
`-m32` to generate 32 bit bytecode that can run on an embedded 32 bit
system.

Use the option `--no-column` to remove the column number debug info
(only line numbers are remaining) if you want to save some storage.

## Stricter mode

MQuickJS only supports a subset of JavaScript (mostly ES5). It is
always in **stricter** mode where some error prone JavaScript features
are disabled. The general idea is that the stricter mode is a subset
of JavaScript, so it still works as usual in other JavaScript
engines. Here are the main points:

- Only **strict mode** constructs are allowed, hence no `with` keyword
  and global variables must be declared with the `var` keyword.

- Arrays cannot have holes. Writing an element after the end is not
  allowed:
```js
    a = []
    a[0] = 1; // OK to extend the array length
    a[10] = 2; // TypeError
```
  If you need an array like object with holes, use a normal object
  instead:
```js
    a = {}
    a[0] = 1;
    a[10] = 2;
```
  `new Array(len)` still works as expected, but the array elements are
  initialized to `undefined`.
  Array literals with holes are a syntax error:
```js
    [ 1, , 3 ] // SyntaxError
```
- Only global `eval` is supported so it cannot access to nor modify
  local variables:
```js
    eval('1 + 2'); // forbidden
    (1, eval)('1 + 2'); // OK
```
- No value boxing: `new Number(1)` is not supported and never
  necessary.

## JavaScript Subset Reference
 
- Only strict mode is supported with emphasis on ES5 compatibility.

- `Array` objects:

    - They have no holes.
    
    - Numeric properties are always handled by the array object and not
      forwarded to its prototype.
  
    - Out-of-bound sets are an error except when they are at the end of
      the array.
      
    - The `length` property is a getter/setter in the array prototype.

- all properties are writable, enumerable and configurable.

- `for in` only iterates over the object own properties. It should be
  used with this common pattern to have a consistent behavior with
  standard JavaScript:
  
```js
    for(var prop in obj) {
        if (obj.hasOwnProperty(prop)) {
            ...
        }
    }
```    
Always prefer using `for of` instead which is supported with arrays:

```js
    for(var prop of Object.keys(obj)) {
        ...
    }
```

- `prototype`, `length` and `name` are getter/setter in function objects.

- C functions cannot have their own properties (but C constructors
  behave as expected).

- The global object is supported, but its use is discouraged. It
  cannot contain getter/setters and properties directly created in it
  are not visible as global variables in the executing script.

- The variable associated with the `catch` keyword is a normal
  variable.

- Direct `eval` is not supported. Only indirect (=global) `eval` is
  supported.

- No value boxing (e.g. `new Number(1)` is not supported)

- Regexp:

    - case folding only works with ASCII characters.

    - the matching is unicode only i.e. `/./` matches a unicode code
      point instead of an UTF-16 character as with the `u` flag.

- String: `toLowerCase` / `toUpperCase` only handle 