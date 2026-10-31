# The Derivative and the Mean Value Theorem

> **Layer:** [06 Real Analysis](../README.md) › [Calculus of One Variable](README.md)
> **Builds on:** [Continuity](../01-limits-and-convergence/continuity.md), [Sequences and limits](../01-limits-and-convergence/sequences-and-limits.md), [Linear maps and matrices](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md)
> **Enables:** [Taylor expansion](taylor-expansion.md), [The fundamental theorem of calculus](the-fundamental-theorem-of-calculus.md), [The derivative as a linear map](../04-calculus-of-several-variables/the-derivative-as-a-linear-map.md), [Root-finding and Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md), [Calculus for computing](../../../cs-first-principles/01-mathematical-foundations/05-continuous-mathematics/calculus.md)

## Essence

The derivative of f at a is the slope of the best linear approximation to f near a: f(a + h) = f(a) + f′(a)h + o(h), where o(h) stands for an error that is small even compared with h. It is defined as the limit of the slopes of chords, so "instantaneous rate of change" becomes an ordinary limit. Its power comes from the mean value theorem (MVT): on an interval, the average slope (f(b) − f(a))/(b − a) equals f′(c) at some point c in between. The MVT is the bridge from local information, the derivative at each point, to global conclusions such as monotonicity, constancy and error bounds. It rests on the extreme value theorem, and therefore on the completeness of ℝ.

## Core tenets

1. **The derivative is the slope of the unique line with error o(h).** f′(a) is the limit of (f(a + h) − f(a))/h as h → 0, when it exists. Equivalently f(a + h) = f(a) + f′(a)h + r(h) with r(h)/h → 0; any other slope leaves an error of order h. For example (a + h)² = a² + 2ah + h², and h² = o(h), so x² has derivative 2x. This approximation form is the one that generalises: in several variables the slope becomes a linear map.

2. **Differentiable implies continuous, but not conversely.** If f(a + h) − f(a) = f′(a)h + o(h), the right side tends to 0 with h. The function |x| is continuous at 0, but its chord slopes are −1 from the left and 1 from the right, so it has no derivative there. Weierstrass's function is continuous everywhere and differentiable nowhere.

3. **The chain rule composes linear approximations.** If g is differentiable at a and f at g(a), then (f ∘ g)′(a) = f′(g(a))·g′(a). Substitute g(a + h) = g(a) + g′(a)h + o(h) into the linear approximation of f at g(a); the errors stay o(h). The tempting proof, multiplying and dividing by g(a + h) − g(a), breaks when that difference vanishes for small h.

4. **At an interior extremum the derivative vanishes (Fermat's theorem).** If f has a local maximum at an interior point c and f′(c) exists, the chord slopes are ≥ 0 for h < 0 and ≤ 0 for h > 0, so their limit is 0. "Interior" matters: x on [0, 1] is largest at 1, where its derivative is 1. The converse fails: x³ has derivative 0 at 0 but no extremum there.

5. **Mean value theorem: if f is continuous on [a, b] and differentiable on (a, b), then f′(c) = (f(b) − f(a))/(b − a) for some c in (a, b).** First Rolle's theorem, the case f(a) = f(b): by the extreme value theorem f has a maximum and a minimum on [a, b]; if both occur at the ends, f is constant, and otherwise one is interior, where Fermat gives f′(c) = 0. For the MVT, apply Rolle to f minus its chord. Each hypothesis is needed: |x| on [−1, 1] has equal end values but no horizontal tangent, and f(x) = x on [0, 1) with f(1) = 0 fails at the discontinuous end.

6. **The MVT turns local facts into global ones, but only on an interval.** If f′ = 0 on an interval then f is constant, since f(x) − f(y) = f′(c)(x − y) = 0. Likewise f′ > 0 makes f increasing, and |f′| ≤ M gives |f(x) − f(y)| ≤ M|x − y|. All of this fails off intervals of ℝ. On ℚ, the function equal to 0 where x² < 2 and 1 where x² > 2 has derivative 0 at every point, yet is not constant. The same idea proves inequalities: x − sin x vanishes at 0 and has derivative 1 − cos x ≥ 0, so sin x ≤ x for x ≥ 0.

7. **For vector-valued functions the MVT fails, but the inequality survives.** For f(t) = (cos t, sin t) on [0, 2π], f(2π) − f(0) = 0, yet the velocity (−sin t, cos t) never vanishes. What survives is ∥f(b) − f(a)∥ ≤ (b − a)·sup ∥f′∥. Multivariable calculus uses this inequality form.

8. **Derivatives need not be continuous, but they have the intermediate value property (Darboux's theorem).** f(x) = x² sin(1/x), with f(0) = 0, has f′(0) = 0 because |f(x)| ≤ x². For x ≠ 0, f′(x) = 2x sin(1/x) − cos(1/x), which keeps oscillating between values near −1 and 1 as x → 0. Still, every derivative takes all values between any two of its values: apply the extreme value theorem to f(x) − kx. So a function with a jump, such as the sign function, is the derivative of nothing.

## Key concepts

| Term | Meaning |
|---|---|
| Difference quotient | (f(a + h) − f(a))/h, the slope of a chord |
| Derivative f′(a) | The limit of the difference quotients as h → 0 |
| Linear approximation | h ↦ f(a) + f′(a)h, the unique line whose error is o(h) |
| Critical point | A point where f′ = 0 |
| Mean value theorem (MVT) | f(b) − f(a) = f′(c)(b − a) for some c between a and b |
| Cauchy mean value theorem | (f(b) − f(a))·g′(c) = (g(b) − g(a))·f′(c) for some c; it yields L'Hôpital's rule |
| Lipschitz bound | ∣f(x) − f(y)∣ ≤ M∣x − y∣ on an interval where ∣f′∣ ≤ M |

## How it fits

- **Below:** The derivative is a limit, from [sequences and limits](../01-limits-and-convergence/sequences-and-limits.md). Rolle's theorem needs the extreme value theorem from [continuity](../01-limits-and-convergence/continuity.md), which needs completeness. The approximation h ↦ f′(a)h is a [linear map](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md) from ℝ to ℝ.
- **Above:** In several variables the derivative becomes a [linear map](../04-calculus-of-several-variables/the-derivative-as-a-linear-map.md) with a matrix. [Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md) iterates the linear approximation, and [differential equations](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md) are statements about derivatives.
- **Siblings:** [Taylor expansion](taylor-expansion.md) iterates Rolle's theorem to get higher-order approximations. [The fundamental theorem of calculus](the-fundamental-theorem-of-calculus.md) uses the MVT on each piece of a partition. [exp](the-exponential-and-trigonometric-functions.md) is the function equal to its own derivative.

## Common misconceptions

- **"A function differentiable everywhere has a continuous derivative."** x² sin(1/x) is a counterexample (tenet 8).
- **"If f′(a) > 0, then f is increasing near a."** f(x) = x + 2x² sin(1/x), with f(0) = 0, has f′(0) = 1. Yet f′(x) = −1 at every x = 1/(2πk), so f is monotone on no interval around 0.
- **"The MVT tells you where c is."** It only says that c exists. Its value lies in the bound it gives wherever c happens to be.

## Go deeper

- Michael Spivak, *Calculus* (4th edition, 2008): careful proofs and superb exercises.
- Stephen Abbott, *Understanding Analysis* (2nd edition, 2015): a gentle path that includes Darboux's theorem.
- E. Hairer and G. Wanner, *Analysis by Its History* (1996): how the derivative evolved from Newton and Leibniz to Cauchy and Weierstrass.
