<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="logo-dark.png">
    <img width="55%" src="logo-light.png" alt="torchcomms">
  </picture>
</p>


# torchcomms

torchcomms is a new experimental communications API for PyTorch. This provides
both the high level collectives API as well as several out of the box backends.

* [Documentation](https://meta-pytorch.org/torchcomms/main/index.html)
* [Examples](./comms/torchcomms/examples)

## Prerequisites

torchcomms requires the following software and hardware:

- Python 3.10 or higher
- PyTorch 2.8 or higher
- CUDA-capable GPU (for NCCL/NCCLX or RCCL backends)

## Installation

torchcomms is available on PyPI and can be installed using pip. Alternatively,
you can build torchcomms from source.

### Using pip (Nightly Builds)

You can install torchcomms and PyTorch nightly builds using pip:

```bash
# Cuda 12.6
pip install --pre torch torchcomms --index-url https://download.pytorch.org/whl/nightly/cu126

# Cuda 12.8
pip install --pre torch torchcomms --index-url https://download.pytorch.org/whl/nightly/cu128

# Cuda 12.9
pip install --pre torch torchcomms --index-url https://download.pytorch.org/whl/nightly/cu129

# Cuda 13.0
pip install --pre torch torchcomms --index-url https://download.pytorch.org/whl/nightly/cu130
```

### Building from Source

#### Prerequisites

- CMake 3.22 or higher
- Ninja 1.10 or higher

Alternatively, you can build torchcomms from source. If you want to build the NCCLX backend, we recommend building it under a virtual conda environment.
Run the following commands to build and install torchcomms:

```bash
# Create a conda environment
conda create -n torchcomms python=3.10
conda activate torchcomms
# Clone the repository
git clone git@github.com:meta-pytorch/torchcomms.git
cd torchcomms
```

#### Build the backend (choose one based on your hardware):

##### Standard NCCL Backend

No build needed - uses the library provided by PyTorch

##### NCCLX Backend

If you want to install the third-party dependencies directly from conda, run the following command:
```bash
USE_SYSTEM_LIBS=1 ./build_ncclx.sh
```

If you want to build and install the third-party dependencies from source, run the following command:
```bash
./build_ncclx.sh
```

##### RCCL Backend

Install some prerequisites
```
conda install conda-forge::glog=0.4.0 conda-forge::gflags conda-forge::fmt -y
```

Environment variables to find rocm/rccl headers
```
export ROCM_HOME=/opt/rocm
export RCCL_INCLUDE=$ROCM_HOME/include/rccl
```

```bash
./build_rccl.sh
```

##### RCCLX Backend

Install some prerequisites
```
conda install conda-forge::glog=0.4.0 conda-forge::gflags conda-forge::fmt -y
```

Environment variables to find rocm/rcclx headers
```
export BUILD_DIR=${PWD}/comms/rcclx/develop/build/release/build
export ROCM_HOME=/opt/rocm
export RCCLX_INCLUDE=${BUILD_DIR}/include/rccl
export RCCLX_LIB=${BUILD_DIR}/lib
```

```bash
./build_rcclx.sh
```


#### Install torchcomms:

```bash
# Install PyTorch (if not already installed)
pip install -r requirements.txt
pip install --no-build-isolation -v .
```

### Build Configuration

You can customize the build by setting environment variables before running pip install:

```bash
# Enable/disable specific backends (ON/OFF or 1/0)
export USE_NCCL=ON    # Default: ON
export USE_NCCLX=ON   # Default: ON
export USE_GLOO=ON    # Default: ON
export USE_RCCL=OFF   # Default: OFF
export USE_RCCLX=OFF  # Default: OFF
```

Then run:

```bash
# Install PyTorch (if not already installed)
pip install -r requirements.txt
pip install --no-build-isolation -v .
```

## Quick Start Example

Here's a simple example demonstrating synchronous `AllReduce` communication across multiple GPUs:

```python
#!/usr/bin/env python3
# example.py
import torch
from torchcomms import new_comm, ReduceOp

def main():
    # Initialize TorchComm with NCCLX backend
    device = torch.device("cuda")
    torchcomm = new_comm("nccl", device, name="main_comm")

    # Get rank and world size
    rank = torchcomm.get_rank()
    world_size = torchcomm.get_size()

    # Calculate device ID
    num_devices = torch.cuda.device_count()
    device_id = rank % num_devices
    target_device = torch.device(f"cuda:{device_id}")

    print(f"Rank {rank}/{world_size}: Running on device {device_id}")

    # Create a tensor with rank-specific data
    tensor = torch.full(
        (1024,),
        float(rank + 1),
        dtype=torch.float32,
        device=target_device
    )

    print(f"Rank {rank}: Before AllReduce: {tensor[0].item()}")

    # Perform synchronous AllReduce (sum across all ranks)
    torchcomm.all_reduce(tensor, ReduceOp.SUM, async_op=False)

    # Synchronize CUDA stream
    torch.cuda.current_stream().synchronize()

    print(f"Rank {rank}: After AllReduce: {tensor[0].item()}")

    # Cleanup
    torchcomm.finalize()

if __name__ == "__main__":
    main()
```

### Running the Example

To run this example with multiple processes (one per GPU):

`