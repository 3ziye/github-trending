<!--
Copyright 2025 XTX Markets Technologies Limited

SPDX-License-Identifier: GPL-2.0-or-later
-->

[![TernFS Logo](https://github.com/user-attachments/assets/03c2f7f9-649f-4411-9cd9-e375ff97e3b4 "TernFS Logo")](https://ternfs.com)


A distributed file system. For a high-level description of TernFS, see [the TernFS blog post on the XTX Markets Tech Blog](https://xtxmarkets.com/tech/2025-ternfs). This document provides a more bare-bones overview and an introduction to the codebase.

## Goals

The target use case for TernFS is the kind of machine learning we do at XTX: reading and writing large immutable files. By "immutable" we mean files that do not need modifying after they are first created. By "large" we mean that most of the storage space will be taken up by files bigger than a few MBs.

We don't expect new directories to be created often, and files (or directories) to be moved between directories often. In terms of numbers, we expect the upper bound for TernFS to roughly be the upper bound for the data we're planning for a single data center:

- 10EB of logical file storage (i.e. if you sum all file sizes = 10EB)
- 1 trillion files -- average ~10MB file size
- 100 billion directories -- average ~10 files per directory
- 1 million clients

We want to drive the filesystem with commodity hardware and Ethernet networking.

We want the system to be robust in various ways:

* Witnessing half-written files should be impossible -- a file is fully written by the writer or not readable by other clients
* Power loss or similar failure of storage or metadata nodes should not result in a corrupted filesystem (be it metadata or filesystem corruption)
* Corrupted reads due to hard drives bitrot should be exceedingly unlikely
* Data loss should be exceedingly unlikely, unless we suffer a datacenter-wide catastrophic event (fire, flooding, datacenter-wide vibration, etc.)
* The filesystem should keep working through maintenance or failure of metadata or storage nodes

We also want to be able to restore deleted files or directories, using a configurable "permanent deletion" policy.

Finally, we want to have the option to replicate TernFS to multiple regions, to be able to scale up compute across multiple data centres, and to remove any single data centre as a point of failure.

## Components

```                                   
 A ──► B means "A sends requests to B" 
                                       
                                       
 ┌────────────────┐                    
 │ Metadata Shard ◄─────────┐          
 └─┬────▲─────────┘         │          
   │    │                   │          
   │    │                   │          
   │ ┌──┴──┐                │          
   │ │ CDC ◄──────────┐     │          
   │ └──┬──┘          │     │          
   │    │             │ ┌───┴────┐     
   │    │             └─┤        │     
 ┌─▼────▼────┐          │ Client │     
 │ Registry  ◄──────────┤        │     
 └──────▲────┘          └─┬──────┘     
        │                 │            
        │                 │            
 ┌──────┴────────┐        │            
 │ Block Service ◄────────┘            
 └───────────────┘                     
```

* **servers**
  * **registry**
    * 1 logical instance
    * `ternregistry`, C++ binary
    * TCP bincode req/resp
    * UDP replication
    * stores metadata about a specific TernFS deployment
      * shard/cdc addresses
      * block services addresses and storage statistics
    * state persisted through RocksDB with 5-node distributed consensus through LogsDB
  * **filesystem data**
    * **metadata**
      * **shard**
        * 256 logical instances
        * `ternshard`, C++ binary
        * stores all metadata for the filesystem
          * file attributes (size, mtime, atime)
          * directory attributes (mtime)
          * directories listings (includes file/directory names)
          * file to blocks mapping
          * block service to file mapping
        * UDP bincode req/resp
        * state persisted through RocksDB with 5-node distributed consensus through LogsDB
        * communicates with registry to fetch block services, register itself, insert statistics
    * **CDC**
      * 1 logical instance
      * `terncdc`, C++ binary
      * coordinates actions which span multiple directories
        * create directory
        * remove directory
        * move file or directory between from one directory to the other
        * "Cross Directory Coordinator"
      * UDP bincode req/resp
      * very little state required
        * information about which transactions are currently being executed and which are queued (currently transactions are executed serially)
        * directory -> parent directory mapping to perform "no loops" checks
      * state persisted through RocksDB with 5-node distributed consensus through LogsDB
      * communicates with the shards to perform the cross-directory actions
      * communicates with registry to register itself