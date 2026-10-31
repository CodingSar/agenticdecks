# Computational Complexity

> **Layer:** [13 Structure and Metamathematics](../README.md) › [Computability and incompleteness](README.md)
> **Builds on:** [Computable functions and the Church–Turing thesis](computable-functions-and-the-church-turing-thesis.md), [Undecidable problems](undecidable-problems.md), [Propositional logic](../../00-logic-and-proof/01-formal-logic/propositional-logic.md), [Colouring and planarity](../../03-combinatorics-and-graph-theory/02-graph-theory/colouring-and-planarity.md)
> **Enables:** [Open problems](../../15-mathematics-in-context/open-problems.md), [Cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md), [Linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md), [P, NP and NP-completeness (CS)](../../../cs-first-principles/02-theory-of-computation/04-complexity/p-np-and-np-completeness.md)

## Essence

Computability asks whether a problem can be solved by an algorithm at all; complexity asks what the solution costs, as a function of the input's length. The robust dividing line is polynomial time, the class P. The class NP collects the problems whose yes-answers have short certificates checkable in polynomial time, such as a colouring of a graph. The Cook–Levin theorem shows that satisfiability is as hard as anything in NP, so thousands of natural problems stand or fall together. Whether P equals NP, whether finding is essentially harder than checking, is open as of 2026.

## Core tenets

1. **Cost is a growth rate, and P does not depend on the machine.** Time complexity is the worst-case number of steps as a function of the input length n. Reasonable deterministic classical models, such as Turing machines and random-access machines, simulate one another with polynomial overhead, so the class P of problems solvable in time O(nᵏ) for some k is the same in all of them. Alan Cobham and Jack Edmonds (1965) proposed P as the notion of feasible. Polynomials are closed under composition, so polynomial-time algorithms that call one another stay polynomial.

2. **More time decides more problems.** The time hierarchy theorem of Juris Hartmanis and Richard Stearns (1965) says that time g, growing sufficiently faster than f, decides problems that time f cannot. The proof is the halting diagonal argument with a clock: on input e, simulate machine e for f(|e|) steps and answer the opposite. Hence P is strictly smaller than exponential time (EXP): some decidable problems are provably infeasible.

3. **NP is the class of problems with short, checkable certificates.** A problem is in NP (nondeterministic polynomial time) when a polynomial-time verifier accepts some polynomial-length certificate for every yes-instance and none for any no-instance. P ⊆ NP, since a polynomial-time algorithm needs no certificate, and NP ⊆ EXP, since one can try every certificate. Ronald Fagin (1974) showed that NP is exactly the class of properties of finite structures definable in existential second-order logic: "there exists a relation such that" is the guessed certificate.

4. **Reductions turn hardness into an ordering.** A polynomial-time many-one reduction from A to B is a polynomial-time map f with x ∈ A if and only if f(x) ∈ B. If B is in P, so is A: run f, then B's algorithm. They are the reductions of undecidability theory with a clock. A problem is NP-hard if every NP problem reduces to it, and NP-complete if it is also in NP.

5. **Satisfiability is NP-complete (Cook–Levin).** Stephen Cook (1971) and, independently, Leonid Levin (1973) showed that Boolean satisfiability (SAT), the question whether a propositional formula has a satisfying assignment, is NP-complete. The proof writes the run of a polynomial-time verifier as a tableau of polynomially many cells, and states in clauses that the first row holds the input, each row follows from the last by the transition rules, and some row accepts. The formula is satisfiable exactly when some certificate is accepted.

6. **NP-completeness spreads by reduction.** Richard Karp (1972) reduced SAT to 21 problems, including clique, vertex cover, Hamiltonian cycle and graph colouring, and thousands more followed. Because reductions compose, a polynomial-time algorithm for one NP-complete problem gives one for all, and a superpolynomial lower bound for one separates P from NP. Small changes cross the line: 2-colourability and 2-SAT are in P, while 3-colourability and 3-SAT are NP-complete.

