# Risk prediction and stratification

> **Layer:** [10 Epidemiology and Evidence](../README.md) › [Screening and prevention](README.md)
> **Builds on:** [Regression, adjustment and survival analysis](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md), [Measures of frequency and association](../01-epidemiology/measures-of-frequency-and-association.md), [Complex traits and heritability](../../04-genetics-evolution-and-development/01-inheritance/complex-traits-and-heritability.md), [Levels of prevention](levels-of-prevention.md)
> **Enables:** [Prognosis and shared decision-making](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/prognosis-and-shared-decision-making.md), [Hypertension and vascular disease](../../12-organ-system-specialties/01-cardiology/hypertension-and-vascular-disease.md), [Perioperative risk and complications](../../13-acute-perioperative-and-procedural-care/02-anaesthesia-and-perioperative-medicine/perioperative-risk-and-complications.md), [Health informatics and artificial intelligence](../../15-medicine-in-society/01-health-systems/health-informatics-and-artificial-intelligence.md)

## Essence

A risk prediction model takes what is known about a person now (age, sex, blood pressure, smoking, a biomarker, a genotype) and returns the probability of an outcome over a stated horizon: a 10-year risk of cardiovascular disease, a 30-day risk of death after surgery, the probability that a chest pain is a myocardial infarction. It is the quantitative form of the high-risk strategy of prevention and of prognosis at the bedside. The model is a regression equation fitted to a cohort; its worth is measured by discrimination (does it rank people correctly?) and calibration (are its probabilities right?), and its central limitation is that most people who will have the event are not in the high-risk group, because risk is spread thinly across a large population at modest risk.

## Core tenets

1. **A prediction model is an association model, and it need not be causal.** The variables in a cardiovascular risk score are chosen because they predict, not because changing them changes the outcome; age predicts and cannot be changed, and a marker that is a consequence of early disease predicts well for that reason. This is the opposite of the [causal](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/causal-inference.md) question. Confusing the two leads to the belief that lowering a predictor will lower risk by the amount the model implies, which is true only for causal predictors acted on by interventions proven in trials.

2. **The model is a regression fitted to a cohort, and it inherits the cohort.** Logistic regression gives a probability at a fixed time; Cox regression gives it over time with censoring ([survival analysis](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md)). The Framingham equations were fitted to a largely white American town from 1948; applied elsewhere they over- or under-predict, which is why regions refit their own (QRISK in the United Kingdom, SCORE in Europe). A model's baseline risk is the cohort's, and it drifts as populations and treatments change.

3. **Discrimination and calibration are different virtues, and a model can have one without the other.** *Discrimination* is the ability to rank: the c-statistic (area under the receiver operating characteristic curve) is the probability that a random person with the event was given a higher risk than a random person without it; 0.5 is a coin toss, cardiovascular scores reach about 0.75–0.80. *Calibration* is the agreement between predicted and observed risk across the range: a model that says 10% to a group in which 20% have events is miscalibrated even if it ranks perfectly. Calibration decays faster with time and place than discrimination does.

4. **Validation in new data is the only evidence that a model works, and most models never receive it.** A model fitted and tested on the same data overfits: it learns the cohort's noise and performs worse elsewhere. Internal validation (cross-validation, bootstrapping) corrects optimism; external validation in a different population, time and setting is the real test. Thousands of prediction models are published; few are externally validated, fewer are compared with existing ones, and almost none have been shown in a trial to improve outcomes when used.

5. **A threshold turns a probability into a decision, and the threshold is a value judgement.** Treating everyone above a 10% ten-year cardiovascular risk is a choice about how many people to treat per event prevented (the number needed to treat rises as the threshold falls) and how much harm to accept. Decision-curve analysis compares strategies across thresholds by net benefit. Lowering a threshold always increases the number treated far more than the number helped, because the newly eligible are at lower risk.

6. **Genomic and machine-learned predictors add information at the margin and inherit every problem above.** Polygenic risk scores summarise thousands of variants from [complex-trait](../../04-genetics-evolution-and-development/01-inheritance/complex-traits-and-heritability.md) studies; for common diseases they reclassify some people but add modestly to conventional factors, and they transfer poorly between ancestries because the discovery cohorts were mostly European. Machine-learning models fitted to electronic records can discriminate well and calibrate badly, learn the practices of the hospital rather than the biology of the patient, and fail silently when the data pattern shifts ([health informatics](../../15-medicine-in-society/01-health-systems/health-informatics-and-artificial-intelligence.md)). The validation standards are the same, and so is the gap between accuracy and benefit.

## Key concepts

| Term | Meaning |
|---|---|
| Prediction model (risk score) | An equation giving the probability of an outcome from a person's characteristics |
| Prognostic versus diagnostic model | Predicting a future event versus the presence of a current condition |
| Discrimination (c-statistic) | Ability to rank those who will have the event above those who will not |
| Calibration | Agreement between predicted and observed risk across the range |
| Overfitting | A model that learns the development data's noise and performs worse in new data |
| External validation | Testing a model in a population, place or time different from the one it was fitted to |
| Decision threshold | The predicted risk above which an action is taken; a value judgement |
| Reclassification | The share of people moved across a threshold by adding a predictor |
| Polygenic risk score | Weighted sum of many common genetic variants predicting a complex trait |

## How it fits

- **Below:** the models are [regression and survival analysis](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md) fitted to cohorts; their outputs are the [risks](../01-epidemiology/measures-of-frequency-and-association.md) of epidemiology; genetic predictors come from [complex traits and heritability](../../04-genetics-evolution-and-development/01-inheritance/complex-traits-and-heritability.md).
- **Above:** a risk estimate is the starting point of [prognosis and shared decision-making](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/prognosis-and-shared-decision-making.md); cardiovascular scores drive the treatment of [hypertension and lipids](../../12-organ-system-specialties/01-cardiology/hypertension-and-vascular-disease.md); surgical scores inform [perioperative risk](../../13-acute-perioperative-and-procedural-care/02-anaesthesia-and-perioperative-medicine/perioperative-risk-and-complications.md); early-warning scores on wards and [triage](../../13-acute-perioperative-and-procedural-care/04-emergency-medicine/triage-and-the-abcde-approach.md) are prediction models applied in minutes.
- **Siblings:** stratification is the instrument of the high-risk strategy in [levels of prevention](levels-of-prevention.md); targeting [screening](screening-principles-and-biases.md) by predicted risk raises prevalence and so predictive value.

## Common misconceptions

- **"A risk of 15% means the model is uncertain."**: it is a calibrated probability: of 100 people like this, about 15 will have the event. The uncertainty is in who, not in the number.
- **"Lowering a predictor lowers risk by what the model says."**: only if the predictor is causal and the intervention has been shown to work; a risk score is not a treatment model.
- **"A model with a high c-statistic can be used."**: it must also be calibrated in the population where it is used, and using it must be shown to help, which is a separate question.

## Go deeper

- Ewout W. Steyerberg, *Clinical Prediction Models* (2nd ed., 2019): the standard text on development, validation and updating.
- Gary S. Collins and colleagues, "Transparent reporting of a multivariable prediction model for individual prognosis or diagnosis (TRIPOD)", *Annals of Internal Medicine* (2015): the reporting standard, which lists what a model must demonstrate.
- Geoffrey Rose, *The Strategy of Preventive Medicine* (1992): why high-risk strategies capture a minority of events.
