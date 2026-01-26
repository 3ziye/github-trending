# libbbf: Bound Book Format 

![alt text](https://img.shields.io/badge/Format-BBF1-blue.svg)
![alt text](https://img.shields.io/badge/License-MIT-green.svg)

> [!WARNING]
> **Official Source Notice: Please only download releases from this repository (ef1500/libbbf). External mirrors or forks may contain malware.**

Bound Book Format (.bbf) is a high-performance binary container designed specifically for digital comic books and manga. Unlike CBR/CBZ, BBF is built for DirectStorage/mmap, easy integrity checks, and mixed-codec containerization.

---

## Getting Started

### Prerequisites
- C++17 compliant compiler (GCC/Clang/MSVC), and optionally CMake
- [xxHash](https://github.com/Cyan4973/xxHash) library

### Compilation

#### CMake

```bash
cmake -B build
cmake --build build
sudo cmake --install build
```

#### Manual

Linux
```bash
g++ -std=c++17 bbfenc.cpp libbbf.cpp xxhash.c -o bbfmux -pthread
```

Windows
```bash
g++ -std=c++17 bbfenc.cpp libbbf.cpp xxhash.c -o bbfmux -municode
```

Alternatively, if you need python support, use [libbbf-python](https://github.com/ef1500/libbbf-python). 

---

## Technical Details

BBF is designed as a Footer-indexed binary format. This allows for rapid append-only creation and immediate random access to any page without scanning the entire file.

### MMAP Compatibility
The `bbfmux` reference implementation utilizes **Memory Mapping (mmap/MapViewOfFile)**. Instead of reading file data into intermediate buffers, the tool maps the container directly into the process address space. This allows the CPU to access image data at the speed of your NVMe drive's hardware limit.

### High-Speed Parallel Verification
Integrity checks utilize **Parallel XXH3**. On multi-core systems, the verifier splits the asset table into chunks and validates multiple pages simultaneously. This makes BBF verification up to **10x faster** than ZIP/RAR CRC checks.

### 4KB Alignment
Every asset in a BBF file starts on a **4096-byte boundary**. This alignment is critical for modern hardware, allowing for DirectStorage transfers directly from disk to GPU memory, bypassing CPU bottlenecks entirely.

Note: DirectStorage isn't avaliable for images yet (as far as I know), but I've made sure to accomodate such a thing in the future with this format.

### Binary Layout
1. **Header (13 bytes)**: Magic `BBF1`, versioning, and initial padding.
2. **Page Data**: The raw image payloads (AVIF, PNG, etc.), each padded to **4096-byte boundaries**.
4. **String Pool**: A deduplicated pool of null-terminated strings for metadata and section titles.
5. **Asset Table**: A registry of physical data blobs with XXH3 hashes.
6. **Page Table**: The logical reading order, mapping logical pages to assets.
7. **Section Table**: Markers for chapters, volumes, or gallery sections.
8. **Metadata Table**: Key-Value pairs for archival data (Author, Scanlation team, etc.).
9. **Footer (76 bytes)**: Table offsets and a final integrity hash.

NOTE: `libbbf.h` includes a `flags` field, as well as extra padding for each asset entry. This is so that in the future `libbbf` can accomodate future technical advancements in both readers and image storage. I.E. If images support DirectStorage in the future, then BBF will be able to use it.

### Feature Comparison: Digital Comic & Archival Formats

| Feature | **BBF** | CBZ (Zip) | CBR (Rar) | PDF | EPUB | Folder |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Random Page Access** | ✅ | ✅[8] | ✅[8] | ✅ | ❌ | ✅ |
| **Native Data Deduplication** | ✅ | ❌ | ❌ | ⚠️ [1] | ❌ | ❌ |
| **Per-Asset Integrity (XXH3)** | ✅ | ⚠️[9] | ⚠️[9] | ❌ | ❌ | ❌ |
| **4KB Sector Alignment** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Native Sections/Chapters** | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ |
| **Arbitrary Metadata (UTF-8)** | ✅ | ⚠️ [2] | ❌ | ✅ | ✅ | ❌ |
| **Mixed-Codec Support** | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| **DirectStorage/mmap Ready** | ✅ | ❌ | ❌ | ❌ | ❌ | ⚠️ [3] |
| **Low Parser Complexity** | ✅ | ⚠️ [4] | ❌ | ❌ | ❌ | ✅ |
| **Bit-Rot Detection** | ✅ | ⚠️ [5] | ⚠️ [5] | ❌ | ❌ | ❌ |
| **Streaming-Friendly Index** | ⚠️ [6] | ⚠️ [6] | ❌ | ✅ [7] | ⚠️ | ❌ |
| **Wide Software Support** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

<font size="2">
[1] - PDF supports XObjects to reuse resources, but lacks native content-hash deduplication; identical images must be manually referenced.<br/>
[2] - CBZ does not support metadata natively in the ZIP spec; it relies on unofficial sidecar files like <code>ComicInfo.xml</code>.<br/>
[3] - While folders allow memory mapping, individual images within them are rarely sector-aligned for optimized DirectStorage throughput.<br/>
[4] - ZIP/RAR require large, complex libraries (zlib/libarchive); BBF is a "Plain Old Data" (POD) format requiring only a few lines of C++ to parse.<br/>
[5] - ZIP/RAR use CRC32, which is aging, collision-prone, and significantly slower to verify than XXH3 for large archival collections. See [8].<br/>
[6] - Because the index is at the end (Footer), web-based streaming requires a "Range Requ