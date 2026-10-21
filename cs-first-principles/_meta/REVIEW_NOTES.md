# Review notes

Collected from writer reports, to be resolved in the review pass.

## Taxonomy suggestions

- 01: add a Fourier analysis leaf (used by signals, compression, graphics), probably `05-continuous-mathematics/fourier-analysis.md`.
- 01: add a Markov chains leaf under `06-probability-and-statistics/` (used by networking queues, randomized algorithms, Reinforcement Learning (RL), PageRank).
- 05: no dedicated union–find (disjoint-set) leaf; Kruskal's algorithm and relations link to MST instead.
- 15: possible leaf on environmental impact (energy, e-waste).

## Claims to verify

### 01 Mathematical Foundations
- Random 1,024-bit odd number is prime with probability ~1/355; CRT speeds RSA decryption ~4x; Euclid's remainder halves every two steps.
- 256-bit ECC ≈ 3,072-bit RSA/DH; Pohlig–Hellman motivates prime-order subgroups.
- Birthday bound ≈ 1.18√m for 50%; log₂ n! ≈ n log₂ n − 1.44n.
- Fan-out to 100 servers: 63% exceed single-server p99 (Dean & Barroso 2013).
- Gradient descent stable for step < 2/L; Kelly et al. 1998 dual decomposition view of TCP.
- Matmul 2n³ flops on 3n² data; Strassen O(n^2.81) 1969.
- Shannon switching paper 1938 from 1937 thesis.
- Finite differences lose ~half the digits.

### 12 Software Engineering / 15 Computing in Context
- ~70% of outages due to changes (SRE book); Google's 50% toil cap.
- Bacchelli & Bird 2013 code-review findings.
- Unix file I/O "about five calls" (Ousterhout).
- Norvig 1996: 16 of 23 GoF patterns invisible/simpler in dynamic languages.
- MacCormack, Rusnak & Baldwin 2012; Nagappan et al. 2008 org metrics predict defects.
- Therac-25: six known massive overdoses 1985–87.
- ACM Code 2018 principle list.
- Sweeney 87% (2000); GDPR details (six lawful bases, Art. 5, €20M/4%, 72 h); Google v. Oracle 2021 fair use; Schrems II 2020; EU AI Act Regulation (EU) 2024/1689.
- Shannon 1937 thesis; Manchester Baby June 1948; TCP/IP flag day 1 Jan 1983; Moore 1975 revision.
- Kernighan quote in *The Elements of Programming Style*.

### 06 Programming Languages
- Shi et al. register vs stack VM: ~47% fewer instructions, ~25% larger code.
- Interpreters ~3–30x slower than optimised native code.
- seL4 ~9k lines C, ~20 person-years (Klein et al. 2009).
- Csmith found no wrong-code bugs in CompCert's verified middle end.
- ~70% of serious security bugs are memory safety (Google/Microsoft).
- HM inference DEXPTIME-complete (Mairson 1990; Kfoury/Tiuryn/Urzyczyn); System F inference undecidable (Wells 1999).
- PGO ~10%.
- **Suspect:** "~1 ms or less pauses for G1, ZGC, Go": true for ZGC/Go, not G1 (default pause target 200 ms). Fix.
- x86-64 16 GPRs, AArch64 31.
- Generational hypothesis: Lieberman & Hewitt 1983, Ungar 1984.
- Alpern & Schneider 1985 safety ∩ liveness.
- Newcombe et al. 2015 TLA+ at AWS; Coq renamed Rocq; HACL* in Firefox; Gonthier 2005, Flyspeck 2014.
- Gödel incompleteness has no home leaf (linked to halting problem).
