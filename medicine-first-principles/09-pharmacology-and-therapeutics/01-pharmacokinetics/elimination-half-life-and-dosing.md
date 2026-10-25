# Elimination, half-life and dosing

> **Layer:** [09 Pharmacology and Therapeutics](../README.md) › [Pharmacokinetics](README.md)
> **Builds on:** [Compartment models and exponential processes](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md), [Glomerular filtration and clearance](../../06-physiology/05-renal-system/glomerular-filtration-and-clearance.md), [Tubular transport and the countercurrent system](../../06-physiology/05-renal-system/tubular-transport-and-the-countercurrent-system.md), [Distribution and protein binding](distribution-and-protein-binding.md), [Drug metabolism and interactions](drug-metabolism-and-interactions.md)
> **Enables:** [Dose–response and therapeutic index](../02-pharmacodynamics/dose-response-and-therapeutic-index.md), [Antimicrobials](../03-drug-classes-by-mechanism/antimicrobials.md), [Acute kidney injury](../../12-organ-system-specialties/03-nephrology/acute-kidney-injury.md), [Chronic kidney disease and dialysis](../../12-organ-system-specialties/03-nephrology/chronic-kidney-disease-and-dialysis.md), [Frailty, multimorbidity and polypharmacy](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md)

## Essence

Most drugs leave the body at a rate proportional to how much is present, so their concentration decays exponentially with a characteristic half-life. Two independent quantities set that half-life: clearance (the volume of plasma cleared of drug per unit time, a property of the liver and kidney) and volume of distribution (how widely the drug spreads). From these three numbers almost all of practical dosing follows: how much to give first, how much to give repeatedly and how often, how long to wait for steady state, and how to adjust when the kidneys fail. The single idea is that at steady state the rate in equals the rate out, so the average concentration is simply dose rate divided by clearance.

## Core tenets

1. **First-order elimination gives an exponential decay with a constant half-life.** If the rate of removal is k × amount, the concentration follows C(t) = C₀·e^(−kt), and the half-life t½ = ln2/k ≈ 0.693/k is the same at every concentration. After one half-life 50% remains, after two 25%, after four ~6%, after five ~3%. This is the [exponential process](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md) of a single leaky compartment, and it holds for most drugs at therapeutic concentrations.

2. **Half-life is derived from clearance and volume, not a primary property.** t½ = 0.693 × Vd ÷ CL. A drug with a huge volume of distribution has a long half-life even if the liver clears it efficiently, because most of the drug is out of reach of the clearing organ at any moment. Conversely renal failure lengthens half-life by cutting CL while leaving Vd unchanged. Reasoning from t½ alone confuses cause and effect; reason from the two primary parameters.

3. **Clearance is additive across organs, and renal clearance is filtration plus secretion minus reabsorption.** Total CL = hepatic + renal + other. The kidney filters free drug at the glomerular filtration rate (GFR, ~120 mL/min in a healthy adult), secretes some drugs actively in the proximal tubule (penicillins, many organic anions and cations) and reabsorbs lipid-soluble, un-ionised molecules passively along the nephron. A drug cleared mainly by filtration, such as gentamicin or digoxin, has a clearance that falls in step with GFR, so its dose must fall in step too; this is the quantitative core of prescribing in [kidney disease](../../12-organ-system-specialties/03-nephrology/chronic-kidney-disease-and-dialysis.md).

4. **Steady state is reached after four to five half-lives, regardless of the dose.** With repeated dosing, each dose adds to what remains of the previous ones until the amount eliminated per interval equals the amount given. The approach is exponential: 50% of steady state after one half-life, ~94% after four, ~97% after five. A drug with a 40-hour half-life, such as digoxin, needs about a week to reach steady state and a week to wash out; the same time applies whether the dose is doubled or halved. This delay is why dose changes must be judged after, not before, steady state is reached.

5. **Average steady-state concentration is dose rate over clearance; the fluctuation around it is set by the interval relative to half-life.** C̄ss = (F × dose ÷ interval) ÷ CL. Giving the same daily amount as one dose or four changes the peak-to-trough swing, not the average. Dosing once per half-life gives roughly two-fold swing; dosing much less often than the half-life gives large peaks and troughs, which is acceptable for a drug whose effect outlasts its presence (aminoglycosides once daily) and dangerous for one with a narrow window.

6. **A loading dose fills the volume; a maintenance dose replaces what clearance removes.** Loading = target concentration × Vd ÷ F; maintenance rate = target × CL ÷ F. The loading dose does not depend on clearance, and the maintenance dose does not depend on volume. In renal failure the loading dose of a renally cleared drug is unchanged while the maintenance dose falls; getting this backwards either delays effect or causes accumulation.

