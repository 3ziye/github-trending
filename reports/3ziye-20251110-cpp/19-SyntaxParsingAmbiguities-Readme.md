# Syntax Parsing Ambiguities

This repository contains code examples demonstrating syntax parsing ambiguities in C++. Ambiguities organized into three separate buckets: **Syntactic**, **Lexical**, and **Semantic**. It also contains a custom language interpreter to show the complexity of parsing the syntax of a program.

## Code Examples

### 1. The Most Vexing Parse (`vex.cpp`)

```bash
g++ -std=c++20 vex.cpp -o vex
./vex
```

### 2. The Dangling Else (`dangle_login.cpp`)

```bash
g++ -std=c++20 dangle_login.cpp -o dangle_login
./dangle_login
```

### 3. Bonus Example (`hmm.cpp`)

```bash
g++ -std=c++20 hmm.cpp -o hmm
./hmm
```

### 4. Nested Generics (`nest.cpp`)

```bash
# This fails in C++98
g++ -std=c++98 nest.cpp -o nest

# This works in C++11 and later
g++ -std=c++20 nest.cpp -o nest
./nest
```

### 5. Dependent Type Names (`temple.cpp`)

```bash
g++ -std=c++20 temple.cpp -o temple
./temple
```

### 6. Dependent Template Functions (`less.cpp`)

```bash
g++ -std=c++20 less.cpp -o less
./less
```

## Custom Parser

The `CustomParser/` directory contains **Rember Script**, a toy language interpreter built with Flex and Bison, demonstrating how to create custom parsers.

**Build and Run**:
```bash
cd CustomParser
make
./remberscript test.rember
```
