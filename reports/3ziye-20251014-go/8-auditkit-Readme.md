# AuditKit - Open-Source Compliance Scanner

**Scan AWS, Azure, and M365 for SOC2, PCI-DSS, HIPAA, and CMMC compliance. Get audit-ready reports in minutes.**

[![GitHub stars](https://img.shields.io/github/stars/guardian-nexus/auditkit)](https://github.com/guardian-nexus/auditkit/stargazers)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Version](https://img.shields.io/badge/version-v0.6.6-green.svg)](https://github.com/guardian-nexus/auditkit/releases)
[![Newsletter](https://img.shields.io/badge/Newsletter-Subscribe-orange)](https://auditkit.substack.com)
---

## Quick Start

```bash
# Install
git clone https://github.com/guardian-nexus/auditkit
cd auditkit/scanner
go build ./cmd/auditkit

# Scan AWS for SOC2
aws configure
./auditkit scan -provider aws -framework soc2

# Generate PDF report
./auditkit scan -provider aws -framework soc2 -format pdf -output report.pdf
```

**That's it.** You'll get a compliance score and list of what needs fixing.

---

## What It Does

AuditKit automates the **technical controls** for compliance audits:

- Scans your cloud infrastructure (AWS, Azure, M365)
- Checks ~150 automated controls per framework
- Shows exact CLI commands to fix issues
- Generates PDF/HTML reports auditors understand
- Tracks your progress over time

**What it doesn't do:** Replace your auditor, scan for vulnerabilities, or handle organizational policies.

---

## Examples and Sample Reports

### Terminal Output

Here's what you see when running AuditKit against your cloud environment:

![Terminal Scan Output](./docs/examples/screenshots/azure-cmmc-scan-console-output-sample.png)

### HTML Report Preview

Interactive HTML reports with compliance scores, automated vs manual check breakdowns, and evidence collection guides:

![HTML Report - Compliance Score](./docs/examples/screenshots/html-report-score.png)

![HTML Report - Disclaimer](./docs/examples/screenshots/html-report-disclaimer.png)

![HTML Report - Evidence Guide](./docs/examples/screenshots/html-report-evidence.png)

### Available Sample Reports

**AWS Compliance Reports:**
- [AWS SOC2 Report (PDF)](./docs/examples/reports/sample-aws-soc2-report.pdf)
- [AWS SOC2 Report (HTML)](https://guardian-nexus.github.io/auditkit/examples/reports/sample-aws-soc2-report.html)
- [AWS PCI-DSS Report (PDF)](./docs/examples/reports/sample-aws-pci-report.pdf)
- [AWS CMMC Report (PDF)](./docs/examples/reports/sample-aws-cmmc-report.pdf)

**Azure Compliance Reports:**
- [Azure CMMC Report (PDF)](./docs/examples/reports/sample-azure-cmmc-report.pdf)
- [Azure CMMC Report (HTML)](https://guardian-nexus.github.io/auditkit/examples/reports/sample-azure-cmmc-report.html)

[View all examples](./docs/examples/)

---

## Supported Frameworks

| Framework | AWS | Azure | M365 | Status |
|-----------|-----|-------|------|--------|
| **SOC2** | 64 controls | 64 controls | 100+ rules | Production |
| **PCI-DSS v4.0** | 30 controls | 30 controls | Mapped | Production |
| **CMMC Level 1** | 17 practices | 17 practices | Mapped | Production |
| **HIPAA** | ~10 controls | ~10 controls | Basic | Experimental |
| **CMMC Level 2** | 110 practices | 110 practices | Mapped | [Pro Only](https://auditkit.io/pro) |

---

## Why Use AuditKit?

### For Startups
- Free SOC2 preparation without consultants
- Audit-ready PDF reports for your CPA firm
- Most technical issues fixed in hours

### For DoD Contractors
- CMMC Level 1 assessment (17 practices)
- November 10, 2025 deadline compliance
- Self-assessment before C3PAO review

### For Enterprises
- Single tool for AWS, Azure, and M365
- Track compliance improvement over time
- Replace multiple expensive tools

---

## Installation

### Download Binary
See [Releases](https://github.com/guardian-nexus/auditkit/releases) for pre-built binaries.

### From Source
```bash
git clone https://github.com/guardian-nexus/auditkit
cd auditkit/scanner
go build ./cmd/auditkit
./auditkit scan
```

### Using Go
```bash
go install github.com/guardian-nexus/auditkit/scanner/cmd/auditkit@latest
```

**Requirements:**
- Go 1.19+
- Cloud credentials configured (AWS CLI, Azure CLI, or M365 via ScubaGear)
- Read-only permissions to cloud resources

---

## Examples

### Basic Scanning

```bash
# SOC2 scan
auditkit scan -provider aws -framework soc2

# PCI-DSS scan
auditkit scan -provider azure -framework pci

# CMMC Level 1 scan
auditkit scan -provider aws -framework cmmc

# See all controls (no truncation)
auditkit scan -provider aws -framework soc2 --full
```

### Generate Reports

```bash
# PDF report for auditors
auditkit scan -format pdf -output report.pdf

# Interactive HTML report
auditkit scan -format html -output report.html

# JSON output for automation
auditkit scan -format json -output results.json
```

### M365 Integration

```bash
# Step 1: Run ScubaGear (Windows PowerShell)
Install-Module -Name ScubaGear
Invoke-SCuBA -ProductNames aad,exo,sharepoint,teams -OutPath ./ScubaResu