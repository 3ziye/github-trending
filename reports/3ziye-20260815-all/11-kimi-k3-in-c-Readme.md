<div align="center">

<h1>kimi-k3-in-c</h1>

<h3>A 2.78-trillion-parameter model. One CPU. 8 GB of RAM.</h3>

<p>Kimi K3 inference in portable C99.<br>No BLAS. No framework. No GPU.</p>

<p>
<a href="https://github.com/FareedKhan-dev/kimi-k3-in-c/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/FareedKhan-dev/kimi-k3-in-c/ci.yml?branch=main&style=flat-square&label=CI" alt="CI"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue?style=flat-square" alt="License"></a>
<a href="Makefile"><img src="https://img.shields.io/badge/C99-portable-lightgrey?style=flat-square" alt="C99"></a>
<a href="#requirements"><img src="https://img.shields.io/badge/platform-Linux%20x86--64-lightgrey?style=flat-square" alt="Platform"></a>
<a href="CHANGELOG.md"><img src="https://img.shields.io/badge/version-1.0.0-brightgreen?style=flat-square" alt="Version"></a>
</p>

<table>
<tr>
<td align="center"><b>2.78T</b><br><sub>parameters</sub></td>
<td align="center"><b>1.56 TB</b><br><sub>checkpoint on disk</sub></td>
<td align="center"><b>8.24 GB</b><br><sub>peak RSS, measured</sub></td>
<td align="center"><b>176 KB</b><br><sub>the whole engine</sub></td>
<td align="center"><b>0</b><br><sub>GPUs</sub></td>
</tr>
</table>

<p><b>The same 2.78-trillion-parameter model, the same answer, on whatever machine you own.</b><br>More memory only buys speed:</p>

<table>
<tr>
<th align="left">the machine you have</th>
<th align="right">RAM</th>
<th align="right">time per token</th>
<th align="left">what is going on</th>
</tr>
<tr>
<td align="left">an ordinary laptop</td>
<td align="right">8 GB</td>
<td align="right"><b>26.5 s</b></td>
<td>the whole model streams off the disk on every step</td>
</tr>
<tr>
<td align="left">a high-end laptop</td>
<td align="right">32 GB</td>
<td align="right"><b>24.2 s</b></td>
<td>some of the model now sits in memory</td>
</tr>
<tr>
<td align="left">a desktop</td>
<td align="right">64 GB</td>
<td align="right"><b>19.8 s</b></td>
<td>more of it sits in memory</td>
</tr>
<tr>
<td align="left">a heavy workstation</td>
<td align="right">128 GB+</td>
<td align="right"><b>5.6 s</b></td>
<td>the model fits entirely in memory, the disk wait is gone</td>
</tr>
</table>

<sub>Same short prompt at every size, and the output is <b>byte-identical</b> from the smallest machine to the largest; only the clock changes. One machine, 124 cores, fast NVMe drive: the first three rows still read the model from disk each step, so a slower drive is slower there, while the 128 GB+ row keeps everything in memory and no longer waits on the disk. On that same machine v1.0.0 made the math per token about <b>8&times;</b> lighter, a follow-up question in a chat <b>3.9&times;</b> faster, and long prompts about <b>half</b> as costly. (A token is roughly a short word-piece; the two runnable demos below are the original captures on a slower drive, so their clock reads a little higher.) Full data in <a href="docs/data/">docs/data/</a>.</sub>

<hr>

<p>
  <img src="docs/images/patrick_pray.png" height="44" align="middle" alt="">
  <i>I am open to AI research roles and PhD positions. <a href="https://drive.google.com/file/d/1yW5xHDS6Mr9ByrkCgVve85OqF4UOPv9K/view?usp=sharing">CV</a>.</i>
</p>

<hr>

</div>

<br>

```console
$ ./bin/k3 ~/k3model --trunk ~/k3trunk --preset laptop \
           --tok ~/k3model --prompt "The capital of France is" --gen 8 --incremental

--- generated text ---
 Paris.",
+            "The Eiffel
----------------------
8 tokens in 261.5 s, 32.69 s/token average
PEAK RSS for the whole run: 8.24 GB
```

Slow, and answering correctly, in 8.24 GB, from a checkpoint of 1.56 TB. This is a base
model, so what follows " Paris." is a continuation rather than a reply; there is no chat
template. Give it more memory and the answer does not change, only the clock:

```console
$ ./bin/k3 ~/k3model --trunk ~/k3trunk --preset server \
           --tok ~/k3model --prompt "def fibonacci(n):" --gen 28 --incremental

--- generated text ---
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci
----------------------
28 tokens in 299.3 s, 10.69 s/token average
PEAK RSS for the whole run: 127.92 GB
```

Every figure in this document comes from the measurement output in
[`docs/data/`](docs/data/).

![A small resident working set on top, the model itself on NVMe underneath, and a few labelled pipes between them](docs/images/main_architecture_with_spongbob.png)

The dense trunk stays in memory to whatever depth you choose and streams the rest; the
1.45 TB of routed experts are never resident, and are multiplied straight out of their
packed 4-bit form. The consequence is that **the same model runs in 8 GB and in 224 GB and
produces byte-identical output at every budget between.**

Four decisions about where bytes live take it from a cluster to a laptop, and the answer
at the bottom is the same as the answer at the top:

![Four steps from a server cluster