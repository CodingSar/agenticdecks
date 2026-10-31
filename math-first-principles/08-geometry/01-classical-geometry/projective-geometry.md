# Projective Geometry

> **Layer:** [08 Geometry](../README.md) › [Classical Geometry](README.md)
> **Builds on:** [Euclidean geometry](euclidean-geometry.md), [Linear maps and matrices](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md), [Dual spaces](../../04-linear-algebra/01-vector-spaces-and-linear-maps/dual-spaces.md), [Equivalence relations and quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md)
> **Enables:** [The Erlangen programme](the-erlangen-programme.md), [Projective varieties and Bézout's theorem](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/projective-varieties-and-bezouts-theorem.md), [Elliptic curves](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/elliptic-curves.md), [Geometry and transformations](../../../cs-first-principles/14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md), [Computer vision](../../../cs-first-principles/14-human-and-visual-computing/03-media-and-vision/computer-vision.md)

## Essence

Projective geometry began with Renaissance perspective: projecting a scene onto a canvas keeps straight lines straight and keeps incidences, but changes lengths, angles and parallelism. Made precise, it is the geometry of lines through the origin of a vector space. The projective plane adds to the ordinary plane a line at infinity on which parallel lines meet, so that any two lines meet in exactly one point and points and lines become interchangeable. Its one numerical invariant is the cross-ratio, and its two classical theorems, Desargues' and Pappus's, turn out to say exactly what kind of algebra the coordinates come from.

## Core tenets

1. **The projective plane is a quotient of a vector space.** Define ℝP² as ℝ³ ∖ {0} modulo v ∼ λv for λ ≠ 0, a [quotient](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md) whose classes are written in homogeneous coordinates [x : y : z]. Points with z ≠ 0 can be scaled to [x : y : 1], a copy of the ordinary plane; the points [x : y : 0] form the line at infinity, one point per direction. A projective line is a plane through 0 in ℝ³, with equation ax + by + cz = 0. The construction works over any field: over the field with two elements it gives the Fano plane, with 7 points and 7 lines.

2. **Two points determine one line, and two lines meet in exactly one point.** Two independent vectors span exactly one plane, and two distinct planes through 0 in ℝ³ meet in a line, since 2 + 2 − 3 = 1. The parallel lines y = mx + c and y = mx + d meet at [1 : m : 0], their shared direction. Removing the exceptions of Euclidean geometry is what lets [Bézout's theorem](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/projective-varieties-and-bezouts-theorem.md) count intersections exactly.

3. **Duality: every theorem has a dual with points and lines exchanged.** The point [a : b : c] corresponds to the line ax + by + cz = 0; this is the passage from a vector space to its [dual space](../../04-linear-algebra/01-vector-spaces-and-linear-maps/dual-spaces.md), which turns lines through 0 into planes through 0. Incidence, "p lies on ℓ", becomes ℓ(p) = 0, which is symmetric in the two, so the dual of any proof is a proof. Pascal's theorem about six points on a conic dualises to Brianchon's theorem about six tangent lines.

4. **Projective maps can move any four general points to any four, so lengths, angles and parallelism are not invariant.** The projective transformations come from invertible [linear maps](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md) of ℝ³ and form PGL(3, ℝ), invertible 3 × 3 matrices up to scaling, of dimension 8. Given four points with no three collinear, three of them fix a basis up to scaling and the fourth fixes the scalings, so exactly one transformation sends them to any other such four. Since the line at infinity can be moved to any line, parallelism is not invariant. All non-degenerate conics are equivalent: ellipse, parabola and hyperbola differ only in meeting the line at infinity in 0, 1 or 2 points.

5. **The cross-ratio is the only invariant of four collinear points.** In a coordinate t on a line, projective maps are t ↦ (pt + q)/(rt + s). Under such a map each difference x − y is multiplied by a factor depending on x and on y separately, and in the cross-ratio below every point appears once above and once below the line, so the factors cancel. Since three points can be sent to any three, two quadruples are equivalent if and only if their cross-ratios agree. This is why a photograph of equally spaced fence posts shows shrinking gaps but a fixed cross-ratio, and why the Klein model of [non-Euclidean geometry](non-euclidean-geometry.md) measures distance by it.

   ```
   (a, b; c, d) = ( (c − a)(d − b) ) / ( (c − b)(d − a) )
   ```

6. **Desargues' and Pappus's theorems record the algebra of the coordinates.** Desargues: if two triangles are in perspective from a point, the three intersections of corresponding sides are collinear. Pappus: for A, B, C on one line and A′, B′, C′ on another, the points AB′ ∩ A′B, AC′ ∩ A′C and BC′ ∩ B′C are collinear. Starting from incidence axioms alone, a projective plane has coordinates in a division ring if and only if Desargues holds, and in a field if and only if Pappus holds; commutativity of multiplication is exactly Pappus. Desargues is a theorem in any projective space of dimension at least 3 (lift the triangles into different planes, which meet in a line), but not in every plane: Moulton's plane, with lines bent where they cross an axis, is a counterexample.

7. **Finite projective planes raise an open problem.** The plane over the field with q elements has q² + q + 1 points, with q + 1 on each line, and every known finite projective plane has prime-power order. The Bruck–Ryser theorem (1949) excludes orders such as 6 and 14, and a long computer search by Lam, Thiel and Swiercz (1989) excluded 10. Whether a plane of order 12, or any order that is not a prime power, exists is open as of 2026.

## Key concepts

| Term | Meaning |
|---|---|
| Projective plane ℝP² | Lines through 0 in ℝ³; the plane plus a line at infinity |
| Homogeneous coordinates | [x : y : z], defined up to a common non-zero factor |
| Line at infinity | z = 0; one point for each direction of parallel lines |
| Duality | Exchange of points and lines, from a vector space and its dual |
| Projective transformation | A map induced by an invertible linear map; the group PGL(3, ℝ) |
| Cross-ratio | The invariant of four collinear points |
| Conic | The zero set of a non-degenerate quadratic form in x, y, z |
| Desarguesian plane | A plane in which Desargues holds; equivalently, one with division-ring coordinates |
| Fano plane | The smallest projective plane: 7 points and 7 lines, over the field of two elements |

## How it fits

- **Below:** [Quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md) build the space, linear maps give its transformations, and [Euclidean geometry](euclidean-geometry.md) is the part away from infinity.
- **Above:** Projective space is the home of [projective varieties](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/projective-varieties-and-bezouts-theorem.md) and of [elliptic curves](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/elliptic-curves.md), whose point at infinity is the identity of the group law. Computer graphics uses homogeneous coordinates so that translation and perspective become matrices ([geometry and transformations](../../../cs-first-principles/14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md)), and a camera is a projective map ([computer vision](../../../cs-first-principles/14-human-and-visual-computing/03-media-and-vision/computer-vision.md)).
- **Siblings:** [The Erlangen programme](the-erlangen-programme.md) puts the projective group at the top of a chain of geometries, and the Klein disc of [non-Euclidean geometry](non-euclidean-geometry.md) is projective.

## Common misconceptions

- **"Points at infinity are a convenient fiction"**: In ℝP² they are ordinary points, and a projective map can send the line at infinity to any other line.
- **"Projective geometry has no metric content"**: Cayley and Klein recovered Euclidean and hyperbolic distance by fixing a conic and measuring with the cross-ratio.
- **"Desargues' theorem is just a fact of plane geometry"**: It cannot be proved from the plane incidence axioms; non-Desarguesian planes exist, and it holds only when the plane sits in a larger space or has division-ring coordinates.

## Go deeper

- Coxeter, *Projective Geometry*: the classical synthetic treatment, short and elegant.
- Richter-Gebert, *Perspectives on Projective Geometry* (2011): modern, with cross-ratios, conics and computation.
- Stillwell, *The Four Pillars of Geometry* (2005): a gentle route from perspective to coordinates and the Pappus–Desargues story.
