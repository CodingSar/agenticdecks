# Probability

> **Layer:** [01 Quantitative and Scientific Foundations](../README.md) › [Probability and Measurement](README.md)
> **Builds on:** [The scientific method and models](../03-systems-and-models/the-scientific-method-and-models.md)
> **Enables:** [Bayesian reasoning](bayesian-reasoning.md), [Mendelian inheritance and pedigrees](../../04-genetics-evolution-and-development/01-inheritance/mendelian-inheritance-and-pedigrees.md), [Measures of frequency and association](../../10-epidemiology-and-evidence/01-epidemiology/measures-of-frequency-and-association.md), [Using tests, pre-test probability and thresholds](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md)

## Essence

Medicine never knows; it estimates. Whether a chest pain is a heart attack, whether a child will inherit a disease, whether a drug will help this patient and whether an outbreak will grow are all questions with uncertain answers, and probability is the only consistent language for them. A probability is a number between 0 and 1 that obeys three rules, and from those rules follow the tools medicine uses daily: the conversion between probability and odds, the multiplication of independent risks, the arithmetic of combining a test result with what was known before, and the idea that a rare event becomes common when enough people are exposed to it. The clinician's intuitions about chance are systematically wrong in known ways, which is why the rules must be learned rather than felt.

## Core tenets

1. **Probability has two readings, and medicine uses both.** The *frequency* reading: the proportion of times an event occurs in many repetitions, as in "5% of people with this test result have the disease". The *degree of belief* reading: how confident one is about a single case, as in "this patient has a 5% chance of the disease". The rules are the same under both, and the Bayesian clinician moves between them: population frequencies supply the starting belief about one patient.

2. **Three rules generate everything.** Probabilities lie between 0 and 1; the probabilities of all possible outcomes sum to 1; and the probability of either of two mutually exclusive events is the sum of their probabilities. From these follow the complement rule, `P(not A) = 1 − P(A)`, which is why "the chance of at least one event" is easiest found as one minus the chance of none, and the general addition rule, `P(A or B) = P(A) + P(B) − P(A and B)`, which stops one double-counting patients who have both conditions.

3. **Independence multiplies; dependence must be stated.** If A and B are independent, `P(A and B) = P(A) × P(B)`: two parents each carrying a recessive allele give each child a ¼ chance of being affected, and each child's chance is unaffected by siblings' outcomes. If they are not independent, `P(A and B) = P(A) × P(B | A)`, where `P(B | A)` is the conditional probability of B given A. Most medical events are dependent: the chance of a second fracture is higher given a first, and treating risk factors as independent when they cluster (smoking, hypertension, diabetes) misstates total risk.

4. **Conditional probability is directional, and reversing it is the commonest error.** `P(positive test | disease)` (sensitivity) is not `P(disease | positive test)` (what the clinician wants). A sign present in 90% of patients with a disease may be present in 1% of the healthy, and if the disease is rare, most people showing the sign are healthy. Confusing the two directions is the prosecutor's fallacy in court and the base-rate error at the bedside; Bayes' theorem is the correction.

5. **Odds are an alternative scale that makes updating multiplicative.** Odds = `P / (1 − P)`; a probability of 0.2 is odds of 1:4 or 0.25. Odds have no upper bound, and multiplying them by a likelihood ratio is how a test result updates belief, so clinicians who estimate pre-test probability convert to odds, multiply, and convert back. Odds and probability nearly coincide below ~0.1, which is why odds ratios from case–control studies approximate relative risks for rare diseases and exaggerate them for common ones.

6. **Rare events are common across many trials.** A complication with probability 1 in 1,000 per operation will occur in roughly 63% of surgeons performing 1,000 operations (1 − 0.999¹⁰⁰⁰) and about 100 times a year in a country performing 100,000. The law of large numbers says the observed proportion converges to the true probability as numbers grow, so a hospital's complication rate over 50 cases is noise and over 5,000 is signal. Clusters of rare events also occur by chance.

7. **Human intuition misjudges probability in predictable ways.** People overweight vivid or recent events (availability), anchor on the first number given, ignore base rates, see patterns in randomness and judge a conjunction more likely than one of its parts. Tversky and Kahneman documented these in the 1970s and clinicians show them as reliably as anyone, which is why structured tools (pre-test probability estimates, decision rules, checklists) outperform unaided judgement for calibrated probability.

## Key concepts

| Term | Meaning |
|---|---|
| Probability | A number in [0, 1] obeying the three axioms; frequency or degree of belief |
| Complement rule | `P(not A) = 1 − P(A)` |
| Mutually exclusive | Events that cannot both occur; their probabilities add |
| Independent | Events where one's occurrence does not change the other's probability; their probabilities multiply |
| Conditional probability | `P(B | A)`, the probability of B given that A has occurred |
| Joint probability | `P(A and B) = P(A) × P(B | A)` |
| Odds | `P / (1 − P)`; the scale on which likelihood ratios multiply |
| Law of large numbers | Observed frequency converges to probability as trials increase |
| Base rate | The prior frequency of a condition before any test result |

## How it fits

- **Below:** nothing; this is a root leaf. It presupposes only the idea, from [the scientific method and models](../03-systems-and-models/the-scientific-method-and-models.md), that a model can be a quantitative statement about an uncertain world.
- **Above:** [Bayesian reasoning](bayesian-reasoning.md) is tenets 4 and 5 made into a method; [Mendelian inheritance](../../04-genetics-evolution-and-development/01-inheritance/mendelian-inheritance-and-pedigrees.md) is tenet 3 with alleles; [measures of frequency and association](../../10-epidemiology-and-evidence/01-epidemiology/measures-of-frequency-and-association.md) are probabilities and their ratios in populations; [using tests at the bedside](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md) applies tenets 4–7 to one patient; entropy in [thermodynamics](../../00-physical-and-chemical-foundations/01-physics-of-the-body/energy-and-thermodynamics.md) is probability over molecular states.
- **Siblings:** [distributions](distributions-and-descriptive-statistics.md) describe how probability is spread over values; [measurement error](measurement-error-and-biological-variation.md) is probability applied to the instrument; [Bayesian reasoning](bayesian-reasoning.md) is probability applied to belief.

## Common misconceptions

- **"A test that is 95% accurate means a positive result is 95% likely to be right."** That depends on how common the disease is; for a rare disease most positives are false even with a good test.
- **"After several healthy children, the next is more likely to be affected."** Independent events have no memory; the ¼ risk is the same for every pregnancy.

## Go deeper

- Gerd Gigerenzer, *Reckoning with Risk* (2002): how to state and compute medical probabilities so that doctors and patients get them right.
- Daniel Kahneman, *Thinking, Fast and Slow* (2011): the heuristics and biases that distort probability judgement.
- Dennis V. Lindley, *Understanding Uncertainty* (revised ed., 2014): probability as the logic of belief, by one of its clearest expositors.
