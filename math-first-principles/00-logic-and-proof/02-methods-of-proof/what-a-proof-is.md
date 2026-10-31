# What a Proof Is

> **Layer:** [00 Logic and Proof](../README.md) › [Methods of Proof](README.md)
> **Builds on:** [Propositional Logic](../01-formal-logic/propositional-logic.md), [Predicate Logic and Quantifiers](../01-formal-logic/predicate-logic-and-quantifiers.md), [Formal Proof Systems](../01-formal-logic/formal-proof-systems.md)
> **Enables:** [Direct Proof, Contraposition and Contradiction](direct-proof-contraposition-and-contradiction.md), [Axioms, Definitions and Theorems](../03-the-axiomatic-method/axioms-definitions-and-theorems.md), [Mathematical Practice and Discovery](../../15-mathematics-in-context/mathematical-practice-and-discovery.md), [Computers and Proof](../../15-mathematics-in-context/computers-and-proof.md), [Philosophy of Mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md)

## Essence

A proof is a finite argument that leads from accepted starting points (axioms, definitions and earlier theorems) to a conclusion by steps that any competent reader can check. It is what separates mathematics from the empirical sciences: no number of confirming cases establishes a general statement, while one valid proof settles every case at once, given the axioms. A proof as written is informal, a compressed sketch of a formal derivation that could be supplied and that a proof assistant can now check. A good proof also explains why the statement holds.

## Core tenets

1. **Evidence is not proof.** n² + n + 41 is prime for n = 0, 1, …, 39, but at n = 40 it is 1681 = 41². Joining n points on a circle by all chords, with no three chords meeting inside, cuts the disc into 1, 2, 4, 8, 16 regions for n = 1 to 5, and into 31, not 32, for n = 6. Fermat conjectured that every 2^(2ⁿ) + 1 is prime, and the first five are; Euler found 2³² + 1 = 641 × 6,700,417. Empirical fields such as medicine must weigh and grade evidence ([Grading Evidence and Guidelines](../../../medicine-first-principles/10-epidemiology-and-evidence/02-evidence-based-medicine/grading-evidence-and-guidelines.md)); a claim about infinitely many cases is settled only by an argument covering all of them.

2. **A proof is a chain of locally checkable steps.** Each line follows from axioms, definitions, earlier theorems or earlier lines by a rule of logic, so checking a proof means checking each step, never seeing the whole truth at once. A gap is a step whose justification is missing; it may be routine, or it may hide the entire difficulty. How much may be left out depends on the reader: a proof is complete when its intended reader can fill every gap routinely.

3. **The logical form of the statement gives the skeleton of the proof.** Each connective and quantifier has a standard way to be proved and to be used, the rules of natural deduction in everyday dress ([Formal Proof Systems](../01-formal-logic/formal-proof-systems.md)):

```
To prove     start with                          To use it once known
∀x P(x)      let x be arbitrary; prove P(x)      apply it to any object
∃x P(x)      exhibit an object a; prove P(a)     name a witness, new to the argument
P ⇒ Q        assume P; prove Q                   from P conclude Q
P ∧ Q        prove P, then prove Q               use either part
P ∨ Q        prove one of them                   split into two cases
¬P           assume P; derive a contradiction    from P derive a contradiction
P ⇔ Q        prove P ⇒ Q and Q ⇒ P               replace one by the other
```

Writing out the form first usually gives the first line of the proof and says what the last line must be.

4. **A proof from axioms holds in every model of them.** A proof may use only what the axioms and definitions say, never a picture or an intended example, so its conclusion holds in every structure satisfying them; for first-order logic this is the soundness theorem ([Soundness, Completeness and Compactness](../01-formal-logic/soundness-completeness-and-compactness.md)). Euclid's first proposition builds an equilateral triangle by intersecting two circles, but nothing in his axioms makes them meet; Hilbert's axioms of 1899 supplied what the diagram had been supplying.

5. **Informal proofs can be wrong, and are now also checked by machine.** Kempe's 1879 proof of the four colour theorem was accepted until Heawood found a flaw in 1890. Appel and Haken proved the theorem in 1976 with a computer check of many configurations, and Gonthier completed a formal proof in the Coq proof assistant in 2005. Hales's 1998 proof of the Kepler conjecture on sphere packing was too large for referees to check fully; the Flyspeck project completed a formal verification in 2014 ([Computers and Proof](../../15-mathematics-in-context/computers-and-proof.md)).

6. **A good proof explains as well as verifies.** Euclid's proof that there are infinitely many primes shows that every finite list misses one, since the product of the list plus 1 has a prime factor outside it; Euler's proof that the sum of 1/p over primes diverges shows more, that primes are dense enough for their reciprocals to diverge. Lakatos (1976) showed how proofs and definitions are refined together as counterexamples appear, using Euler's formula V − E + F = 2 for polyhedra.

7. **Only a proof can establish impossibility.** No search shows that a 60° angle cannot be trisected with straightedge and compass, or that no algorithm decides whether every program halts; such results need an argument that some invariant rules out every attempt ([impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction)).

## Key concepts

| Term | Meaning |
|---|---|
| Proof | A finite argument from accepted premises in which every step can be checked |
| Theorem | A statement that has been proved |
| Conjecture | A statement believed true but not proved |
| Gap | A step whose justification is missing |
| Rigour | The standard that every step is justified from stated premises |
| Formalisation | Rewriting a proof as a derivation in a formal system |
| Proof assistant | Software that checks formal proofs, such as Coq, Isabelle or Lean |
| Counterexample | An instance satisfying the hypotheses but not the conclusion |

## How it fits

- **Below:** [Formal Proof Systems](../01-formal-logic/formal-proof-systems.md) gives the idealised derivation that a written proof abbreviates; [Predicate Logic and Quantifiers](../01-formal-logic/predicate-logic-and-quantifiers.md) gives the logical forms of tenet 3.
- **Above:** [Axioms, Definitions and Theorems](../03-the-axiomatic-method/axioms-definitions-and-theorems.md) fixes the starting points; [Mathematical Practice and Discovery](../../15-mathematics-in-context/mathematical-practice-and-discovery.md) and [Philosophy of Mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md) ask how proofs are found and what they establish; programs are proved correct the same way ([Correctness and Invariants](../../../cs-first-principles/05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md)).
- **Siblings:** [Direct Proof, Contraposition and Contradiction](direct-proof-contraposition-and-contradiction.md), [Cases, Constructions and Counterexamples](cases-constructions-and-counterexamples.md) and [Mathematical Induction](mathematical-induction.md) are the standard ways to fill in the skeleton.

## Common misconceptions

- **"A theorem is true absolutely"**: it is true in every model of its axioms; the angles of a triangle sum to 180° in Euclidean geometry and to less in hyperbolic geometry.
- **"A proof accepted by experts is correct"**: Kempe's proof stood for eleven years; acceptance is evidence, not a guarantee.
- **"A proof must be written formally"**: almost none is; what matters is that every step could be expanded into formal steps if challenged.

## Go deeper

- Daniel J. Velleman, *How to Prove It: A Structured Approach* (3rd edition, 2019): logical form as the guide to the structure of a proof.
- George Pólya, *How to Solve It* (1945): heuristics for finding proofs.
- Imre Lakatos, *Proofs and Refutations* (1976): how proofs, counterexamples and definitions evolve together.
- Martin Aigner and Günter M. Ziegler, *Proofs from THE BOOK* (first edition 1998): proofs chosen for elegance and insight.
