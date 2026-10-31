# Complex Dynamics

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Dynamical Systems](README.md)
> **Builds on:** [Iterated maps](iterated-maps.md), [Holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md), [Conformal maps and the Riemann mapping theorem](../../09-advanced-analysis/02-complex-analysis/conformal-maps-and-the-riemann-mapping-theorem.md), [Hausdorff dimension and fractals](../../09-advanced-analysis/01-measure-and-integration/hausdorff-dimension-and-fractals.md)
> **Enables:** [Root-finding and Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md), [Computers and proof](../../15-mathematics-in-context/computers-and-proof.md), [Open problems](../../15-mathematics-in-context/open-problems.md)

## Essence

Iterate a polynomial such as z ↦ z² + c on the complex plane. Most starting points either settle into regular behaviour or escape to infinity, and the boundary between the two kinds, the Julia set, is usually a fractal on which the map is chaotic. Pierre Fatou and Gaston Julia, working independently around 1918, built the theory on Paul Montel's normal families, decades before computers could draw the sets. Collecting the parameters c whose Julia set is connected gives the Mandelbrot set, and Adrien Douady and John Hubbard showed in the 1980s that its structure is governed by the same conformal maps that classify simply connected domains. Because the maps are holomorphic, rigidity results from complex analysis turn pictures into theorems.

## Core tenets

1. **The plane splits into a stable Fatou set and a chaotic Julia set.** For a polynomial or rational map f of degree d ≥ 2, the Fatou set is where the iterates fⁿ form a normal family: every sequence of them has a locally uniformly convergent subsequence. The Julia set J is its complement. Both are completely invariant, mapped onto themselves by f and by f⁻¹. For z², J is the unit circle: inside, orbits tend to 0; outside, to ∞; on the circle the map doubles angles, which is the coin-tossing shift of the [logistic map at r = 4](iterated-maps.md).

2. **The Julia set is where small regions blow up.** By Montel's theorem, a family of holomorphic maps omitting two values is normal. So near any point of J the iterates of a small disc cover the whole plane except at most one point. From this J is non-empty, closed, has no isolated points, and is the closure of the repelling periodic points, those whose cycle has multiplier of modulus greater than 1. Zooming into J shows the same structure everywhere, since f expands it onto itself.

3. **Each attracting cycle captures a critical point.** Fatou showed that the immediate basin of an attracting cycle contains a critical point, where f′ = 0. Proof idea: otherwise an inverse branch of f could be continued throughout the basin, and Schwarz's lemma would force it to be a non-contracting isometry, contradicting attraction. So z² + c, with its one critical point 0, has at most one attracting cycle, and the orbit of 0 finds it.

4. **The orbit of 0 decides whether the Julia set is connected.** For f(z) = z² + c, either the orbit of 0 stays bounded and the filled Julia set K, the points with bounded orbit, is connected, or 0 escapes and J = K is a Cantor set, a totally disconnected dust. Proof idea: near ∞, Böttcher's coordinate φ conjugates f to z ↦ z². It extends inwards along the level curves of escape rate until it meets the critical point. If 0 never escapes, φ is a Riemann map from the complement of K onto the complement of the closed unit disc, so K is connected; if 0 escapes, the level curve through it is a figure eight, and K splits into two pieces, each again into two, and so on. Any orbit with ∣z∣ > max(2, ∣c∣) escapes, which bounds every connected K.

5. **The Mandelbrot set is connected.** Let M be the set of c for which the orbit of 0 stays bounded; Douady and Hubbard named it after Benoit Mandelbrot. It lies in the disc ∣c∣ ≤ 2. Its main cardioid, the c = μ/2 − μ²/4 with ∣μ∣ < 1, is where z² + c has an attracting fixed point of multiplier μ, and the disc ∣c + 1∣ < 1/4 is where it has an attracting 2-cycle. Douady and Hubbard (1982) proved M connected: Φ(c) = φ_c(c), the Böttcher coordinate of the critical value, is a conformal bijection from the complement of M to the complement of the closed unit disc.

