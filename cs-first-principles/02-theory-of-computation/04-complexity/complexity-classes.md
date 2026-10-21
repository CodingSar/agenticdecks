# Complexity Classes

> **Layer:** [02 Theory of Computation](../README.md) › [Complexity](README.md)
> **Builds on:** [P, NP and NP-Completeness](p-np-and-np-completeness.md), [Asymptotic Analysis](asymptotic-analysis.md), [Halting Problem and Undecidability](../03-computability/halting-problem-and-undecidability.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md)
> **Enables:** [Quantum Algorithms](../05-quantum-computation/quantum-algorithms.md), [Randomized Algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md), [Work, Span and Parallel Models](../../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md), [Search and Planning](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md)

## Essence

A complexity class is the set of problems solvable within a given budget of a given resource on a given kind of machine: polynomial time on a deterministic machine (P), polynomial space (PSPACE), polynomial time with random bits (BPP), polynomial time on a quantum computer (BQP), and so on. Classifying problems this way turns a zoo of algorithms into a map. Two kinds of result shape the map. Hierarchy theorems, proved by diagonalisation, show that more of the same resource lets you solve strictly more. Containments and completeness results relate different resources. Strikingly few separations are proved: we know P ≠ EXP (exponential time), but not whether P ≠ PSPACE.

## Core tenets

1. **Classes are defined by machine, resource and bound.** DTIME(f) and NTIME(f) are problems decided by deterministic and nondeterministic Turing machines in O(f(n)) time; DSPACE(f) and NSPACE(f) are the space analogues. The main named classes are L (logarithmic space), NL (its nondeterministic version), P, NP (nondeterministic polynomial time), PSPACE (polynomial space), EXP (exponential time) and their complements. Because reasonable models simulate each other with polynomial overhead, polynomial-based classes do not depend on the details of the machine.

2. **The time hierarchy theorem: more time solves more.** If f is time-constructible, then DTIME(f(n)) ⊊ DTIME(f(n) log f(n)). In particular P ⊊ EXP. Why: diagonalisation, as in the [halting proof](../03-computability/halting-problem-and-undecidability.md), but with a clock. Build a machine D that, on input ⟨M⟩, simulates M on ⟨M⟩ for f(n) steps and does the opposite. D differs from every f(n)-time machine, and the log factor pays for the simulation overhead. The space hierarchy theorem is analogous and tighter: DSPACE(f) ⊊ DSPACE(f log f), indeed ⊊ DSPACE(g) whenever f = o(g).

3. **The known chain of containments is L ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE ⊆ EXP.** Each step has a simple reason: a log-space machine has only polynomially many configurations, so NL ⊆ P (search the configuration graph); an NP machine uses only polynomial time, hence polynomial space, and can try all certificates one by one in reused space, so NP ⊆ PSPACE; a polynomial-space machine has at most exponentially many configurations, so PSPACE ⊆ EXP. By the hierarchy theorems, NL ⊊ PSPACE and P ⊊ EXP, so at least one inclusion in each span is strict, but we do not know which.

4. **Space is more forgiving than time.** Savitch's theorem: NSPACE(f) ⊆ DSPACE(f²), so PSPACE = NPSPACE and nondeterminism costs at most a square in space. The Immerman–Szelepcsényi theorem: NL = co-NL, so nondeterministic space is closed under complement. Both work because space can be reused, while time cannot. The analogous questions for time (P vs NP, NP vs co-NP) remain open.

5. **Completeness identifies each class's hardest problems.** Under suitable reductions, SAT is NP-complete, directed graph reachability is NL-complete, the circuit value problem is P-complete (believed inherently sequential, hence hard to parallelise), and True Quantified Boolean Formulas (TQBF) is PSPACE-complete. Generalised games such as Go with Japanese ko rules or generalised chess on n×n boards are PSPACE- or EXP-complete, because alternating "exists a move / for all replies" quantifiers mirror quantified formulas.

