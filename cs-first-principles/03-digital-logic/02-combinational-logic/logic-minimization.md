# Logic Minimization

> **Layer:** [03 Digital Logic](../README.md) › [Combinational Logic](README.md)
> **Builds on:** [Logic Gates](logic-gates.md), [Boolean Algebra](../../01-mathematical-foundations/04-algebra/boolean-algebra.md), [P, NP and NP-Completeness](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md)
> **Enables:** [Hardware Description Languages](../04-hardware-design/hardware-description-languages.md), [FPGA and ASIC](../04-hardware-design/fpga-and-asic.md), [Model Checking](../../06-programming-languages/05-formal-methods/model-checking.md)

## Essence

Any Boolean function can be built directly from its truth table, but the direct circuit is usually far larger and slower than necessary. Logic minimisation finds an equivalent circuit that costs less: fewer gates, fewer literals, less depth, less power. For two-level circuits (an OR of ANDs) the problem is well understood: the answer is a minimum cover of the function's ones by "prime implicants", found by hand with Karnaugh maps or by algorithm with Quine-McCluskey. Exact minimisation is computationally hard, so real tools use heuristics such as Espresso and, for multi-level logic, algebraic restructuring and graph representations such as Binary Decision Diagrams (BDDs). Today minimisation is one stage of logic synthesis, aimed at delay, area and power rather than gate count alone.

## Core tenets

1. **Every function has a canonical sum-of-products form, which is usually wasteful.** Writing one AND term (minterm) for each input combination where the output is 1, and ORing them, implements any function. For `n` inputs there can be up to `2ⁿ` minterms of `n` literals each. Minimisation exploits the identity `xy + x¬y = x`: two terms that differ in one variable merge into a smaller term.

2. **Prime implicants are the building blocks of a minimum two-level circuit.** An implicant is a product term that implies the function (is 1 only where the function is 1). A prime implicant cannot be enlarged by dropping a literal. Every minimum sum-of-products uses only prime implicants, so minimisation reduces to choosing the cheapest set of primes that together cover every 1 of the function: a set cover problem.

3. **Karnaugh maps make merging visible for small functions.** A Karnaugh map (Maurice Karnaugh, 1953) arranges the truth table in a grid ordered by Gray code, so adjacent cells differ in one variable and mergeable terms appear as rectangles of size 1, 2, 4, 8 (wrapping at edges). Circling the largest rectangles that cover all ones gives a minimal expression. It works well up to about four to six variables, beyond which the geometry is unmanageable.

4. **Quine-McCluskey systematises the same idea, at exponential cost.** The Quine-McCluskey method (1950s) tabulates minterms, repeatedly merges terms differing in one bit to generate all prime implicants, and then solves the covering problem. It is exact but the number of primes can grow exponentially in `n`, and the covering step is NP-hard. Exact two-level minimisation is therefore infeasible for large functions.

5. **Don't-care conditions are free optimisation.** When some input combinations can never occur, or their output does not matter (for example, invalid codes in a decoder), the minimiser may assign whichever output yields the simplest circuit. Capturing don't-cares from the surrounding design often saves more than any clever algorithm.

6. **Practical tools use heuristics and multi-level logic.** Espresso (Brayton and colleagues, 1980s) iteratively expands, reduces and makes irredundant a cover, giving near-minimal two-level results quickly. Real chips use multi-level logic, factoring shared subexpressions (`ab + ac = a(b + c)`), which can be much smaller than any two-level form. Synthesis tools then perform technology mapping: covering the optimised logic with the cells actually available in the library.

7. **Canonical graph forms make equivalence checkable.** A Reduced Ordered Binary Decision Diagram (Randal Bryant, 1986) represents a function as a directed acyclic graph that is unique for a given variable order, so two circuits are equivalent exactly when their diagrams are identical. Diagram size can be exponential for some functions (multipliers) and depends heavily on variable order, but for many control functions it is compact. BDDs and Boolean satisfiability (SAT) solvers underpin equivalence checking and model checking.

8. **The cost function is not gate count any more.** Modern minimisation trades area against delay (depth), power (switching activity) and wiring. A smaller circuit may be slower; a minimal two-level form may introduce hazards that a redundant term would prevent. The right "minimum" depends on what the design is constrained by.

## Key concepts

| Term | Meaning |
|---|---|
| Literal | A variable or its complement in an expression. |
| Minterm | A product term containing every variable once; true for exactly one input. |
| Sum of Products (SOP) | An OR of AND terms; a two-level form. |
| Implicant / prime implicant | A product implying the function / one that cannot be enlarged. |
| Essential prime implicant | A prime that alone covers some minterm, so it must be in every cover. |
| Karnaugh map | Gray-coded grid of a truth table for visual minimisation. |
| Don't care | An input combination whose output may be chosen freely. |
| Binary Decision Diagram (BDD) | Graph representation of a Boolean function, canonical for a fixed variable order. |
| Technology mapping | Implementing optimised logic with a given library of cells. |

## How it fits

- **Below:** The identities used are those of [Boolean algebra](../../01-mathematical-foundations/04-algebra/boolean-algebra.md); the targets are [logic gates](logic-gates.md). Its hardness is an instance of [P, NP and NP-completeness](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md), and the covering step is a classic [approximation](../../05-algorithms-and-data-structures/07-advanced-topics/approximation-algorithms.md) problem.
- **Above:** Minimisation is a stage inside synthesis from [hardware description languages](../04-hardware-design/hardware-description-languages.md) to [FPGA and ASIC](../04-hardware-design/fpga-and-asic.md) implementations, where field-programmable gate arrays map logic onto lookup tables instead of gates. BDDs and SAT reasoning reappear in [model checking](../../06-programming-languages/05-formal-methods/model-checking.md) and [constraint satisfaction](../../13-artificial-intelligence/01-classical-ai/constraint-satisfaction.md). Compiler [optimization](../../06-programming-languages/03-compilers/optimization.md) faces the same problem at the software level: find a cheaper equivalent program.
- **Siblings:** [Logic gates](logic-gates.md) are the vocabulary; minimisation is how to say things in fewer words; [arithmetic and building blocks](arithmetic-and-building-blocks.md) are hand-optimised structures too regular for general minimisers to rediscover.

## Common misconceptions

- **"Engineers still minimise logic by hand."** Karnaugh maps are a teaching tool and for tiny functions; production logic is optimised by synthesis software.
- **"The minimum two-level circuit is the best circuit."** Multi-level circuits are often much smaller, and the best circuit depends on delay and power, not just size.
- **"Logic minimisation is solved."** Exact minimisation is intractable in general; tools rely on heuristics that are good, not optimal.

## Go deeper

- Robert Brayton, Gary Hachtel, Curtis McMullen and Alberto Sangiovanni-Vincentelli, *Logic Minimization Algorithms for VLSI Synthesis* (1984): the Espresso algorithms.
- Giovanni De Micheli, *Synthesis and Optimization of Digital Circuits* (1994): two-level, multi-level and sequential synthesis.
- Randal Bryant, "Graph-Based Algorithms for Boolean Function Manipulation" (1986): the paper that introduced reduced ordered BDDs.
