# The Geometry of General Relativity

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Mathematical Modelling](README.md)
> **Builds on:** [Riemannian Manifolds](../../08-geometry/02-differential-geometry/riemannian-manifolds.md), [Topological and Smooth Manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md), [The Euler–Lagrange Equation](../../10-differential-equations-and-dynamics/03-calculus-of-variations/the-euler-lagrange-equation.md), [Nonlinear PDEs](../../10-differential-equations-and-dynamics/02-partial-differential-equations/nonlinear-pdes.md)
> **Enables:** [Numerical Methods for Differential Equations](../01-numerical-analysis/numerical-methods-for-differential-equations.md), [History of Mathematics](../../15-mathematics-in-context/history-of-mathematics.md), [Philosophy of Mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md)

## Essence

General relativity, completed by Albert Einstein in November 1915, says that gravity is not a force but the curvature of spacetime. Spacetime is a four-dimensional manifold with a Lorentzian metric, one whose inner product has signature (−, +, +, +), so that each tangent space carries a light cone separating past, future and elsewhere. Freely falling bodies follow geodesics, and matter curves the metric through the Einstein field equations, a system of nonlinear partial differential equations (PDEs). The theory is geometry made predictive: it explains Mercury's orbit, the bending of light, black holes and gravitational waves. It also predicts its own breakdown, since the singularity theorems show that under mild energy conditions spacetime must end at singularities.

## Core tenets

1. **A Lorentzian metric gives every point a light cone.** A tangent vector v is timelike, null or spacelike as g(v, v) is negative, zero or positive. Massive particles travel along timelike curves, light along null curves, and the cones fix which events can influence which. The clock reading along a timelike curve is its proper time, τ = ∫ √(−g(γ′, γ′)) dt, in units with c = 1.

2. **Free fall is geodesic motion, and timelike geodesics locally maximise proper time.** Applying the Euler–Lagrange equation to proper time gives the geodesic equation. Because of the minus sign, the straight line is the longest timelike path between nearby events, not the shortest: in the twin paradox, the twin who stays in free fall ages most. The equivalence principle, that all bodies fall alike, becomes the statement that the path depends only on the geometry.

3. **Tidal force is curvature.** Two neighbouring free-falling particles separate according to the geodesic deviation equation, D²J/dτ² = −R(J, u)u, where R is the Riemann curvature, u the velocity and J the separation. Gravity cannot be removed by choosing coordinates, as a uniform field can, exactly when R ≠ 0.

4. **The field equations are the simplest ones compatible with conservation.** Einstein's equations read

   ```
   G_μν + Λ g_μν = (8πG / c⁴) T_μν,      G_μν = R_μν − ½ R g_μν
   ```

   with Ricci curvature R_μν, scalar curvature R, cosmological constant Λ and stress–energy T_μν. The contracted Bianchi identity makes G divergence-free, matching local conservation of energy and momentum, ∇^μ T_μν = 0. Lovelock's theorem says that in four dimensions the combinations aG + bg are the only divergence-free symmetric tensors built from the metric and its first two derivatives, and Hilbert obtained the same equations from the action ∫ R √(−det g) d⁴x. For weak, slow fields the equations reduce to Newton's ∇²Φ = 4πGρ.

5. **Coordinates are gauge, and the equations are well posed once a gauge is fixed.** Diffeomorphism invariance means four of the ten equations are constraints on initial data rather than evolution equations. In harmonic coordinates the system becomes a set of nonlinear wave equations, and Yvonne Choquet-Bruhat (1952) proved that suitable initial data have a unique local solution. Numerical relativity builds on this formulation.

6. **The Schwarzschild solution describes every spherical vacuum and contains a black hole.** Karl Schwarzschild found it in 1916:

   ```
   ds² = −(1 − r_s/r) c² dt² + (1 − r_s/r)⁻¹ dr² + r² dΩ²,    r_s = 2GM/c²
   ```

   Birkhoff's theorem says any spherically symmetric vacuum solution is locally of this form, so a pulsating spherical star emits no gravitational waves. At r = r_s only the coordinates fail: other coordinates continue smoothly through this event horizon. At r = 0 the invariant R_abcd R^abcd = 12 r_s²/r⁶ blows up, so the singularity there is real.

7. **The predictions have been measured precisely.** The theory gives Mercury's anomalous perihelion advance of 43″ per century and starlight bending of 1.75″ at the Sun's edge (tested in 1919). Satellite clocks of the Global Positioning System (GPS) gain about 38 microseconds a day relative to the ground. The Laser Interferometer Gravitational-Wave Observatory (LIGO) detected gravitational waves from merging black holes on 14 September 2015, and the Event Horizon Telescope published an image of a black hole's shadow in 2019.

8. **Singularities are generic (Penrose, 1965).** If spacetime has a non-compact Cauchy surface, contains a closed trapped surface (one from which even outgoing light converges), and satisfies the null energy condition R_μν k^μ k^ν ≥ 0 for null k, then some null geodesic ends after finite affine parameter. Proof idea: the Raychaudhuri equation forces light rays from the trapped surface to focus, which makes the boundary of its future compact, and that is incompatible with a non-compact Cauchy surface. Hawking and Penrose extended this in 1970. Whether singularities are generically hidden behind horizons (cosmic censorship) is open as of 2026.

## Key concepts

| Term | Meaning |
|---|---|
| Lorentzian metric | A smooth symmetric bilinear form of signature (−, +, +, +) on each tangent space |
| Proper time | Elapsed time along a timelike curve, as read by a clock carried on it |
| Geodesic | A curve with zero covariant acceleration; the path of free fall |
| Riemann tensor | The curvature measuring how parallel transport fails to commute; tidal force |
| Einstein tensor G_μν | Ricci curvature minus half its trace times g; divergence-free |
| Stress–energy tensor T_μν | Density and flux of energy and momentum of matter |
| Event horizon | Boundary of the region from which no signal reaches distant observers |
| Trapped surface | A closed surface whose outgoing and ingoing light rays both converge |

## How it fits

- **Below:** Riemannian geometry supplies connections and curvature, now with an indefinite metric; manifold theory supplies the stage; the calculus of variations gives geodesics and the Hilbert action; nonlinear PDE theory handles the Cauchy problem.
- **Above:** [numerical methods](../01-numerical-analysis/numerical-methods-for-differential-equations.md) simulate black-hole mergers; the [history of mathematics](../../15-mathematics-in-context/history-of-mathematics.md) records how Riemann's geometry of 1854 became physics sixty years later.
- **Siblings:** [quantum mechanics](the-mathematics-of-quantum-mechanics.md) is the other fundamental theory, and reconciling the two is open as of 2026. [Modelling](modelling-and-dimensional-analysis.md) shows Newtonian gravity as the small-parameter limit GM/(rc²) → 0.

## Common misconceptions

- **"The event horizon is a singularity."** It is a coordinate artefact at r = r_s; curvature there is finite, and for a large black hole an infalling observer notices nothing special.
- **"Relativity says everything is relative."** Its content lies in invariants: proper time, the light cones and curvature are the same for every observer.
- **"Free fall is motion under a force."** A falling body feels no force; it follows the straightest available path through curved spacetime.

## Go deeper

- C. W. Misner, K. S. Thorne and J. A. Wheeler, *Gravitation* (1973): the encyclopaedic classic with strong geometric intuition.
- R. M. Wald, *General Relativity* (1984): the mathematically careful standard, including the singularity theorems.
- S. M. Carroll, *Spacetime and Geometry* (2004): a gentler modern introduction.
