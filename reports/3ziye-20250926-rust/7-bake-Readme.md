# bake

`bake` is a Linux CLI tool that can embed microVM resources (firecracker binary, kernel, initrd, boot disk) into itself. It also implements bidirectional communication between VM and host - including networking and directory sharing - entirely in userspace, without requiring root privilege.

## Usage

The Docker image includes pre-packaged `bake`, firecracker, kernel and initrd binaries for amd64 and arm64 platforms.

```bash
# make sure `./rootfs.squashfs.img` exists
# create output directory
$ mkdir -p output

# assuming you are building on an amd64 host for an amd64 target
$ docker run -it --rm \
  -v ./rootfs.squashfs.img:/rootfs.img:ro \
  -v ./output:/output \
  --entrypoint /opt/bake/bake.amd64 \
  ghcr.io/losfair/bake \
  --input /opt/bake/bake.amd64 \
  --firecracker /opt/bake/firecracker.amd64 \
  --kernel /opt/bake/kernel.amd64 \
  --initrd /opt/bake/initrd.amd64.img \
  --rootfs /rootfs.img \
  --output /output/app.elf

# start microVM and print uname
$ ./output/app.elf -- uname -a
Linux container 6.1.149-bottlefire #1 SMP Sat Sep  6 13:50:25 UTC 2025 x86_64 GNU/Linux

# show usage
$ ./output/app.elf --help
Bottlefire microVM Image

Usage: app.elf [OPTIONS] [SUBCOMMAND]

Options:
      --cpus <CPUS>              Number of CPU cores
      --memory <MEMORY>          Amount of memory (in MB) allocated to the microVM [default: 256]
      --boot-args <BOOT_ARGS>    Kernel command line [default: "console=ttyS0 reboot=k panic=-1"]
      --entrypoint <ENTRYPOINT>  Container entrypoint
      --                         Separator; everything after goes to the container
      --env <KEY=VALUE>          Container environment variables
      --verbose                  Enable verbose output
      --cwd <CWD>                Container working directory [default: ]
  -p, --publish <HOST:VM>        Publish host:vm port forward (e.g. -p 8080:8080)
  -v, --volume <HOST:VM[:ro]>    Directory/volume mappings (e.g. -v ./data:/data)
  -h, --help                     Print help

Subcommands:
  ssh        Auto-connect to the running microVM via SSH
             Options: -p, --pid <PID>
             Pass-through: arguments after `--` go to ssh(1)
  systemd    Print a systemd service unit and exit
```

## How it works

Depending on whether embedded data is detected and whether running as PID 1, `bake` runs in one of the following modes:

- If PID is 1 and env var `BAKE_NOT_INIT` is not `1`: vminit mode. `bake` assumes that it is running as the init task inside the Firecracker VM, and perform the init sequence.
- If PID is not 1, and embedded data is detected: run mode - accept Firecracker startup parameters (e.g. number of CPUs, memory size, network config), extract kernel and initrd into memfd, start firecracker.
- If PID is not 1, and embedded data is not detected: build mode - accept `--input`, `--firecracker`, `--kernel`, `--initrd`, `--rootfs`, build a binary from `/proc/self/exe` (or the provided input elf) with everything embedded.

### Init sequence (src/vminit.rs)

When running as PID 1 inside the microVM, `bake` executes an init routine that prepares the root filesystem, host-guest connectivity, optional volume mounts, and finally launches the container process with `runc`.

- Bootstrap system mounts and loopback
  - Mount `proc`, `sysfs`, `devtmpfs`, and unified `cgroup2`.
  - Bring `lo` up.

- Parse kernel cmdline and banner
  - Read `/proc/cmdline`, parse `bake.*` parameters and `quiet`.
  - If not quiet, print a banner and `/proc/version` for diagnostics.
  - Fetch BootManifest from host vsock port 13 containing container runtime parameters.

- Expose embedded rootfs via device-mapper
  - Read `bake.rootfs_offset` and `bake.rootfs_size` (sectors) from cmdline.
  - Create a linear mapping `rootfs` with `dmsetup` over `/dev/vda` at the given offset/size.

- Build overlay root on top of ephemeral disk
  - Format `/dev/vdb` as ext4 and mount at `/ephemeral`.
  - Prepare overlay dirs: `/ephemeral/rootfs.overlay/{upper,work}` and `/ephemeral/container-tmp` (mode 1777).
  - Mount the base rootfs from `/dev/mapper/rootfs` at `/rootfs.base`.
  - Mount an overlay at `/rootfs` with `lowerdir=/rootfs.base`, `upperdir=/ephemeral/rootfs.overlay/upper`, `workdir=/ephemeral/rootfs.overlay/work`.

- Set up host-guest networking over vsock with SOCKS5 and tun2socks
  - Inside the VM, start a SOCKS5 server listening on vsock port 10.
  - Start a small TCP proxy that exposes that vsock service on `127.0.0.10:10` for local clients.
  - Create a TUN device `hostnet` (L3), assign `198.18.0.1/32`, bring it up, and add a default route via `hostnet`.
  - Start a UDP bridge that exchanges UDP packets with the host over vsock port 11 (length-prefixed rkyv-encoded frames).
  - Add nftables and `ip rule` entries to policy-route UDP (fwmark `0x64`) via table 100 (via interface `hostudp` created by the UDP injector).
  - Launch `tun2socks` to route TCP over the local SOCKS5 proxy (`socks5://127.0.0.10:10`), keeping the VM’s loopback a