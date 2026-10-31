# Concentration Inequalities

> **Layer:** [11 Probability and Statistics](../README.md) › [Limit Theorems](README.md)
> **Builds on:** [The Law of Large Numbers](the-law-of-large-numbers.md), [The Central Limit Theorem](the-central-limit-theorem.md), [Expectation and Variance](../../03-combinatorics-and-graph-theory/03-discrete-probability/expectation-and-variance.md), [The Probabilistic Method](../../03-combinatorics-and-graph-theory/03-discrete-probability/the-probabilistic-method.md)
> **Enables:** [Statistical Learning Theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md), [High-Dimensional Geometry and Random Matrices](../../14-applied-and-computational-mathematics/06-data-and-learning/high-dimensional-geometry-and-random-matrices.md), [Sampling and Compressed Sensing](../../14-applied-and-computational-mathematics/06-data-and-learning/sampling-and-compressed-sensing.md), [Hypothesis Tests and Confidence Intervals](../04-statistical-inference/hypothesis-tests-and-confidence-intervals.md), [Randomized Algorithms](../../../cs-first-principles/05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md)

## Essence

The law of large numbers says that an average approaches its mean; the central limit theorem says how it fluctuates in the limit. Neither says how unlikely a deviation of a given size is at a fixed sample size n, and that is what algorithms, statistics and learning theory need. Concentration inequalities answer with explicit bounds valid for every n: a sum of many independent bounded terms deviates from its mean by t with probability at most about e^(−2t²/n). The method is one idea applied with growing sharpness: bound a probability by an expectation, choosing the expectation that best exploits independence.

## Core tenets

1. **Markov's inequality is the root.** For X ≥ 0 and a > 0, a·1{X ≥ a} ≤ X pointwise, so taking expectations gives P(X ≥ a) ≤ E[X]/a. It is tight: the law putting mass E[X]/a at a and the rest at 0 attains it. Every inequality below is Markov's inequality applied to a well-chosen function of X.

2. **Chebyshev's inequality applies Markov to the square.** P(∣X − E[X]∣ ≥ t) ≤ Var(X)/t². For an average of n independent terms of variance σ², this is σ²/(nt²): enough for the weak law, but the decay in t is only polynomial, because it uses no information beyond the second moment.

3. **The Chernoff method applies Markov to an exponential.** For every λ > 0,

   ```
   P(S ≥ a)  =  P(e^(λS) ≥ e^(λa))  ≤  e^(−λa)·E[e^(λS)],
   and if S = X₁ + … + Xₙ with independent terms,
   E[e^(λS)]  =  E[e^(λX₁)] × … × E[e^(λXₙ)].
   ```

   The product is where independence enters, and it is what turns a polynomial bound into an exponential one; one then minimises over λ. Herman Chernoff (1952) used this for sums of Bernoulli variables. Cramér's theorem in large-deviation theory shows that the optimised exponent is exactly right: P(S ≥ na) decays like e^(−n·I(a)), where I is the Legendre transform of log E[e^(λX₁)].

4. **Hoeffding's inequality: bounded independent terms give Gaussian tails.** If the Xᵢ are independent with aᵢ ≤ Xᵢ ≤ bᵢ, then

   ```
   P( S − E[S] ≥ t )  ≤  exp( −2t² / ∑ᵢ (bᵢ − aᵢ)² ).
   ```

   The key step, Hoeffding's lemma, says that a variable with mean 0 confined to [a, b] has E[e^(λX)] ≤ e^(λ²(b − a)²/8); the proof bounds the convex function e^(λx) by its chord on [a, b]. Wassily Hoeffding proved the inequality in 1963. It ignores the variance; Bernstein's inequality uses it and is much sharper when the variance is small compared with the range.

5. **The sharpening is dramatic.** For 1000 fair coin tosses with S heads, the probability that S ≥ 600 is:

   | Bound | Value |
   |---|---|
   | Markov, E[S]/600 | 0.83 |
   | Chebyshev, 250/100² | 0.025 |
   | Hoeffding, e^(−2·100²/1000) | 2.1 × 10⁻⁹ |
   | Optimised Chernoff, e^(−1000·D(0.6‖0.5)) | 1.8 × 10⁻⁹ |
   | Exact | 1.4 × 10⁻¹⁰ |

   Here D(0.6‖0.5) ≈ 0.0201 is the Kullback–Leibler divergence between coins with heads probabilities 0.6 and 0.5. The exponential bounds are within a factor of about 15 of the truth; Chebyshev is off by a factor of a hundred million.

