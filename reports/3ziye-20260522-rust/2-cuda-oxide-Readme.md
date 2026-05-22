<p align="center">
  <a href="https://github.com/NVlabs/cuda-oxide/actions/workflows/clippy.yml"><img alt="clippy" src="https://github.com/NVlabs/cuda-oxide/actions/workflows/clippy.yml/badge.svg?branch=main"></a>
  <a href="https://github.com/NVlabs/cuda-oxide/actions/workflows/unit-tests.yml"><img alt="unit-tests" src="https://github.com/NVlabs/cuda-oxide/actions/workflows/unit-tests.yml/badge.svg?branch=main"></a>
  <a href="https://github.com/NVlabs/cuda-oxide/actions/workflows/cargo-deny.yml"><img alt="cargo-deny" src="https://github.com/NVlabs/cuda-oxide/actions/workflows/cargo-deny.yml/badge.svg?branch=main"></a>
  <a href="https://github.com/NVlabs/cuda-oxide/actions/workflows/codeql.yml"><img alt="CodeQL" src="https://github.com/NVlabs/cuda-oxide/actions/workflows/codeql.yml/badge.svg?branch=main"></a>
  <br>
  <img src="assets/logo.png" alt="cuda-oxide logo" width="100%">
</p>

# cuda-oxide

cuda-oxide is a custom rustc backend for compiling GPU kernels in pure Rust.
The workspace combines:

- single-source compilation -- host and device code live in the same file, built with one `cargo oxide build`
- a rustc codegen backend that compiles `#[kernel]` functions to CUDA PTX
- device-side abstractions (type-safe indexing, shared memory, scoped atomics, barriers, TMA, warp/cluster ops)
- a host-side runtime for memory management, pinned host transfers, and kernel launching (`cuda-core`, `cuda-async`)
- a rust-native compilation pipeline using [Pliron](https://github.com/vaivaswatha/pliron), an MLIR-like IR framework in Rust (Rust → Rust MIR → Pliron IR → LLVM IR → PTX)

## Project Status

cuda-oxide is an experimental compiler that demonstrates how CUDA SIMT kernels can be written natively in pure Rust -- no DSLs, no foreign language bindings -- and made available to the broader Rust community. The project is in an early stage (alpha) and under active development: you should expect bugs, incomplete features, and API breakage as we work to improve it. That said, we hope you'll try it in your own work and help shape its direction by sharing feedback on your experience.

Please see [CONTRIBUTING.md](CONTRIBUTING.md) if you're interested in contributing to the project.

## Quick Start

```rust
use cuda_device::{cuda_module, kernel, thread, DisjointSlice};
use cuda_core::{CudaContext, DeviceBuffer, LaunchConfig};

// Device: generic kernel that applies any function to each element.
// F can be a closure with captures — rustc monomorphizes it to a concrete type.
#[cuda_module]
mod kernels {
    use super::*;

    #[kernel]
    pub fn map<T: Copy, F: Fn(T) -> T + Copy>(f: F, input: &[T], mut out: DisjointSlice<T>) {
        let idx = thread::index_1d();
        let i = idx.get();
        if let Some(out_elem) = out.get_mut(idx) {
            *out_elem = f(input[i]);
        }
    }
}

fn main() {
    let ctx = CudaContext::new(0).unwrap();
    let stream = ctx.default_stream();

    let data: Vec<f32> = (0..1024).map(|i| i as f32).collect();
    let input = DeviceBuffer::from_host(&stream, &data).unwrap();
    let mut output = DeviceBuffer::<f32>::zeroed(&stream, 1024).unwrap();

    let module = kernels::load(&ctx).unwrap();

    // Launch with a closure — factor is captured and passed to the GPU automatically
    let factor = 2.5f32;
    module
        .map::<f32, _>(
            &stream,
            LaunchConfig::for_num_elems(1024),
            move |x: f32| x * factor,
            &input,
            &mut output,
        )
        .unwrap();

    let result = output.to_host_vec(&stream).unwrap();
    assert!((result[1] - 2.5).abs() < 1e-5);
}
```

The above example defines a generic `#[kernel]` function `map` that accepts any
`Fn(T) -> T` closure. `#[cuda_module]` embeds the generated device artifact into
the host binary and generates a typed `module.map::<f32, _>(...)` launch method.
The closure `move |x| x * factor` is captured, scalarized, and passed as kernel
parameters automatically.

For composable async GPU work, `stream:` disappears, `{kernel}_async` returns a
lazy `DeviceOperation`, and execution happens when you call `.sync()` or
`.await`.

```rust
use cuda_async::device_operation::DeviceOperation;

// Assuming `module`, `input`, and `output` come from the cuda-async setup:
let factor = 2.5f32;
module
    .map_async::<f32, _>(
        LaunchConfig::for_num_elems(1024),
        move |x: f32| x * factor,
        &input,
        &mut output,
    )?
    .sync()?;
// or: .await?;
```

See the `async_mlp` example and `crates/cuda-async/README.md` for the full async setup.

```bash
# Build and run an example
cargo oxide run host_closure

# Show full compilation pipeline (Rust MIR → dialect-mir → mem2reg → dialect-llvm → LLVM IR → PTX)
cargo oxide pipeline vecadd

# Debug with cuda-gdb
cargo oxide debug vecadd --tui
```

## Setup

### Requirements

- **cargo-oxide** — cargo subcommand that drives the build pipeline (`cargo oxide run`, `build`, `debug`, etc.)
- **Rust nightly** with `rust-src` and `rus