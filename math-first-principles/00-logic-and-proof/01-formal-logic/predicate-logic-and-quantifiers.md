# Predicate Logic and Quantifiers

> **Layer:** [00 Logic and Proof](../README.md) › [Formal Logic](README.md)
> **Builds on:** [Propositional Logic](propositional-logic.md)
> **Enables:** [Formal Proof Systems](formal-proof-systems.md), [Soundness, Completeness and Compactness](soundness-completeness-and-compactness.md), [Sets and Set Operations](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md), [Sequences and Limits](../../06-real-analysis/01-limits-and-convergence/sequences-and-limits.md), [Models and the Löwenheim–Skolem Theorems](../../13-structure-and-metamathematics/03-model-theory-and-independence/models-and-the-lowenheim-skolem-theorems.md)

## Essence

Predicate logic, also called first-order logic, opens the atomic statements of propositional logic into statements about objects: predicates such as "x is prime", functions such as x + y, and the quantifiers ∀ ("for every") and ∃ ("there exists") which range over a domain. A sentence is true or false only in a structure, a domain with an interpretation of each symbol: ∀x ∃y (x · y = e) is true in every group but false in ℕ with · read as + and e as 0. Truth is defined by Tarski's recursion on formulas. The logic is strong enough to express essentially all of mathematics, since set theory is a first-order theory, and weak enough to keep a complete proof system.

## Core tenets

1. **A language fixes the vocabulary; a structure gives it meaning.** A signature lists constant, function and relation symbols, for groups a constant e and a binary function ·. Terms (x, e, x · y, …) name objects and formulas say things about them; a structure supplies a non-empty domain and interprets each symbol on it. A structure is a group exactly when it satisfies the three group axioms, so an axiom system describes a class of structures, whose members can disagree about other sentences, such as commutativity.

2. **Truth is defined by recursion, with quantifiers handled through assignments.** Tarski's definition (1933) says when a structure M satisfies a formula under an assignment s of objects to variables: connectives work as in propositional logic; M satisfies ∀x φ under s if and only if M satisfies φ under every assignment that differs from s at most at x. A sentence, a formula with no free variables, is then true or false in M, written M ⊨ φ. No table computes this over an infinite domain: Church and Turing showed in 1936 that validity is undecidable, although the valid sentences, being exactly the provable ones by the completeness theorem, can be listed.

3. **The order of quantifiers carries the meaning.** Swapping ∀ and ∃ changes a statement; the classic case is continuity:

```
f continuous on ℝ:            ∀ε>0  ∀x  ∃δ>0  ∀y  ( |x − y| < δ  ⇒  |f(x) − f(y)| < ε )
f uniformly continuous on ℝ:  ∀ε>0  ∃δ>0  ∀x  ∀y  ( |x − y| < δ  ⇒  |f(x) − f(y)| < ε )
```

In the first, δ may depend on x; in the second, one δ must serve every x. The function x² is continuous but not uniformly continuous on ℝ: for ε = 1 and any δ > 0, take x = 1/δ and y = x + δ/2; then |x² − y²| = |x − y| · |x + y| > 1.

4. **Negation passes through quantifiers by swapping them.** ¬∀x φ ≡ ∃x ¬φ and ¬∃x φ ≡ ∀x ¬φ, so negation is mechanical: push ¬ inward, flipping each quantifier. "aₙ → L" is ∀ε>0 ∃N ∀n≥N |aₙ − L| < ε, so "aₙ does not tend to L" is ∃ε>0 ∀N ∃n≥N |aₙ − L| ≥ ε: some tolerance is broken infinitely often. Every formula can be rewritten with all quantifiers in front (prenex form), and the number of alternations ∀∃∀… measures how complicated a statement is.

5. **∀ goes with ⇒ and ∃ goes with ∧.** "Every prime is odd" is ∀x (Prime(x) ⇒ Odd(x)), false because of 2; "some prime is even" is ∃x (Prime(x) ∧ Even(x)), true because of 2. Mixing them gives nonsense: ∃x (Prime(x) ⇒ Even(x)) is true merely because 9 is not prime, and ∀x (Prime(x) ∧ Odd(x)) claims that every number is an odd prime. The restricted quantifiers ∀x∈A and ∃x∈A abbreviate exactly these two patterns.

6. **Bound variables can be renamed, but substitution must avoid capture.** In ∃y (y > x) the variable x is free and y is bound, so the formula is about x alone, and ∃z (z > x) says the same. Substituting the term y for x carelessly gives ∃y (y > y), false in every strict order, although ∃y (y > x) is true in ℕ for every value of x. So substitution renames bound variables first, and the rule "from ∀x φ(x) infer φ(t)" requires that no variable of t be captured.

7. **First order is a deliberate compromise.** First-order quantifiers range over elements, never over subsets or functions. The induction axiom of arithmetic therefore becomes a schema, one axiom per formula, which covers only the countably many definable sets, and nonstandard models slip in. Second-order logic quantifies over all subsets and pins down ℕ and ℝ up to isomorphism, but loses the complete proof system and the compactness theorem that make first-order logic workable.

## Key concepts

| Term | Meaning |
|---|---|
| Signature | The constant, function and relation symbols of a language |
| Term | A variable, a constant, or a function symbol applied to terms; it names an object |
| Atomic formula | A relation symbol or = applied to terms, such as x · y = e |
| Free and bound variable | A variable outside, or inside, the scope of a quantifier on it |
| Sentence | A formula with no free variables |
| Structure | A non-empty domain with an interpretation of each symbol |
| M ⊨ φ | The sentence φ is true in the structure M |
| Valid | True in every structure for its signature |
| Second-order logic | Logic that also quantifies over subsets, relations and functions |

## How it fits

- **Below:** [Propositional Logic](propositional-logic.md) supplies the connectives and the recursive definition of truth.
- **Above:** analysis is written in quantified formulas ([Sequences and Limits](../../06-real-analysis/01-limits-and-convergence/sequences-and-limits.md), [Continuity](../../06-real-analysis/01-limits-and-convergence/continuity.md)); the axioms of [Zermelo–Fraenkel Set Theory](../../01-sets-and-foundations/03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md) are first-order sentences in the single relation symbol ∈; [Models and the Löwenheim–Skolem Theorems](../../13-structure-and-metamathematics/03-model-theory-and-independence/models-and-the-lowenheim-skolem-theorems.md) studies which structures a set of sentences can have.
- **Siblings:** [Formal Proof Systems](formal-proof-systems.md) adds rules for ∀ and ∃; [Soundness, Completeness and Compactness](soundness-completeness-and-compactness.md) proves that those rules capture ⊨ exactly.

## Common misconceptions

- **"∀x ∃y and ∃y ∀x say the same"**: ∀x ∃y (y > x) is true in ℕ, while ∃y ∀x (y > x) is false, since no number exceeds itself.
- **"First-order logic is too weak for real mathematics"**: Zermelo–Fraenkel set theory is a first-order theory in which statements about all subsets of ℕ or ℝ become statements about sets; what no first-order theory can do is pin down an infinite structure up to isomorphism.
- **"A sentence is simply true or false"**: truth is relative to a structure; ∀x ∃y (x · y = 1) holds in the non-zero rationals and fails in the non-zero integers, where 2 has no inverse.

## Go deeper

- Herbert B. Enderton, *A Mathematical Introduction to Logic* (2nd edition, 2001), chapter 2: first-order languages, structures and Tarski's definition of truth.
- Jean van Heijenoort (editor), *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931* (1967): the founding papers, starting with Frege's *Begriffsschrift*, where the modern quantifier was born.
