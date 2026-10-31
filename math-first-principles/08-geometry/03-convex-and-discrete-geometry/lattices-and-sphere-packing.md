# Lattices and Sphere Packing

> **Layer:** [08 Geometry](../README.md) › [Convex and Discrete Geometry](README.md)
> **Builds on:** [Convex sets and separation](convex-sets-and-separation.md), [Polytopes](polytopes.md), [Quadratic forms and positive definiteness](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md), [Determinants](../../04-linear-algebra/02-determinants-and-eigenvalues/determinants.md)
> **Enables:** [The Fourier transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md), [Modular forms](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/modular-forms.md), [Error-correcting codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md), [Computers and proof](../../15-mathematics-in-context/computers-and-proof.md), [Public-key cryptography](../../../cs-first-principles/11-security-and-cryptography/02-cryptography/public-key-cryptography.md)

## Essence

A lattice is a discrete grid in ℝⁿ, all integer combinations of a basis, and the sphere-packing problem asks how densely equal balls can fill space. Lattices give the natural candidates, and Minkowski's geometry of numbers uses their volume to force lattice points into convex bodies. Kepler's 1611 claim that oranges stacked in a pyramid are densest in three dimensions resisted proof until Hales's computer-assisted proof of 1998, formally verified in 2014. In dimensions 8 and 24, where the exceptional E₈ and Leech lattices live, Viazovska and coauthors found short proofs in 2016 using modular forms, work recognised by her Fields Medal in 2022.

## Core tenets

1. **A lattice has a volume that does not depend on the basis.** If the columns of B form a basis, the lattice Λ = Bℤⁿ has fundamental parallelepiped of volume ∣det B∣. Another basis is BU with U an integer matrix whose inverse is also integer, so det U = ±1 and the volume is unchanged; it is called the covolume, det Λ. Equivalently, Λ is described by the [positive-definite quadratic form](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md) x ↦ ‖Bx‖² on ℤⁿ, and lattices up to rotation correspond to such forms up to integer change of variables.

2. **Minkowski's theorem forces lattice points into large symmetric convex bodies.** If K ⊆ ℝⁿ is convex, symmetric about 0, and has volume greater than 2ⁿ det Λ, then K contains a non-zero lattice point. Proof: the translates of ½K by lattice vectors cannot all be disjoint, since they would then pack space with density above 1; if two overlap, ½k₁ + λ = ½k₂ + μ, and symmetry and convexity make ½(k₂ − k₁) = λ − μ a non-zero lattice point in K. Without symmetry it fails: a large box shifted off 0 can miss every lattice point. Applications include Fermat's two-squares theorem and the finiteness of the class number.

3. **Packing density is the fraction of space covered by the balls.** For a lattice packing, balls of radius half the minimal distance are centred at lattice points, and the density is the ball's volume divided by det Λ. In the plane the hexagonal lattice gives π/√12 ≈ 0.9069, optimal among lattices (Lagrange) and among all packings. In three dimensions the face-centred cubic (FCC) lattice gives π/√18 ≈ 0.7405, and Gauss (1831) proved it optimal among lattice packings.

4. **Kepler's conjecture is a theorem, proved by computer and then formally checked.** Kepler's claim that no packing of equal balls in space beats π/√18 is hard because non-lattice packings must be included and because there is no unique optimum: hexagonal close packing, layered differently, ties with FCC. Hales, with Ferguson for part of the work, announced a proof in 1998 that reduced the problem to many inequalities on finite configurations checked by computer; it was published in 2005, and referees could not certify every computation. The Flyspeck project completed a formal verification in proof assistants in 2014, as described in [computers and proof](../../15-mathematics-in-context/computers-and-proof.md).

