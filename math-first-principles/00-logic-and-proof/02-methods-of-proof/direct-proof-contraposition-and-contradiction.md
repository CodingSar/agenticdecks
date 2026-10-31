# Direct Proof, Contraposition and Contradiction

> **Layer:** [00 Logic and Proof](../README.md) › [Methods of Proof](README.md)
> **Builds on:** [What a Proof Is](what-a-proof-is.md), [Propositional Logic](../01-formal-logic/propositional-logic.md), [Predicate Logic and Quantifiers](../01-formal-logic/predicate-logic-and-quantifiers.md)
> **Enables:** [Cases, Constructions and Counterexamples](cases-constructions-and-counterexamples.md), [Constructive and Intuitionistic Logic](../03-the-axiomatic-method/constructive-and-intuitionistic-logic.md), [Primes and Unique Factorisation](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md), [Cantor's Diagonal Argument](../../01-sets-and-foundations/02-infinity-and-cardinality/cantors-diagonal-argument.md), [Undecidable Problems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/undecidable-problems.md)

## Essence

Most proofs of a statement P ⇒ Q take one of three shapes. A direct proof assumes P and reasons forward to Q. A proof by contraposition proves the equivalent statement ¬Q ⇒ ¬P. A proof by contradiction assumes the negation of what is to be proved and derives a contradiction. Each is justified by a propositional tautology, and choosing among them is mostly a matter of which assumption gives the most to work with.

## Core tenets

1. **A direct proof unfolds definitions and reasons forward.** To prove that the sum of two odd integers is even, write them as 2a + 1 and 2b + 1; their sum is 2a + 2b + 2 = 2(a + b + 1), even by definition. Assume the hypothesis, rewrite it through definitions, manipulate, then recognise the definition of the conclusion: this pattern covers most routine proofs, and the deduction theorem of [Formal Proof Systems](../01-formal-logic/formal-proof-systems.md) is what licenses "assume P".

2. **The contrapositive is equivalent; the converse is not.** P ⇒ Q, ¬Q ⇒ ¬P, ¬P ∨ Q and ¬(P ∧ ¬Q) have the same truth table, but the converse Q ⇒ P is a different statement. To show "if n² is even then n is even", the hypothesis gives little to grip, while the contrapositive is easy: if n = 2k + 1 then n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1 is odd. Contraposition helps whenever the negated conclusion is more concrete than the hypothesis.

3. **Proof by contradiction assumes the negation and derives an absurdity.** Write ⊥ for a contradiction, a statement of the form R ∧ ¬R. If ¬S leads to ⊥, then S holds, because ¬S ⇒ ⊥ is equivalent to S. The classic case: if √2 = a/b in lowest terms, then a² = 2b², so a is even, a = 2c, so b² = 2c² and b is even too, contradicting lowest terms.

4. **Proving a negation is not the same as proof by contradiction.** To prove ¬S, assume S and derive ⊥: that is what ¬S means, and it is valid even in constructive logic. Deriving ⊥ from ¬S to conclude a positive S uses the classical step from ¬¬S to S. The irrationality of √2 is a negation ("√2 is not a ratio of integers") and so is constructively valid; the classical step is needed when "some x has property P" is proved by refuting "no x has P" ([Constructive and Intuitionistic Logic](../03-the-axiomatic-method/constructive-and-intuitionistic-logic.md)).

5. **Many proofs told "by contradiction" are direct.** Euclid's proof that there are infinitely many primes is often told as a contradiction, but its core is direct: for any finite list of primes p₁, …, pₖ, the number N = p₁p₂…pₖ + 1 leaves remainder 1 on division by each pᵢ, so every prime factor of N is missing from the list. N need not be prime: 2 · 3 · 5 · 7 · 11 · 13 + 1 = 30031 = 59 × 509. Recasting a contradiction as a direct argument often shows what the proof really constructs.

6. **From a contradiction anything follows.** Since ⊥ ⇒ S is a tautology for every S (ex falso quodlibet), inconsistent assumptions prove everything. Hence the danger in proof by contradiction: a slip anywhere also produces a contradiction, and the method cannot tell the two apart, whereas the intermediate claims of a direct proof can each be checked for plausibility. It is also why the consistency of an axiom system matters ([Consistency and Independence](../03-the-axiomatic-method/consistency-and-independence.md)).

7. **"If and only if" needs two proofs.** P ⇔ Q is (P ⇒ Q) ∧ (Q ⇒ P), so each direction needs its own argument, often by different methods. A list of equivalent conditions P₁, …, Pₙ is proved most economically by a cycle P₁ ⇒ P₂ ⇒ … ⇒ Pₙ ⇒ P₁, as for the many conditions for a square matrix to be invertible.

8. **Three fallacies imitate these methods.** Affirming the consequent infers P from P ⇒ Q and Q; denying the antecedent infers ¬Q from P ⇒ Q and ¬P; both confuse the converse with the contrapositive. Circular reasoning uses the conclusion, often disguised, as a step.

## Key concepts

| Term | Meaning |
|---|---|
| Direct proof | Assume P and deduce Q |
| Contrapositive | ¬Q ⇒ ¬P, equivalent to P ⇒ Q |
| Converse | Q ⇒ P, not equivalent to P ⇒ Q |
| Proof by contradiction | Assume the negation of the goal and derive ⊥ |
| ⊥ | A contradiction, a statement of the form R ∧ ¬R |
| Ex falso quodlibet | From ⊥ any statement follows |
| Biconditional | P ⇔ Q, proved as two implications |
| Fallacy | An invalid inference form, such as affirming the consequent |

## How it fits

- **Below:** [What a Proof Is](what-a-proof-is.md) gives the skeleton; [Propositional Logic](../01-formal-logic/propositional-logic.md) proves the tautologies behind each method; [Predicate Logic and Quantifiers](../01-formal-logic/predicate-logic-and-quantifiers.md) shows how to negate quantified statements.
- **Above:** contradiction drives [Cantor's Diagonal Argument](../../01-sets-and-foundations/02-infinity-and-cardinality/cantors-diagonal-argument.md) and, through it, [Undecidable Problems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/undecidable-problems.md); Euclid's argument opens [Primes and Unique Factorisation](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md); [Constructive and Intuitionistic Logic](../03-the-axiomatic-method/constructive-and-intuitionistic-logic.md) separates the constructive uses from the classical one.
- **Siblings:** [Cases, Constructions and Counterexamples](cases-constructions-and-counterexamples.md) handles disjunctions and existence; [Mathematical Induction](mathematical-induction.md) handles statements about every natural number.

## Common misconceptions

- **"Proof by contradiction is less rigorous"**: in classical logic it is exactly as valid as a direct proof; its costs are that it may construct nothing and that errors are harder to spot.
- **"Euclid's N = p₁…pₖ + 1 is prime"**: it has a prime factor outside the list, which need not be N itself, as 30031 = 59 × 509 shows.
- **"If P ⇒ Q is proved, so is Q ⇒ P"**: every multiple of 4 is even, but 6 is even and not a multiple of 4.

## Go deeper

- Daniel J. Velleman, *How to Prove It: A Structured Approach* (3rd edition, 2019), chapter 3: proof strategies for each connective and quantifier.
- Richard Hammack, *Book of Proof* (3rd edition, 2018): direct proof, contraposition and contradiction, with many exercises.
- G. H. Hardy, *A Mathematician's Apology* (1940): Euclid's and Pythagoras's proofs as models of mathematical beauty.
