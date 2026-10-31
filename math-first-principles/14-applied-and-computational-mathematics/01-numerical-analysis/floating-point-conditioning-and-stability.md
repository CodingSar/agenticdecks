# Floating Point, Conditioning and Stability

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Numerical Analysis](README.md)
> **Builds on:** [The Real Numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md), [Estimates and Inequalities](../../06-real-analysis/01-limits-and-convergence/estimates-and-inequalities.md), [Taylor Expansion](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md), [Singular Value Decomposition](../../04-linear-algebra/03-inner-product-spaces/singular-value-decomposition.md)
> **Enables:** [Numerical Linear Algebra](numerical-linear-algebra.md), [Root-Finding and Newton's Method](root-finding-and-newtons-method.md), [Numerical Methods for Differential Equations](numerical-methods-for-differential-equations.md), [Computers and Proof](../../15-mathematics-in-context/computers-and-proof.md), [Floating Point (CS)](../../../cs-first-principles/03-digital-logic/01-number-representation/floating-point.md)

## Essence

A computer cannot hold a real number. It holds the nearest member of a finite set of binary fractions, and it rounds the exact result of every operation back into that set. Numerical analysis makes this a theory with two separate questions. *Conditioning* asks how sensitive the problem itself is to small changes in its data, a property of the mathematics, not the machine. *Stability* asks whether an algorithm's rounding errors stay within what the conditioning already forces. The idea that makes it work is backward error analysis: show that the computed answer is the exact answer to a slightly changed problem, and the condition number then bounds its distance from the true one.

## Core tenets

1. **Floating-point numbers have constant relative, not absolute, spacing.** A double in the Institute of Electrical and Electronics Engineers (IEEE) 754 standard (1985, revised 2008 and 2019) is ±(1.f)₂ × 2ᵉ, with 52 fraction bits f and exponent e from −1022 to 1023, plus zeros, subnormal numbers, infinities and Not a Number (NaN) values. Between 1 and 2 the spacing is the machine epsilon ε = 2⁻⁵² ≈ 2.2 × 10⁻¹⁶, and between 2ᵉ and 2^(e+1) it is 2ᵉε. So every real number in range lies within relative distance u = ε/2 = 2⁻⁵³ ≈ 1.1 × 10⁻¹⁶ (the unit roundoff) of a double: about 16 significant digits at every scale from 10⁻³⁰⁸ to 10³⁰⁸.

2. **Each operation is exact, then rounded: fl(x ∘ y) = (x ∘ y)(1 + δ) with ∣δ∣ ≤ u.** The standard requires +, −, ×, ÷ and √ to be correctly rounded, which gives the "standard model" behind every error analysis. It describes one operation; the laws of ℝ do not survive. Addition is not associative: (1 + u) + u rounds to 1 twice, while 1 + (u + u) = 1 + 2u exactly, so a compiler that reorders a sum changes its answer.

3. **The condition number measures the problem, not the algorithm.** For a function f, the relative condition number κ = ∣x f′(x)/f(x)∣ is the factor by which a small relative change in x is amplified in f(x), because f(x + h) − f(x) ≈ f′(x)h. Subtraction a − b has κ = (∣a∣ + ∣b∣)/∣a − b∣, unbounded as a approaches b: catastrophic cancellation, which no algorithm can repair once a and b carry errors. For a linear system Ax = b, κ(A) = ‖A‖ ‖A⁻¹‖, which in the Euclidean norm is σ_max/σ_min, the ratio of the extreme singular values; the 10 × 10 Hilbert matrix, with entries 1/(i + j − 1), has κ ≈ 1.6 × 10¹³.

4. **A backward-stable algorithm gives the exact answer to a nearby problem.** James Wilkinson's idea, developed around 1960 while analysing Gaussian elimination, was to stop chasing the forward error and ask instead: for which perturbed data is the computed result exact? An algorithm is backward stable if that perturbation always has relative size of order u. Backward error is often easy to bound, because each factor (1 + δ) can be pushed back onto an input.

5. **Forward error is at most about condition number times backward error.** This rule, the definition of κ applied to first order, assigns blame. A backward-stable algorithm on a problem with κ = 10¹⁰ loses about 10 of its 16 digits, and loses them honestly: data known to 16 digits does not determine more. A large error on a well-conditioned problem convicts the algorithm.

6. **Unstable algorithms amplify errors that the problem never required.** Summing the Taylor series 1 − 20 + 20²/2! − … for e⁻²⁰ term by term in double precision gives about 6.1 × 10⁻⁹, three times the true 2.06 × 10⁻⁹. The terms alternate in sign and reach 20²⁰/20! ≈ 4.3 × 10⁷, so rounding errors near u × 4.3 × 10⁷ ≈ 5 × 10⁻⁹ swamp the answer, although the problem is well conditioned (κ = 20). The same series summed for e²⁰, whose terms are all positive, gives 1/e²⁰ correct to 15 digits. Rewriting the formula, not adding digits, is the cure.

7. **The order of operations is part of the algorithm.** Adding n numbers from left to right has error bound about (n − 1)u ∑∣xᵢ∣; adding them in pairs, as a binary tree, gives about u log₂ n ∑∣xᵢ∣; William Kahan's compensated summation carries each lost low-order part into the next addition and gives about 2u ∑∣xᵢ∣, independent of n.

## Key concepts

| Term | Meaning |
|---|---|
| Machine epsilon ε | Gap between 1 and the next double: 2⁻⁵² |
| Unit roundoff u | Largest relative error of rounding to nearest: ε/2 = 2⁻⁵³ |
| Condition number κ | Limit of the worst ratio of relative output change to relative input change, as the change tends to 0 |
| Forward error | Distance between the computed answer and the true answer |
| Backward error | Size of the smallest change in the data for which the computed answer is exact |
| Backward stable | Backward error of order u for every input |
| Catastrophic cancellation | Loss of relative accuracy when subtracting nearly equal numbers that carry errors |

## How it fits

- **Below:** floating point imitates [the real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md) but loses their field axioms; [Taylor expansion](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md) gives the first-order analysis behind κ; the [singular value decomposition](../../04-linear-algebra/03-inner-product-spaces/singular-value-decomposition.md) gives κ(A).
- **Above:** every numerical method is judged in this vocabulary. Interval arithmetic, which rounds lower bounds down and upper bounds up, makes floating point a tool of proof: Warwick Tucker's 2002 proof that the Lorenz equations have a strange attractor (Smale's 14th problem) rests on it (see [computers and proof](../../15-mathematics-in-context/computers-and-proof.md)).
- **Siblings:** [numerical linear algebra](numerical-linear-algebra.md) applies backward error analysis to factorisations; [root-finding](root-finding-and-newtons-method.md) meets ill conditioning at multiple roots; for [differential equations](numerical-methods-for-differential-equations.md) "stability" means bounded error growth over many steps, a related but different idea; [Monte Carlo methods](monte-carlo-methods.md) have statistical, not rounding, error.

## Common misconceptions

- **"Double precision means every answer has 16 correct digits"**: only each single operation does. A backward-stable answer has about 16 − log₁₀ κ correct digits, and an unstable algorithm can have none.
- **"0.1 is stored exactly"**: 0.1 is 0.000110011… in binary, so it is stored as the nearest double, 0.1000000000000000055511…; hence 0.1 + 0.2 ≠ 0.3 in floating point.
- **"A small residual means an accurate solution"**: a small residual ‖b − Ax̂‖ for a computed solution x̂ certifies only a small backward error; the forward error can be κ(A) times larger.

## Go deeper

- Nicholas J. Higham, *Accuracy and Stability of Numerical Algorithms* (2nd edition, 2002): the reference for rounding-error analysis.
- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra* (1997): the clearest account of conditioning and backward stability.
- David Goldberg, "What Every Computer Scientist Should Know About Floating-Point Arithmetic", *ACM Computing Surveys* (1991): the standard, worked through.
