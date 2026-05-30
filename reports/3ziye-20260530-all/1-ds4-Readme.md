# DwarfStar

**DwarfStar** is a small native inference engine optimized first for
**DeepSeek V4 Flash**, with support for **DeepSeek V4 PRO** on very high-memory
machines. It is
intentionally narrow: not a generic GGUF runner, not a wrapper around another
runtime: it is completely self-contained. Other than running the model in a
correct and fast way, the project goal is to provide DS4 specific loading,
prompt rendering, tool calling, KV state handling (RAM and on-disk), server
API and integrated coding agent, all ready to work with coding agents or with
the provided CLI interface. There are also tools for GGUF and imatrix generation,
and for quality and speed testing.

We support the following backends:
* **Metal** is our primary target. Starting from MacBooks with 96GB of RAM.
* **NVIDIA CUDA** with special care for the DGX Spark.
* **AMD ROCm** is only supported in the [rocm](https://github.com/antirez/ds4/tree/rocm) branch. It is kept separate from main since I (antirez) don't have direct hardware access, so the community rebases the branch as needed.

This project would not exist without **llama.cpp and GGML**, make sure to read
the acknowledgements section, a big thank you to Georgi Gerganov and all the
other contributors.

## Motivations

Now, back at this project. Why do we believe DeepSeek V4 Flash deserves a
standalone engine? Because after comparing it with powerful smaller dense
models, we can report that:

1. DeepSeek V4 Flash is the practical target of the project: it can run on
   96/128GB machines while still feeling much larger than local dense models.
2. DeepSeek V4 PRO is supported too, as a side path for 512GB Mac Studio class
   machines. It is heavier, but it shares the same engine ideas and can be
   useful when the hardware is available.
3. In thinking mode, if you avoid *max thinking*, Flash produces a thinking
   section that is a lot shorter than other models, even 1/5 of other models in
   many cases, and crucially, the thinking section length is **proportional to
   the problem complexity**. This makes DeepSeek V4 Flash usable with thinking
   enabled when other models are practically impossible to use in the same
   conditions.
4. The models feature a context window of **1 million tokens**.
5. Being so large, Flash knows more things if you go sampling at the edge of
   knowledge. For instance asking about Italian show or political questions soon
   uncovers that 284B parameters are a lot more than 27B or 35B parameters. PRO
   pushes further when you can run it.
6. Flash writes much better English and Italian. It *feels* a quasi-frontier
   model. PRO is stronger still, especially for tasks such as translation.
7. The KV cache is incredibly compressed, allowing long context inference on
   local computers and **on disk KV cache persistence**.
8. Both DeepSeek V4 variants work well with 2-bit quantization, if quantized in
   a special way (read later). This allows Flash to run on MacBooks with 128GB
   of RAM (and many people reported it working with 96GB as well, even at 250k
   context window!), and PRO on 512GB machines.
9. We expect DeepSeek to release **updated versions of V4 Flash and PRO** in the
   future, even better than the current ones.

That said, a few important things about this project:

* The local inference landscape contains many excellent projects, but new models are released continuously, and the attention immediately gets captured by the next model to implement. This project takes a deliberately narrow bet: one model at a time, official-vector validation (logits obtained with the official implementation), long-context tests, and enough agent integration to know if it really works. The exact model may change as the landscape evolves, but the constraint remains: local inference credible on high end personal machines or Mac Studios, starting from 96/128GB of memory.
* This software is developed with **strong assistance from GPT 5.5** and with humans leading the ideas, testing, and debugging. We say this openly because it shaped how the project was built. If you are not happy with AI-developed code, this software is not for you. The acknowledgement below is equally important: this would not exist without `llama.cpp` and GGML, largely written by hand.
* This implementation is based on the idea that compressed KV caches like the one of DeepSeek v4 and the fast SSD disks of modern MacBooks should change our idea that KV cache belongs to RAM. **The KV cache is actually a first-class disk citizen**.
* Our vision is that local inference should be a set of three things working well together, out of the box: A) inference engine with HTTP API + B) GGUF specially crafted to run well under a given engine and given assumptions + C) testing and validation with coding agents implementations. This inference engine only runs with the GGUF files provided. It gets tested against officially obtained logits at different context sizes. This project exists because we wanted to make 