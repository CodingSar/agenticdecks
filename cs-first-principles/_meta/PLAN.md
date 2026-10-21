# Plan: a first-principles taxonomy of Computer Science

## 1. Goal

Build a knowledge base that explains Computer Science (CS) from the ground up: physical engineering at the bottom, each layer resting on the ones beneath it. Every **leaf** holds the few tenets you must understand to grasp the essence of that topic. Every **parent** explains how its children fit together and how it connects to its siblings. The tree should be deep enough to be useful as a map of the whole field, but each file should stay short enough to read in one sitting.

## 2. What "first principles" means here

1. **Dependency order.** A topic appears above everything it needs. When you read bottom-up, nothing relies on an idea you have not yet met.
2. **Essence over coverage.** A leaf says what is *true and load-bearing*, not everything that is known. The test: if you forgot this, would you misunderstand the topic?
3. **Mechanism over vocabulary.** Every tenet says *why* something works or *what forces* shaped it, not only what it is called.
4. **Explicit edges.** A tree can only show one parent per node, but CS is a graph. Every file states what it **builds on** and what it **enables**, and a separate cross-cutting index ([`../CROSS-CUTTING.md`](../CROSS-CUTTING.md)) follows ideas such as caching or abstraction through every layer they appear in.

## 3. Top-level structures considered

Choosing the top level decides which relationships the tree shows for free and which it must spell out by hand. Six candidates were compared.

### A. Pure abstraction stack (physics → transistors → gates → architecture → OS → languages → applications)

*The classic "From NAND to Tetris" or Patt & Patel ordering.*

- **Strengths:** It matches the request exactly (engineering at the bottom). Each layer is a real interface that hides the one below: the Instruction Set Architecture (ISA) hides the microarchitecture, the system-call interface hides the hardware, and so on. Reading it bottom-up is a story.
- **Weaknesses:** Theory has no place. Computability, complexity, algorithms, information theory and logic are not *implemented on* the OS, and they do not depend on transistors. Forcing them into a layer gives false dependencies (for example "algorithms sit on top of the OS"). AI, security and software engineering cut across many layers rather than sitting on one.

### B. Flat body-of-knowledge list (ACM/IEEE CS2023 knowledge areas, ACM Computing Classification System)

- **Strengths:** It is authoritative and complete, and it maps to university curricula. It avoids arguing about order.
- **Weaknesses:** It has no "on top of" relation, which is the main point of this project. Seventeen sibling areas say nothing about why networking needs operating systems or why databases need algorithms. It is good as a **coverage checklist**, and is used that way in §6.

### C. Two converging pillars (a physical pillar and a formal pillar meeting at "the program")

- *Physical pillar:* physics → devices → logic → architecture → OS.
- *Formal pillar:* logic and math → automata → computability → complexity → algorithms.
- They meet at programs and languages, and everything above (data, networks, distributed systems, AI) uses both.
- **Strengths:** This is the most honest picture. CS really does have two roots: Turing's machine is a mathematical object and the transistor is a physical one. The Church–Turing thesis and the stored-program computer are where the two meet.
- **Weaknesses:** A file tree cannot branch below its root. A two-pillar diagram is easy to draw but turns into a confusing directory layout.

### D. Question-driven (What can be computed? How fast? How do we build it? How do we organise complexity? How do machines cooperate? How do machines learn?)

- **Strengths:** It motivates every area by a question, and it is good for teaching.
- **Weaknesses:** The edges between questions are fuzzy, and the same topic answers several questions (caching is about "how fast" and "how to build"). Dependencies are hidden rather than shown.

### E. Great Principles (Denning: computation, communication, coordination, recollection, evaluation, design, automation)

- **Strengths:** Principles last longer than technologies. It shows that the same idea recurs across areas.
- **Weaknesses:** It is orthogonal to areas. A reader looking for "operating systems" will not find it. It is the right shape for an **index**, not for the tree.

### F. Historical (mechanical calculators → stored-program computers → compilers → time-sharing → networks → web → ML)

- **Strengths:** It shows why ideas arose and what problem each solved.
- **Weaknesses:** History is not dependency. Neural networks (1940s) came before relational databases (1970) but build on far more mathematics.

## 4. Decision: a topologically sorted layer stack with two roots, plus a cross-cutting index

The chosen structure is **A's layered stack, re-ordered by C's two-root dependency graph, with E as an orthogonal index and B as a coverage check.**

