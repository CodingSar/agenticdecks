# Agentic Decks

> Also in this repository: **[Computer Science from First Principles](cs-first-principles/README.md)**, a layered knowledge base of Computer Science from engineering foundations up to AI and society (16 layers, 263 leaf topics, plus a cross-cutting principles index).
>
> And **[Medicine from First Principles](medicine-first-principles/README.md)**, the same method applied to Medicine: from the physics and chemistry of living matter, through biochemistry, cells, genetics, anatomy and physiology, microbes and immunity, pathology, pharmacology, evidence and the clinical method, to the branches of medicine and how they interact, and medicine in society (16 layers, 332 leaf topics, plus a cross-cutting principles index).

Anki decks for a cloud / Kubernetes platform and enterprise architect, consolidated from 44 source decks into 32, plus new decks written from scratch (The Pragmatic Programmer, the general-education series, Identity & Zero Trust, SRE & Observability, Software Engineering Classics, Chemistry, From Source to Silicon, Clean Code & Design Patterns).

- **Import:** `decks/*.apkg`
- **Editable source of truth:** `work/out/*.json` (one file per deck) + `media/`
- **Rebuild:** `pip install genanki && python3 tools/check.py && python3 tools/build.py`

## What changed

| | Before | After |
|---|---|---|
| Decks | 44 | 44 |
| Notes | 4,506 | 7,646 |
| Cards | 4,684 | 9,610 |
| Notes with an analogy | 126 | 1,625 |
| Answers > 60 words | many (avg. note 300–950 chars) | 0 (validator-enforced) |

There are more cards because long, multi-part cards were split into atomic ones (minimum information principle). Each card now takes seconds to review instead of a paragraph.
Duplicates, book/author/edition trivia, "chapter N covers…" cards and deck-meta cards were removed. Every deletion is listed with its reason in `work/out/<deck>.changelog.md`. Cross-deck duplicates are in `work/out/INTEGRATION.changelog.md`.

A **product-content review** (Oct 2026) removed or generalised cards that taught one vendor's product rather than a transferable concept (feature lists, SKUs, marketing claims, dated release news); open-source tools that are a deck's subject and cross-provider mapping cards stayed, and in the vendor-scoped exam decks (AZ-305, STACKIT) only marketing phrasing and dated news were removed. Each deck's changelog has a `## Product-content review` section.

**Abbreviations** (Oct 2026): every card is seen on its own, so an abbreviation is written out on first use *on each card* — `memory management unit (MMU)`, then `MMU`. Universally known ones (API, HTTP, CPU, SQL…) and product/ISA names (CUDA, RISC-V, LLVM) stay bare, and an expansion never appears on the front when it is the answer. 23 decks were rewritten this way; each changelog has an `## Abbreviations expanded` section listing the map.

The **general-education decks** (Art History, Philosophy, Music History, Architecture Styles, Physics, Chemistry) were written to `work/WRITER_BRIEF.md`: recognise-the-style, why-it-arose and what-it-reacted-against questions, contrast cards for look-alikes, 1–3 canonical anchors per movement, and hand-drawn SVG diagrams in `media/`. **Chemistry** (Oct 2026) runs from high-school foundations to master's-level ideas in 12 subdecks, each anchored in everyday and practical chemistry (kitchen, body, garage, lab, industry, environment); it was written by six parallel writer agents, one pair of subdecks each, then merged and deduplicated.

**Professional gap-fillers** (Oct 2026): **Identity & Zero Trust** (OAuth 2.0, OIDC, SAML, JWT, PKI, authorization models, NIST 800-207, SPIFFE, cloud IAM patterns), **SRE & Observability** (SLIs/SLOs, error budgets and burn-rate alerting, Prometheus model, tracing, OpenTelemetry, incident response, postmortems) and **Software Engineering Classics**, a composition deck of the enduring ideas in the canonical books and papers (Brooks, Parnas, Ousterhout, McConnell, Fowler, GoF, Feathers, SICP, Bentley, Raymond, Peopleware, Accelerate, Nygard, Humble & Farley, Beck, Kent, Norman, Google SWE, Dijkstra, Lampson, Saltzer et al.), organised by idea with the source work on each card. They were written to the same brief and deduplicated against the existing decks (`work/out/INTEGRATION.changelog.md`).

