# Analytic Number Theory

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › Analytic Number Theory
> **Children:** [The Riemann zeta function](the-riemann-zeta-function.md) · [The prime number theorem](the-prime-number-theorem.md) · [Primes in arithmetic progressions](primes-in-arithmetic-progressions.md) · [Sieves and additive problems](sieves-and-additive-problems.md)

## What this area is about

Euclid proved that there are infinitely many primes; analytic number theory asks how many, how they are spread out, and in which patterns they occur. The method is to encode arithmetic in functions and study those functions with analysis. Euler's product turns unique factorisation into an identity for the zeta function ζ(s); Riemann's continuation of ζ to the complex plane turns the distribution of primes into the location of its zeros; Dirichlet's characters, Fourier analysis on the group (ℤ/q)^×, separate primes by residue class. Where these tools fail, sieves count by inclusion–exclusion and the circle method counts sums of primes by integrating exponential sums.

The unifying idea is that *primes are counted through generating functions*, whose poles give main terms and whose zeros give errors. The results are asymptotic and quantitative, and the open problems are the sharpest forms: the Riemann Hypothesis, the twin prime conjecture and binary Goldbach, all open as of 2026.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [The Riemann zeta function](the-riemann-zeta-function.md) | Euler product, continuation, functional equation, zeros, explicit formula, the Riemann Hypothesis | 09 complex analysis, 02 primes |
| [The prime number theorem](the-prime-number-theorem.md) | π(x) ∼ x/log x from the absence of zeros on Re s = 1; error terms | zeta |
| [Primes in arithmetic progressions](primes-in-arithmetic-progressions.md) | characters, L-functions, L(1, χ) ≠ 0, the class number formula, Siegel zeros | zeta |
| [Sieves and additive problems](sieves-and-additive-problems.md) | Brun and Selberg sieves, parity, the circle method, bounded gaps, Goldbach | PNT, progressions |

The zeta function comes first; it is both the main tool and the model for every later L-function. The prime number theorem (PNT) and Dirichlet's theorem are its two classical applications and can be read in either order. Sieves come last because their inputs, densities and equidistribution in progressions such as the Bombieri–Vinogradov theorem, come from the other three.

```
 Euler product ζ(s) = ∏ (1 − p^(−s))^(−1)
        │ continuation, functional equation
        ▼
 zeros of ζ ──► explicit formula ──► PNT, error terms (RH)
        │
        └─ twist by characters χ ──► L(s, χ) ──► primes in progressions
                                                   │
                       inclusion–exclusion ────────┤
                       exponential sums ───────────┴──► sieves, circle method
```

## Connections to sibling areas

- **[Algebraic Number Theory](../01-algebraic-number-theory/README.md)** meets this area in the class number formula, which expresses L(1, χ) through a class number, and in Chebotarev's density theorem, which needs L-functions of number fields.
- **[Algebraic Geometry](../03-algebraic-geometry/README.md)** gives zeta functions of curves over finite fields, for which the Riemann Hypothesis is proved, by Weil for curves and by Deligne for all varieties.
- **[Elliptic Curves and Modular Forms](../04-elliptic-curves-and-modular-forms/README.md)** produces L-functions of degree 2 whose analytic continuation comes from modularity, and whose behaviour at s = 1 is the subject of the Birch and Swinnerton-Dyer conjecture.

## Connections across layers

- **Below:** [analytic continuation](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md), [residues](../../09-advanced-analysis/02-complex-analysis/singularities-and-residues.md) and [Fourier analysis on groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md) are the analytic tools; [inclusion–exclusion](../../03-combinatorics-and-graph-theory/01-enumeration/inclusion-exclusion-and-the-pigeonhole-principle.md) is the raw sieve; [primes and unique factorisation](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md) is what the Euler product encodes.
- **Above:** prime density sizes key generation in [cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md); zeros of ζ behave like [random matrix eigenvalues](../../14-applied-and-computational-mathematics/06-data-and-learning/high-dimensional-geometry-and-random-matrices.md); the Riemann Hypothesis and twin primes head the [open problems](../../15-mathematics-in-context/open-problems.md).

## Cross-cutting threads

- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): asymptotic counts with explicit error terms.
- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): Cramér's model and equidistribution in residue classes.
- [Duality](../../CROSS-CUTTING.md#duality): the functional equation s ↔ 1 − s and character orthogonality.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): primes are read off the poles and zeros of complex functions.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): the parity problem limits what sieves can prove.
