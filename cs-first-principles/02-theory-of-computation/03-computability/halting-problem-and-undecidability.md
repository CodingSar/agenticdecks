# The Halting Problem and Undecidability

> **Layer:** [02 Theory of Computation](../README.md) › [Computability](README.md)
> **Builds on:** [Turing Machines](turing-machines.md), [Church–Turing Thesis](church-turing-thesis.md), [Functions and Cardinality](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md), [Proof Techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md)
> **Enables:** [Static Analysis and Code Review](../../12-software-engineering/03-quality/static-analysis-and-code-review.md), [Model Checking](../../06-programming-languages/05-formal-methods/model-checking.md), [Semantic Analysis](../../06-programming-languages/03-compilers/semantic-analysis.md), [P, NP and NP-Completeness](../04-complexity/p-np-and-np-completeness.md)

## Essence

Some precisely stated questions about programs have no algorithm that always answers them correctly. The first and most important is the halting problem: given a program and an input, will the program eventually stop? Turing proved in 1936 that no program can decide this for all programs and inputs, by turning a hypothetical decider against itself. Through reductions, the same impossibility spreads to a vast range of questions, and Rice's theorem extends it to *every* non-trivial question about what a program computes. This is why perfect bug finders, optimisers and virus scanners cannot exist.

## Core tenets

1. **The halting problem is undecidable.** Let HALT = {⟨M, w⟩ : machine M halts on input w}. There is no Turing machine that halts on every input and accepts exactly HALT. By the [Church–Turing thesis](church-turing-thesis.md), no algorithm on any hardware does.

2. **The proof is diagonalisation: feed the decider its own contradiction.** Suppose H(M, w) always halts and says whether M halts on w. Build D(M): run H(M, ⟨M⟩); if H says "halts", loop forever; otherwise halt. Now ask what D(⟨D⟩) does. If it halts, H said it does not halt, so it loops; if it loops, H said it halts, so it halts. Both are contradictions, so H cannot exist. This is Cantor's diagonal argument ([cardinality](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md)) applied to the list of all programs.

   ```
   def D(prog):
       if H(prog, prog):    # "prog halts when run on itself"
           while True: pass
       else:
           return
   # D(D) halts  <=>  H(D, D) is False  <=>  D(D) does not halt
   ```

3. **Halting is recognisable but not decidable, and its complement is not even recognisable.** A universal machine accepts ⟨M, w⟩ by simulating M on w and accepting if it stops, so HALT is recursively enumerable. A language is decidable exactly when both it and its complement are recognisable (run both recognisers in parallel; one must stop). So the complement, "M runs forever on w", is not recognisable: no procedure can confirm non-termination in general. Beyond HALT lies an infinite hierarchy of ever-harder undecidable problems (the Turing degrees).

4. **Reductions spread undecidability.** If a decider for problem B could be used to decide A, write A ≤ B; then A undecidable implies B undecidable. Most undecidability proofs reduce HALT to the new problem by building, from ⟨M, w⟩, an instance that has the property exactly when M halts on w. Examples: whether a program reaches a given line, whether two programs are equivalent, whether a context-free grammar generates all strings, and whether a polynomial equation has integer solutions (Hilbert's tenth problem, Matiyasevich 1970).

5. **Rice's theorem: every non-trivial semantic property is undecidable.** A property of programs is *semantic* if it depends only on the function (or language) the program computes, not on its text. It is *non-trivial* if some programs have it and some do not. Rice (1953) proved that every such property is undecidable. Why: given ⟨M, w⟩, build a program that first runs M on w and then behaves like a program with the property; it has the property exactly when M halts (taking, without loss of generality, the empty function not to have it). "Does it ever divide by zero?" and "Is it a virus?" are undecidable.

6. **Undecidable is about all inputs, not each input.** For any single program, the question "does it halt?" has a definite answer, and often it is easy to find. Undecidability says no *single algorithm* gets every case right. So practical tools are sound but incomplete (false alarms or "don't know"), complete but unsound, or restricted to a decidable subset (such as the finite-state models of [model checking](../../06-programming-languages/05-formal-methods/model-checking.md)).

7. **Self-reference also limits logic itself.** Gödel's first incompleteness theorem (1931) says any consistent, effectively axiomatised theory strong enough for basic arithmetic has true statements it cannot prove. A version for sound theories follows from the halting problem: if such a theory proved every true statement of the form "M does not halt on w", searching for proofs would decide halting. The same trick gives Kleene's recursion theorem: programs can obtain their own source code (quines).

## Key concepts

| Term | Meaning |
|---|---|
| Decidable | Some algorithm always halts with the correct yes/no answer |
| Recognisable (semi-decidable) | Some algorithm halts with "yes" exactly on members |
| Diagonalisation | Building an object that differs from every item in a list, including itself |
| Reduction A ≤ B | Transform instances of A into instances of B, preserving the answer |
| Semantic property | Depends only on input/output behaviour, not program text |
| Rice's theorem | Every non-trivial semantic property of programs is undecidable |
| Sound / complete analysis | Never wrong when it says "safe" / never misses a true "safe" |

## How it fits

- **Below:** It uses Cantor's [diagonal argument](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md), proof by contradiction ([proof techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md)), and the encoding of programs as data from [Turing machines](turing-machines.md).
- **Above:** It is why [static analysers](../../12-software-engineering/03-quality/static-analysis-and-code-review.md) and type checkers ([type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md)) must over- or under-approximate, why compiler [optimisation](../../06-programming-languages/03-compilers/optimization.md) cannot always find the best program, why [testing](../../12-software-engineering/03-quality/testing.md) cannot prove absence of bugs, why the shortest description of a string ([Kolmogorov complexity](../01-information-theory/kolmogorov-complexity.md)) cannot be computed, and why malware detection is heuristic, so systems rely on [access control](../../11-security-and-cryptography/03-system-security/access-control.md) instead.
- **Siblings:** [Turing machines](turing-machines.md) provide the model and the universal machine; the [Church–Turing thesis](church-turing-thesis.md) makes the result universal; [lambda calculus](lambda-calculus.md) has the equivalent result for normal forms. [Complexity](../04-complexity/README.md) borrows diagonalisation (hierarchy theorems) and reductions (NP-completeness, where NP is nondeterministic polynomial time) for decidable problems.

## Common misconceptions

- **"We can't tell whether any program halts."** We often can, for specific programs. The theorem rules out one algorithm that works for all of them.
- **"Undecidable means very hard, so a fast enough computer would help."** Speed is irrelevant. No amount of time or hardware decides an undecidable problem in general.
- **"Real computers have finite memory, so halting is decidable and the theorem is irrelevant."** With n bits of state, halting is decidable by detecting a repeated configuration, but that can take 2ⁿ steps, so no feasible general method exists.

## Go deeper

- Alan M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem" (1936): the original undecidability proof.
- H. Gordon Rice, "Classes of Recursively Enumerable Sets and Their Decision Problems" (1953): Rice's theorem.
- Michael Sipser, *Introduction to the Theory of Computation* (3rd ed., 2012), chapters 4–6: diagonalisation, reductions, recursion theorem.
