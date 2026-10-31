# Singularities and Residues

> **Layer:** [09 Advanced Analysis](../README.md) › [Complex Analysis](README.md)
> **Builds on:** [Cauchy's Theorem and Its Consequences](cauchys-theorem-and-its-consequences.md), [Holomorphic Functions](holomorphic-functions.md), [Series](../../06-real-analysis/01-limits-and-convergence/series.md)
> **Enables:** [Analytic Continuation and Riemann Surfaces](analytic-continuation-and-riemann-surfaces.md), [The Riemann Zeta Function](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md), [The Prime Number Theorem](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-prime-number-theorem.md), [Modular Forms](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/modular-forms.md)

## Essence

A holomorphic function on a punctured disc around z₀ has an isolated singularity at z₀. Its behaviour there falls into exactly three types, read off from a Laurent series, a power series that is allowed negative powers. Only one coefficient of that series survives integration around z₀: the coefficient of 1/(z − z₀), called the residue. The residue theorem turns a contour integral into a finite sum of residues, which is both a computing machine for real integrals that resist every calculus trick and a counting device for zeros and poles.

## Core tenets

1. **Laurent series: holomorphic on an annulus means a two-sided power series.** If f is holomorphic on r < ∣z − z₀∣ < R, then f(z) = ∑ aₙ(z − z₀)ⁿ over all integers n, converging on the annulus. Proof idea: apply Cauchy's integral formula on the annulus as the difference of two circles; expanding 1/(w − z) in powers of (z − z₀) on the outer circle gives the non-negative powers, and in powers of 1/(z − z₀) on the inner circle the negative ones. The coefficients are aₙ = (1/2πi)·∮ f(w)/(w − z₀)ⁿ⁺¹ dw, so the series is unique.

2. **There are exactly three kinds of isolated singularity.** If no negative powers occur, the singularity is removable: define f(z₀) = a₀. If finitely many occur, with lowest power −k, it is a pole of order k and ∣f∣ → ∞. If infinitely many occur, it is essential. Riemann's removable singularity theorem says that boundedness near z₀ already forces the first case: Cauchy's estimates on small circles give ∣a₋ₙ∣ ≤ M·rⁿ for every small r, so a₋ₙ = 0. Thus sin z/z has a removable singularity at 0, 1/z² a pole of order 2, and e^(1/z) = ∑ 1/(n!·zⁿ) an essential one.

3. **Near an essential singularity f takes almost every value.** The Casorati–Weierstrass theorem says that f maps every punctured disc around an essential singularity onto a dense set. Proof idea: if f stayed at distance ε from some c, then 1/(f − c) would be bounded, hence have a removable singularity, which would make f have at worst a pole. Picard's great theorem says far more: every complex value except at most one is taken infinitely often. For e^(1/z), the omitted value is 0.

4. **The residue theorem: integrals count residues.** Integrating a Laurent series term by term, ∮ (z − z₀)ⁿ dz is 0 for every n except n = −1, where it is 2πi. So only a₋₁ survives, and it is called the residue Res(f, z₀). If f is holomorphic on U except at isolated points z₁, …, z_m and γ is a closed curve in U that winds around no point outside U, then

   ```
   ∮_γ f(z) dz = 2πi · ∑ₖ n(γ, zₖ) · Res(f, zₖ)
   ```

   where n(γ, zₖ) is the winding number. At a simple pole the residue is lim (z − z₀)·f(z), so for f = g/h with h(z₀) = 0 and h′(z₀) ≠ 0 it is g(z₀)/h′(z₀).

5. **Real integrals become residue sums once the extra arc dies.** To compute ∫ dx/(1 + x²) over ℝ, close the segment [−R, R] with a semicircle in the upper half-plane. Inside lies the pole at i, with residue 1/(2i), so the closed integral is 2πi/(2i) = π. On the arc ∣1/(1 + z²)∣ ≤ 1/(R² − 1) and the arc has length πR, so its contribution tends to 0 and the real integral is π. For ∫ sin x/x = π over ℝ, integrate e^(iz)/z with a small detour round 0; the arc estimate needs Jordan's lemma, because e^(iz) decays only in the upper half-plane and only like e^(−R·sin θ).

6. **The argument principle counts zeros minus poles.** If f is meromorphic inside a simple closed curve γ with no zeros or poles on it, then (1/2πi)·∮ f′/f dz = Z − P, the number of zeros minus the number of poles inside, counted with multiplicity. The reason is that f′/f has a simple pole with residue k at a zero of order k and −k at a pole of order k. Geometrically, it is the winding number of the image curve f(γ) about 0. Rouché's theorem follows: if ∣g∣ < ∣f∣ on γ, then f and f + g have the same number of zeros inside, since the image curve cannot be dragged across 0.

7. **Singularities govern the growth of coefficients.** The radius of convergence of a power series is the distance to its nearest singularity, so the coefficients of a [generating function](../../03-combinatorics-and-graph-theory/01-enumeration/generating-functions.md) grow at a rate fixed by that point. The Fibonacci numbers have generating function z/(1 − z − z²), whose nearest pole is at 1/φ with φ = (1 + √5)/2, so Fₙ grows like φⁿ; the residue gives the constant 1/√5. The [Riemann zeta function](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md) has a simple pole at 1 with residue 1, and that single fact, combined with the absence of zeros on the line Re s = 1, yields the [prime number theorem](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-prime-number-theorem.md).

## Key concepts

| Term | Meaning |
|---|---|
| Isolated singularity | A point where f is undefined but holomorphic on a punctured disc around it |
| Laurent series | ∑ aₙ(z − z₀)ⁿ over all integers n, converging on an annulus |
| Removable singularity | No negative powers; f extends holomorphically |
| Pole of order k | Lowest power is −k; ∣f∣ → ∞ |
| Essential singularity | Infinitely many negative powers |
| Meromorphic | Holomorphic except at isolated poles |
| Residue | The coefficient a₋₁; (1/2πi) times the integral round a small circle |
| Argument principle | (1/2πi)·∮ f′/f dz = Z − P |
| Rouché's theorem | A small perturbation does not change the number of zeros inside a curve |

## How it fits

- **Below:** [Cauchy's theorem](cauchys-theorem-and-its-consequences.md) supplies the integral formula and the estimates; [series](../../06-real-analysis/01-limits-and-convergence/series.md) supply the convergence of Laurent expansions.
- **Above:** the [zeta function](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md), the [prime number theorem](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-prime-number-theorem.md) and [modular forms](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/modular-forms.md) in 12 are studied through their poles and residues.
- **Siblings:** [analytic continuation](analytic-continuation-and-riemann-surfaces.md) asks what happens at singularities that are not isolated, such as branch points; the [Fourier transform](../04-harmonic-analysis/the-fourier-transform.md) is often computed by closing contours.

## Common misconceptions

- **"A singularity is where the formula breaks down"**: sin z/z has a formula that fails at 0, but the singularity is removable and the function is entire.
- **"The residue at a pole of order k is the coefficient you see first"**: it is always the coefficient of 1/(z − z₀), not of the lowest power.

## Go deeper

- Lars V. Ahlfors, *Complex Analysis* (3rd edition, 1979): the residue calculus and real integrals.
- Elias M. Stein and Rami Shakarchi, *Complex Analysis* (2003): residues, Rouché and the route to the prime number theorem.
- Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics* (2009): reading coefficient growth from singularities.
