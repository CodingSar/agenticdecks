# Health Informatics and Artificial Intelligence

> **Layer:** [15 Medicine in Society](../README.md) › [Health systems](README.md)
> **Builds on:** [Information, signals and noise](../../01-quantitative-and-scientific-foundations/03-systems-and-models/information-signals-and-noise.md), [Bayesian reasoning](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md), [Diagnostic accuracy studies](../../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md), [Using tests, pretest probability and thresholds](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md), [Patient safety and quality improvement](patient-safety-and-quality-improvement.md)
> **Enables:** [Consent, capacity and confidentiality](../02-ethics-law-and-the-profession/consent-capacity-and-confidentiality.md), [The future of medicine](../03-populations-and-the-future/the-future-of-medicine.md), [Surveillance and outbreak investigation](../../10-epidemiology-and-evidence/01-epidemiology/surveillance-and-outbreak-investigation.md)

## Essence

Medicine runs on information: a history, a result, an image, a drug chart, a referral. Health informatics represents that information so it can be stored, moved, found and acted on without losing meaning; the Electronic Health Record (EHR) is its central artefact. Artificial Intelligence (AI) in medicine is the next step: a statistical model reads the record, image or signal and outputs a probability or a recommendation. Both rest on the same foundations as a laboratory test: a noisy measurement, a prior, a threshold and a consequence. The idea that makes the subject coherent is that **a record or a model is a clinical instrument, and it must be evaluated like one**: for accuracy, for calibration in the population where it is used, for what it does to behaviour, and for harm.

## Core tenets

1. **Meaning survives transfer only if it is coded.** Free text is rich but unsearchable and ambiguous; "MS" is multiple sclerosis, mitral stenosis or morphine sulphate. Controlled terminologies fix meaning: the International Classification of Diseases (ICD) for diagnoses in statistics and billing, SNOMED CT for clinical concepts, LOINC for laboratory tests, DICOM for images. Exchange standards (HL7, now FHIR) fix the container. The coder's purpose shapes the data: diagnoses coded for reimbursement over-record what pays and under-record what does not, a bias inherited by every study built on claims data.

2. **The record changes the care; it is not a passive mirror.** Order sets, templates, copy-forward and defaults shape what is done; documentation for billing and litigation crowds out documentation for thinking. United States clinicians spend of the order of one to two hours on the EHR per hour with patients (time-motion studies, 2016 onward), a measured contributor to burnout. Interface choices are clinical decisions made at scale.

3. **Decision support works through the same arithmetic as a test, so it fails the same way.** An alert or a risk score has a sensitivity and specificity, and its usefulness depends on prevalence ([Bayes](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md)). A sepsis alert with 90% sensitivity and 90% specificity fired on a ward where 1% of patients are septic gives about nine false alarms for every true one. Clinicians learn to override, and most interruptive alerts are; the alert then protects nobody and slows everybody. The threshold for firing is a [treatment threshold](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md) decision and must be set as one.

4. **A model learns the data it was given, including its errors and its injustices.** Supervised learning finds whatever in the input predicts the label. If the label is a proxy, the model predicts the proxy: Obermeyer and colleagues (2019) showed that a widely used United States algorithm that used past healthcare *cost* as a proxy for *need* rated Black patients as healthier than equally sick white patients, because less had been spent on them; correcting the label would have more than doubled the share of Black patients identified for extra care. Models trained on one hospital's images can learn the hospital (scanner artefacts, portable-film markers) rather than the disease.

5. **Performance in the training population is not performance in yours.** Dataset shift (different case mix, prevalence, equipment, coding) degrades a model silently, so external validation is the equivalent of a [diagnostic accuracy study](../../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md) in a new spectrum of patients. A proprietary sepsis model deployed in hundreds of hospitals was reported by its developer with an area under the curve of 0.76–0.83; external validation at one centre (Wong and colleagues, 2021) found 0.63, with alerts on 18% of admissions. Discrimination and calibration must both be checked, and re-checked over time.

6. **Reading a pixel pattern is not the same as improving an outcome.** Deep learning matches specialists at narrow pattern tasks: diabetic retinopathy from fundus photographs (Gulshan and colleagues, 2016), skin lesion classification (Esteva and colleagues, 2017), mammography and chest radiograph triage. By 2025 the United States Food and Drug Administration had authorised over a thousand AI-enabled devices, mostly in radiology. But test-set accuracy is an intermediate outcome; whether patients do better requires the model to change a decision, a [randomised trial](../../10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md) question few models have yet passed. And automation changes the human: a model right 95% of the time trains its users to stop checking (automation bias), so its 5% of errors reach the patient unfiltered.

7. **Health data are both a public good and a privacy hazard.** Linked population-scale records enabled the detection of rare adverse drug effects, trials recruited through routine records during COVID-19, and much of modern epidemiology. The same linkage allows re-identification from a handful of dates and diagnoses, so the law ([confidentiality](../02-ethics-law-and-the-profession/consent-capacity-and-confidentiality.md)) treats health data as a special category. Trusted research environments, where the analysis goes to the data rather than the data to the analyst, are the current compromise.

## Key concepts

| Term | Meaning |
|---|---|
| EHR | A longitudinal digital record of a patient's care, shared across settings |
| Terminology | A controlled vocabulary that fixes the meaning of a coded concept |
| Clinical decision support | Software that offers a patient-specific recommendation at the point of care |
| Alert fatigue | Desensitisation to warnings when most are irrelevant |
| Calibration | Agreement between predicted probabilities and observed frequencies |
| Dataset shift | A change between training and deployment data that degrades a model |
| External validation | Testing a model on data from a different population or site |

## How it fits

- **Below:** [signal and noise](../../01-quantitative-and-scientific-foundations/03-systems-and-models/information-signals-and-noise.md) and [Bayes](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md) are the mathematics; [diagnostic accuracy studies](../../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md) supply the evaluation design; the hazards are a special case of [patient safety](patient-safety-and-quality-improvement.md).
- **Above:** nothing; the outputs are the record formats, alert thresholds and governance rules that every clinical layer works within, and the data that [surveillance](../../10-epidemiology-and-evidence/01-epidemiology/surveillance-and-outbreak-investigation.md) feeds on.
- **Siblings:** the measurement layer for [quality improvement](patient-safety-and-quality-improvement.md), the claims layer for [financing](organisation-and-financing-of-health-systems.md), and the real-world data source for [economic models](health-economics-and-priority-setting.md).

## Common misconceptions

- **"An AI that matches radiologists on a test set will replace radiologists."** A curated set is not the undifferentiated, shifting workload of practice, and reading is a fraction of the job. Two decades of computer-aided mammography detection in the United States improved nothing measurable (Lehman and colleagues, 2015).
- **"More data makes the bias go away."** Scaling a biased label gives a confidently biased model. Bias is in the labelling and the sampling, not the sample size.
- **"Anonymised data cannot identify anyone."** Date of birth, sex and postcode identify most of a population; rare diagnoses with dates identify the rest.

## Go deeper

- Ziad Obermeyer and colleagues, "Dissecting racial bias in an algorithm used to manage the health of populations", *Science* (2019): the definitive worked example of proxy-label bias.
- Eric Topol, *Deep Medicine* (2019): a clinician's survey of what AI can and cannot do, and the case that it should return time to the encounter.
