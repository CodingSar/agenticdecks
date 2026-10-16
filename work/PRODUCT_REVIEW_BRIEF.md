# Brief for product-content review agents

Goal: the decks in `work/out/*.json` should teach transferable knowledge, not a vendor's product. Go through YOUR decks
card by card and remove or neutralise content that is catered to a particular product.

## What counts as "product-catered" (remove or generalise)
- A card whose only content is a **vendor product's feature list, naming, SKUs/tiers, plugin taxonomy, console/UI
  steps, pricing, roadmap, or marketing claim** ("X is the leading…", "X enables teams to…").
- Cards about **one commercial vendor's packaging** of a generic thing (e.g. Red Hat ACS/RHDH/OpenShift/Lightspeed
  specifics, HashiCorp commercial tiers, Datadog/GitHub/GitLab product features, Jetson/Arduino SKU spec sheets,
  "model X vs model Y" of a vendor's lineup) when the generic concept is what matters.
- **Dated news/version items** ("as of 2026 vendor X added…", "model X released…") with no lasting lesson.

## What is NOT product-catered (keep)
- A concept card that uses a product as a short **example** (`extra`), or a cross-provider mapping cloze
  (AWS/Azure/GCP names for the same concept) — that is the learner's job vocabulary.
- **Open-source tooling that is the subject of the deck** (Kubernetes, Argo CD, Flux, Terraform/OpenTofu, Helm,
  Crossplane, Cilium, Kyverno, Backstage, Kafka, Prometheus, ROS 2…). "How does Argo CD sync?" is fine. A card that
  only recites a tool's menu or marketing is not.
- **Exam/vendor-scoped decks** (`AZ-305_Solutions_Architect_Expert`, `STACKIT_Hybrid_Cloud_Architect`): the product
  IS the scope. There, remove only marketing phrasing, promotional claims, and dated news; keep decision-relevant
  product knowledge.

## How
- For a product-catered card: if a vendor-neutral concept is underneath, **rewrite** it to the concept (keep the guid,
  move the product to a short example in `extra`). If nothing transferable remains, **delete** it.
- Also scrub marketing phrasing inside otherwise-good cards ("enterprise-grade", "seamless", "best-in-class"…).
- Keep every other card exactly as it is. Don't restructure decks. Don't add cards.
- Edit the JSON in place with a Python script in your scratchpad folder (load → modify by guid/front → dump with
  `indent=1, ensure_ascii=False`). Then run `python3 tools/check.py <your files>` → 0 errors.
- Append a section `## Product-content review` to each deck's existing `work/out/<deck>.changelog.md` listing every
  deleted card (front, reason) and every rewritten card (old front → new front). If nothing changed, append one line
  saying so.
- Don't run build.py, don't touch other files, don't commit. Final reply: per deck, # deleted, # rewritten, # scrubbed.
