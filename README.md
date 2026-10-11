# Agentic Decks

Anki decks for a cloud / Kubernetes platform and enterprise architect, consolidated from 44 source decks into 32.

- **Import:** `decks/*.apkg`
- **Editable source of truth:** `work/out/*.json` (one file per deck) + `media/`
- **Rebuild:** `pip install genanki && python3 tools/check.py && python3 tools/build.py`

## What changed

| | Before | After |
|---|---|---|
| Decks | 44 | 32 |
| Notes | 4,506 | 4,728 |
| Cards | 4,684 | 6,089 |
| Notes with an analogy | 126 | 800 |
| Answers > 60 words | many (avg. note 300–950 chars) | 0 (validator-enforced) |

There are more cards because long, multi-part cards were split into atomic ones (minimum information principle). Each card now takes seconds to review instead of a paragraph.
Duplicates, book/author/edition trivia, "chapter N covers…" cards and deck-meta cards were removed. Every deletion is listed with its reason in `work/out/<deck>.changelog.md`. Cross-deck duplicates are in `work/out/INTEGRATION.changelog.md`.

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
| `BPMN_and_Business_Architecture.apkg` | BPMN & Business Architecture | 64 | 69 | 8 |
| `CISSP_Cloud_K8s.apkg` | CISSP (Cloud & Kubernetes Grounded) | 141 | 243 | 8 |
| `Cloud_Architecture.apkg` | Cloud Architecture | 114 | 181 | 10 |
| `Data_Engineering.apkg` | Data Engineering | 82 | 103 | 6 |
| `Deep_C_Kernel_Drivers_Embedded.apkg` | Deep C: Kernel, Drivers, Embedded | 350 | 430 | 8 |
| `Distributed_Systems_and_Data.apkg` | Distributed Systems & Data | 218 | 267 | 12 |
| `Economics_for_Architects.apkg` | Economics for Architects | 64 | 69 | 5 |
| `Foundations_Fitness_Sleep_Money.apkg` | Foundations: Fitness, Sleep & Money | 56 | 58 | 5 |
| `Go_and_K8s_Operators.apkg` | Go & Kubernetes Operators | 176 | 181 | 10 |
| `Kubernetes.apkg` | Kubernetes | 245 | 322 | 12 |
| `LLMs_and_Agentic_Engineering.apkg` | LLMs & Agentic Engineering | 126 | 163 | 9 |
| `Linux_Internals_for_K8s_Security.apkg` | Linux Internals for Kubernetes & Security | 179 | 200 | 12 |
| `NORA_and_GEMMA.apkg` | NORA & GEMMA (Dutch Government Architecture) | 80 | 106 | 8 |
| `Networking.apkg` | Networking | 164 | 203 | 11 |
| `Novius_Bedrijfsarchitectuur.apkg` | Bedrijfsarchitectuur (Novius) | 88 | 137 | 11 |
| `Open_Agile_Architecture.apkg` | Open Agile Architecture | 211 | 340 | 10 |
| `Physics_for_Datacenters.apkg` | Physics for Datacenters | 58 | 63 | 6 |
| `Platform_Engineering.apkg` | Platform Engineering | 241 | 317 | 13 |
| `Quantitative_Foundations.apkg` | Quantitative Foundations | 349 | 402 | 11 |
| `Robotics_Arduino_to_Physical_AI.apkg` | Robotics: Arduino to Physical AI | 293 | 321 | 12 |
| `SAFe_for_Architects.apkg` | SAFe for Architects | 109 | 184 | 10 |
| `STACKIT_Hybrid_Cloud_Architect.apkg` | STACKIT Hybrid Cloud Architect | 158 | 216 | 6 |
| `Software_Architecture_and_DDD.apkg` | Software Architecture & DDD | 123 | 167 | 10 |
| `Software_Testing.apkg` | Software Testing | 120 | 188 | 8 |
| `Spanish_Intermediate_Advanced.apkg` | Spanish (Intermediate/Advanced) | 202 | 202 | 11 |
| `TOGAF_10.apkg` | TOGAF 10 | 80 | 129 | 7 |
| `Team_Topologies.apkg` | Team Topologies | 43 | 55 | 6 |
