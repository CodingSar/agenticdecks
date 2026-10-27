# Receptor theory, agonists and antagonists

> **Layer:** [09 Pharmacology and Therapeutics](../README.md) › [Pharmacodynamics](README.md)
> **Builds on:** [Receptors and ligands](../../02-biochemistry-and-molecular-biology/04-cell-signalling/receptors-and-ligands.md), [Kinetics, equilibrium and catalysis](../../00-physical-and-chemical-foundations/02-chemistry-of-life/kinetics-equilibrium-and-catalysis.md), [Carbon chemistry and molecular recognition](../../00-physical-and-chemical-foundations/02-chemistry-of-life/carbon-chemistry-and-molecular-recognition.md), [Signal amplification, integration and termination](../../02-biochemistry-and-molecular-biology/04-cell-signalling/signal-amplification-integration-and-termination.md)
> **Enables:** [Dose–response and therapeutic index](dose-response-and-therapeutic-index.md), [Tolerance, dependence and withdrawal](tolerance-dependence-and-withdrawal.md), [Autonomic and cardiovascular drugs](../03-drug-classes-by-mechanism/autonomic-and-cardiovascular-drugs.md), [Central nervous system drugs](../03-drug-classes-by-mechanism/central-nervous-system-drugs.md), [From target to approval](../05-drug-development-and-toxicology/from-target-to-approval.md)

## Essence

Most drugs work by binding to a protein the body already uses for its own signalling, and what happens next depends on two separable properties: how tightly the drug binds (affinity) and what it does to the protein once bound (efficacy). An agonist binds and activates; an antagonist binds and does nothing, so its only action is to deny the site to the body's own ligand; a partial agonist activates weakly and so behaves as an agonist when nothing else is present and as an antagonist in the presence of a full agonist. The single idea, due to Clark, Ariëns, Stephenson and Black, is that drug action is a chemical equilibrium between ligand and receptor described by the law of mass action, so the shape of every dose–response curve and the logic of every drug combination follow from a few equations.

## Core tenets

1. **Binding obeys the law of mass action, so occupancy saturates.** For ligand L and receptor R, L + R ⇌ LR with dissociation constant Kd = [L][R]/[LR]. Fractional occupancy = [L]/([L] + Kd): half the receptors are occupied when the concentration equals Kd, and the curve is a hyperbola that becomes the familiar sigmoid on a logarithmic concentration axis. Affinity is the inverse of Kd. This is the [equilibrium chemistry](../../00-physical-and-chemical-foundations/02-chemistry-of-life/kinetics-equilibrium-and-catalysis.md) of [receptors and ligands](../../02-biochemistry-and-molecular-biology/04-cell-signalling/receptors-and-ligands.md) made quantitative.

2. **Affinity and efficacy are independent.** Affinity decides how much drug is needed to occupy receptors; efficacy (intrinsic activity) decides how much response each occupied receptor produces. Two drugs can bind the same receptor with identical affinity while one is a full agonist, one a partial agonist and one an antagonist. Antagonists have affinity and zero efficacy; this is why a potent antagonist is still "potent" even though it does nothing on its own.

3. **Spare receptors mean response can be maximal at low occupancy.** Signal amplification downstream (one activated receptor turning on many G proteins, each making many second-messenger molecules) means a full response may need only a few percent of receptors occupied. The concentration giving half-maximal response (EC50) is then far below Kd, and irreversibly blocking many receptors shifts the agonist curve rightward before it lowers the maximum. Spare receptors explain why tissues differ in sensitivity to the same drug and why partial loss of receptors is tolerated.

4. **Competitive antagonism is surmountable; non-competitive is not.** A competitive antagonist binds reversibly to the same site, so raising the agonist concentration displaces it: the agonist curve shifts right in parallel with no change in maximum. The shift ratio follows the Schild equation and gives the antagonist's affinity (pA2). A non-competitive antagonist binds irreversibly or at a different site that prevents activation; raising the agonist cannot overcome it and the maximum falls. Naloxone reverses opioid overdose competitively, so a large dose of a potent opioid needs more naloxone; phenoxybenzamine blocks alpha-receptors irreversibly, so adrenaline surges in phaeochromocytoma cannot break through.

5. **Partial agonists are both agonist and antagonist, depending on context.** Buprenorphine occupies the opioid receptor with high affinity but low efficacy: alone, it relieves pain and causes less respiratory depression than morphine; in a patient full of heroin, it displaces the full agonist and precipitates withdrawal. The same logic underlies "stabilising" drugs that damp both excess and deficiency of a natural ligand.

