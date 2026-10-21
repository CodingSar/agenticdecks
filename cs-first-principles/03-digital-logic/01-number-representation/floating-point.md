# Floating Point

> **Layer:** [03 Digital Logic](../README.md) › [Number Representation](README.md)
> **Builds on:** [Binary and Positional Notation](binary-and-positional-notation.md), [Integers and Two's Complement](integers-and-twos-complement.md), [Calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md)
> **Enables:** [SIMD and GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md), [Optimization](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md), [Training at Scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md), [Geometry and Transformations](../../14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md)

## Essence

Floating point represents real numbers in a fixed number of bits as a sign, a significand and an exponent, the binary form of scientific notation. It trades exactness for range: a 64-bit double covers magnitudes from about 10⁻³⁰⁸ to 10³⁰⁸ with roughly 16 significant decimal digits everywhere in between. Because only finitely many values exist, almost every real number and almost every arithmetic result must be rounded. The Institute of Electrical and Electronics Engineers (IEEE) 754 standard makes this rounding precise and portable: each basic operation returns the exactly computed result rounded to the nearest representable value. The consequences, such as non-associative addition, cancellation and special values like infinity and NaN (Not a Number), follow from that single rule.

## Core tenets

1. **A float is sign × significand × 2^exponent.** IEEE 754 double precision (binary64) uses 1 sign bit, 11 exponent bits (stored with a bias of 1023) and 52 fraction bits. For normal numbers the significand is `1.f`, with the leading 1 implicit ("hidden bit"), giving 53 bits of precision. Single precision (binary32) uses 1, 8 and 23 bits.

2. **Relative precision is constant; absolute spacing is not.** Between consecutive powers of two there are the same number of representable values (2⁵² for doubles), so spacing doubles with each power of two. Machine epsilon, the gap between 1 and the next double, is 2⁻⁵² ≈ 2.2 × 10⁻¹⁶. Near 10¹⁶, consecutive doubles are 2 apart, so adding 1 to 10¹⁶ may do nothing. Above 2⁵³, not every integer is representable.

3. **Every operation is correctly rounded, which makes error analysable.** IEEE 754 requires that `+`, `-`, `×`, `÷` and square root return the infinitely precise result rounded according to the current mode (default: round to nearest, ties to even). So each operation has relative error at most half an ulp (unit in the last place), about 1.1 × 10⁻¹⁶ for doubles. This guarantee is what makes numerical analysis, the study of how such errors propagate, possible and makes results reproducible across conforming hardware.

4. **Algebraic laws fail because each step rounds.** Addition is commutative but not associative: `(1e20 - 1e20) + 1` gives 1, but `1e20 + (-1e20 + 1)` gives 0, because `-1e20 + 1` rounds back to `-1e20`. Likewise `(0.1 + 0.2) + 0.3` is 0.6000000000000001 while `0.1 + (0.2 + 0.3)` is 0.6. Compilers therefore may not reorder floating-point arithmetic freely, and parallel reductions that sum in different orders give slightly different answers.

5. **Most decimal fractions are not representable.** 0.1 has an infinite binary expansion, so it is stored as the nearest double, slightly above 0.1. Hence `0.1 + 0.2 == 0.3` is false. Money and other quantities that must be exact in decimal belong in integers (cents) or decimal floating point, not binary floats.

6. **Subtracting nearly equal numbers destroys relative accuracy.** If `a` and `b` agree in their first 12 digits, `a - b` is computed exactly but retains only the few digits in which they differ, and any earlier rounding error in `a` or `b` now dominates. This catastrophic cancellation is the most common source of numerical disasters, and is avoided by algebraic rearrangement (for example, a stable form of the quadratic formula) or compensated summation (Kahan summation).

7. **Special values make arithmetic total.** Overflow gives ±infinity rather than a crash; `0/0` and `∞ - ∞` give NaN, which propagates through later operations and compares unequal to everything, including itself. Subnormal numbers fill the gap near zero so that `x - y == 0` only when `x == y` (gradual underflow), at the cost of slower handling on some hardware. Signed zero preserves the sign of results that underflowed.

8. **Precision is a resource, traded for speed and energy.** Arithmetic and memory costs grow with width, so machine learning uses 16-bit formats: binary16 (5-bit exponent, 10-bit fraction) and bfloat16 (8-bit exponent like binary32, 7-bit fraction, keeping range at the expense of precision), and increasingly 8-bit formats. Training tolerates this because gradient descent is robust to noise, often with higher-precision accumulation and loss scaling.

## Key concepts

| Term | Meaning |
|---|---|
| Significand (mantissa) | The fixed-precision digits of the number. |
| Exponent / bias | Power of two scaling the significand; stored offset by a constant. |
| Hidden bit | The implicit leading 1 of normal significands. |
| Machine epsilon | Gap between 1 and the next representable number. |
| Unit in the Last Place (ulp) | Spacing between adjacent floats at a given magnitude. |
| Correct rounding | Result equals the exact result rounded to a representable value. |
| Catastrophic cancellation | Loss of significant digits when subtracting close values. |
| Subnormal number | Value below the normal range with reduced precision, enabling gradual underflow. |
| NaN | A special value marking an undefined result. |

## How it fits

- **Below:** It builds on [binary notation](binary-and-positional-notation.md) and uses integer fields ([integers and two's complement](integers-and-twos-complement.md)) for the exponent and significand. It approximates the real numbers of [calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md).
- **Above:** Floating-point units are among the largest blocks in processors and dominate [Single Instruction, Multiple Data (SIMD) units and Graphics Processing Units (GPUs)](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md). Numerical [optimization](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md), [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md) in practice, [graphics transformations](../../14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md) and [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md) all depend on its error behaviour. Compiler [optimization](../../06-programming-languages/03-compilers/optimization.md) must respect its non-associativity.
- **Siblings:** [Integers](integers-and-twos-complement.md) are exact within a small range; floats are approximate over a huge range. Both are interpretations of [binary](binary-and-positional-notation.md) patterns.

## Common misconceptions

- **"Floating point is inherently imprecise or random."** Each operation is deterministic and correctly rounded; errors are predictable and analysable.
- **"Comparing floats with `==` is always wrong."** Equality is exact and well defined; the mistake is expecting rounded results to equal mathematically equal expressions.
- **"More bits fix numerical problems."** Higher precision delays them; an unstable algorithm stays unstable, and cancellation can still wipe out all the digits.

## Go deeper

- David Goldberg, "What Every Computer Scientist Should Know About Floating-Point Arithmetic" (1991): the standard tutorial.
- Nicholas Higham, *Accuracy and Stability of Numerical Algorithms* (1996): how rounding errors propagate and how to control them.
- Jean-Michel Muller et al., *Handbook of Floating-Point Arithmetic* (2010): comprehensive reference on formats and algorithms.
