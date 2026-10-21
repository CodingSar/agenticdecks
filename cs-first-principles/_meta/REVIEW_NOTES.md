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

### 02 Theory of Computation
- Best explicit circuit lower bound ~ (3 + 1/86)n (Find et al. 2016), later ~3.1n (Li & Yang 2022).
- Quantum: two-qubit error ~10⁻³, surface-code threshold ~1%, ~1M physical qubits for RSA-2048 (Gidney 2025 estimate <1M).
- Earley: O(n²) unambiguous; linear on LR(k) only with Leo's (1991) optimisation — check wording.
- 1-way QFA (Kondacs–Watrous) bounded-error recognise a proper subset of regular languages.
- Hamiltonian simulation BQP-complete (decision version).
- NIST FIPS 203/204/205 (ML-KEM, ML-DSA, SLH-DSA) Aug 2024.
- Generalised chess EXP-complete; Go with Japanese ko EXP-complete; some games PSPACE-complete (Hex, Go without ko as Lichtenstein–Sipser ladder). Check wording.
- Universal TM log-factor overhead (Hennie–Stearns).
- Candidate leaf: Kolmogorov complexity.

### 07 Operating Systems
- **Inconsistent:** seL4 size ~9k (06) vs ~10k (07). Klein et al. 2009: ~8,700 lines C + 600 asm. Harmonise to "~8,700 lines of C".
- Linux syscalls ~350–450; ~100 ns syscall (more with KPTI).
- EEVDF in 6.6 (2023); MGLRU 6.1; cgroups 2.6.24 (2008), v2 stable 4.5; epoll 2.5.44/2.6; kqueue FreeBSD 4.1 (2000); io_uring 5.1 (2019).
- Robson 1971 bound; nested page walk up to 24 refs.
- Chou et al. 2001 driver error rates; Mars Pathfinder 1997; ext4 2009 delayed allocation; VENOM 2015; L1TF SMT.
- HDD 5–10 ms, 100–250 MB/s; dirty writeback ~30 s; O_NONBLOCK no effect on regular files.
- Candidate leaf: IPC under 02-process-management.

### 04 Computer Architecture
- ROB sizes (Pentium Pro 40, Golden Cove 512, M1 ~600+); M1 8-wide decode.
- Apple 128-byte lines; TLB 64 L1 / 1–3k L2.
- RVC ~25–30% code shrink (Waterman).
- Intel APX 32 GPRs (2023 announcement); 5-level paging Ice Lake (server); AMD NX 2003.
- H100 SXM 132 SMs, 16,896 FP32 lanes, ~67 TF FP32, ~989 TF dense FP16 — "~60" should read "~60–67".
- Horowitz 2014 ISSCC energy numbers; TPU v1 15–30x perf, 30–80x perf/W (Jouppi 2017).
- DRAM row conflict 40–50 ns; leakage ×10 per ~60–100 mV; per-core perf ~10–20%/yr post-2005 (Hennessy & Patterson give ~3.5%/yr 2015–18; check).
- NVMe 64K queues × 64K cmds; PCIe 5.0 32 GT/s ≈ 3.94 GB/s/lane/dir.
- Candidate leaves: SMT, roofline, trusted execution / virtualization extensions.

### 13 AI / 14 Human & Visual Computing
- 10^24–10^26 FLOPs frontier; ~16 B/param Adam mixed precision; 80–192 GB HBM; MFU 30–60%; Chinchilla ~20 tok/param; C≈6ND.
- Vocab 30k–250k; >1M context; RLVR reasoning 2024–25.
- Codec 30–50%/generation; Nielsen–Landauer 5 users ~80%(actually ~85%); JPEG ~10:1.
- AlexNet top-5 ~26%→~15.3%; ResNet 2015 below human ~5.1%; RT cores 2018.
- Fovea ~2°; Cowan ~4 chunks; preattentive <200–250 ms; HMD ≥90 Hz.
- Citations: Giesen 2011 blog; Catmull 1974 z-buffer (Straßer 1974 independently); AlphaZero 2017 preprint/2018 Science; Lazar 2nd ed 2017; Sayood 5th 2017; Shneiderman 6th 2016.
- Loose links: electromagnetism for light; hash tables for attention (analogy); search trees for decision trees/BVH.
- Candidate leaves: recurrent/sequence models; retrieval & vector search; data/feature engineering; visualization; AR/VR; audio & speech.

