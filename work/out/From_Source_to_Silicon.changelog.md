# From Source to Silicon — changelog (composer)

**Scope.** Zero-to-hero on how a program becomes electrons, for a cloud/enterprise architect who programs: front end → types → IR/optimisation → codegen/ABI/linking → runtimes/JIT/GC → x86-64 / ARM64 / RISC-V / IBM Z → µarch → caches & memory models → GPU SIMT → TPUs & ML compilers → an explicit *mapping* subdeck that chains the other eleven. Composed from six writer parts (A–F, 56 notes each = 336 in), merged to **318 notes**, 21 hand-drawn SVGs, 36 % of cards with an analogy.

**Subdeck outline (notes).** 01 Lexing & Parsing 24 · 02 Semantic Analysis & Type Systems 24 · 03 IR & Optimisation 26 · 04 Code Generation, ABI & Linking 27 · 05 Runtimes 27 · 06 x86-64 26 · 07 ARM64, RISC-V & IBM Z 26 · 08 Microarchitecture 26 · 09 Memory Hierarchy 26 · 10 GPU 28 · 11 TPUs & AI Compilers 28 · 12 The Mapping 30.

**Within-deck dedupe (28 dropped/folded, 6 re-angled).** `similar.py 0.4` over the parts found 5 pairs; manual reading found the rest.
- Dropped as duplicates: AArch64 leaf-function (04 B37, dup of 07 bl/x30, sim 0.72); AAPCS64 cloze in 07 (kept the fuller one in 04); store buffer in 09 (kept the 08 card, moved the "outbox" analogy to it); FP16-in/FP32-accumulate on tensor cores in 10 (kept the bf16 multiplier-area card in 11, added "same split on GPUs"); hidden class and megamorphic cards in 12 (dups of 05; "what breaks" folded into the 12 inline-cache card); w/x zero-extension in 07 (folded into 06 eax/rax card).
- Folded into a neighbour's `extra` (fact kept, card gone): shift/reduce default → dangling-else; packrat → PEG; upvalues → closures; soundness definition → sound-vs-complete; three-address code → why-an-IR; forward/backward → dataflow; Dijkstra/Yuasa → concurrent write barrier; V8 tier names → tiered JIT; legacy prefixes → encoding layout; x86 register inventory → sub-registers; hazards + superscalar → pipelining; write-back/through → RFO.
- Dropped as low signal/catalogue: token-fields cloze, keyword tie-break, trait coherence, DCE, LLVM's three selectors, occupancy arithmetic (spec-ish), TPU (8,128) tiles.
- Re-angled: `xor eax,eax` (06 = ISA idiom, 08 = renamer mechanism; 06 back trimmed); `call/ret` (06) no longer explains the return-stack predictor (08 does); ARM-vs-TSO (07) asks only what reorders, 09 owns the `mov` vs `ldar/stlr` mapping; arithmetic intensity (11) became "given P and B, which kernels are memory-bound" so it no longer restates Roofline (09); SMT (08) re-angled to mechanism + when it hurts because Cloud Architecture already has shared/private + speedup.

**Bridge and contrast cards added (10).** AST → IR: lost vs gained (03); register allocation vs renaming (04); CPU vs JIT speculation (05); cache line vs coalescing sector (10); SASS vs µops — the GPU's "decode" is `ptxas` (10); compiler fusion vs µop fusion (11); the same loop on AArch64/SVE (12); JAX/TPU path for `a @ b` (12); "30 % slower after a compiler upgrade: which layer?" (12); bytecode vs PTX vs microcode (12). Subdeck 12 now refers to every other subdeck (01…11), and every `<b>Link:</b>` in the deck is normalised to `NN Subdeck · topic` (external: `Deep C · …`, `Cloud Architecture · …`, `Linux Internals · …`, `Go deck · …`, `LLMs deck · …`). Writer D's 33 links were pruned to the useful ones; missing obvious links were added (parsing → AST → IR, calling convention → stack frame → `call`, SSA → register allocation, inline cache → branch prediction, TSO → `mov` vs `ldar`, coalescing → cache lines, XLA fusion → Roofline, tensor cores → bf16).

**Overlap with existing decks (`similar.py 0.4` against Deep C, Cloud Architecture, Linux Internals, Go, LLMs, Physics).** Pairs seen and decisions: Deep C SysV-ABI cloze vs x86-64 register inventory (0.52) → dropped ours, folded into sub-registers; Deep C SysV-ABI vs syscall convention (0.41) → kept, different fact (`r10`, clobbers, `-errno`) with a card explaining *why* it differs; Cloud Architecture SMT (0.42) → re-angled (see above), now below threshold. By design (writers B/D/E/F) the deck references rather than repeats Deep C (strict aliasing, restrict, red zone, barriers x86 vs ARM, false sharing, nm/objdump), Cloud Architecture (HBM, NVLink/NVSwitch, warp/SM definitions, CUDA vs Tensor cores, BF16 range, systolic intro, NUMA, mispredict cost, training vs inference chips), Linux Internals (TLB/huge-page basics, page tables), Go (GC at high level, escape analysis), LLMs (FlashAttention, KV cache, quantisation).

