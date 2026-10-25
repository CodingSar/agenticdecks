# Nuclear medicine and molecular imaging

> **Layer:** [11 Clinical Method and Diagnostics](../README.md) › [Imaging and physiological measurement](README.md)
> **Builds on:** [Waves, sound, light and radiation](../../00-physical-and-chemical-foundations/01-physics-of-the-body/waves-sound-light-and-radiation.md), [Compartment models and exponential processes](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md), [Glycolysis, TCA cycle and oxidative phosphorylation](../../02-biochemistry-and-molecular-biology/02-metabolism/glycolysis-tca-cycle-and-oxidative-phosphorylation.md), [Radiotherapy and radiation biology](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md)
> **Enables:** [Common solid tumours](../../12-organ-system-specialties/07-oncology/common-solid-tumours.md), [Ischemic heart disease](../../12-organ-system-specialties/01-cardiology/ischemic-heart-disease.md), [Thyroid disease](../../12-organ-system-specialties/05-endocrinology/thyroid-disease.md), [Neurodegenerative disease](../../12-organ-system-specialties/10-neurology/neurodegenerative-disease.md)

## Essence

Every other imaging method sends energy into the body and reads what comes back. Nuclear medicine puts the source inside: a molecule chosen for where the body will take it is labelled with a radioactive atom, injected, and the gamma photons it emits are detected from outside to map where the molecule went. The image therefore shows function (perfusion, metabolism, receptor density, bone turnover, filtration) rather than structure, and its resolution is poor because a few millimetres is the best a gamma camera can localise a decay. The idea that makes it powerful is tracer kinetics: a tiny, pharmacologically inert quantity of a labelled molecule traces the fate of its unlabelled counterpart, so the image is a physiological measurement in space, and the idea that makes it safe enough is that the dose is set by the isotope's half-life and the small amount injected.

## Core tenets

1. **A radiopharmaceutical is a targeting molecule carrying an emitter.** The molecule decides the biology: a glucose analogue (fluorodeoxyglucose) accumulates in cells with high glycolytic flux ([glycolysis](../../02-biochemistry-and-molecular-biology/02-metabolism/glycolysis-tca-cycle-and-oxidative-phosphorylation.md)), which most cancers and inflamed tissue have; a phosphonate binds to bone being laid down; iodide is taken up by thyroid tissue; a somatostatin analogue binds neuroendocrine tumours. The isotope decides the physics: technetium-99m emits a 140 keV gamma photon with a 6-hour half-life, convenient for the gamma camera; fluorine-18 emits a positron with a 110-minute half-life. The specificity of the image is the specificity of the molecule's uptake, which is never complete.

