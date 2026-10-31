# Fourier Analysis on Groups

> **Layer:** [09 Advanced Analysis](../README.md) › [Harmonic Analysis](README.md)
> **Builds on:** [Fourier Series](fourier-series.md), [The Fourier Transform](the-fourier-transform.md), [Representations of Finite Groups](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md), [Compactness](../../07-topology/01-point-set-topology/compactness.md), [Modular Arithmetic](../../02-number-systems/02-elementary-number-theory/modular-arithmetic.md)
> **Enables:** [Primes in Arithmetic Progressions](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/primes-in-arithmetic-progressions.md), [The Langlands Programme](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/the-langlands-programme.md), [Error-Correcting Codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md), [Numerical Linear Algebra](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-linear-algebra.md), [Quantum Algorithms (computer science)](../../../cs-first-principles/02-theory-of-computation/05-quantum-computation/quantum-algorithms.md)

## Essence

Fourier series live on the circle and the Fourier transform on the line, but what makes both work is only that the circle and the line are groups. The exponentials e^(inx) and e^(2πixξ) are characters: continuous homomorphisms into the unit circle. On any locally compact abelian group the characters themselves form a group, the dual group, and functions on the group decompose into characters exactly as signals decompose into frequencies. On a finite cyclic group this is the Discrete Fourier Transform (DFT), computed by the Fast Fourier Transform (FFT).

## Core tenets

1. **Characters are the frequencies of a group.** A character of an abelian group G is a homomorphism χ : G → 𝕋, where 𝕋 is the unit circle, continuous if G has a topology. The characters of the circle 𝕋 are z ↦ zⁿ for n ∈ ℤ; those of ℤ are n ↦ e^(inθ), one for each point of 𝕋; those of ℝ are x ↦ e^(2πixξ), one for each ξ ∈ ℝ; those of ℤ/n are j ↦ ω^(jk) with ω = e^(2πi/n). Pointwise multiplication makes them a group Ĝ, so 𝕋̂ = ℤ, ℤ̂ = 𝕋, and ℝ and ℤ/n are their own duals. The Fourier transform is f̂(χ) = ∫ f(x)·χ̄(x) dx, integrating against a translation-invariant measure.

2. **Every locally compact group has an invariant measure.** Alfréd Haar proved in 1933 that a locally compact group carries a translation-invariant measure, unique up to a constant: Lebesgue measure on ℝ, arc length on 𝕋, counting measure on ℤ. Local compactness is what makes this possible; an infinite-dimensional Banach space under addition has no non-zero translation-invariant Borel measure that is finite on some open set.

3. **Pontryagin duality: a group is the dual of its dual.** For a locally compact abelian group G, the natural map from G to the dual of Ĝ, sending x to "evaluate at x", is an isomorphism of topological groups. Lev Pontryagin proved it in 1934 under extra hypotheses, and Egbert van Kampen extended it to all such groups. Compact groups have discrete duals and discrete groups have compact duals, which is why the circle has a series and the line has an integral. Inversion and Plancherel hold in this generality.

4. **On a finite abelian group, characters are an orthonormal basis.** For G finite with ∣G∣ = n, the characters satisfy (1/n)·∑ χ(x)·ψ̄(x) = 1 if χ = ψ and 0 otherwise: if χ ≠ ψ, multiplying the sum by (χψ̄)(y) ≠ 1 permutes its terms, so the sum is 0. There are exactly n characters, so they form an orthonormal basis of the n-dimensional space of functions on G, and Fourier inversion is linear algebra. Characters are eigenvectors of every translation, hence of every convolution operator. In matrix terms, the DFT diagonalises every circulant matrix, which is why circulant systems can be solved quickly in [numerical linear algebra](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-linear-algebra.md).

5. **The FFT computes the DFT in O(n log n) operations.** The DFT of a vector of length n is f̂(k) = ∑ⱼ f(j)·ω^(−jk), which costs n² multiplications directly. If n = 2m, split j into even and odd indices: each half is a DFT of length m, and the two combine with n further operations. Repeating gives O(n log n). James Cooley and John Tukey published the algorithm in 1965, and it was later found that Gauss had used the idea around 1805 to interpolate asteroid orbits. Multiplying two polynomials or two large integers reduces to convolution, so the FFT also speeds up arithmetic.

