# Undecidable Problems

> **Layer:** [13 Structure and Metamathematics](../README.md) › [Computability and incompleteness](README.md)
> **Builds on:** [Computable functions and the Church–Turing thesis](computable-functions-and-the-church-turing-thesis.md), [Cantor's diagonal argument](../../01-sets-and-foundations/02-infinity-and-cardinality/cantors-diagonal-argument.md), [Predicate logic and quantifiers](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md), [Diophantine equations](../../02-number-systems/02-elementary-number-theory/diophantine-equations.md), [Free groups and presentations](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md)
> **Enables:** [Gödel's incompleteness theorems](godels-incompleteness-theorems.md), [Quantifier elimination and decidable theories](../03-model-theory-and-independence/quantifier-elimination-and-decidable-theories.md), [Halting problem and undecidability (CS)](../../../cs-first-principles/02-theory-of-computation/03-computability/halting-problem-and-undecidability.md), [Computers and proof](../../15-mathematics-in-context/computers-and-proof.md)

## Essence

A problem is a family of yes-or-no questions, and it is decidable if one program answers all of them correctly. With computability defined, some families can be proved to have no such program. The first, the halting problem, falls to Cantor's diagonal argument; others are reduced to it by coding computations into them. The striking cases come from outside logic: whether a polynomial equation has integer solutions, whether two words in a finitely presented group are equal. Undecidability is a statement about a family; each single instance has an answer, though a given theory may be unable to prove it.

## Core tenets

1. **The halting problem is undecidable, by diagonalisation.** Let K = {e : program e halts on input e}. If a program h decided K, the program "on input e, run h(e); if it says halt, loop forever, otherwise stop" would have some number d, and on input d it halts if and only if it does not. K is computably enumerable (c.e.), since one can run program e and wait, so its complement is not. F. William Lawvere (1969) showed that this argument and Cantor's are one fixed-point theorem about cartesian closed categories.

2. **Reductions spread undecidability, and Rice's theorem makes it the rule.** If a computable f has x ∈ A if and only if f(x) ∈ B, a decider for B gives one for A. Henry Rice (1953) proved that every non-trivial property of the function a program computes is undecidable: whether it is total, constant or equal to a given function. Problems also have degrees of difficulty: halting is Σ₁-complete, while totality is Π₂-complete, so it stays undecidable even with a halting oracle.

3. **Validity in first-order logic is undecidable.** David Hilbert and Wilhelm Ackermann posed the Entscheidungsproblem in 1928: decide whether a first-order sentence is valid. Church and Turing answered it in 1936, coding a machine's run as a sentence that is valid if and only if the machine halts. By the completeness theorem validity is c.e., since one can list proofs, so it is undecidable yet semi-decidable. Restricted fragments can be decidable: logic with only one-place predicates is, as Leopold Löwenheim showed in 1915.

4. **Hilbert's tenth problem has a negative answer.** Hilbert asked in 1900 for a procedure deciding whether a polynomial equation with integer coefficients has an integer solution. The Matiyasevich–Robinson–Davis–Putnam (MRDP) theorem says every c.e. set is Diophantine: of the form {a : ∃x₁ … xₙ P(a, x₁, …, xₙ) = 0}. Martin Davis, Hilary Putnam and Julia Robinson reduced this in 1961 to showing that exponentiation is Diophantine, and Yuri Matiyasevich proved that in 1970. So no algorithm exists, and there is a polynomial whose positive values, as its variables range over the natural numbers, are exactly the primes (Jones, Sato, Wada and Wiens, 1976).

5. **Unprovability follows for single equations.** Since "ZFC proves a contradiction" is a halting statement, there is a polynomial with no integer root if and only if Zermelo–Fraenkel set theory with choice (ZFC) is consistent; if ZFC is consistent it cannot prove that this equation has no solution. Equations of degree 4 already give an undecidable family, degree 2 is decidable (Carl Ludwig Siegel, 1972), and degree 3 is open as of 2026, as is the analogue over the rational numbers.

6. **The word problem for groups is undecidable.** Max Dehn asked in 1911 for an algorithm deciding whether a word in the generators of a finitely presented group equals the identity. Pyotr Novikov (1955) and, independently, William Boone constructed presentations for which none exists, by encoding machine computations as relations. Consequences reach topology: by the Adian–Rabin theorem almost every property of presentations is undecidable, and Andrei Markov (1958) deduced that homeomorphism of 4-manifolds is undecidable. Restricted classes behave better; Wilhelm Magnus (1932) solved it for groups with one relator.

7. **Undecidability concerns families, not instances.** Each program either halts or not; what fails is uniformity. The busy beaver function, the most steps a halting n-state machine can take, is uncomputable, yet BB(5) = 47,176,870 was established in 2024 by a collaborative, computer-checked proof. Adam Yedidia and Scott Aaronson (2016) built a 7,918-state machine whose halting ZFC cannot settle if consistent; later work reduced the count below 800.

## Key concepts

| Term | Meaning |
|---|---|
| Decidable | Some program answers every instance correctly |
| Halting set K | {e : program e halts on input e} |
| Many-one reduction | A computable f with x ∈ A if and only if f(x) ∈ B |
| Rice's theorem | Every non-trivial property of computed functions is undecidable |
| Diophantine set | The parameters for which a polynomial equation has integer solutions |
| Matiyasevich–Robinson–Davis–Putnam (MRDP) theorem | Diophantine sets are exactly the c.e. sets |
| Word problem | Decide whether a word represents the identity of a presented group |

## How it fits

- **Below:** It applies [Cantor's diagonal argument](../../01-sets-and-foundations/02-infinity-and-cardinality/cantors-diagonal-argument.md) to [computable functions](computable-functions-and-the-church-turing-thesis.md), and its targets are [first-order validity](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md), [Diophantine equations](../../02-number-systems/02-elementary-number-theory/diophantine-equations.md) and [group presentations](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md).
- **Above:** The [computer science treatment](../../../cs-first-principles/02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) draws consequences for program analysis, and the limits of [computer-assisted proof](../../15-mathematics-in-context/computers-and-proof.md) start here.
- **Siblings:** [Gödel's theorems](godels-incompleteness-theorems.md) are the proof-theoretic shadow of these results, and [decidable theories](../03-model-theory-and-independence/quantifier-elimination-and-decidable-theories.md) mark where decision procedures do exist.

## Common misconceptions

- **"Undecidable means no one can ever know the answer."**: Each instance has an answer and many are settled; only a uniform method is ruled out.
- **"Undecidability is about infinite objects."**: Every instance is finite: a polynomial, a finite presentation, a program.

## Go deeper

- Yuri Matiyasevich, *Hilbert's Tenth Problem* (1993): the full proof by its author.
- Martin Davis, "Hilbert's Tenth Problem Is Unsolvable", *American Mathematical Monthly* (1973): a celebrated self-contained exposition.
- Bjorn Poonen, "Undecidability in Number Theory", *Notices of the American Mathematical Society* (2008): a survey of what is known and open.
