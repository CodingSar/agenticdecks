# Plan: a first-principles taxonomy of Medicine

## 1. Goal

Build a knowledge base that explains Medicine from the ground up: the physics and chemistry that constrain living matter at the bottom, the biology they give rise to, the body in health, the mechanisms of disease, the tools for recognising and treating it, the branches of medical practice and how they interact, and finally medicine's place in society. Every **leaf** holds the few tenets you must understand to grasp the essence of that topic. Every **parent** explains how its children fit together and how it connects to its siblings. The tree should be deep enough to be a map of the whole field, but each file short enough to read in one sitting.

This is a sibling of [`../../cs-first-principles/`](../../cs-first-principles/README.md) and follows the same method: a fixed taxonomy, parallel writer agents, a mechanical checker, a review pass, and a cross-cutting index.

## 2. What "first principles" means here

1. **Dependency order.** A topic appears above everything it needs. Read bottom-up, nothing relies on an idea you have not yet met. Heart failure (layer 12) is written for a reader who already knows the cardiac cycle (06), the renin–angiotensin system (06), edema (08) and receptor pharmacology (09).
2. **Essence over coverage.** Medicine is vast; a leaf says what is *true and load-bearing*, not everything known. The test: if you forgot this, would you misunderstand the topic? A leaf on diabetes names the handful of mechanisms that explain every complication, not every drug.
3. **Mechanism over vocabulary.** Every tenet says *why* a thing happens or *what force* shapes it. "Oedema forms when Starling forces favour filtration" is a label; "Fluid leaves capillaries when hydrostatic pressure inside exceeds the oncotic pull of plasma proteins, so heart failure (raised venous pressure), liver failure (low albumin) and inflammation (leaky walls) all produce oedema by moving one term of the same equation" is a tenet.
4. **Explicit edges.** A tree shows one parent per node, but medicine is a graph: inflammation appears in immunology, pathology, every specialty and pharmacology. Every file states what it **builds on** and what it **enables**, and [`../CROSS-CUTTING.md`](../CROSS-CUTTING.md) follows ideas such as feedback, gradients, supply and demand, and compensation through every layer in which they appear.
5. **The patient, not the exam.** Facts that matter only for a licensing exam (eponyms, trivia, drug doses) are left out. Facts that change how one reasons about a patient stay in.

## 3. Top-level structures considered

Choosing the top level decides which relationships the tree shows for free and which it must spell out. Six candidates were compared.

### A. The classical curriculum (preclinical sciences, then clinical disciplines; Flexner, 1910)

- **Strengths:** It is the dependency order most medical schools used for a century: anatomy, physiology, biochemistry, then pathology and pharmacology, then the clinical clerkships. It matches the request (foundations at the bottom).
- **Weaknesses:** It treats the preclinical sciences as a flat list, so it does not show that physiology rests on cell biology, which rests on biochemistry, which rests on chemistry. It also has no place for the quantitative sciences (statistics, epidemiology) that modern medicine rests on, and it says nothing about how the clinical disciplines relate.

### B. Organ-system integration (each system from molecule to bedside; the "integrated curriculum")

- **Strengths:** Everything about the heart sits together, which is how clinicians think.
- **Weaknesses:** Processes that cut across systems (inflammation, neoplasia, infection, pharmacokinetics, shock, aging) must either be duplicated in every system or pulled out, and the foundations (chemistry, cell biology, genetics) are repeated or assumed. It hides the fact that one mechanism explains many diseases.

### C. Scale hierarchy (molecule → cell → tissue → organ → organism → population)

- **Strengths:** This is honest about what the body is made of, and it is the order in which emergent properties appear: no membrane potential below the cell, no blood pressure below the organ, no herd immunity below the population.
- **Weaknesses:** Scale is not the only dependency. Disease mechanisms, diagnosis and therapy are *processes* acting at every scale, and evidence (statistics, trial design) is a method, not a scale. A pure scale ladder has nowhere to put them.

### D. Process ordering (normal → abnormal → recognise → treat → prevent)

- **Strengths:** It mirrors clinical work: know health, know how it fails, detect the failure, correct it, stop it recurring.
- **Weaknesses:** It only applies above the level of the organism. It gives no structure to the foundations, and "normal" alone would be half the tree.

