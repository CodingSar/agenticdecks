# 11 Security and Cryptography

> **Layer:** 11 Security and Cryptography
> **Children:** [Security principles](01-security-principles/README.md) · [Cryptography](02-cryptography/README.md) · [System security](03-system-security/README.md) · [Network and application security](04-network-and-application-security/README.md)

## What this area is about

Security is the study of how systems keep working as intended when someone is actively trying to make them fail. Every other layer in this tree designs against nature: noise, wear, random failures, honest mistakes. Security designs against an **adversary**, an intelligent opponent who chooses inputs, timing and targets to do the most damage, and who only needs to find one weakness while defenders must cover all of them. That asymmetry is the reason security cannot be added at the end or bolted onto one component.

The unifying idea is that **security is a property of a whole system relative to a threat model**. A system is "secure" only with respect to stated goals (what must be protected), a stated adversary (what the attacker can do), and stated assumptions (what is trusted). Cryptography supplies primitives whose security can be stated precisely and reduced to well-studied hard problems. System and network security apply those primitives, together with isolation and access control, to real machines and protocols, where most failures come not from broken mathematics but from bugs, misuse and unexamined assumptions.

## Why this layer sits here

Security sits high in the stack because it is a property of whole systems, and the attacks it must stop exploit every layer below.

- **Hardware ([04 Computer Architecture](../04-computer-architecture/README.md)):** caches, speculative execution and shared hardware leak secrets through [side channels](03-system-security/side-channels.md); [virtual memory hardware](../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md) and privilege rings provide the isolation everything else relies on.
- **Languages ([06 Programming Languages](../06-programming-languages/README.md)):** memory-unsafe languages allow [memory corruption](03-system-security/memory-safety-vulnerabilities.md); [type systems](../06-programming-languages/02-semantics-and-types/type-systems.md) and [garbage collection](../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md) remove whole bug classes.
- **Operating systems ([07](../07-operating-systems/README.md)):** [kernel mode and system calls](../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md), [address spaces](../07-operating-systems/04-memory-management/address-spaces-and-paging.md) and [virtual machines](../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md) are the enforcement mechanisms for [access control](03-system-security/access-control.md) and [isolation](03-system-security/isolation-and-sandboxing.md).
- **Networks ([08](../08-networking/README.md)):** the Internet's core protocols were designed without authentication, so [protocol flaws](04-network-and-application-security/network-attacks-and-defenses.md) in routing, naming and transport are attack surfaces.
- **Data and distribution ([09](../09-data-management/README.md), [10](../10-distributed-and-parallel-computing/README.md)):** injection attacks target query languages; [Byzantine fault tolerance](../10-distributed-and-parallel-computing/03-consensus-and-replication/byzantine-fault-tolerance.md) is distributed agreement against an adversary.
- **Mathematics ([01](../01-mathematical-foundations/README.md), [02](../02-theory-of-computation/README.md)):** cryptography rests on [number theory](../01-mathematical-foundations/03-discrete-mathematics/number-theory.md), [abstract algebra](../01-mathematical-foundations/04-algebra/abstract-algebra.md), [probability](../01-mathematical-foundations/06-probability-and-statistics/probability.md), [information theory](../02-theory-of-computation/01-information-theory/entropy-and-information.md) and [computational complexity](../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md).

Upward, this layer contributes **trust boundaries with stated guarantees**: authenticated, confidential channels; isolated execution; and policies about who may do what. [12 Software Engineering](../12-software-engineering/README.md) turns these into secure development practice and review; [13 Artificial Intelligence](../13-artificial-intelligence/README.md) inherits them and adds new attack surfaces in [alignment and safety](../13-artificial-intelligence/04-advanced-paradigms/alignment-and-safety.md); [15 Computing in Context](../15-computing-in-context/README.md) takes up [privacy law](../15-computing-in-context/law-privacy-and-policy.md) and the [ethics](../15-computing-in-context/ethics-and-professional-responsibility.md) of disclosure.

## How the children fit together

