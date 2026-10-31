# The Fundamental Theorem of Calculus

> **Layer:** [06 Real Analysis](../README.md) › [Calculus of One Variable](README.md)
> **Builds on:** [The Riemann integral](the-riemann-integral.md), [The derivative and the mean value theorem](the-derivative-and-the-mean-value-theorem.md)
> **Enables:** [Multiple integrals and change of variables](../03-calculus-of-several-variables/multiple-integrals-and-change-of-variables.md), [Vector calculus and the integral theorems](../03-calculus-of-several-variables/vector-calculus-and-the-integral-theorems.md), [The Lebesgue integral](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md), [Existence and uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md), [Stochastic calculus](../../11-probability-and-statistics/03-stochastic-processes/stochastic-calculus.md)

## Essence

Differentiation measures local change; integration adds up accumulated change. The fundamental theorem of calculus (FTC) says they undo each other. Part 1: integrating a continuous f from a to x gives a function whose derivative is f. Part 2: integrating a derivative F′ over [a, b] gives the net change F(b) − F(a). This turns the computation of areas, a limit of sums, into the search for an antiderivative, which is why calculus became a practical tool. The precise hypotheses matter: each part fails, in instructive ways, when they are dropped, and repairing those failures is part of the work of Lebesgue's theory.

## Core tenets

1. **Part 1: if f is Riemann integrable on [a, b] and F(x) = ∫ₐˣ f, then F is continuous, and F′(c) = f(c) at every point c where f is continuous.** F is Lipschitz: |F(x) − F(y)| ≤ sup|f|·|x − y|. For the derivative, write
   ```
   (F(c + h) − F(c))/h − f(c) = (1/h)·∫ from c to c+h of (f(t) − f(c)) dt
   ```
   The right side is at most the largest value of |f(t) − f(c)| for t within h of c, which tends to 0 by continuity at c. Where f jumps, F has a corner: for f(t) = sign t, F(x) = |x|, which has no derivative at 0.

2. **Part 2: if F is continuous on [a, b], differentiable on (a, b), and F′ is Riemann integrable, then ∫ₐᵇ F′ = F(b) − F(a).** Take any partition. The net change telescopes, F(b) − F(a) = ∑(F(xᵢ) − F(xᵢ₋₁)), and the mean value theorem writes each term as F′(tᵢ)·Δxᵢ for some tᵢ in the piece. So F(b) − F(a) is a Riemann sum of F′, and therefore lies between the lower and upper sums for every partition. The only number with that property is the integral. Continuity of F′ is never used.

3. **Integrability of F′ cannot be dropped.** F(x) = x² sin(1/x²), with F(0) = 0, is differentiable everywhere, but F′ is unbounded near 0, so it is not Riemann integrable. Worse, Volterra constructed in 1881 a function that is differentiable everywhere with a bounded derivative that is still not Riemann integrable, because the derivative is discontinuous on a set of positive length. The Lebesgue integral repairs this case: a bounded derivative is always Lebesgue integrable, and Part 2 then holds.

4. **Differentiability everywhere cannot be weakened to "almost everywhere".** The Cantor function is continuous and increasing from 0 at x = 0 to 1 at x = 1, yet its derivative is 0 at every point outside the Cantor set, which has length 0. Integrating the derivative gives 0, not 1. In [the Lebesgue theory](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md) the exact condition for Part 2 is absolute continuity, which the Cantor function lacks.

5. **The rules of integration are the rules of differentiation read backwards.** The product rule gives integration by parts, ∫ₐᵇ fg′ = [fg]ₐᵇ − ∫ₐᵇ f′g, for continuously differentiable f and g. The chain rule gives substitution: for continuous f and continuously differentiable φ, the integral of f(φ(t))·φ′(t) over [a, b] equals the integral of f over [φ(a), φ(b)]. Each follows by differentiating both sides as functions of the upper limit and applying Part 2.

6. **Integrals define new functions, including ones with no formula.** Define ln x as the integral of 1/t from 1 to x, for x > 0. Part 1 gives ln′ x = 1/x, and ln(xy) = ln x + ln y because both sides have derivative 1/x in x and agree at x = 1. Every continuous function has an antiderivative by Part 1, but it need not be elementary: Liouville's theory shows that e^(−x²) has no antiderivative built from exp, log, roots and arithmetic, so the error function is defined by an integral.

7. **Differential equations become integral equations.** For continuous f, a continuous y solves y′ = f(t, y) with y(t₀) = y₀ if and only if y(t) = y₀ + ∫ from t₀ to t of f(s, y(s)) ds. The right side is a map on functions, and iterating it is Picard's method. Proving that the iteration converges uses [the contraction mapping principle](../04-metric-spaces/completeness-and-the-contraction-mapping-principle.md), which gives [existence and uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md) for Ordinary Differential Equations (ODEs).

## Key concepts

| Term | Meaning |
|---|---|
| Antiderivative | A function F with F′ = f on an interval; unique up to an added constant |
| Accumulation function | F(x) = ∫ₐˣ f, the running integral |
| Net change | F(b) − F(a), the telescoping sum of the changes over the pieces |
| Integration by parts | The product rule, integrated |
| Substitution | The chain rule, integrated |
| Cantor function | A continuous increasing function, constant off a set of length 0, rising from 0 to 1 |
| Absolute continuity | The condition under which the Lebesgue form of Part 2 holds |
| Elementary function | One built from polynomials, exp, log, roots and trigonometric functions by arithmetic and composition |

## How it fits

- **Below:** Part 1 uses the definition of [the Riemann integral](the-riemann-integral.md) and continuity; Part 2 uses [the mean value theorem](the-derivative-and-the-mean-value-theorem.md) on every piece of a partition.
- **Above:** Fubini's theorem and the [change of variables](../03-calculus-of-several-variables/multiple-integrals-and-change-of-variables.md) formula reduce many-variable integrals to this theorem. [Green, Stokes and Gauss](../03-calculus-of-several-variables/vector-calculus-and-the-integral-theorems.md) are its higher-dimensional forms, unified by the general Stokes theorem in [differential forms](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md). [Stochastic calculus](../../11-probability-and-statistics/03-stochastic-processes/stochastic-calculus.md) needs a new version because Brownian paths have no derivatives.
- **Siblings:** [Taylor expansion](taylor-expansion.md) gets its integral remainder by repeated integration by parts. [The exponential function](the-exponential-and-trigonometric-functions.md) can be defined as the inverse of ln.

## Common misconceptions

- **"Every function has an antiderivative you can write down."** Continuous functions always have antiderivatives, but often not elementary ones (tenet 6).
- **"If F′ exists everywhere, then ∫F′ = F(b) − F(a) automatically."** For the Riemann integral, F′ must also be integrable (tenet 3).
- **"A function with derivative 0 almost everywhere is constant."** The Cantor function rises from 0 to 1 (tenet 4).

## Go deeper

- Michael Spivak, *Calculus* (4th edition, 2008): both parts with exact hypotheses and many exercises.
- Walter Rudin, *Principles of Mathematical Analysis* (3rd edition, 1976): chapter 6 proves the theorem in its standard form.
- Elias M. Stein and Rami Shakarchi, *Real Analysis* (2005): the Lebesgue version, including absolute continuity and the Cantor function.
