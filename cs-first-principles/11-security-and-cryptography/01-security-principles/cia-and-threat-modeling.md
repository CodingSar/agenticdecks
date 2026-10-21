# CIA and Threat Modeling

> **Layer:** [11 Security and Cryptography](../README.md) › [Security principles](README.md)
> **Builds on:** [Tradeoffs and constraints](../../00-engineering-foundations/05-engineering-method/tradeoffs-and-constraints.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [System models and failures](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md)
> **Enables:** [Security design principles](security-design-principles.md), [Foundations of modern cryptography](../02-cryptography/foundations-of-modern-cryptography.md), [Requirements](../../12-software-engineering/02-process/requirements.md)

## Essence

Security goals are usually stated as the CIA triad: **confidentiality** (information is disclosed only to those authorised), **integrity** (information and systems are changed only in authorised ways, and changes are detectable), and **availability** (authorised users can use the system when they need it). Goals alone are meaningless without an adversary, so a **threat model** states what the attacker wants, what they can do (read the network, run code on your machine, bribe an insider), and what you assume they cannot do. Threat modeling is the systematic process of listing assets, drawing trust boundaries, enumerating threats across those boundaries and deciding which to mitigate. Its value is that it converts "is this secure?" into questions that have answers.

## Core tenets

1. **"Secure" is meaningless without "against whom, protecting what".** A home router is secure against a casual neighbour and not against a state intelligence agency, and both statements can be true. A threat model makes the claim falsifiable: it names assets (customer data, signing keys, uptime), adversaries (their goals, resources, access and skill), and assumptions (the hardware is not backdoored, the administrator is honest). Most real breaches violate an assumption no one wrote down.

2. **The three goals conflict and must be balanced.** Encrypting everything and requiring several approvals improves confidentiality and integrity but harms availability; replicating data widely improves availability but multiplies the places it can leak. Denial of service is an availability attack that cryptography alone cannot stop. Treating the goals separately makes these trade-offs explicit.

3. **The triad is often extended because it misses things.** *Authenticity* (the data or party is who it claims to be) and *non-repudiation* (an author cannot later deny an action) are integrity of origin. *Accountability* (actions can be traced to a principal) needs authentication and audit logs. *Privacy* concerns whether data should be collected or used at all, not just who can read it, and is shaped by law as well as engineering.

4. **Trust boundaries are where threats live.** Draw the system as a data-flow diagram and mark every place where data crosses from a less trusted to a more trusted zone: from the internet to a web server, from a user process to the kernel, from a plug-in to its host. Every such crossing needs authentication of the source, validation of the data, and authorisation of the action. Bugs that let data cross a boundary unchecked (injection, deserialisation, confused deputy) are the most common vulnerability classes.

5. **Systematic enumeration beats brainstorming.** STRIDE (developed at Microsoft, 1999) checks each element of a data-flow diagram against six threat types: Spoofing (violates authenticity), Tampering (integrity), Repudiation (non-repudiation), Information disclosure (confidentiality), Denial of service (availability) and Elevation of privilege (authorisation). Attack trees (Schneier, 1999) decompose an attacker goal into alternative and combined sub-goals, which makes the cheapest attack path visible.

6. **Risk is likelihood times impact, and defence is economics.** No system can stop every threat, so each is ranked by how likely it is to be exploited and how much damage it would do, then mitigated, transferred (insurance), accepted or avoided (drop the feature). Attackers also act economically: raising the cost of the cheapest attack path above the value of the asset is often the realistic goal. The weakest link, not the strongest, sets the cost.

7. **The attacker chooses, so the defender must assume adaptivity.** Random failures follow distributions; attackers do not. They find the one input that triggers an edge case, wait for the moment a defence is down, and combine small weaknesses into a chain. So the right question is not "how likely is this input?" but "can an attacker produce it?", and security testing (fuzzing, penetration testing, red teams) plays the attacker's role deliberately.

8. **Insiders and the supply chain are part of the model.** Many serious incidents come from people with legitimate access or from compromised dependencies: a malicious library update, a tampered build server, a stolen developer credential. A model that only considers outside network attackers misses these, which is why principles such as separation of privilege and reproducible, verified builds exist.

## Key concepts

| Term | Meaning |
|---|---|
| Confidentiality | Information is disclosed only to authorised parties |
| Integrity | Data and systems change only in authorised, detectable ways |
| Availability | Authorised users can use the system when needed |
| Threat model | Statement of assets, adversaries, capabilities and assumptions |
| Trust boundary | Interface where data or control passes between trust levels |
| Attack surface | All points where an attacker can supply input or interact |
| STRIDE | Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege |
| Attack tree | Goal decomposed into alternative (OR) and combined (AND) attack steps |
| Risk | Likelihood of a threat being realised times its impact |
| Vulnerability / exploit | A weakness / a method that uses it to violate a security goal |

## How it fits

- **Below:** risk assessment applies [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) and [engineering trade-offs](../../00-engineering-foundations/05-engineering-method/tradeoffs-and-constraints.md); stating a threat model is like stating a [failure model](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md), with the Byzantine model as the adversarial case.
- **Above:** threat models become security [requirements](../../12-software-engineering/02-process/requirements.md); [privacy law](../../15-computing-in-context/law-privacy-and-policy.md) adds obligations that shape the model; [alignment and safety](../../13-artificial-intelligence/04-advanced-paradigms/alignment-and-safety.md) applies threat modeling to AI systems.
- **Siblings:** [design principles](security-design-principles.md) tell you how to build mitigations for the threats found here; [cryptography](../02-cryptography/foundations-of-modern-cryptography.md) formalises threat models as precise adversary games.

## Common misconceptions

- **"Security means confidentiality."** Integrity failures (tampered software updates, altered records) and availability failures (ransomware, denial of service) are often more damaging than leaks.
- **"We are too small to be a target."** Most attacks are automated and opportunistic; scanners probe every reachable address on the internet within hours.
- **"Threat modeling is a one-time document."** Every new feature, dependency or deployment changes the attack surface and the model.

## Go deeper

- Shostack, *Threat Modeling: Designing for Security* (2014): the practical method, including STRIDE.
- Anderson, *Security Engineering* (3rd ed., 2020): the field from the adversary's point of view.
- Schneier, "Attack Trees", *Dr. Dobb's Journal* (1999).
- Saltzer and Schroeder, "The Protection of Information in Computer Systems", *Proceedings of the IEEE* (1975): the original statement of goals and principles.