7. **P versus NP is open, and known methods provably cannot settle it.** As of 2026 there is no proof either way; it is a Clay Mathematics Institute Millennium Prize problem. Three barriers explain why. Relativisation (Theodore Baker, John Gill and Robert Solovay, 1975): there are oracles (black boxes deciding a fixed set) relative to which P = NP and others relative to which P ≠ NP, so simulation and diagonalisation alone, which survive adding any oracle, cannot decide it. Natural proofs (Alexander Razborov and Steven Rudich, 1994): a broad class of circuit lower-bound arguments would break pseudorandom functions believed to exist. Algebrisation (Scott Aaronson and Avi Wigderson, 2008) extends the oracle barrier to algebraic techniques.

8. **Important problems sit between, or have been moved.** Richard Ladner (1975) proved that if P ≠ NP, some NP problems are neither in P nor NP-complete. Primality was placed in P by Manindra Agrawal, Neeraj Kayal and Nitin Saxena (2002), and linear programming by Leonid Khachiyan's ellipsoid method (1979). Factoring, as a decision problem, lies in NP ∩ coNP (coNP holds the complements of NP problems), so it is not NP-complete unless NP = coNP.

## Key concepts

| Term | Meaning |
|---|---|
| P | Problems decidable in time polynomial in the input length |
| NP (nondeterministic polynomial time) | Problems whose yes-instances have polynomial-size certificates checkable in polynomial time |
| coNP | Complements of NP problems, such as tautology |
| Polynomial-time reduction | A polynomial-time f with x ∈ A if and only if f(x) ∈ B |
| NP-complete | In NP, and every NP problem reduces to it |
| Boolean satisfiability (SAT) | Does a propositional formula have a satisfying assignment? |
| Time hierarchy theorem | Substantially more time decides strictly more problems |

## How it fits

- **Below:** [Computable functions](computable-functions-and-the-church-turing-thesis.md) supply the machine model, [undecidable problems](undecidable-problems.md) supply diagonalisation and reduction, [propositional logic](../../00-logic-and-proof/01-formal-logic/propositional-logic.md) supplies SAT, and [graph colouring](../../03-combinatorics-and-graph-theory/02-graph-theory/colouring-and-planarity.md) supplies examples.
- **Above:** P versus NP heads the list of [open problems](../../15-mathematics-in-context/open-problems.md); [cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md) rests on unproved hardness; [linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md) is a celebrated polynomial-time case. [Computer science](../../../cs-first-principles/02-theory-of-computation/04-complexity/p-np-and-np-completeness.md) gives the algorithmic side.
- **Siblings:** In a 1956 letter to John von Neumann, [Gödel](godels-incompleteness-theorems.md) asked how fast one can decide whether a formula has a proof of length n, essentially this question. Stephen Cook and Robert Reckhow (1979) showed NP = coNP exactly when some propositional proof system has polynomial-size proofs of all tautologies, linking it to [proof theory](proof-theory-and-reverse-mathematics.md). Some [decidable theories](../03-model-theory-and-independence/quantifier-elimination-and-decidable-theories.md) are provably infeasible.

## Common misconceptions

- **"NP means not polynomial."**: N stands for nondeterministic, and P ⊆ NP; whether NP contains anything outside P is the open question.
- **"NP-complete problems cannot be solved in practice."**: NP-completeness concerns the worst case; SAT solvers routinely settle huge structured instances.
- **"P ≠ NP would make cryptography secure."**: Cryptography needs problems hard on typical instances (one-way functions), a stronger assumption also unproved as of 2026.

## Go deeper

- Michael Sipser, *Introduction to the Theory of Computation*: a clear first course.
- Sanjeev Arora and Boaz Barak, *Computational Complexity: A Modern Approach* (2009): the standard graduate text.
- Michael Garey and David Johnson, *Computers and Intractability* (1979): the classic catalogue of NP-complete problems.