### E. Specialty organisation (how hospitals and colleges divide the work)

- **Strengths:** A reader finds "cardiology" where they expect it, and the real interactions between specialties (referral, shared patients, disputed territory) can be shown.
- **Weaknesses:** Specialties are historical and administrative, not logical: neurology and psychiatry split for reasons of history, dermatology is defined by an organ and oncology by a disease process, emergency medicine by a time window. Specialties cannot be the bottom of anything; they consume every foundation.

### F. Historical (humoral medicine → anatomy → germ theory → physiology → molecular medicine → evidence-based medicine → genomic medicine)

- **Strengths:** It shows why ideas arose and what each displaced.
- **Weaknesses:** History is not dependency: anatomy (16th century) was mapped long before the chemistry it depends on, and statistics entered medicine (1940s) long after the diseases it now judges treatments for.

## 4. Decision: a scale ladder at the bottom, a process ladder in the middle, specialties near the top, society at the top, with two roots and a cross-cutting index

The chosen structure is **C's scale hierarchy for layers 00–07, D's process ordering for layers 08–11, E's specialty organisation for layers 12–14, and society at 15**, numbered as one topological order, with **A** as the sanity check (a medical graduate should recognise every area) and **F** confined to a leaf on history.

- **Top level = numbered layers 00–15.** The numbers are a topological order of the dependency graph: every layer depends only on lower numbers.
- **Two roots at the bottom.** `00` Physical and Chemical Foundations is the material root: the body is matter and obeys thermodynamics, fluid dynamics, electrostatics and chemistry. `01` Quantitative and Scientific Foundations is the formal root: probability, inference, feedback and models are the language in which physiology, epidemiology and clinical reasoning are stated. `01` does not depend on `00`; it sits at `01` because everything from `02` upward is described in it. As in the CS tree, `00` may cite `01` (physics is written in mathematics); the checker allows that one upward exception.
- **The roots meet at the cell.** `02` Biochemistry is chemistry organised into metabolism and information; `03` Cell Biology is where thermodynamics (gradients, pumps), chemistry (enzymes) and information (genes, signals) first combine into a living unit. From `04` upward every layer uses both roots.
- **Health before disease.** Layers `04`–`07` describe the organism working: inheritance and development, tissues and anatomy, physiology, and the microbes and immune system that define its boundary. `08` Pathology is the first layer about failure, and it is written as *general* pathology (injury, inflammation, hemodynamics, neoplasia) so that every specialty above can cite one mechanism instead of restating it.
- **Treatment before diagnosis-at-the-bedside, evidence before both.** `09` Pharmacology sits directly on physiology and pathology (a drug acts on a receptor to reverse a mechanism). `10` Epidemiology and Evidence supplies the measures (sensitivity, relative risk, number needed to treat) that `11` Clinical Method applies to one patient. Clinical reasoning is applied Bayesian inference; it needs `01` for the mathematics and `10` for the prevalences and test characteristics.
- **Specialties in three layers by what they consume.** `12` Organ-system specialties (cardiology to dermatology) sit directly on a system's physiology, its pathology, its drugs and its tests. `13` Acute, perioperative and procedural care (surgery, anaesthesia, critical care, emergency medicine, the sense organs) uses the organ-system specialties: a resuscitation is cardiology, pulmonology and nephrology at speed. `14` Life course, mind and integrative care (paediatrics, obstetrics, psychiatry, geriatrics and palliative care, primary care) spans every system in a particular body or a particular setting; primary care is the integrator and holds the leaf on how the specialties interact.
- **Society at the top.** `15` is where medicine meets money, law, ethics, information systems, inequality, the planet and its own history.
- **Cross-cutting principles** (feedback and homeostasis, gradients and flow, supply and demand, compensation and decompensation, injury and repair, specificity and recognition, dose–response, probability and uncertainty, harm and benefit, and others) get their own index, `CROSS-CUTTING.md`, linking each to every leaf where it appears. This repairs the main weakness of any tree.

### Why this order and not another (key placement decisions)

