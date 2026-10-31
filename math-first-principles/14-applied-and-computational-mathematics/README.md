# 14 Applied and Computational Mathematics

> **Layer:** 14 Applied and Computational Mathematics
> **Children:** [Numerical Analysis](01-numerical-analysis/README.md) · [Optimisation](02-optimisation/README.md) · [Information, Codes and Cryptography](03-information-codes-and-cryptography/README.md) · [Mathematical Modelling](04-mathematical-modelling/README.md) · [Games, Decisions and Finance](05-games-decisions-and-finance/README.md) · [Data and Learning](06-data-and-learning/README.md)

## What this area is about

This layer asks how mathematics computes, decides and models the world. The rest of the stack proves that objects exist and have properties: a solution to a differential equation, a minimum of a convex function, a code meeting a bound. Here the questions become operational. How is the solution computed to a given accuracy, and at what cost? Which choice is best, and how can its optimality be certified? How much can be sent, compressed, hidden or learned? Which equations describe a population, a market or a spacetime, and how far can their predictions be trusted?

The layer has two halves. Three areas are **toolkits**, each a theory of a kind of computation: numerical analysis (computing with real numbers in finite precision), optimisation (choosing the best point of a set) and information, codes and cryptography (communicating reliably and securely). Three are **worlds** where the toolkits are applied: mathematical modelling of physical, biological and engineered systems; games, decisions and finance, where the systems contain agents who choose; and data and learning, where the model itself is inferred from samples.

The layer's contribution to the stack is **quantified approximation**: every answer comes with a cost and an error bound, and the best theorems say which trade-offs between them are possible and which are impossible.

## Why this layer sits here

Applied mathematics sits near the top because each of its areas draws on several branches at once. Numerical analysis needs [linear algebra](../04-linear-algebra/README.md), [real analysis](../06-real-analysis/README.md) and the theory of [differential equations](../10-differential-equations-and-dynamics/README.md). Optimisation needs the convexity and separation theorems of [geometry](../08-geometry/README.md). Codes and cryptography need finite fields from [abstract algebra](../05-abstract-algebra/README.md) and the arithmetic of [number theory and algebraic geometry](../12-number-theory-and-algebraic-geometry/README.md). Modelling needs functional analysis and differential geometry, finance needs stochastic calculus from [probability and statistics](../11-probability-and-statistics/README.md), and learning needs concentration of measure and high-dimensional geometry. No earlier layer could hold all of this without anticipating what comes later.

Above it, only [mathematics in context](../15-mathematics-in-context/README.md) remains, which treats computation in proof, open problems and the social uses of mathematics, many of which begin here.

## How the children fit together

```
      numerical analysis ──── optimisation ──── information, codes
      (compute)               (choose)           and cryptography
            \                     |               (communicate)
             \                    |                   /
   ───────────────────── toolkits used by ─────────────────────
             /                    |                   \
   mathematical modelling   games, decisions     data and learning
   (physical and living     and finance          (models inferred
    systems)                (agents who choose)   from samples)
```

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Numerical analysis](01-numerical-analysis/README.md) | Algorithms for continuous problems, with condition numbers, stability and convergence rates; the fast Fourier transform and spectral methods | Linear algebra, analysis, differential equations |
| [Optimisation](02-optimisation/README.md) | Linear and convex programming, duality, and gradient methods with optimal rates | Convex geometry, numerical analysis |
| [Information, codes and cryptography](03-information-codes-and-cryptography/README.md) | Limits of compression and communication, algebraic codes, and public-key and post-quantum cryptography | Probability, finite fields, number theory |
| [Mathematical modelling](04-mathematical-modelling/README.md) | Turning systems into equations: scaling, control, biology, quantum mechanics and relativity | Differential equations, numerical analysis, optimisation |
| [Games, decisions and finance](05-games-decisions-and-finance/README.md) | Strategic choice, collective choice and the pricing of risk | Optimisation, probability, stochastic calculus |
| [Data and learning](06-data-and-learning/README.md) | When finite data determine a model: learning theory, random matrices, compressed sensing, deep learning, optimal transport | Optimisation, probability, information theory |

The toolkits come first and lean on each other: interior-point methods are Newton's method plus numerical linear algebra, gradient descent is explicit Euler on a gradient flow, Reed–Solomon decoding is interpolation over a finite field, and channel capacity is a concave maximisation. The worlds then use all three. A model in physics or biology becomes a prediction only through numerical solution, and becomes a design through optimal control. Game theory's minimax theorem is linear programming duality, and option prices are computed by Monte Carlo simulation. Learning is stochastic optimisation in floating point, judged by bounds that come from information theory and concentration of measure.

## Connections to neighbouring layers

- [04 Linear algebra](../04-linear-algebra/README.md): matrix factorisations, the singular value decomposition and positive definiteness are the inner loop of numerics, optimisation and learning.
- [06 Real analysis](../06-real-analysis/README.md): Taylor expansion, contraction mappings and Lagrange multipliers become error bounds, iterations and optimality conditions.
- [08 Geometry](../08-geometry/README.md): convex sets give duality, polytopes give linear programming, and lattices give codes and post-quantum cryptography.
- [09 Advanced analysis](../09-advanced-analysis/README.md): Fourier analysis gives the fast Fourier transform and sampling theory, and functional analysis gives universal approximation and the operators of quantum mechanics.
- [10 Differential equations and dynamics](../10-differential-equations-and-dynamics/README.md): existence theorems become numerical methods, and stability theory becomes control.
- [11 Probability and statistics](../11-probability-and-statistics/README.md): limit theorems underlie Monte Carlo methods, information theory and learning theory; stochastic calculus underlies finance.
- [12 Number theory and algebraic geometry](../12-number-theory-and-algebraic-geometry/README.md): elliptic curves secure communication, and curves over finite fields give codes beating the Gilbert–Varshamov bound.
- [13 Structure and metamathematics](../13-structure-and-metamathematics/README.md): computability marks what no algorithm can do, the backdrop to every complexity bound here.
- [15 Mathematics in context](../15-mathematics-in-context/README.md): computer-assisted proof, open problems such as P versus NP (whether polynomial time equals nondeterministic polynomial time), and the social role of cryptography and learning.

## Cross-cutting threads

- [Approximation and limits](../CROSS-CUTTING.md#approximation-and-limits): every computed answer is a finite approximation with an error bound.
- [Extremal principles and optimisation](../CROSS-CUTTING.md#extremal-principles-and-optimisation): optimal codes, optimal strategies, optimal controls and minimal losses.
- [Duality](../CROSS-CUTTING.md#duality): linear programming duality, Lagrangian duality and the minimax theorem.
- [Randomness and averaging](../CROSS-CUTTING.md#randomness-and-averaging): Monte Carlo, random codes, stochastic gradients and random measurements.
- [Linearisation](../CROSS-CUTTING.md#linearisation): Newton's method, stability analysis and linear control all study the first-order part.
- [Impossibility and obstruction](../CROSS-CUTTING.md#impossibility-and-obstruction): conditioning limits accuracy, capacity limits communication, and Arrow's theorem limits voting rules.