**From Source to Silicon** (Oct 2026) is a zero-to-hero deck on how a program becomes electrons: lexing and parsing, type systems, IR and optimisation, codegen, ABI and linking, interpreters, JITs and GC, x86-64 / ARM64 / RISC-V / IBM Z assembly, pipelines, out-of-order cores and microcode, caches and memory models, GPU SIMT, TPU systolic arrays and ML compilers, with a twelfth subdeck that explicitly maps one program through every layer. Six research-and-writer agents drafted two subdecks each from primary sources; a composer agent merged them, removed duplicates, added bridge and contrast cards across layers, normalised the `Link:` cross-references and deduplicated against Deep C, Cloud Architecture, Linux Internals, Go and LLMs (`work/out/From_Source_to_Silicon.changelog.md`). 21 hand-drawn SVG diagrams (`media/s2s_*.svg`).

**Clean Code & Design Patterns** (Oct 2026) covers Clean Code, SOLID and all 23 Gang of Four patterns, plus what came after: Fowler and Kerievsky (smell → refactoring → pattern), Effective Java, Game Programming Patterns, functional and type-driven design (parse, don't validate; railway-oriented programming; functional core, imperative shell) and anti-patterns. Every pattern is taught through concrete scenarios: which pattern for this situation, the smell that calls for it, its cost and when not to use it, and where it lives in real libraries. A dedicated *Choosing a Pattern* subdeck drills scenario → pattern across the whole catalogue with cross-category contrast cards. Four writer agents drafted three subdecks each; a composer merged and deduplicated them within the deck and against Software Engineering Classics, Pragmatic Programmer, Software Architecture & DDD and Software Testing (`work/out/Clean_Code_and_Design_Patterns.changelog.md`). 19 hand-drawn SVG diagrams (`media/ccdp*.svg`).

**Pipeline Security & SOC Monitoring** (Oct 2026) covers how CI/CD pipelines are attacked and defended (source and dependencies, workflow and build attacks, identity and secrets with OIDC federation, runners, registries and deploy gates) and how a Security Operations Center (SOC) monitors them: telemetry sources per stage, 29 concrete detection use-cases from branch-protection changes to images never pushed by the pipeline, triage and containment, and a maturity ladder. Supply-chain primitives (Sigstore, SLSA, SBOM) are referenced from Platform Engineering rather than repeated (`work/out/Pipeline_Security_and_SOC_Monitoring.changelog.md`). 2 hand-drawn SVG diagrams (`media/psoc_*.svg`).

**Merges** (same topic, different book or exam → one concept-organised deck):
Kubernetes in Action + Golden Kubestronaut → **Kubernetes** ·
platform_gitops + IaC + IDP + policy-as-code → **Platform Engineering** ·
Tanenbaum + Networking below CNI → **Networking** ·
AWS/Azure/GCP + Cloud AI Infrastructure → **Cloud Architecture** ·
DDIA + Distributed Systems → **Distributed Systems & Data** ·
Fundamentals of Software Architecture + DDD → **Software Architecture & DDD** ·
NORA + GEMMA → **NORA & GEMMA** ·
Architect Mental Models + Architect Skills → **Architect Craft** ·
Quantitative Foundations + Statistics/Bayes/ML/RL → **Quantitative Foundations** ·
Transformers + LLM/Agentic/Harness → **LLMs & Agentic Engineering**.

How it was done: `work/PLAN.md` (passes), `work/GUIDELINES.md` (card rules, based on Wozniak's *20 Rules of Formulating Knowledge* and Matuschak's *How to write good prompts*), `work/AGENT_BRIEF.md`.

## Note types and visuals

Every deck uses two shared note types with one stylesheet (light and dark mode):
- **Agentic Basic:** Front, Back, Image, Analogy (amber box), Extra/context (blue box), Source (pill label), Reverse (optional image→name card, used for ArchiMate notation and architecture-style diagrams).
- **Agentic Cloze:** Text, Image, Analogy, Extra, Source.

## Importing into Anki

The original note types were replaced, so importing over the old decks won't update them in place.
1. If your old decks have review history you want to keep, export a backup first (*File → Export → Collection*).
2. Delete the old decks you're replacing (*Browse → select deck → Delete*), then *Tools → Check Database*.
3. Import each file in `decks/` (*File → Import*).

Original note GUIDs are kept on every card that descends from an original note. Future imports of these files will update notes in place instead of creating duplicates.

## Decks

| File | Deck | Notes | Cards | Subdecks |
|---|---|---|---|---|
| `AZ-305_Solutions_Architect_Expert.apkg` | AZ-305 Solutions Architect Expert | 139 | 181 | 12 |
| `Adaptive_Systems.apkg` | Adaptive Systems | 58 | 60 | 6 |
| `Adoption_Epistemics_Governance.apkg` | Adoption, Epistemics & Governance | 91 | 103 | 7 |
| `ArchiMate_3.apkg` | ArchiMate 3 | 145 | 244 | 8 |
| `Architect_Craft.apkg` | Architect Craft | 161 | 185 | 11 |
| `Architecture_Styles.apkg` | Architecture Styles | 217 | 257 | 11 |
| `Art_History.apkg` | Art History | 202 | 210 | 12 |
| `BPMN_and_Business_Architecture.apkg` | BPMN & Business Architecture | 64 | 69 | 8 |
| `CISSP_Cloud_K8s.apkg` | CISSP (Cloud & Kubernetes Grounded) | 141 | 243 | 8 |
| `Chemistry.apkg` | Chemistry | 304 | 346 | 12 |
| `Clean_Code_and_Design_Patterns.apkg` | Clean Code & Design Patterns | 458 | 511 | 12 |
| `Cloud_Architecture.apkg` | Cloud Architecture | 113 | 178 | 10 |
| `Data_Engineering.apkg` | Data Engineering | 79 | 99 | 6 |
| `Deep_C_Kernel_Drivers_Embedded.apkg` | Deep C: Kernel, Drivers, Embedded | 350 | 430 | 8 |
| `Distributed_Systems_and_Data.apkg` | Distributed Systems & Data | 218 | 267 | 12 |
| `Economics_for_Architects.apkg` | Economics for Architects | 64 | 69 | 5 |
| `Foundations_Fitness_Sleep_Money.apkg` | Foundations: Fitness, Sleep & Money | 56 | 58 | 5 |
| `From_Source_to_Silicon.apkg` | From Source to Silicon | 318 | 424 | 12 |
| `Go_and_K8s_Operators.apkg` | Go & Kubernetes Operators | 176 | 181 | 10 |
| `Identity_and_Zero_Trust.apkg` | Identity & Zero Trust | 205 | 249 | 12 |
| `Kubernetes.apkg` | Kubernetes | 245 | 322 | 12 |
| `LLMs_and_Agentic_Engineering.apkg` | LLMs & Agentic Engineering | 126 | 163 | 9 |
| `Linux_Internals_for_K8s_Security.apkg` | Linux Internals for Kubernetes & Security | 179 | 200 | 12 |
| `Music_History.apkg` | Music History | 219 | 260 | 12 |
| `NORA_and_GEMMA.apkg` | NORA & GEMMA (Dutch Government Architecture) | 80 | 106 | 8 |
| `Networking.apkg` | Networking | 164 | 203 | 11 |
| `Novius_Bedrijfsarchitectuur.apkg` | Bedrijfsarchitectuur (Novius) | 88 | 137 | 11 |
| `Open_Agile_Architecture.apkg` | Open Agile Architecture | 211 | 340 | 10 |
| `Philosophy.apkg` | Philosophy | 219 | 265 | 12 |
| `Physics.apkg` | Physics | 219 | 260 | 12 |
| `Physics_for_Datacenters.apkg` | Physics for Datacenters | 58 | 63 | 6 |
| `Pipeline_Security_and_SOC_Monitoring.apkg` | Pipeline Security & SOC Monitoring | 163 | 173 | 12 |
| `Platform_Engineering.apkg` | Platform Engineering | 240 | 316 | 13 |
| `Pragmatic_Programmer.apkg` | The Pragmatic Programmer | 149 | 183 | 9 |
| `Quantitative_Foundations.apkg` | Quantitative Foundations | 349 | 402 | 11 |
| `Robotics_Arduino_to_Physical_AI.apkg` | Robotics: Arduino to Physical AI | 290 | 316 | 12 |
| `SAFe_for_Architects.apkg` | SAFe for Architects | 109 | 184 | 10 |
| `SRE_and_Observability.apkg` | SRE & Observability | 206 | 274 | 12 |
| `STACKIT_Hybrid_Cloud_Architect.apkg` | STACKIT Hybrid Cloud Architect | 157 | 215 | 6 |
| `Software_Architecture_and_DDD.apkg` | Software Architecture & DDD | 123 | 167 | 10 |
| `Software_Engineering_Classics.apkg` | Software Engineering Classics | 211 | 296 | 12 |
| `Software_Testing.apkg` | Software Testing | 120 | 188 | 8 |
| `Spanish_Intermediate_Advanced.apkg` | Spanish (Intermediate/Advanced) | 202 | 202 | 11 |
| `TOGAF_10.apkg` | TOGAF 10 | 80 | 129 | 7 |
| `Team_Topologies.apkg` | Team Topologies | 43 | 55 | 6 |
