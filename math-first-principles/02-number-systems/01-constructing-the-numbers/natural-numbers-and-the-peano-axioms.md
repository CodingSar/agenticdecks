# Natural Numbers and the Peano Axioms

> **Layer:** [02 Number Systems](../README.md) › [Constructing the Numbers](README.md)
> **Builds on:** [Mathematical Induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md), [Axioms, Definitions and Theorems](../../00-logic-and-proof/03-the-axiomatic-method/axioms-definitions-and-theorems.md), [Functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md), [Zermelo–Fraenkel Set Theory](../../01-sets-and-foundations/03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md)
> **Enables:** [Integers and Rational Numbers](integers-and-rational-numbers.md), [Divisibility and the Euclidean Algorithm](../02-elementary-number-theory/divisibility-and-the-euclidean-algorithm.md), [Counting Principles and Binomial Coefficients](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md), [Gödel's Incompleteness Theorems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md), [Models and the Löwenheim–Skolem Theorems](../../13-structure-and-metamathematics/03-model-theory-and-independence/models-and-the-lowenheim-skolem-theorems.md)

## Essence

The natural numbers 0, 1, 2, … are what you reach from 0 by repeatedly taking "the next number", and nothing else. Dedekind (1888) and Peano (1889) turned that picture into axioms about 0 and a successor map S: S never takes a value twice, never returns to 0, and any property that holds at 0 and passes from n to S(n) holds for all n. The axioms determine ℕ up to unique isomorphism, and recursion defines addition, multiplication and every other arithmetic function. Set theory supplies a model, 0 = ∅ and S(n) = n ∪ {n}, from which every later number system is built.

## Core tenets

1. **ℕ is a set with an element 0 and a map S : ℕ → ℕ such that S is injective, 0 is not a successor, and every subset that contains 0 and is closed under S is all of ℕ.** The last is the axiom of induction, and each axiom excludes a wrong model. Without "0 is not a successor", the one-point loop with S(0) = 0 satisfies the rest; without injectivity, so does 0 → 1 → 2 → 2, where S(2) = 2; without induction, so does ℕ plus a disjoint copy of ℤ, unreachable from 0.

2. **Definition by recursion works: for any set A, element a ∈ A and map g : A → A there is exactly one f : ℕ → A with f(0) = a and f(S(n)) = g(f(n)).** Uniqueness is induction. For existence, intersect all relations R ⊆ ℕ × A that contain (0, a) and are closed under (n, x) ↦ (S(n), g(x)), and prove by induction that the result is a function; that step needs the other two axioms (on the loop model, f(S(n)) = f(n) + 1 would force f(0) = f(0) + 1). Recursion defines m + 0 = m, m + S(n) = S(m + n), m · 0 = 0 and m · S(n) = m · n + m, and induction proves the usual laws.

3. **Any two models of the axioms are isomorphic, by exactly one isomorphism (Dedekind's categoricity theorem).** Given models (N, 0, S) and (N′, 0′, S′), recursion gives f with f(0) = 0′ and f(S(n)) = S′(f(n)); its image contains 0′ and is closed under S′, so it is all of N′, and induction shows that f is injective. So "the natural numbers" is one structure up to relabelling. The proof uses induction on arbitrary subsets, which first-order arithmetic gives up (tenet 6).

4. **The order is a well-ordering, and well-ordering is equivalent to induction.** Define m ≤ n when n = m + k for some k. If a set A ⊆ ℕ had no least element, induction on n would show that no number ≤ n lies in A, so A would be empty. Conversely, the least failure of a property could be neither 0 nor the successor of a success. So "take a minimal counterexample" and Fermat's "infinite descent" are induction in disguise.

5. **Set theory builds a model: 0 = ∅ and S(n) = n ∪ {n} (von Neumann's construction).** Then 1 = {0}, 2 = {0, 1}, and each number is the set of those below it, so m < n means m ∈ n, and n has n elements. The axiom of infinity of Zermelo–Fraenkel set theory (ZF) provides a set that contains ∅ and is closed under S; the smallest such set, ω, is the intersection of all of them, so it satisfies induction. Zermelo's S(n) = {n} works equally well: the axioms describe a structure, not particular objects (Benacerraf, "What Numbers Could Not Be", 1965).

6. **First-order Peano arithmetic cannot pin ℕ down.** First-order quantifiers range over numbers, not sets of numbers, so induction becomes a schema, one axiom per formula. Peano arithmetic (PA), this schema plus the recursive equations for + and ×, has non-standard models: add a constant c and the axioms c ≠ 0, c ≠ 1, c ≠ 2, …; any finite set of these holds in ℕ for large c, so by compactness all hold in some model, where c exceeds every numeral. By Gödel's incompleteness theorem (1931), PA also leaves some truths about ℕ unprovable; Goodstein's theorem and the Paris–Harrington theorem (1977) are natural examples.

7. **ℕ can add and multiply, with cancellation, but cannot subtract or divide.** Induction proves that m + k = n + k implies m = n, and that m · k = n · k with k ≠ 0 implies m = n. But 3 + x = 2 and 2 · x = 3 have no solution in ℕ. The next constructions repair exactly these failures, and they work because cancellation holds.

## Key concepts

| Term | Meaning |
|---|---|
| Successor | S(n) = n + 1, the only primitive operation besides the constant 0 |
| Inductive set | A set that contains 0 and is closed under S |
| Recursion theorem | f(0) = a and f(S(n)) = g(f(n)) define exactly one f on ℕ |
| Categorical | Having exactly one model up to isomorphism |
| Well-ordering | An order in which every non-empty subset has a least element |
| von Neumann numeral | n as the set {0, 1, …, n − 1} |
| Peano arithmetic | First-order axioms for 0, S, + and ×, with induction as a schema |
| Non-standard model | A model of PA with an element above every numeral |

## How it fits

- **Below:** induction (00) becomes an axiom; the axiomatic method (00) says what a model is; functions and the axiom of infinity (01) build one inside sets.
- **Above:** ℤ and ℚ are built from pairs of naturals; counting (03) measures finite sets by them; logic (13) studies what first-order axioms for ℕ cannot do.
- **Siblings:** the first rung. [Integers and rational numbers](integers-and-rational-numbers.md) adjoin inverses by quotients, [the real numbers](the-real-numbers.md) fill holes by completion, and [the complex numbers](the-complex-numbers.md) adjoin a root.

## Common misconceptions

- **"Induction needs its own justification"**: it is the axiom saying that ℕ contains nothing beyond 0, 1, 2, …; in set theory it holds because ω is the smallest inductive set.
- **"The Peano axioms settle every question about ℕ"**: the second-order axioms fix the structure, but no consistent axiom system that a computer can list proves every arithmetical truth.
- **"Starting ℕ at 0 or at 1 matters"**: it is a convention; Dedekind and Peano began at 1, while set theory and computer science begin at 0, so that the numeral n has n elements.

## Go deeper

- Richard Dedekind, *Was sind und was sollen die Zahlen?* (1888): the original, with the recursion and categoricity theorems.
- Edmund Landau, *Foundations of Analysis* (German original 1930): from the Peano axioms to ℂ, every step proved.
- Herbert Enderton, *Elements of Set Theory* (1977): the von Neumann model and the recursion theorem, inside ZF.
