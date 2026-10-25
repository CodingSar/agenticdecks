# Laboratory medicine

> **Layer:** [11 Clinical Method and Diagnostics](../README.md) › Laboratory medicine
> **Children:** [Clinical chemistry and reference ranges](clinical-chemistry-and-reference-ranges.md) · [Haematology and coagulation testing](haematology-and-coagulation-testing.md) · [Microbiological and serological diagnosis](microbiological-and-serological-diagnosis.md) · [Histopathology, cytology and molecular diagnostics](histopathology-cytology-and-molecular-diagnostics.md)

## What this area is about

The encounter yields what the clinician can see, hear and feel. Laboratory medicine yields what they cannot: the concentration of potassium, the number and shape of red cells, the organism in the blood, the architecture of a biopsy. Something like two thirds of clinical decisions in hospital involve a laboratory result, and most definitive diagnoses of cancer, infection and metabolic disease are made in a laboratory rather than at a bedside. This area covers the four disciplines that produce those results and, more importantly, the logic shared by all of them for turning a specimen into a number or a name and then into a probability.

The unifying idea is that **a laboratory result is a measurement of a sample, with variation, interpreted against a reference and a pre-test probability**. The sample may not represent the patient (haemolysed blood, a contaminated culture, a biopsy that missed the lesion). The measurement has imprecision and the patient has biological variation. The reference (a range, a breakpoint, normal tissue) is a convention with a built-in false-positive rate. And the result changes a probability by a likelihood ratio rather than delivering a verdict. Each child applies this logic to a different kind of specimen and a different kind of question.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Clinical chemistry and reference ranges](clinical-chemistry-and-reference-ranges.md) | Concentrations of solutes; the theory of reference ranges, decision limits and variation that the others reuse | [Measurement error](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/measurement-error-and-biological-variation.md); [physiology](../../06-physiology/README.md) |
| [Haematology and coagulation testing](haematology-and-coagulation-testing.md) | Counting and examining blood cells; the clotting cascade in a tube | [Blood](../../06-physiology/08-blood/red-cells-haemoglobin-and-iron.md); [haemostasis](../../06-physiology/08-blood/haemostasis-and-coagulation.md); chemistry |
| [Microbiological and serological diagnosis](microbiological-and-serological-diagnosis.md) | Identifying organisms by growth, genome or the host's antibody response | [Microbes](../../07-microbiology-and-immunology/01-microbes-and-infection/README.md); [antibodies](../../07-microbiology-and-immunology/03-adaptive-immunity/b-cells-and-antibodies.md) |
| [Histopathology, cytology and molecular diagnostics](histopathology-cytology-and-molecular-diagnostics.md) | Tissue and cell morphology, protein expression and genomics of a lesion | [Tissues](../../05-tissues-and-anatomy/01-tissues/README.md); [neoplasia](../../08-pathology/03-neoplasia/README.md) |

```
   specimen (blood, fluid, swab, tissue)
        |  pre-analytical: right site, time, container, label?
   measurement
        |  chemistry: concentration     haematology: count, morphology
        |  microbiology: grow / amplify / serology     histology: architecture, markers, genome
   reference (range, breakpoint, normal tissue) + analytical and biological variation
        |
   likelihood ratio  -->  revised probability  -->  decision
```

Read clinical chemistry first: it holds the general theory (reference ranges as percentiles, decision limits, reference change values, pre-analytical error) that the other three assume. Haematology follows naturally because it shares the blood sample and the analyser. Microbiology changes the question from "how much" to "what organism, and is it the cause." Histopathology changes it again to "what is this tissue doing," and is where laboratory medicine becomes the diagnosis rather than a contribution to it.

## Connections to sibling areas

- **[The clinical encounter](../01-the-clinical-encounter/README.md):** supplies the pre-test probability without which no result can be read, and the threshold logic that decides whether a test is worth ordering. The laboratory returns a likelihood ratio; the encounter supplies the odds it multiplies. A result that nobody asked a question of (a screening panel in a well person) produces false positives at the rate the reference range guarantees.
- **[Imaging and physiological measurement](../03-imaging-and-physiological-measurement/README.md):** the two parents are complementary samplings of the same patient: imaging shows where and how large, the laboratory shows what and how much. Staging a cancer needs both (the pathologist's margins and nodes, the radiologist's distant spread); diagnosing a pulmonary embolism combines a D-dimer with a scan; nuclear medicine and molecular pathology both label molecules, one in the living body, the other in a slide.

## Connections across layers

From below, this area takes the [chemistry of solutions and buffers](../../00-physical-and-chemical-foundations/02-chemistry-of-life/README.md) for its assays, [measurement error and distributions](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/README.md) for its reference ranges, [molecular techniques](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/molecular-techniques.md) for amplification and sequencing, [tissue histology](../../05-tissues-and-anatomy/01-tissues/README.md) as the pathologist's reference, [physiology](../../06-physiology/README.md) for what each analyte means, [microbiology and immunology](../../07-microbiology-and-immunology/README.md) for organisms and antibodies, [pathology](../../08-pathology/README.md) for the lesions it names, and [diagnostic accuracy studies](../../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md) for every test's sensitivity and specificity.

To the layers above it gives the definitions and monitoring of most medical disease: [electrolyte disorders](../../12-organ-system-specialties/03-nephrology/electrolyte-and-acid-base-disorders.md), [diabetes](../../12-organ-system-specialties/05-endocrinology/diabetes-mellitus.md), [anaemias](../../12-organ-system-specialties/06-haematology/anaemias.md), [sepsis](../../12-organ-system-specialties/08-infectious-diseases/fever-and-sepsis.md) and every cancer in [oncology](../../12-organ-system-specialties/07-oncology/README.md); the pre-transfusion and coagulation testing of [transfusion medicine](../../12-organ-system-specialties/06-haematology/transfusion-medicine.md) and [trauma](../../13-acute-perioperative-and-procedural-care/01-surgery/trauma-and-haemorrhage-control.md); the newborn bloodspot of [neonatology](../../14-life-course-mind-and-integrative-care/01-paediatrics/the-newborn-and-neonatology.md); the surveillance data of [infection control](../../12-organ-system-specialties/08-infectious-diseases/infection-control-and-healthcare-associated-infection.md); and the cost and information-system questions of [health informatics](../../15-medicine-in-society/01-health-systems/health-informatics-and-artificial-intelligence.md).

## Cross-cutting threads

- [Probability and uncertainty](../../CROSS-CUTTING.md#probability-and-uncertainty): a reference range is a percentile; a result is a likelihood ratio; variation is built into every number.
- [Specificity and recognition](../../CROSS-CUTTING.md#specificity-and-recognition): antibodies, probes and primers recognise their targets imperfectly, and cross-reaction is the laboratory's false positive.
- [Structure determines function](../../CROSS-CUTTING.md#structure-determines-function): histopathology reads function from architecture; a red cell's shape names its disease.
- [Time courses](../../CROSS-CUTTING.md#time-courses): antibody kinetics, enzyme half-lives, culture times and the lag between injury and marker all decide when a test can be positive.
- [Barriers and compartments](../../CROSS-CUTTING.md#barriers-and-compartments): sterile versus colonised sites, intracellular versus plasma analytes; where a sample comes from decides what it means.
