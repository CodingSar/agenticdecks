# Kinetics, Equilibrium and Catalysis

> **Layer:** [00 Physical and Chemical Foundations](../README.md) › [Chemistry of Life](README.md)
> **Builds on:** [Energy and thermodynamics](../01-physics-of-the-body/energy-and-thermodynamics.md), [Water, solutions and concentration](water-solutions-and-concentration.md), [Compartment models and exponential processes](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md)
> **Enables:** [Enzymes and catalysis](../../02-biochemistry-and-molecular-biology/01-macromolecules/enzymes-and-catalysis.md), [Receptor theory, agonists and antagonists](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/receptor-theory-agonists-and-antagonists.md), [Drug metabolism and interactions](../../09-pharmacology-and-therapeutics/01-pharmacokinetics/drug-metabolism-and-interactions.md), [Elimination, half-life and dosing](../../09-pharmacology-and-therapeutics/01-pharmacokinetics/elimination-half-life-and-dosing.md)

## Essence

Thermodynamics says which way a reaction can go; kinetics says how fast it gets there, and in the body the two are deliberately separated. Nearly every reaction of metabolism is thermodynamically favourable yet would take years without help, because reacting molecules must first climb an activation energy barrier. Enzymes lower that barrier, speeding reactions by factors of a million to a trillion, without changing the equilibrium they lead to. This separation is what makes control possible: the cell decides which favourable reactions actually happen by deciding which enzymes are present and active. The same ideas, rate proportional to concentration, saturation of a limited number of catalytic sites, and binding equilibria described by a dissociation constant, govern drug elimination, receptor occupancy and the shape of every dose–response curve.

## Core tenets

1. **Equilibrium is where forward and reverse rates are equal, and the equilibrium constant is set by free energy.** For `A ⇌ B`, `K = [B]/[A]` at equilibrium and `ΔG° = −RT ln K`: a ΔG° of −5.7 kJ/mol corresponds to K = 10 at 37 °C. A reaction's position does not depend on the path or on any catalyst, only on the energies of reactants and products and on their concentrations (Le Chatelier: adding product pushes it back). The cell keeps most reactions far from equilibrium by removing products, which is why metabolic pathways have direction.

2. **Rate depends on the activation energy, exponentially: Arrhenius.** `k = A · e^(−Ea/RT)`. Only the fraction of molecules with energy above `Ea` react on collision, and that fraction rises steeply with temperature (the Q10 of 2–3 for biological processes) and falls steeply with barrier height.

3. **A catalyst lowers the barrier and changes nothing else.** Enzymes bind the transition state more tightly than the substrate, providing a lower-energy path through the same start and end points. They accelerate forward and reverse reactions equally, so the equilibrium constant is untouched; what changes is how soon equilibrium is approached. Carbonic anhydrase turns over ~10⁶ substrates per second; without it the hydration of carbon dioxide would be too slow for the blood's transit through the lung.

4. **Rates are proportional to concentration, and first-order processes decay exponentially.** In a first-order reaction, rate = `k[A]`, so a constant fraction disappears per unit time and the amount falls as `e^(−kt)` with a half-life `t½ = ln2 / k`, independent of starting amount. Most drug elimination, radioactive decay, and the washout of a tracer are first order, which is why a drug reaches 97% of its steady state in five half-lives regardless of dose.

5. **Saturable catalysts give Michaelis–Menten kinetics, and saturation changes everything.** With a fixed number of enzyme molecules, rate `v = Vmax · [S] / (Km + [S])`: nearly proportional to substrate when `[S] << Km`, and flat at `Vmax` when `[S] >> Km`. A saturated enzyme cannot go faster however much substrate arrives, so elimination becomes zero-order: a fixed amount per hour. Ethanol is cleared this way (~7–10 g/h in an adult), and phenytoin's metabolism saturates within the therapeutic range, so a small dose increase produces a disproportionate rise in level.

