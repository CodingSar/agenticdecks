# Deck simplification changes

Branch `deck-simplification`. Counts compare each `work/out/*.json` against commit `6f7cd80` (guids pinned, before any content edit). Edited cards keep their guid; new and changed cards carry the tag `simplified`. "Split" cards are counted under Edited (the original is rewritten) and Added (the extra cards).

## Per-deck changes

| Deck | Before | After | Edited | Added | Deleted |
|---|---|---|---|---|---|
| AZ-305_Solutions_Architect_Expert | 139 | 156 | 6 | 17 | 0 |
| Adaptive_Systems | 58 | 70 | 1 | 12 | 0 |
| Adoption_Epistemics_Governance | 91 | 99 | 2 | 8 | 0 |
| ArchiMate_3 | 145 | 162 | 14 | 18 | 1 |
| Architect_Craft | 161 | 179 | 6 | 18 | 0 |
| Architecture_Styles | 217 | 234 | 2 | 17 | 0 |
| Art_History | 202 | 222 | 4 | 20 | 0 |
| BPMN_and_Business_Architecture | 64 | 76 | 2 | 12 | 0 |
| CISSP_Cloud_K8s | 141 | 171 | 16 | 30 | 0 |
| Chemistry | 304 | 346 | 24 | 45 | 3 |
| Clean_Code_and_Design_Patterns | 458 | 483 | 5 | 25 | 0 |
| Cloud_Architecture | 113 | 132 | 2 | 19 | 0 |
| Data_Engineering | 79 | 89 | 0 | 10 | 0 |
| Deep_C_Kernel_Drivers_Embedded | 350 | 384 | 7 | 34 | 0 |
| Distributed_Systems_and_Data | 218 | 239 | 4 | 21 | 0 |
| Economics_for_Architects | 64 | 77 | 3 | 13 | 0 |
| Foundations_Fitness_Sleep_Money | 56 | 65 | 1 | 9 | 0 |
| From_Source_to_Silicon | 318 | 349 | 15 | 31 | 0 |
| Go_and_K8s_Operators | 176 | 195 | 3 | 19 | 0 |
| Identity_and_Zero_Trust | 205 | 222 | 8 | 17 | 0 |
| Kubernetes | 245 | 262 | 12 | 17 | 0 |
| LLMs_and_Agentic_Engineering | 126 | 141 | 1 | 15 | 0 |
| Linux_Internals_for_K8s_Security | 179 | 200 | 9 | 21 | 0 |
| Music_History | 219 | 233 | 9 | 14 | 0 |
| NORA_and_GEMMA | 80 | 88 | 3 | 8 | 0 |
| Networking | 164 | 191 | 9 | 27 | 0 |
| Novius_Bedrijfsarchitectuur | 88 | 98 | 3 | 10 | 0 |
| Open_Agile_Architecture | 211 | 239 | 10 | 29 | 1 |
| Philosophy | 219 | 253 | 8 | 34 | 0 |
| Physics | 219 | 241 | 5 | 22 | 0 |
| Physics_for_Datacenters | 58 | 65 | 2 | 7 | 0 |
| Pipeline_Security_and_SOC_Monitoring | 163 | 178 | 2 | 15 | 0 |
| Platform_Engineering | 240 | 276 | 22 | 37 | 1 |
| Pragmatic_Programmer | 149 | 167 | 6 | 18 | 0 |
| Quantitative_Foundations | 349 | 379 | 8 | 30 | 0 |
| Robotics_Arduino_to_Physical_AI | 290 | 325 | 9 | 35 | 0 |
| SAFe_for_Architects | 109 | 123 | 4 | 14 | 0 |
| SRE_and_Observability | 206 | 220 | 6 | 15 | 1 |
| STACKIT_Hybrid_Cloud_Architect | 157 | 171 | 3 | 14 | 0 |
| Software_Architecture_and_DDD | 123 | 136 | 3 | 13 | 0 |
| Software_Engineering_Classics | 211 | 236 | 2 | 25 | 0 |
| Software_Testing | 120 | 134 | 5 | 14 | 0 |
| Spanish_Intermediate_Advanced | 202 | 242 | 1 | 40 | 0 |
| TOGAF_10 | 80 | 92 | 3 | 12 | 0 |
| Team_Topologies | 43 | 51 | 5 | 8 | 0 |
| **Total** | 7809 | 8691 | 275 | 889 | 7 |

## Technical errors corrected

| Deck | Card id | Finding | Source |
|---|---|---|---|
| Networking | `t%k0|40R>%` | `tcp_syn_retries=6` was stated as failing at 63 s; 63 s matches 5 retries, the default of 6 fails at about 127 s (7 retries about 255 s is our extrapolation) | kernel.org ip-sysctl documentation |
| Philosophy | `AOxP3R9$9!` | Thesis-antithesis-synthesis is not Hegel's own method; it traces to Kant/Fichte and was popularised as a label for Hegel by Chalybäus (1837) | Mueller 1958, https://doi.org/10.2307/2708008 |
| Linux_Internals_for_K8s_Security | `Dj(kJP|#Z8` | "iptables in maintenance mode" unsupported; IPVS deprecation (1.35) and nftables GA (1.33) confirmed | https://www.k8s.dev/resources/keps/5495/ |
| Linux_Internals_for_K8s_Security | `lcuk,G}Ylk` | cgroup v1 is past maintenance mode: kubelet refuses to start on cgroup v1 from 1.35 unless `failCgroupV1` is false | https://kubernetes.io/blog/2026/10/06/kubernetes-cgroups-v2-shift/ |
| Robotics_Arduino_to_Physical_AI | `xc[?5u|c++` | Servo 1–2 ms pulse covers only about 90–120° on many servos; 0.5–2.5 ms is the usual full sweep | https://www.arduino.cc/reference/en/libraries/servo/attach/ |

Checked and left unchanged: Robotics `C~{j<T0-:*` (arXiv 2604.15483) and `xdsE|-.X9e` (company-stated by Figure AI, not independently confirmed).

Caveat: several sources were read through search summaries only (kubernetes.io, k8s.dev, the Mueller article, kernel.org mirror), so these five fixes deserve a human glance.

## Deleted card ids

Deleted only as merged or cross-deck duplicates.

- ArchiMate_3: `xFiofeWPjn` — Typical application-layer pattern in an ArchiMate model?
- Chemistry: `dU.DG?l[`*` — Why does carbon build life's chains while silicon builds rock?
- Chemistry: `H?*Z2t2p0o` — Why do CO₂, CH₄ and water vapour trap heat but N₂ and O₂ do not?
- Chemistry: `Lc3;O)5@$l` — Why are nitrogen-rich compounds such as trinitrotoluene (TNT) and nitr
- Open_Agile_Architecture: `bwXSisDj_+` — What makes a postmortem <i>blameless</i>?
- Platform_Engineering: `CNvc8d@N,;` — What is the <b>Thinnest Viable Platform (TVP)</b>?
- SRE_and_Observability: `iLgLlT&l&@` — When do <b>metrics beat logs</b>?

Cross-deck duplicates resolved: Thinnest Viable Platform kept in Team_Topologies, blameless postmortem kept in SRE_and_Observability. The Rococo cards (Architecture_Styles / Art_History) ask different questions and were both kept; Networking `QlLJ}QOo<a` vs Quantitative_Foundations `DDDYyt^@:N` was not changed.
