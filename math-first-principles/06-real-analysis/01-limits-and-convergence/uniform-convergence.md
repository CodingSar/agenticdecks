# Uniform Convergence

> **Layer:** [06 Real Analysis](../README.md) › [Limits and Convergence](README.md)
> **Builds on:** [Sequences and limits](sequences-and-limits.md), [Series](series.md), [Continuity](continuity.md)
> **Enables:** [Power series and analytic functions](../02-calculus-of-one-variable/power-series-and-analytic-functions.md), [The exponential and trigonometric functions](../02-calculus-of-one-variable/the-exponential-and-trigonometric-functions.md), [Compactness in metric spaces](../03-metric-spaces/compactness-in-metric-spaces.md), [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md), [Banach spaces](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md), [The Lebesgue integral](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md)

## Essence

A sequence of functions fₙ can converge to f in two very different ways. Pointwise: for each x separately, fₙ(x) → f(x). Uniformly: the worst error over all x, sup |fₙ(x) − f(x)|, tends to 0, so one stage N works for every x at once. Pointwise limits can destroy continuity, change integrals and break derivatives. Uniform limits preserve continuity and integrals, because each question about the limit becomes a question about one good function f_N plus an error that is small everywhere. Uniform convergence is what makes term-by-term work with power series legitimate.

## Core tenets

1. **A pointwise limit of continuous functions need not be continuous.** On [0, 1], fₙ(x) = xⁿ tends to 0 for x < 1 and to 1 at x = 1, a discontinuous limit. For x close to 1, xⁿ is small only for huge n, so the stage N depends on x and no single N works. Indeed sup |xⁿ − 0| over [0, 1) equals 1 for every n, so the convergence is not uniform.

2. **A uniform limit of continuous functions is continuous, by the ε/3 argument.** Split the error into three terms:
   ```
   |f(x) − f(a)| ≤ |f(x) − f_N(x)| + |f_N(x) − f_N(a)| + |f_N(a) − f(a)|
   ```
   Uniformity makes the first and third terms below ε/3 for every x, with one N. Continuity of the single function f_N then makes the middle term below ε/3 for x near a. Pointwise convergence controls the outer terms only for one x at a time, which is why tenet 1 fails. The argument exchanges two limits, in x and in n, and uniformity licenses the exchange.

3. **Uniform convergence passes limits through integrals; pointwise convergence does not.** If fₙ → f uniformly on [a, b], the integrals differ by at most (b − a)·sup |fₙ − f|, which tends to 0. Pointwise convergence fails: let fₙ be the tent of height n over [0, 2/n], zero elsewhere. Each fₙ has area 1 and fₙ(x) → 0 for every x, so the integrals tend to 1 while the limit has integral 0. [The Lebesgue integral](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md) permits the exchange under a weaker hypothesis, a fixed integrable bound.

4. **Derivatives need more: the derivatives must converge uniformly.** fₙ(x) = sin(n²x)/n tends to 0 uniformly, yet fₙ′(x) = n cos(n²x) diverges at most points. The correct theorem: if each fₙ is differentiable on [a, b], the fₙ′ converge uniformly, and fₙ(x₀) converges at one point, then fₙ converges uniformly to a differentiable f with f′ = lim fₙ′. The proof applies the mean value theorem to fₙ − fₘ, whose small derivative makes it nearly constant.

5. **The Weierstrass M-test: a series dominated by a convergent series of numbers converges uniformly.** If |fₙ(x)| ≤ Mₙ for all x and ∑Mₙ converges, the tails of ∑fₙ are bounded by the tails of ∑Mₙ, whatever x is. So the partial sums are uniformly Cauchy, and they converge uniformly. For a power series with radius R, take Mₙ = |cₙ|rⁿ on |x| ≤ r < R. Hence a power series is continuous inside its radius and can be integrated and differentiated term by term there, since the differentiated series has the same radius. This is how exp, sin and cos are shown to be smooth.

