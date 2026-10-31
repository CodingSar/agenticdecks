# Constructive and Intuitionistic Logic

> **Layer:** [00 Logic and Proof](../README.md) › [The Axiomatic Method](README.md)
> **Builds on:** [Direct Proof, Contraposition and Contradiction](../02-methods-of-proof/direct-proof-contraposition-and-contradiction.md), [Cases, Constructions and Counterexamples](../02-methods-of-proof/cases-constructions-and-counterexamples.md), [Formal Proof Systems](../01-formal-logic/formal-proof-systems.md), [Soundness, Completeness and Compactness](../01-formal-logic/soundness-completeness-and-compactness.md)
> **Enables:** [Type Theory and Alternative Foundations](../../01-sets-and-foundations/03-axiomatic-set-theory/type-theory-and-alternative-foundations.md), [Higher Categories and Homotopy Type Theory](../../13-structure-and-metamathematics/01-category-theory/higher-categories-and-homotopy-type-theory.md), [Philosophy of Mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md), [Computers and Proof](../../15-mathematics-in-context/computers-and-proof.md), [Proof Assistants and Dependent Types](../../../cs-first-principles/06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md)

## Essence

Constructive mathematics requires that a proof of existence provide the object, and that a proof of "A or B" say which. Brouwer argued for this view from the early twentieth century; Heyting formalised its logic, intuitionistic logic, in 1930. It is classical logic without the law of excluded middle (A ∨ ¬A) and without double-negation elimination (¬¬A ⇒ A). What remains is weaker but more informative: every constructive proof carries an algorithm, and through the Curry–Howard correspondence proofs become programs.

## Core tenets

1. **A proof is a construction: the Brouwer–Heyting–Kolmogorov (BHK) interpretation.** Instead of truth values, each connective is explained by what counts as a proof of it, following Heyting and Kolmogorov's reading of logic as a calculus of problems (1932):

```
A proof of    consists of
A ∧ B         a proof of A and a proof of B
A ∨ B         a proof of A or a proof of B, together with which one
A ⇒ B         a method turning any proof of A into a proof of B
¬A            a method turning any proof of A into a contradiction
∀x A(x)       a method giving, for each x, a proof of A(x)
∃x A(x)       an object a and a proof of A(a)
```

2. **Some classical laws are lost; many survive.** Without a decision between A and ¬A, A ∨ ¬A has no BHK proof in general. Lost: excluded middle, ¬¬A ⇒ A, proof by contradiction of positive statements, and ¬∀x ¬P(x) ⇒ ∃x P(x). Kept: A ⇒ ¬¬A, ¬¬¬A ⇔ ¬A, ¬(A ∨ B) ⇔ ¬A ∧ ¬B, and proving a negation by refuting its opposite. Even ¬¬(A ∨ ¬A) is provable: if ¬(A ∨ ¬A), then A would give A ∨ ¬A, so ¬A, which also gives A ∨ ¬A, a contradiction. Excluded middle cannot be refuted, only not asserted.

3. **A classical existence proof can name no witness.** Claim: there are irrational a and b with aᵇ rational. Either √2^(√2) is rational, and a = b = √2 works; or it is irrational, and a = √2^(√2), b = √2 gives aᵇ = √2² = 2. The proof does not say which case holds. (The Gelfond–Schneider theorem of 1934 shows that √2^(√2) is transcendental, so the second.) A constructive proof names the pair: a = √2 and b = log₂ 9, irrational since 2ᵖ = 9^q has no solution in positive integers, with aᵇ = 2^(log₂ 3) = 3.

4. **Weak counterexamples show what cannot be constructive.** Let r = ∑ aₙ 2⁻ⁿ, where aₙ = 1 if n is the least even number greater than 2 that is not a sum of two primes, and aₙ = 0 otherwise. Each digit is computable, but deciding r = 0 or r ≠ 0 would settle Goldbach's conjecture, open as of 2026. So "every real number is zero or non-zero" is not constructively provable, and the intermediate value theorem survives only approximately: for every ε > 0 there is x with |f(x)| < ε.

5. **Intuitionistic logic has its own sound and complete semantics.** Kripke (1965) gave models in which knowledge grows along stages and A ∨ ¬A fails at a stage where A is not yet known. Open sets give another: interpret propositions as open subsets of ℝ, ∨ as union and ¬U as the interior of the complement. With A = (0, ∞), ¬A = (−∞, 0) and A ∨ ¬A is ℝ minus the point 0, not all of ℝ. Gödel (1932) showed that no finite truth table characterises intuitionistic propositional logic.

