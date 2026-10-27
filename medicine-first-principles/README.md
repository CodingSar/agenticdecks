# Medicine from First Principles

A layered knowledge base of Medicine. It starts with the physics and chemistry that constrain living matter and climbs, one dependency at a time, through biochemistry, cells, genetics, anatomy and physiology, the microbes and the immune system, the mechanisms of disease, drugs, evidence and the clinical method, to the branches of medicine, how they interact, and medicine's place in society.

- **Leaves** (`*.md` files) hold the few load-bearing tenets you need to understand the essence of one topic.
- **Parents** (`README.md` in each folder) explain how their children fit together and how they connect to sibling areas. In the specialty layers (12–14) every parent also has an **Interfaces with other specialties** section: who refers to whom, which conditions sit on the border, and where decisions are made jointly.
- **[CROSS-CUTTING.md](CROSS-CUTTING.md)** follows ideas that recur in every layer (gradients and flow, feedback and homeostasis, supply and demand, compensation and decompensation, injury and repair, dose–response…) and links each to where it appears.
- **[_meta/PLAN.md](_meta/PLAN.md)** explains why the tree has this shape, which alternative structures were considered, and what was rejected.

The sibling project **[Computer Science from First Principles](../cs-first-principles/README.md)** uses the same method and templates.

## The stack

Read from the bottom up. Each layer depends only on layers with lower numbers.

```
 15  Medicine in Society ................ health systems, economics, ethics, law, inequity, planet, history
 14  Life Course, Mind & Integration .... paediatrics, obstetrics, psychiatry, geriatrics, palliative, primary care
 13  Acute & Procedural Care ............ surgery, anaesthesia, critical care, emergency medicine, eye and ENT
 12  Organ-System Specialties ........... cardiology ... neurology, dermatology: one system's diseases
 11  Clinical Method & Diagnostics ...... history, examination, reasoning, laboratory, imaging
 10  Epidemiology & Evidence ............ measures, study designs, trials, screening: how we know what works
 09  Pharmacology & Therapeutics ........ how an intervention reverses a mechanism, and at what cost
 08  Pathology .......................... the few mechanisms behind most disease
 07  Microbiology & Immunology .......... the organism's boundary: what attacks it and how it defends
 06  Physiology ......................... the body working: gradients, pumps and control loops
 05  Tissues & Anatomy .................. structure constrains function
 04  Genetics, Evolution & Development .. how the organism comes to be the way it is
 03  Cell Biology ....................... the living unit: energy, chemistry and information combine  <- roots meet
 02  Biochemistry & Molecular Biology ... chemistry organised into metabolism and information
 01  Quantitative Foundations ........... the formal root: probability, inference, feedback, models
 00  Physical & Chemical Foundations .... the material root: energy, gradients, charge, bonds, buffers
```

Medicine has **two roots**. The *material* one (00) says what matter can do: energy must flow, things move down gradients, charge separation makes signals, carbon makes recognisable shapes. The *formal* one (01) is the language of variation, inference and control in which physiology, epidemiology and clinical reasoning are stated. They meet in **03 Cell Biology**, where gradients, enzymes and genes first make a living unit. Every layer from 04 upward uses both.

## Layers

