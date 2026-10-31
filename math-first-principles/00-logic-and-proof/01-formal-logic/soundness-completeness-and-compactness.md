# Soundness, Completeness and Compactness

> **Layer:** [00 Logic and Proof](../README.md) › [Formal Logic](README.md)
> **Builds on:** [Formal Proof Systems](formal-proof-systems.md), [Predicate Logic and Quantifiers](predicate-logic-and-quantifiers.md), [Mathematical Induction](../02-methods-of-proof/mathematical-induction.md), [Sets and Set Operations](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md), [Relations and Orders](../../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md)
> **Enables:** [Axioms, Definitions and Theorems](../03-the-axiomatic-method/axioms-definitions-and-theorems.md), [Consistency and Independence](../03-the-axiomatic-method/consistency-and-independence.md), [Models and the Löwenheim–Skolem Theorems](../../13-structure-and-metamathematics/03-model-theory-and-independence/models-and-the-lowenheim-skolem-theorems.md), [Gödel's Incompleteness Theorems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md), [Natural Numbers and the Peano Axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md)

## Essence

Soundness says that a proof system derives only consequences: if Γ ⊢ φ then Γ ⊨ φ. Completeness says it derives all of them: if Γ ⊨ φ then Γ ⊢ φ, which Gödel proved for first-order logic in his doctoral thesis of 1929, published in 1930. Together they make "provable" and "true in every model" one notion: a question about all structures is settled by a finite derivation, and an unprovable sentence fails in some model. Compactness follows: a set of sentences has a model if each finite part does. None of this conflicts with Gödel's incompleteness theorem of 1931, which concerns theories such as arithmetic, not the logic.

## Core tenets

1. **Soundness: the rules preserve truth.** By induction on derivations: every axiom is valid, and each rule turns formulas true in a structure under every assignment into another such formula. So a theory with a model is consistent: φ and ¬φ cannot both hold in it. This is how one shows that something is not provable: exhibit a structure where it fails.

2. **Completeness: every consequence has a derivation.** Equivalently, every consistent set of sentences has a model: if Γ ⊬ φ, then Γ ∪ {¬φ} is consistent, its model shows Γ ⊭ φ. Henkin (1949) gave the proof now taught, building the model from syntax:

```
1. Add new constants c with axioms ∃x φ(x) ⇒ φ(c), one for every formula ∃x φ(x), new constants included.
2. Extend to a maximal consistent set Δ: for each sentence ψ, put ψ or ¬ψ into Δ (Lindenbaum's lemma).
3. Domain: the closed terms, with t and s identified when t = s is in Δ.
4. Truth lemma, by induction on formulas: the structure satisfies ψ if and only if ψ ∈ Δ.
```

Step 3 is a quotient by an [equivalence relation](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md); uncountable languages need a form of [the axiom of choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md) in step 2.

3. **Compactness: if every finite subset has a model, so does the whole set.** If Γ had no model, completeness would give a derivation of a contradiction from Γ; a derivation uses finitely many premises Γ₀, and by soundness Γ₀ would have no model. The name is topological: the complete theories of a language form a space whose [compactness](../../07-topology/01-point-set-topology/compactness.md) is exactly this theorem.

4. **Compactness limits what first-order sentences can say.** Let λₙ say "there are at least n elements". If Γ has arbitrarily large finite models, Γ ∪ {λ₁, λ₂, …} is finitely satisfiable, so it has an infinite model: no set of first-order sentences holds in exactly the finite structures. Add a constant c and the sentences c > 0, c > 1, c > 2, … to all sentences true in ℕ: every finite part holds in ℕ with c large, so the whole set has a model, a nonstandard model with an element above every numeral.

5. **Compactness also builds objects.** Robinson's nonstandard analysis (1961) applies the same argument to ℝ, giving an ordered field with infinitesimals that satisfies every first-order truth about ℝ in a rich language, so limits become infinitely small quantities. By the de Bruijn–Erdős theorem (1951), an infinite graph is k-colourable, for finite k, if every finite subgraph is: the sentences "each vertex gets exactly one colour" and "adjacent vertices differ" are finitely satisfiable. This is the [local-to-global](../../CROSS-CUTTING.md#local-to-global) pattern in its purest form.

6. **Completeness of the logic is not completeness of a theory.** Gödel's completeness theorem is about the logic: whatever holds in every model of some axioms is derivable from them. A theory T is complete in another sense if, for every sentence φ, it proves φ or proves ¬φ. Gödel's first incompleteness theorem (1931), in the form Rosser gave it in 1936, says that no consistent theory that contains enough arithmetic and whose axioms can be listed by an algorithm is complete in this second sense ([Gödel's Incompleteness Theorems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md)). The two fit together: if T proves neither G nor ¬G, completeness gives models of T where G is true and where it is false, and "true but unprovable" means true in ℕ but false in some nonstandard model. Complete theories exist, such as algebraically closed fields of fixed characteristic and real closed fields ([Quantifier Elimination and Decidable Theories](../../13-structure-and-metamathematics/03-model-theory-and-independence/quantifier-elimination-and-decidable-theories.md)).

7. **Stronger logics lose these theorems.** Second-order logic pins down ℕ up to isomorphism, so by tenet 4's argument it is not compact, and it has no sound, complete, effective proof system, whose finite derivations would give compactness. Lindström (1969) showed the trade-off is forced: no logic properly extending first-order logic has both compactness and the downward Löwenheim–Skolem property (a sentence with an infinite model has a countably infinite one).

## Key concepts

| Term | Meaning |
|---|---|
| Γ ⊢ φ | φ is derivable from Γ in a fixed proof system |
| Γ ⊨ φ | φ is true in every structure in which all of Γ is true |
| Soundness | Γ ⊢ φ implies Γ ⊨ φ |
| Completeness of the logic | Γ ⊨ φ implies Γ ⊢ φ |
| Complete theory | A theory proving φ or ¬φ for every sentence φ |
| Compactness | A set of sentences has a model if every finite subset does |
| Nonstandard model | A model of the truths of ℕ not isomorphic to ℕ |

## How it fits

- **Below:** [Formal Proof Systems](formal-proof-systems.md) supplies ⊢ and [Predicate Logic and Quantifiers](predicate-logic-and-quantifiers.md) supplies ⊨; both proofs are inductions ([Mathematical Induction](../02-methods-of-proof/mathematical-induction.md)) and build structures from [sets](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md) and [relations](../../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md).
- **Above:** [Consistency and Independence](../03-the-axiomatic-method/consistency-and-independence.md) proves consistency with one model and independence with two; [Models and the Löwenheim–Skolem Theorems](../../13-structure-and-metamathematics/03-model-theory-and-independence/models-and-the-lowenheim-skolem-theorems.md) continues the story; nonstandard models exist because the induction schema of [the Peano axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md) is first-order.
- **Siblings:** [Propositional Logic](propositional-logic.md) has its own completeness theorem, proved by Post in 1921; [Formal Proof Systems](formal-proof-systems.md) gives systems that are all complete by this theorem.

## Common misconceptions

- **"Gödel proved that logic is incomplete"**: he proved first-order logic complete in 1930; his incompleteness theorems of 1931 concern theories containing arithmetic.
- **"Completeness means every truth about ℕ is provable"**: it yields derivations only of sentences true in every model of the axioms, not of truths of ℕ that fail in a nonstandard model.
- **"Compactness is about finite structures"**: it is about finite sets of sentences, and its typical use is to build infinite structures.

## Go deeper

- Leon Henkin, "The Completeness of the First-Order Functional Calculus" (1949), *Journal of Symbolic Logic*: the proof now taught everywhere.
- Torkel Franzén, *Gödel's Theorem: An Incomplete Guide to Its Use and Abuse* (2005): what incompleteness does and does not say.
