# Propositional Logic

> **Layer:** [00 Logic and Proof](../README.md) › [Formal Logic](README.md)
> **Builds on:** nothing earlier in this tree
> **Enables:** [Predicate Logic and Quantifiers](predicate-logic-and-quantifiers.md), [Formal Proof Systems](formal-proof-systems.md), [Direct Proof, Contraposition and Contradiction](../02-methods-of-proof/direct-proof-contraposition-and-contradiction.md), [Sets and Set Operations](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md), [P, NP and NP-Completeness](../../../cs-first-principles/02-theory-of-computation/04-complexity/p-np-and-np-completeness.md)

## Essence

Propositional logic is the logic of "not", "and", "or", "if … then" and "if and only if", applied to statements treated as indivisible units that are either true or false. It answers one question exactly: which compound statements are true because of their form alone, whatever their parts say. The idea that makes it work is that formulas are built by a recursive grammar, so truth values are computed by the same recursion, and validity, truth under all 2ⁿ assignments to the n letters, is checked by a finite truth table. It is also where the two sides of logic first appear: consequence, written ⊨ (truth under every assignment), and derivability, written ⊢ (proof in a formal system).

## Core tenets

1. **Formulas are trees, so truth is computed by recursion on their structure.** Formulas are built from propositional letters p, q, r, … by one rule: if φ and ψ are formulas, so are ¬φ, (φ ∧ ψ), (φ ∨ ψ), (φ ⇒ ψ) and (φ ⇔ ψ). Brackets make each formula read in exactly one way (unique readability), and that is what lets a valuation, an assignment of T or F to each letter, extend to every formula through the truth tables. Without brackets p ∧ q ∨ r is ambiguous, and the readings differ: with p false and r true, (p ∧ q) ∨ r is true but p ∧ (q ∨ r) is false.

2. **Material implication is the reading of "if" that mathematics forces.** φ ⇒ ψ is false only when φ is true and ψ is false. Theorems force it: "for every n, if n is a prime greater than 2 then n is odd" is true, so every instance is true, and n = 3 (true ⇒ true), n = 9 (false ⇒ true) and n = 4 (false ⇒ false) fill three rows of the table with T; the fourth row must be F, or modus ponens (from φ and φ ⇒ ψ, infer ψ) would fail. Hence claims about the empty set are vacuously true: "every element of ∅ is green" holds.

3. **Validity, consequence and satisfiability are one question.** A formula is a tautology if every valuation makes it true and satisfiable if some valuation does; Γ ⊨ φ (φ is a consequence of the set Γ) if every valuation that makes all of Γ true makes φ true. Then Γ ⊨ φ if and only if Γ ∪ {¬φ} is unsatisfiable, and φ is a tautology exactly when ¬φ is unsatisfiable. One algorithm for satisfiability therefore answers all three questions, which is why satisfiability (SAT) solvers are used throughout hardware and software verification ([Model Checking](../../../cs-first-principles/06-programming-languages/05-formal-methods/model-checking.md)).

4. **A handful of connectives expresses every truth function.** With n letters there are 2^(2ⁿ) truth functions, and each is expressed in disjunctive normal form: one conjunction of literals for each row where the function is T, joined by ∨ (or p ∧ ¬p if there is no such row). Since φ ∨ ψ ≡ ¬(¬φ ∧ ¬ψ), the pair {¬, ∧} already suffices, and so does the single connective NAND ("not both", the Sheffer stroke). A set fails to be complete when it preserves some property: a formula built from ∧ and ∨ alone is true whenever all its letters are true, so {∧, ∨} cannot express ¬p.

5. **Validity is decidable, but no efficient method is known.** A formula with n letters has 2ⁿ rows, so brute force decides validity; whether polynomial time suffices is open. Cook (1971) and, independently, Levin showed that satisfiability is NP-complete: a polynomial-time algorithm for it would solve in polynomial time every problem in NP (nondeterministic polynomial time: problems whose solutions can be checked quickly), so that P, the class solvable in polynomial time, would equal NP, open as of 2026. A satisfying valuation certifies satisfiability briefly; whether every tautology has a short certificate of validity is the question NP = coNP (coNP: complements of problems in NP), also open as of 2026.

6. **Bivalence is an assumption, and dropping it gives other logics.** Every tautology above rests on each letter being exactly true or false, which makes p ∨ ¬p (excluded middle) and ¬¬p ⇒ p (double-negation elimination) valid. Intuitionistic logic reads a statement as true when a proof of it is in hand, rejects both laws as general principles, and is captured by no finite truth table ([Constructive and Intuitionistic Logic](../03-the-axiomatic-method/constructive-and-intuitionistic-logic.md)). Classical mathematics keeps bivalence, and proving a positive statement by contradiction depends on it.

## Key concepts

| Term | Meaning |
|---|---|
| Propositional letter | An atomic statement p, q, r, … with no internal structure |
| Connective | ¬, ∧, ∨, ⇒ or ⇔, each defined by a truth table |
| Valuation | An assignment of T or F to every letter, extended to all formulas by the tables |
| Tautology | A formula true under every valuation, such as p ∨ ¬p |
| Γ ⊨ φ | Every valuation that makes all formulas of Γ true makes φ true |
| φ ≡ ψ | Logical equivalence: the same truth value under every valuation |
| Literal | A letter or its negation |
| Disjunctive normal form | A disjunction of conjunctions of literals |
| Functionally complete | A set of connectives that expresses every truth function |

## How it fits

- **Below:** nothing in this tree; it assumes only that statements combine and that each is true or false.
- **Above:** [Predicate Logic and Quantifiers](predicate-logic-and-quantifiers.md) opens the letters up into statements about objects; set operations mirror the connectives (∩ for ∧, ∪ for ∨, complement for ¬) in [Sets and Set Operations](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md), as events do in [Finite Probability Spaces](../../03-combinatorics-and-graph-theory/03-discrete-probability/finite-probability-spaces.md); circuits are formulas built in hardware ([Logic Gates](../../../cs-first-principles/03-digital-logic/02-combinational-logic/logic-gates.md)).
- **Siblings:** [Formal Proof Systems](formal-proof-systems.md) replaces truth tables by derivations, and [Soundness, Completeness and Compactness](soundness-completeness-and-compactness.md) shows that the two agree; for propositional logic Post proved the agreement in 1921.

## Common misconceptions

- **"φ ⇒ ψ says that φ causes ψ"**: material implication only rules out a true φ with a false ψ, so "if 2 + 2 = 5 then the Moon is made of cheese" is true.
- **"'Or' means one or the other but not both"**: mathematical ∨ is inclusive, so "n is even or n > 1" is true for n = 4. Exclusive or is a different connective.
- **"A valid argument has a true conclusion"**: validity means the conclusion is true whenever all the premises are; a valid argument from a false premise can reach a false conclusion.

## Go deeper

- Herbert B. Enderton, *A Mathematical Introduction to Logic* (2nd edition, 2001): the standard rigorous treatment.
- Dirk van Dalen, *Logic and Structure* (5th edition, 2013): propositional logic with natural deduction and its intuitionistic variant.
- Michael Huth and Mark Ryan, *Logic in Computer Science* (2nd edition, 2004): normal forms, SAT and verification from the computing side.