```
   01 Security principles   (goals, threat models, design principles)
          |                         \
          v                          v
   02 Cryptography           03 System security
   (primitives with          (access control, memory safety,
    proofs/reductions)        isolation, side channels)
          \                          /
           v                        v
       04 Network and application security
       (authentication, web, network attacks)
```

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Security principles](01-security-principles/README.md) | Defines the goals (confidentiality, integrity, availability, privacy), the adversary (threat model) and the design rules | Engineering method, probability |
| [Cryptography](02-cryptography/README.md) | Mathematical tools for secrecy and authenticity over untrusted channels and storage | Number theory, complexity, probability |
| [System security](03-system-security/README.md) | Protecting computation inside a machine: who may access what, and keeping components isolated | Architecture, languages, operating systems |
| [Network and application security](04-network-and-application-security/README.md) | Protecting communication and applications across networks: identity, the web, network protocols, the software supply chain | All three above, networking |

Start with the principles, because every later topic is judged against a threat model. Cryptography and system security can then be read in either order: cryptography protects data that leaves your control (on a wire, on someone else's disk), system security protects computation on a machine you partly control. Network and application security combines them in the place most attacks happen.

## Connections to neighbouring layers

- **[04 Computer Architecture](../04-computer-architecture/README.md):** provides privilege levels and memory protection, but also the shared caches and speculation behind Spectre-class attacks; hardware security modules and trusted execution environments extend the trusted base into silicon.
- **[06 Programming Languages](../06-programming-languages/README.md):** memory safety and type safety are the strongest defence against the most common vulnerability classes; [formal methods](../06-programming-languages/05-formal-methods/README.md) verify cryptographic code and protocols.
- **[07 Operating Systems](../07-operating-systems/README.md):** the kernel is the reference monitor for files and processes; containers and hypervisors are the isolation boundaries of the cloud.
- **[08 Networking](../08-networking/README.md):** Transport Layer Security (TLS) secures the transport layer; the Domain Name System (DNS) and the Border Gateway Protocol (BGP) are attack targets; the end-to-end argument explains why encryption belongs at the endpoints.
- **[10 Distributed and Parallel Computing](../10-distributed-and-parallel-computing/README.md):** Byzantine faults are the distributed-systems name for adversarial behaviour; consensus protocols use signatures and hashes.
- **[12 Software Engineering](../12-software-engineering/README.md):** secure design, [code review and static analysis](../12-software-engineering/03-quality/static-analysis-and-code-review.md), [testing](../12-software-engineering/03-quality/testing.md) (including fuzzing) and patch delivery are how security is achieved in practice; [build pipelines](../12-software-engineering/04-operations/build-and-continuous-delivery.md) are a prime target of [supply chain attacks](04-network-and-application-security/software-supply-chain-security.md).
- **[13 Artificial Intelligence](../13-artificial-intelligence/README.md):** machine-learning systems introduce adversarial examples, data poisoning and prompt injection.
- **[15 Computing in Context](../15-computing-in-context/README.md):** privacy, surveillance and disclosure are legal and ethical questions as much as technical ones; [privacy-enhancing technologies](01-security-principles/privacy-enhancing-technologies.md) supply the technical half.

## Connections across layers

The layer's mathematical floor is complexity theory: modern cryptography assumes certain problems (factoring, discrete logarithms, finding hash collisions) cannot be solved efficiently, which is unproved: a proof that P = NP (every problem whose solutions can be checked in polynomial time can also be solved in polynomial time) would break it, and large [quantum computers](../02-theory-of-computation/05-quantum-computation/quantum-algorithms.md), if built, would break today's public-key schemes, since Shor's algorithm solves factoring and discrete logarithms efficiently. Its physical floor is that computation leaks: [energy use](../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md), timing and electromagnetic emission all carry information about secrets.

## Cross-cutting threads

- [Trust and verification](../CROSS-CUTTING.md#trust-and-verification): every design starts by deciding what is trusted and minimising it.
- [Abstraction and layering](../CROSS-CUTTING.md#abstraction-and-layering): attacks succeed where an abstraction leaks (side channels, undefined behaviour).
- [Limits and impossibility](../CROSS-CUTTING.md#limits-and-impossibility): security rests on computational hardness assumptions and information-theoretic bounds.
- [Virtualization](../CROSS-CUTTING.md#virtualization): isolation by giving each principal its own virtual machine or address space.
- [The end-to-end argument](../CROSS-CUTTING.md#the-end-to-end-argument): encryption and authentication belong at the endpoints.
- [Invariants and correctness](../CROSS-CUTTING.md#invariants-and-correctness): a security policy is an invariant that must hold against adversarial inputs.
- [Composition](../CROSS-CUTTING.md#composition): secure parts do not automatically compose into a secure whole.
