# Epidemiology

> **Layer:** [10 Epidemiology and Evidence](../README.md) › Epidemiology
> **Children:** [Measures of frequency and association](measures-of-frequency-and-association.md) · [Observational study designs](observational-study-designs.md) · [Bias, confounding and chance](bias-confounding-and-chance.md) · [Infectious disease dynamics](infectious-disease-dynamics.md) · [Surveillance and outbreak investigation](surveillance-and-outbreak-investigation.md)

## What this area is about

Epidemiology is the study of how disease is distributed in populations and of what determines that distribution. It answers questions no examination of a single patient can: how common is this condition, who gets it, what raises or lowers the risk, and is a rise in cases real? Its unit of observation is the population, its instrument is the count, and its central difficulty is that populations cannot be put in a laboratory. People choose their own exposures, remember them imperfectly, leave studies and differ from one another in ways that also affect disease. Epidemiology is the set of methods for extracting valid inferences about cause and frequency from data generated under those conditions.

The one idea that unifies the children is **comparison under a known denominator**. A count becomes a frequency when divided by the population and time that could have produced it; a frequency becomes evidence of cause when compared with the frequency in people who differ only in the exposure. Every design is a scheme for making that comparison, every bias is a way the comparison can be unfair, and infectious disease is the case in which the comparison groups infect one another.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Measures of frequency and association](measures-of-frequency-and-association.md) | The quantities: prevalence, incidence, relative risk, risk difference, number needed to treat | [Probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md) |
| [Observational study designs](observational-study-designs.md) | The sampling schemes that estimate those quantities when experiment is impossible | Measures; [causal inference](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/causal-inference.md) |
| [Bias, confounding and chance](bias-confounding-and-chance.md) | The three non-causal explanations of any association, and how design defends against them | Designs; [hypothesis testing](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md) |
| [Infectious disease dynamics](infectious-disease-dynamics.md) | What changes when one person's risk depends on another's: R0, herd immunity, epidemic curves | Measures; [compartment models](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md) |
| [Surveillance and outbreak investigation](surveillance-and-outbreak-investigation.md) | The method run continuously and in the field, linked to action | All four |

```
   count / denominator / time  -->  frequency (prevalence, incidence)
                |
   compare exposed vs unexposed  -->  association (RR, RD, OR, NNT)
                |
   design the comparison (cohort, case-control, cross-sectional)
                |
   rule out bias, confounding, chance  -->  causal judgement
                |                                 |
   risks depend on each other (R0, herd immunity)  surveillance: run it continuously
```

Read measures first: nothing else makes sense until incidence and prevalence, ratios and differences are distinct in your mind. Designs come next because each design can only produce certain measures. Bias, confounding and chance is the critical core: it is the reason the field exists as a discipline rather than as bookkeeping. Infectious disease dynamics is a deliberate break, showing where the independence assumed so far fails. Surveillance and outbreak investigation closes by applying everything under time pressure.

## Connections to sibling areas

- **[Evidence-based medicine](../02-evidence-based-medicine/README.md):** the randomised trial is the one design that removes confounding by construction; it is an experiment conducted with epidemiological measures and judged by epidemiological standards of bias. Diagnostic accuracy studies and meta-analyses are observational designs with their own bias catalogues. Everything in that parent presupposes this one.
- **[Screening and prevention](../03-screening-and-prevention/README.md):** screening is a population intervention whose apparent benefit is inflated by specific selection and time biases (lead time, length, overdiagnosis), and risk prediction is the regression modelling of observational cohorts turned into a tool for one person. Prevention strategy depends on the population attributable fraction introduced here.

## Connections across layers

From below, this area takes [probability and distributions](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/README.md) (a rate is an estimated probability), [inference and causation](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/README.md) (confidence intervals, regression adjustment, causal diagrams), [compartment models](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md) for epidemic dynamics, the [chain of infection](../../07-microbiology-and-immunology/01-microbes-and-infection/transmission-and-the-chain-of-infection.md) and [vaccination](../../07-microbiology-and-immunology/03-adaptive-immunity/immunological-memory-and-vaccination.md) from microbiology and immunology, and the model of disease as [multifactorial risk](../../08-pathology/05-disease-as-process/multifactorial-disease-and-risk.md) from pathology.

To the layers above it gives the prevalences that are a clinician's [pre-test probabilities](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md), the risk factors and relative risks cited by every specialty leaf (for example [ischaemic heart disease](../../12-organ-system-specialties/01-cardiology/ischemic-heart-disease.md) and [stroke](../../12-organ-system-specialties/10-neurology/stroke.md)), the observational evidence for [adverse drug reactions](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/adverse-drug-reactions-and-pharmacovigilance.md), the surveillance methods of [infection control](../../12-organ-system-specialties/08-infectious-diseases/infection-control-and-healthcare-associated-infection.md), and the evidence base for [social determinants of health](../../15-medicine-in-society/03-populations-and-the-future/social-determinants-and-health-inequity.md) and [pandemic response](../../15-medicine-in-society/03-populations-and-the-future/global-health-and-pandemics.md).

## Cross-cutting threads

- [Probability and uncertainty](../../CROSS-CUTTING.md#probability-and-uncertainty): every frequency is an estimate with sampling error; every association is a probability statement.
- [Cause and mechanism](../../CROSS-CUTTING.md#cause-and-mechanism): the Bradford Hill considerations and the taxonomy of confounding are the field's account of how association becomes cause.
- [The host and its environment](../../CROSS-CUTTING.md#the-host-and-its-environment): exposures, behaviours and social position are the independent variables of epidemiology.
- [Feedback and homeostasis](../../CROSS-CUTTING.md#feedback-and-homeostasis): epidemic dynamics are a feedback loop between prevalence and incidence, the only place in the layer where the output drives the input.
- [Dose–response](../../CROSS-CUTTING.md#dose-response): a biological gradient between exposure and risk is one of the strongest arguments for causation.
- [Time courses](../../CROSS-CUTTING.md#time-courses): incubation, latency, generation interval and the shape of the epidemic curve.