6. **Classical logic embeds in intuitionistic logic.** The Gödel–Gentzen negative translation N replaces each atomic P by ¬¬P, A ∨ B by ¬(¬A ∧ ¬B) and ∃x A by ¬∀x ¬A. A classical proof of φ yields an intuitionistic proof of N(φ). Gödel and Gentzen used it, both in 1933, to show that Peano arithmetic is consistent if Heyting arithmetic, its intuitionistic counterpart, is ([Consistency and Independence](consistency-and-independence.md)).

7. **Proofs are programs: the Curry–Howard correspondence.** Curry (1934) observed that the types of the basic combinators are the axioms A1 and A2 of the Hilbert system in [Formal Proof Systems](../01-formal-logic/formal-proof-systems.md). Howard (written 1969, published 1980) extended this to natural deduction: a proof of A ⇒ B is a function, of A ∧ B a pair, of A ∨ B a tagged value, and simplifying a proof is running a program in the typed [lambda calculus](../../../cs-first-principles/02-theory-of-computation/03-computability/lambda-calculus.md). Martin-Löf's dependent type theory extends this to quantifiers, and proof assistants such as Agda and Lean build on it ([Type Theory and Alternative Foundations](../../01-sets-and-foundations/03-axiomatic-set-theory/type-theory-and-alternative-foundations.md), [Higher Categories and Homotopy Type Theory](../../13-structure-and-metamathematics/01-category-theory/higher-categories-and-homotopy-type-theory.md)).

8. **Constructive mathematics is a practice, not only a logic.** Bishop's *Foundations of Constructive Analysis* (1967) showed that much of analysis can be done constructively with theorems that remain classically valid. Brouwer went further, adopting principles under which every function from ℝ to ℝ is continuous, which contradict classical mathematics. The choice between them is the [existence and construction](../../CROSS-CUTTING.md#existence-and-construction) question made precise.

## Key concepts

| Term | Meaning |
|---|---|
| Intuitionistic logic | Classical logic without excluded middle or double-negation elimination |
| BHK interpretation | Meaning of each connective given by what counts as its proof |
| Excluded middle | A ∨ ¬A for every A |
| Double-negation elimination | ¬¬A ⇒ A |
| Weak counterexample | A statement whose constructive proof would settle an open problem |
| Kripke model | A structure of growing stages of knowledge interpreting intuitionistic logic |
| Negative translation | A map N with classical ⊢ φ implying intuitionistic ⊢ N(φ) |
| Curry–Howard correspondence | Propositions as types, proofs as programs |

## How it fits

- **Below:** [Direct Proof, Contraposition and Contradiction](../02-methods-of-proof/direct-proof-contraposition-and-contradiction.md) separates proving a negation from classical contradiction; [Cases, Constructions and Counterexamples](../02-methods-of-proof/cases-constructions-and-counterexamples.md) introduces non-constructive existence; [Formal Proof Systems](../01-formal-logic/formal-proof-systems.md) supplies the rules that are dropped; [Soundness, Completeness and Compactness](../01-formal-logic/soundness-completeness-and-compactness.md) is the classical pattern the Kripke semantics repeats.
- **Above:** [Type Theory and Alternative Foundations](../../01-sets-and-foundations/03-axiomatic-set-theory/type-theory-and-alternative-foundations.md) and [Higher Categories and Homotopy Type Theory](../../13-structure-and-metamathematics/01-category-theory/higher-categories-and-homotopy-type-theory.md) build foundations on it; [Proof Assistants and Dependent Types](../../../cs-first-principles/06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md) and [Computers and Proof](../../15-mathematics-in-context/computers-and-proof.md) put it to work; [Philosophy of Mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md) weighs it.
- **Siblings:** [Axioms, Definitions and Theorems](axioms-definitions-and-theorems.md) fixes the axioms while this leaf varies the logic; [Consistency and Independence](consistency-and-independence.md) uses the negative translation for relative consistency.

## Common misconceptions

- **"Intuitionists believe A ∨ ¬A is false"**: its negation is refutable; they decline to assert it without a decision procedure.
- **"Constructive mathematics rejects proof by contradiction"**: it keeps it for proving negations, such as the irrationality of √2, and rejects only the step from ¬¬A to A.
- **"Constructive mathematics is a small fragment"**: Bishop's analysis and modern type theory cover large parts of mathematics, and every classical theorem has a constructive counterpart through the negative translation.

## Go deeper

- Dirk van Dalen, *Logic and Structure* (5th edition, 2013): intuitionistic logic and Kripke models alongside classical logic.
- Errett Bishop, *Foundations of Constructive Analysis* (1967): analysis rebuilt constructively.
- A. S. Troelstra and D. van Dalen, *Constructivism in Mathematics* (two volumes, 1988): the standard reference.
- Philip Wadler, "Propositions as Types" (2015): an accessible history of the Curry–Howard correspondence.
