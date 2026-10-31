# Consistency and Independence

> **Layer:** [00 Logic and Proof](../README.md) › [The Axiomatic Method](README.md)
> **Builds on:** [Axioms, Definitions and Theorems](axioms-definitions-and-theorems.md), [Soundness, Completeness and Compactness](../01-formal-logic/soundness-completeness-and-compactness.md), [Direct Proof, Contraposition and Contradiction](../02-methods-of-proof/direct-proof-contraposition-and-contradiction.md)
> **Enables:** [Non-Euclidean Geometry](../../08-geometry/01-classical-geometry/non-euclidean-geometry.md), [The Axiom of Choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md), [Forcing and Independence](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md), [Gödel's Incompleteness Theorems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md), [Large Cardinals](../../13-structure-and-metamathematics/03-model-theory-and-independence/large-cardinals.md)

## Essence

An axiom system is consistent if it does not prove a contradiction, and a statement is independent of it if the system proves neither the statement nor its negation. Both are established with models. By soundness, a system with a model is consistent; by completeness, a consistent first-order system has one. So consistency is shown by building one model, and independence by building two: one where the statement holds and one where it fails. The parallel postulate is the classic case, and the axiom of choice and the continuum hypothesis are the modern ones.

## Core tenets

1. **An inconsistent system proves everything.** From φ and ¬φ any statement follows (ex falso), so an inconsistent theory has no content. Frege's *Grundgesetze der Arithmetik* (two volumes, 1893 and 1903) derived arithmetic from logic, but Russell's letter of 1902 showed that its Basic Law V yields the set of all sets that are not members of themselves, and hence a contradiction ([Paradoxes and Naive Set Theory](../../01-sets-and-foundations/03-axiomatic-set-theory/paradoxes-and-naive-set-theory.md)).

2. **A model proves consistency.** If some structure satisfies every axiom, soundness forbids a derivation of φ ∧ ¬φ, since no structure satisfies that. The group axioms are consistent because the one-element group {e}, with e · e = e, satisfies them. A finite model, checked by hand, is as secure a consistency proof as there can be.

3. **Most consistency proofs are relative.** Infinite systems need infinite models, built inside some other theory, so the result reads "if that theory is consistent, so is this one". Hilbert's model of plane geometry, with points as pairs of real numbers and lines as solution sets of linear equations, shows Euclidean geometry consistent if the real numbers are. In practice the base theory is ZFC, Zermelo–Fraenkel set theory with the axiom of choice, in which almost all mathematics can be modelled.

4. **Independence takes two models.** Commutativity, xy = yx, is independent of the group axioms: the integers under addition form a group in which it holds, and the six permutations of three objects under composition form one in which it fails. By soundness, neither commutativity nor its negation can be derived. The same pattern, one model each way, is how every independence result is proved.

5. **The parallel postulate is independent of Euclid's other axioms.** In Playfair's form it says that through a point not on a line there is exactly one parallel. Saccheri (1733) tried to prove it by contradiction, deriving strange consequences of its negation that he took to be absurd. Lobachevsky (1829) and Bolyai (1832) developed those consequences into hyperbolic geometry, and Beltrami (1868) gave a model of it inside Euclidean geometry, showing it consistent if Euclidean geometry is. In the Poincaré disc model, points are those inside a disc and lines are diameters and circular arcs meeting the boundary at right angles; through a point off a line pass infinitely many parallels ([Non-Euclidean Geometry](../../08-geometry/01-classical-geometry/non-euclidean-geometry.md)).

6. **Set theory has independent statements of its own.** Gödel (1938) built the constructible universe L, a model of ZF (Zermelo–Fraenkel set theory without choice) in which the axiom of choice and the continuum hypothesis both hold. Cohen (1963) invented forcing to build models where they fail. Together: if ZF is consistent, the axiom of choice is independent of ZF, and the continuum hypothesis is independent of ZFC ([The Axiom of Choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md), [Forcing and Independence](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md)).

7. **A theory cannot certify its own consistency.** Gödel's second incompleteness theorem (1931) says that a consistent theory containing enough arithmetic, with algorithmically listable axioms, cannot prove the sentence Con(T) expressing its own consistency ([Gödel's Incompleteness Theorems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md)). Consistency is therefore proved from stronger assumptions. Gentzen (1936) proved Peano arithmetic consistent using induction along the ordinals up to ε₀; ZFC plus the existence of an inaccessible cardinal proves Con(ZFC). Theories are ranked by consistency strength, which the [large cardinals](../../13-structure-and-metamathematics/03-model-theory-and-independence/large-cardinals.md) calibrate.

8. **Independence reaches ordinary mathematics.** Goodstein's theorem, about sequences of natural numbers that eventually reach 0, is provable in ZFC but, as Kirby and Paris showed in 1982, not in Peano arithmetic. Whether new axioms should settle the continuum hypothesis is debated as of 2026. Independence results are [impossibility](../../CROSS-CUTTING.md#impossibility-and-obstruction) theorems: they show that no proof can exist.

## Key concepts

| Term | Meaning |
|---|---|
| Consistent | Proving no statement together with its negation |
| Satisfiable | Having a model; equivalent to consistent in first-order logic |
| Relative consistency | Consistency of one theory on the assumption that another is consistent |
| Independent | Neither provable nor refutable from the given axioms |
| Con(T) | An arithmetic sentence expressing that T is consistent |
| Consistency strength | The ordering of theories by which proves the consistency of which |
| Parallel postulate | Through a point off a line passes exactly one parallel |

## How it fits

- **Below:** [Axioms, Definitions and Theorems](axioms-definitions-and-theorems.md) poses the questions; [Soundness, Completeness and Compactness](../01-formal-logic/soundness-completeness-and-compactness.md) turns them into questions about models; [Direct Proof, Contraposition and Contradiction](../02-methods-of-proof/direct-proof-contraposition-and-contradiction.md) gives ex falso.
- **Above:** [Non-Euclidean Geometry](../../08-geometry/01-classical-geometry/non-euclidean-geometry.md) develops the geometries; [Forcing and Independence](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md), [Gödel's Incompleteness Theorems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md) and [Large Cardinals](../../13-structure-and-metamathematics/03-model-theory-and-independence/large-cardinals.md) carry the subject into metamathematics.
- **Siblings:** [Constructive and Intuitionistic Logic](constructive-and-intuitionistic-logic.md) shows that excluded middle is itself independent of the intuitionistic rules.

## Common misconceptions

- **"An independent statement is neither true nor false"**: it is true in some models of the axioms and false in others; a statement about ℕ independent of Peano arithmetic, such as Goodstein's theorem, can still be true in ℕ.
- **"A consistency proof shows the axioms are true"**: it shows that they have a model, usually relative to another theory whose consistency is assumed.
- **"Gödel showed arithmetic might be inconsistent"**: he showed that its consistency cannot be proved within arithmetic; proofs from stronger principles, such as Gentzen's, exist.

## Go deeper

- Marvin Jay Greenberg, *Euclidean and Non-Euclidean Geometries* (4th edition, 2008): the parallel postulate and its models.
- Kenneth Kunen, *Set Theory: An Introduction to Independence Proofs* (1980): Gödel's L and Cohen's forcing.
- Torkel Franzén, *Gödel's Theorem: An Incomplete Guide to Its Use and Abuse* (2005): what the second incompleteness theorem does and does not say.
