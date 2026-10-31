# Complex Dynamics

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Dynamical Systems](README.md)
> **Builds on:** [Iterated maps](iterated-maps.md), [Holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md), [Conformal maps and the Riemann mapping theorem](../../09-advanced-analysis/02-complex-analysis/conformal-maps-and-the-riemann-mapping-theorem.md), [Hausdorff dimension and fractals](../../09-advanced-analysis/01-measure-and-integration/hausdorff-dimension-and-fractals.md)
> **Enables:** [Root-finding and Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md), [Computers and proof](../../15-mathematics-in-context/computers-and-proof.md), [Open problems](../../15-mathematics-in-context/open-problems.md)

## Essence

Iterate a polynomial such as z ↦ z² + c on the complex plane. Most starting points settle into regular behaviour or escape to infinity, and the boundary between the two, the Julia set, is usually a fractal on which the map is chaotic. Pierre Fatou and Gaston Julia, working independently around 1918, built the theory on Paul Montel's normal families, long before computers could draw the sets. Collecting the parameters c whose Julia set is connected gives the Mandelbrot set, and Adrien Douady and John Hubbard showed in the 1980s that its structure is governed by the same conformal maps that classify simply connected domains.

## Core tenets

1. **The plane splits into a stable Fatou set and a chaotic Julia set.** For a polynomial or rational map f of degree d ≥ 2, the Fatou set is where the iterates fⁿ form a normal family: every sequence of them has a locally uniformly convergent subsequence. The Julia set J is its complement. Both are mapped onto themselves by f and by f⁻¹. For z², J is the unit circle: orbits inside tend to 0, outside to ∞, and on the circle the map doubles angles, the coin-tossing shift of the [logistic map at r = 4](iterated-maps.md).

2. **The Julia set is where small regions blow up.** By Montel's theorem, a family of holomorphic maps omitting two values is normal. So near any point of J the iterates of a small disc cover the whole plane except at most one point. From this J is non-empty, closed, has no isolated points, and is the closure of the repelling periodic points, those whose cycle has multiplier of modulus greater than 1.

3. **Each attracting cycle captures a critical point.** Fatou showed that the immediate basin of an attracting cycle contains a critical point, where f′ = 0. Proof idea: otherwise a branch of the inverse fixing the cycle would map the basin into itself, and by Schwarz's lemma could not expand, yet at the cycle it expands by the reciprocal of the multiplier. So z² + c, with its one critical point 0, has at most one attracting cycle, and the orbit of 0 finds it.

4. **The orbit of 0 decides whether the Julia set is connected.** For f(z) = z² + c, either the orbit of 0 stays bounded and the filled Julia set K, the points with bounded orbit, is connected, or 0 escapes and J = K is a Cantor set. Proof idea: near ∞, Böttcher's coordinate φ conjugates f to z ↦ z². It extends inwards along level curves of escape rate until it meets the critical point. If 0 never escapes, φ is a Riemann map from the complement of K onto the complement of the closed unit disc, so K is connected; if 0 escapes, the level curve through it is a figure eight, and K splits into two pieces, each again into two, and so on.

5. **The Mandelbrot set is connected.** Let M be the set of c for which the orbit of 0 stays bounded, named by Douady and Hubbard after Benoit Mandelbrot; it lies in the disc ∣c∣ ≤ 2. Its main cardioid, the c = μ/2 − μ²/4 with ∣μ∣ < 1, is where z² + c has an attracting fixed point of multiplier μ, and the disc ∣c + 1∣ < 1/4 is where it has an attracting 2-cycle. Douady and Hubbard (1982) proved M connected: the Böttcher coordinate of the critical value, Φ(c) = φ_c(c), maps the complement of M conformally onto the complement of the closed unit disc.

6. **The real line of M is the logistic family.** The substitution c = r/2 − r²/4 makes z² + c conjugate to r·x(1 − x), so r = 3 corresponds to c = −3/4, where the cardioid meets the 2-cycle disc, and r = 4 to c = −2, the tip of M, where J = [−2, 2]. The period-doubling cascade is the chain of components along the real axis.

7. **The Fatou set has no wandering domains.** Dennis Sullivan (1985) proved that every Fatou component of a rational map is eventually periodic, using quasiconformal deformations: a wandering domain would yield infinitely many independent deformations, but maps of fixed degree form a finite-dimensional family. Periodic components are then attracting basins, parabolic basins, Siegel discs or Herman rings, the last impossible for polynomials.

8. **The boundary of M is as rough as possible.** Mitsuhiro Shishikura (1998) proved that ∂M has [Hausdorff dimension](../../09-advanced-analysis/01-measure-and-integration/hausdorff-dimension-and-fractals.md) 2. Whether M is locally connected, the Mandelbrot locally connected (MLC) conjecture, is open as of 2026; it would imply that hyperbolic parameters, those with an attracting cycle, are dense in M, also open as of 2026. Jean-Christophe Yoccoz proved local connectivity at every parameter that is not infinitely renormalisable; the real case of density was proved by Jacek Graczyk and Grzegorz Świątek and by Mikhail Lyubich (1997).

## Key concepts

| Term | Meaning |
|---|---|
| Fatou set | Where the iterates form a normal family; stable behaviour |
| Julia set J | The complement of the Fatou set; the closure of the repelling periodic points |
| Mandelbrot set M | The c for which the orbit of 0 under z² + c stays bounded |
| Böttcher coordinate | The change of variable near ∞ conjugating z² + c to z² |
| Hyperbolic map | A map whose critical points all tend to attracting cycles |

## How it fits

- **Below:** [iterated maps](iterated-maps.md) supply multipliers and the logistic family; [holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md) supply Montel and Schwarz; [conformal maps](../../09-advanced-analysis/02-complex-analysis/conformal-maps-and-the-riemann-mapping-theorem.md) supply the Riemann maps of tenets 4 and 5; [Hausdorff dimension](../../09-advanced-analysis/01-measure-and-integration/hausdorff-dimension-and-fractals.md) measures ∂M.
- **Above:** [Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md) for z³ − 1 has three basins whose common boundary is a Julia set, so every boundary point touches all three; computer pictures guided the subject, a theme of [computers and proof](../../15-mathematics-in-context/computers-and-proof.md); MLC is among the [open problems](../../15-mathematics-in-context/open-problems.md).
- **Siblings:** [chaos](chaos-and-strange-attractors.md) on J is the expanding kind; [bifurcations](bifurcations.md) of z² + c occur on ∂M; [ergodic theory](ergodic-theory.md) gives J its natural measure, the harmonic measure seen from ∞.

## Common misconceptions

- **"The Mandelbrot set is self-similar"**: small copies of M appear throughout it, but distorted and differently decorated; M is only approximately self-similar near certain points.
- **"The pictures show the Julia set is a solid region"**: J has empty interior unless it is the whole sphere; the coloured regions are escape-time bands in the Fatou set.

## Go deeper

- John Milnor, *Dynamics in One Complex Variable* (3rd edition, 2006): the standard text, from Montel's theorem to the Mandelbrot set.
- Lennart Carleson and Theodore W. Gamelin, *Complex Dynamics* (1993): a short, proof-driven account including Sullivan's theorem.
