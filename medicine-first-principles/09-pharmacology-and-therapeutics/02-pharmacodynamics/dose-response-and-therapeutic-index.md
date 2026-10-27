# Dose–response and therapeutic index

> **Layer:** [09 Pharmacology and Therapeutics](../README.md) › [Pharmacodynamics](README.md)
> **Builds on:** [Receptor theory, agonists and antagonists](receptor-theory-agonists-and-antagonists.md), [Elimination, half-life and dosing](../01-pharmacokinetics/elimination-half-life-and-dosing.md), [Distributions and descriptive statistics](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/distributions-and-descriptive-statistics.md), [Measurement error and biological variation](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/measurement-error-and-biological-variation.md)
> **Enables:** [Adverse drug reactions and pharmacovigilance](adverse-drug-reactions-and-pharmacovigilance.md), [Toxicology and poisoning](../05-drug-development-and-toxicology/toxicology-and-poisoning.md), [Radiotherapy and radiation biology](../04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md), [Randomized controlled trials](../../10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md), [Clinical chemistry and reference ranges](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/clinical-chemistry-and-reference-ranges.md)

## Essence

There are two different dose–response curves and confusing them causes errors. The graded curve describes one system: as concentration rises, the magnitude of effect rises along the sigmoid that receptor theory predicts, until it saturates. The quantal curve describes a population: as dose rises, the proportion of individuals who show a defined all-or-none response (relief of pain, death) rises, because individuals differ in the dose they need, and that variation is roughly log-normal. The therapeutic index compares the dose that produces the wanted quantal response in half the population with the dose that produces the unwanted one, and it, together with how much the concentration fluctuates between doses, decides whether a drug can be given safely without measuring its level. The single idea is that a drug's safety is a property of the distance between two population curves, not of the drug's chemistry alone.

## Core tenets

1. **The graded dose–response curve is receptor occupancy seen through the tissue's amplification.** Effect = Emax × C^n / (EC50^n + C^n), the Hill equation. Emax is the ceiling, EC50 the concentration for half-maximal effect, and the Hill coefficient n the steepness. On a log scale the curve is nearly linear between about 20% and 80% of maximum, which is the range in which dose changes produce proportional effect changes; below and above it, dose changes do little. Most drugs are used on the steep part, and a drug with a steep curve (large n) is harder to titrate.

2. **Quantal curves describe variation between people, and they are cumulative distributions.** Give increasing doses to a population and record the fraction that responds; the result is the cumulative form of the distribution of individual threshold doses. Because thresholds vary multiplicatively (metabolism, receptor number, body size), they are approximately log-normal, and the cumulative curve on a log-dose axis is a symmetric sigmoid. The median effective dose (ED50) is where half respond; the median toxic dose (TD50) and median lethal dose (LD50) are read from the curves for toxicity and death.

3. **The therapeutic index is the ratio of toxic to effective median doses, and its usefulness depends on the curves' slopes.** TI = TD50/ED50 (or LD50/ED50 in animals). A ratio of 100 for a benzodiazepine is why overdose is rarely fatal alone; a ratio near 2–3 for digoxin, lithium or warfarin is why these drugs are monitored. But two drugs with the same TI differ in safety if their curves have different slopes or if one curve has a long tail of sensitive individuals; the more careful measure is the margin between the dose effective in 99% and toxic in 1% (TD1/ED99), the certain safety factor.

4. **Pharmacokinetic fluctuation and pharmacodynamic index together define the therapeutic window.** A drug with a narrow index can still be safe if its concentration is held steady: a long half-life, frequent dosing or an infusion keeps the peak below toxicity and the trough above efficacy. The window is a band of concentrations, bounded below by minimum effective and above by minimum toxic concentration, and the dosing interval from [elimination kinetics](../01-pharmacokinetics/elimination-half-life-and-dosing.md) decides whether the swing fits inside it. Therapeutic drug monitoring exists for the drugs where it does not.

5. **Many effects have a threshold, a ceiling, or both.** Below a threshold concentration nothing measurable happens; at a ceiling, more drug adds toxicity without benefit, as with partial agonists and with loop diuretics once all transporters are blocked. Some exposures show the opposite at low dose: a small stress induces protective responses (hormesis), seen in radiation biology and exercise, though rarely exploited in drug therapy. Whether a response has a threshold is the central question in setting exposure limits for [toxins](../05-drug-development-and-toxicology/toxicology-and-poisoning.md) and [radiation](../04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md).

