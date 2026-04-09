<img src="https://raw.githubusercontent.com/dashersw/gea/master/docs/public/logo.jpg" height="180" alt="Gea" />

[![npm version](https://badge.fury.io/js/%40geajs%2Fcore.svg)](https://www.npmjs.com/package/@geajs/core)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

# Gea

A batteries-included, reactive JavaScript UI framework. No virtual DOM. Compile-time JSX transforms. Proxy-based stores. Surgical DOM patching. Built-in state management and routing. ~19 kb gzipped with the router, ~15 kb without.

Gea compiles your JSX into efficient HTML string templates at build time, tracks state changes through deep proxies, and patches only the DOM nodes that actually depend on the changed data — no diffing, no reconciliation overhead.

```jsx
// counter-store.ts
import { Store } from '@geajs/core'

class CounterStore extends Store {
  count = 0
  increment() { this.count++ }
  decrement() { this.count-- }
}

export default new CounterStore()
```

```jsx
// app.tsx
import { Component } from '@geajs/core'
import counterStore from './counter-store'

export default class App extends Component {
  template() {
    return (
      <div>
        <h1>{counterStore.count}</h1>
        <button click={counterStore.increment}>+</button>
        <button click={counterStore.decrement}>-</button>
      </div>
    )
  }
}
```

```ts
// main.ts
import App from './app'

new App().render(document.getElementById('app'))
```

## Getting Started

```bash
npm create gea@latest my-app
cd my-app
npm install
npm run dev
```

This scaffolds a Vite-powered project with TypeScript, a sample store, class and function components, and hot module replacement — ready to build on.

## Packages

| Package | Description | Version |
| --- | --- | --- |
| [`@geajs/core`](packages/gea) | Core framework — stores, components, reactivity, DOM patching | [![npm](https://img.shields.io/npm/v/@geajs/core.svg)](https://www.npmjs.com/package/@geajs/core) |
| [`@geajs/ui`](packages/gea-ui) | Headless UI primitives — accessible, composable components built on [Zag.js](https://zagjs.com) | [![npm](https://img.shields.io/npm/v/@geajs/ui.svg)](https://www.npmjs.com/package/@geajs/ui) |
| [`@geajs/mobile`](packages/gea-mobile) | Mobile UI primitives — views, navigation, gestures, layout | [![npm](https://img.shields.io/npm/v/@geajs/mobile.svg)](https://www.npmjs.com/package/@geajs/mobile) |
| [`@geajs/ssr`](packages/gea-ssr) | Server-side rendering — streaming HTML, hydration, store isolation | [![npm](https://img.shields.io/npm/v/@geajs/ssr.svg)](https://www.npmjs.com/package/@geajs/ssr) |
| [`@geajs/vite-plugin`](packages/vite-plugin-gea) | Vite plugin — JSX transform, reactivity wiring, HMR | [![npm](https://img.shields.io/npm/v/@geajs/vite-plugin.svg)](https://www.npmjs.com/package/@geajs/vite-plugin) |
| [`create-gea`](packages/create-gea) | Project scaffolder — `npm create gea@latest` | [![npm](https://img.shields.io/npm/v/create-gea.svg)](https://www.npmjs.com/package/create-gea) |
| [`gea-tools`](packages/gea-tools) | VS Code / Cursor extension — completions, hover, diagnostics | — |

## Philosophy

JavaScript code should be simple and understandable. Gea is built on the belief that a framework should not force you to learn a new programming model. You shouldn't need signals, dependency arrays, compiler directives, or framework-specific primitives to build a reactive UI. You should write regular JavaScript — classes, functions, objects, getters — and it should just work.

Gea finds the right mix of object-oriented and functional style. Stores are classes with state and methods. Components are classes with a `template()` that returns JSX. Function components are true plain functions with **no side-effects**. Computed values are getters. There is nothing to learn that isn't already JavaScript.

The only "magic" is under the hood: the Vite plugin analyzes your ordinary code at compile time and wires up the reactivity for you. You write `this.count++` and the DOM updates. You don't call a setter, you don't wrap values in a signal, and you don't declare dependencies. The framework stays invisible.

Gea is built on the philosophy of the beautifully simple [erste.js](https://github.com/dashersw/erste) and [regie](https://github.com/dashersw/regie) libraries, carrying forward their core ideas — minimal abstraction, class-based components, and direct DOM ownership — while adding compile-time JSX transforms, deep proxy reactivity, and a modern build toolchain.

## Why Gea?

- **Just JavaScript.** No signals, no hooks, no dependency arrays, no new syntax. Classes, functions, objects, and getters — concepts you already know.
- **No virtual DOM.** The Vite plugin analyzes your JSX at build time and generates targeted DOM patches. Updates touch only the elements that changed.
- **Proxy-based reactivity.** Mutate state directly — `this.count++` — and the framework handles the rest. The compile-time analysis makes your regular JS fully reactive w