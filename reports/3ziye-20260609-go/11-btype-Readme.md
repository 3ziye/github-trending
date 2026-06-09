<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/.github/logo-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="/.github/logo-light.png">
  <img alt="Tile38" src="/.github/images/logo-light.png" width="640">
</picture>
<br>
<a href="#map">Map</a> •
<a href="#set">Set</a> •
<a href="#array">Array</a> •
<a href="#table">Table</a> •
<a href="#stack">Stack</a> •
<a href="#queue">Queue</a> • 
<a href="#deque">Deque</a> •
<a href="#prique">Prique</a>
<br>
<br>
<a href="https://godoc.org/github.com/tidwall/btype"
><img src="https://godoc.org/github.com/tidwall/btree?status.svg"
></a>
</p>

The btype package provides btree based collection types that allow Go programmers 
to easily implement common data structures like maps, arrays, queues, and stacks. 

It's hand-crafted with performance in mind and is generally faster than the 
state of the art btrees for Go, Rust, and C++.
[google/btree](https://github.com/google/btree), 
[tidwall/btree](https://github.com/tidwall/btree), 
[rust/BTreeMap](https://doc.rust-lang.org/std/collections/struct.BTreeMap.html), 
[frozenca/btree](https://github.com/frozenca/BTree).
<sup>[[benchmarks]](#performance)</sup>

# Features

- Includes collections types: map, set, queue, stack, table. Each backed by a btree structure.
- Modern Go ergonomics with a friendly API.
- All data operations are O(log n) complexity.
- Instant [copy-on-write](#copy-on-write) (shadow clones), providing O(1) snapshots.
- Uses [btree counting](https://www.chiark.greenend.org.uk/~sgtatham/algorithms/cbtree.html) for O(log n) random access.
- Exhaustively tested code with 100% coverage.
- Optimized for [high performance](#performance) and low memory.

# Types

Includes the following collection types:

- [`Map`](#map): Key value pairs. Sorting ordered by key
- [`Set`](#set): Like Map, but only for storing keys. No values
- [`Array`](#array): Dynamic array of unsorted data
- [`Table`](#table): Data sorted by key fields or a custom compare function
- [`Stack`](#stack): LIFO (last-in, first-out) data structure
- [`Queue`](#queue): FIFO (first-in, first-out) data structure
- [`Deque`](#deque): Double-ended queue
- [`Prique`](#prique): Priority queue


## Map

btype.Map is a sorted associative collection of key-value pairs with unique keys. 
The keys adhere to the parameter type [`cmp.Ordered`](https://pkg.go.dev/cmp#Ordered) and are naturally sorted using [`cmp.Compare`](https://pkg.go.dev/cmp#Compare).

### Operations

```py
Insert(key, val)        # Insert an item. (does not replace if already exists)
Replace(key, val)       # Replace an existing item. (does not insert if not exists)
Set(key, val)           # Insert or replace an item.
Get(key, val)           # Get an existing item.
Contains(key)           # Test if an item exists.
Delete(key)             # Remove an item.

Seek(key)               # Searches for the first item that is >= to key.
SeekNext(key)           # Searches for the first item that is > key.
SeekPrev(key)           # Searches for the first item that is < key.

All()                   # Iterate items in ascending order.            (iter.Seq2[K,V])
Backward()              # Iterate items in descending order.           (iter.Seq2[K,V])
Ascend(key)             # Iterate items in ascending order >= to key.  (iter.Seq2[K,V])
Descend(key)            # Iterate items in descending order <= to key. (iter.Seq2[K,V])
Keys()                  # Iterate key only in ascending order.         (iter.Seq[K])
Values()                # Iterate values only in ascending order.      (iter.Seq[K])
Drain()                 # Iterate and remove in ascending order.       (iter.Seq2[K,V])
DrainBackward()         # Iterate and remove in descending order.      (iter.Seq2[K,V])

PushFront(key, val)     # Insert item to front of map.
PushBack(key, val)      # Insert item to back of map.
PopFront()              # Remove the first item.
PopBack()               # Remove the last item.
Front()                 # Get the first item.
Back()                  # Get the last item.

InsertAt(i, key, val)   # Inserts item at index. (collection size grows by one)
ReplaceAt(i, key, val)  # Replace an item at index.
GetAt(i)                # Get an item at index.
IndexOf(key)            # Get the index of an item.
DeleteAt(i)             # Remove an item at index.
AscendAt(i)             # Iterate items in ascending order >= to index.  (iter.Seq2[K,V])
DescendAt(i)            # Iterate items in descending order <= to index. (iter.Seq2[K,V])

DeleteRange(min, max)   # Remove items within the provided sub-range. [min,max)
DeleteRangeAt(i, count) # Remove items starting at index.

Len()                   # Get the number of items in map.
Copy()                  # Copy map, fast O(1), uses Copy-on-write shadow cloning.
Clear()                 # Remove all items from map
Release()               # Same as Clear() but optimized for copied collections.
```

### Example

```go
package main

import 