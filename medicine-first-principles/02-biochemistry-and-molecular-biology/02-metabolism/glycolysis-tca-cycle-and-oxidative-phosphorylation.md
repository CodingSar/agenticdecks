# Glycolysis, TCA cycle and oxidative phosphorylation

> **Layer:** [02 Biochemistry and Molecular Biology](../README.md) › [Metabolism](README.md)
> **Builds on:** [Bioenergetics: ATP and redox carriers](bioenergetics-atp-and-redox-carriers.md), [Enzymes and catalysis](../01-macromolecules/enzymes-and-catalysis.md), [Carbohydrates and glycobiology](../01-macromolecules/carbohydrates-and-glycobiology.md), [Redox and electron transfer](../../00-physical-and-chemical-foundations/02-chemistry-of-life/redox-and-electron-transfer.md)
> **Enables:** [Skeletal muscle contraction and energetics](../../06-physiology/10-musculoskeletal-system-and-skin/skeletal-muscle-contraction-and-energetics.md), [Red cells, haemoglobin and iron](../../06-physiology/08-blood/red-cells-haemoglobin-and-iron.md), [Cell injury, adaptation and death](../../08-pathology/01-cell-and-tissue-injury/cell-injury-adaptation-and-death.md), [Toxicology and poisoning](../../09-pharmacology-and-therapeutics/05-drug-development-and-toxicology/toxicology-and-poisoning.md), [Hallmarks of cancer](../../08-pathology/03-neoplasia/hallmarks-of-cancer.md)

## Essence

Glucose is oxidised to carbon dioxide in three stages: glycolysis in the cytosol splits it to two pyruvate, the Tricarboxylic Acid (TCA) cycle in the mitochondrial matrix strips the carbons to carbon dioxide and loads electrons onto Nicotinamide Adenine Dinucleotide (NAD) and Flavin Adenine Dinucleotide (FAD), and the respiratory chain in the inner membrane passes those electrons to oxygen while pumping protons that drive Adenosine Triphosphate (ATP) synthase. Only the first stage works without oxygen, and it yields 2 ATP per glucose against about 30 for the whole route. That fifteenfold difference is why tissues die within minutes of losing oxygen, why cyanide kills with fully saturated blood, and why lactate rises when perfusion fails.

## Core tenets

1. **Glycolysis invests 2 ATP to earn 4, needs no oxygen, and is controlled at three irreversible steps.** Ten cytosolic reactions convert glucose to two pyruvate with a net gain of 2 ATP and 2 NADH. The three steps held far from equilibrium are the control points: hexokinase (trapping), phosphofructokinase-1 (the committed step, inhibited by ATP and citrate, activated by Adenosine Monophosphate (AMP) and by fructose-2,6-bisphosphate, through which insulin and glucagon act) and pyruvate kinase. Red cells, which have no mitochondria, live on glycolysis alone.

2. **The fate of pyruvate depends on oxygen and on NAD+.** Glycolysis consumes NAD+; without oxygen the only way to regenerate it is lactate dehydrogenase, which hands the electrons back to pyruvate. Lactate is not waste: liver remakes glucose from it (the Cori cycle) and heart and brain burn it. With oxygen, pyruvate dehydrogenase in the mitochondrion converts pyruvate irreversibly to acetyl-CoA using five cofactors (thiamine, lipoate, FAD, NAD+, coenzyme A), which is why thiamine deficiency produces lactic acidosis and brain failure. The irreversibility matters: acetyl-CoA can never become glucose again.

3. **The TCA cycle is a catalytic loop and a biosynthetic hub.** Each turn oxidises one acetyl group to 2 CO2 and yields 3 NADH, 1 FADH2 and 1 Guanosine Triphosphate (GTP). The intermediates are regenerated, but they are also drawn off: citrate for fatty-acid synthesis, alpha-ketoglutarate for glutamate, succinyl-CoA for haem, oxaloacetate for glucose. What is drawn off must be replaced (anaplerosis, mainly by pyruvate carboxylase). The cycle's speed follows NADH/NAD+ and calcium, so it accelerates when muscle contracts.

4. **The respiratory chain couples electron fall to proton pumping.** Electrons from NADH enter complex I, from FADH2 via complex II, and pass through ubiquinone, complex III, cytochrome c and complex IV to reduce oxygen to water. Complexes I, III and IV pump about 10 protons per NADH (6 per FADH2); ATP synthase uses about 4 protons per ATP (including the cost of importing phosphate and Adenosine Diphosphate (ADP)), giving around 2.5 ATP per NADH, 1.5 per FADH2 and 30–32 per glucose. The older figure of 36–38 assumed integer stoichiometries.

5. **Respiratory control ties oxygen consumption to work.** If ATP is not being used, ADP is scarce, the synthase stalls, the gradient builds and the chain slows; demand pulls supply, which is why whole-body oxygen uptake tracks work rate. A backed-up chain leaks more electrons to oxygen, so overfed, underworked cells generate more reactive oxygen species.

