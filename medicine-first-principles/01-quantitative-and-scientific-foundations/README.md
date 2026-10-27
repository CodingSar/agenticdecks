# 01 Quantitative and Scientific Foundations

> **Layer:** 01 Quantitative and Scientific Foundations (formal root of the tree)
> **Children:** [Probability and Measurement](01-probability-and-measurement/README.md) · [Inference and Causation](02-inference-and-causation/README.md) · [Systems and Models](03-systems-and-models/README.md)

## What this area is about

Medicine is a quantitative science before it is a clinical one. A reference range is a percentile; a diagnosis is a probability revised by evidence; a drug's dosing interval is a half-life; homeostasis is a feedback loop with a gain; an epidemic is an exponential with a reproduction number; a treatment "works" when a trial excludes chance and confounding as explanations for a difference. This layer answers the question: *in what language are the body's workings, the evidence about them and the decisions made from them stated, and what does that language force one to get right?*

It has three children. [Probability and measurement](01-probability-and-measurement/README.md) deals with uncertainty in a single number: how probability behaves, what shapes it takes, how much of a measurement is noise and how a noisy result should update belief. [Inference and causation](02-inference-and-causation/README.md) deals with reasoning from samples to populations and from association to cause. [Systems and models](03-systems-and-models/README.md) deals with change over time: what a model is, pools and flows, feedback, thresholds and rhythms, and signals in noise.

The one idea this layer contributes to the stack is **reasoning under uncertainty about a dynamic system**. The body is never fully observed and never still; every number about it is a sample from a varying process, and every mechanism is a model that must predict something checkable. Later layers supply the content, the physiology, the diseases, the drugs. This layer supplies the forms: the probability, the interval, the loop, the exponential, the threshold, the signal.

## Why this layer sits here

This is the **formal root**. It depends on no other layer: probability, statistics, control theory and information theory were developed for coins, agriculture, telephones and gun turrets, and they would be true if no body existed. It sits beside [00 Physical and Chemical Foundations](../00-physical-and-chemical-foundations/README.md), the material root. The two are twins at the base of the tree: 00 says what the body is made of and what laws that matter obeys, 01 says in what language those laws, and everything built on them, are written. Because physics is written in mathematics, 00 may cite 01 ([entropy](01-probability-and-measurement/probability.md) is probability; radioactive decay is an [exponential process](03-systems-and-models/compartment-models-and-exponential-processes.md); allometry is a [regression](02-inference-and-causation/regression-adjustment-and-survival-analysis.md)); 01 never cites 00 as a prerequisite. That one-way link is the only upward reference the tree permits.

The layer is placed this low, rather than beside epidemiology at 10, because the layers in between already need it. [02 Biochemistry](../02-biochemistry-and-molecular-biology/README.md) describes enzyme kinetics as saturable rates and signalling as amplification with noise. [04 Genetics](../04-genetics-evolution-and-development/README.md) is probability applied to alleles and the normal distribution applied to polygenic traits. [06 Physiology](../06-physiology/README.md) is feedback and control from its first leaf.

```
   01 Quantitative and Scientific Foundations ──┐  (formal root: this layer)
        ▲ cited by 00 for its language          ├──► 02 Biochemistry ──► 03 Cell Biology ──► ... ──► 15
   00 Physical and Chemical Foundations ────────┘  (material root)
```

What the layers above need from this one: the rules of chance and the Bayesian update ([probability](01-probability-and-measurement/probability.md), [Bayesian reasoning](01-probability-and-measurement/bayesian-reasoning.md)); the normal curve, standard error and percentile ([distributions](01-probability-and-measurement/distributions-and-descriptive-statistics.md)); the reference range and the reference change value ([measurement error](01-probability-and-measurement/measurement-error-and-biological-variation.md)); the confidence interval and power ([hypothesis testing](02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md)); adjusted ratios, hazards and risk scores ([regression and survival](02-inference-and-causation/regression-adjustment-and-survival-analysis.md)); the counterfactual and the reason trials are randomised ([causal inference](02-inference-and-causation/causal-inference.md)); the standard of a falsifiable, replicated model ([the scientific method](03-systems-and-models/the-scientific-method-and-models.md)); half-life, clearance and steady state ([compartment models](03-systems-and-models/compartment-models-and-exponential-processes.md)); set point, gain and compensation ([feedback](03-systems-and-models/feedback-and-control.md)); thresholds, rhythms and cascades ([nonlinear dynamics](03-systems-and-models/nonlinear-dynamics-oscillations-and-networks.md)); and the signal-to-noise ratio and detection threshold ([information](03-systems-and-models/information-signals-and-noise.md)).

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Probability and Measurement](01-probability-and-measurement/README.md) | Uncertainty in one number: rules, shapes, noise, updating | Nothing (root) |
| [Inference and Causation](02-inference-and-causation/README.md) | From sample to population and from association to cause | Probability and measurement, the scientific method |
| [Systems and Models](03-systems-and-models/README.md) | Change over time: models, pools, loops, thresholds, signals | Probability (for noise and exponentials) |

