<!---
  Copyright 2024-present Alibaba Inc.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->

# Paimon C++

Paimon C++ is a high-performance C++ implementation of [Apache Paimon](https://paimon.apache.org). Paimon C++ aims to provide a native, high-performance and extensible implementation that allows native engines to access the Paimon datalake format with maximum efficiency.

## What's in the Paimon C++ library

* Write: Paimon append table and primary key table write (without compaction).
* Commit: Paimon append table commit. (Note: Limited support — only works for simple append-only tables; table with compaction, index, changelog, and stats are not supported.)
* Scan: Paimon append and primary key table batch and stream scan (without changelog).
* Read: Paimon append table read and primary key table with deletion vector read (raw read) and primary key table with merge on read (merge read).
* Batch read and write interface using the [Arrow Columnar In-Memory Format](https://arrow.apache.org) to increase throughput.
* IO interfaces to file system and built-in local and jindo file system implementation.
* File format interfaces to customize different format and built-in orc, parquet and lance format implementation.
* Memory pool interfaces and a default implementation.
* Thread pool executor interfaces and a default implementation.
* Compatible with Java Paimon format and communication protocol (e.g., commit message, data splits, manifests).
* Note: The current implementation only supports the x86_64 architecture.

## Write And Commit Example

The writing is divided into two stages:

1. Write records: write records in distributed tasks, generate commit messages.
2. Commit/Abort: collect all commit messages, commit them in a global node ('Coordinator', or named 'Driver', or named 'Committer'). When the commit fails for certain reason, abort unsuccessful commit via commit messages.


```c++
    std::string table_path = "/tmp/paimon/my.db/test_table/";
    WriteContextBuilder context_builder(table_path, "commit_user");
    PAIMON_ASSIGN_OR_RAISE(std::unique_ptr<WriteContext> write_context,
                           context_builder.AddOption(Options::TARGET_FILE_SIZE, "1024mb")
                               .AddOption(Options::FILE_SYSTEM, "local")
                               .Finish());
    PAIMON_ASSIGN_OR_RAISE(std::unique_ptr<FileStoreWrite> file_store_write,
                           FileStoreWrite::Create(std::move(write_context)));

    ::ArrowArray arrow_array;
    // prepare your arrow array
    // ...
    RecordBatchBuilder batch_builder(&arrow_array);
    batch_builder.SetPartition({{"col1", "20240813"}, {"col2", "23"}}).SetBucket(1);
    PAIMON_ASSIGN_OR_RAISE(std::shared_ptr<RecordBatch> batch, batch_builder.Finish());
    PAIMON_RETURN_NOT_OK(file_store_write->Write(batch));
    PAIMON_ASSIGN_OR_RAISE(std::vector<std::shared_ptr<CommitMessage>> commit_messages,
                           file_store_write->PrepareCommit());

    CommitContextBuilder commit_context_builder(table_path, "commit_user");
    PAIMON_ASSIGN_OR_RAISE(std::unique_ptr<CommitContext> commit_context,
                           commit_context_builder.AddOption(Options::MANIFEST_TARGET_FILE_SIZE, "8mb")
                               .AddOption(Options::FILE_SYSTEM, "local")
                               .IgnoreEmptyCommit(false)
                               .Finish());
    PAIMON_ASSIGN_OR_RAISE(std::unique_ptr<FileStoreCommit> commit, FileStoreCommit::Create(std::move(commit_context)));
    PAIMON_RETURN_NOT_OK(commit->Commit(commit_messages));

```

## Scan and Read Example

The reading is divided into two stages:

1. Scan: read snapshot, parse manifests, filter target file set by statistical information, and generate query plan data splits.
2. Read: read the data files according to data splits, and perform schema evolution adjustment and predicate push-down optimization.

```c++
    std::string table_path = "/tmp/paimon/my.db/test_table/";
    ScanContextBuilder context_builder(table_path);
    // prepare predicate if needed
    std::shared_ptr<Predicate> predicate = PredicateBuilder::GreaterThan(/*field_index=*/0, /*field_name=*/"f0",
                               /*field_type=*/FieldType::INT, Literal(10));
    PAIMON_ASSIGN_OR_RAISE(std::unique_ptr<ScanContext> scan_context,
                           context_builder.SetPredicate(predicate)
                               .AddOption(Options::SCAN_SNAPSHOT_ID, "2")
           