**Consistency pass.** `source` labels uniform per subdeck (`Front end · Parsing`, `Types`, `IR & Opt`, `Codegen & ABI`, `Runtimes`, `ISA · x86-64`, `ISA · ARM64 / RISC-V / Z`, `µarch`, `Memory`, `GPU`, `Accelerators`, `Mapping`); tags start with `s2s`; `guid: null`; all backs ≤ 60 words and extras ≤ 50; HTML-escaped; dated phrasing removed ("recent parts", "600-entry ROB", "~900k cores", SVE2/Armv9 product list).

**Diagrams (21, all `media/s2s_*.svg`, rendered and checked).** regex_dfa, lr_trace, scope_chain, ssa_phi, stack_frame, plt_got, tiered_jit, tricolour, x86_regs, x86_encoding, isa_encoding, pipeline_forwarding, ooo_core, cache_lookup, mesi, gpu_mapping, coalescing, cuda_pipeline, systolic_ws, xla_pipeline, layer_stack. Fixed clipped text in isa_encoding, scope_chain, stack_frame, pipeline_forwarding, x86_encoding, tricolour and an unrenderable `⇒` glyph in xla_pipeline. No unused images.

**Deliberately left out.** Product spec sheets (core counts, clocks, SKUs), a second SIMD-vs-SIMT or systolic card outside their home subdecks, NUMA (Cloud Architecture), a Go-GC card beyond the comparative one, Wasm GC proposal details, GPU/TPU interconnect topology, and compiler-construction trivia (tool names, history without a lesson).

## Abbreviations expanded

Notes touched: 200 of 318. Form "full name (ABBR)" at the first occurrence per note (front/text, back, extra; skipping code, cloze interiors, Link: lines and cards that already expand it).

