# AuditKit - Multi-Cloud Compliance Scanner & Evidence Collection

**Open-source compliance scanner for AWS and Azure with auditor-ready evidence collection guides.**

[![GitHub stars](https://img.shields.io/github/stars/guardian-nexus/auditkit)](https://github.com/guardian-nexus/auditkit/stargazers)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![Version](https://img.shields.io/badge/version-v0.6.0-green)
[![Newsletter](https://img.shields.io/badge/Newsletter-Subscribe-orange)](https://auditkit.substack.com)

## What AuditKit Does

AuditKit scans your cloud infrastructure against SOC2, PCI-DSS, and CMMC controls and provides:

1. **Multi-Cloud Support** - AWS (production), Azure (v0.5.0) 
2. **Clear Pass/Fail Status** - 64 SOC2 controls, 30 PCI-DSS controls, 17 CMMC Level 1 controls
3. **Exact Fix Commands** - Cloud-specific CLI commands for remediation
4. **Evidence Collection Guides** - Step-by-step screenshots auditors accept
5. **Priority-Based Fixes** - Critical issues that will fail your audit vs. nice-to-haves

## Quick Start

### AWS
```bash
# Configure AWS credentials
aws configure

# Run SOC2 scan
auditkit scan -provider aws -framework soc2

# Run CMMC Level 1 scan (DoD contractors)
auditkit scan -provider aws -framework cmmc

# Generate PDF report
auditkit scan -provider aws -framework soc2 -format pdf -output aws-soc2.pdf
```

### Azure (v0.5.0)
```bash
# Configure Azure credentials
az login
export AZURE_SUBSCRIPTION_ID="your-subscription-id"

# Run SOC2 scan
auditkit scan -provider azure -framework soc2

# Run CMMC Level 1 scan
auditkit scan -provider azure -framework cmmc

# Generate PCI-DSS report
auditkit scan -provider azure -framework pci -format pdf -output azure-pci.pdf
```

## Recent Updates

**v0.6.0 (Sept 2025)** - CMMC Level 1 support with November 10, 2025 deadline tracking + CMMC Level 2 Pro available  
**v0.5.0 (Sept 2025)** - Azure provider support with full SOC2/PCI-DSS implementation  
**v0.4.1 (Sept 2025)** - Complete SOC2 implementation (all 64 Common Criteria)  
**v0.4.0 (Sept 2025)** - Multi-framework support with PCI-DSS v4.0  
**v0.3.0 (Sept 2025)** - Evidence collection guides based on Reddit feedback

## Current Implementation Status

### Cloud Providers
| Provider | Files | Checks | Status | Authentication |
|----------|-------|--------|--------|----------------|
| **AWS** | 17 check files | ~150 checks | ✅ Production | AWS CLI, IAM roles |
| **Azure** | 12 check files | ~110 checks | ✅ Production | CLI, Service Principal, Managed Identity |
| **GCP** | Not started | 0 | 🚧 Planned v0.7.0 | - |

### Framework Coverage
| Framework | AWS Controls | Azure Controls | Status |
|-----------|--------------|----------------|--------|
| **SOC2** | 64 (CC1-CC9) | 64 (CC1-CC9) | ✅ Production Ready |
| **PCI-DSS v4.0** | 30 technical | 30 technical | ✅ Production Ready |
| **CMMC Level 1** | 17 practices | 17 practices | ✅ Production Ready |
| **CMMC Level 2** | 110 practices (Pro) | 110 practices (Pro) | 🔥 Pro Feature - [AuditKit Pro](https://auditkit.io/pro/) or e-mail hello@auditkit.io |
| **HIPAA** | ~10 mapped | ~10 mapped | 🧪 Experimental Only |
| **ISO 27001** | ~5 mapped | ~5 mapped | 🧪 Experimental Only |

### CMMC Compliance (NEW in v0.6.0)
- **CMMC Level 1**: 17 foundational practices for Federal Contract Information (FCI)
- **Deadline**: November 10, 2025 - All DoD contracts will require CMMC compliance
- **Coverage**: Both AWS and Azure providers support complete Level 1 assessment
- **Evidence**: Screenshot guides for all 17 practices with exact Azure Portal/AWS Console URLs

### Azure Services Covered (v0.5.0+)
- **Azure AD (Entra ID)**: MFA, privileged roles, guest access, password policies
- **Full SOC2 Implementation**: All 64 Common Criteria controls (CC1-CC9)
- **CMMC Implementation**: All 17 Level 1 practices with DoD deadline tracking
- **Storage Accounts**: Public access, encryption, secure transfer, access keys
- **Virtual Machines**: Disk encryption, managed disks, security extensions
- **Network Security Groups**: Open ports, dangerous rules, flow logs
- **Key Vault**: Soft delete, purge protection, access policies
- **Activity Logs**: Retention, log profiles, diagnostic settings
- **Azure SQL**: Transparent encryption, auditing, firewall rules
- **Managed Identities**: System vs user-assigned configuration

## What Makes AuditKit Different

### 1. Evidence Collection That Auditors Accept

```yaml
Control Failed: CC6.2 - Public S3 Bucket
Fix Command: aws s3api put-public-access-block --bucket my-bucket --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"

Evidence Required:
1. Navigate to: https://s3.console.aws.amazon.com/s3/buckets/my-bucket
2. Click "Permissions" tab
3. Screenshot showing all 4 "Block public access" settings = ON
4. Save as: SOC2_CC6.2_S3_Public_Access.png
```

## What's New in v0.6.0

### C