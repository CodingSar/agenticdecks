# Physics for Datacenters changelog

Source: `physics_for_datacenters` (57 notes in, prefix P) → **58 notes out**.

Subdecks: 01 Energy & Power · 02 Laws of Thermodynamics · 03 Heat Transfer & Cooling · 04 Entropy & Information · 05 Chip Power & Scaling · 06 Facility Scaling & Metrics.

## Summary
- Deleted: 0. The deck was already high-signal; author and year attributions moved from prompts into `source`, e.g. "Susskind's definition…" became a neutral prompt.
- Merges: 2
  - P43 + P55 (fan affinity laws + "fan power if you double airflow") → one affinity-law card (8×)
  - P48 + P56 (speed of light constraint + 5 ns per metre) → one latency card
- Splits: 3
  - P17 inlet temperature → COP gain / free-cooling hours
  - P37 Dennard breakdown → why it broke / what it caused
  - P46 PUE → definition and values / blind spot
- Number cards (kT, Landauer limit, heat-capacity ratio, kWh, Carnot formulas, CMOS power) turned into clozes; the concept cards were kept separate (concept vs number angle).
- Intuition fields: the source had a long intuition on every card. Kept 20 as 1–2 sentence analogies (~34%). Where the content was really an example or a consequence, it moved to `extra` with a `<b>Label:</b>` prefix. No new analogies.
- Long answers trimmed (e.g. P44 liquid-cooling synthesis, P31 Landauer gap, P37).

## Cross-cluster notes (left alone)
- Amdahl's law (P49) is also in Quantitative Foundations; it's kept here framed through the end of Dennard scaling.
- PUE (P46) is also in Cloud_AI_Infrastructure (Cloud Architecture cluster).
- The speed-of-light latency card overlaps slightly with the Networking bandwidth/latency card (different angle).

## Product-content review

Reviewed all cards for product-catered content (vendor feature lists, tool plugs, certification marketing, dated news, promotional phrasing): nothing applied, no changes made.
