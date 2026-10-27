# Writer brief

You are writing part of a first-principles knowledge base of Medicine. Read [`PLAN.md`](PLAN.md) (why the tree has this shape) and [`TAXONOMY.md`](TAXONOMY.md) (every path that exists) first. The sibling project [`../../cs-first-principles/`](../../cs-first-principles/README.md) is finished and uses the same templates; open two or three of its leaves (for example `07-operating-systems/03-concurrency/deadlock.md`) to see the target quality and density.

## The reader

A capable, scientifically literate adult (think: an engineer or scientist) who wants the *essence* of each topic: what is true, why it is true, and how it connects to everything else. They can follow equations and mechanisms but are not a clinician and should never need a textbook open to follow a file. They are learning how medicine *thinks*, not how to treat a patient.

## Rules for every file

1. **Create exactly the paths in `TAXONOMY.md`.** Do not add, rename or skip files. If you think the taxonomy is wrong, write the file anyway and add your suggestion to your final report.
2. **Abbreviations:** spell out each abbreviation on its first use *in each file*, then use the short form: "Adenosine Triphosphate (ATP)", then "ATP". Every file may be the first one a reader opens. This includes common ones (Central Nervous System (CNS), Deoxyribonucleic Acid (DNA), Electrocardiogram (ECG)) in the first file where they appear in body text. Do not expand abbreviations inside headings. Units (mmHg, mmol/L, kPa) and pH need no expansion.
3. **Links are relative** and point only to paths in `TAXONOMY.md` (or `README.md` of a directory listed there, or `../CROSS-CUTTING.md`-style paths to the root files). Count the `../` carefully: a leaf at `12-organ-system-specialties/01-cardiology/heart-failure.md` links to `../../06-physiology/03-cardiovascular-system/the-cardiac-cycle-and-pump-function.md`.
4. **Mechanism over vocabulary.** Every tenet explains *why* or *what force* produces it. "Oedema forms when Starling forces favour filtration" is a label; "Fluid leaves a capillary when the hydrostatic pressure inside exceeds the oncotic pull of plasma proteins, so heart failure (high venous pressure), liver failure (low albumin) and inflammation (leaky wall) all cause oedema by moving one term of the same balance" is a tenet.
5. **Accuracy is non-negotiable.** Use well-established facts. Give numbers with their order of magnitude and context ("resting cardiac output ~5 L/min in an adult"; "~10% lifetime risk, high-income countries, 2020s"). Fast-moving figures (prevalence, mortality, approvals) carry a year and, where relevant, a region. No invented citations: cite only real, canonical works you are sure of (author, title, year). Where you are unsure of a figure, give a safe range or omit it, and list it in your report.
6. **Not clinical advice.** No doses, no protocols, no "first-line treatment is X" lists. Name a drug class and its mechanism when it illustrates a tenet; name a specific drug only as an example ("a beta-blocker such as bisoprolol"). Use International Nonproprietary Names (INN), never brand names. Guideline thresholds change; mechanisms do not.
7. **Plain, direct English.** Short sentences. Active voice. No filler, no marketing tone, no reassurance. British spelling by default (haemoglobin, oedema, anaemia, tumour) except inside established names and taxonomy file names. SI units, with mmHg for blood pressure. Use a small example, equation or numerical case when it makes a tenet concrete. Use Markdown tables to compare things.
8. **Length.** Leaves: 500–1,100 words. Parent READMEs: 400–900 words. Layer READMEs (top-level `NN-*/README.md`): 600–1,200 words. Be dense, not long.
9. **No front matter, no emoji, no HTML.** ASCII diagrams in fenced code blocks are welcome when they show structure (a pathway, a feedback loop, a flow of blood or signal, a decision tree).

## Leaf template

```markdown
# <Title>

> **Layer:** [NN Layer name](<relative path to layer README>) › [Parent name](README.md)
> **Builds on:** [Topic](<rel path>), [Topic](<rel path>)
> **Enables:** [Topic](<rel path>), [Topic](<rel path>)

## Essence

One paragraph (3–6 sentences): what this is, the problem it solves or the question it answers, and the single idea that makes it work. A reader who reads only this paragraph should come away with the right mental model.

## Core tenets

1. **<Tenet stated as a claim.>** Two to four sentences of mechanism: why it is true, what follows from it.
2. ...
(5–9 tenets. These are the heart of the file: the load-bearing ideas without which the topic is misunderstood.)

## Key concepts

| Term | Meaning |
|---|---|
| ... | ... |

(5–12 terms that the tenets rely on. Precise one-line definitions.)

## How it fits

- **Below:** what this topic takes from the layers beneath, and which assumption it relies on.
- **Above:** what higher layers build with it.
- **Siblings:** how it contrasts with or complements the other leaves in the same parent.

## Common misconceptions

- **"<Misconception>"**: why it is wrong, in one or two sentences.
(2–4 items.)

## Go deeper

- Author, *Title* (year): one phrase on why it is the right next read.
(2–4 canonical sources.)
```

