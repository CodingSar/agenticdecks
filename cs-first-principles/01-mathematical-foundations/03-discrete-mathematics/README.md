# Discrete Mathematics

> **Layer:** [01 Mathematical Foundations](../README.md) › Discrete Mathematics
> **Children:** [Combinatorics](combinatorics.md) · [Graph Theory](graph-theory.md) · [Induction and Recurrences](induction-and-recurrences.md) · [Number Theory](number-theory.md)

## What this area is about

Discrete mathematics studies structures made of separate, countable pieces: finite sets, integers, graphs, sequences defined step by step. Computers are discrete machines, with finitely many bits, integer addresses and steps that happen one at a time, so this is the mathematics that describes them most directly. The four children answer four questions every algorithm designer asks: how many cases are there (combinatorics), how are the pieces connected (graph theory), how does a quantity defined in terms of smaller ones behave (induction and recurrences), and what happens when arithmetic wraps around (number theory).

The unifying idea is *reasoning about the unbounded with finite arguments*. A graph may have billions of vertices, a recurrence may run for any *n*, an integer may have thousands of digits; discrete mathematics provides counting rules, structural theorems and inductive proofs that cover every case at once. This is exactly what algorithm analysis needs, which is why [05 Algorithms and Data Structures](../../05-algorithms-and-data-structures/README.md) draws on this area more than on any other.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Combinatorics](combinatorics.md) | Counting: search-space sizes, lower bounds, collisions | Sets, functions |
| [Graph Theory](graph-theory.md) | Connectivity structures: paths, trees, cycles, colourings, flows | Relations, combinatorics |
| [Induction and Recurrences](induction-and-recurrences.md) | Proving claims for all sizes; solving cost equations of recursive algorithms | Proof techniques, well-founded orders |
| [Number Theory](number-theory.md) | Integers, primes and modular arithmetic | Proof techniques, equivalence relations |

Combinatorics and induction are the general-purpose tools; graph theory and number theory are the two great subject areas they are applied to.

```
         combinatorics ◄──────► induction & recurrences
          (how many?)            (for every n; T(n) = aT(n/b) + f(n))
              │      \            /      │
              ▼       \          /       ▼
         graph theory  \        /   number theory
        (connections)   ▼      ▼   (wrap-around arithmetic)
                    algorithms, crypto, coding
```

Counting and recursion are entangled: many counts (binary trees, parse trees, tilings) are defined by recurrences, and recurrences are often solved by counting the nodes of a recursion tree. Graph-theoretic proofs are usually inductions on vertices, edges or path length. Number theory supplies the proof that Euclid's algorithm runs in logarithmic time by induction, and counting arguments (the density of primes, the birthday bound) determine how cryptographic parameters are sized.

## Connections to sibling areas

- **[Logic](../01-logic/README.md):** Proof techniques, especially induction and the pigeonhole principle, are the methods every child uses.
- **[Sets, Relations and Functions](../02-sets-relations-functions/README.md):** Graphs are relations, congruences are equivalences, counting is finite cardinality.
- **[Algebra](../04-algebra/README.md):** [Abstract algebra](../04-algebra/abstract-algebra.md) generalises modular arithmetic into groups and finite fields; [linear algebra](../04-algebra/linear-algebra.md) analyses graphs through adjacency matrices and solves linear recurrences by matrix powers.
- **[Continuous Mathematics](../05-continuous-mathematics/README.md):** Integrals bound discrete sums, and continuous relaxations (linear programming) give bounds on discrete optimisation.
- **[Probability and Statistics](../06-probability-and-statistics/README.md):** Finite probability is counting; random graphs and random hashing join the two.

## Connections across layers

This area feeds [asymptotic analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md) and [complexity](../../02-theory-of-computation/04-complexity/README.md); the [design paradigms](../../05-algorithms-and-data-structures/03-design-paradigms/README.md) and [graph algorithms](../../05-algorithms-and-data-structures/05-graph-algorithms/README.md) of layer 05; machine [integer arithmetic](../../03-digital-logic/01-number-representation/integers-and-twos-complement.md), which is arithmetic modulo 2^w; [routing](../../08-networking/03-network-layer/routing-algorithms.md) and [deadlock detection](../../07-operating-systems/03-concurrency/deadlock.md), which are graph problems; and [public-key cryptography](../../11-security-and-cryptography/02-cryptography/public-key-cryptography.md), which is applied number theory.

## Cross-cutting threads

- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): counting lower bounds (sorting needs about n log n comparisons; no compressor shrinks everything).
- [Recursion and self-reference](../../CROSS-CUTTING.md#recursion-and-self-reference): recurrences and structural induction.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): loop invariants are induction on iterations.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): adjacency lists versus matrices; residues versus integers.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): the birthday bound sets the size of hashes and identifiers.
