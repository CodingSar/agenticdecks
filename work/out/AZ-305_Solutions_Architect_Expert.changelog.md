# AZ-305 Solutions Architect Expert — changelog

**Source:** `AZ-305_Solutions_Architect_Expert` (150) → **139 notes out**.
12 subdecks following the AZ-305 skill areas: Monitoring & Logging · Identity & Access · Governance (identity/governance/monitoring) · Relational Data · Non-relational Data & Storage · Data Integration & Analytics (data storage) · Backup & DR · High Availability (business continuity) · Compute · Application Architecture · Migration · Networking (infrastructure). Skill area recorded in `source`; original `AZ305::…` tags kept.

## Rewrites
- Nearly every answer trimmed to the minimum (many were 60–110 words). Expanded acronyms in prompts dropped where the acronym is the working vocabulary.
- Enumerations → per-item clozes: diagnostic-setting destinations, Policy effects, WAF pillars, SQL deployment options, vCore tiers, storage services, Blob tiers (with 30/90/180-day minimums), Cosmos consistency levels, VM series, Functions plans, messaging services, Azure load balancers, CAF phases, migration Rs.
- Exam-meta removed from answers (e.g. "AZ-305 questions test…" moved to extra). Current-state fixes: MMA retired (AMA), Blueprints → Template Specs + Deployment Stacks, DMA noted as being superseded by Azure Migrate/Arc assessments, Flex Consumption plan added.

## Merges (10 notes folded in)
- PIM activation cloze → PIM card. Allowed-SKU deny policy → RBAC vs Policy. Session-default cloze → Cosmos consistency cloze.
- RA-GRS/RA-GZRS HA card → GRS vs RA-GRS. Duplicate Site Recovery RPO cloze → Site Recovery RPO card.
- Spot VM card → "reservations vs Spot" decision card (cross-cloud spot details live in Cloud Architecture).
- Event Grid vs Service Bus → messaging-services cloze. Queue-for-consumer-outage → queue-based load leveling card.
- ExpressRoute connectivity-provider cloze → VPN vs ExpressRoute. VNet peering explanation → non-transitive peering cloze.

## Splits: 2
- Hybrid identity (PHS / PTA / federation) → three decision cards.

## Deletions (3)
- Generic "four factors for VM vs containers vs serverless": enumeration, covered by Cloud Architecture managed-vs-self-run and the AKS/Container Apps/Functions cards.
- GitHub Actions vs Azure DevOps: low signal (org preference).
- Generic IaC recommendation: IaC is owned by Platform Engineering; Bicep is in the Cloud Architecture mapping.

## De-duplication against Cloud Architecture
- Cross-provider items (Spot eviction, commitment discounts, region/AZ concepts, generic service mappings) live in Cloud Architecture. Azure-specific detail stays here: Azure hierarchy scope *purposes*, LRS/ZRS/GRS/GZRS, Cosmos consistency levels, Azure LB family, Private Endpoint + Private DNS.

## Analogies: 25 cards (~18%)
Examples: phone tree (action group), bouncer (Conditional Access), building code vs keys (Policy vs RBAC), shared printer (elastic pool), photo album vs second house (Backup vs Site Recovery), photocopies (redundancy ≠ backup), order rail (queue load leveling), airline hub (hub-spoke), friend of a friend (non-transitive peering), phone directory vs receptionist (Traffic Manager vs Front Door).

## Product-content review

Reviewed card by card for vendor-catered content: 0 deleted, 1 rewritten to the underlying concept, 1 scrubbed of marketing/dated phrasing.

### Rewritten (1)
- "What is Cosmos DB's key differentiator vs a relational database for global apps?" → "When do you recommend Cosmos DB over a relational database?"

### Scrubbed (1)
- "Azure Blueprints is retiring. What replaces it?": removed dated retirement-timeline extra (phase-out dates)
