# Side Channels

> **Layer:** [11 Security and Cryptography](../README.md) › [System security](README.md)
> **Builds on:** [Cache design](../../04-computer-architecture/03-memory-hierarchy/cache-design.md), [Hazards and branch prediction](../../04-computer-architecture/02-processor-microarchitecture/hazards-and-branch-prediction.md), [Superscalar and out-of-order execution](../../04-computer-architecture/02-processor-microarchitecture/superscalar-and-out-of-order.md), [Thermodynamics and energy](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md)
> **Enables:** [Symmetric encryption](../02-cryptography/symmetric-encryption.md), [Isolation and sandboxing](isolation-and-sandboxing.md), [Cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md)

## Essence

A side channel is information that leaks through the physical behaviour of a computation rather than through its intended outputs: how long it takes, which cache lines it touches, how much power it draws, what electromagnetic radiation or sound it emits. Abstractions such as "a program's output is its only observable effect" are false at the physical level, and side-channel attacks exploit the gap. If the secret influences *what the hardware does*, which branch is taken, which memory address is read, how many iterations run, an observer who can measure the effect learns about the secret, without breaking any access-control rule or cryptographic assumption. Since 2018, **transient-execution attacks** such as Spectre and Meltdown have shown that speculative execution makes even code that never architecturally touches a secret leak it.

## Core tenets

1. **Secret-dependent timing leaks secrets.** Kocher (1996) showed that measuring how long RSA and Diffie–Hellman private-key operations take reveals the key, because square-and-multiply exponentiation does extra work for each 1 bit. Brumley and Boneh (2003) showed this works remotely over a network against OpenSSL. Any branch, loop bound or early exit that depends on a secret (including byte-by-byte comparison of a password or MAC (message authentication code) tag) is a potential leak.

2. **Shared caches turn memory access patterns into a channel.** An attacker sharing a cache with a victim can prepare the cache, let the victim run, and time its own accesses to learn which cache sets or lines the victim used. *Prime+Probe* fills a cache set and checks what was evicted; *Flush+Reload* flushes a shared memory line and checks whether the victim reloaded it. Table-based AES (Advanced Encryption Standard) implementations, whose table indices depend on key bytes, fell to these attacks, including across virtual machines on the same host.

3. **Constant-time programming is the main software defence.** Cryptographic code is written so that its sequence of instructions and memory addresses does not depend on secret values: no secret-dependent branches, no secret-dependent table lookups, no variable-time instructions (such as division on some processors) on secrets. Hardware AES instructions remove the table lookups altogether. Compilers can undo constant-time intentions, so such code is checked with dedicated tools.

4. **Speculative execution leaks data that was never architecturally read.** Processors predict branches and execute ahead; if the prediction was wrong, they discard the results, but not the cache footprint. Spectre (Kocher et al., 2018) trains a branch predictor so the victim speculatively reads out of bounds and encodes the value into the cache, where Flush+Reload recovers it. Meltdown (Lipp et al., 2018) exploited processors that let user code speculatively read kernel memory before the permission check took effect. The architectural contract held; the microarchitecture leaked.

5. **Transient-execution defences are costly and partial.** Meltdown was fixed by separating kernel and user page tables (kernel page-table isolation) and then in hardware. Spectre-class variants need speculation barriers, retpolines (a software construct that prevents indirect-branch prediction from being steered), index masking, process-per-site isolation in browsers, and microcode changes, each costing performance. Because speculation is central to processor performance, new variants keep appearing.

6. **Physical channels matter when the attacker is near the device.** Power analysis (Kocher, Jaffe and Jun, 1999) recovers keys from smart cards by recording power use; differential power analysis averages many traces to extract signals far below the noise. Electromagnetic emanations, acoustic noise and fault injection (glitching voltage or clock to make the processor skip an instruction) are related threats. Defences include masking (randomly splitting secrets so intermediate values are independent of them) and hardware shielding.

7. **Software can attack hardware physics too.** Rowhammer (Kim et al., 2014) showed that repeatedly activating one row of Dynamic Random-Access Memory (DRAM) can flip bits in adjacent rows, because cells are packed so densely that charge leaks between them. Attackers used it to gain kernel privileges from unprivileged code. Error-correcting memory and targeted row refresh reduce, but do not eliminate, the risk.

8. **Side channels are a failure of shared resources and abstraction.** They arise wherever principals share hardware (caches, predictors, memory buses, power supplies) and the abstraction promises more isolation than the physics provides. The general mitigations are to avoid sharing (dedicated cores, partitioned caches), to remove secret dependence (constant time), or to add noise, each trading performance or cost for confidentiality.

## Key concepts

| Term | Meaning |
|---|---|
| Side channel | Unintended information flow through physical effects of computation |
| Covert channel | Deliberate signalling between colluding parties via such effects |
| Timing attack | Inferring secrets from operation durations |
| Prime+Probe / Flush+Reload | Cache attacks via eviction sets / via shared memory lines |
| Constant-time code | Code whose control flow and memory addresses do not depend on secrets |
| Transient execution | Instructions executed speculatively and later discarded |
| Spectre / Meltdown | Speculative attacks via mistrained prediction / via delayed permission checks |
| Power analysis | Recovering secrets from a device's power consumption |
| Rowhammer | Inducing DRAM bit flips by repeated row activation |
| Masking | Randomly splitting secret values to decorrelate leakage |

## How it fits

- **Below:** caches from [cache design](../../04-computer-architecture/03-memory-hierarchy/cache-design.md) and [coherence](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md); speculation from [branch prediction](../../04-computer-architecture/02-processor-microarchitecture/hazards-and-branch-prediction.md) and [out-of-order execution](../../04-computer-architecture/02-processor-microarchitecture/superscalar-and-out-of-order.md); power leakage from [complementary metal-oxide-semiconductor (CMOS) switching](../../00-engineering-foundations/03-semiconductor-devices/cmos.md) and [energy physics](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md); Rowhammer from [DRAM](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md) cell physics.
- **Above:** constrains [symmetric](../02-cryptography/symmetric-encryption.md) and [public-key](../02-cryptography/public-key-cryptography.md) implementations; shapes [multi-tenant cloud](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) scheduling and [browser isolation](../04-network-and-application-security/web-security.md).
- **Siblings:** [isolation](isolation-and-sandboxing.md) defines boundaries that side channels cross; [memory-safety bugs](memory-safety-vulnerabilities.md) are the other route across them, via control rather than observation.

## Common misconceptions

- **"If the algorithm is mathematically secure, the implementation is."** Timing, cache and power leaks are properties of implementations on real hardware.
- **"Network jitter hides timing differences."** Averaging many measurements removes noise; remote timing attacks have recovered keys across networks.
- **"Spectre was a bug that has been patched."** It is a class arising from speculation itself; mitigations address known variants at a performance cost.

## Go deeper

- Kocher, "Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems", CRYPTO (1996).
- Kocher et al., "Spectre Attacks: Exploiting Speculative Execution", IEEE Symposium on Security and Privacy (2019).
- Yarom and Falkner, "FLUSH+RELOAD: A High Resolution, Low Noise, L3 Cache Side-Channel Attack", USENIX Security (2014).
- Kim et al., "Flipping Bits in Memory Without Accessing Them", ISCA (2014): Rowhammer.
