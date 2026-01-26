# Zyrox LLVM Obfuscator

### llvm compile and link-time plugin for obfuscating native code

# Why

why not ¯\\\_(ツ)\_/¯

One of my biggest projects, where I learned a lot about LLVM internals, binary formats, assembly and obfuscation techniques.

I believe that learning through building is the best way to learn, thus I built this project to learn more about these topics.

# Research

I have wrote 4 blogs explaining the concepts behind [Zyrox](https://peterr.dev/blogs/zyrox):

-   [Part I: Building Zyrox: A Custom LLVM Obfuscator](https://peterr.dev/blogs/zyrox/llvm-obfuscator-part-one)
-   [Part II: Control Flow Flattening](https://peterr.dev/blogs/zyrox/llvm-obfuscator-part-two)
-   [Part III: Encrypted Jump Tables](https://peterr.dev/blogs/zyrox/llvm-obfuscator-part-three)
-   [Part IV: The Finale](https://peterr.dev/blogs/zyrox/llvm-obfuscator-part-four)

These parts go deeper than this readme, and definitely worth a read if you are interested in the topic.

# Building

## From Template (Quick Start, Recommended)

This is intended for who wants to _quick test_ Zyrox, or learn how to integrate it in a cmake project.

Follow the steps in [Zyrox Template](https://github.com/PeterHackz/zyrox-template) repo.

## From Source

install llvm:

```shell
sudo apt update
sudo apt install llvm-18 llvm-18-dev clang-18
```

clone and compile zyrox:

```shell
git clone --recurse-submodules https://github.com/PeterHackz/zyrox.git
cd zyrox
cmake -S . -B build -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++
cmake --build build --parallel 4
```

## Python (Post-Compile) Plugin setup

make sure you have python3 and pip installed.

### Setup an Environment (Recommended)

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the env
source .venv/bin/activate

pip install -r requirements.txt
```

### Install Globally

```bash
pip install -r requirements.txt
```

# Usage

## Quick Usage

```shell
clang -O0 -flto=full -c main.c -o out/main.o
clang -flto=full -fuse-ld=lld -Wl,--load-pass-plugin=./build/libzyrox.so out/main.o -o out/main
```

After obfuscation, run `PyPlugin.py` to encrypt jump tables:

```shell
# if you installed dependencies in a virtual environment, activate it first:
source .venv/bin/activate
#  then run with:
python PyPlugin.py --in=<input_file> [--out=<output_file>] [--tables=<zyrox_tables_file>] [--android]
```

## With CMake

Check out the [Zyrox Template](https://github.com/PeterHackz/zyrox-template) repo for an example CMake integration.

# Contacts

I get this is a complex topic, and this project was mostly for educational purposes, as well as to serve BSD Brawl.
If you have any question, or just want to chat, feel free to reach out to me:

-   Discord: `@s.b`
-   Email: `mail@peterr.dev` or `me@peterr.dev`
-   [Discord Server](https://discord.peterr.dev)

any help, through pull requests or issues is appreciated!

# How it works

`ZyroxPlugin.cpp` registers the pass, then links `siphash` (more on this later) and call `StringEncryption` to encrypt
strings.

The reason we encrypt strings early is so that decryption logic gets obfuscated too later.

then it calls `ModuleUtils::ExpandCustomAnnotations`
and `QuickConfig::RegisterPasses` to parse all `__attribute__((annotate("...")))` expressions and run
QuickJs config (located in `ZyroxConfig.js`)

Every function is obfuscated by calling `Zyrox::RunOnFunction` located in `ZyroxCore.cpp`,
more documentation about this will be provided in the future.

# Extra Util

switches create jump tables and PHI nodes are annoying to deal with thus we use `FunctionUtils` and `BasicBlockUtils`
to flatten (into if statements) and demote these respectively.

# Passes

oh man, where do I start

-   [Basic Block Splitter](#basic-block-splitter)
-   [Control Flow Flattening](#control-flow-flattening)
-   [Indirect Branching](#indirect-branching)
-   [Simple Indirect Branching](#simple-indirect-branching)
-   [Mixed Boolean Arithmetic](#mixed-boolean-arithmetic)

all js-plugin args are in `index.d.ts` so will not be talked about in this documentation.

for annotations documentation, [click here](#zyrox-annotations)

# Basic Block Splitter

This pass splits and shuffles a basic block into smaller ones. suppose we have this:

```c++
int __test_fn(int x)
{
    if (x == 2) {
        printf("x is 2\n");
    } else {
        printf("x is not 2!, x is: %d\n", x);
    }
    return x + 4 * x - 2 / 4;
}
```

which gets compiled into:

```asm
define internal i32 @__test_fn(i32 noundef %0) #0 !zyrox !8 !obfuscated !11 {
  %2 = alloca i32, align 4
  store i32 %0, ptr %2, align 4
  %3 = load i32, ptr %2, align 4
  %4 = icmp eq i32 %3, 2
  br i1 %4, label %5, label %7

5:                                                ; preds = %1
  %6 = call i32 (ptr, ...) @printf(ptr noundef @.str.1)
  br label %10

7:                                                ; preds = %1
  %8 = load i32, ptr %2, align 4
  %9 = call i32 (ptr, ...) @printf(ptr noundef @.str.2, i