6. **Characters detect structure in number theory and combinatorics.** Dirichlet characters, the characters of the multiplicative group (ℤ/q)ˣ, isolate the integers in one residue class, and Dirichlet used them to prove that every progression a, a + q, a + 2q, … with gcd(a, q) = 1 contains infinitely many [primes](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/primes-in-arithmetic-progressions.md). On (ℤ/2)ⁿ the characters are the Walsh–Hadamard functions, and Fourier analysis there yields the MacWilliams identities for [linear codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md). Roth's 1953 theorem that dense sets of integers contain three-term arithmetic progressions is proved by a density increment on a large Fourier coefficient, the start of [additive combinatorics](../../03-combinatorics-and-graph-theory/04-extremal-combinatorics/additive-combinatorics.md). Peter Shor's 1994 factoring algorithm uses a quantum Fourier transform over ℤ/2ⁿ to find the period of a function, as described in [quantum algorithms](../../../cs-first-principles/02-theory-of-computation/05-quantum-computation/quantum-algorithms.md).

7. **For non-abelian groups, characters become representations.** A non-abelian group has too few one-dimensional characters to span its functions, so one uses irreducible unitary representations instead. For a finite group, the regular representation contains each irreducible ρ with multiplicity dim ρ, giving ∣G∣ = ∑ (dim ρ)² and a Fourier transform with matrix values; see [representations of finite groups](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md). The Peter–Weyl theorem of 1927 does the same for compact groups; [Lie groups](../../08-geometry/04-lie-theory/representations-of-lie-groups.md) carry the theory further. John Tate's 1950 thesis redid the theory of L-functions as Fourier analysis on the adeles, and the [Langlands programme](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/the-langlands-programme.md) is, in part, non-abelian harmonic analysis on such groups.

## Key concepts

| Term | Meaning |
|---|---|
| Character | A continuous homomorphism χ : G → 𝕋 |
| Dual group Ĝ | The group of characters under pointwise multiplication |
| Haar measure | The translation-invariant measure on a locally compact group |
| Pontryagin duality | The dual of Ĝ is G |
| Discrete Fourier Transform | f̂(k) = ∑ f(j)·ω^(−jk) on ℤ/n |
| Fast Fourier Transform | An O(n log n) algorithm for the Discrete Fourier Transform |
| Circulant matrix | A matrix that commutes with cyclic shift; diagonalised by the Discrete Fourier Transform |
| Dirichlet character | A character of (ℤ/q)ˣ, extended by 0 to all integers |
| Peter–Weyl theorem | Matrix coefficients of irreducible representations span L² of a compact group |

## How it fits

- **Below:** [Fourier series](fourier-series.md) and the [Fourier transform](the-fourier-transform.md) are the cases 𝕋 and ℝ; [group representations](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md) and [modular arithmetic](../../02-number-systems/02-elementary-number-theory/modular-arithmetic.md) give the finite cases; [compactness](../../07-topology/01-point-set-topology/compactness.md) underlies Haar measure.
- **Above:** [primes in progressions](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/primes-in-arithmetic-progressions.md) and the [Langlands programme](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/the-langlands-programme.md) in 12; [codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md) and signal processing in 14; convolutional neural networks, as in [convolutional networks](../../../cs-first-principles/13-artificial-intelligence/03-deep-learning/convolutional-networks.md), are built on translation-equivariant maps.
- **Siblings:** [distributions](distributions.md) handle Poisson summation on ℝ; [spectral theory](../03-functional-analysis/spectral-theory.md) generalises diagonalising convolutions to diagonalising any self-adjoint operator.

## Common misconceptions

- **"The FFT is an approximation to the Fourier transform"**: it computes the Discrete Fourier Transform exactly; approximation enters only when one samples a continuous signal.
- **"Fourier analysis needs sines and cosines"**: it needs only a group and its characters; on (ℤ/2)ⁿ the characters take values ±1.

## Go deeper

- Audrey Terras, *Fourier Analysis on Finite Groups and Applications* (1999): finite groups, graphs and codes.
- Walter Rudin, *Fourier Analysis on Groups* (1962): the classical theory for locally compact abelian groups.
- Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction* (2003): finite Fourier analysis, the FFT and Dirichlet's theorem.