6. **Receptors have constitutive activity, and inverse agonists turn it off.** The two-state model treats a receptor as flickering between inactive and active conformations even when empty. Agonists stabilise the active state, inverse agonists stabilise the inactive one and reduce basal signalling, and neutral antagonists bind both equally and only block. Many drugs long classed as antagonists (several antihistamines, some beta-blockers) are inverse agonists; the distinction matters when receptors are over-expressed or constitutively active.

7. **The receptor's type sets the timescale of the response.** Ion-channel receptors (nicotinic, GABA-A) respond in milliseconds; G-protein-coupled receptors through second messengers in seconds; kinase-linked receptors (insulin, growth factors) in minutes to hours; nuclear receptors (steroids, thyroid hormone) by altering transcription over hours to days. A drug's onset and offset follow the receptor's class before they follow its kinetics, which is why corticosteroids take hours to act whatever their plasma profile.

8. **Not all drugs act at receptors.** Enzyme inhibitors (statins at HMG-CoA reductase, aspirin at cyclo-oxygenase), ion-channel blockers (local anaesthetics), transporter inhibitors (selective serotonin reuptake inhibitors, loop diuretics), and agents acting by physical chemistry (antacids neutralising acid, osmotic diuretics, chelators) all have targets but not receptors in the signalling sense. The mass-action logic still applies to any reversible binding, but "efficacy" means something different when the target is a pump or an enzyme.

## Key concepts

| Term | Meaning |
|---|---|
| Affinity | Strength of binding; the inverse of the dissociation constant Kd |
| Efficacy (intrinsic activity) | The response per occupied receptor; zero for a pure antagonist, maximal for a full agonist |
| Potency | Concentration needed for a given effect (EC50); combines affinity, efficacy and spare receptors |
| Agonist, partial agonist, antagonist, inverse agonist | Ligands with full, submaximal, zero or negative efficacy respectively |
| Competitive antagonism | Reversible binding at the agonist site; surmountable, parallel rightward shift |
| Non-competitive antagonism | Irreversible or allosteric block; lowers the maximal response |
| Spare receptors | Receptors beyond the number needed for a maximal response; make EC50 lower than Kd |
| Two-state model | Receptors switch between inactive and active conformations; ligands shift the equilibrium |
| Schild equation and pA2 | Relation between antagonist concentration and the rightward shift it causes; pA2 measures antagonist affinity |
| Allosteric modulator | Ligand binding at a second site that changes the response to the primary ligand (benzodiazepines at GABA-A) |

## How it fits

- **Below:** The receptor families and their signalling cascades are in [receptors and ligands](../../02-biochemistry-and-molecular-biology/04-cell-signalling/receptors-and-ligands.md) and [amplification](../../02-biochemistry-and-molecular-biology/04-cell-signalling/signal-amplification-integration-and-termination.md); the binding chemistry is [molecular recognition](../../00-physical-and-chemical-foundations/02-chemistry-of-life/carbon-chemistry-and-molecular-recognition.md). The assumption is a reversible equilibrium at a single class of sites.
- **Above:** Every leaf in [drug classes by mechanism](../03-drug-classes-by-mechanism/README.md) is an instance; [target validation](../05-drug-development-and-toxicology/from-target-to-approval.md) begins with these measurements; reversal of overdose in [emergency medicine](../../13-acute-perioperative-and-procedural-care/04-emergency-medicine/poisoning-and-overdose.md) is applied competitive antagonism.
- **Siblings:** This leaf gives the curve's shape; [dose–response](dose-response-and-therapeutic-index.md) uses it in a population; [tolerance](tolerance-dependence-and-withdrawal.md) is the receptor equilibrium shifting over days; [adverse reactions](adverse-drug-reactions-and-pharmacovigilance.md) often arise because the same receptor sits in a second tissue.

## Common misconceptions

- **"A more potent drug is a better drug."** Potency only says how little is needed; efficacy says how much effect is possible. A low-potency full agonist outperforms a high-potency partial agonist at maximal effect.
- **"An antagonist has an effect of its own."** A neutral antagonist does nothing unless the endogenous agonist is present; its effect is the absence of that agonist's action. Inverse agonists are the exception.
- **"Half the receptors are occupied at the EC50."** Only in a system without spare receptors; with amplification, half-maximal response may occur at a few percent occupancy.

## Go deeper

- Humphrey Rang, James Ritter, Rod Flower and Graeme Henderson, *Rang & Dale's Pharmacology* (9th ed., 2019), chapters 2–3: the clearest textbook derivation of occupancy, efficacy and antagonism.
- Terry Kenakin, *A Pharmacology Primer* (5th ed., 2018): receptor theory for those who want the equations and their experimental basis.
- James Black and Paul Leff, "Operational models of pharmacological agonism" (*Proceedings of the Royal Society B*, 1983): the operational model that separates affinity from efficacy in practice.
