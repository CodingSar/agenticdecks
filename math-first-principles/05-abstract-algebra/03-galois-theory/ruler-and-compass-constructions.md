# Ruler-and-Compass Constructions

> **Layer:** [05 Abstract Algebra](../README.md) › [Galois Theory](README.md)
> **Builds on:** [Field Extensions](../02-rings-and-fields/field-extensions.md), [The Galois Correspondence](the-galois-correspondence.md), [Algebraic and Transcendental Numbers](../../02-number-systems/01-constructing-the-numbers/algebraic-and-transcendental-numbers.md), [Fermat, Euler and Primitive Roots](../../02-number-systems/02-elementary-number-theory/fermat-euler-and-primitive-roots.md)
> **Enables:** [Euclidean Geometry](../../08-geometry/01-classical-geometry/euclidean-geometry.md), [History of Mathematics](../../15-mathematics-in-context/history-of-mathematics.md), [Open Problems](../../15-mathematics-in-context/open-problems.md)

## Essence

Greek geometers asked for constructions using only an unmarked straightedge and a compass, and left three problems unsolved: doubling the cube, trisecting an arbitrary angle and squaring the circle. For two thousand years nobody could do them or prove they were impossible. Algebra settled all three. Each construction step solves an equation of degree at most 2, so every constructible length lies in a tower of quadratic extensions of ℚ and has degree a power of 2. The cube root of 2 has degree 3, as does cos 20°, so Wantzel (1837) proved the first two impossible; π is not algebraic at all (Lindemann, 1882), which ends the third. The same method, with Galois groups, decides exactly which regular polygons can be drawn.

## Core tenets

1. **Constructible numbers form a field closed under square roots.** Start with the points 0 and 1 in the plane. Given lengths a and b, similar triangles produce a + b, a − b, ab and a/b, and a semicircle on a segment of length 1 + a produces √a. So every number built from integers by field operations and square roots is constructible: the regular pentagon, with cos 72° = (√5 − 1)/4, is an example.

2. **Every constructible number has degree a power of 2 over ℚ.** A new point is an intersection of two lines, a line and a circle, or two circles. Its coordinates solve linear or quadratic equations whose coefficients lie in the field K of coordinates already found, so each step is an extension of degree 1 or 2. By the tower law, a constructible α lies in a field of degree 2ᵏ over ℚ, and [ℚ(α) : ℚ] divides 2ᵏ.

3. **The exact test uses the Galois group: α is constructible if and only if the splitting field of its minimal polynomial has degree a power of 2.** A group of order 2ᵏ has a chain of subgroups each of index 2, which the Galois correspondence turns into a tower of quadratic extensions. Degree a power of 2 is necessary but not sufficient: a real root of x⁴ − x − 1 has degree 4, but the polynomial's Galois group is S₄, of order 24, so the root is not constructible.

4. **Doubling the cube is impossible.** A cube of twice the volume has side ∛2, a root of x³ − 2, which is irreducible by Eisenstein's criterion. So [ℚ(∛2) : ℚ] = 3, which is not a power of 2.

5. **Trisecting a general angle is impossible.** Some angles can be trisected: 90° gives 30°, which is constructible. But trisecting 60° requires cos 20°. From cos 3θ = 4cos³θ − 3cos θ, the number x = 2cos 20° satisfies x³ − 3x − 1 = 0. Neither 1 nor −1 is a root, so by the rational root test this cubic is irreducible, and x has degree 3. Wantzel published both proofs in 1837.

6. **Squaring the circle is impossible because π is transcendental.** A square of area π has side √π, which would make π constructible and hence algebraic. Lindemann proved in 1882 that π is transcendental, extending Hermite's 1873 proof that e is. Degree arguments alone cannot settle this case; it needs analysis.

7. **The Gauss–Wantzel theorem: a regular n-gon is constructible if and only if n is a power of 2 times a product of distinct Fermat primes.** Equivalently, Euler's totient φ(n) is a power of 2. The n-gon needs cos(2π/n), which lies in the cyclotomic field ℚ(ζₙ), whose Galois group (ℤ/n)ˣ is abelian of order φ(n). An abelian 2-group always has a chain of index-2 subgroups, so the condition suffices; conversely the degree must be a power of 2. Gauss found the 17-gon in 1796 and published sufficiency in 1801; Wantzel proved necessity.
   ```
   constructible:      3, 4, 5, 6, 8, 10, 12, 15, 16, 17, 20, …, 257, …, 65537
   not constructible:  7, 9, 11, 13, 14, 18, 19, …       (φ(7) = φ(9) = 6)
   ```

8. **Fermat primes leave an open question.** A Fermat prime has the form 2^(2^m) + 1. The known ones are 3, 5, 17, 257 and 65537. Fermat guessed all such numbers are prime, but Euler showed that 2³² + 1 = 641 × 6700417. Whether a sixth Fermat prime exists is open as of 2026, so the full list of constructible odd polygons is not known to be complete.

## Key concepts

| Term | Meaning |
|---|---|
| Constructible number | A coordinate reachable from 0 and 1 by straightedge and compass |
| Quadratic tower | A chain of fields, each of degree 1 or 2 over the last |
| Wantzel's theorem | Doubling the cube and general trisection are impossible |
| Transcendental number | One that satisfies no polynomial over ℚ |
| Fermat prime | A prime of the form 2^(2^m) + 1 |
| Gauss–Wantzel theorem | The n-gon is constructible exactly when φ(n) is a power of 2 |

## How it fits

- **Below:** the tower law from [field extensions](../02-rings-and-fields/field-extensions.md) does most of the work; [the Galois correspondence](the-galois-correspondence.md) gives the exact test; [transcendental numbers](../../02-number-systems/01-constructing-the-numbers/algebraic-and-transcendental-numbers.md) settle the circle; Euler's totient comes from [elementary number theory](../../02-number-systems/02-elementary-number-theory/fermat-euler-and-primitive-roots.md).
- **Above:** the limits of [Euclidean geometry](../../08-geometry/01-classical-geometry/euclidean-geometry.md) are drawn here; the Fermat-prime question belongs with [open problems](../../15-mathematics-in-context/open-problems.md); the three classical problems are a standard case study in [the history of mathematics](../../15-mathematics-in-context/history-of-mathematics.md).
- **Siblings:** [solvability by radicals](solvability-by-radicals.md) allows roots of every order, while constructions allow only square roots, so the group must be a 2-group rather than merely solvable.

## Common misconceptions

- **"Nobody has found a trisection yet."** It is proved impossible, so claimed constructions contain an error. The theorem concerns straightedge and compass only: a marked ruler (neusis) or paper folding can trisect angles and double cubes, because they solve cubic equations.
- **"Some angles cannot be trisected even approximately."** Any angle can be trisected to any accuracy; the impossibility concerns exact constructions in finitely many steps.
- **"The compass is essential and the straightedge is too."** The Mohr–Mascheroni theorem shows the compass alone constructs every constructible point; the straightedge alone does not suffice.

## Go deeper

- Richard Courant and Herbert Robbins, *What Is Mathematics?* (1941): the classical problems and constructible numbers for a general reader.
- Robin Hartshorne, *Geometry: Euclid and Beyond* (2000): constructions, field theory and the regular polygons in full.
