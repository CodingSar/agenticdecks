# Union–Find

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Fundamental Data Structures](README.md)
> **Builds on:** [Arrays and Linked Lists](arrays-and-linked-lists.md), [Amortized Analysis](../01-foundations/amortized-analysis.md), [Relations and Orders](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md), [Graph Theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md)
> **Enables:** [Minimum Spanning Trees](../05-graph-algorithms/minimum-spanning-trees.md), [Graph Traversal](../05-graph-algorithms/graph-traversal.md), [Polymorphism and Type Inference](../../06-programming-languages/02-semantics-and-types/polymorphism-and-type-inference.md), [Unsupervised Learning](../../13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md)

## Essence

A union–find (disjoint-set) structure maintains a partition of n elements into disjoint sets under two operations: *find(x)* returns a canonical representative of x's set, and *union(x, y)* merges two sets. It answers "are x and y in the same group?" while groups keep merging, which is exactly what Kruskal's algorithm, incremental connectivity and type unification need. The standard implementation is a *disjoint-set forest*: each set is a tree of parent pointers stored in an array, and the root is the representative. Two cheap rules, *union by rank* (hang the shorter tree under the taller) and *path compression* (point every node on a find path straight at the root), make any sequence of m operations cost O(m·α(n)), where α is the inverse Ackermann function. That bound is not an artefact of the analysis: it is provably the best any structure can do.

## Core tenets

1. **A set is named by its root, so union is one pointer write.** Store `parent[i]` for every element; a root points to itself. find(x) follows parents to the root. union(x, y) finds both roots and makes one the parent of the other. Nothing else moves, which is why merging is cheap. The price is that find must walk a path, so the whole design problem is keeping paths short (Galler and Fischer, 1964).

2. **Naive linking can build a path of length n.** If union always hangs the first root under the second, unions in an unlucky order produce a chain, and each find costs Θ(n). This is the same degeneration as an unbalanced [search tree](search-trees.md), and it has the same cure: a balance rule.

3. **Union by rank or size keeps height O(log n).** Attach the root of smaller rank (an upper bound on height) or smaller size beneath the other. A tree's height grows only when two trees of equal rank merge, and that at least doubles the number of nodes it contains. So a node of rank r roots a subtree of at least 2ʳ nodes, rank never exceeds log₂ n, and find is O(log n) worst case with no other help.

4. **Path compression makes the structure repair itself.** During find(x), after locating the root, reset the parent of every node on the path to the root. The first find on a long path pays for it; later finds through those nodes take one step. One-pass variants, *path halving* and *path splitting* (point each node to its grandparent), give the same bounds without a second pass or recursion. Compression alone, with arbitrary linking, already gives O(log n) amortized cost per operation (Tarjan and van Leeuwen, 1984).

5. **Together they cost O(m·α(n)) amortized, and α(n) ≤ 4 in practice.** Tarjan (1975) proved that m operations on n elements with both rules cost O(m·α(m, n)), improving an earlier O(m log* n) bound (Hopcroft and Ullman, 1973). The inverse Ackermann function α(n) is the smallest k for which the k-th level of the Ackermann hierarchy, applied to 1, reaches n; it exceeds 4 only for n beyond 10⁸⁰, more than the number of atoms in the observable universe. The proof is a potential argument (see [amortized analysis](../01-foundations/amortized-analysis.md)): compression spends potential stored in nodes whose rank is far below their parent's, and the ranks grow so slowly that few such levels exist.

6. **The bound is tight, for this algorithm and for any algorithm.** Tarjan's 1975 paper showed that sequences exist on which union by rank with path compression really does take Θ(m·α(m, n)). Fredman and Saks (1989) then proved, in the cell-probe model, that *every* union–find data structure needs Ω(α(n)) amortized time per operation. Inverse Ackermann is therefore the true complexity of the problem, not a weakness of the proof. It is one of the rare places where a superconstant but practically constant function is exactly right.

7. **It only merges; it never splits.** Union–find answers *incremental* connectivity: edges are added, never removed. It cannot undo a union, enumerate a set's members efficiently, or handle edge deletions. Fully dynamic connectivity, with deletions, needs far more complex structures with polylogarithmic cost per update. When a problem is offline, a common trick is to reverse time so deletions become insertions.

8. **Many problems are "maintain an equivalence relation as facts arrive".** Kruskal's [Minimum Spanning Tree (MST)](../05-graph-algorithms/minimum-spanning-trees.md) algorithm adds an edge only if find(u) ≠ find(v). [Connected components](../05-graph-algorithms/graph-traversal.md) of a graph read as a stream of edges, or of pixels in an image, are union–find runs. Hindley–Milner [type inference](../../06-programming-languages/02-semantics-and-types/polymorphism-and-type-inference.md) unifies type variables by merging equivalence classes. Percolation simulations add open sites one at a time and ask when top and bottom first join (Newman and Ziff, 2000). Single-linkage [clustering](../../13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md) is Kruskal stopped early.

## Key concepts

| Term | Meaning |
|---|---|
| Disjoint-set forest | Each set stored as a tree of parent pointers; the root is the representative |
| find(x) | Follow parent pointers from x to its root |
| union(x, y) | Link the root of one set under the root of the other |
| Rank | Upper bound on a node's height; used to choose which root becomes the child |
| Union by size | Link the smaller set under the larger; same O(log n) height bound as rank |
| Path compression | Repoint every node on a find path directly at the root |
| Path halving / splitting | One-pass compression: point each visited node at its grandparent |
| Inverse Ackermann α(n) | Functional inverse of the Ackermann function; at most 4 for any physically realisable n |

## How it fits

- **Below:** an [equivalence relation is a partition](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md), and union–find is that partition made dynamic; the forest lives in an [array](arrays-and-linked-lists.md) of parent indices; the cost bound is a potential-method [amortized](../01-foundations/amortized-analysis.md) proof.
- **Above:** [Kruskal's algorithm](../05-graph-algorithms/minimum-spanning-trees.md), unification in [type checkers](../../06-programming-languages/02-semantics-and-types/polymorphism-and-type-inference.md) and [Prolog](../../06-programming-languages/01-paradigms/logic-and-declarative.md), register coalescing in [compilers](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md), connected-component labelling in [computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md), and [clustering](../../13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md).
- **Siblings:** like a [heap](heaps-and-priority-queues.md), it keeps a tree in an array and stores only as much order as its query needs; unlike a [search tree](search-trees.md), its trees carry no key order at all, only membership; [hash tables](hash-tables.md) map names to element indices when elements are not already integers.

## Common misconceptions

- **"Union–find is O(1) per operation."** It is O(α(n)) amortized, which is at most 4 in practice but provably not constant; a single find can still take O(log n).
- **"Path compression alone is enough."** It gives logarithmic amortized cost; the inverse-Ackermann bound needs union by rank or size as well.
- **"It can answer any connectivity question."** Only incremental ones; deleting an edge or splitting a set is outside its interface.

## Go deeper

- Robert E. Tarjan, "Efficiency of a Good But Not Linear Set Union Algorithm" (1975): the inverse-Ackermann upper bound and its tightness.
- Robert E. Tarjan and Jan van Leeuwen, "Worst-Case Analysis of Set Union Algorithms" (1984): every combination of linking and compression rules, compared.
- Michael L. Fredman and Michael E. Saks, "The Cell Probe Complexity of Dynamic Data Structures" (1989): the matching lower bound for any structure.
- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (4th ed., 2022): chapter 19, with a full potential-function proof.
