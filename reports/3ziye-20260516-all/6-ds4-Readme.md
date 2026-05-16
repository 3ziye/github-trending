# DwarfStar 4

DwarfStar 4 is a small native inference engine specific for **DeepSeek V4 Flash**. It is
intentionally narrow: not a generic GGUF runner, not a wrapper around another
runtime: it is completely self-contained. Other than running the model in a
correct and fast way, the project goal is to provide DS4 specific loading,
prompt rendering, tool calling, KV state handling (RAM and on-disk), and server
API, all ready to work with coding agents or with the provided CLI interface.
There are also tools for GGUF and imatrix generation, and for quality and
speed testing.

We support the following backends:
* **Metal** is our primary target. Starting from MacBooks with 96GB of RAM.
* **NVIDIA CUDA** with special care for the DGX Spark.
* **AMD ROCm** is only supported in the [rocm](https://github.com/antirez/ds4/tree/rocm) branch. It is kept separate from main since I (antirez) don't have direct hardware access, so the community rebases the branch as needed.

This project would not exist without **llama.cpp and GGML**, make sure to read
the acknowledgements section, a big thank you to Georgi Gerganov and all the
other contributors.

## Motivations

Now, back at this project. Why we believe DeepSeek v4 Flash to be a pretty special
model deserving a standalone engine? Because after comparing it with powerful smaller
dense models, we can report that:

1. DeepSeek v4 Flash is faster because of less active parameters.
2. In thinking mode, if you avoid *max thinking*, it produces a thinking section that is a lot shorter than other models, even 1/5 of other models in many cases, and crucially, the thinking section length is **proportional to the problem complexity**. This makes DeepSeek v4 Flash usable with thinking enabled when other models are practically impossible to use in the same conditions.
3. The model features a context window of **1 million tokens**.
4. Being so large, it knows more things if you go sampling at the edge of knowledge. For instance asking about Italian show or political questions soon uncovers that 284B parameters are a lot more than 27B or 35B parameters.
5. It writes much better English and Italian. It *feels* a quasi-frontier model.
6. The KV cache is incredibly compressed, allowing long context inference on local computers and **on disk KV cache persistence**.
7. It works well with 2-bit quantization, if quantized in a special way (read later). This allows to run it in MacBooks with 128GB of RAM (and many people reported it working with 96GB as well, even at 250k context window!).
8. We expect DeepSeek to release **updated versions of v4 Flash** in the future, even better than the current one.

That said, a few important things about this project:

* The local inference landscape contains many excellent projects, but new models are released continuously, and the attention immediately gets captured by the next model to implement. This project takes a deliberately narrow bet: one model at a time, official-vector validation (logits obtained with the official implementation), long-context tests, and enough agent integration to know if it really works. The exact model may change as the landscape evolves, but the constraint remains: local inference credible on high end personal machines or Mac Studios, starting from 96/128GB of memory.
* This software is developed with **strong assistance from GPT 5.5** and with humans leading the ideas, testing, and debugging. We say this openly because it shaped how the project was built. If you are not happy with AI-developed code, this software is not for you. The acknowledgement below is equally important: this would not exist without `llama.cpp` and GGML, largely written by hand.
* This implementation is based on the idea that compressed KV caches like the one of DeepSeek v4 and the fast SSD disks of modern MacBooks should change our idea that KV cache belongs to RAM. **The KV cache is actually a first-class disk citizen**.
* Our vision is that local inference should be a set of three things working well together, out of the box: A) inference engine with HTTP API + B) GGUF specially crafted to run well under a given engine and given assumptions + C) testing and validation with coding agents implementations. This inference engine only runs with the GGUF files provided. It gets tested against officially obtained logits at different context sizes. This project exists because we wanted to make one local model feel finished end to end, not just runnable. However this is just alpha quality code, so probably we are not still there.
* The optimized graph path targets **Metal on macOS** and **CUDA on Linux**. The CPU path is only for correctness checks and model/tokenizer diagnostics. For CPU-only Linux builds, use `make cpu`; it builds the normal `./ds4` and `./ds4-server` binaries without CUDA or Metal. On macOS, **warning: current macOS versions have a bug in the virtual memory implementation that will crash the kernel** if you try to run the CPU code. Rem