| # | Layer | The question it answers | Its key contribution to the stack |
|---|---|---|---|
| 00 | [Physical & Chemical Foundations](00-physical-and-chemical-foundations/README.md) | What can matter and energy do, and what do they forbid? | The constraints: gradients drive flow, energy is conserved and degraded, shape decides recognition, buffers hold pH |
| 01 | [Quantitative & Scientific Foundations](01-quantitative-and-scientific-foundations/README.md) | How do we reason about variation, uncertainty and control? | Probability, inference, feedback loops, compartment models and signal-versus-noise as medicine's grammar |
| 02 | [Biochemistry & Molecular Biology](02-biochemistry-and-molecular-biology/README.md) | How does chemistry become metabolism and information? | Enzymes, pathways, the gene-to-protein flow, receptors and ion gradients |
| 03 | [Cell Biology](03-cell-biology/README.md) | What is the smallest thing that is alive, and how does it live and die? | The cell: compartments, cycle, death, differentiation, and how cells form communities |
| 04 | [Genetics, Evolution & Development](04-genetics-evolution-and-development/README.md) | Why is the organism built this way, and how does it get built? | Inheritance, selection's fingerprints on health and disease, and the embryo |
| 05 | [Tissues & Anatomy](05-tissues-and-anatomy/README.md) | How are cells arranged into a body, and what does arrangement allow? | Four tissues, the body plan, and the relations that explain signs and surgery |
| 06 | [Physiology](06-physiology/README.md) | How does the body work, and how does it hold itself steady? | Organ systems as gradients, pumps and feedback loops kept near set points |
| 07 | [Microbiology & Immunology](07-microbiology-and-immunology/README.md) | What attacks the body, and how does it tell self from non-self? | Microbes, pattern recognition, specificity with memory, and the cost of recognition errors |
| 08 | [Pathology](08-pathology/README.md) | How does the body fail? | General mechanisms of disease: injury, inflammation, repair, haemodynamic failure, neoplasia |
| 09 | [Pharmacology & Therapeutics](09-pharmacology-and-therapeutics/README.md) | How do we change the body on purpose, and what does it cost? | The intervention: a mechanism reversed, with kinetics, dose–response and harm |
| 10 | [Epidemiology & Evidence](10-epidemiology-and-evidence/README.md) | How do we know what causes disease and what works? | Population measures, study designs, trials and the biases that fool them |
| 11 | [Clinical Method & Diagnostics](11-clinical-method-and-diagnostics/README.md) | How do we find out what is wrong with one person? | The encounter as Bayesian updating, and the laboratory and imaging that observe the body |
| 12 | [Organ-System Specialties](12-organ-system-specialties/README.md) | How does each organ system fail, and what reverses it? | Disease by system, each tracing mechanism to sign to test to treatment |
| 13 | [Acute, Perioperative & Procedural Care](13-acute-perioperative-and-procedural-care/README.md) | How do we intervene when time and physiology are against us? | Controlled injury, reversible unconsciousness, organ support and triage |
| 14 | [Life Course, Mind & Integrative Care](14-life-course-mind-and-integrative-care/README.md) | How does medicine differ by body, by mind and by setting, and who holds it together? | The child, the pregnant body, the mind, old age, the end of life, and the generalist as integrator |
| 15 | [Medicine in Society](15-medicine-in-society/README.md) | Who pays, who decides, who is left out, and what comes next? | Constraints and values (cost, consent, equity, safety, sustainability) that become requirements |

## How to read this

- **Bottom-up (the intended path).** Start at 00 and read each layer's README, then the leaves that interest you. You will never meet an idea that depends on something you have not seen.
- **Top-down (by need).** Start at the disease or specialty you care about. Each leaf's header lists what it **builds on**. Follow those links downward until things feel solid.
- **Across (by principle).** Pick an idea in [CROSS-CUTTING.md](CROSS-CUTTING.md), for example feedback, and follow it from the hormone axis to the baroreflex, the pharmacokinetic steady state and the epidemic that burns out.
- **By specialty interaction.** Start at [how the specialties interact](14-life-course-mind-and-integrative-care/05-primary-care-and-integration/how-the-specialties-interact.md), then read the "Interfaces with other specialties" section of any specialty parent in layers 12–14.

## Suggested short paths

