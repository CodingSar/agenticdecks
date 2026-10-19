# Software Architecture & DDD: changelog

**In:** 116 notes (Fundamentals_of_Software_Architecture 64 + Domain-Driven_Design 52) → **Out:** 123 notes in 10 concept subdecks.

Subdecks: 01 Architectural Thinking · 02 Architecture Characteristics · 03 Modularity & Coupling · 04 Architecture Styles · 05 Decisions, Risk & Communication · 06 DDD Model & Language · 07 DDD Tactical Building Blocks · 08 DDD Supple Design · 09 DDD Bounded Contexts & Context Maps · 10 DDD Distillation & Large-Scale Structure.

## Merges
- FoSA "no right or wrong answers, only expensive ones" → First Law card (moved to extra).
- FoSA "Conway's Law and Inverse Conway Maneuver" and "team boundaries (Team Topologies idea)" → merged into the **Team Topologies** deck's Conway / Reverse Conway cards (same cluster), so they are not duplicated here.
- FoSA "Bounded context, and why microservices embrace it": the definition now lives only in the DDD Bounded Context card; the FoSA card was refocused on "why one service per bounded context".
- FoSA style "strengths and weaknesses" cards became focused "when to choose" / "main weakness" cards.

## Deletions
- FoSA "8 core expectations of an architect": an 8-item generic list with low recall value.
- FoSA "How does the book compare styles (star system)": book meta; the actual tradeoffs are in the per-style cards.
- FoSA #60, #61, #62: merged (see above).

## Splits: 9
Instability vs distance-from-main-sequence formulas; why dynamic connascence is worse; layered (when to use / weaknesses); space-based (mechanism / when to use); ADR (purpose / sections cloze); Ubiquitous Language (definition / awkward-term signal); Open Host Service / Published Language; Core Domain / Distillation; Segregated Core / Abstract Core.

## New contrast cards: 3
Service-based vs microservices; upstream vs downstream; Conformist vs Anticorruption Layer.

## Other changes
- The 7 "which style is shown?" image cards now use `image` + `reverse: true` (diagram → name the style), and every style diagram is kept.
- Enumerations (four dimensions, characteristic criteria/categories, connascence types, 8 fallacies, filter types, C4) became clozes.
- Formulas use MathJax.
- **Analogies added: 25** (sources had none).

## Product-content review

Reviewed all cards for product-catered content (vendor feature lists, tool plugs, certification marketing, dated news, promotional phrasing): nothing applied, no changes made.

## Abbreviations expanded

Notes touched: 10

- SOA → service-oriented architecture
- ESB → enterprise service bus
- ADR → Architecture Decision Record
- ACID → atomicity, consistency, isolation and durability
- ACL → anticorruption layer
- CQS → command-query separation
- XP → extreme programming
