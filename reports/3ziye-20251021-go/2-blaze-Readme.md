# Blaze

<div align="center">
  <img alt="image" src="./media/image.png" />
  <p>
    <a href="https://wizenheimer.github.io/blaze/"><strong>Docs </strong> </a>
  </p>
</div>

**Built for hackers, not hyperscalers.**  
A tiny, hackable full-text search engine you can actually fit in your head. Features inverted indexing, boolean queries, phrase search, proximity queries, and BM25 ranking—powered by a flexible query engine, roaring bitmaps, and skip lists.

> [!NOTE]
> This focuses on keyword-based full-text search. For semantic search with embeddings, see [Comet](https://github.com/wizenheimer/comet) ([docs](https://pkg.go.dev/github.com/wizenheimer/comet)).

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Not for Everyone](#not-for-everyone)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Concepts](#core-concepts)
  - [Inverted Index](#inverted-index)
  - [Skip Lists](#skip-lists)
  - [Text Analysis Pipeline](#text-analysis-pipeline)
  - [Search Operations](#search-operations)
- [Query Builder API](#query-builder-api)
  - [Why Use Builder Pattern](#why-use-builder-pattern)
  - [Quick Start](#query-builder-quick-start)
  - [Core Methods](#query-builder-core-methods)
  - [Boolean Operations](#boolean-operations)
  - [Query Patterns](#query-patterns)
  - [Performance](#query-builder-performance)
  - [Best Practices](#query-builder-best-practices)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Performance Characteristics](#performance-characteristics)
- [Configuration](#configuration)
- [Use Cases](#use-cases)
- [Testing](#testing)
- [Architecture](#architecture)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [Related Projects](#related-projects)
- [License](#license)

## Overview

Blaze is a Go engine that provides fast, full-text search capabilities through an inverted index implementation. It's designed for applications that need to search through text documents efficiently without relying on external search engines.

> [!TIP]
> Blaze handles keyword-based search (BM25, phrase matching, boolean queries). If you need vector embeddings or hybrid retrieval, [Comet](https://github.com/wizenheimer/comet) ([docs](https://pkg.go.dev/github.com/wizenheimer/comet)) implements HNSW, IVF, and quantization-based indexes with metadata filtering. It's a hybrid vector store written from scratch in Go, purpose built for hackers, not hyperscalers.

**Key Highlights:**

- **Inverted Index**: Maps terms to document positions for instant lookups
- **Skip Lists**: Probabilistic data structure providing O(log n) operations
- **Query Builder**: Type-safe, fluent API for boolean queries with roaring bitmaps
- **Advanced Search**: Phrase search, BM25 ranking, proximity ranking, and boolean queries
- **BM25 Algorithm**: Industry-standard relevance scoring with IDF and length normalization
- **Text Analysis**: Tokenization, stemming, stopword filtering, and case normalization
- **Thread-Safe**: Concurrent indexing with mutex protection
- **Serialization**: Efficient binary format for persistence

## Features

### Search Capabilities

- **Term Search**: Find documents containing specific terms
- **Phrase Search**: Exact multi-word matching ("quick brown fox")
- **Boolean Queries**: Type-safe AND, OR, NOT operations with query builder
- **BM25 Ranking**: Industry-standard relevance scoring (used by Elasticsearch, Solr)
- **Proximity Ranking**: Score results by term proximity
- **Position Tracking**: Track exact word positions within documents
- **Roaring Bitmaps**: Compressed bitmap operations for fast boolean queries

### Text Processing

- **Tokenization**: Unicode-aware text splitting
- **Stemming**: Snowball (Porter2) stemmer for English
- **Stopword Filtering**: Remove common words (the, a, is, etc.)
- **Case Normalization**: Case-insensitive search
- **Configurable Pipeline**: Customize analysis behavior

### Data Structures

- **Skip Lists**: O(log n) search, insert, and delete operations
- **Inverted Index**: Efficient term-to-position mapping
- **Binary Serialization**: Compact storage format

## Not for Everyone

> [!CAUTION]
> Blaze is an educational implementation. For production use, see [Bleve](https://github.com/blevesearch/bleve) - a mature, battle-tested full-text search library.

Blaze focuses on keyword-based full-text search with inverted indexes. If you need semantic search with vector embeddings, [Comet](https://github.com/wizenheimer/comet) ([docs](https://pkg.go.dev/github.com/wizenheimer/comet)) implements various vector indexes (Flat, HNSW, IVF, PQ, IVFPQ) along with hybrid retrieval combining BM25 and vector similarity.

Blaze is purpose-built to be hackable—small enough to understand completely. If you've ever wondered how inverted indexes are structured, how BM25 scoring works, or how boolean queries execute, Blaze provides a readable implementation to learn from.

## Installation

```bash
go get github.com/wizenheimer/blaze