6. **Every inhibitor of the chain is a poison, and each has a site.** Rotenone blocks complex I, antimycin A complex III, cyanide and carbon monoxide complex IV, oligomycin the synthase. In cyanide poisoning the blood is fully saturated but cells cannot use the oxygen: histotoxic hypoxia with lactic acidosis. Uncouplers do the opposite, letting electrons flow without ATP and releasing heat, the mechanism of brown-fat thermogenesis and of salicylate-overdose hyperthermia.

7. **The mitochondrion is a compartment with its own genome.** The inner membrane is impermeable, so cytosolic NADH enters via shuttles and pyruvate, ADP, phosphate and acyl-carnitine cross by specific carriers. Thirteen chain subunits are encoded by mitochondrial Deoxyribonucleic Acid (DNA), inherited from the mother in hundreds of copies per cell; mutations are therefore heteroplasmic and strike the tissues with the highest ATP demand (brain, muscle, retina, heart).

8. **Cells shift between the stages for reasons other than oxygen.** Hypoxia-inducible factor raises glycolytic enzymes when oxygen is low. Many cancers run glycolysis with oxygen present (the Warburg effect), not because their mitochondria are broken but because glycolytic intermediates feed biosynthesis; the resulting avid glucose uptake is what fluorodeoxyglucose positron emission tomography images. Proliferating lymphocytes and healing wounds do the same.

```
  glucose --(cytosol, 10 steps)--> 2 pyruvate   net 2 ATP, 2 NADH
     |                                 |
  no O2: pyruvate -> lactate (regenerates NAD+)
     |                                 v
  O2: pyruvate --PDH--> acetyl-CoA --TCA--> 2 CO2 + 3 NADH + FADH2 + GTP
                                       |
            NADH/FADH2 --> complexes I-IV --> O2 -> H2O ; H+ pumped out
                                       |
                           H+ back through ATP synthase --> ~30 ATP/glucose
```

## Key concepts

| Term | Meaning |
|---|---|
| Oxidative phosphorylation | ATP made by ATP synthase using the proton gradient built by electron transport |
| Committed step | First irreversible step unique to a pathway; where control acts (PFK-1) |
| Pyruvate dehydrogenase | Irreversible gate from carbohydrate to acetyl-CoA |
| Anaplerosis | Replenishment of TCA intermediates drawn off for biosynthesis |
| Electron transport chain | Complexes I–IV plus mobile carriers that pass electrons to oxygen |
| Heteroplasmy | Mixture of mutant and normal mitochondrial genomes within one cell |
| Warburg effect | Glycolysis despite available oxygen, typical of proliferating cells |

## How it fits

- **Below:** the pathway is a sequence of [enzyme](../01-macromolecules/enzymes-and-catalysis.md)-catalysed [redox](../../00-physical-and-chemical-foundations/02-chemistry-of-life/redox-and-electron-transfer.md) and group-transfer steps whose yield is fixed by the [bioenergetics](bioenergetics-atp-and-redox-carriers.md) of the carriers.
- **Above:** it sets the power available to [muscle](../../06-physiology/10-musculoskeletal-system-and-skin/skeletal-muscle-contraction-and-energetics.md) and the fuel of the [red cell](../../06-physiology/08-blood/red-cells-haemoglobin-and-iron.md); ATP failure on hypoxia is the start of [cell injury](../../08-pathology/01-cell-and-tissue-injury/cell-injury-adaptation-and-death.md); chain inhibitors are classical [poisons](../../09-pharmacology-and-therapeutics/05-drug-development-and-toxicology/toxicology-and-poisoning.md); rewired metabolism is a [hallmark of cancer](../../08-pathology/03-neoplasia/hallmarks-of-cancer.md).
- **Siblings:** [lipid](lipid-metabolism.md) and [amino acid](amino-acid-and-nitrogen-metabolism.md) catabolism feed acetyl-CoA and TCA intermediates into the same final stages; the [fed–fasted cycle](metabolic-integration-and-the-fed-fasted-cycle.md) decides which fuel is used.

## Common misconceptions

- **"Lactate causes fatigue and is a waste product."** It is a fuel shuttled between tissues; the acidosis of anaerobic work comes from the protons released by ATP hydrolysis when the chain is not resorbing them, and fatigue has other causes.
- **"Oxygen is consumed in the TCA cycle."** The cycle uses NAD+ and FAD; oxygen is used only at complex IV, which is why the cycle stops without oxygen only indirectly, when NADH cannot be reoxidised.
- **"Fat can be turned into glucose."** Acetyl-CoA enters the cycle as two carbons and leaves as two CO2; no net carbon reaches oxaloacetate, so fatty acids cannot sustain blood glucose.

## Go deeper

- Nelson and Cox, *Lehninger Principles of Biochemistry* (8th ed., 2021), chapters 14, 16 and 19: the three stages in full.
- Nicholls and Ferguson, *Bioenergetics* (4th ed., 2013): the chain and its stoichiometry.
- Nick Lane, *Power, Sex, Suicide: Mitochondria and the Meaning of Life* (2005): why the mitochondrion is organised as it is.
