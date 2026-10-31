# Iterated Maps

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Dynamical Systems](README.md)
> **Builds on:** [Stability and phase portraits](../01-ordinary-differential-equations/stability-and-phase-portraits.md), [The derivative and the mean value theorem](../../06-real-analysis/02-calculus-of-one-variable/the-derivative-and-the-mean-value-theorem.md), [Completeness and the contraction mapping principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md), [Recurrence relations](../../03-combinatorics-and-graph-theory/01-enumeration/recurrence-relations.md)
> **Enables:** [Bifurcations](bifurcations.md), [Chaos and strange attractors](chaos-and-strange-attractors.md), [Ergodic theory](ergodic-theory.md), [Root-finding and Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md), [Mathematical biology and epidemics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md)

## Essence

Iterating a map, xₙ₊₁ = f(xₙ), is the simplest dynamical system: time moves in steps, as in yearly population counts, Newton's method, or the successive crossings of a flow through a surface. One dimension already holds almost every phenomenon of dynamics. The logistic map f(x) = r·x(1 − x) moves, as r grows, from a stable equilibrium through a cascade of period doublings into chaos, and the rate of that cascade is a universal constant shared by every smooth map with a single hump. Robert May's 1976 survey in *Nature* made the point widely known: simple deterministic rules can behave unpredictably.

## Core tenets

1. **A fixed point attracts when |f′| < 1 there.** If f(x*) = x* and f is C¹ with |f′(x*)| < 1, the mean value theorem makes f a contraction on a small interval around x*, so nearby orbits converge to it geometrically; if |f′(x*)| > 1 they are pushed away. At |f′(x*)| = 1 the test is silent: sin x attracts to 0 slowly and x + x³ repels, though both have derivative 1 there. Newton's method x ↦ x − g(x)/g′(x) has derivative 0 at a simple root, so the error is squared at each step.

2. **The logistic map loses stability by period doubling.** For 0 ≤ r ≤ 4 the map f(x) = r·x(1 − x) sends [0, 1] into itself. The fixed point x* = 1 − 1/r has f′(x*) = 2 − r, so it attracts for 1 < r < 3. At r = 3 the derivative passes −1, and an attracting orbit of period 2 is born. A cycle's stability is governed by the product of f′ along it, and this 2-cycle in turn loses stability at r = 1 + √6 ≈ 3.449, giving period 4.

3. **The cascade is universal.** Period 8 appears at r ≈ 3.5441, period 16 at r ≈ 3.5644, and the doublings accumulate at r∞ ≈ 3.5699. The gaps between successive doublings shrink by the factor δ = 4.6692016…, and the same δ appears for every smooth one-humped map with a quadratic maximum, and in experiments on fluids. Feigenbaum (1978) explained this by renormalisation: rescaling the second iterate is an operator on maps whose fixed point has unstable eigenvalue δ. Lanford (1982) gave a computer-assisted proof; Sullivan, McMullen and Lyubich later gave conceptual ones.

4. **Period three implies all periods.** Li and Yorke (1975): a continuous map of an interval with a point of period 3 has points of every period. Proof idea: for an orbit a < b < c with f(a) = b, f(b) = c and f(c) = a, the intervals I = [a, b] and J = [b, c] satisfy f(I) ⊇ J and f(J) ⊇ I ∪ J, and by the intermediate value theorem each loop of such coverings contains a periodic point following it. Sharkovskii (1964) had found the complete ordering 3 ▷ 5 ▷ 7 ▷ … ▷ 2·3 ▷ 2·5 ▷ … ▷ 4·3 ▷ … ▷ 8 ▷ 4 ▷ 2 ▷ 1: period m forces every period after it. The order needs the line: rotation of the plane by 120° has period 3 everywhere except the centre, and no period 2.

5. **At r = 4 the logistic map is a coin toss.** The substitution x = sin²(πθ) turns 4x(1 − x) into θ ↦ 2θ mod 1, which shifts the binary digits of θ one place left. So orbits correspond to binary sequences, periodic points are dense, nearby points separate like 2ⁿ (Lyapunov exponent ln 2), and almost every orbit spends time near x in proportion to the density 1/(π·√(x(1 − x))).

6. **Order and chaos are interleaved.** In the logistic family, windows with an attracting cycle are dense among parameters (Graczyk and Świątek; Lyubich; both 1997), the period-3 window opening at r = 1 + √8 ≈ 3.8284. Yet the parameters with chaotic behaviour, an absolutely continuous invariant measure, have positive length (Jakobson, 1981). The complex map z ↦ z² + c contains the logistic family on its real line, and its Mandelbrot set, the c for which the orbit of 0 stays bounded, is connected (Douady and Hubbard, 1982).

## Key concepts

| Term | Meaning |
|---|---|
| Orbit | The sequence x, f(x), f(f(x)), … |
| Periodic point | A point with fⁿ(x) = x for some n ≥ 1; the least such n is its period |
| Multiplier | The product of f′ over the points of a cycle, which decides its stability |
| Period doubling | A cycle losing stability as its multiplier passes −1, creating a cycle of twice the period |
| Feigenbaum constant | δ = 4.6692016…, the universal ratio of successive doubling intervals |
| Conjugacy | A change of variables h with h ∘ f = g ∘ h, showing two maps have the same dynamics |
| Lyapunov exponent | The average exponential rate, lim (1/n)·ln∣(fⁿ)′(x)∣, at which nearby orbits separate |

## How it fits

- **Below:** |f′| < 1 is the [contraction mapping principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md) with its constant from the [mean value theorem](../../06-real-analysis/02-calculus-of-one-variable/the-derivative-and-the-mean-value-theorem.md); linear [recurrence relations](../../03-combinatorics-and-graph-theory/01-enumeration/recurrence-relations.md) are the solvable case; the continuous-time analogue is [stability of equilibria](../01-ordinary-differential-equations/stability-and-phase-portraits.md), with |f′| < 1 in place of negative real part.
- **Above:** [Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md) is an iterated map whose basins in the complex plane are fractal; discrete-generation population models in [mathematical biology](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md) are logistic maps.
- **Siblings:** [bifurcations](bifurcations.md) classify how fixed points and cycles appear; [chaos](chaos-and-strange-attractors.md) extends the coding of tenet 5 to the horseshoe; [ergodic theory](ergodic-theory.md) explains the invariant density.

## Common misconceptions

- **"Simple rules produce simple behaviour."**: a one-line quadratic recurrence is chaotic at r = 4.
- **"A computer plot shows the long-term behaviour."**: floating-point orbits eventually cycle, and stable windows can be too narrow to see; theorems such as Jakobson's are needed to know what is typical.
- **"Period doubling is a quirk of the logistic map."**: the constant δ is universal across a whole class of maps and physical systems.

## Go deeper

- Robert L. Devaney, *An Introduction to Chaotic Dynamical Systems* (2nd edition, 1989): one-dimensional dynamics, Sharkovskii's theorem and symbolic dynamics with proofs.
- Robert M. May, "Simple Mathematical Models with Very Complicated Dynamics" (1976): the survey in *Nature* that made the logistic map famous.
- Welington de Melo and Sebastian van Strien, *One-Dimensional Dynamics* (1993): the research-level theory, including renormalisation.
