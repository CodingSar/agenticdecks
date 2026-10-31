# Error-Correcting Codes

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Information, Codes and Cryptography](README.md)
> **Builds on:** [Information Theory](information-theory.md), [Finite Fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md), [Polynomial Rings](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md), [Linear Systems and Rank–Nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md), [Interpolation and Approximation](../01-numerical-analysis/interpolation-and-approximation.md)
> **Enables:** [Cryptography](cryptography.md), [Sampling and Compressed Sensing](../06-data-and-learning/sampling-and-compressed-sensing.md), [Channel Capacity and Error Correction (CS)](../../../cs-first-principles/02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md), [Encoding and Framing (CS)](../../../cs-first-principles/08-networking/02-link-layer/encoding-and-framing.md)

## Essence

An error-correcting code adds redundancy to a message so that the receiver can recover it even after some symbols are corrupted. Shannon's theorem promises codes that approach channel capacity but does not say how to build or decode them. Coding theory answers with algebra: codes are subspaces of vector spaces over finite fields, their power is measured by the minimum distance between codewords, and the best families come from polynomials. The subject runs from Richard Hamming's single-error-correcting codes (1950) through Reed–Solomon codes, which protect compact discs and QR (quick response) codes, to the iteratively decoded codes in today's mobile phones that operate close to Shannon's limit.

## Core tenets

1. **Minimum distance governs error correction.** The Hamming distance between two words of length n counts the positions where they differ. If every two codewords differ in at least d positions, the balls of radius t = ⌊(d − 1)/2⌋ around codewords are disjoint, so up to t errors can be corrected by choosing the nearest codeword, and up to d − 1 errors can be detected. The design problem is a packing problem: many codewords, far apart.

2. **Linear codes are subspaces.** A linear [n, k, d] code over the finite field F_q is a k-dimensional subspace of F_qⁿ with minimum distance d. It is the image of a k × n generator matrix G and the kernel of an (n − k) × n parity-check matrix H, and its minimum distance is the smallest weight of a nonzero codeword. If y = c + e is received, the syndrome Hy = He depends only on the error, which reduces decoding to finding the lightest e with a given syndrome. For general linear codes this is hard: Elwyn Berlekamp, Robert McEliece and Henk van Tilborg (1978) proved it NP-complete (complete for nondeterministic polynomial time), so good codes need extra structure.

3. **Hamming codes correct one error perfectly.** Take for H the 3 × 7 binary matrix whose columns are the seven nonzero vectors of F₂³. Any two columns are distinct, so d = 3, and the syndrome of a single error is the column at its position, which names the position directly. The [7, 4, 3] Hamming code is perfect: its 16 codewords, each with its 7 neighbours at distance 1, fill all 128 words of length 7 exactly.

4. **Counting bounds limit what codes can exist.** The Hamming bound says the disjoint balls of radius t must fit in the whole space:

   ```
   q^k · ( C(n,0) + C(n,1)(q − 1) + ⋯ + C(n,t)(q − 1)^t ) ≤ q^n
   ```

   Apart from repetition codes, the only perfect codes over prime-power alphabets correcting more than one error are the binary [23, 12, 7] and ternary [11, 6, 5] Golay codes (Aimo Tietäväinen, and independently Victor Zinoviev and Vladimir Leontiev, 1973). The Singleton bound (Richard Singleton, 1964), d ≤ n − k + 1, follows by deleting d − 1 coordinates. In the other direction, a greedy argument (Edgar Gilbert, 1952; Rom Varshamov, 1957) gives binary codes of rate at least 1 − H(δ) at relative distance δ, where H is the binary entropy; whether this is asymptotically optimal for binary codes is open as of 2026. Michael Tsfasman, Serge Vlăduţ and Thomas Zink (1982) beat it for square alphabet sizes q ≥ 49 using codes from algebraic curves.

5. **Reed–Solomon codes evaluate polynomials.** Irving Reed and Gustave Solomon (1960) encoded a message as a polynomial of degree less than k over F_q and transmitted its values at n distinct points. Two distinct such polynomials agree at fewer than k points, so d = n − k + 1, meeting the Singleton bound: the codes are maximum distance separable (MDS). Correcting errors is interpolation in the presence of wrong values, which Berlekamp's algorithm (1968) does efficiently; Venkatesan Guruswami and Madhu Sudan (1999) corrected beyond half the minimum distance by returning a short list of candidates. Since one wrong byte is one symbol error, Reed–Solomon codes are robust to bursts, which is why they protect compact discs, deep-space links and QR codes.

6. **Sparse graphs and polarisation approach capacity.** Low-density parity-check (LDPC) codes, introduced by Robert Gallager (1960, 1963), have a parity-check matrix with few ones per row and column, and are decoded by passing probability messages along its graph. Forgotten for decades, they were revived after turbo codes (Claude Berrou, Alain Glavieux and Punya Thitimajshima, 1993) showed iterative decoding reaching close to capacity in practice. Erdal Arıkan's polar codes (2009) were the first explicit family proved to achieve the capacity of binary-input symmetric memoryless channels with encoding and decoding in O(n log n) operations, by recursively splitting a channel into nearly perfect and nearly useless ones. Both families are used in fifth-generation mobile standards.

## Key concepts

| Term | Meaning |
|---|---|
| Hamming distance | Number of positions in which two words differ |
| Minimum distance d | Smallest distance between distinct codewords; corrects ⌊(d − 1)/2⌋ errors |
| [n, k, d] code | Length n, dimension k, minimum distance d; rate k/n |
| Syndrome | Hy, which depends only on the error pattern |
| Perfect code | One whose correction balls exactly fill the space |
| Maximum distance separable code | One meeting the Singleton bound d = n − k + 1 |
| Belief propagation | Iterative decoding by passing probabilities on the code's graph |

## How it fits

- **Below:** codes live in vector spaces over [finite fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md); Reed–Solomon codes use the fact from [polynomial rings](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md) that a nonzero polynomial of degree m has at most m roots; syndromes are [linear systems](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md); [information theory](information-theory.md) sets the target.
- **Above:** the extended Hamming and Golay codes build the E₈ and Leech [lattices](../../08-geometry/03-convex-and-discrete-geometry/lattices-and-sphere-packing.md); [compressed sensing](../06-data-and-learning/sampling-and-compressed-sensing.md) is decoding over the real numbers; the computer-science view is in [channel capacity and error correction](../../../cs-first-principles/02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md) and [link-layer encoding](../../../cs-first-principles/08-networking/02-link-layer/encoding-and-framing.md).
- **Siblings:** Reed–Solomon decoding is [polynomial interpolation](../01-numerical-analysis/interpolation-and-approximation.md) over a finite field; the hardness of decoding random linear codes underlies code-based [cryptography](cryptography.md).

## Common misconceptions

- **"More redundancy always means better protection"**: repetition codes add redundancy with poor distance per bit; good codes spread redundancy so that every codeword differs from every other in many places.
- **"Correcting beyond half the minimum distance is impossible"**: unique decoding is, but list decoding returns a few candidates and usually only one is plausible.

## Go deeper

- F. Jessie MacWilliams and Neil J. A. Sloane, *The Theory of Error-Correcting Codes* (1977): the classic encyclopaedia of algebraic codes.
- Ron M. Roth, *Introduction to Coding Theory* (2006): a rigorous modern text.
- Tom Richardson and Rüdiger Urbanke, *Modern Coding Theory* (2008): low-density parity-check codes and iterative decoding.