"Builds on" may only link to the same layer or lower layers (exception: layer 00 may build on 01). A related idea in a higher layer is mentioned in the body text with a link, never listed as a prerequisite. The checker reports violations as `UPWARD`. "Builds on" and "Enables" each list 1–5 links to other leaves or READMEs, *anywhere* in the tree (cross-layer links are the point). At least one of them should cross a layer boundary.

**For disease leaves (layers 12–14):** the tenets must trace the chain *mechanism → pathophysiology → the symptoms and signs it produces → what the tests show → what a treatment reverses and why*. Cite the pathology, physiology and pharmacology leaves rather than restating them. Include one tenet on *who else is involved*: which other specialties this condition pulls in and why (heart failure pulls in nephrology because the kidney is both victim and culprit; diabetes pulls in ophthalmology, nephrology, vascular surgery and primary care).

## Parent README template (directories below the top level)

```markdown
# <Name>

> **Layer:** [NN Layer name](<rel path>) › <this node>
> **Children:** [Child](child.md) · [Child](child.md) · ...

## What this area is about

The question this area answers and the one idea that unifies its children (1–2 paragraphs).

## How the children fit together

Explain the internal logic: the order to read them, which child depends on which, and how together they make up the parent. A table (Child | Its role in the whole | Depends on) followed by a short narrative works well. An ASCII diagram is welcome if it shows real structure.

## Connections to sibling areas

For each sibling directory under the same layer: one short paragraph or bullet on how this area and that sibling connect (shared mechanisms, patients or data flowing between them, tension between them). Link to the sibling's README.

## Connections across layers

What this area takes from lower layers and gives to higher ones, with links.

## Cross-cutting threads

Bullets linking to `CROSS-CUTTING.md` anchors (see list below) for the principles visible here, each with one phrase on how it shows up.
```

**For specialty parents (every parent directory in layers 12, 13 and 14)** add one more section, after "Connections to sibling areas":

```markdown
## Interfaces with other specialties

How this specialty shares patients, disputes territory and hands over care with the other branches of medicine, across layers 12–14: who refers to whom and why, which conditions sit on the border (and with which neighbour), which decisions are made jointly (the multidisciplinary team), and which emergencies cross the boundary. Link each named specialty's README.
```

The checker requires this heading in those READMEs.

## Layer README template (`NN-*/README.md`)

Same as the parent template, plus, before "How the children fit together":

```markdown
## Why this layer sits here

What it needs from the layers below (with links) and what the layers above need from it. State the one abstraction or idea this layer contributes to the stack.
```

and the "Connections to sibling areas" section becomes **"Connections to neighbouring layers"**: how this layer connects to each other top-level layer it touches meaningfully (not all 15; the 4–8 that matter), with links to their READMEs.

## Cross-cutting principle anchors

`CROSS-CUTTING.md` will be written last, with these anchors. Link to them as `<rel path>/CROSS-CUTTING.md#<anchor>`:

| Anchor | Principle |
|---|---|
| `structure-determines-function` | Shape, surface and arrangement decide what a molecule, cell, organ or body can do |
| `gradients-and-flow` | Everything moves down a gradient; life spends energy to make gradients (pumps, pressure, concentration) |
| `feedback-and-homeostasis` | Measure the output and adjust the input: set points, gain, delay, oscillation |
| `compensation-and-decompensation` | Reserve hides damage until it is exhausted; failure is compensation running out |
| `supply-and-demand` | Oxygen, substrate and perfusion must match consumption; mismatch is ischaemia, hypoxia, failure |
| `barriers-and-compartments` | Membranes, epithelia, the blood–brain barrier, body cavities: what is kept apart and what crosses |
| `signalling-and-information` | Genetic, neural, endocrine and immune signals: encoding, specificity, amplification, noise |
| `specificity-and-recognition` | Lock and key: enzymes, receptors, antibodies, drugs, and the cost of imperfect recognition |
| `redundancy-and-reserve` | Paired organs, collateral circulation, clotting cascades, immune overlap: why one failure is survivable |
| `trade-offs-and-evolutionary-legacy` | Every design is a compromise shaped by selection on past environments |
| `scale-and-surface-to-volume` | Why size dictates diffusion distances, metabolic rate, dosing and anatomy |
| `time-courses` | Acute versus chronic, latency, half-life, natural history: the same insult differs by its tempo |
| `dose-response` | The dose makes the poison, the drug and the exposure; thresholds, saturation and hormesis |
| `probability-and-uncertainty` | Variation, risk, Bayes: medicine reasons under uncertainty at every level |
| `cause-and-mechanism` | Necessary, sufficient and component causes; confounding; from association to mechanism |
| `the-host-and-its-environment` | Genes meet exposures, microbes, behaviour and society; disease is an interaction |
| `injury-and-repair` | Inflammation, regeneration, fibrosis: the body's one response to damage and its costs |
| `harm-and-benefit` | Every intervention has a cost; number needed to treat and to harm; first, do no harm |

## Your final report (to the coordinator)

When done, report: files written (count), any taxonomy suggestions, any link you were unsure about, and any claim or figure you were not fully sure of so the reviewer can check it. Do not paste the files.
