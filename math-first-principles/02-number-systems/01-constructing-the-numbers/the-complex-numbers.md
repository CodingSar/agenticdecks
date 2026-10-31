# The Complex Numbers

> **Layer:** [02 Number Systems](../README.md) › [Constructing the Numbers](README.md)
> **Builds on:** [The Real Numbers](the-real-numbers.md), [Equivalence Relations and Quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md)
> **Enables:** [Holomorphic Functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md), [Cauchy's Theorem and Its Consequences](../../09-advanced-analysis/02-complex-analysis/cauchys-theorem-and-its-consequences.md), [Homotopy and the Fundamental Group](../../07-topology/02-algebraic-topology/homotopy-and-the-fundamental-group.md), [Polynomial Rings](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md), [Eigenvalues and Diagonalisation](../../04-linear-algebra/02-determinants-and-eigenvalues/eigenvalues-and-diagonalisation.md)

## Essence

ℝ has no square root of −1, so x² + 1 = 0 has no real solution. The complex numbers are pairs of reals, ℂ = ℝ², with (a, b) + (c, d) = (a + c, b + d) and (a, b)(c, d) = (ac − bd, ad + bc); writing i = (0, 1), every complex number is a + bi and i² = −1. Nothing mysterious is added: once i² = −1, distributivity leaves no other rule, and the rule makes ℂ a field. The payoff is out of all proportion to the cost. By the fundamental theorem of algebra, adjoining this one root makes every non-constant polynomial split into linear factors, so no further rung is needed to solve polynomial equations.

## Core tenets

1. **ℂ is a field, with three equivalent descriptions.** Associativity and distributivity are routine checks. The inverse of z = a + bi ≠ 0 is z̄/|z|², where z̄ = a − bi is the conjugate and |z|² = z · z̄ = a² + b², which is positive; that positivity is where the order of ℝ is used. Equivalently, ℂ is the quotient ring ℝ[x]/(x² + 1), polynomials modulo x² + 1, and it is the set of real matrices [[a, −b], [b, a]], each of which rotates and scales the plane.

2. **The multiplication rule is forced, and real problems forced it on mathematicians.** In any field that contains ℝ and an element i with i² = −1, distributivity gives (a + bi)(c + di) = (ac − bd) + (ad + bc)i, so there is no other choice. Cubic equations demanded the rule before anyone wanted it: Cardano's formula for x³ = 15x + 4 gives x = ∛(2 + 11i) + ∛(2 − 11i), and Bombelli (1572) saw that (2 ± i)³ = 2 ± 11i, so x = (2 + i) + (2 − i) = 4, a real root reached only through complex numbers.

3. **ℂ cannot be ordered.** In an ordered field every non-zero square is positive, so 1 = 1² > 0 and −1 = i² > 0, and adding gives 0 > 0. What ℂ loses is the order. What it keeps is the modulus, with |zw| = |z| · |w|, which is all that limits need, and ℂ is complete for it because ℝ is.

4. **Multiplication is rotation plus scaling, so the roots of unity form a regular polygon.** Write z = r(cos θ + i sin θ) with r = |z|. The angle-addition formulas say that a product multiplies the moduli and adds the angles, which is de Moivre's formula (cos θ + i sin θ)ⁿ = cos nθ + i sin nθ. So the solutions of zⁿ = 1 are cos(2πk/n) + i sin(2πk/n) for k = 0, …, n − 1, the vertices of a regular n-gon. Real analysis (06) defines e^(iθ) = cos θ + i sin θ, and |zw|² = |z|²|w|² is the two-square identity (a² + b²)(c² + d²) = (ac − bd)² + (ad + bc)².

5. **Conjugation is the only automorphism of ℂ, besides the identity, that fixes every real number.** Such an automorphism must send i to a square root of −1, so to i or −i, and then a + bi goes to a + bi or to a − bi. So the symmetry group of ℂ over ℝ has two elements, the smallest non-trivial Galois group (05). Automorphisms that do not fix ℝ also exist, uncountably many, but their existence needs the axiom of choice and all of them are discontinuous.

6. **The fundamental theorem of algebra: every non-constant polynomial with complex coefficients has a complex root.** By induction on the degree, every polynomial of degree n then factors as c(z − z₁)⋯(z − zₙ). The proof that stays closest to ℂ: |p(z)| tends to ∞ with |z|, so by compactness |p| attains a minimum at some z₀. If p(z₀) ≠ 0, write p(z₀ + h) = p(z₀) + c·hᵏ + (higher powers of h) with c ≠ 0; choosing h small along a k-th root of −p(z₀)/c makes |p| smaller, a contradiction. Other proofs use the winding number (07), Liouville's theorem (09) and Galois theory (05). Gauss gave four proofs, the first in his doctoral thesis of 1799.

7. **Some analysis is unavoidable.** Every proof uses completeness somewhere, at least through the fact that a real polynomial of odd degree has a real root, which is the intermediate value theorem. Galois theory reduces the theorem to exactly that fact plus the existence of square roots in ℂ. Without completeness the statement fails: over ℚ(i), the rationals with i adjoined, x² − 2 has no root.

## Key concepts

| Term | Meaning |
|---|---|
| Imaginary unit | i = (0, 1), with i² = −1 |
| Conjugate | z̄ = a − bi for z = a + bi; z · z̄ = \|z\|² |
| Modulus | \|z\| = √(a² + b²), the distance from 0 |
| Argument | The angle θ in z = r(cos θ + i sin θ) |
| Root of unity | A solution of zⁿ = 1 for some n ≥ 1 |
| Algebraically closed | Every non-constant polynomial over the field has a root in it |
| Fundamental theorem of algebra | ℂ is algebraically closed |

## How it fits

- **Below:** built on [the real numbers](the-real-numbers.md), whose completeness the fundamental theorem needs; the description ℝ[x]/(x² + 1) is a quotient in the sense of 01.
- **Above:** complex analysis (09) studies differentiable functions of z and proves the fundamental theorem by Liouville's theorem; topology (07) proves it by winding numbers; linear algebra (04) uses it to guarantee eigenvalues; polynomial rings and Galois theory (05) study the roots, as in [the Galois correspondence](../../05-abstract-algebra/03-galois-theory/the-galois-correspondence.md).
- **Siblings:** [algebraic and transcendental numbers](algebraic-and-transcendental-numbers.md) sorts complex numbers by the polynomials they satisfy; [extending number systems](extending-number-systems.md) doubles ℂ again, to the quaternions, and loses commutativity.

## Common misconceptions

- **"√(ab) = √a · √b for all complex numbers"**: no choice of square root on ℂ is consistent with products; with the usual one, √((−1)(−1)) = 1 but √(−1) · √(−1) = −1.
- **"Imaginary numbers are less real than real numbers"**: both are built from ℕ; ℂ is ℝ² with a multiplication, as concrete as ℝ, and quantum mechanics is written in it.
- **"The fundamental theorem of algebra is pure algebra"**: every proof needs some analysis or topology of ℝ; algebra alone cannot give x² − 2 a root.

## Go deeper

- Tristan Needham, *Visual Complex Analysis* (1997): multiplication as rotation, and the geometry behind every formula.
- Benjamin Fine and Gerhard Rosenberger, *The Fundamental Theorem of Algebra* (1997): the analytic, topological and algebraic proofs side by side.
- Heinz-Dieter Ebbinghaus and others, *Numbers* (Graduate Texts in Mathematics 123): the construction of ℂ, its history and the fundamental theorem.
