# 11 Clinical Method and Diagnostics

> **Layer:** 11 Clinical Method and Diagnostics
> **Children:** [The clinical encounter](01-the-clinical-encounter/README.md) · [Laboratory medicine](02-laboratory-medicine/README.md) · [Imaging and physiological measurement](03-imaging-and-physiological-measurement/README.md)

## What this area is about

Every layer so far has been about disease in general or in populations. This layer is about one patient, now. Someone arrives with a complaint, and a clinician must work out what is probably wrong, how dangerous it is, what to find out next, and what will happen with and without each option. The first parent is the method: history, examination, reasoning, the logic of tests and thresholds, and the conversation about prognosis and choice. The second and third are the instruments the method calls on: the laboratory, which measures what the body contains and what grows from it, and imaging and physiological measurement, which observe the body's structure and function from outside. Together they are how medicine *observes*, and they are taught here as method, to be cited by every specialty above as service.

The one abstraction this layer contributes is **the probability of a diagnosis in one person, and the thresholds that turn it into action**. Layer 10 produced population measures: prevalences, likelihood ratios, effect sizes, risk scores. This layer applies them to an individual: prevalence becomes the pre-test probability, each symptom, sign and test result multiplies the odds by its likelihood ratio, and the result is compared with a test threshold and a treatment threshold set by the consequences of the two possible errors. Every result from the laboratory and every image is read inside that frame. A test that cannot move the probability across a threshold should not be ordered, and a test ordered without a probability in mind yields an incidental finding rather than an answer.

## Why this layer sits here

From below, the method is Bayesian, so it needs [01 Quantitative Foundations](../01-quantitative-and-scientific-foundations/README.md) for [Bayesian reasoning](../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md), [measurement error](../01-quantitative-and-scientific-foundations/01-probability-and-measurement/measurement-error-and-biological-variation.md) and [signals in noise](../01-quantitative-and-scientific-foundations/03-systems-and-models/information-signals-and-noise.md). The instruments are physics pointed at physiology, so imaging needs [00 Physical and Chemical Foundations](../00-physical-and-chemical-foundations/README.md) ([radiation, sound and radio waves](../00-physical-and-chemical-foundations/01-physics-of-the-body/waves-sound-light-and-radiation.md), [electricity in excitable membranes](../00-physical-and-chemical-foundations/01-physics-of-the-body/electricity-and-excitable-membranes.md)) and the laboratory needs its [chemistry](../00-physical-and-chemical-foundations/02-chemistry-of-life/README.md). Reading an image needs [05 Anatomy](../05-tissues-and-anatomy/README.md); reading a trace or an analyte needs [06 Physiology](../06-physiology/README.md); naming an organism or a lesion needs [07 Microbiology and Immunology](../07-microbiology-and-immunology/README.md) and [08 Pathology](../08-pathology/README.md). And the numbers that fill in the method come from [10 Epidemiology and Evidence](../10-epidemiology-and-evidence/README.md): prevalence as prior, [likelihood ratios](../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md) from accuracy studies, [effect sizes](../10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md) for the treatment threshold, [risk scores](../10-epidemiology-and-evidence/03-screening-and-prevention/risk-prediction-and-stratification.md) for prognosis.

What the layers above need is the method and the instruments as a shared service. Every disease leaf in [12](../12-organ-system-specialties/README.md), [13](../13-acute-perioperative-and-procedural-care/README.md) and [14](../14-life-course-mind-and-integrative-care/README.md) has a section on "what the tests show," and this is where those tests are explained once: the ECG, troponin, CT, culture and biopsy are described here and cited there. The reasoning method is the same in a cardiology clinic, a resuscitation bay and a general practice, differing in tempo and in the dangerous diagnosis that must be excluded first. [15 Medicine in Society](../15-medicine-in-society/README.md) takes diagnostic error as a safety problem, the test-ordering decision as an economic one, the conversation as a legal one (consent), and the image and the record as data for information systems.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [01 The clinical encounter](01-the-clinical-encounter/README.md) | History, examination, reasoning and its biases, tests and thresholds, prognosis and shared decisions: the method | 01 Bayes; 10 measures, accuracy, trials, risk scores |
| [02 Laboratory medicine](02-laboratory-medicine/README.md) | Chemistry, haematology, microbiology, histopathology: measuring what the body contains and naming what grows or what a tissue is | 00 chemistry; 01 measurement error; 06, 07, 08 |
| [03 Imaging and physiological measurement](03-imaging-and-physiological-measurement/README.md) | X-ray, ultrasound, MRI, nuclear medicine, electrophysiology, functional tests: observing structure and function from outside | 00 physics; 05 anatomy; 06 physiology; 09 radiation biology |

