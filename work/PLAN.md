# Deck consolidation plan

Starting point: 44 decks, 4,506 notes. Pipeline:
`*.apkg` → `tools/normalize.py` → `work/source/*.json` → (review passes) → `work/out/*.json` → `tools/check.py` → `tools/build.py` → `decks/*.apkg`

## Pass 1: map the areas (done before the per-cluster work)

| Area | Source decks (notes) | Decision |
|---|---|---|
| Kubernetes | Kubernetes_in_Action (64), Golden_Kubestronaut (225) | **merge** → `Kubernetes` |
| Platform engineering | platform_gitops (116), iac_control_plane_abstraction (30), idp_platform_engineering (39), policy_as_code_supply_chain_security (39) | **merge** → `Platform Engineering` |
| Vendor platform | STACKIT_Hybrid_Cloud_Architect (90) | keep; dedupe against Kubernetes/Platform |
| Systems programming | Go_Intricacies_and_K8s_Operators (204), deep_c_kernel_drivers_embedded (147) | keep both; drop operator cards that duplicate Platform Engineering |
| OS & security | Linux_OS_Internals_for_K8s_Security (193), cissp_cloud_k8s_grounded (82) | keep both; dedupe |
| Networking | Networking_Fundamentals_Tanenbaum (166), networking-below-cni (69) | **merge** → `Networking` (subdecks: Fundamentals / Below CNI) |
| Datacenter physics | physics_for_datacenters (57) | keep |
| Cloud | cloud_aws_azure_gcp (54), Cloud_AI_Infrastructure (86) | **merge** → `Cloud Architecture` |
| Azure exam | AZ-305_Solutions_Architect_Expert (150) | keep (exam-scoped); dedupe against Cloud |
| Distributed data | Designing_Data-Intensive_Applications (65), distributed_systems_aws_azure_k8s (98) | **merge** → `Distributed Systems & Data` |
| Data engineering | data-engineering-basics (59) | keep |
| EA frameworks | TOGAF_10 (86), ArchiMate3 (160), Agile_Architecture (273) | keep; dedupe across them |
| EA (NL/process/scaled) | NORA (42), GEMMA (53) → **merge** → `NORA & GEMMA`; SAFe ARCH (117), BPMN (61), Novius (119, Dutch) | keep the rest |
| Software architecture | Fundamentals_of_Software_Architecture (64), Domain-Driven_Design (52) | **merge** → `Software Architecture & DDD` |
| Org design / testing | team_topologies_2e (45), software_testing (138) | keep |
| Architect craft | architect-mental-models (118), architect_skills_k8s (55) | **merge** → `Architect Craft` |
| Thinking & economics | adoption_epistemics_governance (127), adaptive_systems_deck (64), Economics_for_Architects (72) | keep; dedupe against Architect Craft |
| Quantitative | quantitative_foundations (99), statistics-bayes-ml-rl-geometric (176) | **merge** → `Quantitative Foundations` (stats/probability deduped) |
| LLMs | transformers_llm_working_understanding (46), LLM_Agentic_Harness_Engineering_2026 (55) | **merge** → `LLMs & Agentic Engineering` |
| Personal | robotics (200), spanish (202), Foundations_Fitness_Sleep_Money (49) | keep |

The merges are where the topic is the same and only the source (book or exam) differs.
Learning is organised by concept, not by book, so a merged deck gets concept subdecks.

## Passes 2–5 (run per cluster by parallel subagents, each over its own group of decks)

2. **Combine / split:** remove duplicates within and across decks, merge overlapping cards, and split cards
   that ask more than one thing or whose answers go over the length limit (see `GUIDELINES.md`).
3. **Best practices:** rewrite for atomicity, precision and short answers; turn enumerations into clozes;
   add contrast cards for look-alikes; tidy the HTML.
4. **Analogies:** add accurate 1–2 sentence analogies where an abstract idea needs a concrete hook.
5. **Signal filter:** delete meta and trivia cards (author, year, edition, "chapter N covers…", deck-meta)
   and anything with no impact on the job or the exam.

Each cluster writes `work/out/<deck>.json` plus `work/out/<deck>.changelog.md`, which records merges,
deletions with reasons, and the number of cards split.

## Pass 6: integration (main session)
Run the validator across all decks, check for cross-cluster duplicates (`tools/similar.py`) and build the `.apkg` files into `decks/`.
