# P, NP and NP-Completeness

> **Layer:** [02 Theory of Computation](../README.md) › [Complexity](README.md)
> **Builds on:** [Asymptotic Analysis](asymptotic-analysis.md), [Turing Machines](../03-computability/turing-machines.md), [Propositional Logic](../../01-mathematical-foundations/01-logic/propositional-logic.md), [Halting Problem and Undecidability](../03-computability/halting-problem-and-undecidability.md)
> **Enables:** [Approximation Algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/approximation-algorithms.md), [Backtracking and Branch and Bound](../../05-algorithms-and-data-structures/03-design-paradigms/backtracking-and-branch-and-bound.md), [Constraint Satisfaction](../../13-artificial-intelligence/01-classical-ai/constraint-satisfaction.md), [Foundations of Modern Cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md)

## Essence

P is the class of decision problems that can be *solved* in polynomial time; NP (nondeterministic polynomial time) is the class whose "yes" answers can be *checked* in polynomial time given a short certificate. Every problem in P is in NP, and the central open question of computer science is whether the converse holds: is finding a solution ever fundamentally harder than recognising one? NP-complete problems are the hardest problems in NP: each one can encode every other via a polynomial-time reduction, so a fast algorithm for any of them would give fast algorithms for all. Thousands of practical problems (scheduling, routing, packing, circuit layout, protein folding variants) are NP-complete, which is why engineers routinely reach for heuristics, approximations and special cases.

## Core tenets

1. **P captures "efficiently solvable".** P = ∪ₖ TIME(nᵏ), problems decidable by a deterministic Turing machine in polynomial time. The class is robust: it is the same for multitape Turing machines, Random Access Machines (RAMs) and every realistic classical model, because they simulate each other with polynomial overhead, and polynomials compose. Shortest paths, sorting, linear programming and primality testing (Agrawal, Kayal and Saxena, 2002) are in P.

2. **NP captures "efficiently verifiable".** A problem is in NP if there is a polynomial-time verifier V and a polynomial p such that x is a "yes" instance exactly when some certificate c with |c| ≤ p(|x|) makes V(x, c) accept. For Boolean satisfiability (SAT) the certificate is a satisfying assignment; for Hamiltonian cycle it is the cycle. Equivalently, NP is what a nondeterministic Turing machine decides in polynomial time: it "guesses" the certificate. NP is about "yes" answers; co-NP is the class whose "no" answers have short certificates.

3. **Polynomial-time reductions compare difficulty.** A ≤ₚ B if a polynomial-time function f maps every instance x of A to an instance f(x) of B with the same answer. Then an efficient algorithm for B yields one for A. B is NP-hard if every NP problem reduces to it, and NP-complete if it is also in NP. Reductions are transitive, so proving a new problem NP-complete only needs one reduction *from* a known NP-complete problem.

4. **The Cook–Levin theorem: SAT is NP-complete.** Cook (1971) and Levin (1973) independently showed that any NP problem reduces to SAT. Why: an NP verifier is a Turing machine that runs for p(n) steps, so its entire computation fits in a p(n) × p(n) "tableau" of tape cells over time. Each cell's content depends only on a few cells in the row above, and that local rule, plus "the start row holds the input and the machine ends in the accept state", can be written as a polynomial-size Boolean formula. The formula is satisfiable exactly when some certificate makes the verifier accept.

5. **NP-completeness spreads by reduction.** Karp (1972) reduced SAT to 21 problems, including clique, vertex cover, Hamiltonian cycle, 3-dimensional matching and subset sum. 3-SAT (clauses of three literals) is NP-complete, while 2-SAT is in P, which shows how thin the line can be. Garey and Johnson's 1979 catalogue lists hundreds more. Optimisation versions (the shortest tour, the smallest cover) are NP-hard because their decision versions ("is there a tour of length ≤ k?") are NP-complete.

6. **P = NP is open, and most experts believe P ≠ NP.** If P = NP, every efficiently checkable problem would be efficiently solvable: mathematical proofs of reasonable length could be found automatically and most public-key cryptography would fall. Known proof techniques provably cannot settle it: relativisation (Baker–Gill–Solovay, 1975), natural proofs (Razborov–Rudich, 1997) and algebrisation (Aaronson–Wigderson, 2009) each rule out a broad family of arguments. If P ≠ NP, Ladner's theorem (1975) says there are NP problems that are neither in P nor NP-complete; factoring and graph isomorphism are candidates.

