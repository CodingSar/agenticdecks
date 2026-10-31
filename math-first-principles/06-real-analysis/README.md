# 06 Real Analysis

> **Layer:** 06 Real Analysis
> **Children:** [Limits and Convergence](01-limits-and-convergence/README.md) · [Calculus of One Variable](02-calculus-of-one-variable/README.md) · [Metric Spaces](03-metric-spaces/README.md) · [Calculus of Several Variables](04-calculus-of-several-variables/README.md)

## What this area is about

Calculus was invented in the seventeenth century and used with spectacular success for nearly two hundred years before anyone could say exactly what a derivative or an integral was. Real analysis is the rigorous version. It replaces infinitesimals by limits, defined with ε and δ, and then proves the theorems that calculus took for granted: that continuous functions on closed intervals have maxima, that a function with zero derivative is constant, that integration undoes differentiation, and that power series can be differentiated term by term.

Rigour pays for itself here in two ways. First, it locates exactly where each hypothesis is needed, through counterexamples: a pointwise limit of continuous functions that jumps, a continuous function differentiable nowhere, a series that can be rearranged to any sum, a field that is curl-free but not a gradient. Second, the definitions turn out to work far beyond the real line. The same arguments apply in ℝⁿ, in spaces of functions and in abstract metric spaces, and that generality is what the higher layers of analysis, topology, geometry and differential equations build on.

## Why this layer sits here

**What it needs from below.** Everything rests on the completeness of [the real numbers](../02-number-systems/01-constructing-the-numbers/the-real-numbers.md), built in layer 02: every bounded set of reals has a least upper bound. This layer uses that property and does not rebuild it. The ε–δ definitions are sentences with alternating quantifiers, so the habits of [predicate logic](../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md) from layer 00 are needed to read and negate them. [Functions and sets](../01-sets-and-foundations/01-sets-relations-and-functions/functions.md) from layer 01 supply the language of images, preimages and unions. Several-variable calculus needs [linear maps and matrices](../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md), [determinants](../04-linear-algebra/02-determinants-and-eigenvalues/determinants.md) and [inner products](../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md) from layer 04, because the derivative of a map between spaces of several dimensions is a linear map.

**What the layers above need from it.** [07 Topology](../07-topology/README.md) abstracts metric continuity and compactness into open sets. [08 Geometry](../08-geometry/README.md) uses the inverse and implicit function theorems to build manifolds and generalises the integral theorems to differential forms. [09 Advanced Analysis](../09-advanced-analysis/README.md) repairs the Riemann integral with the Lebesgue integral, extends calculus to ℂ, and studies complete spaces of functions. [10 Differential Equations and Dynamics](../10-differential-equations-and-dynamics/README.md) proves existence of solutions with the contraction mapping principle and compactness. [11 Probability and Statistics](../11-probability-and-statistics/README.md) needs limits, series, inequalities and integrals throughout, and [14 Applied and Computational Mathematics](../14-applied-and-computational-mathematics/README.md) bounds the error of every numerical method with Taylor remainders and fixed-point estimates.

The one idea this layer contributes is **the limit, made rigorous by completeness**: an object is defined as the limit of approximations, its existence is guaranteed by completeness or compactness, and every proof is an estimate of how fast the approximations close in.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Limits and Convergence](01-limits-and-convergence/README.md) | Sequences, series, continuity, uniform convergence and the inequalities that drive all estimates | Completeness of ℝ (layer 02) |
| [Calculus of One Variable](02-calculus-of-one-variable/README.md) | The derivative, the mean value theorem, Taylor expansion, power series, the Riemann integral, the fundamental theorem, exp and π | Limits and Convergence |
| [Metric Spaces](03-metric-spaces/README.md) | Distance in general; completeness and the contraction principle; compactness and Arzelà–Ascoli | Limits and Convergence |
| [Calculus of Several Variables](04-calculus-of-several-variables/README.md) | The derivative as a linear map, inverse and implicit functions, extrema, multiple integrals, the integral theorems | One variable, Metric Spaces, linear algebra (layer 04) |

