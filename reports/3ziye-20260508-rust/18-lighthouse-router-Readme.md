# Lighthouse Router

Off-chain DEX route discovery for Solana. Built so that I'd stop hand-rolling
the same constant-product math in every script I write.

![Rust](https://img.shields.io/badge/rust-1.74+-orange?style=flat-square)
![License](https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square)
![Solana](https://img.shields.io/badge/solana-1.18-9945FF?style=flat-square)

## Why?

When you want to quote a swap across Solana DEXs without delegating it to a
third-party router, you end up reimplementing pool math, account decoding,
and shortest-path search. This crate is the small set of primitives I use
for that, kept honest by tests.

It is **not** a Jupiter replacement. It is small, dependency-light, and
predictable. If you need cross-program invocation, MEV bundle building, or
slippage protection in production: keep using something else.

## What's in here

- Pool decoders for Raydium AMM v4, Orca Whirlpool, and Phoenix order books
  (the last is a typed model — feed it from `phoenix-sdk`).
- Constant-product and concentrated-liquidity quote math, with tests.
- A token graph and a depth-limited router for multi-hop quotes.
- Bellman-Ford negative-cycle detection for marginal-price arbitrage scans.
- A `lighthouse` CLI that wires it all up against an RPC endpoint.

## Architecture

```
┌────────────────┐     ┌──────────────────┐     ┌──────────────┐
│  Solana RPC    │ ──► │  client::fetch_  │ ──► │  decoders    │
│  (mainnet/RPC) │     │  many (parallel) │     │  raydium /   │
└────────────────┘     └──────────────────┘     │  orca /      │
                                                │  phoenix     │
                                                └──────┬───────┘
                                                       │ AnyPool
                                                       ▼
                              ┌────────────┐   ┌───────────────┐
                              │  cache     │ ◄─┤  pool::Quoter │
                              │  (TTL)     │   └──────┬────────┘
                              └────────────┘          │
                                                      ▼
                                              ┌───────────────┐
                                              │  graph::Graph │
                                              └──┬──────────┬─┘
                                                 │          │
                                       router::best_route   │
                                                            ▼
                                                arbitrage::find_negative_cycle
```

The `Quoter` trait is the seam between pool decoding and routing — every
DEX integration needs to provide `mints()`, `quote()`, and `is_active()`.
`AnyPool` is the runtime sum type the graph stores, so the router doesn't
need to be generic over each concrete venue.

## Install & Run

```bash
cargo add lighthouse-router      # as a library
# or, for the CLI:
cargo install --path .
```

Quote a route:

```bash
lighthouse quote \
  --from EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v \
  --to   So11111111111111111111111111111111111111112  \
  --amount 1_000_000_000 \
  --max-hops 3
```

## Library usage

```rust
use lighthouse_router::{best_route, AnyPool, Graph, Pool};

let pools: Vec<AnyPool> = load_pools_from_somewhere();
let graph = Graph::build(pools);

let route = best_route(&graph, usdc_mint, sol_mint, 1_000_000, 3)?;
println!("out = {}", route.amount_out);
for step in &route.steps {
    println!("  {} via {}", step.pool_idx, step.venue);
}
```

See `examples/quote.rs` and `examples/find_arb.rs` for runnable end-to-end
examples that don't need an RPC connection.

## Configuration

| Flag                | Default                                | Notes                                |
|---------------------|----------------------------------------|--------------------------------------|
| `--rpc`             | `https://api.mainnet-beta.solana.com`  | Read from `SOLANA_RPC_URL` if unset. |
| `--max-hops`        | `3`                                    | Routing depth ceiling.               |
| `--probe` (arb)     | `1_000_000`                            | Probe size for marginal-price weights. |

## Status

Early but useful. The bits I rely on day-to-day (CP math, the graph builder,
and the CLI quote command) are stable. The Whirlpool quoter is honest about
its single-tick-range limitation: it refuses to quote rather than lie when
a swap would cross a tick. Phoenix is a typed model — you wire it up.

## License

Apache-2.0. See [LICENSE](LICENSE).
