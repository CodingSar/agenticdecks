# Security Principles

> **Layer:** [11 Security and Cryptography](../README.md) › Security principles
> **Children:** [CIA and threat modeling](cia-and-threat-modeling.md) · [Security design principles](security-design-principles.md)

## What this area is about

Before choosing a cipher or a firewall rule, you must say what you are protecting, from whom, and what you are willing to trust. This area supplies that vocabulary and the design rules that have proved durable since the 1970s. It answers two questions: *what does "secure" mean for this system?* (security goals and threat models) and *how should a system be built so that it stays secure when parts of it fail or are attacked?* (design principles).

The unifying idea is that **security is relative and adversarial**. There is no secure system in the abstract, only a system that meets stated goals against a stated attacker under stated assumptions. And because the attacker adapts, defences must be structured so that a single mistake does not lose everything: few trusted components, minimal privileges, safe defaults, and several independent layers.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [CIA and threat modeling](cia-and-threat-modeling.md) | States the goals (confidentiality, integrity, availability and their relatives) and the method for finding threats against a specific system | Engineering trade-offs, probability |
| [Security design principles](security-design-principles.md) | The rules for building systems that meet those goals robustly: least privilege, complete mediation, fail-safe defaults, defence in depth, small trusted base | Threat modeling, modularity |

Read threat modeling first. It turns "make it secure" into a concrete list of assets, adversaries and attack paths, and it tells you where the trust boundaries are. The design principles then say how to place and shape mechanisms at those boundaries. The two form a loop in practice: a design is checked against the threat model, the threat model is updated as the design reveals new attack surface, and both are revised after incidents.

```
  assets + adversary + assumptions  --->  threats (STRIDE, attack trees)
                 ^                                  |
                 |                                  v
         incidents, new attacks  <---  design under principles
                                        (least privilege, mediation, ...)
```

(STRIDE is the threat taxonomy explained in [CIA and threat modeling](cia-and-threat-modeling.md).)

## Connections to sibling areas

- **[Cryptography](../02-cryptography/README.md):** cryptography's formal definitions (what an adversary may query, what counts as a break) are threat models made mathematically precise; Kerckhoffs's principle is a design principle.
- **[System security](../03-system-security/README.md):** access control and isolation are the mechanisms that implement least privilege, complete mediation and separation of privilege.
- **[Network and application security](../04-network-and-application-security/README.md):** web and network attacks are where unexamined trust assumptions (trusting input, trusting the network) most often fail.

## Connections across layers

These principles generalise ideas from [engineering trade-offs](../../00-engineering-foundations/05-engineering-method/tradeoffs-and-constraints.md) and [reliability and redundancy](../../00-engineering-foundations/05-engineering-method/reliability-and-redundancy.md): defence in depth is redundancy against an adversary. They lean on [modularity and information hiding](../../12-software-engineering/01-design/modularity-and-information-hiding.md) to keep trusted components small. Threat modeling feeds [requirements](../../12-software-engineering/02-process/requirements.md) and connects to the [ethics](../../15-computing-in-context/ethics-and-professional-responsibility.md) and [law](../../15-computing-in-context/law-privacy-and-policy.md) of protecting people's data. The Byzantine failure model in [distributed systems](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md) is a threat model for replicas.

## Cross-cutting threads

- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): minimise what must be trusted, verify the rest.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): security against usability, cost and performance.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): defence in depth.
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): trust boundaries usually coincide with interfaces.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): a security policy is an invariant.
