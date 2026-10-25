# The clinical encounter

> **Layer:** [11 Clinical Method and Diagnostics](../README.md) › The clinical encounter
> **Children:** [History taking and communication](history-taking-and-communication.md) · [Physical examination and signs](physical-examination-and-signs.md) · [Clinical reasoning and cognitive bias](clinical-reasoning-and-cognitive-bias.md) · [Using tests, pre-test probability and thresholds](using-tests-pretest-probability-and-thresholds.md) · [Prognosis and shared decision-making](prognosis-and-shared-decision-making.md)

## What this area is about

A patient arrives with a complaint. Within an hour, often within minutes, a clinician must decide what is probably wrong, how dangerous it is, whether a test would help, what to do, and what to tell the patient about what lies ahead. This area is the method by which that is done. It is the oldest part of medicine (Hippocratic case histories record it) and the part most recently given a formal basis, because the probability theory of layer 01 and the population measures of layer 10 turned out to describe what good clinicians were already doing.

The unifying idea is **Bayesian updating toward a decision**. The history and examination generate hypotheses and set their probabilities; each further finding or test multiplies the odds by a likelihood ratio; the resulting probability is compared with thresholds set by the consequences of acting or not; and prognosis extends the same probabilistic reasoning forward in time, where the patient's values decide between options. Cognitive bias is what happens when the fast, pattern-matching mind that performs this reasoning in practice takes shortcuts that the formal model would not.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [History taking and communication](history-taking-and-communication.md) | The richest source of evidence and the relationship within which everything else happens | [Information and noise](../../01-quantitative-and-scientific-foundations/03-systems-and-models/information-signals-and-noise.md); physiology of symptoms |
| [Physical examination and signs](physical-examination-and-signs.md) | Physical measurements made with the senses; each sign a test with a likelihood ratio | Physics of [pressure](../../00-physical-and-chemical-foundations/01-physics-of-the-body/fluids-pressure-and-flow.md) and [sound](../../00-physical-and-chemical-foundations/01-physics-of-the-body/waves-sound-light-and-radiation.md); anatomy |
| [Clinical reasoning and cognitive bias](clinical-reasoning-and-cognitive-bias.md) | Generating and testing hypotheses; fast and slow thinking and their failure modes | History, examination; [Bayes](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md) |
| [Using tests, pre-test probability and thresholds](using-tests-pretest-probability-and-thresholds.md) | When a test can change a decision: odds, likelihood ratios, the two thresholds | Reasoning; [diagnostic accuracy](../../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md) |
| [Prognosis and shared decision-making](prognosis-and-shared-decision-making.md) | What will happen, and choosing between options with the patient's values | [Risk prediction](../../10-epidemiology-and-evidence/03-screening-and-prevention/risk-prediction-and-stratification.md); [guidelines](../../10-epidemiology-and-evidence/02-evidence-based-medicine/grading-evidence-and-guidelines.md) |

```
   history  -->  hypotheses with prior probabilities
   examination -> each sign x likelihood ratio -> revised probabilities
                        |
   reasoning: most likely? most dangerous? what else?   (watch for anchoring, premature closure)
                        |
   probability vs thresholds -> no test | test (lab, imaging) | treat
                        |
   prognosis: with and without each option -> shared decision with the patient's values
```

Read in order. The history and examination are the inputs; reasoning is the engine; tests and thresholds are where probability becomes action; prognosis and shared decision-making are where the decision meets the person. The laboratory and imaging parents that follow in this layer are the tests that the fourth child decides whether to order.

## Connections to sibling areas

- **[Laboratory medicine](../02-laboratory-medicine/README.md):** every laboratory result is interpreted against the pre-test probability set here, and the reference range is a threshold whose false-positive rate the clinician must carry in mind. The laboratory also returns information the encounter cannot obtain (a potassium, a culture, a tissue diagnosis), and the clinician's job is to have asked a question the result can answer.
- **[Imaging and physiological measurement](../03-imaging-and-physiological-measurement/README.md):** imaging is the examination's physics extended by instruments (ultrasound as palpation with sound; the electrocardiogram as the pulse written down), and it generates incidental findings whose interpretation depends on the pre-test probability. Which modality to order, and whether to order any, is the threshold decision of the fourth child.

## Connections across layers

From below, the encounter takes [Bayesian reasoning](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md) as its normative model, the [signals-and-noise](../../01-quantitative-and-scientific-foundations/03-systems-and-models/information-signals-and-noise.md) view of a symptom, the physics of [pressure](../../00-physical-and-chemical-foundations/01-physics-of-the-body/fluids-pressure-and-flow.md) and [sound](../../00-physical-and-chemical-foundations/01-physics-of-the-body/waves-sound-light-and-radiation.md) behind every sign, the [natural history](../../08-pathology/05-disease-as-process/etiology-pathogenesis-and-natural-history.md) of disease as the time course the history reconstructs, and from layer 10 the prevalences, [likelihood ratios](../../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md), [effect sizes](../../10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md) and [risk scores](../../10-epidemiology-and-evidence/03-screening-and-prevention/risk-prediction-and-stratification.md) that fill in the numbers.

To the layers above it gives the method every specialty uses: the symptoms and signs listed in each disease leaf of [12](../../12-organ-system-specialties/README.md) are features with likelihood ratios; [triage](../../13-acute-perioperative-and-procedural-care/04-emergency-medicine/triage-and-the-abcde-approach.md) and [the surgical decision](../../13-acute-perioperative-and-procedural-care/01-surgery/the-surgical-decision.md) are reasoning under time pressure and threshold analysis respectively; the [psychiatric formulation](../../14-life-course-mind-and-integrative-care/03-psychiatry/the-mental-state-and-psychiatric-formulation.md) and [generalist consultation](../../14-life-course-mind-and-integrative-care/05-primary-care-and-integration/family-medicine-and-the-generalist.md) are the encounter in its purest form; and [consent](../../15-medicine-in-society/02-ethics-law-and-the-profession/consent-capacity-and-confidentiality.md), [patient safety](../../15-medicine-in-society/01-health-systems/patient-safety-and-quality-improvement.md) and [health economics](../../15-medicine-in-society/01-health-systems/health-economics-and-priority-setting.md) each take one aspect of it (the conversation, the error, the cost) as their subject.

## Cross-cutting threads

- [Probability and uncertainty](../../CROSS-CUTTING.md#probability-and-uncertainty): the whole area is Bayesian updating under uncertainty, and the honest output of an encounter is often a probability.
- [Harm and benefit](../../CROSS-CUTTING.md#harm-and-benefit): the thresholds are set by the harms of each error; shared decision-making weighs them with the patient.
- [Signalling and information](../../CROSS-CUTTING.md#signalling-and-information): the symptom is a noisy signal from a mechanism; the history is its decoding.
- [Time courses](../../CROSS-CUTTING.md#time-courses): tempo of onset is the most discriminating feature in a history; prognosis is probability over time.
- [Cause and mechanism](../../CROSS-CUTTING.md#cause-and-mechanism): differentials organised by mechanism widen the search that pattern recognition narrows.
