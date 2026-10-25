# Compartment Models and Exponential Processes

> **Layer:** [01 Quantitative and Scientific Foundations](../README.md) › [Systems and Models](README.md)
> **Builds on:** [The scientific method and models](the-scientific-method-and-models.md), [Probability](../01-probability-and-measurement/probability.md)
> **Enables:** [Elimination, half-life and dosing](../../09-pharmacology-and-therapeutics/01-pharmacokinetics/elimination-half-life-and-dosing.md), [Infectious disease dynamics](../../10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md), [Glomerular filtration and clearance](../../06-physiology/05-renal-system/glomerular-filtration-and-clearance.md), [Kinetics, equilibrium and catalysis](../../00-physical-and-chemical-foundations/02-chemistry-of-life/kinetics-equilibrium-and-catalysis.md)

## Essence

A great deal of medicine is the bookkeeping of substances moving between pools: a drug from gut to blood to tissue to urine, oxygen from air to blood, a tracer through the kidney, people from susceptible to infected to recovered. The compartment model treats each pool as a well-mixed box and each transfer as a rate proportional to the amount in the box it leaves. That one assumption, rate proportional to amount, gives exponential curves everywhere: a drug concentration falls by a constant fraction per unit time, an epidemic grows by a constant factor per generation, a radioactive tracer decays with a fixed half-life. Exponential processes are counter-intuitive because their speed changes while their rule does not, and most of the practical arithmetic of dosing, washout, steady state and outbreak growth comes from knowing three numbers: the rate constant, the half-life and the volume of the box.

## Core tenets

1. **A first-order process removes a constant fraction per unit time and decays exponentially.** If `dA/dt = −kA`, then `A(t) = A₀ e^(−kt)`. The half-life is `t½ = ln 2 / k ≈ 0.693 / k`, independent of how much is present. After one half-life 50% remains, after two 25%, after five ~3%, after seven ~1%. This is why "when will the drug be gone?" has the answer "about five half-lives" for any dose, and why a tracer's or an isotope's decay is predicted by one constant.

2. **Clearance is the volume of fluid cleared of substance per unit time, and it links rate to concentration.** Elimination rate = clearance × concentration. For a substance filtered freely and not reabsorbed, renal clearance equals the glomerular filtration rate (~120 mL/min in a young adult), which is how creatinine and inulin measure kidney function. Clearance is a property of the organs (liver blood flow, enzyme capacity, kidney filtration); the rate constant is clearance divided by the volume of the compartment, `k = CL / V`, so a drug with a large volume has a long half-life even if cleared briskly.

3. **The apparent volume of distribution is the box's size implied by the concentration, not an anatomical space.** `V = dose / initial concentration`. A drug confined to plasma has V ≈ 3 L; one distributed in total body water ~40 L; one that binds heavily in tissue can have an apparent volume of hundreds of litres (digoxin ~500 L, chloroquine many thousands), because plasma concentration is low relative to the dose given. V and clearance are the two independent parameters; half-life is derived from them, `t½ = 0.693 V / CL`.

4. **Constant input into a first-order box approaches a plateau, not a runaway; the plateau is input over clearance.** With infusion rate R, the concentration rises toward `C_ss = R / CL` along `1 − e^(−kt)`: half-way in one half-life, 97% in five. The time to steady state depends only on half-life, never on the dose; the dose sets the height. A loading dose fills the box at once; without one, a drug with a 40-hour half-life takes over a week to reach its working level. The same curve describes a tracer equilibrating, oxygen saturating a tissue and a hormone infusion reaching its effect.

5. **Zero-order processes remove a fixed amount per unit time, and the two kinetics behave oppositely.** When the removing mechanism is saturated, elimination is constant regardless of concentration (ethanol at roughly one standard drink per hour, phenytoin and salicylate at high doses). Here half-life lengthens as concentration rises, small dose increases produce large concentration increases and there is no plateau: input above the capacity accumulates without limit. Recognising which kinetics apply is the difference between a safe dose adjustment and a toxic one.

6. **Several compartments give several exponentials, and the slowest one dominates the tail.** A drug injected into blood first distributes into tissue (a fast decline) and then is eliminated (a slow decline); the concentration curve is a sum of exponentials and appears as two straight segments on a log plot. Fat-soluble anaesthetics show this: the patient wakes as the drug leaves the brain for muscle and fat, long before the body has eliminated it, and repeated doses fill the slow compartment so recovery lengthens. Oxygen stores, body potassium and bone calcium are each modelled the same way.

