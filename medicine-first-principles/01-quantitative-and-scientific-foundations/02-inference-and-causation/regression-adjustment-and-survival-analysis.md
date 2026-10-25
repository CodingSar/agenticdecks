# Regression, Adjustment and Survival Analysis

> **Layer:** [01 Quantitative and Scientific Foundations](../README.md) › [Inference and Causation](README.md)
> **Builds on:** [Distributions and descriptive statistics](../01-probability-and-measurement/distributions-and-descriptive-statistics.md), [Hypothesis testing and confidence intervals](hypothesis-testing-and-confidence-intervals.md), [Compartment models and exponential processes](../03-systems-and-models/compartment-models-and-exponential-processes.md)
> **Enables:** [Observational study designs](../../10-epidemiology-and-evidence/01-epidemiology/observational-study-designs.md), [Risk prediction and stratification](../../10-epidemiology-and-evidence/03-screening-and-prevention/risk-prediction-and-stratification.md), [Prognosis and shared decision making](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/prognosis-and-shared-decision-making.md), [Scale and allometry](../../00-physical-and-chemical-foundations/01-physics-of-the-body/scale-and-allometry.md)

## Essence

Most medical questions involve many variables at once: does this drug lower mortality *after allowing for* the fact that the patients who received it were older and sicker? How much does each of smoking, blood pressure and cholesterol contribute to a person's ten-year risk? How long do patients survive when some are still alive at the end of the study? Regression is the general tool for describing how an outcome depends on several inputs together, and adjustment is its use to compare like with like when randomisation was not possible. Survival analysis extends it to time-to-event data, where the central fact is that not everyone has had the event yet. These methods produce most of the numbers in modern medical literature: adjusted odds ratios, hazard ratios and risk scores. They are powerful and routinely over-trusted, because a model can only adjust for what was measured.

## Core tenets

1. **Regression fits a line (or surface) that predicts an outcome from predictors; the coefficient is the change in outcome per unit predictor, holding the others fixed.** In linear regression, `y = a + b₁x₁ + b₂x₂ + …`; `b₁` is the expected change in y for one unit of x₁ when x₂ and the rest are unchanged. Blood pressure regressed on age and weight gives the effect of a year of age at constant weight. The "holding fixed" is statistical, not experimental: it compares people who differ in x₁ but happen to share x₂, which works only if such people exist in the data.

2. **The outcome's type picks the regression, and each gives a different measure of effect.** A continuous outcome gives linear regression and differences in means. A binary outcome (died or not) gives logistic regression and odds ratios, because odds can be modelled on a log scale without exceeding 1. A count gives Poisson regression and rate ratios. A time to event gives Cox regression and hazard ratios. Reading a paper begins with noticing which was used, because an odds ratio of 2 and a hazard ratio of 2 mean different things.

3. **Adjustment removes the part of an association explained by measured confounders, and only that part.** If treated patients are older and age predicts death, the crude comparison is unfair; including age in the model estimates the treatment effect at equal age. Adjustment cannot remove confounding by variables not measured, measured badly or not thought of (frailty, adherence, socioeconomic position), and residual confounding is the usual reason observational findings fail in trials. Hormone replacement therapy appeared to halve heart disease after adjustment in cohorts; a randomised trial (2002) found it did not.

4. **Adding predictors improves fit but can mislead: overfitting, collinearity and adjusting for the wrong thing.** A model with many predictors and few events describes the noise of its own sample and fails on the next; a rough rule is ten events per predictor. Two predictors that measure nearly the same thing (weight and body mass index) share their effect unstably. Adjusting for a variable that lies *between* exposure and outcome (a mediator) or is caused by both (a collider) removes real effect or creates spurious association. Which variables to include is a causal question, not a statistical one.

5. **Interaction means an effect differs by level of another variable, and it is not the same as confounding.** If aspirin's benefit is larger in men than women, sex modifies the effect; the correct report is two estimates, not one adjusted average. Interactions are tested with product terms, have low power, and are often claimed from subgroup analyses with no prior hypothesis. Confounding distorts an effect; interaction means there is more than one effect.

6. **Survival analysis handles censoring: people who have not yet had the event still carry information.** A patient alive at the end of a five-year study is censored; dropping them would bias survival downward, counting them as survivors forever would bias it upward. The Kaplan–Meier method estimates the survival curve by multiplying the probability of surviving each interval among those still at risk, using every patient up to their last observation. Median survival is read where the curve crosses 50%, and "five-year survival" is the curve's height at five years.

