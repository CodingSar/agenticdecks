# Arrays and Linked Lists

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Fundamental Data Structures](README.md)
> **Builds on:** [Models of Computation](../01-foundations/models-of-computation.md), [Amortized Analysis](../01-foundations/amortized-analysis.md), [Instruction Encoding and Addressing](../../04-computer-architecture/01-instruction-set-architecture/instruction-encoding-and-addressing.md), [Locality and Caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md)
> **Enables:** [Stacks and Queues](stacks-and-queues.md), [Hash Tables](hash-tables.md), [Heaps and Priority Queues](heaps-and-priority-queues.md), [Memory Allocation](../../07-operating-systems/04-memory-management/memory-allocation.md)

## Essence

There are only two ways to organise a sequence in memory. An **array** puts elements in consecutive addresses, so the address of element i is `base + i × size`, computed in one step. A **linked list** puts each element in its own node with a pointer to the next, so nodes can live anywhere and be spliced in or out by rewriting pointers. Arrays give O(1) random access and excellent cache behaviour but O(n) insertion in the middle. Linked lists give O(1) insertion and deletion at a known node but O(n) access by position and poor cache behaviour. Every other data structure is built from one or both.

## Core tenets

1. **Array indexing is O(1) because address arithmetic is O(1).** The hardware computes `base + i × size` with a multiply (often a shift) and an add, usually folded into a single load instruction's addressing mode. This is the Random Access Machine (RAM) model's unit-cost random access made concrete, and it is why arrays underpin hash tables, heaps, matrices and nearly every fast structure.

2. **Inserting into the middle of an array costs O(n) because order is position.** To insert at index i, every element after i must shift one slot right. Deleting shifts them left. Appending at the end is the exception: it costs O(1) if there is spare capacity.

3. **Dynamic arrays get O(1) amortized append by growing geometrically.** When full, allocate a new block of c × capacity (c is commonly 1.5 or 2) and copy. Copies total O(n) over n appends, so each append costs O(1) amortized ([amortized analysis](../01-foundations/amortized-analysis.md)). This is `std::vector`, Java's `ArrayList`, Python's `list` and Go's slices. The price is up to (c − 1)/c wasted capacity and an occasional Θ(n) pause.

4. **Linked lists trade access speed for cheap splicing.** Given a pointer to a node, inserting after it or (in a doubly linked list) deleting it is O(1): rewrite two to four pointers. But reaching the i-th node requires following i pointers, so access by position and search are O(n). Linked lists shine when you already hold the node: Least Recently Used (LRU) caches pair a hash table with a doubly linked list for exactly this reason.

5. **Cache behaviour, not asymptotics, often decides between them.** A cache line is typically 64 bytes, so scanning an array of 4-byte integers loads 16 elements per memory access, and the hardware prefetcher fetches ahead. Following a linked list costs one potential cache miss (~100 ns from Dynamic Random-Access Memory (DRAM)) per node, and the next address is unknown until the current load completes, so the misses cannot overlap. In practice an O(n) shift in a contiguous array often beats an O(1) linked-list insert for lists of thousands of elements, because the search to find the insertion point is itself O(n) and runs far faster over an array.

6. **Pointers cost memory.** A singly linked list of 4-byte integers on a 64-bit machine stores an 8-byte pointer per element, plus allocator headers, often tripling or quadrupling memory use. Arrays store only the data. This overhead matters for cache capacity as much as for total memory.

7. **Multi-dimensional arrays have a layout, and the layout must match the traversal.** A 2D array in row-major order (C, Python's NumPy default) stores rows contiguously; column-major (Fortran, MATLAB) stores columns contiguously. Traversing against the layout strides through memory and can be ten times slower for large matrices. Blocked (tiled) layouts and loop tiling exist to fix this.

8. **Variants mix the two.** Circular buffers give O(1) operations at both ends of an array. Unrolled linked lists store small arrays in each node. Skip lists add layers of forward pointers to linked lists for O(log n) expected search. Gap buffers (used in text editors) keep a hole at the cursor so local edits are O(1).

## Key concepts

| Term | Meaning |
|---|---|
| Array | Fixed-size block of equal-sized elements at consecutive addresses |
| Dynamic array | Array that resizes by a constant factor when full |
| Capacity vs length | Allocated slots vs slots in use |
| Singly / doubly linked list | Nodes with a next pointer / next and previous pointers |
| Sentinel node | A dummy head or tail node that removes special cases for empty lists and ends |
| Spatial locality | Accessing addresses near recent ones; arrays have it, scattered nodes do not |
| Row-major / column-major | Storing a 2D array row by row / column by column |
| Intrusive list | Link fields embedded in the element itself, as in operating-system kernels |

## How it fits

- **Below:** array indexing relies on the [addressing modes](../../04-computer-architecture/01-instruction-set-architecture/instruction-encoding-and-addressing.md) of the Instruction Set Architecture (ISA); the speed gap between them comes from [caches](../../04-computer-architecture/03-memory-hierarchy/cache-design.md) and prefetching.
- **Above:** [memory allocators](../../07-operating-systems/04-memory-management/memory-allocation.md) keep free lists; kernels use intrusive doubly linked lists for run queues; [column stores](../../09-data-management/02-storage-and-indexing/storage-layouts.md) are arrays per attribute chosen for scan speed; [tensors](../../13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md) are strided multi-dimensional arrays.
- **Siblings:** [stacks and queues](stacks-and-queues.md) are thin interfaces over either; [hash tables](hash-tables.md) are arrays of buckets; [heaps](heaps-and-priority-queues.md) are trees stored implicitly in arrays; [search trees](search-trees.md) are linked structures.

## Common misconceptions

- **"Linked lists are faster for insertion."** Only if you already hold a pointer to the position. Finding the position is O(n), and with caches the array version is often faster overall.
- **"Dynamic array append is O(1)."** It is O(1) *amortized*. A single append can take Θ(n) when the array resizes.
- **"Memory access is uniform cost."** Sequential access through an array can be one to two orders of magnitude faster per element than random pointer chasing.

## Go deeper

- Donald E. Knuth, *The Art of Computer Programming, Vol. 1: Fundamental Algorithms* (3rd ed., 1997): section 2.2 on linear lists, sequential and linked allocation.
- Ulrich Drepper, "What Every Programmer Should Know About Memory" (2007): why access patterns dominate data-structure speed.
- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (4th ed., 2022): elementary data structures chapter.
