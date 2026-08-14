# Dogwood

Dogwood is a governance language designed for AI agents and their tools. It
supports [Cedar](https://www.cedarpolicy.com/) policies and adds temporal
conditions (`since`, `formerly`, `once`, aggregations) to look back over an
agent's recent events.

```text
permit(principal, action, resource)
when { context.input.amount < 1000 }
when formerly within 1h {
    Action::"Approve"::request{ approver: context.input.approver }
};
```

This repository contains a **reference interpreter** for the language for the
purpose of understanding the semantics of the language, with simple examples of
the kinds of policies Dogwood supports.  This reference interpreter is **NOT**
intended for production use. Please see the end of this document for a list
of important limitations of the interpreter.

📖 **[Read the full documentation →](https://dogwood-policy.github.io/dogwood/index.html)**


## Key features

- **Cedar-derived syntax** — familiar `permit`/`forbid` with `when`/`unless`
- **Temporal conditions** — express "since login," "formerly approved," rate
  limits, and windowed aggregations over an event history
- **Information providers** — computed facts (Rhai scripts) injected at
  evaluation time as guardrail context fields
- **Compile-to-Cedar** — policies lower to standard Cedar; the temporal and
  provider fields become `context.*` slots filled at runtime
- **Pluggable backends** — swap the policy engine (local Cedar or a remote
  policy store) and the temporal engine (in-memory or database-backed)
  independently

## Repository layout

| Path | Description |
|------|-------------|
| [`dogwood-language/`](dogwood-language/README.md) | The core Rust library — parser, interpreter, lowering, and API |
| [`dogwood-docs/guide/`](dogwood-docs/guide/README.md) | The language guide (syntax, schemas, temporal expressions, providers, formal spec) |
| [`dogwood-cli/`](dogwood-docs/guide/12-cli.md) | The `dogwood` CLI (validate, lower, replay) |
| [`dogwood-docs/examples/`](dogwood-docs/examples/) | Runnable example policies with traces and expected output |
| [`dogwood-language/configuration/`](dogwood-language/configuration/README.md) | Starter action schemas and event schemas |

## Quick start

```bash
# Validate a policy against its schemas:
dogwood validate policy.dw --policy-schema schema.cedarschema

# Lower to Cedar and see the output:
dogwood lower policy.dw --policy-schema schema.cedarschema --emit both

# Replay a trace and see verdicts:
dogwood replay policy.dw --policy-schema schema.cedarschema --trace events.log
```

### Worked example

The [`read_after_login`](dogwood-docs/examples/read_after_login/) example
permits a Read only if the same user logged in within the last hour:

```text
// policy.dw
@id("read_after_login")
permit (
    principal,
    action == Drupe::Action::"Read",
    resource
)
when temporal {
    formerly within 1h Drupe::Action::"Login"::request{ input.user: context.input.user }
};
```

Replay it against a trace of three events (login at t=0, read at t=10s, read at
t=2h):

```bash
$ dogwood replay dogwood-docs/examples/read_after_login/policy.dw \
    --policy-schema dogwood-docs/examples/read_after_login/schema.cedarschema \
    --trace dogwood-docs/examples/read_after_login/trace.log

@0 (time point 0): DENY
@10 (time point 1): ALLOW  [rules: 0]
@7200 (time point 2): DENY
```

The first event is the login itself (no read requested) → DENY. Ten seconds
later Alice reads → ALLOW (she logged in recently). Two hours later she tries
again → DENY (the login has expired from the 1-hour window).

You can also validate and lower to Cedar:

```bash
$ dogwood validate dogwood-docs/examples/read_after_login/policy.dw \
    --policy-schema dogwood-docs/examples/read_after_login/schema.cedarschema
OK: validation passed with no errors or warnings.

$ dogwood lower dogwood-docs/examples/read_after_login/policy.dw \
    --policy-schema dogwood-docs/examples/read_after_login/schema.cedarschema \
    --emit cedar-policies
@id("read_after_login")
permit(principal, action == Drupe::Action::"Read", resource) when { context.policy_0__temporal_0 };
```

The lowered Cedar replaces the temporal condition with a `context.*` slot that
Dogwood fills at runtime from the event history.

See the [Getting Started guide](dogwood-docs/guide/01-getting-started.md) for
full setup instructions and more examples in
[`dogwood-docs/examples/`](dogwood-docs/examples/).

## Using Dogwood as a Rust library

Add the crate to your `Cargo.toml`:

```toml
[dependencies]
dogwood-language = { git = "https://github.com/dogwood-policy/dogwood.git" }
```

See the [library README](dogwood-language/README.md) for the API overview and
the [API and Workflow guide](dogwood-docs/guide/07-api-and-workflow.md) for
detailed usage.

## AI agent integration

This repo ships agent skills that let AI coding assistants author Dogwood
policies from natural-language requirements. See
[AGENTS-README.md](AGENTS-README.md) for setup across Claude Code,