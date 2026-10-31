# Algebraic Curves and Riemann–Roch

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › [Algebraic Geometry](README.md)
> **Builds on:** [Projective Varieties and Bézout's Theorem](projective-varieties-and-bezouts-theorem.md), [Ideals and the Class Group](../01-algebraic-number-theory/ideals-and-the-class-group.md), [Analytic Continuation and Riemann Surfaces](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md), [Classification of Surfaces](../../07-topology/03-manifolds/classification-of-surfaces.md)
> **Enables:** [Schemes](schemes.md), [Elliptic Curves](../04-elliptic-curves-and-modular-forms/elliptic-curves.md), [Modular Forms](../04-elliptic-curves-and-modular-forms/modular-forms.md), [Error-Correcting Codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md)

## Essence

A smooth projective curve over ℂ is the same thing as a compact Riemann surface, so it has a topological invariant, the genus g, its number of holes. The Riemann–Roch theorem answers the basic question about such a curve: how many independent rational functions are there with poles only at prescribed points, of at most prescribed orders? The answer is the number of conditions minus g plus 1, corrected by a dual term. From this one formula follow the classification of curves of genus 0, the equation of every elliptic curve, and the threefold division of curves into spherical, flat and hyperbolic, which reappears in arithmetic as the question of how many rational points a curve can have.

## Core tenets

1. **Curves, Riemann surfaces and function fields are one subject.** Over ℂ, a smooth projective curve is a compact Riemann surface, and Riemann's existence theorem says every compact Riemann surface arises this way. Algebraically, a curve is determined by its field of rational functions, a finitely generated extension of k of transcendence degree 1, and morphisms between curves correspond to field inclusions in the reverse direction.

2. **The genus of a plane curve comes from its degree.** A smooth plane curve of degree d has genus g = (d − 1)(d − 2)/2: lines and conics have genus 0, cubics genus 1, quartics genus 3. One proof projects the curve to a line from a point off it, a d-to-1 map, counts the branch points with Bézout, and applies the Riemann–Hurwitz formula, 2g(X) − 2 = n·(2g(Y) − 2) + ∑ (eₚ − 1) for an n-to-1 map with ramification indices eₚ. So no smooth plane curve has genus 2; such curves appear instead as y² = f(x) with f of degree 5 or 6.

3. **Divisors are the curve's ideals.** A divisor is a finite formal sum D = ∑ nₚP of points with integer coefficients; its degree is ∑ nₚ. A non-zero rational function f has a divisor div f, its zeros minus its poles with multiplicity, and on a projective curve deg div f = 0: a function has as many zeros as poles. Divisors modulo principal divisors form the Picard group. For an affine curve the coordinate ring is a Dedekind domain, and its ideal class group is a Picard group, so this is the [class group](../01-algebraic-number-theory/ideals-and-the-class-group.md) in geometric form.

4. **Riemann–Roch counts functions with bounded poles.** For a divisor D, let L(D) be the space of rational functions f with div f + D ≥ 0, together with 0, and ℓ(D) its dimension. There is a canonical divisor K, the divisor of any meromorphic differential, of degree 2g − 2. Then

   ```
   ℓ(D) − ℓ(K − D) = deg D − g + 1
   ```

   Riemann proved the inequality ℓ(D) ≥ deg D − g + 1 in the 1850s, and Roch identified the correction term in the 1860s. The modern proof uses sheaf cohomology and Serre duality.

5. **Large divisors make the formula exact.** If deg D > 2g − 2, then K − D has negative degree, so ℓ(K − D) = 0 and ℓ(D) = deg D − g + 1. Setting D = 0 gives ℓ(K) = g: the genus counts the independent holomorphic differentials, as Riemann had defined it. If g = 0 and P is a point, ℓ(P) = 2, so there is a function with a single simple pole, which is an isomorphism to ℙ¹.

6. **Riemann–Roch writes down every elliptic curve.** If g = 1 and O is a point, then ℓ(nO) = n for n ≥ 1. So there is a function x with a double pole at O and a function y with a triple pole. The seven functions 1, x, y, x², xy, x³ and y² lie in L(6O), which has dimension 6, so they satisfy a linear relation, and since only x³ and y² have poles of order 6 it can be arranged as y² + a₁xy + a₃y = x³ + a₂x² + a₄x + a₆. This is the Weierstrass equation of an [elliptic curve](../04-elliptic-curves-and-modular-forms/elliptic-curves.md).

7. **Genus divides curves into three worlds.** Over ℂ, genus 0 curves are the sphere, genus 1 curves are flat tori ℂ/Λ for a lattice Λ, and curves of genus at least 2 are quotients of the hyperbolic upper half-plane, by the uniformisation theorem. Arithmetic follows suit over ℚ: genus 0 curves with one rational point have infinitely many, genus 1 curves have a finitely generated group of them, and Faltings proved in 1983 that a curve of genus at least 2 has only finitely many rational points, which was Mordell's conjecture.

8. **Over finite fields the genus bounds the number of points.** For a curve C of genus g over the finite field 𝔽_q, Weil proved in the 1940s that ∣#C(𝔽_q) − q − 1∣ ≤ 2g·√q. This is the Riemann Hypothesis for the zeta function of C: its zeros all lie on the line Re s = 1/2. Curves over finite fields with many points give Goppa's algebraic geometry codes, whose parameters come straight from Riemann–Roch.

## Key concepts

| Term | Meaning |
|---|---|
| Genus g | Number of holes; also dimension of the space of holomorphic differentials |
| Divisor | A finite formal integer combination of points |
| Principal divisor | div f, the zeros minus poles of a rational function, of degree 0 |
| Picard group | Divisors modulo principal divisors, the curve's class group |
| L(D) and ℓ(D) | Functions whose poles are bounded by D, and its dimension |
| Canonical divisor K | Divisor of a differential, of degree 2g − 2 |
| Riemann–Roch | ℓ(D) − ℓ(K − D) = deg D − g + 1 |
| Riemann–Hurwitz | Relates the genera of two curves through the ramification of a map |

## How it fits

- **Below:** [Riemann surfaces](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md) give the analytic picture; the [classification of surfaces](../../07-topology/03-manifolds/classification-of-surfaces.md) shows that genus is a complete topological invariant; [Bézout](projective-varieties-and-bezouts-theorem.md) gives the degree–genus formula.
- **Above:** curves over finite fields give [error-correcting codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md); modular curves carry [modular forms](../04-elliptic-curves-and-modular-forms/modular-forms.md) as differentials.
- **Siblings:** [schemes](schemes.md) give the sheaf-cohomology proof; function fields parallel [number fields](../01-algebraic-number-theory/number-fields-and-algebraic-integers.md); Weil's bound is the curve analogue of the [Riemann Hypothesis](../02-analytic-number-theory/the-riemann-zeta-function.md).

## Common misconceptions

- **"A curve is one-dimensional, so it is a line-like object"**: over ℂ it is a real surface, and its genus is a hole count of that surface.
- **"Riemann–Roch gives ℓ(D) directly"**: it gives a difference; exact values need deg D > 2g − 2 or knowledge of ℓ(K − D).

## Go deeper

- Rick Miranda, *Algebraic Curves and Riemann Surfaces* (1995): Riemann–Roch from the analytic side, with many examples.
- William Fulton, *Algebraic Curves* (1969, revised edition freely available online): Riemann–Roch by pure algebra.
- Robin Hartshorne, *Algebraic Geometry* (1977), chapter IV: curves in the language of schemes and cohomology.
