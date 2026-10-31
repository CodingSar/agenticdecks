# Numerical Analysis

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › Numerical Analysis
> **Children:** [Floating Point, Conditioning and Stability](floating-point-conditioning-and-stability.md) · [Numerical Linear Algebra](numerical-linear-algebra.md) · [Root-Finding and Newton's Method](root-finding-and-newtons-method.md) · [Interpolation and Approximation](interpolation-and-approximation.md) · [Numerical Methods for Differential Equations](numerical-methods-for-differential-equations.md) · [Monte Carlo Methods](monte-carlo-methods.md)

## What this area is about

Lloyd Trefethen defined numerical analysis as the study of algorithms for the problems of continuous mathematics. Its problems are the ones the rest of mathematics poses (solve this system, find this root, integrate this equation, compute this expectation), but its answers must come in finitely many operations on finitely many digits. Two errors therefore haunt every computation: truncation error, from replacing an infinite process by a finite one, and rounding error, from replacing real numbers by floating-point numbers. The area's achievement is a vocabulary for controlling both: the order of convergence measures truncation, the condition number measures what the problem itself forces, and stability measures what the algorithm adds. A good numerical method is one whose answer is provably close to the truth, and whose cost is known in advance.

## How the children fit together

```
            floating point, conditioning, stability
             (what any computed answer can mean)
                 /          |             \
   numerical linear     root-finding     interpolation and
       algebra          (Newton)          approximation
                \          |             /
           numerical methods for differential equations
                           |
                 Monte Carlo methods  (random, not grid-based)
```

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Floating point, conditioning and stability](floating-point-conditioning-and-stability.md) | The language of error: unit roundoff, condition numbers, backward stability | Real analysis, singular values |
| [Numerical linear algebra](numerical-linear-algebra.md) | Factorisations and iterations for Ax = b, least squares and eigenvalues; the inner loop of almost everything else | Floating point |
| [Root-finding and Newton's method](root-finding-and-newtons-method.md) | Iterations for nonlinear equations; quadratic convergence and its failures | Floating point, contraction mapping |
| [Interpolation and approximation](interpolation-and-approximation.md) | Replacing functions by polynomials and splines; where to put the nodes | Floating point, Taylor and Fourier series |
| [Numerical methods for differential equations](numerical-methods-for-differential-equations.md) | Time-stepping, stability regions, the Courant–Friedrichs–Lewy (CFL) condition, finite elements | All four above |
| [Monte Carlo methods](monte-carlo-methods.md) | Averaging random samples; dimension-free N^(−1/2) error; Markov chain sampling | Probability, Markov chains |

The first leaf supplies the questions every other leaf answers. The middle three are the basic tools, and they call one another: Newton's method in n dimensions is a sequence of linear solves, eigenvalue problems are solved by iteration, and the secant method is linear interpolation. Differential equations combine all of them: an implicit step is a Newton iteration whose linear systems come from a discretisation built from interpolants. Monte Carlo methods stand slightly apart: they give up the deterministic error bounds of the others in exchange for an error rate that does not depend on dimension, which is what makes integrals over hundreds of variables computable at all. A recurring theme is that the best algorithms are short: Jack Dongarra and Francis Sullivan's list of the ten most influential algorithms of the twentieth century (2000) includes the Metropolis algorithm, the simplex method, Krylov subspace iteration, the QR algorithm and the fast Fourier transform.

## Connections to sibling areas

- [Optimisation](../02-optimisation/README.md): Newton's method on ∇f = 0 drives interior-point methods, and gradient descent with a fixed step is explicit Euler on the gradient flow, with the same stability limit.
- [Information, codes and cryptography](../03-information-codes-and-cryptography/README.md): Reed–Solomon decoding is polynomial interpolation over a finite field.
- [Mathematical modelling](../04-mathematical-modelling/README.md): models become predictions only through numerical solution of their equations.
- [Games, decisions and finance](../05-games-decisions-and-finance/README.md): option prices are computed by finite differences and Monte Carlo simulation.
- [Data and learning](../06-data-and-learning/README.md): random sketching speeds up numerical linear algebra, and training a network is large-scale stochastic optimisation in floating point.

## Connections across layers

The area turns theorems from lower layers into algorithms: the [contraction mapping principle](../../06-real-analysis/04-metric-spaces/completeness-and-the-contraction-mapping-principle.md) into fixed-point iteration, [the spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md) into the QR algorithm, [weak solutions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md) into finite elements and the [law of large numbers](../../11-probability-and-statistics/02-limit-theorems/the-law-of-large-numbers.md) into Monte Carlo integration. In return, interval arithmetic makes floating point a tool of rigorous proof (see [computers and proof](../../15-mathematics-in-context/computers-and-proof.md)).

## Cross-cutting threads

- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): every leaf replaces a limit by a finite computation and bounds the difference.
- [Linearisation](../../CROSS-CUTTING.md#linearisation): Newton's method, condition numbers and stability analysis all study the first-order part.
- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): Monte Carlo trades certainty for dimension-free rates.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): no finite formula for eigenvalues, no A-stable explicit method, no algorithm more accurate than the conditioning allows.