Read probability and measurement first; it is the shortest and everything uses it. Systems and models can be read next or in parallel: its first leaf, the scientific method, is the frame for inference, and its compartment and feedback leaves are what physiology will use most. Inference and causation closes the layer: it decides what counts as evidence that a treatment works.

## Connections to neighbouring layers

- **[00 Physical and Chemical Foundations](../00-physical-and-chemical-foundations/README.md):** the twin root. It borrows this layer's probability, exponentials, regression and signal theory and returns nothing, by design.
- **[02 Biochemistry and Molecular Biology](../02-biochemistry-and-molecular-biology/README.md):** enzyme kinetics are saturable rates; signalling cascades are amplification and noise; feedback inhibition is control at the molecular scale.
- **[04 Genetics, Evolution and Development](../04-genetics-evolution-and-development/README.md):** Mendelian ratios are independent probabilities; heritability is a partition of variance; natural selection is a dynamical system.
- **[06 Physiology](../06-physiology/README.md):** the largest consumer. Homeostasis is negative feedback, hormone axes are nested loops, the heartbeat and circadian clock are limit cycles, sensory coding is information theory, clearance is a compartment model.
- **[08 Pathology](../08-pathology/README.md):** compensation and decompensation are a loop saturating; aetiology is component causation; natural history is a time course.
- **[09 Pharmacology and Therapeutics](../09-pharmacology-and-therapeutics/README.md):** pharmacokinetics is compartment modelling; dose–response is a binding hyperbola; whether a drug works is a trial question.
- **[10 Epidemiology and Evidence](../10-epidemiology-and-evidence/README.md):** this layer's inference leaves made into a discipline, plus epidemics as compartment models and screening as Bayes at population scale.
- **[11 Clinical Method and Diagnostics](../11-clinical-method-and-diagnostics/README.md):** Bayes at the bedside, reference ranges, prognostic regression, signal extraction from electrocardiograms and images, and the cognitive biases that distort probability judgement.

## Connections across layers

This layer gives the stack its standards of evidence and its recurring forms. The base-rate problem of [Bayesian reasoning](01-probability-and-measurement/bayesian-reasoning.md) reappears in [screening](../10-epidemiology-and-evidence/03-screening-and-prevention/screening-principles-and-biases.md) and in [artificial intelligence in health care](../15-medicine-in-society/01-health-systems/health-informatics-and-artificial-intelligence.md). The counterfactual of [causal inference](02-inference-and-causation/causal-inference.md) is why [randomised trials](../10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md) decide what [guidelines](../10-epidemiology-and-evidence/02-evidence-based-medicine/grading-evidence-and-guidelines.md) recommend and why [social determinants](../15-medicine-in-society/03-populations-and-the-future/social-determinants-and-health-inequity.md) are hard to prove. The loop of [feedback](03-systems-and-models/feedback-and-control.md) is [homeostasis](../06-physiology/01-integrative-principles/homeostasis-and-set-points.md), then [shock](../08-pathology/02-hemodynamic-disorders/hemorrhage-shock-and-sepsis.md) when it saturates, then [heart failure](../12-organ-system-specialties/01-cardiology/heart-failure.md) when counter-regulation becomes the disease. The exponential of [compartment models](03-systems-and-models/compartment-models-and-exponential-processes.md) is a [dosing interval](../09-pharmacology-and-therapeutics/01-pharmacokinetics/elimination-half-life-and-dosing.md), a [tumour's doubling time](../08-pathology/03-neoplasia/hallmarks-of-cancer.md) and a [pandemic's early weeks](../15-medicine-in-society/03-populations-and-the-future/global-health-and-pandemics.md). The network cascade of [nonlinear dynamics](03-systems-and-models/nonlinear-dynamics-oscillations-and-networks.md) is [multi-organ failure](../13-acute-perioperative-and-procedural-care/03-critical-care/sepsis-and-multi-organ-failure.md) in the young and [frailty](../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md) in the old.

## Cross-cutting threads

- [Probability and uncertainty](../CROSS-CUTTING.md#probability-and-uncertainty): the layer's organising idea; variation, risk and Bayes at every level.
- [Feedback and homeostasis](../CROSS-CUTTING.md#feedback-and-homeostasis): set point, gain, delay and oscillation, stated as mathematics.
- [Cause and mechanism](../CROSS-CUTTING.md#cause-and-mechanism): from association through confounding to component causes.
- [Time-courses](../CROSS-CUTTING.md#time-courses): half-life, steady state, doubling time, survival curves.
- [Compensation and decompensation](../CROSS-CUTTING.md#compensation-and-decompensation): a loop conceals the disturbance until its effector saturates.
- [Signalling and information](../CROSS-CUTTING.md#signalling-and-information): encoding, noise, redundancy and the detection threshold.
- [Harm and benefit](../CROSS-CUTTING.md#harm-and-benefit): test and treatment thresholds; effect sizes with intervals.
- [Redundancy and reserve](../CROSS-CUTTING.md#redundancy-and-reserve): redundancy in codes and networks is why one failure is survivable.
- [Dose–response](../CROSS-CUTTING.md#dose-response): a biological gradient as a regression slope and a criterion for causation.