6. **Binding is an equilibrium described by a dissociation constant, which is the ligand concentration at half-occupancy.** For `R + L ⇌ RL`, `Kd = [R][L]/[RL]`, and fractional occupancy is `[L]/(Kd + [L])`, the same hyperbola as Michaelis–Menten. A drug with Kd of 1 nM occupies half its receptors at 1 nM and 90% at 9 nM; ten times more raises occupancy only to 99%. Affinity (low Kd) says how little drug is needed; it says nothing about what binding does. Competitive inhibitors and antagonists raise the apparent Kd or Km without changing the maximum; non-competitive ones lower the maximum.

7. **The slowest step controls the pathway, and that is where regulation acts.** In a sequence of reactions the rate-limiting step sets the throughput, and enzymes at these steps are the ones controlled by feedback inhibition, phosphorylation and hormones (phosphofructokinase in glycolysis, HMG-CoA reductase in cholesterol synthesis, the target of statins). This is why drug targets are chosen at control points.

## Key concepts

| Term | Meaning |
|---|---|
| Equilibrium constant (K) | Ratio of products to reactants at equilibrium; `ΔG° = −RT ln K` |
| Activation energy (Ea) | The barrier between reactants and the transition state |
| Arrhenius equation | `k = A e^(−Ea/RT)`: rate rises exponentially with temperature and falls with barrier height |
| Catalyst | Lowers Ea and speeds both directions equally; does not change K |
| First-order kinetics | Rate ∝ concentration; exponential decay; constant half-life |
| Zero-order kinetics | Rate constant, independent of concentration; a saturated system |
| Michaelis–Menten equation | `v = Vmax[S]/(Km + [S])`; Km is the substrate concentration at half Vmax |
| Dissociation constant (Kd) | Ligand concentration at which half the receptors are occupied; lower is tighter |
| Rate-limiting step | The slowest step in a pathway, which sets its throughput and is the site of control |

## How it fits

- **Below:** K follows from [free energy](../01-physics-of-the-body/energy-and-thermodynamics.md); rates are stated in [concentrations](water-solutions-and-concentration.md); first-order decay is the one-compartment case of [exponential processes](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md).
- **Above:** [enzymes and catalysis](../../02-biochemistry-and-molecular-biology/01-macromolecules/enzymes-and-catalysis.md) and [receptors and ligands](../../02-biochemistry-and-molecular-biology/04-cell-signalling/receptors-and-ligands.md) are tenets 3, 5 and 6 as proteins; [receptor theory](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/receptor-theory-agonists-and-antagonists.md) and [dose–response](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/dose-response-and-therapeutic-index.md) are the Kd hyperbola; [drug metabolism](../../09-pharmacology-and-therapeutics/01-pharmacokinetics/drug-metabolism-and-interactions.md) and [half-life and dosing](../../09-pharmacology-and-therapeutics/01-pharmacokinetics/elimination-half-life-and-dosing.md) are tenets 4 and 5.
- **Siblings:** [acids and bases](acids-bases-and-buffers.md) is the equilibrium of one reaction, proton dissociation, in logarithmic form; [molecular recognition](carbon-chemistry-and-molecular-recognition.md) explains where the specificity of Kd comes from.

## Common misconceptions

- **"Enzymes make reactions happen that otherwise would not."** They only speed reactions that are already favourable; an enzyme cannot drive a reaction uphill unless it couples it to one going downhill.
- **"Doubling the dose doubles the effect."** Receptor occupancy and enzyme rate are hyperbolic in concentration; beyond Kd or Km, extra drug or substrate buys little, and in a saturated system elimination stops keeping pace.

## Go deeper

- Peter Atkins and Julio de Paula, *Physical Chemistry for the Life Sciences* (2nd ed., 2011): equilibrium and kinetics with biological examples throughout.
- Alan Fersht, *Structure and Mechanism in Protein Science* (1999): how enzymes achieve catalysis, from transition-state binding to kinetic measurement.
- H. P. Rang and colleagues, *Rang & Dale's Pharmacology* (9th ed., 2019), chapters on how drugs act: binding equilibria applied to receptors and drug elimination.
