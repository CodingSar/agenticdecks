# Adverse drug reactions and pharmacovigilance

> **Layer:** [09 Pharmacology and Therapeutics](../README.md) › [Pharmacodynamics](README.md)
> **Builds on:** [Dose–response and therapeutic index](dose-response-and-therapeutic-index.md), [Hypersensitivity and allergy](../../07-microbiology-and-immunology/04-immunity-in-disease/hypersensitivity-and-allergy.md), [Antigen presentation and MHC](../../07-microbiology-and-immunology/03-adaptive-immunity/antigen-presentation-and-mhc.md), [Probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md), [Causal inference](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/causal-inference.md)
> **Enables:** [From target to approval](../05-drug-development-and-toxicology/from-target-to-approval.md), [Observational study designs](../../10-epidemiology-and-evidence/01-epidemiology/observational-study-designs.md), [Patient safety and quality improvement](../../15-medicine-in-society/01-health-systems/patient-safety-and-quality-improvement.md), [Frailty, multimorbidity and polypharmacy](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md), [Allergy and immunodeficiency in practice](../../12-organ-system-specialties/09-rheumatology-and-clinical-immunology/allergy-and-immunodeficiency-in-practice.md)

## Essence

Every drug that does something can do something unwanted. Most adverse drug reactions (ADRs) are the drug's known pharmacology appearing in the wrong tissue, at the wrong dose or in the wrong patient; these are predictable, dose-related and common. A minority are not predictable from the pharmacology at all: immune responses to the drug or its metabolite, and idiosyncratic reactions arising from rare genetic differences. Because the rare reactions occur too seldom to be seen in trials of a few thousand people, every drug enters the market with its rare harms unknown, and pharmacovigilance is the system of reporting and epidemiology that discovers them afterwards. The single idea is that harm is the other dose–response curve, and the question for any suspected reaction is whether the drug caused it, which is a problem in causal inference.

## Core tenets

1. **Type A reactions are augmented pharmacology: dose-related, predictable and the large majority.** A beta-blocker slows the heart (the intended action) and causes bronchospasm (the same receptor in the airways) and fatigue (the same receptor in the brain); an anticoagulant causes bleeding; a hypoglycaemic agent causes hypoglycaemia. They account for roughly 80% of ADRs, they are read directly from the [toxicity curve](dose-response-and-therapeutic-index.md), and they are managed by reducing dose, which is why they are the reactions that kinetics (renal failure, interactions, age) make more likely.

2. **Type B reactions are bizarre: unrelated to known pharmacology, not dose-related, rare and often severe.** Anaphylaxis to penicillin, agranulocytosis with clozapine, Stevens–Johnson syndrome with carbamazepine, hepatitis with isoniazid. They affect a susceptible minority, they cannot be predicted from the drug's action and they recur on re-exposure, so the only management is withdrawal and avoidance. The extended classification adds type C (chronic, from cumulative use: adrenal suppression), type D (delayed: carcinogenesis, teratogenesis), type E (end of use: withdrawal) and type F (failure of therapy).

