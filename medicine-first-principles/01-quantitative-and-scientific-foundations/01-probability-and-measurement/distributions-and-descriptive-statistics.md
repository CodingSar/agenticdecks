# Distributions and Descriptive Statistics

> **Layer:** [01 Quantitative and Scientific Foundations](../README.md) › [Probability and Measurement](README.md)
> **Builds on:** [Probability](probability.md)
> **Enables:** [Measurement error and biological variation](measurement-error-and-biological-variation.md), [Hypothesis testing and confidence intervals](../02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md), [Complex traits and heritability](../../04-genetics-evolution-and-development/01-inheritance/complex-traits-and-heritability.md), [Scale and allometry](../../00-physical-and-chemical-foundations/01-physics-of-the-body/scale-and-allometry.md)

## Essence

A distribution is the shape that probability takes over the possible values of a quantity: how heights, blood pressures, survival times or counts of infections are spread across a population. Describing that shape with a few numbers (a centre, a spread, a skew) is the first act of every medical study and the basis of every reference range, growth chart and risk score. Three shapes do most of the work: the normal (bell) curve for quantities that are sums of many small influences, the log-normal for quantities that are products, and the binomial and Poisson for counts. The central limit theorem explains why the normal curve appears so often and why averages of noisy measurements are more trustworthy than single values, and it is the quiet foundation of the confidence interval.

## Core tenets

1. **A distribution assigns probability to values; summarising it means choosing a centre and a spread.** The mean is the arithmetic average and the centre of mass; the median is the middle value and is unmoved by extremes; the mode is the commonest value. The standard deviation measures spread around the mean; the interquartile range measures the span of the middle half. For a symmetrical distribution they agree; for a skewed one (hospital length of stay, income, viral load) the mean is dragged toward the tail and the median is the honest centre.

2. **The normal distribution arises when many small independent effects add.** Height, blood pressure, haemoglobin and measurement error are each the sum of many genes, exposures and chance events, and the central limit theorem says such sums tend toward a bell curve whatever the shape of the parts. In a normal distribution ~68% of values lie within one standard deviation of the mean, ~95% within two and ~99.7% within three, which is where the "mean ± 2 SD" reference range and the 95% convention come from.

3. **Multiplicative processes give log-normal distributions, and a log transform makes them normal.** When effects multiply rather than add (drug concentrations after several first-order steps, hormone levels, antibody titres, bacterial counts), the distribution is skewed right with a long tail, and its logarithm is normal. Such quantities are summarised by the geometric mean and compared on a log scale; a two-standard-deviation reference range on a raw scale would have a nonsensical negative lower limit.

4. **Counts follow the binomial and Poisson distributions.** The number of successes in n independent trials with probability p is binomial, with mean `np` and standard deviation `√(np(1−p))`: 20 patients at 30% response rate give 6 ± 2 responders, so a trial of 20 cannot distinguish 30% from 20%. When events are rare and the opportunities many (deaths per year in a ward, infections per 1,000 catheter-days, mutations per genome), the Poisson approximation applies, with variance equal to the mean, so a rate observed as 4 events could easily be a true rate of 2 or 7. Small counts carry large uncertainty.

5. **The standard error is the standard deviation of a sample statistic, and it shrinks with `√n`.** If individual values have standard deviation σ, the mean of n of them has standard deviation `σ/√n`, the standard error of the mean. Quadrupling the sample halves it. This is the bridge from description to inference: the spread of individuals (SD) describes the population; the spread of the estimate (SE) describes how well a study has pinned down its mean.

6. **Percentiles describe position and are the language of growth and development.** A child on the 10th centile for weight is heavier than 10% of children of the same age and sex; crossing centiles over time matters more than any single position. Centile charts are empirical distributions by age, and the z-score (how many standard deviations from the mean) is the same idea standardised, used for bone density, body mass index in children and fetal growth.

7. **Correlation measures linear association between two distributions and nothing else.** The correlation coefficient r runs from −1 to 1 and its square is the fraction of variance in one variable explained linearly by the other. An r of 0.3 (common in biology) explains 9% of variance. It says nothing about cause or agreement, and is zero for a U-shaped relation such as mortality against body mass index.

## Key concepts

| Term | Meaning |
|---|---|
| Mean, median, mode | Arithmetic average; middle value; commonest value |
| Standard deviation (SD) | Root-mean-square spread of individuals around the mean |
| Interquartile range | Span from the 25th to the 75th percentile |
| Normal distribution | Symmetric bell curve from additive effects; 95% within ±2 SD |
| Central limit theorem | Sums and means of many independent variables tend toward normality |
| Log-normal distribution | Right-skewed; its logarithm is normal; from multiplicative effects |
| Binomial distribution | Number of successes in n trials of probability p |
| Poisson distribution | Counts of rare events in a fixed interval; variance equals mean |
| Standard error (SE) | SD of a sample statistic; for a mean, `σ/√n` |
| Percentile and z-score | Position in a distribution; distance from the mean in SDs |
| Correlation coefficient (r) | Strength of linear association, −1 to 1 |

## How it fits

- **Below:** a distribution is a [probability](probability.md) spread over values; this is a root leaf.
- **Above:** [measurement error](measurement-error-and-biological-variation.md) uses the normal curve to define reference ranges; [hypothesis tests and confidence intervals](../02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md) rest on the standard error; [complex traits](../../04-genetics-evolution-and-development/01-inheritance/complex-traits-and-heritability.md) are the normal distribution produced by many genes; [allometry](../../00-physical-and-chemical-foundations/01-physics-of-the-body/scale-and-allometry.md) is a power law fitted on log scales.
- **Siblings:** [probability](probability.md) gives the rules; [measurement error](measurement-error-and-biological-variation.md) applies the spread to one patient's repeated values; [Bayesian reasoning](bayesian-reasoning.md) treats a distribution as a state of belief to be updated.

## Common misconceptions

- **"Most biological variables are normally distributed."** Many are log-normal or skewed; assuming normality for length of stay, cost or hormone levels gives absurd ranges and wrong tests.
- **"Standard deviation and standard error are interchangeable."** SD describes individuals; SE describes the precision of an estimate and shrinks with sample size. Error bars showing SE make variable data look tight.

## Go deeper

- Douglas G. Altman, *Practical Statistics for Medical Research* (1991): distributions and summaries for clinical data, with the pitfalls.
- David Spiegelhalter, *The Art of Statistics* (2019): how to look at data before testing it, with medical examples.
- Michael J. Campbell, David Machin and Stephen J. Walters, *Medical Statistics: A Textbook for the Health Sciences* (4th ed., 2007): a compact standard text.