5. **Dimensions 8 and 24 have exceptional lattices.** E₈ consists of the vectors in ℤ⁸ or (ℤ + ½)⁸ whose coordinates sum to an even number; its 240 minimal vectors form the root system of the exceptional [Lie algebra E₈](../04-lie-theory/the-classification-of-simple-lie-algebras.md), and its density is π⁴/384 ≈ 0.254. The Leech lattice in dimension 24 has 196,560 minimal vectors, each ball touching that many others, and no vectors of squared length 2. Both can be built from [error-correcting codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md): E₈ from the extended Hamming code of length 8, Leech from the binary Golay code of length 24.

6. **Viazovska proved E₈ and Leech optimal using Fourier analysis and modular forms.** Cohn and Elkies (2003) showed that a function f on ℝⁿ with f ≤ 0 outside a ball, a [Fourier transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md) that is non-negative, and f(0) = f̂(0) > 0, gives an upper bound on the density of every packing, by Poisson summation over the lattice. Their numerical bounds nearly matched E₈ and Leech. Viazovska (2016, published 2017) built the exact function in dimension 8 from [modular forms](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/modular-forms.md); within weeks Cohn, Kumar, Miller, Radchenko and Viazovska did dimension 24. She received the Fields Medal in 2022. As of 2026 the optimal density is known only in dimensions 1, 2, 3, 8 and 24.

7. **Hard lattice problems underpin modern cryptography.** Finding a shortest non-zero vector in a high-dimensional lattice given by a bad basis is believed hard, even for quantum computers. The Lenstra–Lenstra–Lovász (LLL) algorithm (1982) finds a vector within an exponential factor of shortest in polynomial time, which suffices for many applications but not to break well-chosen schemes. The post-quantum standards adopted in 2024, such as the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM), rest on such problems ([public-key cryptography](../../../cs-first-principles/11-security-and-cryptography/02-cryptography/public-key-cryptography.md)).

## Key concepts

| Term | Meaning |
|---|---|
| Lattice | The integer combinations Bℤⁿ of a basis of ℝⁿ |
| Covolume | ∣det B∣; the volume of a fundamental domain |
| Packing density | The fraction of space covered by the balls |
| Kissing number | How many balls can touch one ball; 12 in three dimensions, 240 in eight, 196,560 in twenty-four |
| Minkowski's theorem | A symmetric convex body of volume above 2ⁿ det Λ contains a non-zero lattice point |
| FCC lattice | Face-centred cubic packing; Kepler's oranges |
| E₈ lattice | The even unimodular lattice in dimension 8 |
| Leech lattice | The even unimodular lattice in dimension 24 with no roots |
| Linear programming bound | The Cohn–Elkies density bound from an auxiliary function and its Fourier transform |

## How it fits

- **Below:** Determinants give covolume, quadratic forms describe lattices, and [convex sets](convex-sets-and-separation.md) supply Minkowski's bodies.
- **Above:** Fourier analysis and modular forms solved dimensions 8 and 24; codes, number theory and cryptography use lattices.
- **Siblings:** [Polytopes](polytopes.md) give Voronoi cells; the crystallographic lattices of [symmetry groups and tilings](../01-classical-geometry/symmetry-groups-and-tilings.md) are the same objects; E₈ is a root system in [Lie theory](../04-lie-theory/README.md).

## Common misconceptions

- **"The densest packing is always a lattice"**: In three dimensions non-lattice packings tie with FCC, and in many high dimensions the best known packings are not lattices.
- **"Kepler's conjecture was settled in 1998"**: The proof was announced then, published in 2005, and only fully verified formally in 2014.
- **"Sphere packing is solved in every dimension below 24"**: As of 2026 only dimensions 1, 2, 3, 8 and 24 are solved.

## Go deeper

- Conway and Sloane, *Sphere Packings, Lattices and Groups* (1988): the encyclopaedic reference.
- Thompson, *From Error-Correcting Codes through Sphere Packings to Simple Groups* (1983): the history linking codes, E₈ and Leech.
- Viazovska, "The sphere packing problem in dimension 8", *Annals of Mathematics* (2017): the proof, under thirty pages.
