# Mathematical Biology and Epidemics

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Mathematical Modelling](README.md)
> **Builds on:** [Stability and Phase Portraits](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/stability-and-phase-portraits.md), [Bifurcations](../../10-differential-equations-and-dynamics/04-dynamical-systems/bifurcations.md), [The Heat Equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md), [Markov Chains](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md), [Modelling and Dimensional Analysis](modelling-and-dimensional-analysis.md)
> **Enables:** [Game Theory](../05-games-decisions-and-finance/game-theory.md), [Mathematics and Society](../../15-mathematics-in-context/mathematics-and-society.md), [Infectious Disease Dynamics (Medicine)](../../../medicine-first-principles/10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md), [Natural Selection and Population Genetics (Medicine)](../../../medicine-first-principles/04-genetics-evolution-and-development/02-evolution/natural-selection-and-population-genetics.md)

## Essence

Mathematical biology writes populations, infections and tissues as dynamical systems and asks which qualitative behaviours the mechanisms force: saturation, oscillation, outbreak or pattern. The models are deliberately crude, because their value lies in thresholds and conserved quantities that do not depend on fine detail. Logistic growth explains saturation, the Lotka–Volterra equations explain predator–prey cycles, and the susceptible–infectious–removed (SIR) model of Kermack and McKendrick (1927) explains why an epidemic either fizzles or explodes according to whether one number, R₀, is below or above 1. Turing (1952) showed the most surprising case: diffusion, which smooths everything on its own, can destabilise a stable chemical system and create spots and stripes.

## Core tenets

1. **Growth with a limited resource saturates.** The logistic equation N′ = rN(1 − N/K) (Verhulst, 1838) has an unstable equilibrium at 0 and a stable one at the carrying capacity K, and its solution is an S-shaped curve. The linearisation at each equilibrium decides everything: slope r > 0 at 0, slope −r at K. In discrete time the same law, x_(n+1) = r·x_n(1 − x_n), passes through period doubling into chaos as r rises, which Robert May (1976) urged biologists to take seriously.

2. **Predator–prey cycles come from a conserved quantity, which makes them fragile.** For prey x and predators y, x′ = αx − βxy and y′ = δxy − γy. Differentiating shows that H = δx − γ·ln x + βy − α·ln y is constant along solutions, so every orbit is a closed curve around the equilibrium (γ/δ, α/β). Integrating (ln x)′ = α − βy over one period shows that the average populations equal the equilibrium values. Hence Volterra's principle: moderate fishing of both species raises the average prey and lowers the average predators. Closed orbits are structurally unstable, though: almost any extra term, such as prey self-limitation, turns them into spirals or a limit cycle.

3. **The SIR model has a sharp threshold, R₀ = β/γ.** Susceptible, infectious and removed fractions obey s′ = −βsi, i′ = i(βs − γ), r′ = γi. Infections rise exactly when βs > γ, so a small introduction into a fully susceptible population grows if and only if R₀ = β/γ > 1: R₀ is the mean number of secondary cases from one case. The epidemic peaks when s falls to 1/R₀, and vaccinating a fraction above 1 − 1/R₀ prevents outbreaks. The threshold is the instability of the disease-free equilibrium, read from a linearisation.

4. **The final size solves a transcendental equation, and some people always escape.** Dividing the equations gives ds/dr = −R₀·s, so s = s₀·e^(−R₀r). With s₀ ≈ 1 and r∞ = z, the fraction ever infected satisfies

   ```
   z = 1 − e^(−R₀ z)          R₀ = 2  →  z ≈ 0.797
   ```

   Since e^(−R₀z) > 0, the epidemic ends with susceptibles left: it stops because infectives run out, not susceptibles.

5. **Early in an outbreak, chance matters.** With few cases, the Markov-chain version of SIR is a birth–death process: each infective infects at rate β and recovers at rate γ. Its offspring count is geometric, and the branching-process extinction probability from one case is 1/R₀ when R₀ > 1. Even with R₀ = 2, half of all introductions die out unnoticed; the deterministic model describes only the outbreaks that take off.

6. **Diffusion can create patterns (Turing, 1952).** Add diffusion to two reacting species, u′ = f(u) + D∇²u, with D diagonal. A Fourier mode of wavenumber k evolves by the matrix J − k²D, where J is the Jacobian at a uniform steady state. Suppose the state is stable without diffusion (tr J < 0, det J > 0). Then tr(J − k²D) stays negative, but det(J − k²D) can become negative for a band of k, giving one growing mode and a pattern of wavelength about 2π/k_c. This needs an activator that boosts itself and an inhibitor that diffuses much faster: short-range activation, long-range inhibition. With equal diffusion rates it is impossible.

7. **Structural conclusions outlast numerical ones.** Parameter estimates for real populations are poor, but thresholds, signs and conserved quantities depend only on the form of the model. Policy uses those qualitative facts more reliably than precise forecasts.

## Key concepts

| Term | Meaning |
|---|---|
| Carrying capacity K | The stable population level set by limited resources |
| Lotka–Volterra system | Bilinear predator–prey equations with a conserved quantity |
| Structural stability | Qualitative behaviour survives small changes to the equations |
| SIR model | Compartments susceptible, infectious, removed, with mass-action infection |
| Basic reproduction number R₀ | Mean secondary cases from one case in a fully susceptible population |
| Herd immunity threshold | Immune fraction 1 − 1/R₀ above which outbreaks cannot grow |
| Final-size equation | z = 1 − e^(−R₀z), the fraction ever infected |
| Turing instability | Diffusion destabilising a steady state that is stable without it |

## How it fits

- **Below:** equilibria and linearisation from stability theory, period doubling from bifurcation theory, the heat equation for diffusion, and Markov chains for chance extinction.
- **Above:** [mathematics and society](../../15-mathematics-in-context/mathematics-and-society.md) asks how epidemic projections should inform policy; the medicine tree's [infectious disease dynamics](../../../medicine-first-principles/10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md) applies R₀ clinically.
- **Siblings:** this leaf runs the [modelling](modelling-and-dimensional-analysis.md) cycle on living systems; [control theory](control-theory.md) designs feedback where biology discovers it. Evolutionary [game theory](../05-games-decisions-and-finance/game-theory.md) treats strategies as competing species.

## Common misconceptions

- **"An epidemic stops when everyone has been infected."** It stops when the susceptible fraction falls well below 1/R₀ and infectives run out; the final-size equation leaves a positive fraction untouched.
- **"R₀ is a fixed property of a pathogen."** It is β/γ, which depends on contact rates, behaviour and population structure as much as on biology.
- **"Diffusion always smooths things out."** Alone it does; coupled to reactions with unequal rates it can create structure.

## Go deeper

- J. D. Murray, *Mathematical Biology* (3rd ed., two volumes, 2002–2003): the standard reference, including Turing patterns.
- L. Edelstein-Keshet, *Mathematical Models in Biology* (1988): a gentler introduction built on examples.
- W. O. Kermack and A. G. McKendrick, "A Contribution to the Mathematical Theory of Epidemics" (1927): the origin of the threshold theorem.
