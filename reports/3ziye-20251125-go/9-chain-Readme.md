## JuChain

[![CI/CD Pipeline](https://github.com/juchain-network/chain/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/juchain-network/chain/actions/workflows/ci.yml)
[![Go Version](https://img.shields.io/badge/Go-1.23-blue.svg)](https://golang.org/)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-green.svg)](https://www.gnu.org/licenses/lgpl-3.0.en.html)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/juchain-network/chain.svg)](https://github.com/juchain-network/chain/stargazers)

JuChain aims to bring programmability and interoperability to the Ju Beacon Chain. To embrace the existing Ethereum ecosystem and advanced technologies, JuChain is developed as a fork of go-ethereum, supporting all Ethereum smart contracts and tooling.

JuChain is based on go-ethereum, so you will find many tools, binaries, and documentation similar to Ethereum, such as the name "geth".

On top of EVM compatibility, JuChain introduces a Proof of Staked Authority (JPoA) consensus mechanism with 21 validators, supporting shorter block times and lower transaction fees. The top staking candidates become validators and produce blocks. Double-sign detection and slashing logic guarantee security, stability, and chain finality.

**JuChain Features:**

* **Self-sovereign blockchain:** Security and reliability through elected validators.
* **EVM compatible:** Supports all Ethereum tooling, with faster finality and lower transaction fees.
* **On-chain governance and decentralization:** JPoA consensus brings decentralization and community participation. The native token JU serves as both gas for smart contract execution and staking/governance.

See more details in the [JuChain Docs](https://juchain.gitbook.io/juchain-docs).

## Key Features

### JPoA Consensus

While Proof-of-Work (PoW) has proven effective for decentralization, it is not environmentally friendly and requires a large number of participants for security.

Proof-of-Authority (PoA) improves efficiency and tolerates a certain proportion of Byzantine nodes, but is less decentralized. Many blockchains (such as EOS, Cosmos) use Delegated Proof of Stake (DPoS), allowing token holders to vote and elect validators, increasing decentralization and favoring community governance.

JuChain combines DPoS and PoA, implementing an innovative JPoA consensus engine:

1. Blocks are produced by a limited set of validators.
2. Validators take turns producing blocks in a PoA manner, similar to Ethereum's Clique consensus.
3. Validator set is dynamically elected through staking and on-chain governance.
4. The JPoA engine interacts with system contracts for liveness slashing, revenue distribution, and validator set renewal.

## Native Token

JU is the native token of JuChain, similar to ETH on Ethereum:

1. Used to pay gas for smart contract deployment and invocation
2. Used for staking and governance

## Building the source

For prerequisites and detailed build instructions please read the [Installation Instructions](https://geth.ethereum.org/docs/install-and-build/installing-geth).

Building `geth` requires both Go (version 1.24 or later) and a C compiler (GCC 5 or higher). Once dependencies are installed, run:

```shell
make geth
```

or, to build the full suite of utilities:

```shell
make all
```

## Executables

The go-ethereum project comes with several wrappers/executables found in the `cmd`
directory.

|    Command    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :-----------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  **`geth`**   | Our main Ethereum CLI client. It is the entry point into the Ethereum network (main-, test- or private net), capable of running as a full node (default), archive node (retaining all historical state) or a light node (retrieving