# Weak Solutions and Sobolev Spaces

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Partial Differential Equations](README.md)
> **Builds on:** [Distributions](../../09-advanced-analysis/04-harmonic-analysis/distributions.md), [Lp spaces](../../09-advanced-analysis/01-measure-and-integration/lp-spaces.md), [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md), [Laplace's equation and harmonic functions](laplaces-equation-and-harmonic-functions.md), [First-order equations and characteristics](first-order-equations-and-characteristics.md)
> **Enables:** [Nonlinear partial differential equations](nonlinear-pdes.md), [Existence of minimisers](../03-calculus-of-variations/existence-of-minimisers.md), [Numerical methods for differential equations](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md), [The mathematics of quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md)

## Essence

Looking directly for twice-differentiable solutions of a partial differential equation (PDE) usually fails: the natural spaces of smooth functions are not complete for the right norms, and the solutions often are not smooth. The modern method splits the problem in two. First find a weak solution, one satisfying an integrated form of the equation, in a Sobolev space: a complete space of functions whose derivatives, taken in the integrated sense, are square integrable or Lᵖ. Hilbert-space tools such as the Lax–Milgram theorem make this step almost automatic. Then prove regularity: that the weak solution is in fact smooth. Sobolev embedding converts integral bounds into pointwise ones.

## Core tenets

1. **Classical solutions are too few.** Poisson's equation −Δu = f with f merely continuous need not have any C² solution; Hölder continuity of f is what the classical theory needs. Minimising the Dirichlet energy ∫|∇u|² over C² functions can fail because minimising sequences converge to something outside the space. Shocks in conservation laws are a third failure. The cure in each case is to ask less of a solution and to work in a complete space.

2. **Weak derivatives define integration by parts as the rule.** A function v is the weak derivative of u if ∫u·φ′ = −∫v·φ for every smooth φ vanishing outside a compact set. So |x| has weak derivative sign x, while sign x has none that is a function: its derivative is the distribution 2δ. The Sobolev space W^(k,p)(Ω) holds the functions in Lᵖ whose weak derivatives up to order k are in Lᵖ, and it is complete because Lᵖ is. H^k = W^(k,2) is a Hilbert space, and H¹₀(Ω), the closure of the smooth compactly supported functions in H¹, holds the functions that vanish on the boundary.

3. **The weak formulation needs one derivative, not two.** Multiplying −Δu = f by v ∈ H¹₀(Ω) and integrating by parts gives

   ```
   ∫ over Ω of ∇u·∇v dx  =  ∫ over Ω of f·v dx     for every v ∈ H¹₀(Ω).
   ```

   Every classical solution satisfies this, and a weak solution that happens to be C² is classical, so nothing is lost; but the problem is now posed in a Hilbert space.

4. **Lax–Milgram theorem (1954).** Let H be a real Hilbert space, a a bilinear form on H that is bounded, |a(u, v)| ≤ C·‖u‖·‖v‖, and coercive, a(u, u) ≥ α‖u‖² with α > 0, and ℓ a bounded linear functional. Then exactly one u ∈ H satisfies a(u, v) = ℓ(v) for all v, and ‖u‖ ≤ ‖ℓ‖/α. For symmetric a this is the Riesz representation theorem in the inner product a(u, v). For the Dirichlet problem, coercivity is the Poincaré inequality ∫u² ≤ C·∫|∇u|² on a bounded region. Without coercivity it fails: −Δu − λu = f with λ a Dirichlet eigenvalue is not solvable for every f.

5. **Sobolev embedding turns integral control into pointwise control.** In one dimension u(y) − u(x) = ∫ from x to y of u′, and the Cauchy–Schwarz inequality gives |u(y) − u(x)| ≤ |y − x|^(1/2)·‖u′‖, so H¹ functions are Hölder continuous. On a bounded region with smooth boundary in ℝⁿ, W^(k,p) lies inside C^m when k − n/p > m, and H^k consists of continuous functions when k > n/2. At the borderline it fails: in the plane u = log log(1/|x|) has ∫|∇u|² = 2π on the disc |x| < 1/e, yet is unbounded. For p < n, W^(1,p) ⊂ L^(p*) with 1/p* = 1/p − 1/n, the only exponent compatible with rescaling x ↦ λx.

6. **Compactness and regularity finish the job.** On a bounded region the inclusion of H¹₀ in L² is compact (Rellich–Kondrachov theorem): bounded sequences have subsequences converging in L². This gives the Dirichlet Laplacian a discrete spectrum and minimisers their existence; on ℝⁿ it fails, as translates of one bump show. Elliptic regularity then gains two derivatives, f ∈ H^k giving u ∈ H^(k+2) inside Ω, so smooth f give smooth u. For coefficients that are only bounded and measurable, De Giorgi (1957) and Nash (1958) independently proved weak solutions Hölder continuous.

7. **Weak formulations are what computers solve.** Galerkin's method restricts the weak formulation to a finite-dimensional subspace. With piecewise polynomials on a mesh this is the finite element method, and Céa's lemma bounds the error by C/α times the best approximation error available in the subspace.

## Key concepts

| Term | Meaning |
|---|---|
| Classical solution | One whose derivatives in the equation exist and are continuous |
| Test function | A smooth function vanishing outside a compact subset of Ω |
| Weak derivative | v with ∫u·∂φ = −∫v·φ for every test function φ |
| Sobolev space | W^(k,p): functions in Lᵖ with weak derivatives up to order k in Lᵖ; H^k = W^(k,2) |
| Coercive form | a(u, u) ≥ α‖u‖² for a fixed α > 0 |
| Sobolev embedding | The inclusion of a Sobolev space in a space of continuous or more integrable functions |
| Elliptic regularity | The gain of two derivatives from data to solution |
| Galerkin method | Solving the weak formulation on a finite-dimensional subspace |

## How it fits

- **Below:** [distributions](../../09-advanced-analysis/04-harmonic-analysis/distributions.md) supply weak derivatives, [Lp spaces](../../09-advanced-analysis/01-measure-and-integration/lp-spaces.md) and [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md) supply completeness and the Riesz theorem; the model problem is the Dirichlet problem of [Laplace's equation](laplaces-equation-and-harmonic-functions.md), and weak [conservation laws](first-order-equations-and-characteristics.md) were the first weak solutions.
- **Above:** [finite elements](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md) are tenet 7; Schrödinger operators in [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) live on Sobolev domains; [existence of minimisers](../03-calculus-of-variations/existence-of-minimisers.md) uses Rellich compactness.
- **Siblings:** [nonlinear PDEs](nonlinear-pdes.md) work in H^s with s > n/2, where products are controlled; the [heat](the-heat-equation.md) and [wave](the-wave-equation.md) equations have weak formulations and energy estimates in the same spaces.

## Common misconceptions

- **"A weak solution is an approximate solution."**: it solves an equivalent integrated statement exactly, and if it is smooth it is classical.
- **"Functions in H¹ are continuous."**: only in one dimension; log log(1/|x|) is an unbounded H¹ function in the plane.
- **"Lax–Milgram solves every linear elliptic problem."**: it needs coercivity, which fails at eigenvalues, where the [Fredholm alternative](../../09-advanced-analysis/03-functional-analysis/compact-operators-and-fredholm-theory.md) takes over.

## Go deeper

- Lawrence C. Evans, *Partial Differential Equations* (2nd edition, 2010): Sobolev spaces, weak solutions and regularity, chapters 5 and 6.
- Haim Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations* (2011): the functional analysis behind the method.
- David Gilbarg and Neil S. Trudinger, *Elliptic Partial Differential Equations of Second Order* (2nd edition, 1983): the standard reference for regularity.