6. **The real line of M is the logistic family.** The substitution c = r/2 − r²/4 makes z² + c conjugate to r·x(1 − x), so r = 3 corresponds to c = −3/4, where the cardioid meets the 2-cycle disc, and r = 4 to c = −2, the tip of M, where J = [−2, 2]. The period-doubling cascade of the logistic map is the chain of discs along the real axis.

7. **The Fatou set has no wandering domains.** Dennis Sullivan (1985) proved that every Fatou component of a rational map is eventually periodic, using quasiconformal deformations: a wandering domain would give an infinite-dimensional family of distinct maps of fixed degree, which form a finite-dimensional family. Periodic components are then attracting basins, parabolic basins, Siegel discs or Herman rings, the last impossible for polynomials.

8. **The boundary of M is as wiggly as a planar set can be.** Mitsuhiro Shishikura (1998) proved that ∂M has [Hausdorff dimension](../../09-advanced-analysis/01-measure-and-integration/hausdorff-dimension-and-fractals.md) 2. Whether M is locally connected, the Mandelbrot locally connected (MLC) conjecture, is open as of 2026; it would imply that hyperbolic parameters, those with an attracting cycle, are dense in M, also open as of 2026. Jean-Christophe Yoccoz proved local connectivity at every parameter that is not infinitely renormalisable, and the real case of density was proved by Jacek Graczyk and Grzegorz Świątek and by Mikhail Lyubich (1997).

## Key concepts

| Term | Meaning |
|---|---|
| Normal family | A family of holomorphic maps in which every sequence has a locally uniformly convergent subsequence |
| Fatou set | Where the iterates form a normal family; stable behaviour |
| Julia set J | The complement of the Fatou set; the closure of the repelling periodic points |
| Filled Julia set K | The points whose orbit under a polynomial stays bounded |
| Mandelbrot set M | The c for which the orbit of 0 under z² + c stays bounded |
| Böttcher coordinate | The change of variable near ∞ conjugating z² + c to z² |
| Hyperbolic map | A map whose critical points all tend to attracting cycles |

## How it fits

- **Below:** [iterated maps](iterated-maps.md) supply multipliers and the logistic family; [holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md) supply Montel's and Schwarz's rigidity; [conformal maps](../../09-advanced-analysis/02-complex-analysis/conformal-maps-and-the-riemann-mapping-theorem.md) supply the Riemann maps behind tenets 4 and 5; [Hausdorff dimension](../../09-advanced-analysis/01-measure-and-integration/hausdorff-dimension-and-fractals.md) measures J and ∂M.
- **Above:** [Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md) for z³ − 1 has three basins whose common boundary is a Julia set, so every boundary point touches all three; computer pictures guided the theory and rigorous numerics now prove facts about it, part of [computers and proof](../../15-mathematics-in-context/computers-and-proof.md); MLC is among the [open problems](../../15-mathematics-in-context/open-problems.md).
- **Siblings:** [chaos](chaos-and-strange-attractors.md) on J is the expanding, coded kind; [bifurcations](bifurcations.md) of z² + c happen at the boundary of M; [ergodic theory](ergodic-theory.md) gives J its natural measure, the harmonic measure seen from ∞.

## Common misconceptions

- **"The Mandelbrot set is self-similar"**: small copies of M appear throughout it, but they are distorted and decorated differently, and M is not exactly similar to any part of itself.
- **"The pictures show the Julia set is a solid region"**: J has empty interior unless it is the whole sphere; the coloured regions are escape-time bands in the Fatou set.
- **"The theory of z² + c is complete"**: local connectivity of M and density of hyperbolicity remain open.

## Go deeper

- John Milnor, *Dynamics in One Complex Variable* (3rd edition, 2006): the standard graduate text, from Montel's theorem to the Mandelbrot set.
- Lennart Carleson and Theodore W. Gamelin, *Complex Dynamics* (1993): a short, proof-driven account including Sullivan's theorem.
- Heinz-Otto Peitgen and Peter H. Richter, *The Beauty of Fractals* (1986): the pictures that brought the subject to a wide audience, with expository essays.