6. **Uniform limits build monsters as well as tools.** Weierstrass's function ∑ aⁿ cos(bⁿπx), with 0 < a < 1, b an odd integer and ab > 1 + 3π/2, converges uniformly by the M-test and so is continuous. Weierstrass showed in 1872 that it is differentiable nowhere: each new term adds wiggles steeper than the earlier terms are smooth. Uniform convergence keeps continuity, but not differentiability.

7. **Every continuous function on [a, b] is a uniform limit of polynomials (the Weierstrass approximation theorem).** On [0, 1], Bernstein's proof uses Bₙ(x) = ∑ f(k/n)·C(n, k)·xᵏ(1 − x)^(n−k), summed over k = 0, …, n, where C(n, k) is the binomial coefficient. The weights are binomial probabilities concentrated near k/n ≈ x, with variance x(1 − x)/n. Uniform continuity of f and this variance bound make sup |Bₙ − f| → 0. Polynomials are thus dense in the continuous functions under the sup distance.

## Key concepts

| Term | Meaning |
|---|---|
| Pointwise convergence | fₙ(x) → f(x) for each x separately |
| Uniform convergence | sup over x of ∣fₙ(x) − f(x)∣ tends to 0 |
| Sup norm | ∥f∥∞ = sup ∣f(x)∣; uniform convergence is convergence in this norm |
| Uniformly Cauchy | For each ε some N gives ∥fₙ − fₘ∥∞ < ε for all m, n ≥ N; implies uniform convergence |
| ε/3 argument | Bound a difference by three terms, each controlled by a different hypothesis |
| Weierstrass M-test | ∣fₙ∣ ≤ Mₙ with ∑Mₙ convergent implies ∑fₙ converges uniformly |
| Bernstein polynomial | Bₙ(x) = ∑ f(k/n)·C(n, k)·xᵏ(1 − x)^(n−k), a weighted average of values of f |

## How it fits

- **Below:** The definitions of [sequences and limits](sequences-and-limits.md) and [continuity](continuity.md), now with a sup over x. [Series](series.md) supplies the comparison series for the M-test.
- **Above:** Tenet 5 makes every [power series](../02-calculus-of-one-variable/power-series-and-analytic-functions.md) smooth inside its radius, and [exp, sin and cos](../02-calculus-of-one-variable/the-exponential-and-trigonometric-functions.md) are built that way. [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md) forced the distinction between pointwise and uniform convergence. Completeness under the sup norm makes the continuous functions a [Banach space](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md) and underlies [Arzelà–Ascoli](../03-metric-spaces/compactness-in-metric-spaces.md). Tenet 7 is the start of [approximation theory](../../14-applied-and-computational-mathematics/01-numerical-analysis/interpolation-and-approximation.md).
- **Siblings:** The ε/3 argument is a pattern from [estimates and inequalities](estimates-and-inequalities.md), applied uniformly in x.

## Common misconceptions

- **"A convergent series of continuous functions has a continuous sum."** Only under uniform convergence. Cauchy's 1821 textbook asserted it without that condition, and a Fourier series refutes it: ∑(−1)ⁿ⁺¹ sin(nx)/n equals x/2 on (−π, π) but 0 at x = π.
- **"If fₙ → f uniformly, then fₙ′ → f′."** Tenet 4 shows the derivatives can diverge; it is the derivatives that must converge uniformly.
- **"Uniform convergence is a technicality."** Without it, continuity, integrals and derivatives can all change in the limit, and every term-by-term manipulation of power series depends on it.

## Go deeper

- Walter Rudin, *Principles of Mathematical Analysis* (3rd edition, 1976): chapter 7, "Sequences and Series of Functions", the standard account, including the Stone–Weierstrass theorem.
- Stephen Abbott, *Understanding Analysis* (2nd edition, 2015): a gentle treatment, with the nowhere-differentiable function built in detail.
- T. W. Körner, *Fourier Analysis* (1988): shows how Fourier series forced these distinctions.
