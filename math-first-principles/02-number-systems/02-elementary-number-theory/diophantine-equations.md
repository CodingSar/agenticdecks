# Diophantine Equations

> **Layer:** [02 Number Systems](../README.md) › [Elementary Number Theory](README.md)
> **Builds on:** [Divisibility and the Euclidean Algorithm](divisibility-and-the-euclidean-algorithm.md), [Primes and Unique Factorisation](primes-and-unique-factorisation.md), [Modular Arithmetic](modular-arithmetic.md), [Quadratic Reciprocity](quadratic-reciprocity.md)
> **Enables:** [Fermat's Last Theorem](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/fermats-last-theorem.md), [Elliptic Curves](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/elliptic-curves.md), [p-adic Numbers and Local Fields](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/p-adic-numbers-and-local-fields.md), [Ideals and the Class Group](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/ideals-and-the-class-group.md), [Undecidable Problems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/undecidable-problems.md)

## Essence

A Diophantine equation is a polynomial equation whose solutions are sought in integers or rationals, named after Diophantus of Alexandria. Linear equations are completely solved by Bézout; quadratic ones in two variables by geometry, unique factorisation and continued fractions; beyond that, every degree brings new difficulty, and Fermat's Last Theorem took over three hundred years. The tools of this area each catch part of the truth: congruences prove impossibility, factorisation and descent prove finiteness, geometry finds infinite families. Hilbert's tenth problem asked for one general method, and in 1970 the answer was that none can exist.

## Core tenets

1. **Linear equations are solved completely.** ax + by = c has integer solutions if and only if gcd(a, b) ∣ c, where gcd is the greatest common divisor, and all of them form one line of solutions found by the extended Euclidean algorithm. So 6x + 10y = 7 has none, since 2 ∤ 7.

2. **Pythagorean triples come from rational points on a circle.** Solutions of x² + y² = z² correspond to rational points on the unit circle. A line through (−1, 0) with rational slope t meets the circle again at ((1 − t²)/(1 + t²), 2t/(1 + t²)), and every rational point arises this way. Clearing denominators with t = n/m gives every primitive triple as (m² − n², 2mn, m² + n²) with m > n > 0 coprime and of opposite parity, up to swapping x and y; m = 2, n = 1 gives (3, 4, 5).

3. **A positive integer is a sum of two squares if and only if every prime ≡ 3 (mod 4) divides it to an even power.** Modulo 4 rules out primes ≡ 3. For p ≡ 1 (mod 4), −1 ≡ a² for some a; by the pigeonhole principle (Thue's lemma) there are x, y with 0 < |x|, |y| < √p and x ≡ ay (mod p), so p ∣ x² + y² < 2p, which forces x² + y² = p. The identity (a² + b²)(c² + d²) = (ac − bd)² + (ad + bc)², multiplication of norms in ℂ, does the rest. Fermat stated the theorem and Euler proved it; Lagrange proved in 1770 that every positive integer is a sum of four squares.

4. **Pell's equation x² − dy² = 1 has infinitely many solutions for every non-square d > 0.** The continued fraction of √d produces the smallest solution, and powers of x + y√d give the rest. The smallest solution can be huge: for d = 61 it is x = 1766319049, y = 226153980. Brahmagupta (seventh century) composed solutions, Bhāskara II (twelfth century) gave the cyclic method, and Lagrange proved existence in general; the name comes from Euler's misattribution to John Pell.

5. **Descent and factorisation prove that solutions do not exist.** Fermat showed that x⁴ + y⁴ = z² has no solutions in positive integers: from one, the Pythagorean parametrisation builds a smaller one, and an infinite descending chain of positive integers is impossible. This settles Fermat's Last Theorem, xⁿ + yⁿ = zⁿ with n ≥ 3, for n = 4. The general case resisted until Wiles, with Taylor, proved it in 1994 (published 1995) through elliptic curves and modular forms, the subject of layer 12.

6. **Local solutions are necessary but not always sufficient.** An equation with no real solution, or no solution modulo some prime power, has no rational solution. The Hasse–Minkowski theorem says that for quadratic forms the converse holds: a solution over ℝ and over every p-adic field ℚₚ implies a rational one. For cubics it fails: Selmer (1951) showed that 3x³ + 4y³ + 5z³ = 0 has non-zero solutions over ℝ and every ℚₚ, but none in integers other than zero.

7. **No algorithm decides all Diophantine equations.** Hilbert's tenth problem (1900) asked for a procedure to decide whether any polynomial equation with integer coefficients has an integer solution. Davis, Putnam and Robinson (1961) reduced it to a single exponential relation, and Matiyasevich (1970) completed the proof that every computably enumerable set is the set of values of a parameter for which a polynomial equation is solvable: the Matiyasevich–Robinson–Davis–Putnam (MRDP) theorem. So the [halting problem](../../../cs-first-principles/02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) reduces to Diophantine solvability, which is therefore undecidable; as a by-product, Jones, Sato, Wada and Wiens (1976) wrote down a polynomial whose positive values are exactly the primes. The analogous question for rational solutions is open as of 2026.

## Key concepts

| Term | Meaning |
|---|---|
| Diophantine equation | A polynomial equation to be solved in integers or rationals |
| Primitive Pythagorean triple | Coprime x, y, z with x² + y² = z² |
| Pell's equation | x² − dy² = 1 for a non-square d > 0 |
| Infinite descent | Deriving a smaller solution from any solution, so none exist |
| Local solvability | Solvability over ℝ and over every ℚₚ, or modulo every prime power |
| Hasse principle | Local solvability implies rational solvability; true for quadratic forms |
| MRDP theorem | Diophantine sets are exactly the computably enumerable sets |

## How it fits

- **Below:** [divisibility](divisibility-and-the-euclidean-algorithm.md) solves the linear case and gives continued fractions; [primes](primes-and-unique-factorisation.md), [modular arithmetic](modular-arithmetic.md) and [quadratic reciprocity](quadratic-reciprocity.md) supply factorisation, obstructions and the sum-of-squares criteria.
- **Above:** elliptic curves and Fermat's Last Theorem (12) treat cubics and beyond; p-adic numbers (12) make local solvability precise; ideals and the class group (12) repair factorisation in rings such as ℤ[√−d]; undecidable problems (13) place tenet 7 in computability theory.
- **Siblings:** this leaf collects the tools of the area; each earlier leaf solves one family of equations.

## Common misconceptions

- **"Fermat proved his Last Theorem"**: his marginal note (around 1637) gave no proof, and the only case he is known to have proved is n = 4.
- **"Undecidable means some equation has unknowable solutions"**: each equation is either solvable or not; what does not exist is one algorithm that decides every case.
- **"If there is no obstruction modulo any n, there is a solution"**: Selmer's cubic has no local obstruction and no solution.

## Go deeper

- G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers* (1938; 6th edition 2008): sums of squares, Pell's equation and the n = 4 case.
- Martin Davis, "Hilbert's Tenth Problem is Unsolvable", American Mathematical Monthly (1973): a self-contained account of the proof.
- Yuri Matiyasevich, *Hilbert's Tenth Problem* (1993): the full story, by the person who finished it.
- Simon Singh, *Fermat's Last Theorem* (1997): a popular history from Pythagoras to Wiles.
