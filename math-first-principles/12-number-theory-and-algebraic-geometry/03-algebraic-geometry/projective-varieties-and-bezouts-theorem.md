# Projective Varieties and Bézout's Theorem

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › [Algebraic Geometry](README.md)
> **Builds on:** [Varieties and the Nullstellensatz](varieties-and-the-nullstellensatz.md), [Projective Geometry](../../08-geometry/01-classical-geometry/projective-geometry.md), [Polynomial Rings](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md), [Compactness](../../07-topology/01-point-set-topology/compactness.md)
> **Enables:** [Algebraic Curves and Riemann–Roch](algebraic-curves-and-riemann-roch.md), [Schemes](schemes.md), [Elliptic Curves](../04-elliptic-curves-and-modular-forms/elliptic-curves.md)

## Essence

Two distinct lines in the plane meet in one point, unless they are parallel. A line meets a circle in two points, unless it misses it or touches it. Counting intersections is full of exceptions until three repairs are made: add points at infinity, so parallel lines meet; use complex coordinates, so missing becomes meeting at complex points; and count tangencies with multiplicity. After all three, Bézout's theorem holds without exception: plane curves of degrees d and e with no common component meet in exactly d·e points. Projective space is the setting where these repairs are built in, and projective varieties are the compact objects of algebraic geometry.

## Core tenets

1. **Projective space adds the points at infinity.** The projective space ℙⁿ over a field k is the set of lines through the origin in kⁿ⁺¹. A point is written in homogeneous coordinates (x₀ : ⋯ : xₙ), not all zero, with (x₀ : ⋯ : xₙ) = (λx₀ : ⋯ : λxₙ) for λ ≠ 0. The set where x₀ ≠ 0 is a copy of kⁿ, through (1 : x₁ : ⋯ : xₙ), and the rest, x₀ = 0, is a copy of ℙⁿ⁻¹, the hyperplane at infinity. In ℙ², parallel lines y = mx + b meet at the point (0 : 1 : m), which depends only on the direction.

2. **Projective varieties are zero sets of homogeneous polynomials.** Only homogeneous polynomials have a well-defined zero set on ℙⁿ, since F(λx) = λᵈF(x). To close up an affine curve, homogenise: f(x, y) of degree d becomes F = zᵈf(x/z, y/z). The hyperbola xy = 1 becomes xy = z², which adds the points (1 : 0 : 0) and (0 : 1 : 0), the directions of its asymptotes. Every projective variety is covered by the affine charts xᵢ ≠ 0, and the Nullstellensatz carries over, except that the ideal (x₀, …, xₙ) cuts out nothing.

3. **Projective varieties are compact, and that drives elimination.** Over ℂ, ℙⁿ is a quotient of the unit sphere in ℂⁿ⁺¹, hence compact. The algebraic replacement, valid over any field, is that projective varieties are complete: the image of a projective variety under a morphism is closed. This is the main theorem of elimination theory, and it explains why projecting a curve from ℙ² × ℙ¹ never loses limit points. Liouville's theorem has an analogue: on a connected projective variety every regular function is constant.

4. **Intersections need multiplicities.** The parabola y = x² meets the line y = 0 only at the origin, but the line is tangent there and a nearby line y = ε meets the parabola twice. The intersection multiplicity of curves F and G at a point P is the dimension over k of the local ring at P modulo (F, G); here it is the dimension of k[x]/(x²), which is 2. It equals 1 exactly when the curves are smooth at P and cross transversally.

5. **Bézout's theorem.** Let F and G be homogeneous polynomials in three variables over an algebraically closed field, of degrees d and e, with no common factor. Then the curves F = 0 and G = 0 in ℙ² meet in exactly d·e points, counted with multiplicity. The proof eliminates one variable: the resultant of F and G with respect to x₀ is a homogeneous polynomial of degree d·e in x₁ and x₂, a [determinant](../../04-linear-algebra/02-determinants-and-eigenvalues/determinants.md) of their coefficients, whose roots record the intersection points and whose multiplicities match.

6. **All three repairs are needed, as two circles show.** The circles x² + y² = 1 and (x − 1)² + y² = 1 have degree 2 each, so Bézout predicts 4 intersections. Two are the real points (1/2, ±√3/2). Homogenised, the circles are x² + y² = z² and (x − z)² + y² = z²; at infinity, z = 0, both reduce to x² + y² = 0, giving the complex points (1 : i : 0) and (1 : −i : 0). Every circle passes through these two "circular points", so any two circles meet in at most two further points.

7. **Degree and dimension come from counting.** The homogeneous coordinate ring of a projective variety X is graded by degree. Hilbert showed that the dimension of its degree-m part is, for large m, a polynomial in m whose leading term is (deg X)·mʳ/r!, where r is the dimension of X. The degree is the number of points in which X meets a general linear space of complementary dimension. Bézout generalises: n hypersurfaces in ℙⁿ of degrees d₁, …, dₙ meeting in finitely many points meet in d₁⋯dₙ of them.

8. **Bézout has classical consequences.** A cubic curve through eight general points of the plane passes through a fixed ninth point, the Cayley–Bacharach theorem: two cubics through the eight points meet in 3·3 = 9 points, and every cubic through the eight is a combination of those two. This gives Pascal's theorem on hexagons inscribed in a conic, and it is one proof that the chord-and-tangent law on an [elliptic curve](../04-elliptic-curves-and-modular-forms/elliptic-curves.md) is associative.

## Key concepts

| Term | Meaning |
|---|---|
| Projective space ℙⁿ | Lines through the origin in kⁿ⁺¹, with homogeneous coordinates |
| Homogenisation | Making a polynomial homogeneous with an extra variable, to add points at infinity |
| Projective variety | An irreducible zero set of homogeneous polynomials in ℙⁿ |
| Completeness | Images of projective varieties under morphisms are closed |
| Intersection multiplicity | dim of the local ring modulo the two equations |
| Bézout's theorem | Curves of degrees d, e with no common component meet in d·e points |
| Degree | Number of intersections with a general complementary linear space |

## How it fits

- **Below:** [projective geometry](../../08-geometry/01-classical-geometry/projective-geometry.md) supplies the space and its symmetries; [affine varieties](varieties-and-the-nullstellensatz.md) are the charts; [compactness](../../07-topology/01-point-set-topology/compactness.md) is what completeness imitates.
- **Above:** elliptic curves are plane cubics in ℙ², and their group law rests on Bézout.
- **Siblings:** [curves and Riemann–Roch](algebraic-curves-and-riemann-roch.md) use Bézout to compute the genus of plane curves; [schemes](schemes.md) record intersection multiplicities as nilpotent structure.

## Common misconceptions

- **"Bézout's theorem is a bound"**: in ℙ² over an algebraically closed field, with multiplicity, it is an exact count.
- **"Points at infinity are a convention"**: they are honest points, interchangeable with the others by a projective change of coordinates.

## Go deeper

- William Fulton, *Algebraic Curves* (1969, revised edition freely available online): intersection multiplicity and Bézout from first principles.
- Joe Harris, *Algebraic Geometry: A First Course* (1992): projective varieties through many examples.
- Igor Shafarevich, *Basic Algebraic Geometry 1* (3rd edition, 2013): varieties, completeness and intersections.