### 05 Algorithms
- Random BST height ≈ 4.311 ln n (Reed 2003); STP shortest-path tree; EEVDF still rbtree.
- Median selection ≥ (2+ε)n (Dor–Zwick); HLL ~2% in ~1.5 KB; Bloom 1% at 9.6 bits/elt, k=7.
- Max-flow almost-linear Chen et al. 2022; Karlin–Klein–Oveis Gharan STOC 2021; ω < 2.372.
- Bentley binary search ~10%; Java overflow bug 2006 (Bloch).
- Union-find tightness: Tarjan 1975, Fredman–Saks 1989.
- CLRS 4th ed chapter numbers (RAM model ch 2; amortized analysis ch 16) — verify.
- Candidate leaf: union-find.

### 08 Networking / 09 Data Management
- Packet switching 35 users 10% activity P(>10) ≈ 0.0004; 1986 collapse 32 kbit/s→40 bit/s; Mathis 1.22; CUBIC default 2.6.19 (2006); IW10 (RFC 6928).
- CRC-32 detection guarantees (softened).
- BGP ~75k ASes, ~1M IPv4 prefixes; Pakistan/YouTube 2008 ~2 h; Griffin et al. stable-paths NP-complete.
- Dyn 2016; Saltzer naming RFC 1498.
- HTTPS >90%; video majority of volume; Zipf hit ratio log growth.
- MACAW 1994; Heusse et al. 2003.
- LSM write amp 10–30x; Bloom 10 bits ~1%.
- Default isolation: PG/Oracle/SQL Server RC; InnoDB RR; Oracle "Serializable" = SI; Berenson et al.
- PostgreSQL fsyncgate 2018; System R DP ~10–15 relations.
- **Rule violation:** `layering-and-the-end-to-end-principle.md` "Builds on" links up to layer 12. Builds-on must point downward. Add mechanical check.
- Candidate leaves: SDN / data-centre networks; hash indexes; analytical warehouses.

### 00 Engineering / 03 Digital Logic
- Kuon & Rose 2007: FPGA ~35x area (~18x w/ hard blocks), 3–4x delay, ~14x dynamic power (~7x).
- Elmore ~0.5 rcL²; cooling ~100 W/cm²; CMOS fJ/op ~10⁶× Landauer; Bérut et al. 2012.
- GAA ~2022 (Samsung 3nm); EUV HVM ~2019; high-k 2007 (Intel 45nm).
- Unicode ~150k chars (v15–16); Rust overflow debug panic / release wrap.
- Citations to verify: Pike & Thompson UTF-8 1993 title; Box 1976 "Science and Statistics"; Sarpeshkar 1998; Ginosar 2011; Kogge & Stone 1973.
- Candidate leaf: memory cells (SRAM/DRAM/flash) in 03 or 00.

### 10 Distributed / 11 Security
- ~70% high-severity bugs memory safety; causal consistency strongest available (Mahajan et al. 2011, hedged).
- AES-GCM random nonce 2³² limit (NIST SP 800-38D); FIPS 203/204/205 2024.
- TrueTime ε a few ms (Spanner paper: typically <7 ms); drift 10–100 ppm.
- Mirai ~1 Tbps (OVH 2016); memcached amplification up to ~50,000x.
- Ring all-reduce 2(P−1)/P; OWASP 2021 A01 broken access control.
- Citations: HotStuff PODC 2019; Bailis et al. HAT PVLDB 7 (2013/2014); Kleppmann & Beresford TPDS 2017; Hellerstein & Alvaro CACM 2020; Ristić 2nd ed 2022.
- BFT 3f+1 statement (oral messages synchronous; partial synchrony even with signatures) — check.
- New leaves: privacy-enhancing-technologies, software-supply-chain-security.