| Goal | Path |
|---|---|
| Why does the heart fail, and why does that involve the kidney? | [fluids, pressure and flow](00-physical-and-chemical-foundations/01-physics-of-the-body/fluids-pressure-and-flow.md) → [the cardiac cycle](06-physiology/03-cardiovascular-system/the-cardiac-cycle-and-pump-function.md) → [sodium, water and volume](06-physiology/05-renal-system/sodium-water-and-volume-regulation.md) → [oedema](08-pathology/02-hemodynamic-disorders/edema-and-fluid-imbalance.md) → [autonomic and cardiovascular drugs](09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/autonomic-and-cardiovascular-drugs.md) → [heart failure](12-organ-system-specialties/01-cardiology/heart-failure.md) |
| How does one mutation become a cancer? | [DNA replication and repair](02-biochemistry-and-molecular-biology/03-genetic-information-flow/dna-replication-and-repair.md) → [the cell cycle](03-cell-biology/02-the-cell-life-cycle/the-cell-cycle-and-its-checkpoints.md) → [hallmarks of cancer](08-pathology/03-neoplasia/hallmarks-of-cancer.md) → [invasion and metastasis](08-pathology/03-neoplasia/invasion-metastasis-and-the-tumour-microenvironment.md) → [anticancer drugs](09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anticancer-drugs.md) → [principles of cancer care](12-organ-system-specialties/07-oncology/principles-of-cancer-care.md) |
| Why does a nerve conduct, and why does a stroke kill? | [electricity and excitable membranes](00-physical-and-chemical-foundations/01-physics-of-the-body/electricity-and-excitable-membranes.md) → [membrane transport and ion gradients](02-biochemistry-and-molecular-biology/04-cell-signalling/membrane-transport-and-ion-gradients.md) → [the action potential](06-physiology/02-nervous-system/membrane-potential-and-the-action-potential.md) → [thrombosis, embolism and infarction](08-pathology/02-hemodynamic-disorders/thrombosis-embolism-and-infarction.md) → [stroke](12-organ-system-specialties/10-neurology/stroke.md) → [rehabilitation](14-life-course-mind-and-integrative-care/05-primary-care-and-integration/rehabilitation-and-disability.md) |
| How does an infection become sepsis? | [bacteria](07-microbiology-and-immunology/01-microbes-and-infection/bacteria.md) → [pattern recognition](07-microbiology-and-immunology/02-innate-immunity/barriers-and-pattern-recognition.md) → [cytokines](07-microbiology-and-immunology/02-innate-immunity/cytokines-interferons-and-nk-cells.md) → [haemorrhage, shock and sepsis](08-pathology/02-hemodynamic-disorders/hemorrhage-shock-and-sepsis.md) → [antimicrobials](09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/antimicrobials.md) → [sepsis and multi-organ failure](13-acute-perioperative-and-procedural-care/03-critical-care/sepsis-and-multi-organ-failure.md) |
| How does a drug get from a tablet to a receptor, and how do we know it works? | [compartment models](01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md) → [receptors and ligands](02-biochemistry-and-molecular-biology/04-cell-signalling/receptors-and-ligands.md) → [absorption](09-pharmacology-and-therapeutics/01-pharmacokinetics/absorption-and-bioavailability.md) → [dose–response](09-pharmacology-and-therapeutics/02-pharmacodynamics/dose-response-and-therapeutic-index.md) → [randomized controlled trials](10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md) → [grading evidence](10-epidemiology-and-evidence/02-evidence-based-medicine/grading-evidence-and-guidelines.md) |
| How does a doctor decide what is wrong? | [Bayesian reasoning](01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md) → [diagnostic accuracy studies](10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md) → [history taking](11-clinical-method-and-diagnostics/01-the-clinical-encounter/history-taking-and-communication.md) → [clinical reasoning](11-clinical-method-and-diagnostics/01-the-clinical-encounter/clinical-reasoning-and-cognitive-bias.md) → [using tests](11-clinical-method-and-diagnostics/01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md) → [shared decision-making](11-clinical-method-and-diagnostics/01-the-clinical-encounter/prognosis-and-shared-decision-making.md) |
| Why does diabetes touch almost every specialty? | [glucose homeostasis](06-physiology/07-endocrine-system/glucose-homeostasis.md) → [atherosclerosis](08-pathology/02-hemodynamic-disorders/atherosclerosis.md) → [diabetes mellitus](12-organ-system-specialties/05-endocrinology/diabetes-mellitus.md) → [chronic kidney disease](12-organ-system-specialties/03-nephrology/chronic-kidney-disease-and-dialysis.md) → [the eye and vision loss](13-acute-perioperative-and-procedural-care/05-ophthalmology-and-ent/the-eye-and-vision-loss.md) → [chronic disease and self-management](14-life-course-mind-and-integrative-care/05-primary-care-and-integration/chronic-disease-and-self-management.md) |
| Why do we age and die? | [energy and thermodynamics](00-physical-and-chemical-foundations/01-physics-of-the-body/energy-and-thermodynamics.md) → [senescence and telomeres](03-cell-biology/02-the-cell-life-cycle/senescence-and-telomeres.md) → [evolutionary medicine](04-genetics-evolution-and-development/02-evolution/evolutionary-medicine.md) → [diseases of aging](08-pathology/04-genetic-metabolic-and-environmental-disease/diseases-of-aging-and-degeneration.md) → [frailty and multimorbidity](14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md) → [death, dying and end-of-life decisions](14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/death-dying-and-end-of-life-decisions.md) |
| Where does medicine meet society? | [bias, confounding and chance](10-epidemiology-and-evidence/01-epidemiology/bias-confounding-and-chance.md) → [screening principles](10-epidemiology-and-evidence/03-screening-and-prevention/screening-principles-and-biases.md) → [health economics](15-medicine-in-society/01-health-systems/health-economics-and-priority-setting.md) → [social determinants](15-medicine-in-society/03-populations-and-the-future/social-determinants-and-health-inequity.md) → [medical ethics](15-medicine-in-society/02-ethics-law-and-the-profession/medical-ethics.md) → [the future of medicine](15-medicine-in-society/03-populations-and-the-future/the-future-of-medicine.md) |

## Maintenance

- Every path is fixed in [`_meta/TAXONOMY.md`](_meta/TAXONOMY.md). Change the taxonomy first, then the files.
- Run `python3 _meta/check.py` to check for missing files, missing sections, broken links and anchors, and upward "Builds on" links.
- Style and templates: [`_meta/WRITER_BRIEF.md`](_meta/WRITER_BRIEF.md).
