# SILVERPICK

## VERSION

- `v1.0`

## BRIEF

Project `SILVERPICK` is a `Windows User-Mode Shellcode Development Framework (WUMSDF)` whose sole purpose is to empower capability developers to build `Position Independent Code (PIC)` blobs for `Windows` `x64` using `C/C++` in an easy manner so as to reduce the development costs of such an endeavour.

It derives from project [WILDBEAST](https://github.com/winterknife/WILDBEAST) and, as such, leverages:
1. `Visual Studio Code` as the code editor
2. `MinGW-w64` toolchain as the compiler toolchain
3. `GNU Make` as the build system

## SETUP

You may find the setup instructions from here: [GCC-Clang-Setup-Windows](https://gist.github.com/winterknife/0b177a75a55bad895b19aad64cffa14f)

Please note that this project is using [MSYS2](https://www.msys2.org/).

## FEATURES

Writing shellcode in higher-level programming languages is nothing new, and countless blog posts and research papers have been published on the same since 2010. So, what is new in `SILVERPICK`?

Well, I am glad that you asked.

`SILVERPICK` has a nice little bag of tricks hidden up its sleeve, but most of all, this is my take on the subject.

So, without further ado, I present to you my first trick.

### TRICK 01

Ever since Matt Graeber popularised writing shellcode in `C`, most people have been using his [16-byte stack alignment stub written in `Assembly` language](https://github.com/mattifestation/PIC_Bindshell/blob/master/PIC_Bindshell/AdjustStack.asm).

While this is not a problem, seeing as how we aren't `IKEA`, assembly should not be necessary, and indeed it is not.

There exists a [`GCC` Function Attribute](https://gcc.gnu.org/onlinedocs/gcc/Function-Attributes.html) that will emit the stack alignment stub for you.

Meet the `force_align_arg_pointer` function attribute in the form of a helpful [ALIGN_STACK](/Inc/Common.h#L84) macro, which generates the following assembly:
```asm
Disassembly of section .init:

<PicEntry>:
	push   rbp
	mov    rbp,rsp
	and    rsp,0xfffffffffffffff0
	sub    rsp,0x20
	call   <PicEntry+0x11>	IMAGE_REL_AMD64_REL32	.text$payload
	leave
	ret
```

What's the `.init` section, you ask? Well, that serves as a nice segue into my second trick.

### TRICK 02

Matt Graeber might have popularised writing shellcode in `C` at some point, but really, it was Paul Ungur who revived this black art with [Stardust](https://github.com/Cracked5pider/Stardust).

Now, `Stardust` uses a [Binutils linker script](https://sourceware.org/binutils/docs/ld/Scripts.html) to control the placement of functions and data into the appropriate `PE` section in the correct order. This technique itself is derived from Austin Hudson's work, and many people use a variant of his linker scripts.

While linker scripts are great for linker section ordering, if all you need is to place a certain function at the beginning of the code section, they are unnecessary.

Enter the `section` function attribute with a special section name called `.init`, which indicates to the linker that the function contains pre-`main()` runtime initialization code and must be _first_ in the link order.

To this effect, the [CODE_BEGIN](/Inc/Common.h#L81) macro has been created.

### TRICK 03

For my third trick, I present to you the [STACK_STRING](/Inc/StackString.h#L35) macro.

In `C`, you can create a stack string (a string that is dynamically built on the stack) by declaring the string literal as an array of `ANSI` characters:
```c
char charrHelloKitty[] = { 'H', 'e', 'l', 'l', 'o', 'K', 'i', 't', 't', 'y', '\0' };
```

In `C++`, you can create a stack string by simply marking a `char` array as `constexpr`:
```cpp
constexpr char charrHelloKitty[]{ "HelloKitty" };
```

However, both of these techniques are rendered useless in the face of compiler optimizations _if_ the string literals are sufficiently large, unlike our solution, which will work regardless of the string length and the level of compiler optimizations, thanks to some clever `C++` template metaprogramming hack courtesy of Can Bölük.

Using this macro is pretty straightforward:
```c
STACK_STRING(sstrText, "an extra long hello world!");
STACK_STRING(sstrCaption, "Demo");

MessageBoxA(nullptr, sstrText.data(), sstrCaption.data(), MB_OK);
```

This will generate the following assembly:
```asm
mov     [rsp+58h+var_23], 61h ; 'a'
mov     [rsp+58h+var_22], 6Eh ; 'n'
mov     [rsp+58h+var_21], 20h ; ' '
mov     [rsp+58h+var_20], 65h ; 'e'
mov     [rsp+58h+var_1F], 78h ; 'x'
mov     [rsp+58h+var_1E], 74h ; 't'
mov     [rsp+58h+var_1D], 72h ; 'r'
mov     [rsp+58h+var_1C], 61h ; 'a'
mov     [rsp+58h+var_1B], 20h ; ' '
mov     [rsp+58h+var_1A], 6Ch ; 'l'
mov     [rsp+58h+var_19], 6Fh ; 'o'
mov     [rsp+58h+var_18], 6Eh ; 'n'
mov     [rsp+58h+var_17], 67h ; 'g'
mov     [rsp+58h+var_16], 20h ; ' '
mov     [rsp+58h+var_15], 68h ; 'h'
mov     [rsp+58h+var_14], 65h ; 'e'
mov     [r