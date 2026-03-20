# enject

Hide .env secrets from prAIng eyes.

(Note: this project was previously called enveil and has been renamed to enject)

AI coding tools like Claude Code, Copilot, Cursor, and others can read files in your project directory, which means a plaintext `.env` file is an accidental secret dump waiting to happen. This isn’t theoretical. It is a known issue that has happened to me several times (even after explicitly telling Claude not to peek in Claude Code’s settings.json file). `enject` solves this by ensuring plaintext secrets **never exist on disk at all**. Your `.env` file contains only symbolic references; the real values live in an encrypted local store and are injected directly into your subprocess at launch. 

This project is inspired by Filip Hric’s solution/[blog post](https://filiphric.com/dont-let-ai-read-your-env-files), which uses a similar concept leveraging 1Password. I wanted a self-contained solution that didn’t rely on a third party services giving rise to this solution. And yes, this project was built almost entirely with Claude Code with a bunch of manual verification and testing.

## Benefits and Caveats

This project is primarily designed to mitigate the known issue of AI/LLM tools accidentally reading `.env` secrets in your project. Additional benefits include preventing secret leakage if a `.env` is accidentally committed to a repository, the ability to share `.env` files containing references instead of plaintext secrets, and the option to share the encrypted store itself.                               

This project is not a silver bullet for preventing an AI agent from obtaining your secrets. For example, an agent can still write code (by accident or via prompt injection) that exfiltrates secrets to terminal output or a file at runtime. We strongly advise against relying on this tool, or `.env` files in general, to store production secrets

## How it works

Your `.env` file looks like this:

```
DATABASE_URL=en://database_url
STRIPE_KEY=en://stripe_key
PORT=3000
```

Technically it is safe to commit (maybe don’t do that, though), and more importantly: safe for any AI tools accidentally (or perhaps not-so-accidentally) snooping in on it.

When you run `enject run -- npm start`, it:

1. Prompts for your master password (never echoed, never in shell history)
2. Derives a 256-bit AES key from your password using **Argon2id** (64 MB memory, 3 iterations)
3. Decrypts the local store with **AES-256-GCM** — the store file is a 12-byte random nonce followed by authenticated ciphertext
4. Resolves every `en://` reference against the decrypted map
5. Zeroizes the key and password bytes from memory
6. Spawns your subprocess with the resolved values injected into its environment

The store file is a binary blob. Without the master password, it is indistinguishable from random noise. The nonce is freshly generated on every write, so AES-GCM nonce reuse is impossible. Any modification to the ciphertext — even a single flipped bit — causes authentication to fail and decryption to be refused.

---

## Installation

### Via cargo

This release is still in alpha, so requires appending the latest version to install when calling `cargo install`

```bash
cargo install enject --version 0.2.0-alpha 
```

### From source

Requires [Rust](https://rustup.rs) 1.70+.

```bash
git clone https://github.com/greatscott/enject
cd enject
cargo build --release
```

The compiled binary is at `target/release/enject`. Install it once to a location on your `PATH` so you can run it from any project:

**macOS / Linux (bash or zsh)**

```bash
# Option A: ~/.local/bin (no sudo required, common on Linux)
mkdir -p ~/.local/bin
cp target/release/enject ~/.local/bin/

# Option B: /usr/local/bin (requires sudo, available system-wide)
sudo cp target/release/enject /usr/local/bin/

# Option C: ~/.cargo/bin (already on PATH if you used rustup)
cp target/release/enject ~/.cargo/bin/
```

If you used option A and `~/.local/bin` is not already on your `PATH`, add this to your shell config (`~/.zshrc`, `~/.bashrc`, or `~/.bash_profile`):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then reload it:

```bash
source ~/.zshrc   # or ~/.bashrc
```

Verify it worked:

```bash
enject --version
```

### Per-project setup (run once per project)

The binary is installed globally — you never reinstall it. But each project gets its own encrypted store:

```bash
cd your-project
enject init
```

This creates `.enject/` in the current directory with the project's config and encrypted store. Add it to `.gitignore` — it should never be committed.

---

## Usage

### Initialize a store

Run this once per project, in the project root:

```bash
enject init
```

This generates a random 32-byte salt, writes `.enject/config.toml`, creates an empty encrypted store at `.enject/store`, and prompts you to set a master password. Add `.enject/` to your `.gitignore` — the store should never be committed.

### Add secrets

```bash
enject set some_database_