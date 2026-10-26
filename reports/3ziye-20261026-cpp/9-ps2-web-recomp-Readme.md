# PS2 Web Recomp

PlayStation 2 games running in the browser through static recompilation. The game's Emotion Engine machine code is translated ahead of time into C++ and compiled to WebAssembly, so the main CPU is never interpreted; the rest of the console, its operating system and hardware, is emulated by a runtime that draws with WebGPU.

<p align="center">
  <img src="docs/media/demo.webp" alt="Gran Turismo 4 running in a browser" width="720">
  <br>
  <a href="docs/media/demo.mp4">Watch the full recording (1:24)</a>
</p>

This is the sibling of [psp-web-recomp](https://github.com/snuri00/psp-web-recomp) and follows the same method. The first title brought up this way is Gran Turismo 4, chosen because it is one of the most demanding games on the system: it leans on both vector units, on exact floating point behaviour for its replays and license tests, and on graphics tricks that read rendered images back as palettes. It plays from boot through the opening movie, the menus and races, with music and sound effects, and saves to a memory card kept in the browser. A race runs at full speed, 50 frames per second for this PAL release, in Chrome on a laptop's integrated GPU at twice the PS2's resolution, which is how the recording above was made.

God of War II followed through the same scripts. It needed no game-specific code, but it found two bugs that Gran Turismo 4 had never triggered, one in the recompiler and one in the vector unit timing, and a few missing pieces of the PS2's input/output processor. It now plays from the menus through its cutscenes into combat, and holds 60 frames per second in heavy combat at the PS2's resolution in Chrome. At twice the resolution it runs at 48 to 60, limited by the laptop's integrated GPU.

No game data is included here. You bring a disc image of a game you own, and the scripts in this repository turn it into a web page on your machine.

## How it works

**Recompilation.** `eerecomp` reads the game's executable, follows its control flow to find the functions and emits C++ for them in units of 16 KiB of guest code. The output keeps the R5900's quirks: 128-bit registers and the multimedia instructions that work on them, branch delay slots, the PS2's floating point unit, which has no infinities or denormals and rounds differently from IEEE, and vector unit 0 used as a coprocessor. Jumps between units become tail calls, and a thread switch unwinds the host stack and resumes at the guest address, so the generated code never needs a stack per guest thread.

**A small PS2 kernel.** The EE side of the operating system is answered by high-level emulation: threads, semaphores, interrupt handlers for the DMA controller and the vertical blank, alarms, and the SIF channel that connects the main CPU to the I/O processor. The I/O processor runs the game's own IRX modules, the sound driver, the disc streaming code and the controller and memory card drivers that ship on the disc, on an interpreter of its R3000 CPU, while the IOP kernel and the libraries those modules call are reimplemented in C++. The disc is read over HTTP Range requests, so only the executable is downloaded up front.

**Vector units.** Most of a PS2 game's 3D work happens in microprograms the game uploads to vector unit 1. They run with the pipeline delays of the MAC, status and clip flags modelled, because games schedule their code around them, and with the PS2's float rules for special values: no infinities or NaNs, denormals flushed to zero and overflow clamped to the largest float. The arithmetic itself is the host's, so a result can differ from the console's in its last bit; the console truncates where the host rounds, and its multiplier is not exact. Microprograms seen during a test run are compiled ahead of time into SIMD C++; any the page meets for the first time are translated into a WebAssembly module on the spot, which takes a few milliseconds per program.

**Graphics.** The Graphics Synthesizer's 4 MB of video memory lives on the GPU, in its native swizzled layouts, and drawing is done by WebGPU compute shaders: triangles are binned into tiles and rasterized with the GS's own rules for texturing, palettes, alpha blending, depth and destination alpha tests. Because everything stays in GS memory, effects that render into a texture or reinterpret a framebuffer as a palette work the way they do on the console. The internal resolution can be one, two or three times the native one. A software rasterizer of the same GS remains as the reference the GPU output is compared against.

**Threads.** The emulation runs in a worker, vector unit 1 has a worker of its own the way it runs in parallel on the console, and the GS commands go through a ring buffer to the page thread, which owns the WebGPU device.

**Sound and movies.** The SPU2 is reimplemented with its 48 voices of ADPCM, ADSR envelopes and the streaming DMA games use for music, and its output goes to an AudioWorklet through shared memory. Movies are decoded b