6. **Combining drugs changes the curve in predictable ways.** Two drugs acting at the same receptor add occupancy; two acting on different steps of one pathway can be synergistic, giving more than the sum (a beta-lactam weakening the cell wall lets an aminoglycoside enter the bacterium). Antagonism between drugs is also exploited deliberately. The isobologram plots the dose pairs that give a fixed effect and reads additivity as a straight line, synergy as a curve bowed towards the origin.

7. **Concentration, not dose, is what the receptor sees, and the two diverge most in the sick.** Dose–response curves drawn against dose fold together kinetics and dynamics. In renal failure, old age or enzyme inhibition the same dose gives a higher concentration and the patient appears "sensitive"; in enzyme induction the reverse. Separating the two (is the concentration abnormal, or the response to it?) is the first question when a usual dose fails or harms, and it is why [reference ranges](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/clinical-chemistry-and-reference-ranges.md) for drug levels exist.

```
   100% |          effect  ____------         toxicity  ____------
        |               _/                            _/
    50% |             _/  ED50                      _/  TD50
        |           _/                            _/
     0% |_______---'                        ___--'
        +----------------------------------------------- log dose
                   <---- therapeutic index = TD50 / ED50 ---->
```

## Key concepts

| Term | Meaning |
|---|---|
| Graded response | Magnitude of effect in one system as a continuous function of concentration |
| Quantal response | Fraction of a population showing an all-or-none effect at each dose |
| Emax and EC50 | Maximal effect and the concentration producing half of it |
| Hill coefficient | Steepness of the graded curve; > 1 indicates cooperativity or threshold behaviour |
| ED50, TD50, LD50 | Doses at which 50% of a population show the therapeutic, toxic or lethal response |
| Therapeutic index | TD50 ÷ ED50; a crude ratio of safety margin |
| Certain safety factor | TD1 ÷ ED99; a stricter margin that respects the tails of the curves |
| Therapeutic window | Range of concentrations between minimum effective and minimum toxic levels |
| Therapeutic drug monitoring | Measuring plasma concentration to keep a narrow-window drug inside its window |
| Synergy and isobologram | More-than-additive effect of two drugs, and the plot used to demonstrate it |

## How it fits

- **Below:** The graded curve is [receptor occupancy](receptor-theory-agonists-and-antagonists.md) with amplification; the quantal curve is a [cumulative distribution](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/distributions-and-descriptive-statistics.md) of thresholds arising from [biological variation](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/measurement-error-and-biological-variation.md). The assumption is that individual thresholds vary log-normally and that effect depends on concentration rather than history.
- **Above:** Trial design in [randomized controlled trials](../../10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md) must choose a dose on the curve; toxicology sets exposure limits from thresholds; [radiotherapy](../04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md) applies the same tumour-control and normal-tissue-complication curves.
- **Siblings:** [Adverse reactions](adverse-drug-reactions-and-pharmacovigilance.md) of the predictable type are the toxicity curve overlapping the efficacy curve; [tolerance](tolerance-dependence-and-withdrawal.md) shifts the curve rightward over time; [pharmacogenomics](pharmacogenomics-and-individual-variation.md) explains the width of the quantal distribution.

## Common misconceptions

- **"A drug with a high therapeutic index cannot cause harm."** The index compares medians; a long tail of sensitive individuals, or an interaction raising concentration, moves a patient into toxicity regardless of the population ratio.
- **"Doubling the dose doubles the effect."** Only near the middle of the log-linear range; near the ceiling, doubling adds little effect and much toxicity.
- **"The quantal and graded curves are the same curve."** One describes one individual's effect size, the other the fraction of a population crossing a threshold; they have different axes and different uses.

## Go deeper

- Humphrey Rang, James Ritter, Rod Flower and Graeme Henderson, *Rang & Dale's Pharmacology* (9th ed., 2019): graded and quantal curves and the therapeutic index.
- Bertram Katzung (ed.), *Basic and Clinical Pharmacology* (15th ed., 2021), chapter 2: therapeutic index and certain safety factor with worked examples.
- Nick Holford and Lewis Sheiner, "Understanding the dose–effect relationship" (*Clinical Pharmacokinetics*, 1981): the paper that joined kinetics to dynamics in one model.
