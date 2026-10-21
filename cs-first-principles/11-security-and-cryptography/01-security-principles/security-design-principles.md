# Security Design Principles

> **Layer:** [11 Security and Cryptography](../README.md) › [Security principles](README.md)
> **Builds on:** [Security goals and threat modeling](cia-and-threat-modeling.md), [Reliability and redundancy](../../00-engineering-foundations/05-engineering-method/reliability-and-redundancy.md), [Kernel architectures](../../07-operating-systems/01-kernel-and-abstractions/kernel-architectures.md), [Kernel mode and system calls](../../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md)
> **Enables:** [Access control](../03-system-security/access-control.md), [Isolation and sandboxing](../03-system-security/isolation-and-sandboxing.md), [Foundations of modern cryptography](../02-cryptography/foundations-of-modern-cryptography.md), [Software architecture](../../12-software-engineering/01-design/software-architecture.md)

## Essence

Security design principles are rules for structuring a system so that it resists attack even when individual components have bugs. Most come from Saltzer and Schroeder's 1975 paper "The Protection of Information in Computer Systems", and they have survived fifty years because they address the structure of trust rather than any particular technology. The core ideas are: keep the part you must trust **small and simple**, give every component **only the privileges it needs**, **check every access** rather than caching a past decision, **default to denial**, and **assume the design is public**. Together they limit both the chance of a vulnerability and the damage when one is exploited.

## Core tenets

1. **Minimise the trusted computing base (TCB).** The TCB is every component whose failure can break the security policy: hardware, kernel, hypervisor, authentication service, cryptographic library. Every line in it is a line that must be right. Saltzer and Schroeder called this *economy of mechanism*: simple, small mechanisms can be inspected and tested; complex ones hide flaws. This is the argument for microkernels, small hypervisors and narrow privileged daemons.

2. **Least privilege limits the blast radius.** Each user, process and service should hold only the rights it needs, only for as long as it needs them. Then a compromised component can do only what it was already allowed to do. Practical forms: run network-facing code as an unprivileged user, drop root after binding a port, give services scoped credentials, and split a program into a small privileged part and a large unprivileged part (privilege separation, as in OpenSSH).

3. **Complete mediation: check every access, every time.** Every access to every object must pass through an authorisation check that cannot be bypassed, and the result should not be cached across changes in policy. A *reference monitor* is the abstract mechanism that does this; to be trustworthy it must be always invoked, tamper-proof and small enough to verify. Time-of-check-to-time-of-use (TOCTOU) bugs show what happens without it: a file is checked, then swapped, then used.

4. **Fail-safe defaults: deny unless explicitly allowed.** A forgotten rule in an allow-list leaves something inaccessible, which is noticed and fixed; a forgotten rule in a deny-list leaves something exposed, which is noticed by an attacker. The same reasoning applies to error handling: when a check fails or throws, the system should refuse the action, not proceed.

5. **Open design: security must not depend on secrecy of the design.** Kerckhoffs's principle (1883) says a cipher should remain secure even if everything about it except the key is public. Designs leak, through reverse engineering, insiders and published standards, so a system that relies on obscurity fails silently and all at once. Secret keys are small, easy to change and easy to protect; secret algorithms are none of those. Obscurity can add cost for attackers but must never carry the load.

6. **Defence in depth: assume each layer will fail.** Independent layers (input validation, memory-safe code, sandboxing, least privilege, network segmentation, monitoring) mean an attacker must defeat several mechanisms, not one. The layers must be genuinely independent; two checks that share the same parser bug add nothing. This is redundancy, applied against an adversary rather than random failure.

7. **Separation of privilege and least common mechanism.** Requiring two independent conditions (two keys, two people approving, a password and a hardware token) means one compromise is not enough. Minimising mechanisms shared between users (shared temporary directories, shared caches, shared processes) removes channels through which one user can attack or observe another; modern cache side channels are a failure of this principle.

8. **Psychological acceptability: secure must be the easy path.** If the secure way is harder than the insecure way, people will route around it: passwords on sticky notes, disabled certificate checks, shared accounts. Security mechanisms must fit how people actually work, and secure defaults in libraries and application programming interfaces (APIs) matter more than documentation telling developers to opt in.

## Key concepts

| Term | Meaning |
|---|---|
| TCB | Trusted computing base: components whose correctness the policy depends on |
| Economy of mechanism | Keep security mechanisms small and simple |
| Least privilege | Grant only the rights needed, for only as long as needed |
| Complete mediation | Check authorisation on every access |
| Reference monitor | Always-invoked, tamper-proof, verifiable access checker |
| Fail-safe defaults | Deny by default; errors lead to refusal |
| Open design / Kerckhoffs's principle | Security rests on keys, not on secret designs |
| Defence in depth | Multiple independent protective layers |
| Separation of privilege | Require several independent conditions to grant access |
| TOCTOU | Race between checking a condition and using the result |

## How it fits

- **Below:** the [kernel/user boundary](../../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md) and [kernel architectures](../../07-operating-systems/01-kernel-and-abstractions/kernel-architectures.md) are the original reference monitor and TCB debates; [modularity](../../12-software-engineering/01-design/modularity-and-information-hiding.md) makes small trusted components possible; [reliability and redundancy](../../00-engineering-foundations/05-engineering-method/reliability-and-redundancy.md) underlies defence in depth.
- **Above:** [software architecture](../../12-software-engineering/01-design/software-architecture.md) applies these to service boundaries ("zero trust" networks are complete mediation applied to every request); [interaction design](../../14-human-and-visual-computing/01-human-computer-interaction/interaction-design-principles.md) bears on psychological acceptability.
- **Siblings:** [threat modeling](cia-and-threat-modeling.md) identifies where to apply these principles; [privacy-enhancing technologies](privacy-enhancing-technologies.md) extend least privilege to data (collect and reveal only what is needed); [access control](../03-system-security/access-control.md) and [isolation](../03-system-security/isolation-and-sandboxing.md) are their main mechanisms; [cryptography](../02-cryptography/foundations-of-modern-cryptography.md) is built on open design.

## Common misconceptions

- **"Security through obscurity is always bad."** Obscurity as an extra layer can raise attacker cost; it is bad only when it is the main defence.
- **"More security features mean more security."** Each feature adds code to the TCB and attack surface; complexity is the enemy of security.
- **"Least privilege is an administrative detail."** It is the main factor deciding whether a single bug becomes a full system compromise.

## Go deeper

- Saltzer and Schroeder, "The Protection of Information in Computer Systems", *Proceedings of the IEEE* (1975): the original eight principles.
- Anderson, *Security Engineering* (3rd ed., 2020): the principles applied across real systems.
- Lampson, "Protection", *Proceedings of the Princeton Symposium* (1971; reprinted in *ACM Operating Systems Review*, 1974): the access matrix model.
- Provos, Friedl and Honeyman, "Preventing Privilege Escalation", USENIX Security (2003): privilege separation in OpenSSH.
