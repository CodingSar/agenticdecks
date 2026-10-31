# Modelling and Dimensional Analysis

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Mathematical Modelling](README.md)
> **Builds on:** [Linear Systems and Rank–Nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md), [Existence and Uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md), [Chaos and Strange Attractors](../../10-differential-equations-and-dynamics/04-dynamical-systems/chaos-and-strange-attractors.md), [Floating Point, Conditioning and Stability](../01-numerical-analysis/floating-point-conditioning-and-stability.md)
> **Enables:** [Control Theory](control-theory.md), [Mathematical Biology and Epidemics](mathematical-biology-and-epidemics.md), [Mathematical Practice and Discovery](../../15-mathematics-in-context/mathematical-practice-and-discovery.md), [The Scientific Method and Models (Medicine)](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/03-systems-and-models/the-scientific-method-and-models.md)

## Essence

A mathematical model replaces a system by equations whose solutions can be compared with measurement. Modelling is a cycle: idealise, write down the laws, simplify by scaling, solve, test against data the model was not built from, and revise. Its most reliable tool is dimensional analysis. A physical law cannot depend on the arbitrary choice of units, so it must be a relation among dimensionless combinations of its variables; the Buckingham π theorem counts those combinations by linear algebra, and rescaling shows which terms are small enough to drop. Every model also has a domain of validity and a horizon of prediction.

## Core tenets

1. **Modelling is a cycle, not a derivation.** Idealise (choose the variables, ignore the rest), formulate (conservation laws plus constitutive assumptions), analyse, validate against data, and revise. The first and last steps are not mathematics, yet they decide whether the mathematics means anything.

2. **Physical laws are dimensionally homogeneous.** Every term of a valid equation carries the same dimension in the base quantities mass M, length L and time T, because only then does the equation survive a change of units. "Distance equals time" might hold in metres and seconds, but not in feet and seconds. This one hypothesis drives everything below.

3. **The Buckingham π theorem: if n quantities have a dimension matrix of rank r, any homogeneous law relating them is a relation among n − r independent dimensionless groups.** Record each quantity's dimension as a column of exponents. A product q₁^(a₁)⋯qₙ^(aₙ) is dimensionless exactly when the exponent vector a lies in the kernel of this matrix, which by rank–nullity has dimension n − r. Resizing the base units acts on the quantities as a group of rescalings, and a law invariant under that group can depend only on its invariants, the π groups. Edgar Buckingham stated it in 1914.

4. **Dimensional analysis alone can fix the form of a law.** The period τ of a pendulum might depend on its length l, gravitational acceleration g, mass m and release angle θ₀:

   ```
               τ    l    g    m    θ₀
      M        0    0    0    1    0
      L        0    1    1    0    0
      T        1    0   −2    0    0

      5 quantities, rank 3  →  2 groups:  τ·√(g/l)  and  θ₀
      law:  τ = √(l/g) · Φ(θ₀)
   ```

   Mass cannot appear, since nothing else carries M, and quadrupling the length doubles the period. The method cannot supply Φ: the small-angle value Φ(0) = 2π needs the differential equation.

5. **Systems with equal π groups behave alike.** The Reynolds number Re = ρUL/μ (density times speed times length over viscosity) measures inertia against friction. Two flows of the same shape and the same Re have the same pattern in scaled variables, so a wind-tunnel model predicts the full-size aircraft, but only if every relevant group matches.

6. **Scaling exposes the small parameter, and dropping it can go wrong.** After rescaling, a coefficient ε ≪ 1 marks a term that looks negligible. If setting ε = 0 keeps the order of the equation, the perturbation is regular and the solution is a power series in ε. If ε multiplies the highest derivative, setting it to zero lowers the order and some boundary condition can no longer be met: the perturbation is singular. In ε·y″ + y′ + y = 0 with y(0) = 0 and y(1) = 1, the reduced equation fits only y(1), and a boundary layer of width about ε forms at x = 0. Prandtl's boundary layer (1904) is the founding case: viscosity is negligible in the bulk of a flow but not next to a wall.

7. **Validation needs predictions on unseen data and identifiable parameters.** A model with enough parameters fits any finite data set, so a good fit proves little. Parameters are identifiable only if different values give different observable outputs. Sensitivity analysis, the modelling form of a condition number, asks how far each output moves when each parameter moves.

8. **Every model has a domain of validity and a prediction horizon.** Newtonian mechanics fails near the speed of light; the ideal gas law fails at high density. Inside its domain a chaotic model still loses track: an initial error δ grows like δ·e^(λt), with λ the largest Lyapunov exponent, so it reaches a tolerance Δ after time (1/λ)·ln(Δ/δ). Measuring ten times more accurately buys only ln(10)/λ more. Edward Lorenz found this in a weather model in 1963.

## Key concepts

| Term | Meaning |
|---|---|
| Dimensional homogeneity | Every term of an equation has the same dimension |
| Dimension matrix | Base dimensions by quantities; its kernel gives the dimensionless products |
| π group | A dimensionless product of powers of the model's quantities |
| Similarity | Equal π groups imply equal behaviour in scaled variables |
| Singular perturbation | A small parameter multiplying the highest derivative, producing a boundary layer |
| Identifiability | Distinct parameter values produce distinct observable outputs |
| Lyapunov exponent | The exponential rate at which nearby trajectories separate |

## How it fits

- **Below:** rank–nullity counts the π groups; existence and uniqueness make a model define one prediction, and chaos limits how far ahead it reaches. Conditioning is the same question as sensitivity, asked of an algorithm.
- **Above:** [mathematical practice](../../15-mathematics-in-context/mathematical-practice-and-discovery.md) and the [philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md) ask why such models work as well as they do.
- **Siblings:** [control theory](control-theory.md) and [mathematical biology](mathematical-biology-and-epidemics.md) run this cycle on engineered and living systems. [Quantum mechanics](the-mathematics-of-quantum-mechanics.md) and [general relativity](the-geometry-of-general-relativity.md) are fundamental theories, yet dimensional analysis still marks where both are needed at once: ħ, G and c combine into the Planck length √(ħG/c³) ≈ 1.6 × 10⁻³⁵ m.

## Common misconceptions

- **"Dimensional analysis gives the whole answer."** It gives the form up to an unknown function of the π groups, never constants such as 2π, and it fails silently if a relevant quantity is left out.
- **"A model that fits the data is validated."** Only predictions of new observations test a model.
- **"A small term can always be neglected."** When the small parameter multiplies the highest derivative, dropping it changes the character of the solution.

## Go deeper

- C. C. Lin and L. A. Segel, *Mathematics Applied to Deterministic Problems in the Natural Sciences* (1974): the classic on the modelling cycle, scaling and perturbation.
- G. I. Barenblatt, *Scaling, Self-Similarity, and Intermediate Asymptotics* (1996): dimensional analysis pushed to its limits, including where it fails.
- C. M. Bender and S. A. Orszag, *Advanced Mathematical Methods for Scientists and Engineers* (1978): perturbation theory and boundary layers in full.