6. **Randomness probably adds little power.** BPP (Bounded-error Probabilistic Polynomial time) is the class of problems solvable in polynomial time with error probability at most 1/3 on every input; repeating and taking a majority vote drives the error down exponentially. Primality testing was the flagship randomised problem until a deterministic polynomial algorithm appeared in 2002. Impagliazzo and Wigderson (1997) showed that if some function in exponential time requires exponential-size circuits, then BPP = P. Most experts conjecture BPP = P, though randomised algorithms remain simpler and faster in practice ([randomized algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md)).

7. **Quantum polynomial time sits between BPP and PSPACE.** BQP (Bounded-error Quantum Polynomial time) contains BPP, because a quantum computer can simulate coin flips, and is contained in PSPACE, because amplitudes can be summed path by path in polynomial space (Bernstein and Vazirani, 1993). Factoring is in BQP (Shor) but not known to be in BPP. NP-complete problems are not believed to be in BQP, and BQP is not believed to contain NP ([quantum algorithms](../05-quantum-computation/quantum-algorithms.md)).

8. **Other resources give other maps.** Circuit complexity measures the size and depth of Boolean circuits; NC (polylogarithmic depth, polynomial size) formalises "efficiently parallelisable", and NC ⊆ P, with P-complete problems the likely exceptions ([work and span](../../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md)). The polynomial hierarchy (PH) stacks alternating quantifiers above NP. Fine-grained complexity relates exact exponents inside P, for example showing edit distance has no truly subquadratic algorithm unless the Strong Exponential Time Hypothesis (SETH) fails.

## Key concepts

| Term | Meaning |
|---|---|
| L / NL | Deterministic / nondeterministic logarithmic space |
| PSPACE | Decidable in polynomial space (any time) |
| EXP | Decidable in time 2^(poly(n)) |
| BPP | Randomised polynomial time with error ≤ 1/3 on every input |
| BQP | Quantum polynomial time with error ≤ 1/3 on every input |
| Time-constructible | f(n) can be computed in O(f(n)) time, so a machine can run a clock |
| Complete problem | In the class, and every problem in the class reduces to it |
| NC | Problems solvable by polynomial-size, polylog-depth circuits |

## How it fits

- **Below:** It generalises [P and NP](p-np-and-np-completeness.md) to space, randomness, alternation and quantum computation. Hierarchy proofs reuse diagonalisation from [computability](../03-computability/halting-problem-and-undecidability.md); randomised classes need [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md).
- **Above:** P-completeness and NC guide [parallel algorithm design](../../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md). PSPACE-hardness of planning explains why [search and planning](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md) uses heuristics, and of linear temporal logic checking why [model checking](../../06-programming-languages/05-formal-methods/model-checking.md) fights state explosion. BPP vs P underlies [randomized algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md); average-case hardness underlies [cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md).
- **Siblings:** [Asymptotic analysis](asymptotic-analysis.md) gives the bounds; [P vs NP](p-np-and-np-completeness.md) is the most famous open edge of this map; [quantum computation](../05-quantum-computation/README.md) adds BQP to it.

## Common misconceptions

- **"We know P ≠ PSPACE (or L ≠ P)."** Neither is proved. Only separations given by hierarchy theorems, such as P ≠ EXP and L ≠ PSPACE, are known.
- **"Randomised algorithms are unreliable."** BPP algorithms can be made to fail with probability below 2⁻¹⁰⁰, far less than the chance of a hardware fault during the run.

## Go deeper

- Sanjeev Arora and Boaz Barak, *Computational Complexity: A Modern Approach* (2009): the standard graduate text.
- Juris Hartmanis and Richard E. Stearns, "On the Computational Complexity of Algorithms" (1965): the time hierarchy theorem and the birth of the field.
- Christos H. Papadimitriou, *Computational Complexity* (1994): elegant treatment of classes and completeness.
