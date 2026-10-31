# Mathematics and Society

> **Layer:** [15 Mathematics in Context](README.md)
> **Builds on:** [Hypothesis Tests and Confidence Intervals](../11-probability-and-statistics/04-statistical-inference/hypothesis-tests-and-confidence-intervals.md), [Cryptography](../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md), [Mathematical Biology and Epidemics](../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md), [Social Choice and Voting](../14-applied-and-computational-mathematics/05-games-decisions-and-finance/social-choice-and-voting.md), [Mathematical Finance](../14-applied-and-computational-mathematics/05-games-decisions-and-finance/mathematical-finance.md)
> **Enables:** [Ethics and Professional Responsibility (CS)](../../cs-first-principles/15-computing-in-context/ethics-and-professional-responsibility.md), [Law, Privacy and Policy (CS)](../../cs-first-principles/15-computing-in-context/law-privacy-and-policy.md), [Global Health and Pandemics (Medicine)](../../medicine-first-principles/15-medicine-in-society/03-populations-and-the-future/global-health-and-pandemics.md)

## Essence

Mathematics shapes society mostly invisibly: number theory secures online payments, linear algebra ranks web pages, relativity corrects satellite navigation, and integral transforms turn X-ray projections into medical images. It also enters public decisions directly, through statistics in courts, epidemic models in policy, risk models in finance and algorithms in hiring, policing and districting. There the mathematics is usually sound and the failures come from misapplying it: ignored assumptions, conditional statements read as unconditional, probabilities inverted. This leaf collects first-principles lessons from those encounters, and looks at the community that produces mathematics: who takes part, how results are shared, and what responsibilities follow.

## Core tenets

1. **Abstract mathematics becomes infrastructure, often unexpectedly.** G. H. Hardy wrote in *A Mathematician's Apology* (1940) that number theory had no warlike use; the Rivest–Shamir–Adleman (RSA) cryptosystem (1977) made the difficulty of factoring the basis of secure communication. Satellite positioning works only because clocks are corrected for special and general relativity, which together shift them by tens of microseconds per day. PageRank (1998) ranked web pages by the leading eigenvector of a stochastic matrix. Computed tomography inverts the Radon transform, studied by Johann Radon in 1917; Allan Cormack and Godfrey Hounsfield shared the 1979 Nobel prize in medicine for the scanner.

2. **Conditional probabilities are easily inverted, with grave consequences.** Sally Clark was convicted in England in 1999 of murdering her two infant sons. An expert told the court the chance of two cot deaths in such a family was about 1 in 73 million, obtained by squaring a single-death rate as if the deaths were independent, ignoring shared genetic and environmental factors. Worse, a small probability of the evidence under innocence was treated as a small probability of innocence: the prosecutor's fallacy. Double murder is also very rare, and the relevant comparison is between the two explanations. The Royal Statistical Society protested, and the conviction was overturned in 2003.

3. **Aggregated data can reverse a trend in every subgroup: Simpson's paradox.** In 1973 graduate admissions at the University of California, Berkeley appeared to favour men overall. Peter Bickel, Eugene Hammel and J. W. O'Connell (1975) showed that department by department there was no bias against women, who had applied more often to departments with low admission rates. Which comparison is right depends on a causal question that the numbers alone cannot answer.

4. **A model's projection is conditional, not a forecast.** Epidemic models in the style of the susceptible–infectious–recovered (SIR) equations compute what happens under stated assumptions about transmission and behaviour. In 2020, projections of COVID-19 deaths without intervention influenced lockdown decisions; when interventions changed behaviour, the unmitigated projection did not come true, which some read as model failure. Communicating "if this, then that", together with uncertainty, is part of the modeller's job.

5. **Models in finance fail when their assumptions are stressed.** The Gaussian copula, popularised for credit derivatives in 2000, priced pools of loans by assuming a simple form of correlation between defaults. It understated the chance that many borrowers default together, and its widespread use is often cited as one factor in the 2008 financial crisis. The mathematics was correct; its assumptions did not hold in a crisis.

6. **Some fairness criteria are mathematically incompatible.** When a risk score is used to make decisions about two groups with different base rates, it cannot in general be both calibrated (a given score means the same risk in each group) and have equal false positive and false negative rates in each, unless prediction is perfect. Jon Kleinberg, Sendhil Mullainathan and Manish Raghavan (2016) and Alexandra Chouldechova (2017) proved versions of this. Choosing among fairness criteria is therefore a value judgement that mathematics clarifies but cannot make. Goodhart's law adds that a measure turned into a target tends to stop measuring what it did.

7. **Mathematics informs democratic design.** Arrow's theorem shows every voting rule trades off desirable properties. To detect partisan gerrymandering, mathematicians generate large ensembles of random district maps by Markov chain Monte Carlo and show that a proposed plan is an extreme outlier; such evidence was presented in several United States cases, although in 2019 the Supreme Court held partisan gerrymandering claims outside the competence of federal courts.

8. **The community is widening, and its norms are changing.** Maryam Mirzakhani became the first woman awarded a Fields Medal (2014) and Maryna Viazovska the second (2022); Karen Uhlenbeck was the first woman to receive the Abel Prize (2019). The arXiv preprint server (1991) made results freely available on posting, and the 2012 Cost of Knowledge boycott of the publisher Elsevier pushed toward open access.

## Key concepts

| Term | Meaning |
|---|---|
| Prosecutor's fallacy | Confusing the probability of evidence given innocence with the probability of innocence given evidence |
| Simpson's paradox | A trend in every subgroup reversed in the aggregate |
| Conditional projection | What a model predicts under stated assumptions, not an unconditional forecast |
| Base rate | The frequency of an outcome in a population before other evidence |
| Calibration | A score means the same probability of the outcome in every group |
| Goodhart's law | A measure that becomes a target ceases to be a good measure |
| Ensemble analysis | Comparing a district map with many randomly generated alternatives |

## How it fits

- **Below:** hypothesis tests and conditional probability for evidence in court; cryptography for digital security; epidemic models, social choice and finance from layer 14 for policy.
- **Above:** nothing; this is the top layer.
- **Siblings:** [computers and proof](computers-and-proof.md) concerns trust in verified software and machine reasoning; [learning and teaching](learning-and-teaching-mathematics.md) concerns the public numeracy these cases need; [history](history-of-mathematics.md) shows earlier cases of pure mathematics becoming applied.

## Common misconceptions

- **"A mathematical model is objective, so its outputs are neutral."** Its assumptions and objectives encode choices, as the fairness impossibility results show.
- **"A model whose scenario did not happen was wrong."** Conditional projections are meant to change the behaviour they describe.
- **"Pure mathematics has no social consequences."** Number theory, linear algebra and integral geometry became cryptography, search engines and medical imaging.

## Go deeper

- G. H. Hardy, *A Mathematician's Apology* (1940): the classic defence of pure mathematics, now read partly for its mistaken predictions.
- C. O'Neil, *Weapons of Math Destruction* (2016): how opaque models in hiring, credit and policing can amplify harm.
- P. J. Davis and R. Hersh, *The Mathematical Experience* (1981): mathematics as a human activity and its place in culture.
