# Radiography and computed tomography

> **Layer:** [11 Clinical Method and Diagnostics](../README.md) › [Imaging and physiological measurement](README.md)
> **Builds on:** [Waves, sound, light and radiation](../../00-physical-and-chemical-foundations/01-physics-of-the-body/waves-sound-light-and-radiation.md), [Thorax](../../05-tissues-and-anatomy/03-regional-anatomy/thorax.md), [Radiotherapy and radiation biology](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md), [Using tests, pre-test probability and thresholds](../01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md)
> **Enables:** [Stroke](../../12-organ-system-specialties/10-neurology/stroke.md), [Trauma and haemorrhage control](../../13-acute-perioperative-and-procedural-care/01-surgery/trauma-and-haemorrhage-control.md), [The acute abdomen](../../13-acute-perioperative-and-procedural-care/01-surgery/the-acute-abdomen.md), [Common solid tumours](../../12-organ-system-specialties/07-oncology/common-solid-tumours.md)

## Essence

An X-ray image is a shadow. A beam of high-energy photons passes through the body, tissues absorb or scatter them in proportion to their density and atomic number, and a detector on the far side records what got through. Bone (calcium) stops most photons and appears white; air stops almost none and appears black; soft tissue and fluid lie between and, crucially, look alike. Computed Tomography (CT) rotates the source and detector around the patient and reconstructs, from hundreds of projections, a map of attenuation at every point in a slice, which separates the soft tissues that a single shadow superimposes. The idea that organises both is differential attenuation: what you can see is what differs in density from its surroundings, and what you cannot see is what does not.

## Core tenets

1. **Contrast comes from differences in attenuation, which depend on density and atomic number.** Attenuation falls off exponentially with the thickness and attenuation coefficient of the tissue traversed ([radiation physics](../../00-physical-and-chemical-foundations/01-physics-of-the-body/waves-sound-light-and-radiation.md)). Photoelectric absorption rises steeply with atomic number, which is why calcium in bone and iodine or barium in contrast agents stand out. The five radiographic densities (air, fat, soft tissue and fluid, bone, metal) are the whole vocabulary of a plain film; a lung full of fluid looks like a lung full of tumour because both are "soft tissue."

2. **A radiograph is a projection, so depth is lost and structures superimpose.** Everything along a ray's path is summed into one point. A nodule behind the heart is hidden; a second view at right angles restores depth; a border is visible only where two densities meet, so a pneumonia abutting the heart erases the cardiac silhouette (the silhouette sign) and locates itself by what it hides. Reading a film is reconstructing three dimensions from two, with knowledge of [anatomy](../../05-tissues-and-anatomy/03-regional-anatomy/thorax.md) as the prior.

3. **CT solves superimposition by measuring attenuation from many angles and solving for each voxel.** Each projection is a line integral of attenuation; with enough angles the inverse problem (filtered back-projection, now iterative reconstruction) recovers the attenuation of every volume element, expressed in Hounsfield units: water 0, air −1,000, fat about −100, soft tissue +20 to +80, acute blood +50 to +90, bone several hundred to over 1,000. A fresh haemorrhage is brighter than brain and an infarct is darker, which is why CT is the first test in [stroke](../../12-organ-system-specialties/10-neurology/stroke.md): it answers "is there bleeding" in minutes.

4. **Iodinated contrast adds a density where the blood goes.** Injected intravenously, iodine raises the attenuation of vessels and of tissues in proportion to their perfusion, and its timing selects the phase: arteries early, veins and parenchyma later, excretion into the urinary tract later still. Angiography, the detection of tumours by their abnormal enhancement, and the visualisation of leaking vessels in [trauma](../../13-acute-perioperative-and-procedural-care/01-surgery/trauma-and-haemorrhage-control.md) all depend on it. Its costs are allergic-type reactions and, in vulnerable kidneys, a transient fall in filtration.

5. **Ionising radiation is the price, and it is a population cost paid by individuals.** A chest radiograph delivers roughly 0.02 mSv, a CT of the abdomen roughly 10 mSv, against a natural background of about 2–3 mSv per year. The excess cancer risk from a single CT is small for one adult, on the order of 1 in 2,000 by linear extrapolation, and larger for children and for repeated scans ([radiation biology](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md)). Multiplied across tens of millions of scans per year it becomes a measurable fraction of cancers, which is why justification (does this scan change management?) is a legal and ethical requirement, not etiquette.

