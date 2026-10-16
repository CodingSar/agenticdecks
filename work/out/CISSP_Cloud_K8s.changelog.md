# Changelog: CISSP (Cloud & Kubernetes Grounded)

Source: `cissp_cloud_k8s_grounded.json` (82 notes, avg about 650 chars plus a long Grounding block) → **145 notes**
(95 basic, 50 cloze), organised into the 8 CISSP domains (01 Security & Risk Management … 08 Software Development Security).

## Splits and new cards (62 cards added)
- 57 cards split off from multi-part notes, e.g. BIA/RTO/RPO/MTD → BIA, RTO-vs-RPO cloze, RTO+WRT≤MTD cloze;
  symmetric vs asymmetric → strengths card, key-count cloze (n(n−1)/2 vs 2n), hybrid-crypto card; PKI → CA vs RA, CRL vs OCSP,
  short-lived certs; Kerberos → components cloze, clock sync, KDC weakness; DNS → poisoning, DNSSEC vs DoH/DoT, tunneling;
  NIS2 → what/how it binds, 24h/72h reporting cloze, management accountability.
- 5 new exam or contrast cards from the source content: risk rejection is not valid, Delphi technique, why HMAC lacks non-repudiation,
  K8s RBAC has no deny (use admission policy), GitOps as Clark-Wilson.
- Long enumerations became clozes (CIA, STRIDE letters with hints, STRIDE → property, control functions/types, data roles, sanitization,
  firewall types, SOC 1/2/3, SAST/DAST/SCA/IAST, DR test ladder, backups, RAID, DR sites, CMMI levels).

## Grounding
- Each Grounding paragraph (40–60 words) trimmed to one short `<b>K8s:</b>` example in `extra`, or turned into its own card when it taught
  something testable (webhook failurePolicy = fail secure/open; don't delete a compromised pod first; secret leak → rotate; workload identity federation).

## Merges (1)
- Linux deck #77 (DAC vs MAC) merged into the DAC-vs-MAC card here (keeps that guid; Linux SELinux/AppArmor example moved to `extra`).

## Deletions (content dropped from inside notes, no whole notes deleted)
- ISC2 "list core secure design principles" laundry list → replaced by a Saltzer & Schroeder cloze + fail-securely card.
- OWASP Top 10 category listing (changes every edition) → kept only injection defense and SSRF-in-cloud.
- TCP handshake detail in the TCP/IP note (owned by Networking deck); hardened-runtime detail in VM-vs-container note (owned by Linux deck).
- Reciprocal agreements / mobile sites (low signal).

## Analogies
- 24 added (about 17%): e.g. due diligence vs due care (home inspection vs repair), Bell-LaPadula (spy), RPO/RTO (save point),
  SOC 2 Type I vs II (photo vs CCTV), SBOM (ingredients label).

## Product-content review
Reviewed card by card: no product-catered cards found (tools present are open-source subjects or short examples in `extra`); nothing deleted, rewritten or scrubbed.
