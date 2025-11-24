# REP MOV based EPT detection

This is a basic POC of detecting EPT based hooking or access watch that verifies behaviour of the string instructions when they fault vs when they can fully execute un-interrupted. [@NickEverdox](https://x.com/nickeverdox/status/1981959428846084269) Decided to release a similar version of the concept, so I might as well release my version that I had come up with independently. The main difference is that I don't rely on on a hardware breakpoint, but rather make the instruction overwrite itself. Emulating this behaviour is also very annoying, because the amount of data copied varies greatly even on the same processor depending on the alignment of source/destination operands and the instruction itself. On machines with E-cores the behaviour can be different even with the same parameters.


```cpp
void check_ept(const void* address)
{
  constexpr uint8_t shellcode[] = {
    0xFC,                                     // 0:  cld
    0x48, 0x89, 0xCE,                         // 1:  mov    rsi,rcx
    0x48, 0x89, 0xD7,                         // 4:  mov    rdi,rdx
    0x44, 0x89, 0xC1,                         // 7:  mov    ecx, r8d
    0xF3, 0x48, 0xA5,                         // a:  rep movs QWORD PTR es:[rdi], QWORD PTR ds:[rsi]
    0xC3                                      // d:  ret
  };
  constexpr uint32_t offset_repmov = 0xA;

  const auto code = (char*)VirtualAlloc(nullptr, 0x2000, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
  const auto repmov_addr = code + 0x1020;
  const auto shellcode_addr = repmov_addr - offset_repmov;

  code[0] = 0;
  memcpy(shellcode_addr, shellcode, sizeof(shellcode));

  Sleep(100);

  __try
  {
    ((void(*)(const void* src, void* dst, uint32_t cnt))shellcode_addr)(address, code + 0xF00, 0x200 / 8);
  }
  __except(EXCEPTION_EXECUTE_HANDLER)
  {
  }

  // REP MOVS will overshoot the copy on every platform except when we're faulting every iteration of the instruction due to EPT.
  bool is_ok = repmov_addr[8] != 0;

  uint32_t overwrite_count = std::count_if(repmov_addr, repmov_addr + 0x100, [](unsigned char c) { return c != 0; });
  printf("OVERWRITES: %u %s\n", overwrite_count, is_ok ? "NOT DETECTED" : "DETECTED");

  VirtualFree(code, 0, MEM_RELEASE);
}
```
