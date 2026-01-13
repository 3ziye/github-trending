# Tailsnitch

A security auditor for Tailscale configurations. Tailsnitch scans your tailnet for 50+ misconfigurations, overly permissive access controls, and security best practice violations.

## Quick Start

```bash
# 1. Set your Tailscale API credentials
export TSKEY="tskey-api-..."

# 2. Run audit
tailsnitch

# 3. See only high-severity findings
tailsnitch --severity high

# 4. Fix some issues  ~interactively~ yolo mode
tailsnitch --fix
```

## Installation

### Download Pre-built Binary

Download the latest release from [GitHub Releases](https://github.com/Adversis/tailsnitch/releases).

**macOS users:** Remove quarantine attribute after download:
```bash
sudo xattr -rd com.apple.quarantine tailsnitch
```

### Install via Go

```bash
go install github.com/Adversis/tailsnitch@latest
```

### Build from Source

```bash
git clone https://github.com/Adversis/tailsnitch.git
cd tailsnitch
go build -o tailsnitch .
```

## Authentication

Tailsnitch supports two authentication methods. OAuth is preferred when both are configured.

### Option 1: OAuth Client (Recommended)

OAuth clients provide scoped, auditable access that doesn't expire when employees leave.

```bash
export TS_OAUTH_CLIENT_ID="..."
export TS_OAUTH_CLIENT_SECRET="tskey-client-..."
```

Create an OAuth client at: https://login.tailscale.com/admin/settings/oauth

**Required scopes for read-only audit:**
- `all:read` (simplest), or individually:
- `policy_file:read` - ACL policy
- `devices:core:read` - Device list
- `dns:read` - DNS configuration
- `auth_keys:read` - Auth keys (for AUTH checks)

**Additional scopes for fix mode:**
- `devices:core` - Delete devices, modify tags (requires tag selection)
- `auth_keys` - Delete auth keys

### Option 2: API Key

API keys operate as the user who created them and inherit that user's permissions.

```bash
export TSKEY="tskey-api-..."
```

Create an API key at: https://login.tailscale.com/admin/settings/keys

## Usage Examples

### Basic Audit

```bash
# Run full audit
tailsnitch

# Show passing checks too (verbose)
tailsnitch --verbose

# Output as JSON for processing
tailsnitch --json

# Audit a specific tailnet (when OAuth client has access to multiple)
tailsnitch --tailnet mycompany.com
```

### Filter Results

```bash
# Only show critical and high severity issues
tailsnitch --severity high

# Filter by category
tailsnitch --category access    # ACL issues
tailsnitch --category auth      # Authentication & keys
tailsnitch --category device    # Device security
tailsnitch --category network   # Network exposure
tailsnitch --category ssh       # SSH rules
tailsnitch --category log       # Logging & admin

# Run specific checks only
tailsnitch --checks ACL-001,AUTH-001,DEV-010
tailsnitch --checks stale-devices,tailnet-lock-not-enabled

# List all available checks
tailsnitch --list-checks
```

### Interactive Fix Mode

Fix mode allows you to remediate issues directly via the Tailscale API:

```bash
# Interactive fix mode
tailsnitch --fix

# Preview what would be fixed (dry run)
tailsnitch --fix --dry-run

# Auto-select safe fixes (still requires confirmation)
tailsnitch --fix --auto

# Disable audit logging of fix actions
tailsnitch --fix --no-audit-log
```

**API-fixable items:**

| Check | Action |
|-------|--------|
| AUTH-001, AUTH-002, AUTH-003 | Delete auth keys |
| AUTH-004 | Replace with ephemeral keys |
| DEV-002 | Remove tags from user devices |
| DEV-004 | Delete stale devices |
| DEV-005 | Authorize pending devices |

Fix mode also provides direct links to the admin console for issues that require manual intervention.

### SOC 2 Evidence Export

Generate evidence reports for SOC 2 audits with Common Criteria (CC) control mappings:

```bash
# Export as JSON
tailsnitch --soc2 json > soc2-evidence.json

# Export as CSV (for spreadsheets)
tailsnitch --soc2 csv > soc2-evidence.csv
```

The SOC 2 report includes:
- Per-resource test results (each device, key, ACL rule tested individually)
- CC code mappings (CC6.1, CC6.2, CC6.3, CC6.6, CC7.1, CC7.2, etc.)
- Pass/Fail/N/A status for each control test
- Timestamp for audit trail

**Example CSV output:**
```csv
resource_type,resource_id,resource_name,check_id,check_title,cc_codes,status,details,tested_at
device,node123,prod-server,DEV-001,Tagged devices with key expiry disabled,CC6.1;CC6.3,PASS,Tags: [tag:server] key expiry enabled,2025-01-05T10:30:00Z
key,tskey-auth-xxx,tskey-auth-xxx,AUTH-001,Reusable auth keys exist,CC6.1;CC6.2;CC6.3,FAIL,Reusable key expires in 45 days,2025-01-05T10:30:00Z
```

### Ignore Known Risks

Create a `.tailsnitch-ignore` file to suppress findings for known-accepted risks:

```bash
# .tailsnitch-ignore
# Ignore informational checks
ACL-008  # We intentionally don't use groups
ACL-009  # Legacy ACLs are fine for our use case

# Ignore specific medium checks with justification
DEV-006  # External devices are approved contractors
LOG-001  # Flow logs require Enterprise plan
```

**Ignore file locations (checked in order):**