```
             completeness of ℝ  (layer 02)
                         │
               01 Limits and Convergence
                ┌────────┴────────┐
   02 Calculus of One Variable   03 Metric Spaces
                └────────┬────────┘
            04 Calculus of Several Variables
```

Begin with [Limits and Convergence](01-limits-and-convergence/README.md), which turns completeness into usable tools. [Calculus of One Variable](02-calculus-of-one-variable/README.md) and [Metric Spaces](03-metric-spaces/README.md) can then be read in either order: one applies limits to derivatives and integrals on the line, the other strips the line down to a distance and proves completeness and compactness theorems in general. [Calculus of Several Variables](04-calculus-of-several-variables/README.md) comes last because it needs both: the inverse function theorem is proved with the contraction mapping principle from Metric Spaces, and the existence of extrema uses compactness. The dependence runs only from 03 to 04, never back.

## Connections to neighbouring layers

- [02 Number Systems](../02-number-systems/README.md): supplies ℝ with its completeness, and ℂ, where exp(ix) = cos x + i sin x lives.
- [04 Linear Algebra](../04-linear-algebra/README.md): derivatives are linear maps, volumes scale by determinants, and the Hessian is a quadratic form.
- [07 Topology](../07-topology/README.md): keeps the open sets and drops the distance; compactness and continuity become topological notions.
- [08 Geometry](../08-geometry/README.md): manifolds come from the implicit function theorem, and Green, Stokes and Gauss become one theorem about differential forms.
- [09 Advanced Analysis](../09-advanced-analysis/README.md): the Lebesgue integral, complex analysis, Banach and Hilbert spaces, and Fourier series continue directly from here.
- [10 Differential Equations and Dynamics](../10-differential-equations-and-dynamics/README.md): existence and uniqueness of solutions comes from the contraction principle, and the heat and Laplace equations come from the divergence theorem.
- [11 Probability and Statistics](../11-probability-and-statistics/README.md): modes of convergence and concentration inequalities sharpen the limits and estimates of this layer.
- [14 Applied and Computational Mathematics](../14-applied-and-computational-mathematics/README.md): numerical analysis and optimisation are real analysis with error bounds made explicit.

## Connections across layers

The same ideas run through the sibling trees. In computer science, [asymptotic analysis](../../cs-first-principles/02-theory-of-computation/04-complexity/asymptotic-analysis.md) is O notation applied to running times, [backpropagation](../../cs-first-principles/13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md) is the chain rule, and [learning as optimisation](../../cs-first-principles/13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md) is gradient descent. In medicine, [drug elimination and half-life](../../medicine-first-principles/09-pharmacology-and-therapeutics/01-pharmacokinetics/elimination-half-life-and-dosing.md) follow the exponential function, and [diffusion](../../medicine-first-principles/00-physical-and-chemical-foundations/01-physics-of-the-body/diffusion-osmosis-and-transport.md) is governed by the divergence theorem.

## Cross-cutting threads

- [Approximation and limits](../CROSS-CUTTING.md#approximation-and-limits): every object in this layer is a limit of approximations, and every proof bounds the error.
- [Completeness and compactness](../CROSS-CUTTING.md#completeness-and-compactness): the two properties that make limits exist, from ℝ to metric spaces and spaces of functions.
- [Linearisation](../CROSS-CUTTING.md#linearisation): the derivative replaces a map by its best linear approximation, and the inverse function theorem says when that suffices.
- [Existence and construction](../CROSS-CUTTING.md#existence-and-construction): contractions construct solutions by iteration; compactness proves they exist without a construction.
- [Extremal principles and optimisation](../CROSS-CUTTING.md#extremal-principles-and-optimisation): the extreme value theorem, critical points and Lagrange multipliers.
- [Abstraction and generalisation](../CROSS-CUTTING.md#abstraction-and-generalisation): metric spaces keep only what the proofs about ℝ actually used.
- [Local to global](../CROSS-CUTTING.md#local-to-global): the mean value theorem and compactness turn pointwise information into statements about whole intervals and spaces.
