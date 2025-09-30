# `tsidp` - Tailscale OpenID Connect (OIDC) Identity Provider

> [!CAUTION]
> This is an experimental update of tsidp. It is under active development and may experience breaking changes.

[![status: community project](https://img.shields.io/badge/status-community_project-blue)](https://tailscale.com/kb/1531/community-projects)

`tsidp` is an OIDC / OAuth Identity Provider (IdP) server that integrates with your Tailscale network. It allows you to use Tailscale identities for authentication into applications that support OpenID Connect as well as authenticated MCP client / server connections.

## Prerequisites

- A Tailscale network (tailnet) with magicDNS and HTTPS enabled
- A Tailscale authentication key from your tailnet
- (Recommended) Docker installed on your system
- Ability to set an Application capability grant

## Running tsidp

### (Recommended) Using the pre-built image

Docker images are automatically published on when releases are tagged.

```bash
# to use the latest image
$ docker pull ghcr.io/tailscale/tsidp:latest

# to use a specific release version
$ docker pull ghcr.io/tailscale/tsidp:v0.0.2
```

Running a tsidp container:

> [!TIP]
> Replace `YOUR_TAILSCALE_AUTHKEY` with your Tailscale authentication key in the following commands:
>
> Use an existing auth key or create a new auth key in the [Tailscale dashboard](https://login.tailscale.com/admin/settings/keys). Ensure you select an existing [tag](https://tailscale.com/kb/1068/tags) or create a new one.

```bash
# Run tsidp with a persistent volume to store state
docker run -d \
  --name tsidp \
  -p 443:443 \
  -v tsidp-data:/data \
  -e TAILSCALE_USE_WIP_CODE=1 \
  -e TS_STATE_DIR=/data \
  -e TS_HOSTNAME=idp \
  -e TSIDP_ENABLE_STS=1 \
  ghcr.io/tailscale/tsidp:latest
```

Visit `https://idp.yourtailnet.ts.net` to confirm the service is running.

> [!NOTE]
> If you're running tsidp for the first time it may take a few minutes for the TLS certificate to generate. You may not be able to access the service until the certificate is ready.

### Other Ways to Build and Run

<details>
<summary>Building your own container</summary>

```bash
$ make docker-image
```

</details>

<details>
<summary>Using Go directly</summary>

If you'd like to build tsidp and / or run it directly you can do the following:

```bash
# Clone the Tailscale repository
$ git clone https://github.com/tailscale/tsidp.git
$ cd tsidp

# run with default values for flags
$ TAILSCALE_USE_WIP_CODE=1 TS_AUTHKEY={YOUR_TAILSCALE_AUTHKEY} TSNET_FORCE_LOGIN=1 go run .
```

</details>

## Setting an Application Capability Grant

> [!IMPORTANT]
> Access to the admin UI and dynamic client registration endpoints are **denied** by default.

To access the admin UI and dynamic client registration endpoints an [Application capability grant](https://tailscale.com/kb/1537/grants-app-capabilities) must be set in the the [Tailscale console](https://login.tailscale.com/admin/acls/).

This is a permissive grant that is suitable for testing purposes:

```json
"grants": [
  {
    "src": ["*"],
    "dst": ["*"],
    "app": {
      "tailscale.com/cap/tsidp": [
        {
          // allow access to UI
          "allow_admin_ui": true,

          // allow dynamic client registration
          "allow_dcr": true,

          // Secure Token Service (STS) controls
          "users":     ["*"],
          "resources": ["*"],
        },
      ],
    },
  },
],
```

## tsidp Configuration Options

The `tsidp-server` is configured by several command-line flags:

| Flag                    | Description                                                                                        | Default  |
| ----------------------- | -------------------------------------------------------------------------------------------------- | -------- |
| `-dir <path>`           | Directory path to save tsnet and tsidp state. Recommend to be set.                                 | `""`     |
| `-hostname <hostname>`  | hostname on tailnet. Will become `<hostname>.your-tailnet.ts.net`                                  | `idp`    |
| `-port <port>`          | Port to listen on                                                                                  | `443`    |
| `-local-port <port>`    | Listen on `localhost:<port>`. Useful for testing                                                   | disabled |
| `-use-local-tailscaled` | Use local tailscaled instead of tsnet                                                              | `false`  |
| `-funnel`               | Use Tailscale Funnel to make tsidp available on the public internet so it works with SaaS products | disabled |
| `-enable-sts`           | Enable OAuth token exchange using RFC 8693                                                         | disabled |
| `-log <level>`          | Set logging level: `debug`, `info`, `warn`, `error`                                                | `info`   |
| `-debug-all-requests`   | For development. Prints all requests and respons