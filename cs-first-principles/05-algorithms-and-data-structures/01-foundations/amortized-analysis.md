# Amortized Analysis

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Foundations](README.md)
> **Builds on:** [Models of Computation](models-of-computation.md), [Correctness and Invariants](correctness-and-invariants.md), [Induction and Recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md)
> **Enables:** [Arrays and Linked Lists](../02-fundamental-data-structures/arrays-and-linked-lists.md), [Hash Tables](../02-fundamental-data-structures/hash-tables.md), [Union–Find](../02-fundamental-data-structures/union-find.md), [LSM-Trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md), [Memory Management and Garbage Collection](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md)

## Essence

Some data structures do a little work most of the time and a lot of work occasionally. A dynamic array appends in O(1) until it fills, then copies everything. Worst-case analysis per operation would call append O(n), which badly overstates the cost of a long sequence. Amortized analysis bounds the *total* cost of any sequence of m operations, then divides by m. It is still a worst-case guarantee, over sequences rather than single operations, and needs no probability. The core idea: cheap operations pre-pay for the expensive ones, and an invariant ensures the prepaid credit never runs out.

## Core tenets

1. **Amortized cost is a worst-case bound on sequences, not an average over inputs.** If every sequence of m operations costs at most m·c, each operation has amortized cost c. There is no assumption about which inputs are likely. This makes it as strong as worst-case analysis for any program that performs many operations, which is nearly every program that uses a data structure.

2. **Aggregate method: count the whole sequence directly.** For a dynamic array that doubles when full, n appends trigger copies of sizes 1, 2, 4, …, up to n, totalling less than 2n. Add the n ordinary writes and the total is under 3n, so append is O(1) amortized. The geometric growth is essential: growing by a fixed amount (say +100 slots) gives Θ(n²) total copying and Θ(n) amortized.

3. **Accounting method: charge each operation a fixed fee and bank the surplus.** Charge each append 3 units: 1 pays for the write, 2 are stored as credit on the new element. When the array doubles from k to 2k, the k/2 elements added since the last doubling each hold 2 credits, which pay for copying all k elements. The invariant "bank balance ≥ 0" proves the fee covers everything.

4. **Potential method: store credit as a function of the state.** Define a potential Φ(state) ≥ Φ(initial). Amortized cost = actual cost + ΔΦ. Summed over a sequence, the potentials telescope, so total actual cost ≤ total amortized cost. For the dynamic array, Φ = 2·size − capacity works. The art is choosing Φ so expensive operations release potential that cheap ones built up. This method proves splay trees, Fibonacci heaps and union–find bounds.

5. **Amortized bounds can be astonishingly small.** [Union–find](../02-fundamental-data-structures/union-find.md) with union by rank and path compression runs m operations on n elements in O(m·α(n)) time, where α is the inverse Ackermann function, at most 4 for any n that fits in the physical universe (Tarjan, 1975); Fredman and Saks (1989) proved no structure can do asymptotically better. Fibonacci heaps give O(1) amortized decrease-key, which improves Dijkstra's algorithm to O(m + n log n). Splay trees give O(log n) amortized search with no balance information stored.

6. **Amortized guarantees do not bound individual latency.** A dynamic array resize, a hash table rehash, a garbage-collection pause or a Log-Structured Merge (LSM) tree compaction can stall one operation for a long time. Real-time and interactive systems care about the worst single operation (tail latency), so they use *de-amortized* variants that spread the expensive work incrementally (incremental rehashing, incremental or concurrent garbage collection).

7. **Persistence and backtracking can break amortization.** Amortized arguments assume the credit is spent once. If a program can rewind to an old state (a persistent data structure, or undo) and repeat an expensive operation, the same credit is spent many times. Okasaki showed how lazy evaluation with memoization restores amortized bounds in purely functional structures.

## Key concepts

| Term | Meaning |
|---|---|
| Amortized cost | An upper bound c such that any sequence of m operations costs at most m·c in total |
| Aggregate method | Bound total cost of n operations directly, divide by n |
| Accounting method | Assign fixed charges; overcharges are stored as credit on parts of the structure |
| Potential function Φ | Non-negative function of state; amortized cost = actual + ΔΦ |
| Geometric resizing | Grow capacity by a constant factor (often 1.5 or 2) so copying cost sums to O(n) |
| Inverse Ackermann α(n) | An extremely slow-growing function; α(n) ≤ 4 for all practical n |
| De-amortization | Spread expensive work over many operations to bound each operation's cost |

## How it fits

- **Below:** uses the Random Access Machine (RAM) cost model from [models of computation](models-of-computation.md) and the telescoping sums of [recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md).
- **Above:** justifies standard-library containers in every language, [garbage collector](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md) cost analysis, [LSM-tree](../../09-data-management/02-storage-and-indexing/lsm-trees.md) compaction, and [Transmission Control Protocol (TCP)](../../08-networking/04-transport-layer/udp-and-tcp.md) buffer growth. The same idea, applied to fixed overheads instead of credit, is [batching](../../CROSS-CUTTING.md#batching-and-amortization).
- **Siblings:** an amortized proof is an [invariant proof](correctness-and-invariants.md) where the invariant is "credit ≥ 0". It is distinct from expected-time analysis in [randomized algorithms](../03-design-paradigms/randomized-algorithms.md), which averages over coin flips.

## Common misconceptions

- **"Amortized means average case."** Average case assumes a distribution over inputs. Amortized assumes nothing; it bounds the worst sequence.
- **"O(1) amortized means every call is fast."** One call can be Θ(n). If you need bounded latency per call, you need a de-amortized design.
- **"Any growth factor works."** Additive growth gives quadratic total cost. Only multiplicative growth gives O(1) amortized append. Shrinking also needs care: halving when half-empty can thrash at the boundary; shrink at one-quarter full instead.

## Go deeper

- Robert E. Tarjan, "Amortized Computational Complexity" (1985): the paper that named and systematised the potential method.
- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (4th ed., 2022): chapter 16 on aggregate, accounting and potential methods.
- Chris Okasaki, *Purely Functional Data Structures* (1998): amortization under persistence.
