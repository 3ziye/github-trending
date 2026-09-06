# darwin-vm

Run iOS/ macOS in Qemu. Supports emulating iPhone 17, 16, 15, 14, 13, and 12
(A19-A14) and M5-M1 Macs (tested with Macbook Air and Mac Mini). You can debug
the kernel, edit the root filesystem, and run a root shell + custom programs.

Features:
- Runs a lightweight debuggable iOS/ macOS (Darwin) system with custom filesystem.
- Boots you directly into a root shell in just a few seconds.
- Compile and run your own programs as root in the VM, no jailbreak or kernel patches required.
- Runs anywhere qemu runs (ARM host not required).
- Supports emulating A19-A14 (iOS) and M5-M1 (macOS) CPUs.
- Supports SPTM based kernels and CPUs with MIE.
- Can debug / patch the kernel, SPTM, TXM, dyld, launchd, and userspace programs.
- Automated setup to get going in just a few minutes.

```
$ ./run.sh
Darwin Kernel Version 27.0.0: Tue Aug 11 22:05:33 PDT 2026; root:xnu-13432.1.9~3/RELEASE_ARM64_T8142
pmap_startup() init/release time: 893478 microsec
vm_page_bootstrap: 463555 free pages, 25917 wired pages
VM bootstrap: 73 maps, 256 entries and 64 nodes available
ptr-packing max: compressor:0x<ptr> page:0x<ptr> vmn:0xfffffeffffffff00 vme:0x<ptr>
zone_map_range: min:0x<ptr> max:0x0, vm-size:0x5cc000000 ro-size:0x29e000000, vm_min:0x<ptr> ro_min:0x<ptr>
vm: "vm_compressor_mode" is 4
VM bootstrap done: 71 maps, 224 entries and 59 nodes left
standard timeslicing quantum is 10000 us
standard background quantum is 2500 us
Long logs support configured: size: 16384
Firehose configured: 16 chunks, 8 io pages
Log queues configured: slot count: 90, per-slot size: 32768, total size: 2949120
OSLog stream configured: stream: 8192 bytes, cache: 2112 bytes
[trap_telemetry] trap_telemetry_init
mig_table_max_displ = 91 mach_kobj_count = 390
debug_log_init: Error!! gPanicBase is still not initialized
libTXM_KernelVersion: 12
libTXM_Image4Version: 1
TXM [Log]: setup logging: 32768 bytes (256 | 128)
TXM [Log]: system supports DIT feature
TXM [Log]: setup device tree range
TXM [Log]: unable to find esdm-fuses property in /chosen
TXM [Log]: resolved system platform identity: 0
TXM [Log]: Code Signing Monitor Image4 Module Version 7.0.0: Mon Aug 10 00:10:03 PDT 2026; root:AppleImage4_txm-374~7048/libima
...
Darwin Ignition Sequence Version 1.0.0: Tue Aug 11 21:44:28 PDT 2026; root:libignition-64~19270/libignition_core/RELEASE_ARM64E
libignition: 1: arguments           :
libignition: 1:   ignition level    : 0x5
libignition: 1:   force dylib root  : 0x0
libignition: 1:   halt after stage  : n/a
...
com.apple.xpc.launchd|1970-01-01 00:00:29.466851 <Notice>: Darwin Bootstrapper Version 7.0.0: Mon Aug 10 01:06:09 PDT 2026; root:libxpc_executables-3298.1.1~29/launchd/RELEASE_ARM64E
com.apple.xpc.launchd|1970-01-01 00:00:29.484709 <Notice>: boot-args = rd=md0 serial=3 -v -noprogress wdt=-1 wlan-olyhal-abort
com.apple.xpc.launchd|1970-01-01 00:00:29.486795 <Notice>: Restore environment starting.
com.apple.xpc.launchd|1970-01-01 00:00:29.487770 <Notice>: System Integrity Protection is engaged.
com.apple.xpc.launchd|1970-01-01 00:00:29.904447 (system/com.jprx.bash) <Notice>: internal event: WILL_SPAWN, code = 0
com.apple.xpc.launchd|1970-01-01 00:00:29.905070 (system/com.jprx.bash) <Notice>: service state: spawn scheduled
com.apple.xpc.launchd|1970-01-01 00:00:29.905166 (system/com.jprx.bash) <Notice>: service state: spawning
com.apple.xpc.launchd|1970-01-01 00:00:29.922055 (system/com.jprx.bash) <Notice>: launching: speculative
bash-3.2# uname -v
Darwin Kernel Version 27.0.0: Tue Aug 11 22:05:33 PDT 2026; root:xnu-13432.1.9~3/RELEASE_ARM64_T8142
bash-3.2# whoami
root
bash-3.2# ls
.fseventsd      mnt1            mnt3            mnt8            usr
System          mnt10           mnt4            mnt9            var
bin             mnt11           mnt5            private
dev             mnt12           mnt6            sbin
etc             mnt2            mnt7            tmp
```

(some kernel messages were removed from the above log to make it easier to read)

# What this is not

This is not a full iPhone/ Mac emulator. Don't expect the screen, wifi,
bluetooth, graphics, GUI apps, or full springboard to work. This just boots iOS
/ macOS to a barebones root shell so you can run custom command line programs,
debug the kernel, and mess around with low-level Darwin internals.

If you've ever compiled Linux + busybox and booted in qemu (with `-kernel` and
`-initrd`) for kernel development, this is like that but for Darwin systems.

# Tested Configurations

`darwin-vm` has been tested with the following systems:

| Device          | `devname`    | CPU name | iOS 27.0 beta 8 | iOS 26.6 |
|-----------------|--------------|----------|-----------------|----------|
| iPhone 17 (A19) | `iPhone18,3` | `t8150`  | ✅              | ✅       |
| iPhone 16 (A18) | `iPhone17,3` | `t8140`  | ✅              | ✅       |
| iPhone 15 (A16) | `iPhone15,4` | `t8120`  | ✅              | ✅       |
| iPhone 14 (A15) | `iPhone14,7` | `t8110`  | ✅              | ✅       |
| iPho