| Decision | Alternative rejected | Reason |
|---|---|---|
| Physics and chemistry as one layer (00) | Two layers | Both are the material root and neither depends on the other in a way medicine cares about. Diffusion, pressure and electrostatics (physics) and bonding, buffers and redox (chemistry) are used side by side from biochemistry upward. |
| Quantitative foundations at 01, below biology | Statistics near epidemiology (10) | Physiology already needs feedback, exponential decay and signal-to-noise; genetics needs probability; every lab value needs the idea of a reference range. Putting the mathematics low says that medicine is a quantitative science before it is a clinical one. |
| Feedback and control in 01 | Inside physiology | Negative feedback is a mathematical idea (gain, set point, delay, oscillation) that homeostasis, hormone axes, pharmacokinetic steady state and epidemic control all instantiate. Physiology (06) applies it. |
| Membrane transport and ion gradients inside 02 Cell signalling | Inside 06 Physiology | Pumps, channels and the Nernst equation are molecular machinery and chemistry. The action potential (06) is what a whole cell does with them. |
| Genetics, evolution and development as one layer (04) above cell biology | Genetics with biochemistry | Inheritance needs meiosis (03); development needs the cell cycle, signalling and differentiation (03); evolution needs population thinking (01) and mutation (02). They are three views of how the organism comes to be the way it is, and evolutionary medicine is the "why" behind much of pathology. |
| Anatomy (05) below physiology (06) | Anatomy and physiology interleaved by system | Structure constrains function: you cannot explain the cardiac cycle without the valves, or ventilation–perfusion matching without the lung's shape. Regional anatomy is kept to four leaves of load-bearing relations; the detail belongs to atlases. |
| Microbiology and immunology together (07), above physiology | Immunology inside physiology; microbiology inside infectious diseases | The immune system is defined by what it defends against, so the microbes are taught first in the same layer. It sits above physiology because immunity uses the circulation, lymphatics and endocrine stress response, and below pathology because inflammation is the immune system seen through a microscope. |
| General pathology (08) as the first layer about disease | Disease inside each specialty | A few mechanisms (injury, inflammation, thrombosis, neoplasia) explain most disease in every organ. Teaching them once lets 46 specialty leaves cite rather than repeat them. |
| Pharmacology (09) below Epidemiology (10) and Clinical Method (11) | Pharmacology beside the specialties | A drug's mechanism follows directly from physiology and pathology; whether it *works* is settled by trials (10) and whether to *give* it to this patient by clinical reasoning (11). Non-drug therapies (surgery principles, radiotherapy, devices, nutrition, behaviour change) are placed here too so that therapy is one layer. |
| Epidemiology and Evidence (10) below Clinical Method (11) | Clinical method first, evidence later | Pre-test probability is prevalence; sensitivity comes from a diagnostic accuracy study; a treatment threshold needs an effect size. The bedside applies population measures to one person, so the measures come first. Screening sits in 10 because it is a population decision judged by epidemiological biases. |
| Imaging and laboratory medicine inside 11 | A separate "diagnostic specialties" layer | Radiology and pathology are specialties, but their content is *how we observe the body*, which every clinical layer needs. They are taught as method and cited by specialties as service. |
| Three specialty layers (12, 13, 14) rather than one | One flat layer of specialties | Topological order is real here: critical care uses cardiology and nephrology; paediatrics and geriatrics use all of 12 and 13 in a different body; primary care integrates everything. One flat layer would hide that. |
| Psychiatry in 14, not with neurology in 12 | Psychiatry beside neurology | Both rest on neuroscience (06), but psychiatry's objects (mood, belief, behaviour) are properties of the whole person in a social context, diagnosed by formulation rather than lesion. It sits with the life-course specialties, with neurology linked explicitly. |
| Ophthalmology and ENT (ear, nose and throat) in 13 | In 12 with the organ systems | Both are predominantly surgical specialties built around procedures and devices, and their emergencies (acute glaucoma, airway obstruction) are time-critical. |
| Health systems, ethics and law at the top (15) | Ethics as a foundation at the bottom | Ethics and law constrain every clinical decision, but their content (consent, capacity, resource allocation) presupposes knowing what medicine can do. They are stated as values that become requirements. |

## 5. File conventions

