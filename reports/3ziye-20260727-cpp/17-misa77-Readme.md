# misa77 (0.5.0)

misa77 is an LZ-based codec that targets the write-once, read-many niche. In particular, it aims to satisfy the following criteria:

- Extremely high decompression throughput (single-threaded).
- Modest compression ratios (LZ4 at high effort levels is a good reference point).
- Constant memory use during compression, regardless of input size (5-16 MB for levels 0-1, ~160 MB for level 2). Decompression uses no extra memory.

Slow compression is the obvious tradeoff that one makes to achieve the above.

In addition, misa77 has a somewhat synergizing tendency to decompress highly compressed files faster. This makes high-effort compression particularly attractive for misa77, and inspires some experimental compression modes (refer to [src/experimental/](src/experimental/)) that aim to spend more effort at compression time to produce a compressed stream that is friendlier to the microarchitectures of most CPUs when decompressing said streams.

misa77 has three compression effort levels as of v0.5.0:

- level 0: offers better decode throughput, slightly worse ratio, similar encode throughput
- level 1 (default): offers slightly worse decode throughput, better ratio, similar encode throughput
- level 2: offers similar decode throughput to level 1, the best ratio (slightly better than `lz4hc -12`), very low encode throughput

There are two decompressor modes:

- unsafe: passing invalid input to this mode is UB.
- safe: guaranteed to exit gracefully (ie. provably terminate, and not access out-of-bounds memory or engage in any other UB) in the case of corrupt/malicious input, is 2-4% slower than unsafe.

Note: as of now, level 2 doesn't have a safe decompressor. It will be added soon.

## Benchmarks

Detailed results are listed ahead, but here's a terse summary:

- misa77 lies on the pareto frontier for decompression throughput vs compression ratio on most shapes of data.
- It very frequently decompresses faster even when competitors have a significantly worse ratio.
- It is quite slow at compression.
- Performance is a bit sensitive to codegen, but even with the worst possible codegen I saw in my testing, misa77 was significantly faster than other codecs.

Let's first see some cross-platform results for the [Silesia Corpus](https://sun.aei.polsl.pl//~sdeor/corpus/silesia.zip).

Note:

1. "Ratio" ahead is equal to `((compressed size)/(original)) * 100` (so lower is better).
2. The benchmarking harness is a public fork of lzbench, and can be accessed [here](https://github.com/welcome-to-the-sunny-side/lzbench/tree/add-misa77-0.4.0).
3. In the tables ahead, rows are sorted by decompression speed.

---

### Intel x86-64

Details:

- CPU: Intel(R) Core(TM) i7-14650HX (@2.2 GHz) (Intel Turbo disabled).
- Single threaded, pinned to a single performance core.
- CPU governor set to `performance`.

| Compressor name       | Compression | Decompress. |  Ratio | Filename    |
| --------------------- | ----------- | ----------- | ------ | ----------- |
| misa77 0.5.0 -0       |   54.3 MB/s |   5359 MB/s |  42.64 | silesia.tar |
| misa77 0.5.0 safe -0  |   54.1 MB/s |   5216 MB/s |  42.64 | silesia.tar |
| misa77 0.5.0 -2       |   7.01 MB/s |   4470 MB/s |  35.51 | silesia.tar |
| misa77 0.5.0 -1       |   51.2 MB/s |   4378 MB/s |  39.65 | silesia.tar |
| misa77 0.5.0 safe -1  |   51.2 MB/s |   4252 MB/s |  39.65 | silesia.tar |
| zxc 0.13.1 -3         |    116 MB/s |   2838 MB/s |  45.46 | silesia.tar |
| zxc 0.13.1 -4         |   81.2 MB/s |   2726 MB/s |  42.63 | silesia.tar |
| lzsse8fast 2019-04-18 |    183 MB/s |   2663 MB/s |  44.80 | silesia.tar |
| zxc 0.13.1 -5         |   48.4 MB/s |   2602 MB/s |  40.25 | silesia.tar |
| lz4hc 1.10.0 -12      |   7.31 MB/s |   2531 MB/s |  36.45 | silesia.tar |
| lzsse4fast 2019-04-18 |    187 MB/s |   2525 MB/s |  45.26 | silesia.tar |
| lz4 1.10.0            |    371 MB/s |   2506 MB/s |  47.59 | silesia.tar |
| lz4hc 1.10.0 -9       |   22.0 MB/s |   2454 MB/s |  36.75 | silesia.tar |
| lzav 5.11 -2          |   58.4 MB/s |   1729 MB/s |  34.97 | silesia.tar |
| zxc 0.13.1 -7         |   4.27 MB/s |   1645 MB/s |  33.00 | silesia.tar |
| zstd 1.5.7 -1         |    297 MB/s |    903 MB/s |  34.54 | silesia.tar |
| snappy 1.2.2          |    376 MB/s |    858 MB/s |  47.89 | silesia.tar |

---

### ARM64 (Apple Silicon)

Details: 

- CPU: Apple M3

| Compressor name      | Compression | Decompress. |  Ratio | Filename    |
| -------------------- | ----------- | ----------- | ------ | ----------- |
| misa77 0.5.0 -0      |    134 MB/s |  12660 MB/s |  42.64 | silesia.tar |
| misa77 0.5.0 safe -0 |    134 MB/s |  12484 MB/s |  42.64 | silesia.tar |
| misa77 0.5.0 -1      |    127 MB/s |  10270 MB/s |  39.65 | silesia.tar |
| misa77 0.5.0 safe -1 |    127 MB/s |  10100 MB/s |  39.65 | silesia.tar |
| misa77 0.5.0 -2      |   13.6 MB/s |   9935 MB/s |  35.51 | silesia.tar |
| zxc 0.13.1 -3        |    279 MB/s |   8030 MB/s |  45.77 | silesia.tar |
| zxc 0.13.1 -4     