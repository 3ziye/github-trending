<h3 align="center">When HTTP gets complicated...</h3>
<p align="center">
  <img src="other/assets/saul-logo (1).png" width="600"/>
</p>

<p align="center">
  <a href="https://github.com/DeprecatedLuar/better-curl-saul/stargazers">
    <img src="https://img.shields.io/github/stars/DeprecatedLuar/better-curl-saul?style=for-the-badge&logo=github&color=1f6feb&logoColor=white&labelColor=black"/>
  </a>
  <a href="https://github.com/DeprecatedLuar/better-curl-saul/releases">
    <img src="https://img.shields.io/github/v/release/DeprecatedLuar/better-curl-saul?style=for-the-badge&logo=go&color=00ADD8&logoColor=white&labelColor=black"/>
  </a>
  <a href="https://github.com/DeprecatedLuar/homebrew-tap">
    <img src="https://img.shields.io/badge/Homebrew-tap-FBB040?style=for-the-badge&logo=homebrew&logoColor=white&labelColor=black"/>
  </a>
  <a href="/nix-saul">
    <img src="https://img.shields.io/badge/Nix-flake-5277C3?style=for-the-badge&logo=nixos&logoColor=white&labelColor=black"/>
  </a>
  <a href="https://github.com/DeprecatedLuar/better-curl-saul/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/DeprecatedLuar/better-curl-saul?style=for-the-badge&color=green&labelColor=black"/>
  </a>
</p>

**v0.3.0 Try out the new curl import/exporting**: `saul myapi set --raw` and `saul myapi get --raw` 

---


<p align="center">
  <img src="other/assets/saul-catboy-final.png" width="700"/>
</p>

<p align="center"> Better Curl Saul is a way to simplify and organize api re-callability (if that's a word)</p>
 
 ---

## **In a nutshell,** this is... not my favorite UX:
```bash
curl -X POST "https://company.atlassian.net/rest/api/3/issue" \
  -H "Authorization: Basic $(echo -n 'user@company.com:api-token-here' | base64)" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "X-Atlassian-Token: no-check" \
  -d '{
    "fields": {
      "project": {"key": "PROJ"},
      "summary": "API Bug: Users can'\''t login after deployment",
      "description": "Steps:\n1. Deploy v2.1.0\n2. Try login\n3. Gets 500 error\n\nExpected: Login works\nActual: Server error",
      "issuetype": {"name": "Bug"},
      "priority": {"name": "High"},
      "assignee": {"accountId": "123456:abcd-efgh-ijkl"},
      "labels": ["api", "login", "production"],
      "customfield_10001": "2024-01-15",
      "customfield_10002": {"value": "Backend Team"}
    }
  }'
```

# Try this instead
<p align="center">
  <img src="other/assets/demo.gif" alt="Better-Curl Demo" width="800"/>
</p>

---

## The nice features you've never seen before

- **Workspace-based** - Each API gets its own organized folder (reusable)
- **Inline editor** - the `edit` command for any given field also supports `$EDITOR`
- **Smart variables** - `{@token}` persists,`{?name}` prompts every time
- **Response filtering** - Show only the fields you care about
- **Git-friendly** - Store the preset workspaces on git
- **Unix composable** - Script it, pipe it, shell it
- **TOML converter** - JSON gets reorganized into TOML for readability
- **Saul Goodman** - It has Saul Goodman on it.
  
<img src="other/assets/saul-hd-wide.png" width="1000"/>


# Installation

![macOS](https://img.shields.io/badge/macOS-black?style=flat-square&logo=apple&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black) ![Windows](https://img.shields.io/badge/Windows-0078D4?style=flat-square&logo=windows11&logoColor=white) ![Nix](https://img.shields.io/badge/Nix-5277C3?style=flat-square&logo=nixos&logoColor=white)

### Universal
```bash
curl -sSL https://raw.githubusercontent.com/DeprecatedLuar/better-curl-saul/main/install.sh | bash
```

### Homebrew
```bash
brew install deprecatedluar/tap/better-curl-saul
```

### NixOS
```bash
nix profile install github:DeprecatedLuar/better-curl-saul?dir=nix-saul
```

<details>
<summary>Other Install Methods</summary>

<br>

**Manual Install**
1. Download binary for your OS from [releases](https://github.com/DeprecatedLuar/better-curl-saul/releases)
2. Make executable: `chmod +x saul-*`
3. Move to PATH: `sudo mv saul-* /usr/local/bin/saul`

---

**From Source** (for try-harders)
```bash
git clone https://github.com/DeprecatedLuar/better-curl-saul.git
cd better-curl-saul
./other/install-local.sh  # Local development build
```

---

**In case you already have Saul** (basically gambling at this point)
```bash
saul temp set url https://raw.githubusercontent.com/DeprecatedLuar/better-curl-saul/main/install.sh && saul temp call --raw | bash
```

>[!NOTE]
> Quick install auto-detects your system and downloads binaries or builds from source as fallback.
> Windows users: I don't know powershell I expect you to have bash 👍

</details>

<br>

---

## Commands

| Action | Targets                                                            | Description                              | Example                                    |
|--------|----------------------------------------------------------