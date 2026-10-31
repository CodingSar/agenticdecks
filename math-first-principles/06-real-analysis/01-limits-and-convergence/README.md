# Limits and Convergence

> **Layer:** [06 Real Analysis](../README.md) › Limits and Convergence
> **Children:** [Sequences and limits](sequences-and-limits.md) · [Series](series.md) · [Continuity](continuity.md) · [Uniform convergence](uniform-convergence.md) · [Estimates and inequalities](estimates-and-inequalities.md)

## What this area is about

How can a process that never ends have a definite outcome? The decimal 0.999… equals 1, the sum 1/2 + 1/4 + 1/8 + ⋯ equals 1, and a curve can have an exact slope at a point, yet each involves infinitely many steps. The answer, made precise in the nineteenth century, is the limit. A limit is a claim about finite approximations: the error can be made smaller than any tolerance ε by going far enough. The limiting value itself is guaranteed to exist by the completeness of ℝ.

One idea unifies the children. Each applies the same ε–N definition to a different object: numbers (sequences), partial sums (series), the values of a function near a point (continuity), and whole functions at once (uniform convergence). Every proof in this area is an estimate, and the fifth child collects the inequalities that make the estimates work.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Sequences and limits](sequences-and-limits.md) | Defines the limit; proves monotone convergence, Bolzano–Weierstrass and the Cauchy criterion from completeness | The real numbers (layer 02) |
| [Series](series.md) | Limits of partial sums: convergence tests, absolute convergence, rearrangement, power series | Sequences and limits |
| [Continuity](continuity.md) | Functions that preserve limits: the intermediate value, extreme value and Heine–Cantor theorems | Sequences and limits |
| [Uniform convergence](uniform-convergence.md) | Limits of functions: when continuity, integrals and derivatives survive the limit | Sequences, series, continuity |
| [Estimates and inequalities](estimates-and-inequalities.md) | The toolkit of every proof: triangle, AM–GM, Cauchy–Schwarz, Jensen, Hölder, O and o | Sequences and limits; inner products (layer 04) |

```
               completeness of ℝ  (layer 02)
                          │
                 sequences and limits
                  ┌───────┴────────┐
               series          continuity
                  └───────┬────────┘
                 uniform convergence

    estimates and inequalities: the toolkit used at every step
```

Read [sequences and limits](sequences-and-limits.md) first. It holds the definition and the theorems that turn completeness into usable tools, and every other child cites them. [Series](series.md) and [continuity](continuity.md) are independent applications: one sums a sequence, the other asks a function to respect sequences. [Uniform convergence](uniform-convergence.md) needs both, because its main objects are series of functions and its main question is whether a limit of continuous functions is continuous. [Estimates and inequalities](estimates-and-inequalities.md) is listed last but is best read alongside the others. Its inequalities are the steps of their proofs, and its ε/3 pattern is the shape of the central argument in uniform convergence.

The area also has a recurring lesson: hypotheses matter. Pointwise limits break continuity, conditionally convergent series can be reordered to any sum, and the intermediate value theorem fails over ℚ. Each counterexample marks exactly where completeness, absolute convergence or uniformity enters a proof.

## Connections to sibling areas

- [Calculus of one variable](../02-calculus-of-one-variable/README.md): the derivative is a limit of difference quotients and the integral a limit of sums. The mean value theorem rests on the extreme value theorem from here, integrability rests on Heine–Cantor, and uniform convergence lets power series be differentiated, which is how exp, sin and cos are built.
- [Calculus of several variables](../04-calculus-of-several-variables/README.md): the same ε–δ definitions with the norm ∥·∥ in place of |·|. Cauchy–Schwarz explains why the gradient points in the direction of steepest ascent.
- [Metric spaces](../03-metric-spaces/README.md): keeps only the distance and the triangle inequality, so sequences, continuity and uniform convergence (in the sup metric) become one theory. Bolzano–Weierstrass grows into compactness, and the Cauchy criterion into completeness.

## Connections across layers

From below, this area takes the completeness of [the real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md), the quantifier logic of [predicate logic](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md) (ε–N is a three-quantifier sentence), and inner products from [linear algebra](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md). Above, [the Lebesgue integral](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md) repairs the failure of pointwise limits to commute with integrals. Probability needs several [modes of convergence](../../11-probability-and-statistics/02-limit-theorems/modes-of-convergence.md) and sharpens these inequalities into [concentration inequalities](../../11-probability-and-statistics/02-limit-theorems/concentration-inequalities.md). [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md) and [the Riemann zeta function](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md) are series, and [topology](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md) abstracts continuity away from distance.

## Cross-cutting threads

- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): the exact is defined as the limit of the approximate, and every proof estimates the gap.
- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): the Cauchy criterion and Bolzano–Weierstrass are their first appearances.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): monotone convergence proves that a limit such as Euler's constant γ exists while saying nothing about what it is.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): the counterexamples (rearranged series, discontinuous pointwise limits) show which hypotheses cannot be removed.
