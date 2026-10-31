# The Lebesgue Integral

> **Layer:** [09 Advanced Analysis](../README.md) › [Measure and Integration](README.md)
> **Builds on:** [Measure and σ-Algebras](measure-and-sigma-algebras.md), [The Riemann Integral](../../06-real-analysis/02-calculus-of-one-variable/the-riemann-integral.md), [Uniform Convergence](../../06-real-analysis/01-limits-and-convergence/uniform-convergence.md), [Multiple Integrals and Change of Variables](../../06-real-analysis/03-calculus-of-several-variables/multiple-integrals-and-change-of-variables.md)
> **Enables:** [Lᵖ Spaces](lp-spaces.md), [The Radon–Nikodym Theorem](the-radon-nikodym-theorem.md), [The Fourier Transform](../04-harmonic-analysis/the-fourier-transform.md), [Random Variables and Distributions](../../11-probability-and-statistics/01-measure-theoretic-probability/random-variables-and-distributions.md), [Modes of Convergence](../../11-probability-and-statistics/02-limit-theorems/modes-of-convergence.md)

## Essence

Riemann slices the domain into intervals; Henri Lebesgue, in his thesis of 1902, sliced the range instead and asked how large the set is where the function takes values in each slice. Because that set is measured by a countably additive measure, the new integral inherits countable additivity, and with it three theorems that say when the integral of a limit is the limit of the integrals. Exchanging limit and integral is the whole point: it makes function spaces complete, justifies differentiating under the integral sign, and lets probability treat expectation as an integral. Every Riemann integrable function on an interval is Lebesgue integrable with the same integral, and many more functions are.

## Core tenets

1. **The integral is built from functions that take finitely many values.** A function f: X → ℝ is measurable when every set {f > t} lies in the σ-algebra. A simple function s = ∑ cᵢ·1_(Aᵢ), with 1_A the indicator of A, has integral ∑ cᵢ·μ(Aᵢ). For measurable f ≥ 0, ∫ f dμ is the supremum of ∫ s over simple 0 ≤ s ≤ f. A general f is split as f⁺ − f⁻ into positive and negative parts, and it is integrable when ∫ ∣f∣ dμ < ∞. The Dirichlet function 1_ℚ on [0, 1] has upper Riemann sums 1 and lower sums 0, but its Lebesgue integral is m(ℚ ∩ [0, 1]) = 0.

