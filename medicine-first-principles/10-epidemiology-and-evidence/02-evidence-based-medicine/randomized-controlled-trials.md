# Randomized controlled trials

> **Layer:** [10 Epidemiology and Evidence](../README.md) › [Evidence-based medicine](README.md)
> **Builds on:** [Bias, confounding and chance](../01-epidemiology/bias-confounding-and-chance.md), [Measures of frequency and association](../01-epidemiology/measures-of-frequency-and-association.md), [Hypothesis testing and confidence intervals](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md), [Behaviour change and the placebo effect](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/behaviour-change-and-the-placebo-effect.md)
> **Enables:** [Systematic reviews and meta-analysis](systematic-reviews-and-meta-analysis.md), [Grading evidence and guidelines](grading-evidence-and-guidelines.md), [From target to approval](../../09-pharmacology-and-therapeutics/05-drug-development-and-toxicology/from-target-to-approval.md), [Principles of cancer care](../../12-organ-system-specialties/07-oncology/principles-of-cancer-care.md)

## Essence

The Randomized Controlled Trial (RCT) is the one study design that answers "does this treatment work?" without having to know what else differs between treated and untreated people. Its trick is to let a coin, not a doctor or a patient, decide who gets the treatment. Randomisation makes the two groups alike, on average, in every characteristic, measured or unmeasured, so that any difference in outcome larger than chance must be caused by the treatment. Everything else in trial design (concealment, blinding, intention-to-treat analysis, pre-specified outcomes, sample size) exists to protect that one guarantee from the ways people and investigators can undo it.

## Core tenets

1. **Randomisation removes confounding, including by variables nobody thought of.** In an observational study the treated differ from the untreated in whatever made someone prescribe the treatment ([confounding by indication](../01-epidemiology/bias-confounding-and-chance.md)). With random allocation, the expected distribution of every baseline variable is identical in both arms, and the only systematic difference is the treatment. Small trials can be unbalanced by chance, which the confidence interval already accounts for; what randomisation guarantees is that the imbalance is random, not systematic.

2. **Allocation concealment protects randomisation from the people enrolling patients.** If a recruiting clinician can foresee the next allocation (envelopes held to the light, alternation by date), they can steer sicker or healthier patients into one arm, and the groups are no longer exchangeable. Central or computerised randomisation that reveals the allocation only after a patient is irrevocably enrolled is the fix. Trials with inadequate concealment overestimate effects by roughly a third in empirical comparisons.

3. **Blinding protects the outcome from expectation.** A patient who knows they received the active drug reports less pain ([the placebo effect](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/behaviour-change-and-the-placebo-effect.md)), a clinician who knows reads the scan more kindly, an analyst who knows chooses the favourable model. Blinding patients, clinicians, outcome assessors and analysts makes measurement error non-differential. It matters most for subjective outcomes; death needs no blinding to count, though decisions that influence survival still do.

4. **Analyse by the group randomised, not the treatment received.** Patients stop drugs, cross over and are lost. Analysing only those who completed treatment reintroduces the selection that randomisation removed, because those who stop are different (sicker, more side-effects). *Intention-to-treat* analysis keeps every patient in the arm they were assigned, estimating the effect of the *policy* of offering treatment, which is what a clinician decides; it is conservative for superiority and dangerously lenient for non-inferiority trials, where sloppy adherence makes any two treatments look alike.

5. **The trial answers the question written down before it began.** The primary outcome, the hypothesis, the sample size and the analysis are pre-specified and registered (public registries since 2005) because a trial free to choose its outcome after seeing the data will find one. The sample size is set so that the trial has adequate power (usually 80–90%) to detect the smallest effect worth knowing about: a trial of 40 patients cannot show that a drug halves a 5% mortality, and its null result means nothing.

6. **Efficacy under ideal conditions and effectiveness in practice are different questions.** An explanatory trial selects adherent patients without comorbidity, titrates the drug and follows closely, maximising the chance of showing an effect. A pragmatic trial enrols the people a clinic actually sees. The first tells you whether the drug *can* work; the second whether it *does* when used as it will be. Trial populations are commonly younger, fitter and less multimorbid than the patients treated on their evidence, which is the gap that [frailty and polypharmacy](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md) exposes.

7. **A trial estimates an average effect in a population, not the effect in the patient in front of you.** The relative risk reduction is often fairly stable across baseline risks, so the absolute benefit (and the number needed to treat) is larger in higher-risk patients. Subgroup results are hypotheses, not findings, because of multiplicity. Applying a trial is a judgement that this patient resembles the trial population in what matters, which is the work of [clinical reasoning](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/clinical-reasoning-and-cognitive-bias.md).

## Key concepts

| Term | Meaning |
|---|---|
| Randomisation | Allocation to arms by a chance process, making groups exchangeable in expectation |
| Allocation concealment | Preventing those enrolling patients from foreseeing the next allocation |
| Blinding | Keeping patients, clinicians, assessors or analysts unaware of allocation |
| Intention-to-treat | Analysing every patient in the arm assigned, regardless of treatment received |
| Primary outcome | The single pre-specified outcome on which the trial's conclusion rests |
| Power | Probability of detecting a true effect of a stated size; set by sample size and variance |
| Non-inferiority margin | The largest loss of effect that would still count as "not worse" |
| Pragmatic versus explanatory | Trial designed to measure effect in routine practice versus under ideal conditions |
| Cluster randomisation | Randomising groups (practices, villages) rather than individuals, when the intervention acts on a group |
| Crossover trial | Each patient receives both treatments in random order; valid only when effects do not carry over |

## How it fits

- **Below:** the trial is the experimental answer to [bias and confounding](../01-epidemiology/bias-confounding-and-chance.md); its results are reported as the [measures of association](../01-epidemiology/measures-of-frequency-and-association.md); its sample size and interpretation rest on [hypothesis testing](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md).
- **Above:** trials are the units that [meta-analysis](systematic-reviews-and-meta-analysis.md) combines and that [guidelines](grading-evidence-and-guidelines.md) grade; phase III trials are the gate in [drug approval](../../09-pharmacology-and-therapeutics/05-drug-development-and-toxicology/from-target-to-approval.md); the evidence base of [oncology](../../12-organ-system-specialties/07-oncology/principles-of-cancer-care.md) and [cardiology](../../12-organ-system-specialties/01-cardiology/heart-failure.md) is a sequence of named trials.
- **Siblings:** [diagnostic accuracy studies](diagnostic-accuracy-studies.md) are the observational analogue for tests; [research integrity](research-integrity-and-publication-bias.md) covers what happens to trials after they finish.

## Common misconceptions

- **"A trial proves the drug works in everyone."**: it estimates an average effect in people who met the entry criteria; benefit and harm vary with baseline risk and the trial population is often unlike the clinic's.
- **"A non-significant trial shows the treatment does not work."**: an underpowered trial cannot distinguish no effect from a modest one; look at the confidence interval, not the p-value.
- **"Per-protocol analysis is more accurate because it analyses people who actually took the drug."**: it reintroduces selection, because the people who stop are not a random sample of those who started.

## Go deeper

- Austin Bradford Hill, "The clinical trial", *British Medical Bulletin* (1951): the rationale for randomisation from the designer of the 1948 streptomycin trial.
- Kenneth F. Schulz and David A. Grimes, *The Lancet Handbook of Essential Concepts in Clinical Research* (2006): short, precise chapters on concealment, blinding and sample size.
- Stuart J. Pocock, *Clinical Trials: A Practical Approach* (1983): the classic text on design and analysis.
