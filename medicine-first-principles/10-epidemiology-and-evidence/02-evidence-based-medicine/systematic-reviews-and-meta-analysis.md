# Systematic reviews and meta-analysis

> **Layer:** [10 Epidemiology and Evidence](../README.md) › [Evidence-based medicine](README.md)
> **Builds on:** [Randomized controlled trials](randomized-controlled-trials.md), [Hypothesis testing and confidence intervals](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md), [Bias, confounding and chance](../01-epidemiology/bias-confounding-and-chance.md)
> **Enables:** [Grading evidence and guidelines](grading-evidence-and-guidelines.md), [Research integrity and publication bias](research-integrity-and-publication-bias.md), [Health economics and priority setting](../../15-medicine-in-society/01-health-systems/health-economics-and-priority-setting.md)

## Essence

No single trial settles a question. Trials are small, their populations differ, and chance scatters their results around the truth. A systematic review is a study of studies: a pre-specified, reproducible search for every piece of evidence on a question, an appraisal of each study's risk of bias, and a synthesis. When the studies are similar enough, meta-analysis combines their estimates into one, weighting each by its precision, and so gains the power that none had alone. The idea that makes it work is that the review is itself a piece of research with a protocol, and the idea that makes it dangerous is that combining biased studies with great precision yields a precisely biased answer.

## Core tenets

1. **A narrative review is an opinion with references; a systematic review is a method.** The difference lies in the protocol: a stated question (population, intervention, comparator, outcome), a search strategy covering several databases and registries, explicit inclusion criteria applied by two reviewers, and a pre-planned analysis. The reader can check every step. Without this, a review reports the studies its author knew or liked, and a selective reading of the literature can support almost any conclusion.

2. **Meta-analysis is a weighted average, with weight proportional to precision.** Each study contributes its effect estimate (a relative risk, a mean difference) weighted by the inverse of its variance, so large, precise studies dominate. The pooled estimate has a narrower confidence interval than any contributor. The 1980s meta-analyses of streptokinase after myocardial infarction showed a mortality benefit from trials that were individually inconclusive, years before the large trials that confirmed it.

3. **Heterogeneity is information, not a nuisance.** Studies differ in populations, doses, follow-up and outcome definitions, so their true effects may differ. The I² statistic estimates the share of variation beyond chance. A fixed-effect model assumes one true effect; a random-effects model assumes a distribution of true effects and widens the interval accordingly. When heterogeneity is large, the question is *why* (subgroup analysis, meta-regression), and a single pooled number may mislead more than it informs.

4. **The forest plot is the review's evidence laid bare.** Each study is a line: a square at its estimate, sized by its weight, with its confidence interval; the diamond at the bottom is the pooled result. One glance shows whether studies agree, whether one large trial drives the conclusion, and whether a precise pooled estimate is being extracted from a cloud of imprecise and conflicting ones.

   ```
   Trial A   ---[==]---          RR 0.7 (0.4-1.2)
   Trial B      -[====]-         RR 0.9 (0.7-1.1)
   Trial C  ------[=]------      RR 0.6 (0.3-1.3)
   Pooled         <>             RR 0.85 (0.72-0.99)
                  |
                 1.0 (no effect)
   ```

5. **Risk of bias within studies must be assessed before results are pooled.** Trials with inadequate concealment or blinding overestimate effects, so a review that averages them inherits the bias with added confidence. Structured tools (the Cochrane risk-of-bias tool, with domains for randomisation, deviations from intended interventions, missing data, outcome measurement and selective reporting) make the judgement explicit. Sensitivity analyses that drop high-risk studies show whether the conclusion survives.

6. **Bias between studies, in which studies exist and are found, can be larger than any within them.** Positive trials are published more often, faster and in more visible journals than negative ones ([publication bias](research-integrity-and-publication-bias.md)). A funnel plot (effect against precision) that is asymmetric, with small positive studies and no small negative ones, suggests it. Searching trial registries, regulatory submissions and unpublished data is the only remedy; the antidepressant literature, where unpublished trials reversed the apparent effect size, is the standard warning.

7. **Individual participant data and network meta-analysis extend the method.** Pooling raw patient data rather than summary results allows consistent definitions and genuine subgroup analysis. Network meta-analysis compares treatments that were never trialled head to head by using the chain of comparisons through common comparators, at the price of assuming the trials are similar enough that indirect comparison is fair. Both multiply the ways the assumptions can fail.

## Key concepts

| Term | Meaning |
|---|---|
| Systematic review | A review with a protocol: explicit question, search, selection, appraisal and synthesis |
| Meta-analysis | Statistical combination of results from several studies into one estimate |
| Inverse-variance weighting | Weighting each study by the reciprocal of the variance of its estimate |
| Fixed-effect and random-effects models | Assume one true effect versus a distribution of true effects across studies |
| Heterogeneity (I²) | Share of variation between study results not explained by chance |
| Forest plot | Graphical display of each study's estimate and interval with the pooled result |
| Funnel plot | Effect size against precision; asymmetry suggests publication or small-study bias |
| Risk of bias assessment | Structured judgement of each study's susceptibility to systematic error |
| Network meta-analysis | Comparison of several treatments using direct and indirect evidence |

## How it fits

- **Below:** pooling is weighted estimation with [confidence intervals](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md); the units are [trials](randomized-controlled-trials.md) and observational studies; the appraisal applies the catalogue of [bias](../01-epidemiology/bias-confounding-and-chance.md).
- **Above:** [guidelines](grading-evidence-and-guidelines.md) start from systematic reviews rather than single studies; [health economic](../../15-medicine-in-society/01-health-systems/health-economics-and-priority-setting.md) models take pooled effect sizes as inputs; regulators and [drug development](../../09-pharmacology-and-therapeutics/05-drug-development-and-toxicology/from-target-to-approval.md) rely on pooled safety data.
- **Siblings:** [research integrity and publication bias](research-integrity-and-publication-bias.md) explains why the evidence the search finds is a biased sample of the evidence that exists; [diagnostic accuracy studies](diagnostic-accuracy-studies.md) need their own meta-analytic methods because sensitivity and specificity trade along a threshold.

## Common misconceptions

- **"A meta-analysis is the highest form of evidence."**: it is only as good as the studies it pools and the search that found them; a meta-analysis of biased trials is biased, with a narrower confidence interval.
- **"Pooling studies that disagree gives the right average."**: if the studies estimate different things, the average estimates nothing; heterogeneity must be explained before it is averaged.
- **"A systematic review has settled the question for good."**: reviews go out of date as trials accumulate, and the conclusion can reverse when a large trial reports.

## Go deeper

- Julian P. T. Higgins and colleagues (eds.), *Cochrane Handbook for Systematic Reviews of Interventions* (2nd ed., 2019): the operational standard.
- Michael Borenstein, Larry V. Hedges, Julian P. T. Higgins and Hannah R. Rothstein, *Introduction to Meta-Analysis* (2009): the statistics, clearly explained.
- Matthias Egger, George Davey Smith and Douglas G. Altman (eds.), *Systematic Reviews in Health Care: Meta-Analysis in Context* (2nd ed., 2001): the method and its pitfalls, including funnel plots.