2. **The new integral extends the Riemann integral, with one caveat.** A bounded function on [a, b] is Riemann integrable if and only if its points of discontinuity form a null set (Lebesgue's criterion), and then the two integrals agree. The caveat concerns improper integrals. ∫₀^∞ (sin x)/x dx converges to π/2 as a limit of Riemann integrals, but ∫ ∣sin x∣/x dx = ∞, so the function is not Lebesgue integrable. The Lebesgue theory admits only absolutely convergent integrals, as it admits only absolutely convergent series.

3. **Monotone convergence: increasing limits pass through the integral.** If 0 ≤ f₁ ≤ f₂ ≤ … are measurable and fₙ → f pointwise, then ∫ fₙ → ∫ f, with ∞ allowed. One inequality is monotonicity. For the other, fix a simple s ≤ f and c < 1. The sets Eₙ = {fₙ ≥ c·s} increase to the whole space, so continuity of the measure gives ∫ fₙ ≥ c·∫ over Eₙ of s → c·∫ s. Countable additivity is the engine, and the corollary ∫ ∑ gₙ = ∑ ∫ gₙ holds for every series of non-negative functions.

4. **Fatou's lemma: in the limit mass can be lost, never gained.** For measurable fₙ ≥ 0, ∫ liminf fₙ ≤ liminf ∫ fₙ; apply monotone convergence to gₙ = inf over k ≥ n of f_k. The inequality can be strict, in two typical ways:

   ```
   fₙ = n·1_(0, 1/n)  on [0, 1]:  ∫ fₙ = 1 for all n,  fₙ → 0 pointwise   (mass escapes upward)
   fₙ = 1_[n, n+1]    on ℝ:       ∫ fₙ = 1 for all n,  fₙ → 0 pointwise   (mass escapes to infinity)
   ```

   Positivity matters: with fₙ replaced by −fₙ, the inequality reverses.

5. **Dominated convergence: one integrable bound stops the escape.** If fₙ → f almost everywhere and ∣fₙ∣ ≤ g for every n, with ∫ g < ∞, then ∫ ∣fₙ − f∣ → 0, so ∫ fₙ → ∫ f. The proof applies Fatou's lemma to 2g − ∣fₙ − f∣ ≥ 0. Neither example above has an integrable dominating function: the smallest bound for n·1_(0, 1/n) behaves like 1/x near 0. The Riemann theory needs uniform convergence on a bounded interval; this needs only convergence almost everywhere and a bound.

6. **Functions equal almost everywhere are the same for integration.** Changing f on a null set changes no integral, and ∫ ∣f∣ = 0 if and only if f = 0 almost everywhere. So the natural objects are equivalence classes of functions, which is how [Lᵖ spaces](lp-spaces.md) are defined. In [probability](../../11-probability-and-statistics/01-measure-theoretic-probability/random-variables-and-distributions.md) the expectation E[X] is just ∫ X dP, and "almost surely" means "almost everywhere".

7. **Fubini–Tonelli: integrate in either order when the function is non-negative or absolutely integrable.** On a product of σ-finite measure spaces, Tonelli's theorem says that for measurable f ≥ 0 both iterated integrals equal the double integral, possibly ∞. Fubini's theorem says the same for any f with ∫∫ ∣f∣ < ∞. Each hypothesis is needed:

   ```
   f(x, y) = (x² − y²)/(x² + y²)²  on (0, 1]²
   ∫₀¹ f dy = 1/(1 + x²),   so  ∫₀¹ ∫₀¹ f dy dx =  π/4
   ∫₀¹ f dx = −1/(1 + y²),  so  ∫₀¹ ∫₀¹ f dx dy = −π/4      (∫∫ ∣f∣ = ∞)
   ```

   Without σ-finiteness the indicator of the diagonal of [0, 1]², with counting measure in one factor and length in the other, has iterated integrals 1 and 0.

## Key concepts

| Term | Meaning |
|---|---|
| Measurable function | f with {f > t} in the σ-algebra for every real t |
| Simple function | A finite sum ∑ cᵢ·1_(Aᵢ) with measurable Aᵢ |
| Integrable | Measurable with ∫ ∣f∣ dμ < ∞ |
| Almost everywhere | Outside a set of measure 0 |
| Monotone convergence theorem | 0 ≤ fₙ increasing to f implies ∫ fₙ → ∫ f |
| Fatou's lemma | ∫ liminf fₙ ≤ liminf ∫ fₙ for fₙ ≥ 0 |
| Dominated convergence theorem | fₙ → f almost everywhere and ∣fₙ∣ ≤ g integrable imply ∫ fₙ → ∫ f |
| Product measure | The measure on X × Y with (μ × ν)(A × B) = μ(A)·ν(B) |
| Fubini–Tonelli theorem | Iterated integrals agree for non-negative or absolutely integrable functions |

## How it fits

- **Below:** the [Riemann integral](../../06-real-analysis/02-calculus-of-one-variable/the-riemann-integral.md) is the special case; [uniform convergence](../../06-real-analysis/01-limits-and-convergence/uniform-convergence.md) was the old, too strong, condition for swapping limits; [multiple integrals](../../06-real-analysis/03-calculus-of-several-variables/multiple-integrals-and-change-of-variables.md) become Fubini's theorem.
- **Above:** [modes of convergence](../../11-probability-and-statistics/02-limit-theorems/modes-of-convergence.md) in 11 compare almost-sure convergence with convergence of expectations; the [Fourier transform](../04-harmonic-analysis/the-fourier-transform.md) is an integral whose continuity is dominated convergence.
- **Siblings:** [measure](measure-and-sigma-algebras.md) supplies the sizes; [Lᵖ spaces](lp-spaces.md) measure functions by integrals of their powers; the [Radon–Nikodym theorem](the-radon-nikodym-theorem.md) asks which measures are integrals of a density.

## Common misconceptions

- **"The Lebesgue integral exists to integrate strange functions"**: its value lies in the convergence theorems, which make ordinary analysis with limits rigorous.
- **"Pointwise convergence gives convergence of integrals"**: n·1_(0, 1/n) converges to 0 everywhere while every integral is 1.
- **"Every convergent improper Riemann integral is a Lebesgue integral"**: (sin x)/x on [0, ∞) is the standard exception.
- **"Iterated integrals can always be swapped"**: only under Tonelli's or Fubini's hypotheses.

## Go deeper

- Gerald B. Folland, *Real Analysis: Modern Techniques and Their Applications* (2nd edition, 1999): the convergence theorems and Fubini–Tonelli, cleanly done.
- Walter Rudin, *Real and Complex Analysis* (3rd edition, 1987): the classic graduate route.
- David M. Bressoud, *A Radical Approach to Lebesgue's Theory of Integration* (2008): the history of why the theory was needed.
