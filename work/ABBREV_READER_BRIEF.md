# Brief: abbreviation reader (read-only)

The learner (a cloud/enterprise architect) does not yet know the abbreviations in these decks. Every Anki card is seen
on its own, in random order, so an abbreviation must be written out **on each card where it appears**: "full name (ABBR)".

Your job: read ONE deck file `work/out/<Deck>.json` and report how bad the abbreviation problem is. Do not edit anything.

Count as an abbreviation: acronyms/initialisms and short technical codes (MMU, TLB, ISA, SRAM, DDR5, OIDC, SAML, SLO, CRI,
PCIe, NUMA, QoS, ...). Do NOT count the universally known set for this learner: API, URL, HTTP/HTTPS, DNS, TCP, IP, CPU,
GPU, RAM, SSD, OS, VM, AWS, GCP, SQL, JSON, YAML, CLI, UI, ID, PDF, USB, AI, ML, LLM, CI/CD, IT, REST, SaaS/PaaS/IaaS, K8s,
RBAC, TLS, SSH, PR, OSS, 2D/3D, units (GB, MHz, ms...), element symbols and chemical formulas, Roman numerals, model/product
names. Also don't count an abbreviation whose expansion *is the card's answer* ("What does TLB stand for?").

A note is "unexpanded" for ABBR if ABBR appears in its front/text/back/extra and the note nowhere contains the written-out
name (in any phrasing) next to it. Scan every note.

Write your result to the scratchpad path you were given as JSON:
{"deck": "<Deck>", "notes": <total>, "notes_with_unexpanded": <n>,
 "abbreviations": {"MMU": {"expansion": "memory management unit", "unexpanded_notes": 7}, ...},
 "verdict": "big" | "minor" | "none"}
Verdict: "big" if ≥ 15% of notes have at least one unexpanded abbreviation, "minor" if 1–15%, "none" if 0.
Keep `expansion` to the standard written-out form (lowercase unless a proper noun). Reply with the verdict line and the
top 10 abbreviations only. Use a short Python script to help you scan if useful; be fast.
