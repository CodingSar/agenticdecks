# Surveillance and outbreak investigation

> **Layer:** [10 Epidemiology and Evidence](../README.md) › [Epidemiology](README.md)
> **Builds on:** [Infectious disease dynamics](infectious-disease-dynamics.md), [Measures of frequency and association](measures-of-frequency-and-association.md), [Observational study designs](observational-study-designs.md), [Information, signals and noise](../../01-quantitative-and-scientific-foundations/03-systems-and-models/information-signals-and-noise.md)
> **Enables:** [Infection control and healthcare-associated infection](../../12-organ-system-specialties/08-infectious-diseases/infection-control-and-healthcare-associated-infection.md), [Global health and pandemics](../../15-medicine-in-society/03-populations-and-the-future/global-health-and-pandemics.md), [Health informatics and artificial intelligence](../../15-medicine-in-society/01-health-systems/health-informatics-and-artificial-intelligence.md)

## Essence

Surveillance is epidemiology run continuously: the systematic collection, analysis and interpretation of health data, linked to the people who can act on them. Its purpose is to detect a change against a background (a rise in cases, a new pathogen, a cluster of birth defects) early enough for action to matter, and to measure whether the action worked. Outbreak investigation is what happens when surveillance fires: a compressed field version of the whole epidemiological method, in which a case definition, a line list, a descriptive picture and an analytical study are produced in days instead of years. The organising idea is signal detection: an outbreak is an excess over the expected, so you must know the expected, and every design choice trades sensitivity for false alarms.

## Core tenets

1. **Surveillance is defined by the link to action, not by the data.** William Farr's registration of deaths in England (from 1839) became surveillance when the weekly returns went to people who could close a pump or a cesspool. A dataset nobody watches is a registry; a dataset with a threshold, a reader and a response is surveillance. Timeliness, sensitivity, specificity, representativeness and simplicity are the attributes a system is judged by, and they conflict: a system that captures every case is slow and expensive; a fast one misses cases.

2. **Passive, active, sentinel and syndromic systems trade completeness for speed and cost.** *Passive* surveillance waits for clinicians and laboratories to notify statutory diseases: cheap, broad, and under-reporting by a large and variable fraction. *Active* surveillance seeks cases out and is used when completeness matters, as in polio eradication. *Sentinel* systems watch a sample of sites intensively to track trends (influenza-like illness in a network of practices). *Syndromic* surveillance counts symptoms, prescriptions or search queries before diagnoses exist, buying days of warning at the cost of specificity.

3. **An outbreak is an excess of observed over expected, and the expected must be modelled.** Seasonal diseases have seasonal baselines; reporting has weekday patterns and holiday gaps; a change in testing changes the count without changing the disease. Aberration-detection algorithms compare the current week with a historical expectation and its variance, and the alert threshold is a [signal-to-noise](../../01-quantitative-and-scientific-foundations/03-systems-and-models/information-signals-and-noise.md) choice: lower it and you chase false alarms; raise it and you detect late. A rise in diagnoses after a new test is introduced is the commonest pseudo-outbreak.

4. **The case definition is the first and most consequential decision of an investigation.** It states who counts: clinical criteria, laboratory confirmation, place and time. A broad definition is sensitive and finds cases early; a narrow one is specific and needed for the analytical study, where misclassified cases dilute the association. Investigators run tiers (confirmed, probable, possible) and tighten as the agent is identified. Changing the definition mid-investigation breaks comparability.

5. **Time, place and person usually reveal the source before any statistics.** The *epidemic curve* (cases by onset date) distinguishes a point source (one sharp peak within an incubation period), a continuing common source (a plateau) and person-to-person spread (successive waves one serial interval apart), and its width hints at the agent. A *spot map* shows clustering (Snow's cholera deaths around the Broad Street pump, 1854). Attack rates by age, occupation and exposure say who was exposed. Hypotheses come from this picture; the analytical study tests them.

6. **The analytical step is a case-control or cohort study done fast.** When the exposed population is enumerable (a wedding, a ward) a retrospective cohort compares attack rates in those who did and did not eat or do each thing. When it is not, a case-control study compares exposures of cases and controls. The suspect is the item with the largest difference in attack rate between the exposed and unexposed; a food every guest ate cannot be implicated by comparison. Whole-genome sequencing of isolates now confirms that cases share a strain and links them to the source.

7. **Control starts before the investigation finishes, and acts on whatever link in the chain is reachable.** Remove the source (recall the food), interrupt transmission (isolation, hand hygiene, vector control), protect susceptibles (vaccination, prophylaxis). Which measure fits depends on the reproduction number and the timing of infectiousness in [infectious disease dynamics](infectious-disease-dynamics.md). The final product is a report naming what failed and what should change, because the same lapse recurs.


## Key concepts

| Term | Meaning |
|---|---|
| Surveillance | Ongoing systematic collection, analysis and dissemination of health data for action |
| Notifiable disease | A condition that clinicians and laboratories are legally required to report |
| Sentinel surveillance | Intensive monitoring at a sample of sites to track trends |
| Syndromic surveillance | Counting symptoms or proxies before diagnosis to gain time |
| Case definition | The criteria (clinical, laboratory, time, place) deciding who counts as a case |
| Line list | The table of cases with onset, exposures and outcome from which everything is computed |
| Epidemic curve | Histogram of cases by onset date; its shape indicates the mode of spread |
| Attack rate | Cases divided by people exposed over the outbreak period |
| Pseudo-outbreak | An apparent excess caused by changed testing, reporting or definitions |

## How it fits

- **Below:** detecting an excess against a noisy baseline is the problem of [signals and noise](../../01-quantitative-and-scientific-foundations/03-systems-and-models/information-signals-and-noise.md); the analytical step reuses [observational designs](observational-study-designs.md); the epidemic curve is explained by [infectious disease dynamics](infectious-disease-dynamics.md).
- **Above:** hospital [infection control](../../12-organ-system-specialties/08-infectious-diseases/infection-control-and-healthcare-associated-infection.md) is surveillance plus investigation inside one building; national and global systems feed [pandemic preparedness](../../15-medicine-in-society/03-populations-and-the-future/global-health-and-pandemics.md); electronic records make surveillance a problem of [health informatics](../../15-medicine-in-society/01-health-systems/health-informatics-and-artificial-intelligence.md).
- **Siblings:** [bias, confounding and chance](bias-confounding-and-chance.md) applies in compressed form: reporting artefacts are information bias, and a cluster that attracts attention may be chance.

## Common misconceptions

- **"More cases reported means more disease."**: a new test, a media story or a changed definition raises counts without changing incidence.
- **"The food most cases ate is the source."**: if nearly everyone ate it, cases and non-cases ate it equally; the source shows the greatest *difference* in attack rate.
- **"Investigation must finish before control begins."**: measures aimed at the probable source are taken as soon as a hypothesis is credible, because a wrong recall usually costs less than continued exposure.

## Go deeper

- Michael B. Gregg (ed.), *Field Epidemiology* (3rd ed., 2008): the practical manual of outbreak investigation.
- John Snow, *On the Mode of Communication of Cholera* (2nd ed., 1855): the founding case study of spot maps and a natural experiment.
- Stephen B. Thacker and Ruth L. Berkelman, "Public health surveillance in the United States", *Epidemiologic Reviews* (1988): what surveillance is and how to evaluate it.
