<p align="center">
  <img src="assets/banner.png" alt="Pixel art banner: a crab on rocky tide pools at sunset, with waves, sea stacks, and a forested headland, under the title Beautiful Rust and the subtitle Idiomatic Rust, distilled">
</p>

# Beautiful Rust

Three standard [Agent Skills](https://agentskills.io) and a lints config that teach coding
agents to write, review, port, and enforce idiomatic Rust:

- **`rust-best-practices`** loads whenever an agent writes or changes Rust, and steers it
  toward idiomatic, robust, maintainable code.
- **`rust-review`** reviews existing Rust code, a file, a crate, or a diff, and writes a
  prioritized report where every finding cites the rule it breaks and shows the fix.
- **`rust-port`** ports C, C++, Python, Go, or JavaScript to idiomatic Rust with the same
  behavior, porting the original tests first so you can prove the two match.
- **`lints/`** is a drop-in clippy configuration that enforces the machine-checkable rules
  in CI.

They work with Claude Code, OpenAI Codex, GitHub Copilot, Cursor, Gemini CLI, and any other
agent that reads the Agent Skills format. Every code example in the skills compiles on
stable Rust, and every lint in the config was checked against current clippy.

The guidance is distilled from five sources, with a condensed digest of each bundled in
the skill so the agent can consult the original reasoning when it needs to:

- [Google Rust Style Guide](https://google.github.io/styleguide/rustguide.html)
- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/) (official rust-lang checklist)
- [Effective Rust](https://www.lurklurk.org/effective-rust/) by David Drysdale
- [Rust Design Patterns](https://rust-unofficial.github.io/patterns/) (idioms, patterns, anti-patterns)
- [Microsoft Pragmatic Rust Guidelines](https://microsoft.github.io/rust-guidelines/)

Where the sources disagree, the skill picks a side and says why.

## What it changes

Asked for a small semver-parsing library, an agent without the skill produced working
code with public fields, no `# Errors` docs, and `unwrap()` in its doc examples. With the
skill, the same agent kept the fields private, documented failure modes, and wrote doc
examples users can copy safely. Condensed from those two runs:

```rust
// Without the skill
/// A semantic version. The fields are public for convenience.
pub struct Version {
    pub major: u64,
    pub minor: u64,
    pub patch: u64,
    pub pre: Vec<Identifier>,
    pub build: Vec<String>,
}

impl Version {
    /// Parses a version string.
    ///
    /// ```
    /// let v = Version::parse("1.2.3").unwrap();
    /// ```
    pub fn parse(s: &str) -> Result<Version, ParseError> { /* ... */ }
}
```

```rust
// With the skill
/// A semantic version. Equality, hashing, and ordering ignore build metadata.
pub struct Version {
    major: u64,
    minor: u64,
    patch: u64,
    pre: Vec<Identifier>,
    build: Vec<String>,
}

impl Version {
    /// Parses a version string according to SemVer 2.0.0.
    ///
    /// # Errors
    ///
    /// Returns [`ParseVersionError`] if the string is empty, a numeric part has a
    /// leading zero or overflows `u64`, or an identifier contains invalid characters.
    ///
    /// ```
    /// # use semver_lite::Version;
    /// # fn main() -> Result<(), semver_lite::ParseVersionError> {
    /// let v = Version::parse("1.2.3-beta.1")?;
    /// assert_eq!(v.major(), 1);
    /// # Ok(())
    /// # }
    /// ```
    pub fn parse(s: &str) -> Result<Self, ParseVersionError> { /* ... */ }

    /// Returns the major version number.
    pub fn major(&self) -> u64 { self.major }
}
```

Across three test tasks (a library, a CLI, and refactoring a messy module), the skill
passed 29 of 30 checks against 24 of 30 without it. See [Testing the skills](#testing-the-skills).

## Install

Each skill is a folder under `skills/`: `rust-best-practices/`, `rust-review/`, and
`rust-port/`. Every option below puts those folders where your agent looks for skills.
Install all three; the review and port skills lean on the best-practices skill for style.

### Any agent, one command

The [`skills`](https://github.com/vercel-labs/skills) installer supports most agents
(Node 22.20 or later):

```bash
npx skills add morganlinton/BeautifulRust
```

Add `-g` to install for your user instead of the current project, or `-a <agent>` to pick
an agent, such as `-a codex` or `-a cursor`.

### Claude Code

Install it as a plugin so updates arrive with one command:

```bash
claude plugin install beautiful-rust --marketplace morganlinton/BeautifulRust
```

Inside a session, the same thing is:

```
/plugin marketplace add morganlinton/BeautifulRust
/plugin install beautiful-rust@beautiful-rust
```

This installs all three skills. They appear as `/beautiful-rust:rust-best-practices`,
`/beautiful-rust:rust-review`, and `/beautiful-rust:rust-port`, though you rarely need to
call them, since they trigger on their own. To try it for one session without insta