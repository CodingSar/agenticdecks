# Complexity

> **Layer:** [02 Theory of Computation](../README.md) › Complexity
> **Children:** [Asymptotic Analysis](asymptotic-analysis.md) · [P, NP and NP-Completeness](p-np-and-np-completeness.md) · [Complexity Classes](complexity-classes.md)

## What this area is about

Computability separates what can be computed from what cannot. Complexity asks the next question: **among computable problems, what does each one fundamentally cost?** Cost means time, memory, random bits, parallel depth or quantum operations, measured as a function of input size. The goal is not to time a particular program but to find the inherent difficulty of a *problem*, the cost every possible algorithm must pay.

The unifying idea is that problems can be grouped into classes by resource budget and compared by **reductions**: if any algorithm for B can be cheaply turned into one for A, then A is no harder than B. This turns isolated algorithmic facts into a structured map, with complete problems marking the hardest point of each class. The map has a few proven walls (hierarchy theorems) and many famous open borders (P versus NP, where P is polynomial time and NP is nondeterministic polynomial time).

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Asymptotic Analysis](asymptotic-analysis.md) | The yardstick: Big-O, growth rates, recurrences, lower bounds | Calculus, recurrences, a machine model |
| [P, NP and NP-Completeness](p-np-and-np-completeness.md) | The central divide: solving vs verifying; reductions; Cook–Levin | Asymptotics, Turing machines, logic |
| [Complexity Classes](complexity-classes.md) | The wider map: space, randomness, quantum, parallelism; hierarchy theorems | P and NP, diagonalisation |

Read in order. Asymptotic analysis lets you say "polynomial" and "exponential" precisely. P versus NP applies that vocabulary to the most practically important question: which search problems have efficient algorithms. Complexity classes then places P and NP inside a larger picture.

```
   L  ⊆  NL  ⊆  P  ⊆  NP  ⊆  PSPACE  ⊆  EXP
                |                |
                BPP  ⊆  BQP  ⊆  PSPACE      (BPP: randomised, BQP: quantum)

   proved strict:  NL ≠ PSPACE,  P ≠ EXP     (hierarchy theorems)
   open:           P vs NP,  P vs PSPACE,  BPP vs P (conjectured equal)
```

## Connections to sibling areas

- **[Information Theory](../01-information-theory/README.md):** Shannon's theorems prove good codes exist but say nothing about decoding cost; complexity asks whether decoding is tractable. Pseudorandomness and cryptographic security are defined complexity-theoretically, as indistinguishability from true entropy by efficient observers.
- **[Automata and Formal Languages](../02-automata-and-formal-languages/README.md):** Language classes are complexity classes: regular languages need constant space, context-sensitive languages are exactly nondeterministic linear space, and parsing algorithms are analysed asymptotically.
- **[Computability](../03-computability/README.md):** Complexity is computability with a budget. It inherits the Turing machine model, reductions and diagonalisation, and adds clocks and space bounds.
- **[Quantum Computation](../05-quantum-computation/README.md):** Quantum computers change the cost of some problems but not what is computable. The class BQP (bounded-error quantum polynomial time) formalises their power, and its relation to BPP and NP is where the extended Church–Turing thesis is tested.

## Connections across layers

From below, the area uses [calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md), [recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md), [propositional logic](../../01-mathematical-foundations/01-logic/propositional-logic.md) and [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md).

Upward, it is the theoretical frame for all of [algorithms and data structures](../../05-algorithms-and-data-structures/README.md): the [models of computation](../../05-algorithms-and-data-structures/01-foundations/models-of-computation.md) there refine the Turing-machine cost model to match real hardware. NP-hardness explains the heuristics in [compilers](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md), [query optimisers](../../09-data-management/03-query-processing/query-optimization.md), [logic synthesis](../../03-digital-logic/02-combinational-logic/logic-minimization.md) and [Artificial Intelligence (AI) planning](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md). Computational hardness assumptions are the entire basis of [modern cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md). Parallel complexity informs [parallel computing](../../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md).

## Cross-cutting threads

- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): lower bounds and hardness results say which costs no algorithm can avoid.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): time against space, exactness against speed (approximation), certainty against speed (randomisation).
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): asymptotic notation abstracts away the machine so results survive hardware changes.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): input size is measured in bits, so encoding choices (unary vs binary numbers) change a problem's complexity.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): NP is exactly the problems whose answers can be checked quickly, the basis of certificates and proofs.
