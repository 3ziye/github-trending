# state-machines

> **A learning-focused Rust port of Ruby's state_machines gem**

[![Crates.io](https://img.shields.io/crates/v/state-machines.svg)](https://crates.io/crates/state-machines)
[![Documentation](https://docs.rs/state-machines/badge.svg)](https://docs.rs/state-machines)
[![License: MIT OR Apache-2.0](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/github-state--machines/state--machines--rs-blue)](https://github.com/state-machines/state-machines-rs)

## About This Project

This is a Rust port of the popular [state_machines](https://github.com/state-machines/state_machines) Ruby gem, created as a **learning platform for Rubyists transitioning to Rust**.

While learning Rust, I chose to port something familiar and widely used—so I could compare implementations side-by-side and understand Rust's patterns through a lens I already knew. This library is intentionally **over-commented**, not because the code is disorganized, but because it's designed to be a **teaching tool**. The goal is elegant, idiomatic Rust code that Rubyists can learn from without the usual compile-pray-repeat cycle.

### Philosophy

- **Learning Ground First**: Extensive inline comments explain Rust concepts, ownership, trait bounds, and macro magic
- **Ruby Parallels**: Familiar DSL syntax and callbacks make the transition smoother
- **Production Ready**: Despite the educational focus, this is a fully functional state machine library with:
  - **Typestate pattern** for compile-time state safety
  - **Zero-cost abstractions** using PhantomData
  - Guards and unless conditions
  - Before/after event callbacks
  - Sync and async support
  - `no_std` compatibility (for embedded systems)
  - Payload support for event data
  - Move semantics preventing invalid state transitions

### For the Rust Community

**You're welcome to open PRs** to fix fundamentally wrong Rust concepts—but please **don't remove comments just because "we know it"**. This codebase serves beginners. If something can be explained better, improve the comment. If a pattern is unidiomatic, fix it *and document why*.

---

## Features

**Typestate Pattern** – Compile-time state safety using Rust's type system with zero runtime overhead

**Guards & Unless** – Conditional transitions at event and transition levels

**Callbacks** – `before`/`after` hooks at event level

**Around Callbacks** – Wrap transitions with Before/AfterSuccess stages for transaction-like semantics

**Async Support** – First-class `async`/`await` for guards and callbacks

**Event Payloads** – Pass data through transitions with type-safe payloads

**No-std Compatible** – Works on embedded targets (ESP32, bare metal)

**Type-safe** – Invalid transitions become compile errors, not runtime errors

**Hierarchical States** – Superstates with polymorphic transitions via SubstateOf trait

**Dynamic Dispatch** – Runtime event dispatch for event-driven systems (opt-in via feature flag or explicit config)

---

## Quick Start

Add to your `Cargo.toml`:

```toml
[dependencies]
state-machines = "0.1"
```

### Basic Example

```rust
use state_machines::state_machine;

// Define your state machine
state_machine! {
    name: TrafficLight,

    initial: Red,
    states: [Red, Yellow, Green],
    events {
        next {
            transition: { from: Red, to: Green }
            transition: { from: Green, to: Yellow }
            transition: { from: Yellow, to: Red }
        }
    }
}

fn main() {
    // Typestate pattern: each transition returns a new typed machine
    let light = TrafficLight::new(());
    // Type is TrafficLight<Red>

    let light = light.next().unwrap();
    // Type is TrafficLight<Green>

    let light = light.next().unwrap();
    // Type is TrafficLight<Yellow>
}
```

### With Guards and Callbacks

```rust
use state_machines::{state_machine, core::GuardError};
use std::sync::atomic::{AtomicBool, Ordering};

static DOOR_OBSTRUCTED: AtomicBool = AtomicBool::new(false);

state_machine! {
    name: Door,

    initial: Closed,
    states: [Closed, Open],
    events {
        open {
            guards: [path_clear],
            before: [check_safety],
            after: [log_opened],
            transition: { from: Closed, to: Open }
        }
        close {
            transition: { from: Open, to: Closed }
        }
    }
}

impl<C, S> Door<C, S> {
    fn path_clear(&self, _ctx: &C) -> bool {
        !DOOR_OBSTRUCTED.load(Ordering::Relaxed)
    }

    fn check_safety(&self) {
        println!("Checking if path is clear...");
    }

    fn log_opened(&self) {
        println!("Door opened at {:?}", std::time::SystemTime::now());
    }
}

fn main() {
    // Successful transition
    let door = Door::new(());
    let door = door.open().unwrap();
    let door = door.close().unwrap();

    // Failed guard check
    DOOR_OBSTRUCTED.store(true, Ordering::Relaxed);
    let err = door.open().expect_err("should fail when obstructed"