7. **NP-complete describes the worst case, not every instance.** Modern SAT solvers routinely handle industrial instances with millions of variables, because real instances have structure that conflict-driven clause learning exploits. Hardness is about the *family*: no algorithm is known that is fast on all instances. Engineers respond with [approximation algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/approximation-algorithms.md) with proven ratios, [branch and bound](../../05-algorithms-and-data-structures/03-design-paradigms/backtracking-and-branch-and-bound.md), fixed-parameter algorithms that are exponential only in a small parameter, and solvers for SAT, integer programming and [constraint satisfaction](../../13-artificial-intelligence/01-classical-ai/constraint-satisfaction.md).

8. **Cryptography needs more than P ≠ NP.** Security requires problems that are hard on *average* for randomly generated instances, and one-way functions that are easy to compute but hard to invert. P ≠ NP only says some instances are hard in the worst case. The existence of one-way functions is an unproven assumption stronger than P ≠ NP; factoring and discrete logarithms are the usual candidates ([foundations of modern cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md)).

## Key concepts

| Term | Meaning |
|---|---|
| Decision problem | A question with a yes/no answer; a language of "yes" instances |
| P | Decidable in deterministic polynomial time |
| NP | "Yes" answers verifiable in polynomial time with a polynomial-size certificate |
| co-NP | "No" answers verifiable in polynomial time |
| Polynomial reduction ≤ₚ | Efficient, answer-preserving translation between problems |
| NP-hard | Every NP problem reduces to it (need not be in NP) |
| NP-complete | NP-hard and in NP |
| SAT / 3-SAT | Satisfiability of Boolean formulas (in conjunctive normal form with 3 literals per clause) |
| Certificate (witness) | Short proof of a "yes" answer that a verifier can check |

## How it fits

- **Below:** It uses [Turing machines](../03-computability/turing-machines.md) as the cost model, [asymptotic analysis](asymptotic-analysis.md) for "polynomial", and [propositional logic](../../01-mathematical-foundations/01-logic/propositional-logic.md) for SAT. Reductions are borrowed from [computability](../03-computability/halting-problem-and-undecidability.md), with a time limit added.
- **Above:** It tells algorithm designers when to stop looking for exact efficient algorithms ([approximation](../../05-algorithms-and-data-structures/07-advanced-topics/approximation-algorithms.md), [backtracking](../../05-algorithms-and-data-structures/03-design-paradigms/backtracking-and-branch-and-bound.md)). It explains why join ordering in [query optimisation](../../09-data-management/03-query-processing/query-optimization.md), register allocation in [code generation](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md), [logic minimisation](../../03-digital-logic/02-combinational-logic/logic-minimization.md) and [classical planning](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md) use heuristics. Its assumptions underpin [cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md).
- **Siblings:** [Asymptotic analysis](asymptotic-analysis.md) supplies the yardstick; [complexity classes](complexity-classes.md) places P and NP in a larger map that includes space, randomness and quantum computation.

## Common misconceptions

- **"NP means non-polynomial."** It means nondeterministic polynomial: verifiable in polynomial time. Every problem in P is also in NP.
- **"NP-complete problems can't be solved in practice."** Many instances are solved routinely. The claim is only that no known algorithm is efficient on *every* instance.
- **"Quantum computers solve NP-complete problems efficiently."** There is no evidence for this. Grover's search gives only a square-root speedup over brute force, and NP is not believed to be contained in BQP (bounded-error quantum polynomial time).

## Go deeper

- Stephen A. Cook, "The Complexity of Theorem-Proving Procedures" (1971): the first NP-completeness proof.
- Richard M. Karp, "Reducibility Among Combinatorial Problems" (1972): the 21 problems that showed NP-completeness is everywhere.
- Michael R. Garey and David S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness* (1979): the classic catalogue and method.
- Lance Fortnow, *The Golden Ticket: P, NP, and the Search for the Impossible* (2013): a non-technical account of what is at stake.