- **Directories** are parent nodes; each has a `README.md` (the parent explanation).
- **Leaves** are `.md` files inside a parent directory, one topic each.
- **Numeric prefixes** (`00-`, `01-`…) give reading order at every level.
- **Links** are relative so the tree works on GitHub and in any Markdown viewer.
- **Abbreviations:** each file spells an abbreviation out on first use, for example "Adenosine Triphosphate (ATP)", then uses the short form. Every file may be the first one a reader opens.
- **Nomenclature:** International Nonproprietary Names (INN) for drugs, SI units, British spelling as default (haemoglobin, oedema) except in established names.
- Templates and style rules: [`WRITER_BRIEF.md`](WRITER_BRIEF.md). The full path list is in [`TAXONOMY.md`](TAXONOMY.md).

## 6. Coverage check against a standard medical curriculum

| Curriculum area (typical undergraduate medical programme) | Where it lives |
|---|---|
| Biophysics, medical chemistry | 00 |
| Biostatistics, research methods | 01, 10 |
| Biochemistry, molecular biology | 02 |
| Cell biology, histology | 03, 05 |
| Medical genetics, embryology | 04 |
| Anatomy | 05 |
| Physiology, neuroscience | 06 |
| Microbiology, immunology | 07 |
| Pathology (general) | 08; systemic pathology inside 12 |
| Pharmacology, therapeutics | 09 |
| Epidemiology, public health, preventive medicine | 10, 15 |
| Clinical skills, laboratory medicine, radiology | 11 |
| Internal medicine and its subspecialties, neurology, dermatology | 12 |
| Surgery, anaesthesia, intensive care, emergency medicine, ophthalmology, ENT | 13 |
| Paediatrics, obstetrics and gynaecology, psychiatry, geriatrics, palliative care, general practice, rehabilitation | 14 |
| Medical ethics, law, health systems, health informatics, global health, history | 15 |

Dentistry, veterinary medicine, nursing and the allied professions are outside the scope, as is clinical management detail (doses, protocols), which changes faster than a knowledge base should.

## 7. Process

1. **Plan** (this file) and fix the full path list (`TAXONOMY.md`) so that cross-links can be written before the target files exist.
2. **Draft in parallel.** One writer agent per layer or half-layer (15 writers), all working to `WRITER_BRIEF.md`.
3. **Verify mechanically.** `_meta/check.py` finds missing files, files outside the taxonomy, missing sections, broken relative links and anchors, and "Builds on" links that point upward.
4. **Review.** A separate pass per pair of layers reads for factual errors, missing load-bearing tenets and weak connections, and fixes them (`REVIEW_BRIEF.md`).
5. **Cross-cutting index.** Build `CROSS-CUTTING.md` from the finished leaves.
6. **Iterate** until the checker is clean and the review finds nothing load-bearing.

## 8. Lessons carried over from the CS tree

- **"Builds on" must point down; everything else goes in the body.** A higher-layer idea that is related (heart failure, for a physiology leaf on the cardiac cycle) goes in "Enables" or in the text with a link, never in "Builds on". The checker reports violations as `UPWARD`.
- **00 and 01 are twin roots.** Physics is written in mathematics, so 00 may build on 01; nothing else may point upward.
- **Gaps found by writers become new leaves in the review pass**, not ad hoc files. Writers report them; the taxonomy is amended first.
- **Fast-moving figures are dated.** Prevalences, mortality figures and drug approvals carry a year and, where relevant, a region.

## 9. What was done

(Filled in as passes complete.)

| Pass | Work | Result |
|---|---|---|
| 1. Draft | 15 writer agents to `WRITER_BRIEF.md` | |
| 2. Review | Reviewer agents to `REVIEW_BRIEF.md` | |
| 3. Index | `CROSS-CUTTING.md` | |
| 4. Coherence | Audit of the 16 layer READMEs as one bottom-up story | |

## 10. Known limits and next iterations

- Leaves are capped at about 1,100 words, so each one is an essence, not a textbook chapter. The "Go deeper" sources are the next step.
- Clinical management (doses, protocols, guideline thresholds) is deliberately absent or illustrative only; it is where medicine changes fastest and where a knowledge base is least trustworthy.
- Candidate leaves not yet added: medical imaging physics as its own parent, audiology, clinical nutrition as a specialty, transfusion as a separate laboratory discipline, military and expedition medicine, forensic medicine, dentistry's interface with medicine.
