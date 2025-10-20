### EDR-Freeze

This is a tool that exploits the software vulnerability of WerFaultSecure to suspend the processes of EDRs and antimalware without needing to use the BYOVD (Bring Your Own Vulnerable Driver) attack method.

EDR-Freeze operates in user mode, so you don't need to install any additional drivers. It can run on the latest version of Windows.

*The experiment was conducted with the latest version of Windows at the time of the project creation: __Windows 11 24H2__*

### Command Line Syntax

**EDR-Freeze.exe [TargetPID] [SleepTime]**

*Example: __EDR-Freeze.exe 1234 10000__*

*Freeze the target for 10000 milliseconds*

## Links

[EDR-Freeze: A Tool That Puts EDRs And Antivirus Into A Coma State](https://www.zerosalarium.com/2025/09/EDR-Freeze-Puts-EDRs-Antivirus-Into-Coma.html)

[Tool to run process with PPL without driver](https://github.com/TwoSevenOneT/CreateProcessAsPPL)

## How to Use EDR-Freeze Effectively

Instead of running EDR-Freeze with a long sleep duration, you should incorporate it into a script with the following steps:

1. Temporarily halt all Antimalware/EDR processes for a short period (1-3 seconds).
2. Execute tasks immediately after a successful suspension.

Since the GUI may become unresponsive in some cases, you should choose the shortest sleep time possible. Just make sure that the script executions are completed before the Antimalware/EDR resumes.

Alternatively, it's best to insert the code you want to execute directly into the source code of EDR-Freeze:

<img width="748" height="387" alt="Insert code" src="https://github.com/user-attachments/assets/1c6f8819-5a21-4cc4-b72f-ea00be0fd092" />


## Author:

[Two Seven One Three](https://x.com/TwoSevenOneT)