2. **Decay is exponential, and the half-life sets both the imaging window and the dose.** Activity falls by half every half-life ([exponential processes](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md)); the effective half-life in the body is shorter still because of excretion. A short half-life allows a larger injected activity for a given absorbed dose and clears quickly, but must be produced nearby (fluorine-18 needs a cyclotron within a few hours' transport; technetium is eluted on site from a molybdenum generator). The absorbed dose depends on the isotope, the amount, and which organ concentrates and excretes the tracer; a typical study delivers a few millisieverts, comparable to CT ([radiation biology](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md)).

3. **The gamma camera counts photons through a collimator; Positron Emission Tomography (PET) localises them by coincidence.** A gamma camera accepts only photons travelling perpendicular to a lead collimator, so each count is placed along a known line; rotating the camera gives tomographic slices (single-photon emission computed tomography). In PET the emitted positron annihilates with an electron within a millimetre or two, producing two 511 keV photons travelling in opposite directions; detecting both within nanoseconds places the decay on the line between the detectors without a collimator, giving higher sensitivity and resolution of about 4–5 mm. Both are limited by counting statistics: images are noisy because every photon costs dose.

4. **Metabolic imaging stages cancer and measures response because tumours change their metabolism before they change their size.** Fluorodeoxyglucose PET-CT finds metastases that CT misses and distinguishes viable tumour from scar in a residual mass, which changes the stage and the treatment in a substantial fraction of patients with lymphoma and lung cancer ([solid tumours](../../12-organ-system-specialties/07-oncology/common-solid-tumours.md)). Its false positives are the other causes of high glycolysis (infection, inflammation, healing, brown fat, normal brain and heart), and its false negatives are slow-growing or non-glycolytic tumours. It is a [likelihood ratio](../01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md), not a biopsy.

5. **Perfusion imaging shows supply against demand.** A tracer taken up by heart muscle in proportion to blood flow, imaged at rest and under stress (exercise or a vasodilator drug), shows territory that is perfused at rest but not when demand rises: reversible ischaemia, the physiological lesion of [coronary disease](../../12-organ-system-specialties/01-cardiology/ischemic-heart-disease.md). Lung perfusion and ventilation scans detect the mismatch of pulmonary embolism; renal tracers measure each kidney's share of filtration; bone scans show the increased turnover around metastases, fractures and infection before the plain film changes.

6. **The same targeting turns diagnosis into therapy.** Replace the gamma- or positron-emitting isotope with a beta emitter and the molecule delivers radiation to the tissue that takes it up: iodine-131 for thyroid overactivity and cancer ([thyroid disease](../../12-organ-system-specialties/05-endocrinology/thyroid-disease.md)), radiolabelled somatostatin analogues for neuroendocrine tumours, radiolabelled prostate-specific membrane antigen ligands for prostate cancer. Theranostics uses the diagnostic scan to prove uptake, then the therapeutic isotope to exploit it. Amyloid and tau ligands for [neurodegenerative disease](../../12-organ-system-specialties/10-neurology/neurodegenerative-disease.md) extend molecular imaging to proteins, and are redefining diagnoses that were previously made only at autopsy.

## Key concepts

| Term | Meaning |
|---|---|
| Radiopharmaceutical | A molecule with known biological distribution labelled with a radioactive isotope |
| Tracer principle | A minute labelled quantity follows the fate of the unlabelled substance without perturbing it |
| Half-life (physical, biological, effective) | Time for activity to halve by decay, by excretion, and by both together |
| Gamma camera and collimator | Detector that localises single photons by accepting only those along known lines |
| Positron emission tomography (PET) | Localising decays by coincident detection of the two annihilation photons |
| Hybrid imaging (PET-CT, SPECT-CT) | Functional image fused with anatomical image from one acquisition |
| Fluorodeoxyglucose | Glucose analogue trapped in cells with high glycolytic flux; the main oncology tracer |
| Stress perfusion imaging | Comparing myocardial tracer uptake at rest and under stress to show reversible ischaemia |
| Theranostics | Using the same targeting molecule with a diagnostic and then a therapeutic isotope |

## How it fits

- **Below:** detection is the [physics of gamma radiation](../../00-physical-and-chemical-foundations/01-physics-of-the-body/waves-sound-light-and-radiation.md); decay is an [exponential process](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md); the tracers exploit [glycolysis](../../02-biochemistry-and-molecular-biology/02-metabolism/glycolysis-tca-cycle-and-oxidative-phosphorylation.md), [thyroid iodide uptake](../../06-physiology/07-endocrine-system/thyroid-adrenal-and-stress-hormones.md) and [receptor binding](../../02-biochemistry-and-molecular-biology/04-cell-signalling/receptors-and-ligands.md); the harm and the therapy are [radiation biology](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md).
- **Above:** staging and response assessment in [oncology](../../12-organ-system-specialties/07-oncology/common-solid-tumours.md), the functional diagnosis of [ischaemic heart disease](../../12-organ-system-specialties/01-cardiology/ischemic-heart-disease.md), the diagnosis and treatment of [thyroid disease](../../12-organ-system-specialties/05-endocrinology/thyroid-disease.md), and the molecular diagnosis of [dementia](../../12-organ-system-specialties/10-neurology/neurodegenerative-disease.md).
- **Siblings:** [CT](radiography-and-computed-tomography.md) and [MRI](magnetic-resonance-imaging.md) supply the anatomy that nuclear images lack and are fused with them; [histopathology](../02-laboratory-medicine/histopathology-cytology-and-molecular-diagnostics.md) labels the same molecules in a slide that molecular imaging labels in the body.

## Common misconceptions

- **"A hot spot on PET is cancer."**: it is high glucose uptake; infection, inflammation, healing tissue and brown fat are all hot, and some cancers are not.
- **"Nuclear medicine is a low-resolution version of CT."**: it measures a different quantity, function, at a resolution set by photon physics; its value is what it shows that structure cannot.
- **"The patient is dangerously radioactive afterwards."**: after a diagnostic study the activity is small and decays within hours; simple precautions suffice. After therapeutic iodine-131 the activity is large and isolation is real.

## Go deeper

- Fred A. Mettler and Milton J. Guiberteau, *Essentials of Nuclear Medicine and Molecular Imaging* (7th ed., 2019): the clinical applications organ by organ.
- Simon R. Cherry, James A. Sorenson and Michael E. Phelps, *Physics in Nuclear Medicine* (4th ed., 2012): detectors, PET and dosimetry.
- Michael E. Phelps, "Positron emission tomography provides molecular imaging of biological processes", *Proceedings of the National Academy of Sciences* (2000): the case for imaging biology rather than anatomy, by PET's co-inventor.
