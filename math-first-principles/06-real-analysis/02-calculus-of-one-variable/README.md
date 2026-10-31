# Calculus of One Variable

> **Layer:** [06 Real Analysis](../README.md) › Calculus of One Variable
> **Children:** [The derivative and the mean value theorem](the-derivative-and-the-mean-value-theorem.md) · [Taylor expansion](taylor-expansion.md) · [The Riemann integral](the-riemann-integral.md) · [The fundamental theorem of calculus](the-fundamental-theorem-of-calculus.md) · [The exponential and trigonometric functions](the-exponential-and-trigonometric-functions.md)

## What this area is about

Newton and Leibniz built calculus in the seventeenth century as a set of extraordinarily effective rules, justified by infinitesimals nobody could define. This area rebuilds those rules on the limit. The derivative becomes the limit of difference quotients, and the integral becomes the limit of sums of rectangles. Every familiar fact then needs a proof, and the proofs show which hypotheses each fact depends on.

Two tools carry most of the weight. The mean value theorem (MVT) turns information about the derivative at points into information about the function on whole intervals. The fundamental theorem of calculus (FTC) shows that differentiation and integration are inverse operations. Around them sit Taylor's theorem, which extends the linear approximation to polynomials, and the construction of exp, sin, cos and π from power series.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [The derivative and the mean value theorem](the-derivative-and-the-mean-value-theorem.md) | Defines the derivative as the best linear approximation; Rolle and the MVT pass from local to global | Continuity, extreme value theorem |
| [Taylor expansion](taylor-expansion.md) | Best polynomial approximation with remainder bounds; smooth versus analytic | The derivative, series |
| [The Riemann integral](the-riemann-integral.md) | Area as the squeeze of upper and lower sums; which functions are integrable | Continuity, completeness |
| [The fundamental theorem of calculus](the-fundamental-theorem-of-calculus.md) | Links the derivative and the integral, with exact hypotheses | The derivative, the Riemann integral |
| [The exponential and trigonometric functions](the-exponential-and-trigonometric-functions.md) | Defines exp by a power series and derives log, sin, cos, π and Euler's formula | Series, uniform convergence, the derivative |

```
     continuity, series, uniform convergence  (area 01)
             │                         │
     the derivative + MVT       the Riemann integral
        │            │                 │
   Taylor expansion  └──────┬──────────┘
        │                 FTC
        └──────┬────────────┘
     exponential and trigonometric functions
```

Read the derivative first. The MVT is the engine behind Taylor's theorem, which iterates Rolle's theorem, and behind Part 2 of the FTC, which applies the MVT on every piece of a partition. The Riemann integral can be read independently, since it rests only on continuity and completeness. The FTC joins the two strands. The exponential leaf is a capstone: it uses power series, termwise differentiation and the MVT to build the functions that school calculus takes for granted, and it ends at Euler's formula, where real analysis meets ℂ.

The counterexamples are as important as the theorems. x² sin(1/x) has a discontinuous derivative, Volterra's function has a bounded derivative that cannot be Riemann integrated, e^(−1/x²) is smooth but not analytic, and the indicator of ℚ is not Riemann integrable at all. Each one marks a place where a later theory, usually Lebesgue's or complex analysis, does better.

## Connections to sibling areas

- [Limits and convergence](../01-limits-and-convergence/README.md): supplies every tool used here. The extreme value theorem drives Rolle, Heine–Cantor makes continuous functions integrable, and uniform convergence allows power series to be differentiated term by term.
- [Calculus of several variables](../04-calculus-of-several-variables/README.md): the derivative becomes a linear map, Taylor's second-order term becomes the Hessian, and the integral and the FTC grow into multiple integrals and the theorems of Green, Stokes and Gauss.
- [Metric spaces](../03-metric-spaces/README.md): the FTC turns an ordinary differential equation into an integral equation, which the contraction mapping principle then solves.

## Connections across layers

From below, this area uses the completeness of [the real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md) and [the complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md). Above, [the Lebesgue integral](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md) repairs the Riemann integral's failures under limits, and [holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md) explain the radius of convergence of Taylor series. [Existence and uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md) for differential equations starts from the FTC, and [root-finding and Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md) runs on Taylor remainders. In computing, these ideas reappear in [calculus for computer science](../../../cs-first-principles/01-mathematical-foundations/05-continuous-mathematics/calculus.md) and in the rounding error of [floating-point arithmetic](../../../cs-first-principles/03-digital-logic/01-number-representation/floating-point.md).

## Cross-cutting threads

- [Linearisation](../../CROSS-CUTTING.md#linearisation): the derivative replaces a function by its best linear approximation near a point.
- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): Taylor polynomials and Riemann sums approximate, and remainder bounds control the error.
- [Local to global](../../CROSS-CUTTING.md#local-to-global): the MVT turns a sign condition on the derivative at every point into monotonicity on an interval.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): exp and π are constructed from power series rather than assumed.