7. **Saturable elimination breaks every rule above.** When the enzyme or transporter approaches capacity, elimination becomes constant per unit time (zero order), half-life rises with dose and steady state may never be reached: a small dose increment produces a large concentration rise. Phenytoin, ethanol and salicylate at high dose behave this way, which is why their concentrations are monitored rather than predicted.

8. **Dialysis and extracorporeal removal work only for drugs that are small, free, water-soluble and in plasma.** A low Vd, low protein binding and low molecular mass make a drug dialysable (lithium, salicylate, methanol); a large Vd or heavy binding (digoxin, tricyclics) make dialysis useless because almost none of the drug is in the blood passing through the filter. The same parameters that set dosing therefore decide what [critical care](../../13-acute-perioperative-and-procedural-care/03-critical-care/organ-support-and-icu-syndromes.md) can remove in [poisoning](../../13-acute-perioperative-and-procedural-care/04-emergency-medicine/poisoning-and-overdose.md).

```
   dose rate (F x D / tau)  --->  [ body: amount = C x Vd ]  --->  CL x C
                                           |
   steady state when input = output:  Css = F x D / (tau x CL)
   approach to steady state:          1 - e^(-kt),  k = CL / Vd
```

## Key concepts

| Term | Meaning |
|---|---|
| Clearance (CL) | Volume of plasma completely cleared of drug per unit time; additive across organs |
| Half-life (t½) | Time for concentration to fall by half; 0.693 × Vd ÷ CL |
| Elimination rate constant (k) | Fraction of drug removed per unit time; CL ÷ Vd |
| Steady state | Condition where input per interval equals elimination per interval; reached after 4–5 half-lives |
| Loading dose | Single dose to reach target concentration at once; depends on Vd |
| Maintenance dose | Repeated dose that replaces what is eliminated; depends on CL |
| Dosing interval (τ) | Time between doses; relative to half-life it sets peak-to-trough fluctuation |
| Zero-order elimination | Constant amount removed per unit time when the eliminating process is saturated |
| Glomerular filtration rate (GFR) | Volume filtered per minute; the clearance of a freely filtered, non-secreted, non-reabsorbed substance |
| Dialysability | Removability by dialysis: favoured by low Vd, low protein binding, low molecular mass, water solubility |

## How it fits

- **Below:** The mathematics is the single-compartment [exponential model](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md); the organ physiology is [glomerular filtration](../../06-physiology/05-renal-system/glomerular-filtration-and-clearance.md) and [tubular transport](../../06-physiology/05-renal-system/tubular-transport-and-the-countercurrent-system.md). The assumption is first-order kinetics; the leaf itself says when it fails.
- **Above:** Concentration–time profiles connect to effect through [dose–response](../02-pharmacodynamics/dose-response-and-therapeutic-index.md); time-above-threshold versus peak-dependent killing shapes [antimicrobial](../03-drug-classes-by-mechanism/antimicrobials.md) dosing and [stewardship](../../12-organ-system-specialties/08-infectious-diseases/antimicrobial-stewardship.md); the decline of GFR with age is the quantitative heart of [polypharmacy in the elderly](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md).
- **Siblings:** This leaf assembles the others: F from [absorption](absorption-and-bioavailability.md), Vd from [distribution](distribution-and-protein-binding.md), hepatic CL from [metabolism](drug-metabolism-and-interactions.md), and adds renal clearance to complete the balance.

## Common misconceptions

- **"A drug with a long half-life is cleared slowly."** It may be cleared quickly but distributed so widely that little is in plasma to be cleared; half-life conflates two independent quantities.
- **"Doubling the dose halves the time to steady state."** The time to steady state depends only on half-life; a larger dose reaches a higher plateau in the same time. Only a loading dose shortens the wait.
- **"Dialysis removes an overdose."** It removes only drugs that are predominantly in plasma and unbound; most lipid-soluble or tissue-bound drugs are untouched.

## Go deeper

- Malcolm Rowland and Thomas Tozer, *Clinical Pharmacokinetics and Pharmacodynamics* (4th ed., 2011): the definitive treatment of clearance, half-life and dosing-regimen design.
- Laurence Brunton, Björn Knollmann (eds), *Goodman & Gilman's The Pharmacological Basis of Therapeutics* (14th ed., 2023), appendix of pharmacokinetic data: parameters for several hundred drugs in one table.
- Nick Holford, "Pharmacokinetic and pharmacodynamic principles" in Bertram Katzung (ed.), *Basic and Clinical Pharmacology* (15th ed., 2021): a compact derivation of the dosing equations.
