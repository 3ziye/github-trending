# Blaze

<div align="center">
  <img alt="image" src="./media/image.png" />
  <p>
    <a href="https://wizenheimer.github.io/blaze/"><strong>Docs </strong> </a>
  </p>
</div>

**Built for hackers, not hyperscalers.**  
A tiny, hackable full-text search engine you can actually fit in your head. Features inverted indexing, boolean queries, phrase search, proximity queries, and BM25 ranking—powered by a flexible query engine, roaring bitmaps, and skip lists.

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

> **Looking for hybrid search indexes?** Check out [Comet](https://github.com/wizenheimer/comet) - a companion project for hybrid vector search that brings together BM25, Flat, HNSW, IVF, PQ and IVFPQ indexes. It pairs hybrid retrieval with reciprocal rank fusion, autocut, pre-filtering, semantic search, full-text search, and multi-KNN searches, and multi-query operations — all in pure Go.
>
> Understand search internals from the inside out. Built for hackers, not hyperscalers.

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

We'd admit, Blaze isn't for everyone. If you're looking for a production-ready, battle-tested full-text search engine, check out [Bleve](https://github.com/blevesearch/bleve) - a modern, feature-rich indexing library in Go.

If you need **vector search** or **hybrid search** capabilities, check out [Comet](https://github.com/wizenheimer/comet) - **built for hackers, not hyperscalers**. It's a high-performance hybrid vector index written in Go that brings together multiple indexing strategies and search modalities. Comet supports:

- **Multiple Index Types**: Flat (exact), HNSW (graph), IVF (clustering), PQ (quantization), and IVFPQ (hybrid)
- **Full-Text Search**: BM25 ranking with tokenization and normalization
- **Metadata Filtering**: Fast filtering using Roaring Bitmaps and Bit-Sliced Indexes
- **Hybrid Retrieval**: Reciprocal Rank Fusion, semantic search, multi-KNN, and multi-query operations
- **Advanced Features**: Quantization, reranking, autocut, pre-filtering, soft d