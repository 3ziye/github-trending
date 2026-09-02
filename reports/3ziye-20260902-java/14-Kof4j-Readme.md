# Kof

<p align="center">
  <img src="kof.png" alt="Kof Logo" width="200">
</p>

### Uma linguagem. Um compilador. Vários mundos.
se pronuncia coffe

**Menos código. Mais intenção. JVM, nativo, script e web. Tudo partindo da mesma linguagem.**

---

> Algumas pessoas olham para um problema e escrevem uma biblioteca.
>
> Outras escrevem um framework.
>
> Algumas criam uma ferramenta.
>
> Eu aparentemente olhei para o ecossistema inteiro e pensei:
>
> **"Tá tudo complicado demais. Vou criar uma linguagem."**
>
> E, aparentemente, uma linguagem só também não era suficiente.

Bem-vinda à **Kof**.

---

# O que é Kof?

Kof é uma linguagem de programação **geral, fortemente tipada e estaticamente tipada**, construída com uma ideia central:

> **Uma única linguagem não deveria obrigar você a escolher um único mundo.**

Kof possui seu próprio compilador, lexer, parser, sistema de tipos, análise semântica e representação intermediária.

A partir dessa representação, diferentes backends podem transformar o mesmo programa em diferentes formas de execução.

```text
                         KOF
                          │
                    Kof Compiler
                          │
                       Kof IR
                          │
          ┌───────────────┼────────────────┐
          │               │                │
       Kof4J          KofNative        KofScript
          │               │                │
          ▼               ▼                ▼
        JVM          Native Binary      Runtime
       .class        Executável        Interativo
          │               │                │
          ▼               ▼                ▼
        JVM             OS/CPU        Kof Runtime
                          │
                          ▼
                        KofJS
                          │
                          ▼
                         Web
```

---

# O que é Kof?

Kof é uma linguagem de programação **geral, fortemente tipada e estaticamente tipada**.

Uma linguagem. Um compilador. Múltiplos targets.

```text
Kof Source
    │
    ▼
Kof Compiler
    │
    ▼
Kof IR
    │
    ├──────────► Kof4J ───────► JVM
    │
    ├──────────► KofNative ───► Executável nativo
    │
    ├──────────► KofScript ───► Runtime
    │
    └──────────► KofJS ───────► Web
```

**A linguagem não muda. O target muda.**

---

# Kof não é um transpiler

Kof não funciona assim:

```text
Kof → Java → javac → JVM
```

Funciona assim:

```text
Kof → Kof Compiler → Kof IR → Backend → Target
```

O compilador possui sua própria implementação de:

* lexer
* parser
* AST
* resolução de símbolos
* sistema de tipos
* análise semântica
* IR
* diagnostics
* geração de código

Kof não depende de Java como linguagem intermediária.

---

# Estado Atual

Kof está em desenvolvimento ativo — **0.1.0**.

O compilador possui frontend próprio, type system, Kof IR e três backends.

| Feature | JVM | Native | KofJS |
|---------|-----|--------|-------|
| println | ✅ | ✅ | ✅ |
| variables | ✅ | ✅ | ✅ |
| arithmetic | ✅ | ✅ | ✅ |
| if/else, if-expr | ✅ | ✅ | ✅ |
| while, for, do-while, for-in | ✅ | ✅ | ✅ |
| switch | ✅ | ✅ | ✅ |
| functions (sem `fun`) | ✅ | ✅ | ✅ |
| records | ✅ | ✅ | ✅ |
| classes | ✅ | ✅ | ✅ |
| constructors (`constructor(...)` + primary) | ✅ | ✅ | ✅ |
| inheritance, interfaces, virtual dispatch | ✅ | ✅ | ✅ |
| generics (erasure) | ✅ | ✅ | ✅ |
| lambdas | ✅ | ✅ | ✅ |
| exceptions (try/catch/finally) | ✅ | ✅ | ✅ |
| assert | ✅ | ✅ | ✅ |
| spawn (concorrência) | ✅ | CONC001 | — |
| strings (concat `+`, `==`, API completa) | ✅ | ✅ | ✅ |
| arrays | ✅ | ✅ | ✅ |
| List\<T\>, listOf | ✅ | ✅ | ✅ |
| JSON encode/decode (objetos no JVM) | ✅ | ✅ | ✅ |
| kof.io (File, Path, Directory) | ✅ | ✅ |
| kof.ui (Color, Palette, Theme) | ✅ | ✅ |
| kof.ui Window/Label/Button/Input (bind + ações) | ✅ | ✅ (JS render) | ✅ |
| kof.ui Column/Row/View/Style (layout) | ✅ | ✅ (JS render) | ✅ |
| Lambdas com capturas | ✅ | ✅ | ✅ |
| kof.time (`now()`) | ✅ | ✅ | ✅ |
| kof.web (`web.app()`, rotas, middleware) | ✅ | — | — |
| kof.security (passwords, crypto, jwt, secrets, auth) | ✅ | ~ | ~ |
| kof.config (arquivo > env > profile, typed) | ✅ | CONF001 | CONF001 |
| kof.log (níveis, off, JSON estruturado, requestId) | ✅ | ✅ (asm; UTC) | LOG001 |
| kof.db (JDBC, query tipada, `transaction {}`) | ✅ | ✅ (SQLite nativo; MySQL WIP) | DB001 |
| kof.orm (`entity`, CRUD, where c/ operadores, saveAll, page, deleteAll, migrate, MongoDB) | ✅ | ORM001 | ORM001 |
| String.toInt/toLong/toDouble/toFloat | ✅ | ✅ | ✅ |
| JSON Float/Double + arrays (`json.decode<Int[]>`) | ✅ | — | — |

**KofJS** (target `js`): o mesmo frontend e a mesma Kof IR geram ES Modules
(ECMAScript 2022+) executados na engine JS embarcada (GraalJS — sem Node.js
nem runtime externo). `kof build --target js` / `kof run --target js`.
Status alpha: [docs/targets/KOFJS.md](docs/targets/KOFJS.md).

**Concorrência**: `spawn tarefa()` / `spawn { ... }` — virtual threads na JVM,
join implícito; Native reporta `CONC001` 