6. **McDiarmid's inequality: functions with bounded differences concentrate.** If f(x₁, …, xₙ) changes by at most cᵢ when only the i-th argument changes, then for independent Xᵢ, P(f − E[f] ≥ t) ≤ exp(−2t²/∑ᵢ cᵢ²). The proof writes f − E[f] as a sum of martingale differences E[f ∣ X₁, …, Xᵢ] − E[f ∣ X₁, …, Xᵢ₋₁], each bounded, and applies the Azuma–Hoeffding inequality (Kazuoki Azuma, 1967). Colin McDiarmid stated it in this form in 1989. The function need not be a sum: the chromatic number of a random graph on n vertices with edge probability 1/2 changes by at most 1 when the edges at one vertex change, so it lies within a few multiples of √n of its mean with high probability, although the mean itself is hard to compute.

7. **Union bounds turn concentration into uniform guarantees.** If each of N quantities deviates by ε with probability at most 2e^(−2nε²), then all are within ε simultaneously with probability at least 1 − δ once n ≥ log(2N/δ)/(2ε²). The sample size grows only like log N, which is why a finite class of hypotheses can be learned from few examples, and why, for observations in [0, 1], Hoeffding's interval X̄ ± √(log(2/α)/(2n)) holds with confidence 1 − α at every n. In high dimensions the same phenomenon appears geometrically: a Lipschitz function on a high-dimensional sphere is almost constant on most of the sphere.

## Key concepts

| Term | Meaning |
|---|---|
| Markov's inequality | P(X ≥ a) ≤ E[X]/a for X ≥ 0 |
| Chebyshev's inequality | P(∣X − E[X]∣ ≥ t) ≤ Var(X)/t² |
| Moment generating function | E[e^(λX)], whose logarithm controls exponential tails |
| Chernoff bound | e^(−λa)·E[e^(λS)], minimised over λ > 0 |
| Hoeffding's inequality | Gaussian-type tail for sums of independent bounded variables |
| Bounded differences | Changing one input moves the function by at most cᵢ |
| Large deviations | The exponential rate at which P(S ≥ na) decays, given by Cramér's theorem |
| Union bound | P(A₁ ∪ … ∪ A_N) ≤ P(A₁) + … + P(A_N) |

## How it fits

- **Below:** Markov's and Chebyshev's inequalities come from [expectation and variance](../../03-combinatorics-and-graph-theory/03-discrete-probability/expectation-and-variance.md) in 03, and [the probabilistic method](../../03-combinatorics-and-graph-theory/03-discrete-probability/the-probabilistic-method.md) uses these bounds to prove that objects exist; the martingale proof of McDiarmid's inequality uses [martingales](../03-stochastic-processes/martingales.md) only in their simplest form.
- **Above:** [statistical learning theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md) in 14 is built on Hoeffding plus the union bound; [random matrices](../../14-applied-and-computational-mathematics/06-data-and-learning/high-dimensional-geometry-and-random-matrices.md) and [compressed sensing](../../14-applied-and-computational-mathematics/06-data-and-learning/sampling-and-compressed-sensing.md) rest on concentration of measure; [randomized algorithms](../../../cs-first-principles/05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md) use Chernoff bounds to show that they rarely fail.
- **Siblings:** the [central limit theorem](the-central-limit-theorem.md) gives the right constant in the limit but no guarantee at finite n; the [law of large numbers](the-law-of-large-numbers.md) is the qualitative statement these bounds quantify.

## Common misconceptions

- **"The central limit theorem gives the tail probabilities"**: its error bound is of order 1/√n in absolute terms, larger than the tail probabilities themselves far from the mean. Only a concentration or large-deviation bound controls P(S ≥ 600) reliably.
- **"Concentration needs a sum of independent terms"**: McDiarmid's inequality covers any function with bounded differences, and martingale versions allow dependence.
- **"Chebyshev is good enough"**: to guarantee an average within ε of its mean with failure probability 10⁻⁹, Chebyshev with variance 1/4 needs about 2.5 × 10⁸/ε² samples and Hoeffding about 10.7/ε², a factor of more than ten million.

## Go deeper

- Stéphane Boucheron, Gábor Lugosi and Pascal Massart, *Concentration Inequalities: A Nonasymptotic Theory of Independence* (2013): the modern theory in full.
- Roman Vershynin, *High-Dimensional Probability* (2018): concentration as the engine of high-dimensional statistics and data science.
- Noga Alon and Joel Spencer, *The Probabilistic Method* (4th edition, 2016): Chernoff bounds and martingale inequalities in combinatorics.