```
   patient --> history, examination --> hypotheses with probabilities      (01 encounter)
                                              |
                     probability vs test and treatment thresholds
                                              |
                  +---------------------------+---------------------------+
                  |                                                       |
          laboratory (02):                                      imaging & function (03):
          what and how much; what organism; what tissue          where, how large, how it works
                  |                                                       |
                  +--------------- likelihood ratios ---------------------+
                                              |
                    revised probability --> diagnosis, prognosis, shared decision
                                              |
                               specialties (12-14), society (15)
```

Read the encounter first and in full: it supplies the frame in which every result of the other two parents is interpreted. The laboratory parent then begins with clinical chemistry, because the theory of reference ranges and variation it states is reused by every other test in the layer, including the predicted values of functional testing. The imaging parent is best read as six answers to one question, "what physical property does this modality measure, and so what can it see," followed by the electrical and functional tests that measure physiology directly.

## Connections to neighbouring layers

- **[00 Physical and Chemical Foundations](../00-physical-and-chemical-foundations/README.md):** the imaging parent is the most concentrated application of layer 00 in the clinical half of the tree; X-ray attenuation, acoustic impedance, nuclear spin and relaxation, radioactive decay and extracellular currents are each a leaf there made into an instrument here.
- **[01 Quantitative and Scientific Foundations](../01-quantitative-and-scientific-foundations/README.md):** clinical reasoning is Bayes' theorem performed by a human mind, and cognitive bias is the catalogue of where the mind departs from it; reference ranges are percentiles; the ECG and EEG are signals extracted from noise.
- **[06 Physiology](../06-physiology/README.md):** every sign, analyte and trace is a physiological variable observed; the layer could be described as physiology measured in one person.
- **[08 Pathology](../08-pathology/README.md):** histopathology is pathology's method made a service; the natural history of disease is the time course the history reconstructs and prognosis projects.
- **[10 Epidemiology and Evidence](../10-epidemiology-and-evidence/README.md):** the direct supplier of every number the method uses, and the standard by which each test's accuracy is judged. Layer 10 is about populations; this layer is about the person drawn from them.
- **[12 Organ-system Specialties](../12-organ-system-specialties/README.md), [13 Acute Care](../13-acute-perioperative-and-procedural-care/README.md), [14 Life Course and Integrative Care](../14-life-course-mind-and-integrative-care/README.md):** the customers. Each specialty applies this method with its own priors, its own dangerous diagnoses and its own preferred instruments; emergency medicine compresses it into minutes and primary care stretches it over years.
- **[15 Medicine in Society](../15-medicine-in-society/README.md):** diagnostic error becomes patient safety, test ordering becomes cost, the conversation becomes consent, and the record and image become the data of health informatics and its machine-learning readers.

## Connections across layers

This layer is the point at which the knowledge of the lower layers is brought to bear on one person and turned into a decision. Below it, the tree describes how bodies work and fail and how populations are studied; above it, the specialties apply the method to particular organs, ages and settings. It carries two things upward: a method of reasoning under uncertainty that is the same in every specialty, and a set of instruments, each explained once by its physics and physiology, that every specialty orders and interprets.

## Cross-cutting threads

- [Probability and uncertainty](../CROSS-CUTTING.md#probability-and-uncertainty): the layer's defining thread; the honest output of an encounter is a probability, and every test is a likelihood ratio.
- [Harm and benefit](../CROSS-CUTTING.md#harm-and-benefit): the thresholds are set by the harms of each error; radiation, false positives and incidental findings are the costs of looking.
- [Signalling and information](../CROSS-CUTTING.md#signalling-and-information): symptoms, signs, traces and images are noisy signals from mechanisms, decoded against a prior.
- [Structure determines function](../CROSS-CUTTING.md#structure-determines-function): imaging infers function from structure, histopathology reads function from architecture, functional tests infer structure from function.
- [Compensation and decompensation](../CROSS-CUTTING.md#compensation-and-decompensation): reserve hides disease at rest, which is why stress tests exist and why creatinine stays normal until half the nephrons are gone.
- [Time courses](../CROSS-CUTTING.md#time-courses): tempo of onset is the most discriminating feature of a history; antibody kinetics, marker half-lives and tracer decay decide when a test can be positive.
- [Specificity and recognition](../CROSS-CUTTING.md#specificity-and-recognition): antibodies, probes, primers and radiotracers recognise their targets imperfectly; sensitivity and specificity are the measure of that imperfection.
