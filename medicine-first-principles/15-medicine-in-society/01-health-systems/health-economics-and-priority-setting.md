# Health Economics and Priority Setting

> **Layer:** [15 Medicine in Society](../README.md) › [Health systems](README.md)
> **Builds on:** [Organisation and financing of health systems](organisation-and-financing-of-health-systems.md), [Probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md), [Randomized controlled trials](../../10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md), [Grading evidence and guidelines](../../10-epidemiology-and-evidence/02-evidence-based-medicine/grading-evidence-and-guidelines.md), [Prognosis and shared decision-making](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/prognosis-and-shared-decision-making.md)
> **Enables:** [Medical ethics](../02-ethics-law-and-the-profession/medical-ethics.md), [From target to approval](../../09-pharmacology-and-therapeutics/05-drug-development-and-toxicology/from-target-to-approval.md), [Global health and pandemics](../03-populations-and-the-future/global-health-and-pandemics.md)

## Essence

A health budget is finite and the things it could buy are not, so funding one treatment is a decision not to fund another. Health economics is decision analysis with that constraint explicit: how much health does a spend buy, compared with what the same money would buy elsewhere? The working unit is a measure of health that can be compared across diseases, usually the Quality-Adjusted Life Year (QALY), and the working number is the incremental cost per QALY gained. The idea that makes the whole discipline work is **opportunity cost**: the true price of a treatment is not its invoice but the health forgone by the people who will not be treated because the money went here. Priority setting is acting on that arithmetic in public.

## Core tenets

1. **The relevant cost is what you give up.** If a health system's marginal spending buys one QALY for roughly £15,000 (an estimate for the English National Health Service by Claxton and colleagues, 2015), then funding a drug that costs £60,000 per QALY displaces about four QALYs elsewhere for every one it adds. Those displaced patients are real but invisible, which is why rationing by cost-effectiveness feels colder than rationing by waiting list even when it saves more lives.

2. **Comparing across diseases needs a common currency of health.** A QALY weights each life-year by a utility from 0 (dead) to 1 (full health), elicited from the public by methods such as the time trade-off; two years at utility 0.5 equal one QALY. The Disability-Adjusted Life Year (DALY), used in global burden-of-disease work, is the mirror image: years lost to death plus years lived with disability. Both are crude, both embed value judgements, and both beat deciding by anecdote.

3. **The incremental cost-effectiveness ratio is the decision quantity.** ICER = (cost of new − cost of old) / (QALYs of new − QALYs of old). A treatment is adopted if its ICER falls below a threshold representing the health the money would buy elsewhere. The National Institute for Health and Care Excellence (NICE) in England has used an explicit range of £20,000–30,000 per QALY since the early 2000s, with higher values for end-of-life and very rare diseases; the World Health Organization once suggested one to three times Gross Domestic Product (GDP) per capita, now widely considered too generous. These are worked examples, not constants; the right threshold matches the system's true marginal productivity.

4. **Effect sizes come from trials; costs and utilities are modelled over a lifetime.** A trial reports a risk reduction over a few years; a Markov model of health states extrapolates it over the patient's remaining life, with transition probabilities, costs and utilities per state. Future costs and benefits are discounted (commonly 3–3.5% a year), which makes prevention look worse than rescue and is an unavoidable value choice. Sensitivity analysis shows how much the answer depends on each uncertain input; sometimes the best decision is to buy more information first (value-of-information analysis).

5. **Prevention is not automatically cheaper.** It only saves money when the intervention is cheap, the condition is common and expensive, and the delay is short. Most prevention costs money and buys health, like treatment; the decision is still cost per QALY. Screening in particular can cost a lot per QALY because of the [biases and harms](../../10-epidemiology-and-evidence/03-screening-and-prevention/screening-principles-and-biases.md) that inflate its apparent benefit.

6. **Efficiency is not the only value; the public does not weigh QALYs equally.** People give extra weight to severity (the "rule of rescue" for an identifiable patient in peril), to the young and to those who have had less of life ("fair innings"). Daniels and Sabin's accountability for reasonableness (1997) argues that since no formula commands agreement, legitimacy must come from process: public reasons, transparency, appeal and enforcement. NICE's severity modifiers are that argument made institutional.

7. **Prices are negotiated, not discovered, and the threshold sets them.** A patented drug's production cost is far below its price; the manufacturer prices to the payer's willingness to pay, so where a threshold is public, companies price at it. Confidential discounts, managed-entry agreements and international reference pricing are the payer's counter-moves. [Approval](../../09-pharmacology-and-therapeutics/05-drug-development-and-toxicology/from-target-to-approval.md) asks "does it work and is it safe"; reimbursement asks "is it worth it at this price", now the harder gate.

8. **Guideline thresholds are cost-effectiveness decisions in disguise.** "Treat if ten-year risk exceeds some figure": lowering the figure treats more people with smaller absolute benefit each, raising the Number Needed to Treat (NNT) and the cost per QALY. This is how a population judgement in [guidelines](../../10-epidemiology-and-evidence/02-evidence-based-medicine/grading-evidence-and-guidelines.md) reaches the individual conversation in [shared decision-making](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/prognosis-and-shared-decision-making.md).

## Key concepts

| Term | Meaning |
|---|---|
| Opportunity cost | The best alternative use of a resource; the health forgone by spending here |
| QALY | A life-year weighted by a utility from 0 (dead) to 1 (full health) |
| DALY | Years of life lost plus years lived with disability, weighted; a burden measure |
| ICER | Incremental cost divided by incremental QALYs, new versus current care |
| Threshold | The ICER above which a treatment displaces more health than it adds |
| Discounting | Valuing future costs and benefits less than present ones |
| Markov model | A lifetime simulation of transitions between health states |
| Value of information | The expected gain from reducing uncertainty before deciding |

## How it fits

- **Below:** expected value under [probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md); effect sizes from [trials](../../10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md) and [meta-analyses](../../10-epidemiology-and-evidence/02-evidence-based-medicine/systematic-reviews-and-meta-analysis.md); the budget from [financing](organisation-and-financing-of-health-systems.md).
- **Above:** nothing; the output is a formulary, a guideline threshold and a price, which constrain every prescribing decision in layers 12 to 14.
- **Siblings:** [financing](organisation-and-financing-of-health-systems.md) sets the pool, this leaf spends it; [safety and quality](patient-safety-and-quality-improvement.md) asks whether the purchased care was delivered; [informatics](health-informatics-and-artificial-intelligence.md) supplies the real-world cost and outcome data models use.

## Common misconceptions

- **"Putting a price on a life is unethical."** Not pricing it does not avoid the choice; it hides it, and hidden rationing falls on those with the least voice.
- **"A cost-effective treatment is a cheap one."** A £100,000 drug that adds ten QALYs is cost-effective; a £5 drug that adds nothing is not. The ratio, not the price, decides.
- **"The threshold is a scientific constant."** It is an estimate of what the system's marginal spending achieves, differs between countries and is contested within them.

## Go deeper

- Michael F. Drummond and colleagues, *Methods for the Economic Evaluation of Health Care Programmes* (4th ed., 2015): the standard textbook.
- Norman Daniels and James Sabin, "Limits to Health Care: Fair Procedures, Democratic Deliberation, and the Legitimacy Problem for Insurers", *Philosophy and Public Affairs* (1997): why process matters when principles conflict.
- Karl Claxton and colleagues, "Methods for the estimation of the NICE cost effectiveness threshold", *Health Technology Assessment* (2015): the empirical approach to the threshold.
