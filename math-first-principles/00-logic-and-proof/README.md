# 00 Logic and Proof

> **Layer:** 00 Logic and Proof (the deductive root of the tree)
> **Children:** [Formal Logic](01-formal-logic/README.md) · [Methods of Proof](02-methods-of-proof/README.md) · [The Axiomatic Method](03-the-axiomatic-method/README.md)

## What this area is about

Mathematics is the subject in which statements are established by proof. This layer asks what a proof is, which arguments are valid, and what can be known about a system of axioms as a whole. Its first area makes logic precise: a formal language, a definition of truth in a structure, and mechanical rules of derivation. Its second area is the working mathematician's version: the handful of proof shapes (direct, contrapositive, contradiction, cases, construction, counterexample, induction) from which almost every proof is assembled. Its third area treats axiom systems as objects, asking whether they are consistent, which statements they leave undecided, and what changes when the logic itself is weakened.

The spine running through all three is the distinction between syntax and semantics. Γ ⊢ φ says that φ can be derived from Γ by the rules; Γ ⊨ φ says that φ is true in every structure in which Γ is true. The soundness and completeness theorems show that for first-order logic the two coincide, so a finite derivation settles a question about all structures, and a single countermodel shows that no derivation exists.

## Why this layer sits here

Logic and proof form one of the two roots of the tree, with [01 Sets and Foundations](../01-sets-and-foundations/README.md). Logic says how to reason; sets say what is reasoned about. Neither reduces to the other without circularity: Zermelo–Fraenkel set theory is a theory written in first-order logic, while the semantics of logic, in which a model is a set with relations on it, is written in sets. The tree makes the circle explicit through one narrow link: only the leaf on [soundness, completeness and compactness](01-formal-logic/soundness-completeness-and-compactness.md) builds on layer 01, and only on its basic leaves about sets and relations. Everything else in this layer builds on nothing outside it.

Every layer above uses this one. Each proof in the tree is an instance of a method from the methods of proof, each axiom system (the Peano axioms, the group axioms, the axioms of a metric space or a probability space) is an instance of the axiomatic method, and the metamathematics of [13 Structure and Metamathematics](../13-structure-and-metamathematics/README.md) is formal logic turned on mathematics itself.

The one idea this layer contributes is **proof as the standard of truth, with provability and truth in all models shown to agree**.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Formal Logic](01-formal-logic/README.md) | The languages, the semantics ⊨, the proof systems ⊢, and the theorems joining them | nothing earlier, except basic sets for soundness |
| [Methods of Proof](02-methods-of-proof/README.md) | How proofs are written in practice, and why each method is valid | Formal Logic (propositional, predicate, proof systems) |
| [The Axiomatic Method](03-the-axiomatic-method/README.md) | Axiom systems as objects: consistency, independence, constructive logic | both, including soundness and completeness |

```
  Propositional ─► Predicate ─► Formal Proof Systems ──────────┐
                       │                                        ▼
                       └──► Methods of Proof ──(induction)──► Soundness, Completeness   ◄── 01: sets,
                              (what a proof is, direct,         and Compactness              relations,
                               cases, induction)                      │                      functions
                                    │                                 ▼
                                    └──────────────────────► The Axiomatic Method
                                                             (axioms, consistency,
                                                              constructive logic)
```

The first three formal-logic leaves and the methods of proof form the base, building only on each other. The soundness leaf joins syntax and semantics, using induction from the methods of proof and sets from layer 01. The axiomatic method sits on top, because consistency and independence are proved with models and therefore need soundness and completeness.

## Connections to neighbouring layers

- **[01 Sets and Foundations](../01-sets-and-foundations/README.md):** the twin root. Its paradoxes, Zermelo–Fraenkel set theory and the axiom of choice are the axiomatic method applied to sets; its transfinite induction extends induction beyond ℕ.
- **[02 Number Systems](../02-number-systems/README.md):** the Peano axioms make induction an axiom, and Euclid's proof of infinitely many primes is the model direct argument.
- **[03 Combinatorics and Graph Theory](../03-combinatorics-and-graph-theory/README.md):** pigeonhole, double counting and the probabilistic method are the richest source of non-constructive existence proofs, and the four colour theorem is the classic computer-assisted case analysis.
- **[06 Real Analysis](../06-real-analysis/README.md):** ε–δ definitions are where quantifier order first matters in practice, and the extreme value theorem is the standard example of why each hypothesis needs a counterexample.
- **[08 Geometry](../08-geometry/README.md):** Euclid's *Elements* and Hilbert's axioms are the origin of the axiomatic method, and the parallel postulate is the classic independence result.
- **[13 Structure and Metamathematics](../13-structure-and-metamathematics/README.md):** incompleteness, computability, model theory, forcing and homotopy type theory are this layer studied at full depth. Completeness of first-order logic here does not conflict with incompleteness of arithmetic there: the first is about the logic, the second about theories.
- **[15 Mathematics in Context](../15-mathematics-in-context/README.md):** how proofs are discovered, what they establish philosophically, and how computers now find and check them.

## Connections across layers

Beyond the neighbours above, every layer uses this one through its axioms and its proofs. Outside mathematics, the same logic underlies circuits, satisfiability solvers, type systems and program verification ([Logic in computer science](../../cs-first-principles/01-mathematical-foundations/01-logic/README.md)), and the contrast between proof and graded empirical evidence is what separates mathematics from the sciences.

## Cross-cutting threads

- [Completeness and compactness](../CROSS-CUTTING.md#completeness-and-compactness): Gödel's completeness theorem and the compactness theorem of first-order logic.
- [Induction and recursion](../CROSS-CUTTING.md#induction-and-recursion): mathematical and structural induction, and recursive definitions of formulas and proofs.
- [Impossibility and obstruction](../CROSS-CUTTING.md#impossibility-and-obstruction): countermodels, independence proofs and proofs by contradiction show that something cannot exist.
- [Existence and construction](../CROSS-CUTTING.md#existence-and-construction): constructive and non-constructive existence, made precise by intuitionistic logic.
- [Duality](../CROSS-CUTTING.md#duality): syntax and semantics, ∧ and ∨, ∀ and ∃.
- [Abstraction and generalisation](../CROSS-CUTTING.md#abstraction-and-generalisation): axioms with many models let one proof cover every instance.