- **Top level = numbered layers 00–15.** The numbers are a *topological order* of the dependency graph: every layer depends only on lower numbers, never higher ones. This keeps the bottom-up reading guarantee without inventing false dependencies.
- **Two roots at the bottom.** `00` Engineering Foundations is the physical root, as requested. `01` Mathematical Foundations is the formal root. It does not depend on `00`; it sits at `01` because it is the *language* in which everything from `02` up is described. The README for each says this plainly.
- **The two pillars meet early.** `02` Theory of Computation is pure formal pillar, and `03` Digital Logic is where the pillars meet (Boolean algebra from `01` built out of transistors from `00`). From `04` upward every layer uses both.
- **Algorithms sit above architecture (05 above 04)** because the algorithm-analysis machine, the Random Access Machine (RAM) model, is an idealised computer. Its costs (unit-time memory access, word-sized arithmetic) are abstractions of real hardware, and modern algorithm engineering (cache-aware and external-memory algorithms) only makes sense once you know the memory hierarchy.
- **Cross-cutting principles** (abstraction, caching, indirection, pipelining, redundancy, the end-to-end argument, and others) get their own index, `CROSS-CUTTING.md`. It links each principle to every leaf where it appears. This repairs the main weakness of any tree.

### Why this order and not another (key placement decisions)

| Decision | Alternative rejected | Reason |
|---|---|---|
| Theory of Computation (02) below Digital Logic (03) | Theory near the top as "advanced" | Automata and computability need only logic and sets. Putting them low says that what a machine *can* compute is settled before you build one. |
| Information theory inside 02 | Inside Networking | Shannon's entropy and channel capacity limit compression, storage and coding at every layer, not just networks. |
| Number representation inside 03 | Inside 01 Math | Two's complement and IEEE 754 are *engineering encodings* of mathematical numbers. Their quirks (overflow, rounding) come from finite hardware. |
| Boolean algebra inside 01 | Inside 03 | It is pure mathematics (a lattice and an algebra). 03 is about *realising* it in hardware. |
| Compilers inside 06 Programming Languages | Separate layer | A compiler is how a language's semantics becomes machine behaviour. It is the bridge from 06 down to 04. |
| Operating Systems (07) above Languages (06) | OS directly above architecture | Real OSs are written in a language and compiled. Runtime systems (06) and OS kernels (07) depend on each other, but the OS uses everything in 06 and adds protection, sharing and persistence. |
| Data Management (09) above Networking (08) | Below networking | Single-node databases do not need networks, but modern data systems assume client/server and replication. Both rest on 07. 09 is placed after 08 so that replication can be mentioned without a forward reference. |
| Distributed Systems (10) above Data (09) | Inside Networking | Distributed systems are about *agreement under partial failure*. That needs networks (08) and the transaction concepts of 09. |
| Security (11) high in the stack | Low, as a foundation | Security is a property of whole systems. Its attacks exploit every layer (side channels in 04, memory corruption in 06, protocol flaws in 08), so it must come after them. Cryptography's mathematics is in 01 and 02. |
| Software Engineering (12) above Security | Near Languages | It is about building large systems *with people* over time. It uses every technical layer, including security practice. |
| AI and Machine Learning (13) near the top | Near Algorithms | Modern ML relies on linear algebra and probability (01), optimisation (01, 05), parallel hardware (04, 10), data systems (09) and engineering practice (12). |
| Human & Visual Computing (14) and Computing in Context (15) at the top | Leave out | HCI and graphics are where computation meets human perception. Ethics, law and history are where it meets society. Both sit on top of everything else. |

## 5. File conventions

- **Directories** are parent nodes. Each has a `README.md` (the parent explanation).
- **Leaves** are `.md` files inside a parent directory. Each holds one topic's essential tenets.
- **Numeric prefixes** (`00-`, `01-`…) give reading order at every level.
- **Links** are relative so the tree works on GitHub and in any Markdown viewer.
- **Abbreviations:** each file spells an abbreviation out on first use, for example "Translation Lookaside Buffer (TLB)", and uses the short form after that. Every file may be the first one a reader opens.
- Templates and style rules: [`WRITER_BRIEF.md`](WRITER_BRIEF.md). The full path list is in [`TAXONOMY.md`](TAXONOMY.md).

## 6. Coverage check against CS2023 knowledge areas

