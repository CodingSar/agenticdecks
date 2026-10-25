# Health Systems

> **Layer:** [15 Medicine in Society](../README.md) › Health systems
> **Children:** [Organisation and financing of health systems](organisation-and-financing-of-health-systems.md) · [Health economics and priority setting](health-economics-and-priority-setting.md) · [Patient safety and quality improvement](patient-safety-and-quality-improvement.md) · [Health informatics and artificial intelligence](health-informatics-and-artificial-intelligence.md)

## What this area is about

A clinician never treats a patient in a vacuum. Someone pays, someone decided the treatment was worth paying for, someone designed the ward and the drug chart so that the right dose reaches the right vein, and someone built the record that carried the test result. This area answers the question: **what is the machine around the consultation, and what does it do to the consultation?** The World Health Organization (WHO) defines a health system as all the organisations, people and actions whose primary intent is to promote, restore or maintain health; its goals are better health, fairness in financing and responsiveness to people.

The idea that unifies the four children is that **a health system is a control system under scarcity**. It has inputs (money, staff, information), a transfer function (how care is organised), outputs (health, harm, cost) and feedback (measurement, payment, regulation). Everything in the lower layers tells you what *can* be done for a patient; this area tells you what *will* be done, for whom, how reliably, and at what price to everyone else.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Organisation and financing](organisation-and-financing-of-health-systems.md) | Where the money comes from, how it is pooled, how providers are paid, and why those choices shape behaviour | [Supply and demand](../../CROSS-CUTTING.md#supply-and-demand); epidemiology for need |
| [Health economics and priority setting](health-economics-and-priority-setting.md) | How to choose between treatments when the budget cannot fund them all: cost per unit of health, thresholds, opportunity cost | Decision analysis (01), effect sizes from trials (10), financing (the budget) |
| [Patient safety and quality improvement](patient-safety-and-quality-improvement.md) | Why care harms people, why the cause is usually the system not the individual, and how to measure and change a system | Feedback and control (01), measurement error (01), clinical reasoning (11) |
| [Health informatics and artificial intelligence](health-informatics-and-artificial-intelligence.md) | How clinical information is represented, moved and increasingly interpreted by machines, and what goes wrong | Signal and noise, Bayes (01), diagnostic accuracy (10), using tests (11) |

Read them in that order. Financing sets the budget; economics decides how to spend it; safety and quality ask whether what was bought was delivered without harm; informatics is the nervous system that carries the information every other child depends on, and increasingly the place where decisions are made. Economics and safety share one logic: both are about getting the most health from a fixed input, one by choosing what to do, the other by doing it reliably. Informatics is the enabler and the new hazard for both.

```
   money in  -->  pooling & purchasing  -->  providers  -->  care  -->  health, harm, cost
                      ^                          ^                          |
                      |  priority setting        |  safety & quality         |
                      +------- measurement, records, informatics  <---------+
```

## Connections to sibling areas

- **[Ethics, law and the profession](../02-ethics-law-and-the-profession/README.md):** priority setting is applied distributive justice; a safety culture depends on candour, which law can protect or punish; informatics makes [confidentiality](../02-ethics-law-and-the-profession/consent-capacity-and-confidentiality.md) a technical problem; [regulation](../02-ethics-law-and-the-profession/professionalism-regulation-and-medical-education.md) of doctors is one of the system's feedback loops.
- **[Populations and the future](../03-populations-and-the-future/README.md):** financing arrangements decide whether the poor reach care ([social determinants](../03-populations-and-the-future/social-determinants-and-health-inequity.md)); surge capacity and surveillance decide how a system meets a [pandemic](../03-populations-and-the-future/global-health-and-pandemics.md); the health sector's own carbon footprint is a [planetary health](../03-populations-and-the-future/environmental-and-planetary-health.md) problem; [history](../03-populations-and-the-future/history-of-medicine.md) explains why systems look the way they do.

## Connections across layers

From below, this area takes decision theory, feedback and signal-to-noise from [01](../../01-quantitative-and-scientific-foundations/README.md); the measures of effect, cost and harm from [10](../../10-epidemiology-and-evidence/README.md), especially [randomised trials](../../10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md) and [guidelines](../../10-epidemiology-and-evidence/02-evidence-based-medicine/grading-evidence-and-guidelines.md); the test characteristics and thresholds of [11](../../11-clinical-method-and-diagnostics/README.md); and from [09](../../09-pharmacology-and-therapeutics/README.md) the [approval pathway](../../09-pharmacology-and-therapeutics/05-drug-development-and-toxicology/from-target-to-approval.md) that a price negotiation follows. It gives back requirements that reach every clinical layer: formularies, safety checklists, structured records, alert thresholds and reimbursement rules that shape what [primary care](../../14-life-course-mind-and-integrative-care/05-primary-care-and-integration/family-medicine-and-the-generalist.md), [surgery](../../13-acute-perioperative-and-procedural-care/01-surgery/the-surgical-decision.md) and the [specialties](../../12-organ-system-specialties/README.md) actually do.

## Cross-cutting threads

- [Supply and demand](../../CROSS-CUTTING.md#supply-and-demand): beds, staff and money against need; waiting lists are the queue that forms when they mismatch.
- [Feedback and homeostasis](../../CROSS-CUTTING.md#feedback-and-homeostasis): payment, audit and regulation as feedback loops, with the gains and delays that make them stabilise or oscillate.
- [Harm and benefit](../../CROSS-CUTTING.md#harm-and-benefit): cost per QALY is harm and benefit priced; patient safety is harm counted.
- [Probability and uncertainty](../../CROSS-CUTTING.md#probability-and-uncertainty): decision analysis under uncertain effect sizes; AI prediction as Bayes at scale.
- [Signalling and information](../../CROSS-CUTTING.md#signalling-and-information): the record, the alert and the code set as the system's signalling layer, with noise, loss and misreading.
- [Compensation and decompensation](../../CROSS-CUTTING.md#compensation-and-decompensation): a system with reserve absorbs a bad winter; one without it fails suddenly.
