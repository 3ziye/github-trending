<h1 align="center">Resterm</h1>

<p align="center">
  <em>a terminal-based REST client.</em>
</p>

<p align="center">
  <img src="_media/resterm.png" alt="Screenshot of resterm TUI" width="720" />
</p>

## Features
- **Workspace explorer.** Filters `.http`/`.rest` files, respects workspace roots, and keeps the file pane navigable with incremental search.
- **Editor with modal workflow.** Starts in view mode, supports Vim-style motions, visual selections with inline highlighting, clipboard yank/cut, `Shift+F` search, and an `i` / `Esc` toggle for insert mode.
- **Inline requests.** Type `https://api.example.com` or `GET https://api.example.com` directly in the editor and press `Ctrl+Enter` - no `.http`/`.rest` file required.
- **Curl command parsing (limited).** supports basic `curl` invocations (method, headers, data flags) - more in the road-map.
- **Status-aware response pane.** Pill-style header calls out workspace, environment, active request, and script/test outcomes; response tabs cover Pretty, Raw, Headers, and History, plus request previews.
- **Split response views with diffing.** Snap responses into vertical or horizontal splits, pin panes, and compare Pretty/Raw/Headers tabs side-by-side with a unified diff view.
- **Auth & variable helpers.** `@auth` directives cover basic, bearer, API key, and custom headers; variable resolution spans request, file, environment, and OS layers with helpers like `{{$timestamp}}` and `{{$uuid}}`.
- **Pre-request & test scripting.** JavaScript (goja) hooks mutate outgoing requests, assert on responses, and surface pass/fail summaries inline.
- **GraphQL tooling.** `@graphql` and `@variables` directives produce proper payloads, attach operation names, and keep previews/history readable.
- **gRPC client.** `GRPC host:port` requests with `@grpc` metadata build messages from descriptor sets or reflection, stream metadata/trailers, and log history entries beside HTTP calls.
- **Session persistence.** Cookie jar, history store, and environment-aware entries survive restarts; `@no-log` can redact bodies.
- **Configurable transport.** Flag-driven timeout, TLS, redirect, and proxy settings alongside environment file discovery (`resterm.env.json` or legacy `rest-client.env.json`).

> [!WARNING]
> Resterm is still in early stages so bugs and undesired behaviors can be expected.

## Request File Structure

Resterm reads plain-text `.http`/`.rest` files. Each request follows the same conventions so the editor, parser, and history can reason about it consistently.

```http
### get user
# @name getUser
# @description Fetch a user profile
GET https://{{baseUrl}}/users/{{userId}}
Authorization: Bearer {{token}}
X-Debug: {{$timestamp}}

{
  "verbose": true
}

### create user
POST https://{{baseUrl}}/users
Content-Type: application/json

< ./payloads/create-user.json
```

- **Request separators.** Start a new request with a line beginning `###` (an optional label after the hashes is ignored by the parser but is handy for readability).
- **Metadata directives.** Comment lines (`#` or `//`) before the request line can include directives such as `@name`, `@description`, `@tag`, `@auth`, `@graphql`, `@grpc`, `@variables`, and `@script`. See [Request Metadata & Settings](#request-metadata--settings) for the full list.
- **Request line.** The first non-comment line specifies the verb and target. HTTP calls use `<METHOD> <URL>`, whereas gRPC calls begin with `GRPC host:port` followed by `@grpc package.Service/Method` metadata.
- **Headers.** Subsequent lines of the form `Header-Name: value` are sent verbatim after variable substitution.
- **Body.** A blank line separates headers from the body. You can inline JSON/text, use heredoc-style scripts, or include external files with `< ./path/to/file`.
- **Inline variables.** Placeholders like `{{userId}}` or `{{token}}` are resolved using the variable stack (request variables, file-level variables, selected environment, then OS environment). Helpers such as `{{$uuid}}` and `{{$timestamp}}` are available out of the box.

## Getting Started

### Install prebuilt binaries

Download from [GitHub Releases](https://github.com/unkn0wn-root/resterm/releases). You can use the snippets below to automatically detect the latest tag and fetch the matching binary for your platform.

> [!NOTE]
> The examples require `curl` and `jq`. Install `jq` with your package manager (e.g. `brew install jq`, `sudo apt install jq` etc.).

#### Linux / macOS

```bash
# Detect latest version
LATEST_TAG=$(curl -fsSL https://api.github.com/repos/unkn0wn-root/resterm/releases/latest | jq -r .tag_name)

# Download the appropriate binary (Darwin/Linux + amd64/arm64)
curl -fL -o resterm "https://github.com/unkn0wn-root/resterm/releases/download/${LATEST_TAG}/resterm_$(uname -s)_$(uname -m)"

# Make it executable and install into your PATH
chmod +x resterm
sudo install -m 0755 resterm /usr/local/bin/resterm
```

If your system does not include `install`, replace the final line with `