| CS2023 knowledge area | Where it lives |
|---|---|
| Algorithmic Foundations (AL) | 02, 05 |
| Architecture and Organization (AR) | 03, 04 |
| Artificial Intelligence (AI) | 13 |
| Data Management (DM) | 09 |
| Foundations of Programming Languages (FPL) | 06 |
| Graphics and Interactive Techniques (GIT) | 14 |
| Human-Computer Interaction (HCI) | 14 |
| Mathematical and Statistical Foundations (MSF) | 01 |
| Networking and Communication (NC) | 08 |
| Operating Systems (OS) | 07 |
| Parallel and Distributed Computing (PDC) | 04 (hardware), 10 |
| Security (SEC) | 11 |
| Society, Ethics, and the Profession (SEP) | 15 |
| Software Development Fundamentals (SDF) | 05, 06, 12 |
| Software Engineering (SE) | 12 |
| Specialized Platform Development (SPD) | 14 (partly), outside the core scope |
| Systems Fundamentals (SF) | 04, 07, 08, cross-cutting index |

Engineering foundations (00) are beyond CS2023, which assumes them. They are here because the request starts there.

## 7. Process

1. **Plan** (this file) and fix the full path list (`TAXONOMY.md`) so that cross-links can be written before the target files exist.
2. **Draft in parallel.** One writer agent per one or two layers, all working to `WRITER_BRIEF.md`.
3. **Verify mechanically.** A link checker (`_meta/check.py`) finds broken relative links, missing READMEs, empty files and leaves without the required sections.
4. **Review.** A separate pass reads each layer for factual errors, missing load-bearing tenets, and weak sibling connections, and fixes them.
5. **Cross-cutting index.** Build `CROSS-CUTTING.md` from the finished leaves.
6. **Iterate.** Repeat steps 3 and 4 until the checker is clean and the review finds nothing load-bearing.

## 8. Lessons from the first draft

- **00 and 01 are twin roots, not a strict order.** The engineering writers needed calculus, linear algebra and probability to state Ohm's and Kirchhoff's laws, RC timing, band theory and reliability. Mathematics does not need engineering, but engineering is *written in* mathematics. The checker allows 00 → 01 "builds on" links as the only upward exception. Engineering stays at 00 because the stack is ordered by *what the machine is made of*, and 01 is the notation used to describe it.
- **"Builds on" must point down; everything else goes in the body.** A mechanical check (`UPWARD`) found that writers sometimes listed a higher layer as a prerequisite when they meant "related to" (for example scheduling → networking's queueing theory, which really belongs to probability in 01). Real forward dependencies, such as Byzantine fault tolerance (10) using digital signatures (11), are mentioned in the text with a link, not listed as prerequisites.
- **Gaps found by writers became new leaves.** Writers reported thirteen load-bearing topics with no home. All were added in pass 2: Fourier analysis, Markov chains, Kolmogorov complexity, memory cells, union–find, inter-process communication, data-centre networks and Software-Defined Networking (SDN), recurrent networks, retrieval and embeddings, information visualisation, privacy-enhancing technologies, software supply-chain security, and environmental impact.

## 9. What was done

| Pass | Work | Result |
|---|---|---|
| 1. Draft | 11 writer agents, one or two layers each, to `WRITER_BRIEF.md` | 340 files: 262 leaves, 78 parent READMEs |
| 2. Review | 10 reviewer agents to `REVIEW_BRIEF.md`: fact-check every number, date and citation; fix upward links; write the 13 new leaves; strengthen sibling connections | About 80 factual corrections (listed in each reviewer's report and summarised in `REVIEW_NOTES.md`); 13 new leaves |
| 3. Index | `CROSS-CUTTING.md`: 18 principles traced bottom-up through 173 links | Every anchor resolves |
| 4. Coherence | Audit of the 16 layer READMEs as one bottom-up story | Neighbouring layers agree on what each gives and takes |

`python3 _meta/check.py` reports 0 problems: every taxonomy path exists, every link and anchor resolves, every leaf has the required sections, and no "Builds on" link points upward.

## 10. Known limits and next iterations

- Fast-moving figures (AI compute and energy, hardware specifications, data-centre electricity) are dated in the text and will need refreshing.
- Leaves are capped at about 1,100 words, so each one is an essence, not a textbook chapter. The "Go deeper" sources are the next step.
- Candidate leaves not yet added: simultaneous multithreading and the roofline model (now tenets inside existing leaves), trusted execution environments, hash indexes and analytical warehouses, audio and speech, Augmented and Virtual Reality (AR/VR), Gödel's incompleteness theorems (currently derived inside the halting-problem leaf).