7. **Exponential growth is the same law with a positive constant, and it is how epidemics and tumours begin.** If each case infects R others per generation, cases grow as `Rⁿ`; with R = 3 and a generation of five days, one case becomes ~60,000 in ten weeks. A tumour doubling every 100 days reaches 1 cm³ (~10⁹ cells) after 30 doublings, about eight years, and is detectable only for the last few of them. Growth looks negligible then sudden because a constant doubling time produces an accelerating absolute increase; the time to act is when the curve still looks flat.

8. **Growth is checked when the box it draws on empties: the logistic curve.** Exponential growth cannot continue; an epidemic slows as susceptibles are used up, giving the S-shaped curve of susceptible–infected–recovered models and the herd-immunity threshold `1 − 1/R₀` (about 67% for R₀ = 3). A tumour slows as it outgrows its blood supply; a bacterial culture as nutrients fall. The compartment framework gives the shape; the parameters say where the bend comes.

## Key concepts

| Term | Meaning |
|---|---|
| Compartment | A well-mixed pool in which a substance has one concentration |
| First-order kinetics | Rate proportional to amount; exponential change; constant half-life |
| Zero-order kinetics | Constant rate independent of amount; saturated process |
| Rate constant (k) | Fraction removed per unit time; `k = CL/V` |
| Half-life (t½) | Time to halve; `0.693/k`; five half-lives to ~97% of any change |
| Clearance (CL) | Volume cleared of substance per unit time; an organ property |
| Volume of distribution (V) | Dose divided by resulting concentration; apparent box size |
| Steady state | Input equals output; concentration `R/CL`, reached after ~5 half-lives |
| Loading dose | A dose sized to fill the volume at once |
| Reproduction number (R₀) | Cases produced by one case in a fully susceptible population |
| Logistic growth | Exponential growth that slows as its resource is depleted |

## How it fits

- **Below:** a compartment is a [model](the-scientific-method-and-models.md) whose assumption (well mixed, proportional rate) is stated and testable; the exponential arises because each molecule leaves with a fixed [probability](../01-probability-and-measurement/probability.md) per unit time.
- **Above:** [half-life and dosing](../../09-pharmacology-and-therapeutics/01-pharmacokinetics/elimination-half-life-and-dosing.md) and [distribution](../../09-pharmacology-and-therapeutics/01-pharmacokinetics/distribution-and-protein-binding.md) are tenets 1–6 for drugs; [glomerular filtration and clearance](../../06-physiology/05-renal-system/glomerular-filtration-and-clearance.md) is tenet 2 for the kidney; [infectious disease dynamics](../../10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md) is tenets 7–8; [chemical kinetics](../../00-physical-and-chemical-foundations/02-chemistry-of-life/kinetics-equilibrium-and-catalysis.md) and [radioactive decay](../../00-physical-and-chemical-foundations/01-physics-of-the-body/waves-sound-light-and-radiation.md) are the same mathematics in layer 00; the [cable equation](../../00-physical-and-chemical-foundations/01-physics-of-the-body/electricity-and-excitable-membranes.md) is exponential decay in space.
- **Siblings:** [feedback and control](feedback-and-control.md) adds a controller that changes the input in response to the output; [nonlinear dynamics](nonlinear-dynamics-oscillations-and-networks.md) covers what happens when rates are not proportional to amounts.

## Common misconceptions

- **"Doubling the dose doubles the time the drug lasts."** It adds one half-life, since the concentration must fall through one more halving to reach the same level.
- **"A drug with a long half-life is slowly cleared."** Half-life depends on volume as well as clearance; a widely distributed drug can be cleared fast yet persist for days.
- **"Linear growth of cases means the epidemic is under control."** An exponential looks linear early; the test is whether the doubling time is lengthening.

## Go deeper

- Malcolm Rowland and Thomas N. Tozer, *Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications* (4th ed., 2011): compartment models for drugs, from first principles.
- Roy M. Anderson and Robert M. May, *Infectious Diseases of Humans: Dynamics and Control* (1991): the susceptible–infected–recovered framework and its consequences.
- John A. Jacquez, *Compartmental Analysis in Biology and Medicine* (3rd ed., 1996): the general mathematics of compartment systems.