7. **The hazard is the instantaneous event rate among those still at risk, and the Cox model compares hazards.** A hazard ratio of 0.7 means that at any moment the treated group's death rate is 70% of the control group's. The Cox model assumes this ratio is constant over time (proportional hazards); when curves cross or separate late, as with surgery versus medical therapy or immunotherapy, a single hazard ratio misrepresents both arms. The hazard ratio is also not a ratio of survival times or of risks at a fixed time, and converting it to "lives 30% longer" is wrong.

8. **Regression yields prediction, which is a different goal from explanation.** A risk score (for cardiovascular events, for surgical mortality, for fracture) is a regression equation tuned to predict well, and its coefficients need not be causal: a variable can predict because it marks something else. Prediction models are judged by discrimination (how well they rank patients, the c-statistic) and calibration (whether predicted risks match observed ones) in *new* data; nearly all perform worse outside the population that built them, which is the problem of transportability.

## Key concepts

| Term | Meaning |
|---|---|
| Regression coefficient | Change in outcome per unit of a predictor, other predictors held fixed |
| Linear / logistic / Poisson / Cox regression | Models for continuous, binary, count and time-to-event outcomes |
| Odds ratio | Ratio of odds of outcome between groups; from logistic regression |
| Hazard ratio | Ratio of instantaneous event rates; from Cox regression |
| Adjustment | Estimating an effect at equal levels of measured confounders |
| Residual confounding | Confounding left by unmeasured or mismeasured variables |
| Overfitting | A model that fits its own sample's noise and predicts new data poorly |
| Interaction (effect modification) | An effect whose size depends on another variable |
| Censoring | An observation that ends before the event occurs |
| Kaplan–Meier curve | Non-parametric estimate of survival over time using censored data |
| Proportional hazards | The assumption that the hazard ratio is constant over time |
| Discrimination and calibration | Whether a model ranks patients correctly and whether its predicted risks are right |

## How it fits

- **Below:** coefficients are estimated by least squares or maximum likelihood on [distributions](../01-probability-and-measurement/distributions-and-descriptive-statistics.md) and reported with [confidence intervals](hypothesis-testing-and-confidence-intervals.md); the hazard is the rate constant of a [first-order process](../03-systems-and-models/compartment-models-and-exponential-processes.md), and constant hazard gives exponential survival.
- **Above:** [observational study designs](../../10-epidemiology-and-evidence/01-epidemiology/observational-study-designs.md) depend on adjustment; [risk prediction](../../10-epidemiology-and-evidence/03-screening-and-prevention/risk-prediction-and-stratification.md) and [prognosis](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/prognosis-and-shared-decision-making.md) are tenets 6–8; [allometry](../../00-physical-and-chemical-foundations/01-physics-of-the-body/scale-and-allometry.md) is a regression on log scales; [complex traits](../../04-genetics-evolution-and-development/01-inheritance/complex-traits-and-heritability.md) are partitioned by regression of phenotype on genotype.
- **Siblings:** [hypothesis testing](hypothesis-testing-and-confidence-intervals.md) supplies the uncertainty around each coefficient; [causal inference](causal-inference.md) decides which variables a model should adjust for and which it must not.

## Common misconceptions

- **"Adjusted means the confounding has been removed."** Only measured confounders, measured well, and only if the model's form is right; unmeasured confounding remains.
- **"A hazard ratio of 0.5 means patients live twice as long."** It means the event rate is halved at each moment; the effect on median survival depends on the shape of the curves.
- **"A risk score's variables are the causes of the disease."** Predictors can mark rather than cause; a score is judged by prediction in new data, not by biological meaning.

## Go deeper

- Frank E. Harrell Jr, *Regression Modeling Strategies* (2nd ed., 2015): the authoritative text on building and validating models without overfitting.
- David G. Kleinbaum and Mitchel Klein, *Survival Analysis: A Self-Learning Text* (3rd ed., 2012): Kaplan–Meier and Cox models explained step by step.
- Ewout W. Steyerberg, *Clinical Prediction Models* (2nd ed., 2019): discrimination, calibration and transportability for risk scores.
