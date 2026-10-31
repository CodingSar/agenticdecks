# Computers and Proof

> **Layer:** [15 Mathematics in Context](README.md)
> **Builds on:** [Formal Proof Systems](../00-logic-and-proof/01-formal-logic/formal-proof-systems.md), [Type Theory and Alternative Foundations](../01-sets-and-foundations/03-axiomatic-set-theory/type-theory-and-alternative-foundations.md), [Colouring and Planarity](../03-combinatorics-and-graph-theory/02-graph-theory/colouring-and-planarity.md), [Lattices and Sphere Packing](../08-geometry/03-convex-and-discrete-geometry/lattices-and-sphere-packing.md), [Mathematical Practice and Discovery](mathematical-practice-and-discovery.md)
> **Enables:** [Open Problems](open-problems.md), [Mathematics and Society](mathematics-and-society.md), [Proof Assistants and Dependent Types (CS)](../../cs-first-principles/06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md)

## Essence

Computers entered mathematical proof in three ways. First, as calculators doing case checks too large for humans, starting with the four colour theorem in 1976. Second, as proof checkers: proof assistants such as Lean, Rocq (formerly Coq) and Isabelle verify every logical step of a proof written in a formal language, reducing trust to a small kernel. Third, recently, as sources of ideas: machine learning systems now find constructions and write proofs of competition problems. Each raised the question of how to trust a proof no single person can check; for long proofs, formal checking is now more reliable than refereeing, provided the formal statement says what was meant.

## Core tenets

1. **The four colour theorem was the first major computer-assisted proof.** Kenneth Appel and Wolfgang Haken (1976) showed that every planar map can be coloured with four colours by exhibiting an unavoidable set of configurations, one of which must occur in any minimal counterexample, and checking by computer that each is reducible. Nearly two thousand configurations were checked. Neil Robertson, Daniel Sanders, Paul Seymour and Robin Thomas (1997) simplified the proof to 633 configurations, and Georges Gonthier (2005) formalised the whole theorem in Coq, removing doubts about the programs.

2. **The Kepler conjecture showed refereeing reaching its limit.** Thomas Hales announced in 1998 a proof that no packing of equal spheres is denser than the familiar stacking of oranges, combining hand arguments with extensive computer optimisation. The referees of the *Annals of Mathematics* reported they were very confident but could not certify every computation; it was published in 2005. Hales then led the Flyspeck project, which completed a formal proof in the HOL Light and Isabelle proof assistants in 2014.

3. **SAT solvers prove finite statements by exhaustive search with certificates.** A satisfiability (SAT) solver decides whether a Boolean formula can be made true. Marijn Heule, Oliver Kullmann and Victor Marek (2016) showed that {1, …, 7825} cannot be split into two parts without a part containing a Pythagorean triple a² + b² = c², while {1, …, 7824} can; the proof certificate was about 200 terabytes. Heule (2017) found the Schur number S(5) = 160 the same way. Such certificates are checked by small, independently verified programs, so trust shifts from the solver to the checker.

4. **Proof assistants reduce trust to a small kernel.** In a proof assistant, definitions, statements and proofs are written in a formal language, usually a dependent type theory, and a kernel checks each inference. Following N. G. de Bruijn's criterion, the kernel is small enough to inspect, so elaborate automation can be untrusted: whatever it produces is rechecked. Isabelle and HOL Light rest on higher-order logic; Rocq, renamed from Coq in 2025, and Lean, started by Leonardo de Moura in 2013, rest on dependent type theory, linked by the Curry–Howard correspondence to programs. [Homotopy type theory](../13-structure-and-metamathematics/01-category-theory/higher-categories-and-homotopy-type-theory.md) offers an alternative foundation designed for such systems. Gonthier's team formalised the Feit–Thompson odd order theorem in Coq in 2012.

5. **Formalisation has reached current research.** Lean's community library mathlib covers much of undergraduate and some graduate mathematics. In December 2020 Peter Scholze challenged formalisers to check a key theorem of his work with Dustin Clausen on condensed mathematics; the Liquid Tensor Experiment, led by Johan Commelin, verified the crucial part by June 2021 and completed it in July 2022. When Timothy Gowers, Ben Green, Freddie Manners and Terence Tao proved the polynomial Freiman–Ruzsa conjecture in November 2023, a collaborative effort formalised the proof in Lean in about three weeks.

6. **Machine learning now contributes constructions and proofs.** Google DeepMind's FunSearch (December 2023) used a language model inside an evolutionary search to find larger cap sets in dimension 8 than previously known. AlphaGeometry (January 2024) solved 25 of 30 olympiad geometry problems from a benchmark set. At the International Mathematical Olympiad (IMO) in July 2024, AlphaProof, whose proofs were checked in Lean, and AlphaGeometry 2 together reached silver-medal standard. In July 2025 a Google DeepMind system, graded by IMO coordinators, and an OpenAI system, by its own report, reached gold-medal standard with natural-language proofs. How far such systems contribute to research mathematics is actively debated as of 2026.

7. **A formal proof is only as good as its statement.** The kernel guarantees that the formal statement follows from the formal axioms. It cannot guarantee that the formal statement means what the informal theorem says: a wrong definition can make a "proof" vacuous. This specification gap is narrowed by human review of statements, which are short, rather than of proofs, which may be enormous.

## Key concepts

| Term | Meaning |
|---|---|
| Computer-assisted proof | A proof in which part of the argument is a computation too large to check by hand |
| Unavoidable set | A list of configurations at least one of which appears in every planar map |
| SAT solver | A program deciding satisfiability of Boolean formulas, often emitting a checkable certificate |
| Proof assistant | Software in which proofs are written formally and checked step by step |
| Kernel | The small trusted core of a proof assistant that checks every inference |
| de Bruijn criterion | Only a small checker need be trusted; automation is rechecked |
| mathlib | The community library of formalised mathematics for Lean |
| Specification gap | The possibility that a formal statement does not mean what was intended |

## How it fits

- **Below:** formal proof systems and type theory are what proof assistants implement; colouring and sphere packing supplied the first landmark cases; [practice](mathematical-practice-and-discovery.md) explains the human checking that computers supplement.
- **Above:** nothing; this is the top layer.
- **Siblings:** [open problems](open-problems.md) are the targets for both human and machine; [mathematics and society](mathematics-and-society.md) discusses verification of software and cryptography; the computing tree's [proof assistants](../../cs-first-principles/06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md) leaf covers the engineering side.

## Common misconceptions

- **"A computer proof is less certain than a human one."** A formally checked proof is usually more reliable than a refereed long proof; the residual risk lies in the statement and the kernel.
- **"Proof assistants find proofs automatically."** Mostly humans write the proofs and the assistant checks them, with automation filling routine steps.
- **"Olympiad success means machines do research mathematics."** Competition problems have known short solutions; research requires choosing problems and inventing concepts.

## Go deeper

- T. C. Hales, "Formal Proof" (2008): a short survey by the author of the Kepler proof.
- D. MacKenzie, *Mechanizing Proof* (2001): a history of computing, risk and trust in proof.
- R. Wilson, *Four Colors Suffice* (2002): the story of the four colour theorem.
