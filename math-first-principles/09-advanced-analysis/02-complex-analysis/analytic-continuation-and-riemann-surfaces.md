# Analytic Continuation and Riemann Surfaces

> **Layer:** [09 Advanced Analysis](../README.md) › [Complex Analysis](README.md)
> **Builds on:** [Cauchy's Theorem and Its Consequences](cauchys-theorem-and-its-consequences.md), [Conformal Maps and the Riemann Mapping Theorem](conformal-maps-and-the-riemann-mapping-theorem.md), [Covering Spaces](../../07-topology/02-algebraic-topology/covering-spaces.md), [Topological and Smooth Manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md), [Classification of Surfaces](../../07-topology/03-manifolds/classification-of-surfaces.md)
> **Enables:** [The Riemann Zeta Function](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md), [Algebraic Curves and Riemann–Roch](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/algebraic-curves-and-riemann-roch.md), [Elliptic Curves](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/elliptic-curves.md)

## Essence

Because a holomorphic function is determined by its values on any small disc, a power series converging near one point can have at most one holomorphic extension along a given path. Following it around different paths, however, can give different answers: the logarithm gains 2πi each time it circles the origin, and the square root changes sign. Riemann's idea was to build the surface on which they are single-valued. The result is the Riemann surface, a one-dimensional complex manifold. Compact Riemann surfaces turn out to be the same thing as algebraic curves.

## Core tenets

1. **Continuation is unique where it exists.** If f and g are holomorphic on a connected open set and agree on a small disc, they agree everywhere, by the identity theorem: the set where all derivatives of f − g vanish is open, closed and non-empty. So an analytic continuation of a function element (a disc with a power series on it) to a larger connected domain is unique if it exists.

2. **Continuation along a path can depend on the path.** Continue a function element along a curve by a chain of overlapping discs; by uniqueness, the result depends only on the path. Start with the branch of log z near 1 with log 1 = 0 and continue around the unit circle: since d(log z) = dz/z and ∮ dz/z = 2πi, one returns with log 1 = 2πi. Likewise √z returns as −√z after one circuit and as itself after two. Points like 0, around which continuation is multivalued, are branch points.

3. **The monodromy theorem: homotopic paths give the same continuation.** If a function element can be continued along every path in a domain U, and two paths with the same endpoints are homotopic in U, then the two continuations agree. Proof idea: along a continuous deformation the result is locally constant, because continuations along nearby paths share their discs. Hence on a simply connected domain, unrestricted continuation yields a single-valued function, which is why log z has a single-valued branch on ℂ minus a ray. The failure of single-valuedness is measured by the [fundamental group](../../07-topology/02-algebraic-topology/homotopy-and-the-fundamental-group.md): the monodromy of log around 0 is the homomorphism from π₁(ℂ ∖ {0}) = ℤ that sends a loop to its winding number times 2πi.

4. **Multivalued functions become single-valued on covering spaces.** The map exp : ℂ → ℂ ∖ {0} is a [covering map](../../07-topology/02-algebraic-topology/covering-spaces.md), indeed the universal cover, and log is a genuine function on it: each point of ℂ is a choice of a value of the logarithm. For √z, take two copies of the plane cut along the negative real axis and glue each upper edge to the other copy's lower edge. The result is a two-sheeted cover of ℂ ∖ {0}, branched at 0, on which √z is single-valued.

5. **A Riemann surface is a connected complex manifold of dimension one.** It is a connected Hausdorff space covered by charts to open sets of ℂ whose transition maps are holomorphic. Examples are ℂ, the Riemann sphere and every domain in ℂ. Holomorphic maps preserve orientation, so compact Riemann surfaces are spheres with g handles, by the [classification of surfaces](../../07-topology/03-manifolds/classification-of-surfaces.md).

6. **Compact Riemann surfaces are algebraic curves.** The surface of w² = (z − e₁)(z − e₂)(z − e₃), with distinct eᵢ, is a two-sheeted cover of the sphere branched at e₁, e₂, e₃ and ∞. It is a torus, the complex points of an [elliptic curve](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/elliptic-curves.md), conformally a quotient ℂ/Λ by a lattice. In general every compact Riemann surface carries enough meromorphic functions to embed it in projective space as a smooth algebraic curve. The existence of those functions is proved analytically, and [Riemann–Roch](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/algebraic-curves-and-riemann-roch.md) counts them.

7. **Uniformisation: only three simply connected Riemann surfaces exist.** Every simply connected Riemann surface is biholomorphic to exactly one of the Riemann sphere, the plane ℂ or the disc 𝔻. Koebe and Poincaré proved it independently in 1907. Every Riemann surface is therefore a quotient of one of these three by deck transformations. Compact surfaces of genus 0 are the sphere, of genus 1 are ℂ/Λ, and of genus at least 2 are quotients of the disc by a group of hyperbolic isometries, so they carry a hyperbolic metric.

8. **Continuation can be blocked, or can reveal deep structure.** The series ∑ z^(2ⁿ) converges on 𝔻, but it tends to infinity along a dense set of radii, at every root of unity of order a power of 2, so the unit circle is a natural boundary across which no continuation exists. In the other direction, the zeta function ∑ n^(−s), defined for Re s > 1, continues to a meromorphic function on all of ℂ with a single pole at s = 1; Riemann proved this in 1859, and the location of the zeros of the continued function is the [Riemann hypothesis](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md), open as of 2026.

## Key concepts

| Term | Meaning |
|---|---|
| Function element | A disc together with a convergent power series on it |
| Analytic continuation | A holomorphic extension of a function element to a larger domain or along a path |
| Branch point | A point around which continuation returns a different value |
| Monodromy | The change in a continued function after a loop, as a map from π₁ |
| Monodromy theorem | Homotopic paths give the same continuation |
| Riemann surface | A connected one-dimensional complex manifold |
| Genus | The number of handles of a compact surface |
| Uniformisation theorem | Every simply connected Riemann surface is the sphere, ℂ or 𝔻 |
| Natural boundary | A curve across which no continuation is possible |

## How it fits

- **Below:** [covering spaces](../../07-topology/02-algebraic-topology/covering-spaces.md) and the [fundamental group](../../07-topology/02-algebraic-topology/homotopy-and-the-fundamental-group.md) in 07 describe the global behaviour; [manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md) supply the definition; [Cauchy's theorem](cauchys-theorem-and-its-consequences.md) and the identity theorem supply the uniqueness.
- **Above:** [zeta](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md) and L-functions are known through their continuations; [algebraic curves](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/algebraic-curves-and-riemann-roch.md) and [elliptic curves](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/elliptic-curves.md) in 12 are compact Riemann surfaces.
- **Siblings:** [conformal maps](conformal-maps-and-the-riemann-mapping-theorem.md) give the planar case of uniformisation; [Hilbert spaces](../03-functional-analysis/hilbert-spaces.md) give a modern proof that Riemann surfaces carry functions.

## Common misconceptions

- **"log z is not a function"**: it is a perfectly good function on the right surface, the universal cover of ℂ ∖ {0}; the problem is only the choice of domain.
- **"ζ(−1) = −1/12 means 1 + 2 + 3 + ⋯ = −1/12"**: the series diverges at −1; −1/12 is the value of the continuation, not a sum.

## Go deeper

- Otto Forster, *Lectures on Riemann Surfaces* (1981): coverings, sheaves and the existence of meromorphic functions.
- Tristan Needham, *Visual Complex Analysis* (1997): branch points and multivalued functions in pictures.
