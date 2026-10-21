# Byzantine Fault Tolerance

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Consensus and replication](README.md)
> **Builds on:** [Consensus](consensus.md), [Impossibility results](../02-distributed-foundations/impossibility-results.md), [Public-key cryptography](../../11-security-and-cryptography/02-cryptography/public-key-cryptography.md), [Hash functions and MACs](../../11-security-and-cryptography/02-cryptography/hash-functions-and-macs.md)
> **Enables:** [CIA and threat modeling](../../11-security-and-cryptography/01-security-principles/cia-and-threat-modeling.md), [Distributed transactions](../04-distributed-data/distributed-transactions.md)

## Essence

Byzantine fault tolerance (BFT) is consensus and replication when faulty nodes may behave arbitrarily: send conflicting messages to different peers, forge claims, stay silent selectively, or collude. The name comes from Lamport, Shostak and Pease's "Byzantine Generals" (1982). Arbitrary faults cover malicious attackers, but also memory corruption and software bugs. The core result is that tolerating f such nodes requires **n ≥ 3f + 1** nodes and **quorums of 2f + 1**, so that any two quorums overlap in at least f + 1 nodes, at least one of them honest. Cryptographic signatures and message authentication stop faulty nodes from impersonating honest ones, but they cannot stop them from lying about their own state, which is why extra replicas are still needed.

## Core tenets

1. **3f + 1 is forced by "wait for n − f, of which f may lie".** A node cannot wait for all n replies, because f faulty nodes may never answer. Of the n − f it hears from, up to f may be faulty and lying, so the honest replies it hears number at least n − 2f. For the honest view to win in every pair of overlapping quorums, the overlap of two (n − f)-sized quorums, which is n − 2f, must exceed f. Hence n − 2f ≥ f + 1, that is n ≥ 3f + 1. With 4 replicas you tolerate 1 Byzantine fault; with 7, 2.

2. **Byzantine faults include equivocation, which crash faults cannot produce.** A faulty leader can tell half the replicas "the next command is A" and the other half "it is B". Crash-tolerant protocols like Raft trust the leader's messages and would split. BFT protocols add a round in which replicas tell each other what they received, and commit only when 2f + 1 replicas report the same value, so equivocation is detected or outvoted.

3. **Practical Byzantine Fault Tolerance (PBFT) made BFT efficient enough to use.** Castro and Liskov (1999) gave a protocol for partial synchrony with three phases per request: pre-prepare (the primary assigns a sequence number), prepare (replicas broadcast agreement on that assignment) and commit (replicas broadcast that a quorum has prepared). A view-change protocol replaces a faulty or slow primary. Its all-to-all phases cost O(n²) messages per decision, which limits it to tens of replicas.

4. **Signatures change costs, not the bound.** In the synchronous model with unforgeable signatures, agreement is possible for any number of faulty nodes, because a forwarded signed message cannot be altered. Real networks are not synchronous, and under partial synchrony n ≥ 3f + 1 holds even with signatures (Dwork, Lynch and Stockmeyer, 1988). Modern protocols such as HotStuff (2019) use threshold or aggregated signatures to collapse all-to-all voting into linear message complexity and to make leader rotation cheap.

5. **Clients must also verify.** A client cannot trust one replica's reply, since that replica may be faulty. It waits for f + 1 matching replies (at least one must come from an honest replica) or for a certificate of 2f + 1 signed votes. Read and write paths therefore cost more than in crash-tolerant systems, not just consensus.

6. **BFT assumes independent failures, which diversity must supply.** If all replicas run identical software, one exploitable bug compromises all of them at once, and the f bound is meaningless. Meaningful BFT needs diversity of implementation, operators, hardware or jurisdiction, which is expensive. This is why BFT is common where mutually distrusting parties share a ledger and rare inside one company's data centre, where crash-tolerant consensus plus good engineering suffices.

7. **Open-membership systems replace identities with costly resources.** Classical BFT needs a known set of n participants. Permissionless blockchains such as Bitcoin cannot count participants, because identities are free to create (the Sybil attack), so they weight votes by a scarce resource: computation in proof-of-work (Nakamoto, 2008), stake in proof-of-stake. Proof-of-work achieves agreement only probabilistically, with confirmations becoming more final as blocks accumulate, and assumes honest parties control a majority of the resource.

## Key concepts

| Term | Meaning |
|---|---|
| Byzantine fault | Arbitrary behaviour, including lying and collusion |
| Equivocation | Sending different, conflicting messages to different peers |
| n ≥ 3f + 1 | Replicas needed to tolerate f Byzantine faults under partial synchrony |
| Byzantine quorum | 2f + 1 replicas; any two overlap in at least one honest replica |
| PBFT | Three-phase leader-based BFT protocol with view changes |
| View change | Replacing the primary when it is suspected faulty |
| Quorum certificate | 2f + 1 signed votes proving a quorum agreed |
| Sybil attack | Gaining influence by creating many fake identities |
| Proof-of-work | Weighting votes by expended computation |

## How it fits

- **Below:** relies on [digital signatures](../../11-security-and-cryptography/02-cryptography/public-key-cryptography.md) and [message authentication codes (MACs)](../../11-security-and-cryptography/02-cryptography/hash-functions-and-macs.md) to authenticate messages, and on the [impossibility results](../02-distributed-foundations/impossibility-results.md) for its bounds; uses the [Byzantine failure model](../02-distributed-foundations/system-models-and-failures.md).
- **Above:** feeds the [threat modeling](../../11-security-and-cryptography/01-security-principles/cia-and-threat-modeling.md) view that a system must survive compromised components; blockchains apply it to [distributed transactions](../04-distributed-data/distributed-transactions.md) among distrusting parties; avionics and spacecraft use Byzantine-tolerant voting against hardware faults.
- **Siblings:** [consensus](consensus.md) is the crash-fault version with n ≥ 2f + 1; [replication](replication.md) supplies the state machine model BFT protects; [consistency models](consistency-models.md) define what BFT services promise (usually linearizability).

## Common misconceptions

- **"Byzantine faults are only about attackers."** Flipped bits, corrupted disks and buggy nodes producing inconsistent output are Byzantine too.
- **"Signatures let you tolerate any number of traitors."** Only in a synchronous network. With realistic timing assumptions you still need 3f + 1 replicas.
- **"Blockchains solve Byzantine consensus without assumptions."** Proof-of-work assumes an honest majority of computational power and gives only probabilistic finality.

## Go deeper

- Lamport, Shostak and Pease, "The Byzantine Generals Problem", *ACM TOPLAS* (1982): the problem and the 3f + 1 bound.
- Castro and Liskov, "Practical Byzantine Fault Tolerance", OSDI (1999): the protocol that made BFT practical.
- Yin et al., "HotStuff: BFT Consensus with Linearity and Responsiveness", PODC (2019).
- Cachin, Guerraoui and Rodrigues, *Introduction to Reliable and Secure Distributed Programming* (2nd ed., 2011): Byzantine abstractions treated rigorously.
