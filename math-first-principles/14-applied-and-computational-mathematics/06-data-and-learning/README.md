# Data and Learning

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › Data and Learning
> **Children:** [Statistical Learning Theory](statistical-learning-theory.md) · [High-Dimensional Geometry and Random Matrices](high-dimensional-geometry-and-random-matrices.md) · [Sampling and Compressed Sensing](sampling-and-compressed-sensing.md) · [The Mathematics of Deep Learning](the-mathematics-of-deep-learning.md) · [Optimal Transport](optimal-transport.md)

## What this area is about

This area asks when a finite amount of data determines something that is in principle infinite: a function from a few labelled examples, a signal from a few measurements, a structure from a cloud of points in a thousand dimensions. Without assumptions the answer is never, since infinitely many functions agree on any finite sample. Every positive result therefore has the same shape: restrict the possibilities by a structural assumption, then show that random data pins down the answer within that restriction with high probability.

The structural assumptions differ by child: a hypothesis class of finite Vapnik–Chervonenkis (VC) dimension, a band-limited spectrum, a sparse vector, a neural architecture. Optimal transport supplies the geometry in which distributions themselves are compared. The probabilistic engine is shared. Concentration of measure, the fact that a function of many independent variables that does not depend too much on any one of them is nearly constant, makes empirical averages trustworthy, makes random projections preserve distances, and makes random measurement matrices behave like isometries on sparse vectors. Deep learning is the test case where practice has outrun this theory.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Statistical learning theory](statistical-learning-theory.md) | When finite samples suffice to learn: probably approximately correct (PAC) learning, VC dimension, uniform convergence, bias–variance | Nothing in this area |
| [High-dimensional geometry and random matrices](high-dimensional-geometry-and-random-matrices.md) | How space behaves in many dimensions: concentration, Johnson–Lindenstrauss, the semicircle and Marchenko–Pastur laws | Nothing in this area |
| [Sampling and compressed sensing](sampling-and-compressed-sensing.md) | Recovering signals from few measurements: Nyquist–Shannon, sparsity, ℓ¹ minimisation and the restricted isometry property | High-dimensional geometry |
| [The mathematics of deep learning](the-mathematics-of-deep-learning.md) | What is proved and what is open about neural networks: approximation, backpropagation, landscapes, double descent | Learning theory, high-dimensional geometry |
| [Optimal transport](optimal-transport.md) | Comparing distributions by the cheapest way to move one onto another: Kantorovich duality, Brenier's theorem, Wasserstein distances, Sinkhorn's algorithm | Nothing in this area |

Learning theory and high-dimensional geometry are the two foundations, one combinatorial and one geometric. Compressed sensing applies the geometry: random matrices preserve the lengths of all sparse vectors at once, by the same union-bound argument that proves the Johnson–Lindenstrauss lemma. Deep learning draws on both and strains both. Classical learning bounds predict that networks with more parameters than data points should overfit; they do not, and random matrix theory explains part of why, through the double-descent curve. Optimal transport stands beside them as the geometry of the space of distributions: it measures how far an empirical sample lies from the truth and supplies the Wasserstein losses of generative models.

```
  concentration of measure ─────────────┐
        │                               │
  high-dimensional geometry       statistical learning theory
        │            \                 /
  compressed sensing   the mathematics of deep learning
                                       │
                 optimal transport ────┘  (distances between distributions)
```

## Connections to sibling areas

- **[Numerical analysis](../01-numerical-analysis/README.md):** randomised numerical linear algebra uses random projections to compress large matrices, and Monte Carlo is the simplest learning-from-samples problem.
- **[Optimisation](../02-optimisation/README.md):** learning is empirical risk minimisation, compressed sensing is a linear programme, deep learning runs on stochastic gradient descent, and optimal transport is Kantorovich's infinite linear programme with its dual.
- **[Information, codes and cryptography](../03-information-codes-and-cryptography/README.md):** sampling theory is half of Shannon's theory of communication, and sparse recovery is the real-number cousin of syndrome decoding.
- **[Mathematical modelling](../04-mathematical-modelling/README.md):** models built from mechanisms and models fitted from data are the two ends of one spectrum, and validation is the same problem as generalisation.
- **[Games, decisions and finance](../05-games-decisions-and-finance/README.md):** online learning and adversarial training are repeated games, and finance estimates large covariance matrices where the Marchenko–Pastur law warns of noise.

## Connections across layers

From below, the area rests on the [limit theorems](../../11-probability-and-statistics/02-limit-theorems/README.md) and [statistical inference](../../11-probability-and-statistics/04-statistical-inference/README.md) of layer 11, the [inner-product spaces](../../04-linear-algebra/03-inner-product-spaces/README.md) of layer 4 (spectral theorem and singular value decomposition), [harmonic analysis](../../09-advanced-analysis/04-harmonic-analysis/README.md) for sampling, and [extremal set theory](../../03-combinatorics-and-graph-theory/04-extremal-combinatorics/posets-and-extremal-set-theory.md) for the Sauer–Shelah lemma. Upward, [computers and proof](../../15-mathematics-in-context/computers-and-proof.md) discusses machine learning in mathematical research, and [mathematics and society](../../15-mathematics-in-context/mathematics-and-society.md) discusses fairness in automated decisions. The engineering side is in the computing tree's [machine learning foundations](../../../cs-first-principles/13-artificial-intelligence/02-machine-learning-foundations/README.md) and [deep learning](../../../cs-first-principles/13-artificial-intelligence/03-deep-learning/README.md).

## Cross-cutting threads

- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): concentration of measure drives every guarantee in the area.
- [Infinity and size](../../CROSS-CUTTING.md#infinity-and-size): VC dimension measures the effective size of an infinite class of functions.
- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): universal approximation, and the large-dimension limits of random matrix theory.
- [Duality](../../CROSS-CUTTING.md#duality): ℓ¹ recovery is certified by a dual vector, as linear programmes are.
- [Extremal principles and optimisation](../../CROSS-CUTTING.md#extremal-principles-and-optimisation): learning as risk minimisation, sparse recovery as norm minimisation.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): the no-free-lunch theorem and the aliasing of undersampled signals.
