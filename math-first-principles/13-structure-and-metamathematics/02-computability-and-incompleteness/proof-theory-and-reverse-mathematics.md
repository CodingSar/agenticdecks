# Proof Theory and Reverse Mathematics

> **Layer:** [13 Structure and Metamathematics](../README.md) › [Computability and incompleteness](README.md)
> **Builds on:** [Formal proof systems](../../00-logic-and-proof/01-formal-logic/formal-proof-systems.md), [Ordinal numbers and transfinite induction](../../01-sets-and-foundations/02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md), [Ramsey theory](../../03-combinatorics-and-graph-theory/04-extremal-combinatorics/ramsey-theory.md), [Compactness in metric spaces](../../06-real-analysis/03-metric-spaces/compactness-in-metric-spaces.md), [Gödel's incompleteness theorems](godels-incompleteness-theorems.md)
> **Enables:** [Large cardinals](../03-model-theory-and-independence/large-cardinals.md), [Proof assistants and dependent types](../../../cs-first-principles/06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md), [Computers and proof](../../15-mathematics-in-context/computers-and-proof.md), [Philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md)

## Essence

After Gödel, the useful question is no longer whether a theory proves its own consistency but how strong a theory must be to prove a given theorem. Proof theory treats proofs as finite combinatorial objects and measures the strength of theories, often by an ordinal: Gerhard Gentzen proved the consistency of Peano arithmetic (PA) by transfinite induction up to the ordinal ε₀. Reverse mathematics asks, for an ordinary theorem of analysis or algebra, which axioms are needed to prove it, and finds that most theorems are equivalent to one of five subsystems of second-order arithmetic. Statements such as the Paris–Harrington theorem show that PA leaves natural combinatorial questions open.

## Core tenets

1. **Cut elimination makes proofs direct.** Gentzen's sequent calculus (1935) has a cut rule, which uses a lemma A to pass from Γ ⊢ A and A, Δ ⊢ B to Γ, Δ ⊢ B. His Hauptsatz says that cuts can be removed, so every provable sequent has a proof using only subformulas of its conclusion; consistency of pure logic follows, since no such proof ends in the empty sequent. The price is size: cut-free proofs can be longer by a tower of exponentials, as Richard Statman and Vladimir Orevkov showed in 1979.

2. **PA is consistent by induction up to ε₀.** In 1936 Gentzen assigned to each derivation of a contradiction in PA an ordinal below ε₀, the least ordinal with ω^ε = ε, and gave a reduction step that turns it into another such derivation with a smaller ordinal. Since ordinals are well-ordered there is no such derivation. The steps are finitary, formalisable in primitive recursive arithmetic (PRA); the one non-finitary ingredient is the well-ordering of ε₀, which by the second incompleteness theorem PA cannot prove.

3. **Ordinals measure theories.** Gentzen showed in 1943 that PA proves transfinite induction up to each ordinal below ε₀ but not up to ε₀ itself, so ε₀ is the proof-theoretic ordinal of PA. Weaker and stronger theories get smaller and larger ordinals: ω^ω for PRA, Γ₀ for arithmetical transfinite recursion. Ordinal analyses of stronger systems, such as Π¹₁ comprehension, exist; for full second-order arithmetic none is generally accepted as of 2026.

4. **Reverse mathematics finds the axioms a theorem needs.** Harvey Friedman (1975) and Stephen Simpson worked over a weak base, RCA₀ (the recursive comprehension axiom: Σ⁰₁ induction and the existence of computable sets), and proved theorems equivalent to stronger axioms. Most classical theorems about countable or separable objects fall into five systems, the "Big Five":

   | System | Typical equivalent theorems |
   |---|---|
   | RCA₀ | intermediate value theorem; countable fields have algebraic closures |
   | WKL₀ (weak König's lemma) | Heine–Borel for [0, 1]; continuous functions on [0, 1] are bounded; completeness theorem; prime ideals exist |
   | ACA₀ (arithmetical comprehension) | Bolzano–Weierstrass; vector spaces have bases; maximal ideals exist; Ramsey's theorem for triples |
   | ATR₀ (arithmetical transfinite recursion) | comparability of countable well-orderings; perfect set theorem |
   | Π¹₁-CA₀ (Π¹₁ comprehension) | Cantor–Bendixson theorem; abelian groups split as divisible ⊕ reduced |

   The best-known exception is Ramsey's theorem for pairs in two colours (RT²₂). David Seetapun (1995) showed it does not imply ACA₀, Jiayi Liu (2012) that it does not imply WKL₀, and Carl Jockusch (1972) that WKL₀ does not prove it, so it lies outside the Big Five.

5. **Strong-looking theories can be conservative over weak ones.** ACA₀ proves exactly the same arithmetical sentences as PA. WKL₀ proves no more Π¹₁ sentences than RCA₀ (Leo Harrington) and no more Π⁰₂ sentences than PRA (Friedman), so the compactness arguments of WKL₀ are finitistically justified in Hilbert's sense for statements of that form.

6. **Goodstein's theorem is true but unprovable in PA.** Write n in hereditary base 2, replace every 2 by 3 and subtract 1; write the result in hereditary base 3, replace 3 by 4 and subtract 1; and so on. From 4 the sequence runs 4, 26, 41, 60, 83, … and reaches 0 only after more than 10^(100,000,000) steps. Reuben Goodstein (1944) proved that every such sequence reaches 0: replacing the base by ω gives ordinals ω^ω, ω²·2 + ω·2 + 2, ω²·2 + ω·2 + 1, ω²·2 + ω·2, ω²·2 + ω + 5, …, which strictly decrease below ε₀. Laurie Kirby and Jeff Paris (1982) showed PA cannot prove it.

7. **The Paris–Harrington theorem is a natural independent statement.** Jeff Paris and Leo Harrington (1977) modified the finite Ramsey theorem by asking that the homogeneous set H satisfy |H| ≥ min H. The modified statement follows from the infinite Ramsey theorem and compactness, but over PA it implies Con(PA), so PA does not prove it. Empirically, as of 2026, natural theories are linearly ordered by consistency strength, though no theorem explains why.

## Key concepts

| Term | Meaning |
|---|---|
| Cut elimination | Removing lemmas from proofs, leaving only subformulas of the conclusion |
| ε₀ | The limit of ω, ω^ω, ω^(ω^ω), …; the proof-theoretic ordinal of PA |
| Proof-theoretic ordinal | The least ordinal a theory cannot prove well-founded |
| Second-order arithmetic | A theory of natural numbers and sets of natural numbers |
| Conservative extension | A stronger theory that proves no new sentences of a given form |
| Reversal | A proof, over RCA₀, that a theorem implies the axioms used to prove it |

## How it fits

- **Below:** It studies [formal proofs](../../00-logic-and-proof/01-formal-logic/formal-proof-systems.md) with [transfinite induction](../../01-sets-and-foundations/02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md), and calibrates theorems such as [Ramsey's](../../03-combinatorics-and-graph-theory/04-extremal-combinatorics/ramsey-theory.md) and [Heine–Borel](../../06-real-analysis/03-metric-spaces/compactness-in-metric-spaces.md).
- **Above:** Cut elimination is evaluation in [proof assistants](../../../cs-first-principles/06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md), and the [philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md) uses reverse mathematics to weigh partial versions of Hilbert's programme.
- **Siblings:** It refines [Gödel's theorems](godels-incompleteness-theorems.md) into a scale of strength that continues upward through [large cardinals](../03-model-theory-and-independence/large-cardinals.md).

## Common misconceptions

- **"Gentzen's proof is circular because it uses something stronger than PA."**: It must, by the second theorem; the point is that the extra principle, induction along one explicit well-ordering, is clearer than the full strength of PA.
- **"Independent statements are always self-referential."**: Goodstein's and the Paris–Harrington theorems are ordinary statements about numbers and colourings.

## Go deeper

- Stephen Simpson, *Subsystems of Second Order Arithmetic* (1999; 2nd edition 2009): the reference for reverse mathematics.
- John Stillwell, *Reverse Mathematics: Proofs from the Inside Out* (2018): a gentle introduction.
- Jean-Yves Girard, Yves Lafont and Paul Taylor, *Proofs and Types* (1989): cut elimination and the logic of programs.