3. **Immune-mediated reactions follow the hypersensitivity types, and most drugs become antigens only as haptens.** Small molecules are not immunogenic until they bind covalently to a protein (penicillin's beta-lactam ring acylates lysine residues), after which the conjugate can provoke immunoglobulin E (IgE)-mediated anaphylaxis (type I), antibody-mediated cytopenia (type II), immune-complex serum sickness (type III) or T-cell-mediated rashes and severe cutaneous reactions (type IV). Some drugs bind non-covalently to a particular human leukocyte antigen (HLA) molecule and alter which peptides it presents; abacavir hypersensitivity with HLA-B*57:01 and carbamazepine severe cutaneous reactions with HLA-B*15:02 are the clearest cases, which [pharmacogenomics](pharmacogenomics-and-individual-variation.md) now screens for.

4. **The rare reactions are invisible before marketing because of the rule of three.** If an event has not occurred in n exposed people, its true rate is, with 95% confidence, below about 3/n. A programme of 3,000 patients therefore cannot exclude a reaction occurring once per 1,000, and typically cannot see one per 10,000, the frequency at which many serious type B reactions occur. Trials also exclude the elderly, the pregnant, the multi-morbid and those on many other drugs, who are the people most exposed to the drug afterwards. Pre-marketing safety data are necessarily incomplete.

5. **Pharmacovigilance detects signals from spontaneous reports and confirms them with epidemiology.** Spontaneous reporting systems (the Yellow Card scheme in the United Kingdom, from 1964; the Food and Drug Administration's MedWatch; the World Health Organization's VigiBase) collect suspected reactions from clinicians and patients. Disproportionality analysis asks whether a drug–event pair appears more often than expected from the database as a whole. A signal is then tested in cohort or case–control studies in prescription databases, which supply the denominator that spontaneous reports lack. Thalidomide (1961) created the modern system; rofecoxib's cardiovascular risk (withdrawn 2004) showed that a common, non-specific event can hide for years even when it is large in absolute terms.

6. **Attributing an individual reaction to a drug is causal reasoning, not pattern matching.** The evidence is temporal plausibility (onset after exposure, within a window consistent with the mechanism), dechallenge (improvement on stopping), rechallenge (recurrence on restarting, rarely justified), absence of alternative explanation, and prior knowledge of the reaction. Formal algorithms (Naranjo, 1981) score these. Underreporting is the system's weakness: fewer than 10% of serious reactions are thought to be reported, and events that resemble the disease being treated are the least likely to be recognised.

7. **Harm is concentrated in the old, the many-drugged and the kinetically compromised.** ADRs cause around 5–10% of acute hospital admissions in high-income countries (United Kingdom studies, 2000s–2010s), most of them type A reactions to a small set of drug classes: anticoagulants, antiplatelets, diuretics, non-steroidal anti-inflammatory drugs, opioids and hypoglycaemics. The risk rises with the number of drugs faster than linearly, because interactions scale with pairs; this is the quantitative reason for [polypharmacy review](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md) and a central concern of [patient safety](../../15-medicine-in-society/01-health-systems/patient-safety-and-quality-improvement.md).

## Key concepts

| Term | Meaning |
|---|---|
| Adverse drug reaction (ADR) | A harmful, unintended response to a drug at normal doses; distinct from a medication error or overdose |
| Type A (augmented) | Dose-related, predictable extension of pharmacology; the majority |
| Type B (bizarre) | Not dose-related, unpredictable, often immune or idiosyncratic; rare and severe |
| Hapten | A small molecule that becomes immunogenic by binding covalently to a protein |
| Signal | A reported drug–event association that warrants investigation |
| Spontaneous reporting | Voluntary submission of suspected reactions to a national database |
| Disproportionality analysis | Statistical screen for drug–event pairs over-represented in a reporting database |
| Dechallenge and rechallenge | Observing the effect of stopping and restarting a drug on a suspected reaction |
| Rule of three | With zero events in n people, the upper 95% bound on the rate is approximately 3/n |
| Severe cutaneous adverse reaction | T-cell-mediated skin reactions such as Stevens–Johnson syndrome and toxic epidermal necrolysis |

## How it fits

- **Below:** Type A reactions are the [toxicity curve](dose-response-and-therapeutic-index.md); type B immune reactions are [hypersensitivity](../../07-microbiology-and-immunology/04-immunity-in-disease/hypersensitivity-and-allergy.md) with a drug as antigen and [MHC presentation](../../07-microbiology-and-immunology/03-adaptive-immunity/antigen-presentation-and-mhc.md) as the genetic filter; the rule of three is [probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md); attribution is [causal inference](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/causal-inference.md).
- **Above:** Post-marketing surveillance is the last phase of [drug development](../05-drug-development-and-toxicology/from-target-to-approval.md); its methods are the [observational designs](../../10-epidemiology-and-evidence/01-epidemiology/observational-study-designs.md) of epidemiology; drug allergy labels are managed in [clinical immunology](../../12-organ-system-specialties/09-rheumatology-and-clinical-immunology/allergy-and-immunodeficiency-in-practice.md).
- **Siblings:** [Pharmacogenomics](pharmacogenomics-and-individual-variation.md) explains the susceptible minority in type B and the slow metabolisers in type A; [withdrawal](tolerance-dependence-and-withdrawal.md) is type E; the whole area rests on [receptor theory](receptor-theory-agonists-and-antagonists.md), since the commonest reason for an unwanted effect is the receptor's presence in a second tissue.

## Common misconceptions

- **"A drug approved by regulators has been shown to be safe."** It has been shown to have no common serious harms in a selected population; rare harms are discovered after approval, by design of the system.
- **"A reaction listed as 'allergy' in the notes is an immune reaction."** Most recorded penicillin "allergies" are intolerances, side effects or childhood rashes of unknown cause; around 90% of people with the label tolerate penicillin on testing, and the label itself causes harm by forcing worse alternatives.
- **"Side effects are a sign the dose is too high."** Only for type A reactions; type B reactions occur at any dose and require withdrawal, not reduction.

## Go deeper

- Jeffrey Aronson and Robin Ferner, "Joining the DoTS: new approach to classifying adverse drug reactions" (*BMJ*, 2003): classification by dose, time and susceptibility, the modern successor to A/B.
- Munir Pirmohamed and colleagues, "Adverse drug reactions as cause of admission to hospital" (*BMJ*, 2004): the prospective study of 18,820 admissions behind the 6.5% figure.
- Patrick Waller and Mira Harrison-Woolrych, *An Introduction to Pharmacovigilance* (2nd ed., 2017): the reporting systems and the epidemiology of signal confirmation.
