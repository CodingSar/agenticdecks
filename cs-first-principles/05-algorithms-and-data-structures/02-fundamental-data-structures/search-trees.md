# Search Trees

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Fundamental Data Structures](README.md)
> **Builds on:** [Arrays and Linked Lists](arrays-and-linked-lists.md), [Correctness and Invariants](../01-foundations/correctness-and-invariants.md), [Relations and Orders](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md), [Graph Theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md)
> **Enables:** [B-Trees](../../09-data-management/02-storage-and-indexing/b-trees.md), [Searching and Selection](../04-sorting-and-searching/searching-and-selection.md), [Tries and Suffix Structures](../06-string-algorithms/tries-and-suffix-structures.md), [Computational Geometry](../07-advanced-topics/computational-geometry.md)

## Essence

A binary search tree (BST) stores keys in nodes so that, at every node, all keys in the left subtree are smaller and all keys in the right subtree are larger. Searching follows one root-to-leaf path, comparing at each node, so it costs O(height). If the tree stays balanced, height is O(log n) and every dictionary operation is O(log n). Unlike a hash table, a search tree keeps keys in sorted order, so it also answers ordered questions (minimum, successor, range queries, rank) in O(log n + output). The whole design problem is keeping the tree balanced as keys are inserted and deleted in adversarial order.

## Core tenets

1. **The search-tree invariant makes every comparison discard a subtree.** Because left < node < right holds everywhere, comparing the target with a node tells you which subtree could contain it, and the other subtree is eliminated. An in-order traversal visits keys in sorted order, which is why a BST is a dynamic version of a sorted array.

2. **Unbalanced trees degenerate into linked lists.** Inserting keys 1, 2, 3, …, n into a plain BST builds a path of height n, and every operation becomes Θ(n). Random insertion order gives expected height O(log n) (about 4.311 ln n in expectation, Reed 2003), but real data is often sorted or nearly sorted. So production trees enforce balance.

3. **Balanced trees maintain a weaker invariant that still forces logarithmic height.** Perfect balance is too expensive to maintain. Instead: *AVL trees* (Adelson-Velsky and Landis, 1962) keep the heights of sibling subtrees within 1, giving height ≤ about 1.44 log₂ n. *Red–black trees* (Guibas and Sedgewick, 1978) colour nodes so no path is more than twice as long as any other, giving height ≤ 2 log₂(n + 1). Both restore their invariant after each update with O(log n) recolourings and O(1) (red–black) or O(log n) (AVL) rotations.

4. **Rotations restructure locally while preserving order.** A rotation re-hangs three subtrees around two nodes in O(1) time. It changes heights but keeps the in-order sequence identical, so the search invariant survives. Every balanced BST is built from rotations plus a rule for when to apply them.

5. **Ω(log n) comparisons is the floor for comparison-based search.** Any comparison-based search over n keys is a binary decision tree with at least n + 1 outcomes, so its height is at least log₂(n + 1). Balanced BSTs meet this bound up to a constant. Hash tables beat it only by leaving the comparison model.

6. **Wider nodes beat binary nodes when memory is hierarchical.** A binary tree of a million keys has height about 20, and each level may be a cache miss or, on disk, a seek. A *B-tree* stores hundreds of keys per node, one node per disk page or cache-sized block, so height drops to 3 or 4. That is why databases and file systems use B-trees and B+-trees, not red–black trees ([B-trees](../../09-data-management/02-storage-and-indexing/b-trees.md)).

7. **Self-adjusting and randomised trees avoid explicit balance data.** *Splay trees* (Sleator and Tarjan, 1985) move each accessed node to the root by rotations; operations cost O(log n) amortized, and frequently accessed keys become fast. *Treaps* give each key a random priority and keep heap order on priorities, which makes the shape that of a random BST, so expected height is O(log n) for any insertion order. *Skip lists* reach the same expected bounds with layered linked lists.

8. **Augmentation turns a search tree into a query engine.** Store extra data in each node (subtree size, maximum endpoint, sum) and maintain it during rotations. Subtree sizes give order statistics (the k-th smallest key) in O(log n). Interval trees, segment trees and Fenwick trees answer range-sum and overlap queries the same way.

## Key concepts

| Term | Meaning |
|---|---|
| BST invariant | For every node, left-subtree keys < node key < right-subtree keys |
| Height | Length of the longest root-to-leaf path; bounds operation cost |
| Rotation | O(1) local restructuring that preserves in-order sequence |
| AVL tree | BST whose sibling subtree heights differ by at most 1 |
| Red–black tree | BST with node colours ensuring longest path ≤ 2 × shortest |
| B-tree | Balanced multiway tree with large nodes sized to disk or memory blocks |
| Splay tree | Self-adjusting BST with O(log n) amortized operations |
| Augmented tree | Tree storing per-subtree summaries to support extra queries |

## How it fits

- **Below:** the search invariant is a [total order](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md) on keys; trees are [graphs](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md); balance proofs are [invariant](../01-foundations/correctness-and-invariants.md) arguments; the B-tree variant exists because of the [memory hierarchy](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md).
- **Above:** ordered maps in standard libraries (C++ `std::map` and Java `TreeMap` are red–black trees), the Linux scheduler's run queue (a red–black tree keyed by virtual runtime since the Completely Fair Scheduler, see [scheduling](../../07-operating-systems/02-process-management/scheduling.md)), [file system](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md) directories and extents, and database [indexes](../../09-data-management/02-storage-and-indexing/b-trees.md).
- **Siblings:** [hash tables](hash-tables.md) are faster for exact keys but unordered; [heaps](heaps-and-priority-queues.md) keep only enough order to find the minimum; [tries](../06-string-algorithms/tries-and-suffix-structures.md) branch on key digits instead of comparisons.

## Common misconceptions

- **"A BST gives O(log n) operations."** Only a *balanced* one. A plain BST is Θ(n) worst case, and sorted input triggers it.
- **"Red–black trees are the fastest ordered structure."** On modern hardware B-tree-style nodes with many keys per cache line often win, even in memory, because they cause fewer cache misses.
- **"Hash tables make trees obsolete."** Any query involving order (ranges, nearest key, sorted iteration) needs a tree or a sorted structure.

## Go deeper

- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (4th ed., 2022): binary search trees, red–black trees and B-trees chapters.
- Robert Sedgewick and Kevin Wayne, *Algorithms* (4th ed., 2011): left-leaning red–black trees derived from 2-3 trees.
- Daniel D. Sleator and Robert E. Tarjan, "Self-Adjusting Binary Search Trees" (1985): splay trees and their amortized analysis.
- Donald E. Knuth, *The Art of Computer Programming, Vol. 3* (2nd ed., 1998): section 6.2 on tree searching.
