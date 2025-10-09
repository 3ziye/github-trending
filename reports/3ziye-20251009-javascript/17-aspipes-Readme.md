# asPipes: working pipelines today in pure JavaScript

## 1 Summary

asPipes is an experimental runtime abstraction that models the semantics of the proposed |> pipeline operator, implemented entirely in standard JavaScript (ES2020+).
It demonstrates that pipeline-style composition can be expressed using the existing coercion semantics of the bitwise OR operator (|) and Symbol.toPrimitive.

The implementation is small (<50 lines) and supports both synchronous and asynchronous evaluation with a familiar syntax:

```javascript
const greeting = pipe('hello');

greeting 
  | upper 
  | ex('!!!');

await greeting.run(); // → "HELLO!!!"
```

## Installation

```bash
npm install aspipes
```

```javascript
import { createAsPipes } from 'aspipes';
```

⸻

## 2 Motivation

The pipeline operator proposal (tc39/proposal-pipeline-operator) has been under discussion for several years, exploring multiple variants (F#, Smart, Hack, etc.).
The asPipes experiment aims to:

- prototype F#-style semantics directly in today’s JavaScript;
- study ergonomics and readability in real-world code;
- show that deferred, referentially transparent composition can be achieved without syntax extensions; and
- inform the design conversation with practical, user-level feedback.

⸻

## 3 Design Goals

- ✅ Composable — each transformation behaves like a unary function of the previous result.
- ✅ Deferred — no execution until .run() is called.
- ✅ Async-safe — promises and async functions are first-class citizens.
- ✅ Stateless — no global mutation; every pipeline owns its own context.
- ✅ Ergonomic — visually aligns with the future |> operator.

⸻

## 4 Core API

### Installation and Import

```bash
npm install aspipes
```

```javascript
import { createAsPipes } from 'aspipes';
```

### createAsPipes()

Creates an isolated pipeline environment and returns:

```javascript
{
  pipe, // begin a pipeline
  asPipe // lift a function into a pipeable form
}
```

pipe(initialValue)

Begins a new pipeline with initialValue.
The returned object intercepts | operations via Symbol.toPrimitive.
Call .run() to evaluate and retrieve the final result (async).

asPipe(fn)

Wraps a function fn so that it can be used in a pipeline:

```javascript
const upper = asPipe((s) => s.toUpperCase());
const ex = asPipe((s, mark = '!') => s + mark);
```

Pipeable functions can also be called with arguments:

```javascript
pipe('hello') 
  | upper 
  | ex('!!!');
```

.run()

Evaluates the accumulated transformations sequentially, returning a Promise of the final value.

## 5 Examples

**A. String pipeline**

```javascript
import { createAsPipes } from 'aspipes';

const { pipe, asPipe } = createAsPipes();

const upper = asPipe((s) => s.toUpperCase());
const ex = asPipe((s, mark = '!') => s + mark);

const greeting = pipe('hello');
greeting 
  | upper 
  | ex('!!!');
  
console.log(await greeting.run()); // "HELLO!!!"
```

**B. Numeric pipeline**

```javascript
import { createAsPipes } from 'aspipes';

const { pipe, asPipe } = createAsPipes();

const inc = asPipe((x) => x + 1);
const mul = asPipe((x, k) => x * k);

const calc = pipe(3);
calc 
  | inc 
  | mul(10);

console.log(await calc.run()); // 40
```

**C. Async composition (LLM API call)**

```javascript
import { createAsPipes } from 'aspipes';

const { pipe, asPipe } = createAsPipes();

const postJson = asPipe((url, body, headers = {}) =>
  fetch(url, {
    method: 'POST',
    headers: { 'content-type': 'application/json', ...headers },
    body: JSON.stringify(body),
  }),
);
const toJson = asPipe((r) => r.json());
const pick = asPipe((o, ...keys) => keys.reduce((a, k) => a?.[k], o));
const trim = asPipe((s) => (typeof s === 'string' ? s.trim() : s));

const ENDPOINT = 'https://api.berget.ai/v1/chat/completions';
const BODY = {
  model: 'gpt-oss',
  messages: [
    { role: 'system', content: 'Reply briefly.' },
    { role: 'user', content: 'Write a haiku about mountains.' },
  ],
};

const haiku = pipe(ENDPOINT);
haiku 
| postJson(BODY) 
| toJson 
| pick('choices', 0, 'message', 'content') 
| trim;
console.log(await haiku.run());
```

**D. Composable pipes (Higher-Order Pipes)**

Pipes can be composed into reusable, named higher-order pipes by wrapping them with `asPipe`. The implementation automatically detects and executes pipeline expressions, enabling clean, direct syntax:

```javascript
import { createAsPipes } from 'aspipes';

const { pipe, asPipe } = createAsPipes();

// Assume postJson, toJson, pick, trim are defined (see example C)

// Create reusable bot operations
const askBot = asPipe((question) => {
  const p = pipe('https://api.berget.ai/v1/chat/completions');
  p 
  | postJson({
      model: 'gpt-oss',
      messages: [{ role: 'user', content: question }],
    }) 
  | toJson 
  | pick('choices', 0, 'message', 'content') 
  | trim;
  return p;
});

const summarize = asPipe((text) => {
  const p = pipe('https://api.berget.ai/v1/chat/completions');
  p 
  | postJson({
      model: 'gpt-oss',
      messag