6. **Speed and resolution make CT the test of the emergency department, and its sensitivity makes incidental findings inevitable.** A whole-body CT takes seconds, shows fractures, bleeding, organ injury, obstruction, perforation and clot, and has transformed the management of [trauma](../../13-acute-perioperative-and-procedural-care/01-surgery/trauma-and-haemorrhage-control.md) and the [acute abdomen](../../13-acute-perioperative-and-procedural-care/01-surgery/the-acute-abdomen.md). It also finds something unexpected in a large fraction of adults (pulmonary nodules, adrenal and renal lesions, thyroid nodules), the great majority benign, each demanding a decision. The incidentaloma is the direct consequence of imaging people with a low pre-test probability for the finding, as the [threshold model](../01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md) predicts.


## Key concepts

| Term | Meaning |
|---|---|
| Attenuation | Reduction of beam intensity by absorption and scatter; depends on density, atomic number and thickness |
| Radiographic densities | Air, fat, soft tissue/fluid, bone, metal: the contrast steps visible on a plain film |
| Projection | A two-dimensional shadow summing everything along each ray |
| Silhouette sign | Loss of a normal border when adjacent tissue acquires the same density |
| Hounsfield unit | CT attenuation scale: water 0, air −1,000 |
| Reconstruction | Solving for each voxel's attenuation from many projections |
| Contrast phase | Timing of imaging after iodine injection to show arteries, veins, parenchyma or excretion |
| Effective dose (mSv) | Radiation dose weighted for tissue sensitivity; the currency of radiation risk |
| Justification | The requirement that a radiation exposure's expected benefit exceed its risk |
| Incidentaloma | An unexpected lesion found on imaging done for another reason |

## How it fits

- **Below:** image formation is the [physics of radiation](../../00-physical-and-chemical-foundations/01-physics-of-the-body/waves-sound-light-and-radiation.md); interpretation requires regional [anatomy](../../05-tissues-and-anatomy/03-regional-anatomy/thorax.md); the harm is [radiation biology](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md); the decision to scan is the [threshold model](../01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md).
- **Above:** CT is the first test in [stroke](../../12-organ-system-specialties/10-neurology/stroke.md), [trauma](../../13-acute-perioperative-and-procedural-care/01-surgery/trauma-and-haemorrhage-control.md) and the [acute abdomen](../../13-acute-perioperative-and-procedural-care/01-surgery/the-acute-abdomen.md), the staging instrument for [solid tumours](../../12-organ-system-specialties/07-oncology/common-solid-tumours.md), and the basis of low-dose lung-cancer [screening](../../10-epidemiology-and-evidence/03-screening-and-prevention/screening-principles-and-biases.md) in smokers.
- **Siblings:** [ultrasound](ultrasound.md) and [magnetic resonance imaging](magnetic-resonance-imaging.md) image without ionising radiation and show soft tissue contrast that attenuation cannot; [nuclear medicine](nuclear-medicine-and-molecular-imaging.md) images function where CT images structure, and the two are fused.

## Common misconceptions

- **"A normal chest X-ray excludes serious chest disease."**: small nodules, early pneumonia, pulmonary embolism and many mediastinal lesions are invisible on a projection; the film's negative likelihood ratio is modest for most of them.
- **"The radiation from one CT is negligible."**: for one adult the risk is small; across a population imaged repeatedly, and in children, it is not, which is why each scan needs a justification.
- **"A CT finding is a diagnosis."**: it is an attenuation pattern with a differential; a soft-tissue mass may be tumour, abscess, haematoma or collapsed lung, and the pre-test probability decides.

## Go deeper

- Jerrold T. Bushberg, J. Anthony Seibert, Edwin M. Leidholdt and John M. Boone, *The Essential Physics of Medical Imaging* (4th ed., 2020): image formation, CT reconstruction and dose.
- William Herring, *Learning Radiology: Recognizing the Basics* (4th ed., 2019): how images are read, from the five densities up.
- David J. Brenner and Eric J. Hall, "Computed tomography: an increasing source of radiation exposure", *New England Journal of Medicine* (2007): the population dose argument.
