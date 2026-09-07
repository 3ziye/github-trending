![DLSS5 Feeder](dlss5-feeder-logo-dark.png)

[![AI-DECLARATION: copilot](https://img.shields.io/badge/䷼%20AI--DECLARATION-copilot-fee2e2?labelColor=fee2e2)](AI-DECLARATION.md)

> ## ⚠️ Read this before you install: it is usually the *combination*, not the game
>
> This project is a bridge between three things it does not control — **your NVIDIA driver**, the
> **NVIDIA NGX runtimes** (`nvngx_dlssnr.dll`, `nvngx_dlss.dll`) and a third-party **neural
> consumer** (`renodx-dlss5.addon64` or Deep Fried Chicken). Most reports here are not "game X does
> not work"; they are one of those three not getting on with another. The tables below are what has
> actually been measured, and what has not.
>
> **Check your own combination in about fifteen seconds, with no game running:**
> ```
> host64\dlss5-feed-host64.exe --test          (32-bit games; the helper is in host64\)
> ```
> `--test finished: 300/300 evaluates succeeded` means the driver, the runtimes and the consumer all
> work together. Anything less prints the fault and the module chain that produced it.
>
> ### 1. Driver × neural consumer
>
> Measured with `--test` on one RTX 5090, same files throughout, changing only the consumer —
> **through the 64-bit helper**, i.e. the 32-bit game path. A 64-bit game runs the consumer's detour
> in-process through the same code and is expected to behave the same, but has **not** been measured.
> **Blank cells are not claims** — they are combinations nobody has run.
>
> | neural consumer | driver **616.56** | driver **616.64** |
> |---|---|---|
> | *(none — DLAA only, no neural pass)* | — | ✅ 300/300 |
> | **Deep Fried Chicken** 1.4.8-alpha | — | ✅ 300/300 |
> | `renodx-dlss5` **v4.55** (classic engine) | — | ✅ 300/300 |
> | `renodx-dlss5` **"latest"** (classic engine) | — | ✅ 300/300 |
> | `renodx-dlss5` **v4.6** (lazy-adoption engine) | — | ❌ 1/300 |
> | `renodx-dlss5` **v4.7** (lazy-adoption engine) | ✅ 300/300 | ❌ 0/300 |
>
> **The one row measured on both drivers is v4.7, and it flips.** That is what pins the driver
> rather than the machine. One real-game log on **616.86** shows the same v4.7 failure, so it is not
> fixed there — but 616.86 has only that one data point. On 616.64+ the neural evaluate faults
> inside NVIDIA's own NGX runtime:
>
> ```
> evaluate raised 0xC0000005 in D3D12Core.dll
>     D3D12Core.dll <- nvngx_dlssnr.dll <- _nvngx.dll <- renodx-dlss5.addon64 <- dlss5-feed-host64.exe
> ```
>
> Nothing on this side is in that chain past the call itself. 616.64 also changed what NGX answers
> about the feature that path creates (`NotImplemented` on 616.56 → `supported` on 616.64), so the
> driver moved and the v4.6+ engine did not survive it. **Any one of these works:** Deep Fried
> Chicken, a classic-engine `renodx-dlss5` build, or driver 616.56. See
> [#54](https://github.com/jlrouzies-fr/DLSS5-Feeder/issues/54).
>
> ### 2. The NGX runtimes
>
> | file | what it is | builds seen in reports |
> |---|---|---|
> | `nvngx_dlssnr.dll` | the neural-rendering model — **DLSS 5 cannot run without it** | NVIDIA `310.8.0.0`, NVIDIA `310.8.2.0`, ShortFuse repack `310.8.SF.0` |
> | `nvngx_dlss.dll` | the DLSS super-resolution runtime | `310.8.0.0`, `310.9.0.0`, and older DLSS **v3** builds such as `3.8.10.0` |
>
> **Telling NVIDIA's build from ShortFuse's repack:** not by the version number and not by
> `OriginalFilename` — both report `310.8.0.0` and both carry `CL 38718415`. The field that differs
> is the *stated* **FileVersion** string: `310,8,0,0` (NVIDIA) versus `310.8.SF.0` (ShortFuse).
> 0.14.0-beta.2 logs it, and `Verify-DLSS5Feeder.ps1` prints it.
>
> **The `.SF` repack is not known to break anything.** It was the leading hypothesis in
> [#47](https://github.com/jlrouzies-fr/DLSS5-Feeder/issues/47) and was then eliminated by
> counter-example. Do not swap runtimes on the strength of that thread alone.
>
> A `3.x` `nvngx_dlss.dll` beside a `310.x` `nvngx_dlssnr.dll` has been seen in reports. Whether the
> mismatch matters is **unknown** — no test has isolated it. If yours are mismatched, it is worth
> mentioning when you report.
>
> ### 3. Known-open, and not caused by your install
>
> | symptom | where | status |
> |---|---|---|
> | `NVSDK_NGX_D3D12_Init -> 0xBAD00001` on a 64-bit game, while the same files succeed for 32-bit games | [#47](https://github.com/jlrouzies-fr/DLSS5-Feeder/issues/47) | Open, **per-game**. GPU architecture, driver, data path, adapter, model build and game provenance have each been eliminated by counter-example. |
> | Works for minutes, then the neural pass stops; log says `device removed … 0x887A0006` | [#57](https://github.com/jlrouzies-fr/DLSS5-Feeder/issues/57) | Open. A GPU hang; 0.14.0-beta.2 arms the D3D12 breadcrumb recorder on the D3D11 path, which was missing. |
> | Severe flicker or a frozen image on 64-bit **Vulkan** | [#13](https://github.com/jlrouzies-fr/DLSS5-Feeder/issues/13) | Open. Narrowed: the transport is clean, the depth guide reaching NGX is a constant. |
>
> 