# Patient Safety and Quality Improvement

> **Layer:** [15 Medicine in Society](../README.md) › [Health systems](README.md)
> **Builds on:** [Feedback and control](../../01-quantitative-and-scientific-foundations/03-systems-and-models/feedback-and-control.md), [Measurement error and biological variation](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/measurement-error-and-biological-variation.md), [Clinical reasoning and cognitive bias](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/clinical-reasoning-and-cognitive-bias.md), [Adverse drug reactions and pharmacovigilance](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/adverse-drug-reactions-and-pharmacovigilance.md), [Infection control and healthcare-associated infection](../../12-organ-system-specialties/08-infectious-diseases/infection-control-and-healthcare-associated-infection.md)
> **Enables:** [Health informatics and artificial intelligence](health-informatics-and-artificial-intelligence.md), [Professionalism, regulation and medical education](../02-ethics-law-and-the-profession/professionalism-regulation-and-medical-education.md), [Perioperative risk and complications](../../13-acute-perioperative-and-procedural-care/02-anaesthesia-and-perioperative-medicine/perioperative-risk-and-complications.md)

## Essence

Healthcare injures a sizeable minority of the people it treats, mostly not through bad doctors but through ordinary people working in systems that make error easy and recovery hard. The Harvard Medical Practice Study (Brennan and colleagues, 1991) found an adverse event in 3.7% of hospital admissions; the Institute of Medicine's *To Err Is Human* (1999) extrapolated 44,000–98,000 deaths a year in United States hospitals; the World Health Organization (WHO) now estimates that about one in ten patients is harmed in hospital care and roughly half of that harm is preventable. Patient safety is the science of why; quality improvement is the engineering of changing a process and measuring whether the change was an improvement. The idea under both: **outcomes are properties of systems, so fix the system, not the person**.

## Core tenets

1. **Error is a consequence, not a cause.** James Reason's distinction (1990) between *active failures* (the slip or mistake at the sharp end: the wrong vial picked, the decimal point missed) and *latent conditions* (look-alike packaging, a 14-hour shift, an interface that hides the allergy) explains why punishing the last person to touch the patient changes nothing. The latent conditions remain and the next person meets them. The "Swiss cheese" model: harm reaches the patient only when holes in several defensive layers line up, so safety is the number and independence of the layers.

2. **Most harm comes from a few recurring mechanisms.** Medication error (wrong drug, dose, route or patient; [adverse reactions](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/adverse-drug-reactions-and-pharmacovigilance.md)), [healthcare-associated infection](../../12-organ-system-specialties/08-infectious-diseases/infection-control-and-healthcare-associated-infection.md), diagnostic error ([cognitive bias](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/clinical-reasoning-and-cognitive-bias.md) plus results never seen), surgical error, falls, pressure injury, venous thromboembolism and failure to rescue. Each has a known anatomy and known defences; the problem is reliability, not knowledge.

3. **Humans are reliable to about one error in a hundred for routine tasks; systems must be designed for that.** Forcing functions (a connector that cannot fit the wrong port), standardisation (one concentration of a dangerous drug), checklists, read-back and redundancy convert a 1% human error rate into a 0.01% system rate, as aviation did. The WHO Surgical Safety Checklist trial (Haynes and colleagues, 2009) in eight hospitals roughly halved deaths (1.5% to 0.8%) and major complications (11% to 7%); the Michigan Keystone project (Pronovost and colleagues, 2006) cut central-line bloodstream infections by about two-thirds with a five-item checklist and the authority for a nurse to stop the procedure.

4. **You cannot improve what you do not measure, and you can be fooled by what you measure.** Donabedian (1966) separated *structure* (staff, equipment), *process* (was the right thing done) and *outcome* (what happened). Outcomes matter but are noisy, delayed and confounded by case mix; process measures are fast and attributable but can be gamed. Raw mortality rewards hospitals with healthier patients, risk adjustment is partial, and a hospital singled out for a bad year usually looks better next year by [regression to the mean](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/measurement-error-and-biological-variation.md) whether or not it changed anything.

