# Proof Techniques

> **Layer:** [01 Mathematical Foundations](../README.md) › [Logic](README.md)
> **Builds on:** [Propositional Logic](propositional-logic.md), [Predicate Logic](predicate-logic.md)
> **Enables:** [Induction and Recurrences](../03-discrete-mathematics/induction-and-recurrences.md), [Correctness and Invariants](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md), [Halting Problem and Undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md), [Foundations of Modern Cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md)

## Essence

A proof is a finite argument that a claim follows from agreed premises, where each step is justified by a rule of logic. A handful of proof shapes cover almost everything a computer scientist proves: direct proof, contrapositive, contradiction, cases, construction of a witness, induction, and the pigeonhole and diagonal arguments. Each shape mirrors an inference rule of [predicate logic](predicate-logic.md), so choosing a technique is choosing which rule to apply to the claim's outermost connective. Proofs matter in Computer Science (CS) because a test checks finitely many inputs while a proof covers all of them, and because the most important results in the field (undecidability, lower bounds, security reductions) are proofs that something cannot be done.

## Core tenets

1. **The shape of the claim picks the technique.** To prove `∀x. P(x)`, take an arbitrary `x` and prove `P(x)` with no extra assumptions about it. To prove `∃x. P(x)`, exhibit a specific witness. To prove `A → B`, assume `A` and derive `B`. To prove `A ∧ B`, prove each. Reading the claim's logical structure first removes most of the mystery of "how do I start".

2. **The contrapositive is equivalent; the converse is not.** `A → B` is logically equivalent to `¬B → ¬A`, so proving one proves the other. The converse `B → A` is a different claim. "If the cache hit, the data is valid" does not give "if the data is valid, the cache hit". Using the converse by mistake is the most common invalid step in informal reasoning about systems.

3. **Proof by contradiction proves impossibility.** Assume the claim is false and derive an absurdity; then the claim is true. This is the natural technique for "there is no algorithm that…" and "there is no largest…". Euclid's proof that there are infinitely many primes and Turing's proof that halting is undecidable both work this way.

4. **Induction proves claims about unboundedly many structured things.** To prove `P(n)` for all natural numbers, prove `P(0)` and that `P(k)` implies `P(k+1)`. The same principle works on any well-founded structure: lists, trees, programs and derivations (*structural induction*). Loop invariants are induction on the number of iterations, and recursive-function correctness is induction on input size. See [induction and recurrences](../03-discrete-mathematics/induction-and-recurrences.md).

5. **Strengthening the hypothesis often makes a proof go through.** An inductive proof can fail because `P(k)` is too weak to give `P(k+1)`. Proving a stronger statement gives a stronger hypothesis to use. This is exactly why loop invariants usually say more than the final postcondition: the extra facts are what the next iteration needs.

6. **Counting arguments prove existence without construction.** The pigeonhole principle says that putting *n+1* items into *n* boxes forces two into one box. It shows that every lossless compressor must expand some input (there are 2^n strings of length *n* but fewer than 2^n shorter strings), and that every hash function from large keys to small tables has collisions. Counting shows something exists or must happen without telling you which instance.

7. **Diagonalisation proves that one collection is too big for another.** Cantor showed that no list of infinite binary strings can contain them all: build a string that differs from the *i*-th string at position *i*. Turing applied the same construction to programs and their behaviour, producing the [halting problem](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md). The time and space hierarchy theorems in complexity use it too.

8. **Reductions transfer hardness and correctness.** To show B is hard, show that a solver for B would solve a known-hard A. To show a protocol is secure, show that an attacker on it would break an assumed-hard problem. Reductions are proofs by contrapositive packaged as algorithms, and they organise both [complexity theory](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md) and [provable cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md).

## Key concepts

| Term | Meaning |
|---|---|
| Direct proof | Assume the hypothesis, derive the conclusion step by step |
| Contrapositive | `¬B → ¬A`, equivalent to `A → B` |
| Contradiction | Assume the negation of the claim and derive a falsehood |
| Constructive proof | Proves existence by exhibiting a witness (and so gives an algorithm) |
| Induction | Base case plus step case covers all elements of a well-founded set |
| Invariant | A property that holds initially and is preserved by every step |
| Pigeonhole principle | More items than boxes forces a shared box |
| Diagonalisation | Build an object that differs from each listed object somewhere |
| Reduction | Transform problem A into problem B so a solution to B solves A |

## How it fits

- **Below:** The techniques are the inference rules of [propositional](propositional-logic.md) and [predicate](predicate-logic.md) logic, used informally.
- **Above:** Algorithm correctness ([invariants](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md)), lower bounds ([comparison sorting](../../05-algorithms-and-data-structures/04-sorting-and-searching/comparison-sorting.md) needs Ω(n log n) by a counting argument), undecidability, NP-completeness (NP is Nondeterministic Polynomial time), [impossibility results](../../10-distributed-and-parallel-computing/02-distributed-foundations/impossibility-results.md) in distributed systems, and security reductions are all proofs. [Proof assistants](../../06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md) mechanise these same techniques.
- **Siblings:** The other logic leaves define what a valid step is; this leaf is how to find a sequence of valid steps.

## Common misconceptions

- **"Many passing tests prove correctness."** Tests check instances; a ∀-claim needs a proof. Tests can only refute.
- **"A proof by contradiction is less trustworthy."** It is classically valid. It is merely *non-constructive*: it may prove something exists without producing it, which matters when you want an algorithm.
- **"Induction assumes what it proves."** The step proves `P(k) → P(k+1)` for arbitrary `k`; combined with the base case it reaches every `n` by a finite chain.

## Go deeper

- Daniel Velleman, *How to Prove It* (3rd ed., 2019): the structure-of-the-claim method in detail.
- Eric Lehman, F. Thomson Leighton and Albert Meyer, *Mathematics for Computer Science* (2017 revision, free online): proofs taught with computer-science examples.
- George Pólya, *How to Solve It* (1945): heuristics for finding proofs.
