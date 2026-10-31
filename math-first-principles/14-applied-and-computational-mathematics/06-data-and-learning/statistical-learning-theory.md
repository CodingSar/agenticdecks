# Statistical Learning Theory

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Data and Learning](README.md)
> **Builds on:** [Concentration Inequalities](../../11-probability-and-statistics/02-limit-theorems/concentration-inequalities.md), [The Law of Large Numbers](../../11-probability-and-statistics/02-limit-theorems/the-law-of-large-numbers.md), [Posets and Extremal Set Theory](../../03-combinatorics-and-graph-theory/04-extremal-combinatorics/posets-and-extremal-set-theory.md), [Linear Models and Regression](../../11-probability-and-statistics/04-statistical-inference/linear-models-and-regression.md)
> **Enables:** [The Mathematics of Deep Learning](the-mathematics-of-deep-learning.md), [Generalization and Bias–Variance (CS)](../../../cs-first-principles/13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md), [Supervised Learning (CS)](../../../cs-first-principles/13-artificial-intelligence/02-machine-learning-foundations/supervised-learning.md)

## Essence

Statistical learning theory asks when a rule fitted to finitely many examples will work on new ones. Data are drawn independently from an unknown distribution, a learner picks a hypothesis from a class H, and success means low error on fresh draws, not on the sample. Leslie Valiant's model of probably approximately correct (PAC) learning (1984) makes this precise. The central result says a class of yes–no classifiers is learnable if and only if its Vapnik–Chervonenkis (VC) dimension is finite: a combinatorial measure of how many patterns the class can fit. The single idea underneath is uniform convergence: if the class is not too rich, empirical error is close to true error for every hypothesis at once, so minimising the first nearly minimises the second.

## Core tenets

1. **Learning means small true risk with high confidence.** Examples (x, y) come independently from a distribution D. A hypothesis h has true risk R(h) = P(h(x) ≠ y) and empirical risk R̂(h), its error rate on the sample. Empirical risk minimisation (ERM) picks h in H with least R̂. A class is PAC learnable if for every ε, δ > 0 there is a sample size m(ε, δ), independent of D, beyond which some learner's output has R(h) ≤ ε + min over H with probability at least 1 − δ.

2. **Finite classes are learnable with sample size logarithmic in their size.** Suppose some h in H is perfect. A fixed h with R(h) > ε fits m independent examples with probability at most (1 − ε)^m ≤ e^(−εm). A union bound over H shows that every such h is rejected with probability at least 1 − δ once m ≥ (1/ε)(ln∣H∣ + ln(1/δ)). Without a perfect h, Hoeffding's inequality and the same union bound give m of order (ln∣H∣ + ln(1/δ))/ε².

3. **VC dimension measures richness by shattering.** A set of points is shattered by H if every one of its 2ⁿ labellings is realised by some h. The VC dimension is the size of the largest shattered set. Thresholds on the line have dimension 1, intervals 2, half-planes 3, and half-spaces in ℝ^d have d + 1. Dimension is not parameter count: the one-parameter class x ↦ sign(sin(θx)) shatters arbitrarily large sets.

4. **The Sauer–Shelah lemma turns finite dimension into polynomial growth.** Let Π_H(m) be the largest number of distinct labellings H induces on m points. If the VC dimension is d, then Π_H(m) ≤ ∑ᵢ₌₀ᵈ C(m, i) ≤ (em/d)^d for m ≥ d. So beyond d points the class realises a vanishing fraction of the 2^m possible labellings. The proof is an induction on m that removes one point and splits the class.

5. **The fundamental theorem: for binary classification, finite VC dimension, uniform convergence, learnability by ERM and PAC learnability are equivalent.** Proof idea: symmetrisation compares the sample with an independent "ghost" sample, so only the labellings of 2m points matter; there are at most Π_H(2m) of them, and Hoeffding plus a union bound gives uniform convergence once m is of order (d + ln(1/δ))/ε². Conversely, if H shatters arbitrarily large sets, an adversarial distribution on a shattered set defeats every learner. In the realisable case, sample size of order d/ε suffices, up to a logarithmic factor. Vladimir Vapnik and Alexey Chervonenkis developed the theory around 1971.

6. **Error splits into approximation and estimation, and a richer class trades one for the other.** The excess risk of the learned ĥ over the best possible predictor is the approximation error (how far the best h in H is from the best predictor) plus the estimation error (how far ĥ is from the best h in H). Enlarging H shrinks the first and inflates the second. For squared loss the analogous split is expected error = noise + bias² + variance. Structural risk minimisation chooses the class size by penalising complexity.

7. **No free lunch: no learner works for every distribution.** Given any learning algorithm and a sample of fewer than half the points of a domain, some distribution with a perfect target makes the algorithm err with probability at least 1⁄8 on a constant fraction of samples. Hence the class of all functions on an infinite domain is not learnable. Every successful learner carries an inductive bias, a restriction or preference that the data cannot supply.

## Key concepts

| Term | Meaning |
|---|---|
| True risk R(h) | Probability that h errs on a fresh example from D |
| Empirical risk R̂(h) | The fraction of the sample on which h errs |
| PAC learnable | Error ε with confidence 1 − δ from a sample size independent of D |
| Shattering | Realising all 2ⁿ labellings of a set of n points |
| VC dimension | Size of the largest set the class shatters |
| Growth function Π_H(m) | Largest number of labellings the class induces on m points |
| Uniform convergence | Empirical risk close to true risk for all h in H simultaneously |
| Inductive bias | The assumptions a learner brings beyond the data |

## How it fits

- **Below:** the law of large numbers says one hypothesis's empirical risk converges; concentration inequalities give the rate; the Sauer–Shelah lemma comes from extremal set theory; linear regression is the classical case of fitting with a bias–variance trade-off.
- **Above:** [computers and proof](../../15-mathematics-in-context/computers-and-proof.md) discusses learning systems in mathematics; the computing tree's [generalisation](../../../cs-first-principles/13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md) leaf gives the practitioner's view.
- **Siblings:** [high-dimensional geometry](high-dimensional-geometry-and-random-matrices.md) supplies the concentration tools in sharper form; [deep learning](the-mathematics-of-deep-learning.md) is where these bounds become vacuous and new explanations are needed.

## Common misconceptions

- **"More parameters always means more overfitting."** Capacity is measured by VC dimension or similar quantities, not parameter count, and trained networks show the two can diverge sharply.
- **"Low training error shows a model has learned."** Only uniform convergence, or a held-out test, links training error to error on new data.
- **"A clever enough algorithm can learn anything."** The no-free-lunch theorem rules out a universal learner; assumptions are unavoidable.

## Go deeper

- S. Shalev-Shwartz and S. Ben-David, *Understanding Machine Learning: From Theory to Algorithms* (2014): the clearest modern account, with full proofs.
- V. N. Vapnik, *The Nature of Statistical Learning Theory* (1995): the theory from one of its founders.
- M. J. Kearns and U. V. Vazirani, *An Introduction to Computational Learning Theory* (1994): PAC learning with attention to computation.