5. **Improvement is a feedback loop run deliberately: Plan, Do, Study, Act.** Shewhart and Deming's cycle, brought to medicine by Berwick (1989) and the Institute for Healthcare Improvement, is small-scale experimentation on a process: predict, change one thing, measure over time, keep or discard. Statistical process control charts separate common-cause variation (the noise every process has) from special-cause variation (a real change), so that managers neither chase noise nor miss signals. This is [feedback and control](../../01-quantitative-and-scientific-foundations/03-systems-and-models/feedback-and-control.md) with the ward as the plant.

6. **Reporting only works in a just culture.** Incidents are the raw material of learning, and people report only if reporting is safe. A just culture distinguishes human error (console and redesign), at-risk behaviour (coach) and reckless behaviour (sanction), and treats the first two as information. Blame produces silence; silence produces repetition. Legal protection for incident reports and a statutory duty of candour (England, 2014) are the system's attempt to keep the loop open.

7. **Failure to rescue matters as much as failure to prevent.** Hospitals with similar complication rates differ widely in mortality because they differ in how fast deterioration is noticed and acted on (Silber and colleagues, 1992; Ghaferi and colleagues, 2009). Early-warning scores, rapid-response teams and clear escalation paths defend against this second failure. Staffing sets the baseline: each additional patient per nurse was associated with about 7% higher surgical mortality (Aiken and colleagues, 2002).

8. **Safety has a cost and a ceiling.** Every alert, double-check and sign-off slows care and dilutes attention; alert fatigue in electronic prescribing (most interruptive alerts are overridden) is a safety intervention that became a hazard. A safe system removes unnecessary steps as readily as it adds necessary ones.

## Key concepts

| Term | Meaning |
|---|---|
| Adverse event | Injury caused by medical management rather than the underlying disease |
| Active failure | An unsafe act at the point of care |
| Latent condition | A design or organisational weakness that makes active failures likely or lets them through |
| Swiss cheese model | Harm occurs when gaps in successive defences align |
| Structure, process, outcome | Donabedian's three things you can measure about quality |
| PDSA cycle | Plan, Do, Study, Act: a small, measured test of change |
| Just culture | Accountability that distinguishes error from recklessness |
| Failure to rescue | Death after a complication that timely recognition could have survived |

## How it fits

- **Below:** control theory and measurement error from [01](../../01-quantitative-and-scientific-foundations/README.md); the individual mechanisms of harm from pharmacology, infection control and clinical reasoning.
- **Above:** nothing; the outputs are checklists, alerts, escalation protocols and reporting duties that constrain every clinical layer, especially the [perioperative](../../13-acute-perioperative-and-procedural-care/02-anaesthesia-and-perioperative-medicine/perioperative-risk-and-complications.md) pathway where most procedural harm occurs.
- **Siblings:** [informatics](health-informatics-and-artificial-intelligence.md) is both the main new defence (decision support) and the main new hazard (alert fatigue, copy-forward errors); [economics](health-economics-and-priority-setting.md) prices harm, which is expensive; [financing](organisation-and-financing-of-health-systems.md) decides the staffing levels that set the baseline error rate.

## Common misconceptions

- **"Safe care means hiring better doctors."** Competence is necessary, not sufficient; the same competent people make the same errors in a badly designed system.
- **"Public league tables improve quality."** They improve the measured quantity. Published without good risk adjustment, they lead surgeons to avoid high-risk patients.
- **"An incident means someone was negligent."** The Harvard study found that about a quarter of adverse events involved negligence; most were system failures by people doing their jobs as designed.

## Go deeper

- James Reason, *Human Error* (1990): the active/latent distinction and the model every safety programme uses.
- Institute of Medicine, *To Err Is Human: Building a Safer Health System* (1999): the report that made patient safety a field.
- Atul Gawande, *The Checklist Manifesto* (2009): how simple checklists work, and why clinicians resist them.
