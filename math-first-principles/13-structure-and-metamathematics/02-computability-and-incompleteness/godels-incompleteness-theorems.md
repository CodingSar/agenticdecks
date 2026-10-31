# Gödel's Incompleteness Theorems

> **Layer:** [13 Structure and Metamathematics](../README.md) › [Computability and incompleteness](README.md)
> **Builds on:** [Soundness, completeness and compactness](../../00-logic-and-proof/01-formal-logic/soundness-completeness-and-compactness.md), [Consistency and independence](../../00-logic-and-proof/03-the-axiomatic-method/consistency-and-independence.md), [Natural numbers and the Peano axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md), [Computable functions and the Church–Turing thesis](computable-functions-and-the-church-turing-thesis.md), [Undecidable problems](undecidable-problems.md)
> **Enables:** [Proof theory and reverse mathematics](proof-theory-and-reverse-mathematics.md), [Forcing and independence](../03-model-theory-and-independence/forcing-and-independence.md), [Large cardinals](../03-model-theory-and-independence/large-cardinals.md), [Philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md), [Computers and proof](../../15-mathematics-in-context/computers-and-proof.md)

## Essence

In 1931 Kurt Gödel proved that no consistent, effectively axiomatised theory that contains a modest amount of arithmetic can decide every arithmetical sentence, and that such a theory cannot prove its own consistency. The method is to code formulas and proofs as numbers, so that arithmetic can talk about provability in arithmetic, and then to build a sentence that says of itself that it is not provable. The theorems ended the hope of a single complete and self-certifying formal system for mathematics. They are also among the most misquoted results in mathematics, so the exact hypotheses matter as much as the conclusion.

## Core tenets

1. **The first theorem has three hypotheses, and each is needed.** Let T be a first-order theory that is consistent, effectively axiomatised (its axioms form a decidable set) and contains Robinson arithmetic Q, a weak finite fragment of Peano arithmetic (PA). Then some sentence in the language of arithmetic is neither provable nor refutable in T. An inconsistent theory proves everything. True arithmetic, the set of all sentences true in ℕ, is consistent and complete, but not effectively axiomatisable. Presburger arithmetic, without multiplication, and the theory of real closed fields are consistent, effective and complete, because they cannot express enough arithmetic.

2. **Arithmetisation lets arithmetic talk about proofs.** Assign each symbol, formula and finite sequence of formulas a natural number. For an effectively axiomatised T, the relation "p codes a proof in T of the formula with code x" is decidable, and every decidable relation is representable in Q: Q proves each true instance and refutes each false one. So Prov_T(x) = ∃p Prf_T(p, x) is a Σ₁ formula expressing provability in T.

3. **The diagonal lemma builds a sentence that denies its own provability.** For every formula ψ(x) there is a sentence σ with Q ⊢ σ ↔ ψ(⌜σ⌝), where ⌜σ⌝ is the numeral for the code of σ. Applied to ¬Prov_T it gives a sentence G, and Gödel's argument runs as follows. A proof of G would be a number that Q verifies as one, giving T ⊢ Prov_T(⌜G⌝) and contradicting consistency; a refutation of G is excluded by ω-consistency, the requirement that T not prove ∃x φ(x) while refuting each φ(n).

   ```
   T ⊢ G ↔ ¬Prov_T(⌜G⌝)
   consistent T      ⇒  T ⊬ G
   ω-consistent T    ⇒  T ⊬ ¬G
   ```

4. **Rosser removed the extra hypothesis.** J. Barkley Rosser (1936) used the sentence "for every proof of me there is a shorter refutation of me", which is undecided in T assuming only consistency. A second route goes through computability: if T were complete, its theorems would be decidable by listing proofs until φ or ¬φ appears, and then, since Q proves every true instance of halting, a sound T would decide the halting problem. Alfred Tarski's theorem is the semantic version: truth in ℕ is not definable by any arithmetical formula.

5. **The Gödel sentence is a simple, true statement about numbers.** G is equivalent to a Π₁ sentence, one of the form ∀n R(n) with R decidable, much like "this equation has no integer solution". If T is consistent, G is unprovable, which is what G says, so G is true in ℕ. By the completeness theorem T + ¬G also has a model, necessarily a non-standard one in which some non-standard number codes a "proof" of G.

6. **The second theorem: T cannot prove its own consistency.** Let Con(T) be ¬Prov_T(⌜0 = 1⌝). If T contains PA, or meets the Hilbert–Bernays–Löb derivability conditions, then T can formalise the argument for the first theorem and prove Con(T) → G. So if T is consistent, T ⊬ Con(T). The way Con(T) is written matters: Solomon Feferman (1960) gave unnatural consistency formulas that T does prove. This defeated Hilbert's programme of proving the consistency of mathematics by finitary means formalisable inside it.

7. **Incompleteness cannot be repaired by adding axioms.** If T is sound, T + Con(T) is again consistent and effective, so it has its own undecided sentence, and the process never ends. Every effectively axiomatised consistent extension of Q is incomplete, including ZFC, Zermelo–Fraenkel set theory with choice, which is why set theory has independent statements.

## Key concepts

| Term | Meaning |
|---|---|
| Effectively axiomatised | The set of axioms is decidable, so the theorems are c.e. (computably enumerable) |
| Robinson arithmetic Q | Seven axioms for successor, addition and multiplication, without induction |
| Gödel numbering | A coding of formulas and proofs by natural numbers |
| Prov_T(x) | The Σ₁ formula "x is the code of a theorem of T" |
| Diagonal lemma | Every property ψ has a sentence σ with σ ↔ ψ(⌜σ⌝) provable |
| ω-consistency | T never proves ∃x φ(x) while refuting every φ(n) |
| Con(T) | The arithmetical sentence expressing that T is consistent |

## How it fits

- **Below:** It uses the [completeness theorem](../../00-logic-and-proof/01-formal-logic/soundness-completeness-and-compactness.md) to turn unprovability into [independence](../../00-logic-and-proof/03-the-axiomatic-method/consistency-and-independence.md), and [computability](computable-functions-and-the-church-turing-thesis.md) to make "effective" precise for theories of the [natural numbers](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md).
- **Above:** The [philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md) weighs its meaning for formalism, and [computer-checked proof](../../15-mathematics-in-context/computers-and-proof.md) inherits its limits.
- **Siblings:** [Proof theory](proof-theory-and-reverse-mathematics.md) measures how much stronger a theory must be to prove Con(PA), while [forcing](../03-model-theory-and-independence/forcing-and-independence.md) and [large cardinals](../03-model-theory-and-independence/large-cardinals.md) supply the independent statements of set theory.

## Common misconceptions

- **"Some true statements can never be proved."**: Unprovability is always relative to a theory: G is provable in T + Con(T); no sentence is unprovable in every consistent effective theory.
- **"Gödel showed mathematics is uncertain or inconsistent."**: The theorems assume consistency and say nothing against it; Gentzen proved Con(PA) in a different, stronger system.
- **"Completeness and incompleteness contradict each other."**: Gödel's completeness theorem (1929) says every sentence true in all models of T is provable; incompleteness says some sentence is true in some models of T and false in others.

## Go deeper

- Kurt Gödel, "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I" (1931): the original paper.
- Peter Smith, *An Introduction to Gödel's Theorems* (2nd edition, 2013): a careful textbook covering every hypothesis.
- Torkel Franzén, *Gödel's Theorem: An Incomplete Guide to Its Use and Abuse* (2005): what the theorems do not say.
