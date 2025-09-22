### CreateProcessAsPPL

If you want to run a program with PPL protection enabled, then this tool will help you do that.

### Command Line Syntax

**CreateProcessAsPPL.exe Mode:0-4 path_to_exe arg0 arg1 ...**

**Mode:**

* PROTECTION_LEVEL_WINTCB_LIGHT       0
* PROTECTION_LEVEL_WINDOWS            1
* PROTECTION_LEVEL_WINDOWS_LIGHT      2
* PROTECTION_LEVEL_ANTIMALWARE_LIGHT  3
* PROTECTION_LEVEL_LSA_LIGHT          4

## Links

[An article about exploiting the PPL program to destroy Windows Defender](https://www.zerosalarium.com/2025/08/countering-edrs-with-backing-of-ppl-protection.html)

[WSASS - Tool to dump the LSASS process on modern Windows 11](https://github.com/TwoSevenOneT/WSASS)

[An article about exploiting WerFaultSecure.exe to dump LSASS](https://www.zerosalarium.com/2025/09/Dumping-LSASS-With-WER-On-Modern-Windows-11.html)

## Author:

[Two Seven One Three](https://x.com/TwoSevenOneT)
