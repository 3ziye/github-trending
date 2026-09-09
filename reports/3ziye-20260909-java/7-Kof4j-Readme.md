# Kof

<p align="center">
  <img src="kof.png" alt="Kof Logo" width="200">
</p>

### Uma linguagem. Um compilador. Vários mundos.
se pronuncia coffe

**Menos código. Mais intenção. JVM, nativo, script e web. Tudo partindo da mesma linguagem.**

---

## Mascote

<p align="center">
  <img src="kof_mascot.png" alt="Mascote da Kof — uma civetta" width="300">
</p>

O mascote da Kof é uma **civetta** — também conhecida como **gato do almiscar**,
é um felino que come café. Nada mais adequado para uma linguagem que se pronuncia
*coffe*.

---

## Disclaimer

A linguagem Kof não possui qualquer relação com o jogo The King of Fighters ou com sua franquia.

O nome Kof surgiu como uma referência à palavra "coffee" escrita propositalmente de forma incorreta. A escolha foi feita justamente na tentativa de criar um nome curto, único e facilmente identificável para a linguagem.

Koflang e Kof4J não compactuam com a associação do nome à franquia The King of Fighters. Qualquer semelhança ou associação feita nesse sentido é incidental e não representa a origem, o propósito ou a identidade dos projetos.

Nosso objetivo sempre foi criar uma identidade própria para a linguagem e seus componentes.

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

Kof é uma linguagem de programação **geral e estaticamente tipada**, construída com uma ideia central:

> **Uma única linguagem não deveria obrigar você a escolher um único mundo.**

> 📖 **A especificação formal da linguagem** (gramática, sistema de tipos,
> semântica, status de cada feature) está em
> [`docs/language-reference/`](docs/language-reference/). A arquitetura do
> compilador (implementação) está em
> [`docs/compiler-architecture.md`](docs/compiler-architecture.md). A
> distinção **linguagem ≠ compilador ≠ target** é o eixo desses documentos.

Kof possui seu próprio compilador, lexer, parser, sistema de tipos, análise semântica e representação intermediária (Kof IR). A partir dessa IR, diferentes backends transformam o mesmo programa em diferentes formas de execução:

```text
            Linguagem Kof  (definida pela especificação)
                          │
                    Kof Compiler  (uma implementação)
                          │
                       Kof IR  (máquina de pilha linear, 30 ops)
                          │
          ┌───────────────┼────────────────┐
          │               │                │
       JVM Backend    Native Backend    JS Backend
          │               │                │
          ▼               ▼                ▼
        JVM          Native Binary      ES Modules
       (.class)      (ELF x86_64,       (Node /
                      riscv64/aarch64)    browser)
```

**A linguagem não muda. O target muda.** JVM, Native e JS são *targets de
compilação* da mesma Kof — não dialetos semanticamente diferentes. **KofScript**
(`.ks`, REPL) é um *target de execução direta*: Kof puro consumindo o MESMO
frontend e executado pelo interpretador da IR, sem compilar e sem fork de JVM —
**não é JavaScript** (`let`/`const`/`async`/`fn` não existem). KofC é uma
ferramenta separada (subconjunto C → ELF), não consome a IR Kof — ver
[docs/compiler-architecture.md](docs/compiler-architecture.md) §7.)

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

Kof está em desenvolvimento ativo — **0.3.0-beta**.

O compilador possui frontend próprio, type system, Kof IR e **três backends
sobre a IR**, que produzem **seis targets**: JVM (V21 via ASM), Native x86_64
(ELF, sem libc), `native.risc`/`native.arm` (riscv64 real + aarch64 via
tradutor ISA), KofJS (ES Modules) e Android (variante do JVM + empacotamento
APK). **KofScript** (`.ks`, REPL) é um **target de execução direta**: Kof puro
no MESMO frontend, executado pelo interpretador da IR (`KofInterpreter`) sem
emitir bytecode nem fork de JVM. **KofC** (subconjunto C → nativo) é uma
ferramenta separada, não consome a IR Kof — ver
[docs/compiler-architecture.md](docs/compiler-architecture.md) §7.

| Feature | JVM | Native | KofJS |
|---------|-----|--------|-------|
| println, variáveis, aritmética | ✅ | ✅ | ✅ |
| if/else, if-expr, while, for, for-in, switch | ✅ | ✅ | ✅ |
| functions (sem `fun`), lambdas com capturas | ✅ | ✅ | ✅ |
| records, classes, herança, interfaces, virtual dispatch | ✅ | ✅ | ✅ |
| generics (erasure), `Bo