- ABI → application binary interface
- ABIs → application binary interfaces
- ALU → arithmetic logic unit
- AOT → ahead-of-time
- ASLR → address space layout randomisation
- AST → abstract syntax tree
- AVX → Advanced Vector Extensions
- AVX2 → Advanced Vector Extensions 2
- AoS → array of structures
- BCD → binary-coded decimal
- BF16 → brain floating point 16
- BIOS → basic input/output system
- BLAS → Basic Linear Algebra Subprograms
- BPE → byte-pair encoding
- BTB → branch target buffer
- CCWs → channel command words
- CF → carry flag
- CFG → control-flow graph
- CFI → call frame information
- CISC → complex instruction set computer
- CP → central processor
- CPUID → CPU identification
- CPs → central processors
- CSE → common subexpression elimination
- DAG → directed acyclic graph
- DCE → dead-code elimination
- DF → direction flag
- DFA → deterministic finite automaton
- DIMM → dual in-line memory module
- DLL → dynamic-link library
- DPDK → Data Plane Development Kit
- DRAM → dynamic RAM
- DRDA → Distributed Relational Database Architecture
- DSB → decoded stream buffer
- DSLs → domain-specific languages
- EBCDIC → Extended Binary Coded Decimal Interchange Code
- ELF → Executable and Linkable Format
- FLOP → floating-point operation
- FLOP/s → floating-point operations per second
- FLOPs → floating-point operations
- FMAs → fused multiply-add operations
- FP32 → 32-bit floating point
- FP8 → 8-bit floating point
- FPU → floating-point unit
- GC → garbage collection
- GCC → GNU Compiler Collection
- GELU → Gaussian error linear unit
- GEMM → general matrix multiply
- GIL → global interpreter lock
- GLR → generalised LR
- GOT → global offset table
- GSPMD → general and scalable parallelisation for ML computation graphs
- GVN → global value numbering
- HBM → high-bandwidth memory
- HIP → Heterogeneous-computing Interface for Portability
- HLO → high-level operations
- HM → Hindley-Milner
- IBRS → indirect branch restricted speculation
- IFUNC → indirect function
- ILP → instruction-level parallelism
- INT8 → 8-bit integer
- IPC → instructions per cycle
- IR → intermediate representation
- ISA → instruction set architecture
- JIT → just-in-time
- JITs → just-in-time compilers
- JS → JavaScript
- JVM → Java virtual machine
- KPTI → kernel page-table isolation
- L1 → level 1 cache
- L2 → level 2 cache
- L3 → level 3 cache
- LICM → loop-invariant code motion
- LL → left-to-right, leftmost-derivation
- LLC → last-level cache
- LMUL → vector register group multiplier
- LPARs → logical partitions
- LR → left-to-right, rightmost-derivation
- LRU → least recently used
- LSE → Large System Extensions
- LSP → Language Server Protocol
- LTO → link-time optimisation
- MAC → multiply-accumulate
- MCUs → microcontrollers
- MESI → Modified-Exclusive-Shared-Invalid
- MESIF → Modified-Exclusive-Shared-Invalid-Forward
- MFMA → matrix fused multiply-add
- MLIR → multi-level intermediate representation
- MOESI → Modified-Owned-Exclusive-Shared-Invalid
- MSROM → microcode sequencer ROM
- MVC → move characters
- MX → microscaling
- MXU → matrix multiply unit
- ModRM → mode-register-memory
- NFA → nondeterministic finite automaton
- NVMe → Non-Volatile Memory Express
- NZCV → negative, zero, carry, overflow
- OCP → Open Compute Project
- OF → overflow flag
- OoO → out-of-order
- PC → program counter
- PCIe → Peripheral Component Interconnect Express
- PCRE → Perl Compatible Regular Expressions
- PEG → parsing expression grammar
- PEP → Python Enhancement Proposal
- PGO → profile-guided optimisation
- PIE → position-independent executable
- PLT → procedure linkage table
- PRE → partial redundancy elimination
- PSW → program status word
- PTX → parallel thread execution
- RAIM → redundant array of independent memory
- RAS → reliability, availability and serviceability
- RAT → register alias table
- RAW → read-after-write
- RELRO → relocation read-only
- REX → register extension
- RFO → read for ownership
- RISC → reduced instruction set computer
- ROB → reorder buffer
- RRIP → re-reference interval prediction
- SAP → system assist processor
- SASS → NVIDIA's native GPU assembly
- SB → store buffering
- SC → sequential consistency
- SF → sign flag
- SIB → scale-index-base
- SIE → start interpretive execution
- SIMD → single instruction, multiple data
- SIMT → single instruction, multiple threads
- SLP → superword-level parallelism
- SM → streaming multiprocessor
- SMs → streaming multiprocessors
- SPMD → single program, multiple data
- SRAM → static RAM
- SS → storage-to-storage
- SSA → static single assignment
- SSE → Streaming SIMD Extensions
- SSE2 → Streaming SIMD Extensions 2
- SVE → Scalable Vector Extension
- SVM → Secure Virtual Machine
- SoA → structure of arrays
- SysV → System V
- TAGE → tagged geometric history length
- TBDR → tile-based deferred rendering
- TDX → Trust Domain Extensions
- TLAB → thread-local allocation buffer
- TLB → translation lookaside buffer
- TLP → thread-level parallelism
- TLS → thread-local storage
- TPU → tensor processing unit
- TSO → total store order
- UB → undefined behaviour
- UBSan → undefined behaviour sanitizer
- UEFI → Unified Extensible Firmware Interface
- VIPT → virtually indexed, physically tagged
- VLEN → vector register length
- VMCB → virtual machine control block
- VMCS → virtual machine control structure
- VMX → Virtual Machine Extensions
- VPU → vector processing unit
- WAR → write-after-read
- WAW → write-after-write
- XA → extended architecture
- XLA → Accelerated Linear Algebra
- ZF → zero flag
- zIIP → IBM Z Integrated Information Processor

Residual pass: expanded 43 more notes (AF, ALU, AoS, AST, AVX, BF16, CAS, CSE, DCE, DFA, ECC, ERMSB, FLOP, FP4, FP8, FP16, FSRM, GC, HIR, HLO, IDEs, IPC, IR, ISA, L1, L2, L3, LALR, LL/SC, LR, MIR, MLIR, MSRs, MXU, NFA, OF, PF, PLT, PR/SM, PTX, REX, RFO, RTL, SF, SIMD, SIMT, SLR, SM, SMT, SoA, SSA, TSO, UB, VPU, XLA, ZF, zIIPs; also the corresponding full names). Abbreviations that occur only inside cloze deletions are given in a "Terms:" line in `extra`. `Link:` lines (chapter titles such as "03 IR & Optimisation") are left bare by design. Product/ISA/company names and the universal set (CPU, GPU, RAM, OS, VM, API, ML, LLM, units) stay bare. Note #273 trimmed from 63 to 53 words by moving the "algebra, common-subexpression and dead-code elimination (CSE, DCE)" clause to `extra` (cloze deletions untouched). check.py: 0 errors, 0 warnings.
