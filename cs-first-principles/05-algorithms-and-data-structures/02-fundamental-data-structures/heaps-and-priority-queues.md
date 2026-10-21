# Heaps and Priority Queues

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Fundamental Data Structures](README.md)
> **Builds on:** [Arrays and Linked Lists](arrays-and-linked-lists.md), [Correctness and Invariants](../01-foundations/correctness-and-invariants.md), [Amortized Analysis](../01-foundations/amortized-analysis.md)
> **Enables:** [Shortest Paths](../05-graph-algorithms/shortest-paths.md), [Minimum Spanning Trees](../05-graph-algorithms/minimum-spanning-trees.md), [Comparison Sorting](../04-sorting-and-searching/comparison-sorting.md), [Scheduling](../../07-operating-systems/02-process-management/scheduling.md), [Search and Planning](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md)

## Essence

A priority queue holds items with priorities and supports insert and extract-min (or extract-max): always remove the most urgent item. The standard implementation is the *binary heap*, a complete binary tree stored in an array, where every parent's key is no larger than its children's (the heap property). That partial order is just enough to put the minimum at the root, and it is cheap to restore after a change: O(log n) for insert and extract-min, O(1) to peek. Because the tree is complete, it needs no pointers: the children of index i are at 2i + 1 and 2i + 2. Priority queues are the engine of Dijkstra's and Prim's algorithms, event simulation, schedulers, and best-first search.

## Core tenets

1. **A heap keeps only the order it needs.** A sorted array or search tree knows the full order and pays O(log n) or O(n) per update to keep it. A heap only guarantees that each parent beats its children. This weaker invariant is enough to find the minimum (the root) and much cheaper to maintain: building a heap from n items takes O(n), whereas sorting needs Ω(n log n) comparisons.

2. **The complete-tree shape makes the array layout implicit.** A heap fills levels left to right, so it has height ⌊log₂ n⌋ and no gaps. Store level by level in an array: parent of i is ⌊(i − 1)/2⌋. No pointers means less memory and better cache use than any linked tree.

3. **Insert sifts up; extract-min sifts down.** To insert, put the item at the end and swap it with its parent while it is smaller: at most height = O(log n) swaps. To extract the minimum, take the root, move the last item to the root, and swap it with its smaller child until the heap property holds: O(log n). Each operation repairs the invariant along a single root-to-leaf path.

4. **Bottom-up heap construction is O(n), not O(n log n).** Sift down every internal node from the last to the first. Half the nodes are leaves (no work), a quarter sift down at most 1 level, an eighth at most 2, and so on. The sum Σ h·n/2^(h+1) converges to O(n) (Floyd, 1964). This is a standard example where the naive bound (n operations × log n each) is loose.

5. **Heapsort sorts in place in O(n log n) worst case.** Build a max-heap, then repeatedly swap the root with the last element and shrink the heap. It uses O(1) extra space and has no bad inputs, unlike quicksort. In practice it is slower than quicksort because sift-down jumps between distant array positions, causing cache misses, and its branches are hard to predict. Introsort (the basis of C++ `std::sort` implementations) falls back to heapsort only when quicksort's recursion gets too deep.

6. **Decrease-key is what graph algorithms need, and fancier heaps make it cheaper.** Dijkstra and Prim repeatedly lower a vertex's tentative distance. In a binary heap decrease-key is O(log n) (sift up, given a position index), so Dijkstra runs in O((n + m) log n). A Fibonacci heap (Fredman and Tarjan, 1987) makes decrease-key O(1) amortized and extract-min O(log n) amortized, improving Dijkstra to O(m + n log n). In practice Fibonacci heaps are usually slower because of pointer overhead and large constants; binary or 4-ary heaps, often with "lazy deletion" (insert duplicates, skip stale entries), win on real graphs.

7. **Priority queues cannot beat sorting.** Inserting n items and extracting them all yields sorted order, so any comparison-based priority queue must spend Ω(n log n) comparisons on that sequence. Hence one of insert or extract-min must cost Ω(log n) amortized. Integer priorities escape this bound: bucket queues and radix heaps give near-constant operations when priorities are small integers.

8. **Many variants trade features for constants.** d-ary heaps (d children per node) make the tree shallower, speeding insert and decrease-key at the cost of slower extract-min. Pairing heaps are simple and fast in practice. Mergeable heaps (binomial, leftist, skew) support union in O(log n). Indexed heaps track each item's position to support decrease-key and delete.

## Key concepts

| Term | Meaning |
|---|---|
| Priority queue | Abstract type: insert, extract-min (or max), peek, often decrease-key |
| Heap property | Each node's key ≤ its children's keys (min-heap) |
| Complete binary tree | All levels full except possibly the last, filled left to right |
| Sift up / sift down | Swap a node with parent / smaller child until the heap property holds |
| Heapify (build-heap) | Turn an arbitrary array into a heap in O(n) |
| Heapsort | In-place O(n log n) sort using a max-heap |
| Decrease-key | Lower an existing item's priority; central to Dijkstra and Prim |
| Fibonacci heap | Heap with O(1) amortized insert and decrease-key |

## How it fits

- **Below:** the implicit layout relies on O(1) [array](arrays-and-linked-lists.md) indexing; build-heap's O(n) bound is a geometric sum from [recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md).
- **Above:** Operating System (OS) [schedulers](../../07-operating-systems/02-process-management/scheduling.md) and timer wheels, [discrete-event simulators](../../08-networking/01-principles/latency-bandwidth-and-queueing.md), [A\* search](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md), Huffman coding in [compression](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md), top-k queries in [databases](../../09-data-management/03-query-processing/query-optimization.md), and k-way merging in [external sorting](../07-advanced-topics/external-memory-and-cache-oblivious.md).
- **Siblings:** a [queue](stacks-and-queues.md) is a priority queue where priority is arrival time; a [search tree](search-trees.md) can serve as a priority queue but keeps more order than needed and costs more.

## Common misconceptions

- **"A heap is sorted."** Only along each root-to-leaf path. Siblings and cousins are in no particular order.
- **"Building a heap is O(n log n)."** Bottom-up construction is O(n). Inserting one at a time is O(n log n) worst case.
- **"Fibonacci heaps make Dijkstra faster in practice."** They improve the asymptotic bound, but binary heaps are usually faster for real graph sizes.

## Go deeper

- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (4th ed., 2022): heapsort chapter and the O(n) build-heap proof.
- J. W. J. Williams, "Algorithm 232: Heapsort" (1964): the original binary heap.
- Michael L. Fredman and Robert E. Tarjan, "Fibonacci Heaps and Their Uses in Improved Network Optimization Algorithms" (1987).
