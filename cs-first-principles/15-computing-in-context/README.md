# 15 Computing in Context

> **Layer:** 15 Computing in Context
> **Children:** [History of computing](history-of-computing.md) · [Ethics and professional responsibility](ethics-and-professional-responsibility.md) · [Law, privacy and policy](law-privacy-and-policy.md)

## What this area is about

Every layer below this one asks how to make computation correct, fast, reliable or useful. This layer asks what computation does to the people and societies that build and use it, and what they in turn do to it. It is the top of the stack because it is where all the technical layers meet the world at once: a single product decision can involve energy use in [silicon](../00-engineering-foundations/README.md), surveillance through [networks](../08-networking/README.md), bias in [Artificial Intelligence (AI) and machine learning](../13-artificial-intelligence/README.md) and liability in [software engineering](../12-software-engineering/README.md).

The unifying idea is that **technical choices are also social choices**. An encryption default, a data-retention period, a ranking objective or a recommendation threshold decides who benefits, who bears the risk and who decides. Lawrence Lessig put it as "code is law" (*Code and Other Laws of Cyberspace*, 1999): the architecture of a system regulates behaviour as surely as statutes do, but without public debate unless engineers bring it. The three children look at this from three angles: how we got here (history), what engineers owe others (ethics), and what society requires of systems (law and policy).

## Why this layer sits here

This layer depends on every other layer, because each one raises its own societal questions:

| Layer | Societal question it raises |
|---|---|
| [00 Engineering foundations](../00-engineering-foundations/README.md) | Energy use of data centres and chips, mining of materials, e-waste from short device lifetimes |
| [02 Theory of computation](../02-theory-of-computation/README.md) | Limits of automated verification, so who is accountable when software cannot be proven safe |
| [05 Algorithms](../05-algorithms-and-data-structures/README.md) | Ranking, matching and allocation algorithms that decide access to jobs, housing and information |
| [07 Operating systems](../07-operating-systems/README.md) | Platform control: who may install software on a device they own |
| [08 Networking](../08-networking/README.md) | Net neutrality, censorship and shutdowns, the digital divide in access |
| [09 Data management](../09-data-management/README.md) | Collection, retention and the right to erasure; what may be linked to whom |
| [11 Security and cryptography](../11-security-and-cryptography/README.md) | Surveillance, lawful access to encrypted data, vulnerability disclosure, cybercrime law |
| [12 Software engineering](../12-software-engineering/README.md) | Liability for defects, safety-critical certification, professional licensing |
| [13 Artificial intelligence](../13-artificial-intelligence/README.md) | Bias and fairness, explanation of automated decisions, copyright of training data, safety of capable systems |
| [14 Human and visual computing](../14-human-and-visual-computing/README.md) | Accessibility, manipulative "dark pattern" interfaces, synthetic media and deepfakes |

What the layer contributes back to the stack is a set of **constraints and values** that become requirements: privacy by design, accessibility, safety cases, fairness metrics, audit logs. Unlike technical constraints, these are contested and change with time and jurisdiction.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [History of computing](history-of-computing.md) | Explains why the stack has its current shape and which forces (war, markets, physics, research funding) shaped it | All technical layers |
| [Ethics and professional responsibility](ethics-and-professional-responsibility.md) | States what engineers owe users, the public and each other, and how to reason about harm | History (case studies), all layers (the harms) |
| [Law, privacy and policy](law-privacy-and-policy.md) | Describes how societies turn some ethical expectations into enforceable rules | Ethics (the values), history (how rules lagged technology) |

Read history first. It shows that today's architecture was not inevitable: the stored-program design, the end-to-end Internet and the dominance of a few platforms were choices made under particular pressures. Ethics then asks what responsibilities follow from the power those choices created, using cases such as the Therac-25 radiation overdoses. Law and policy show how some of those responsibilities become binding, through data-protection law such as the General Data Protection Regulation (GDPR), intellectual-property law and sector regulation, and why law tends to lag the technology it regulates.

## Connections to neighbouring layers

- **[12 Software Engineering](../12-software-engineering/README.md):** professional responsibility is the ethical side of engineering practice; legal requirements arrive through [requirements engineering](../12-software-engineering/02-process/requirements.md); postmortems and safety cases are accountability tools.
- **[13 Artificial Intelligence](../13-artificial-intelligence/README.md):** the most active area of ethics and regulation today, from fairness in [supervised learning](../13-artificial-intelligence/02-machine-learning-foundations/supervised-learning.md) to [alignment and safety](../13-artificial-intelligence/04-advanced-paradigms/alignment-and-safety.md) and the European Union (EU) AI Act.
- **[11 Security and Cryptography](../11-security-and-cryptography/README.md):** cryptography sits at the centre of conflicts between privacy and state access; security failures become data breaches with legal duties to notify.
- **[14 Human and Visual Computing](../14-human-and-visual-computing/README.md):** [interaction design](../14-human-and-visual-computing/01-human-computer-interaction/interaction-design-principles.md) can respect or exploit [human cognition](../14-human-and-visual-computing/01-human-computer-interaction/perception-and-cognition.md); accessibility is both an ethical and a legal requirement.
- **[09 Data Management](../09-data-management/README.md):** most privacy law is in effect law about databases: what may be stored, for how long, linked to what, and deleted when.
- **[08 Networking](../08-networking/README.md):** the [end-to-end design](../08-networking/01-principles/layering-and-the-end-to-end-principle.md) of the Internet made it open to innovation and hard to control, which underlies debates on neutrality and censorship.
- **[00 Engineering Foundations](../00-engineering-foundations/README.md):** the [thermodynamics](../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md) of computation becomes a climate question at data-centre scale.

## Connections across layers

This layer takes facts from every layer and gives back values and rules. The flow is two-way: [history](history-of-computing.md) shows that funding and regulation shaped technical directions (military funding of early computers and the Advanced Research Projects Agency Network (ARPANET); antitrust cases shaping the software industry), and technical affordances shape what laws can enforce (end-to-end encryption limits lawful interception).

## Cross-cutting threads

- [Tradeoffs](../CROSS-CUTTING.md#tradeoffs): privacy versus utility, security versus access, innovation versus precaution.
- [Trust and verification](../CROSS-CUTTING.md#trust-and-verification): audits, certification and transparency reports as social verification of systems.
- [Limits and impossibility](../CROSS-CUTTING.md#limits-and-impossibility): fairness criteria that cannot all hold at once; anonymisation that cannot fully protect rich data.
- [Abstraction and layering](../CROSS-CUTTING.md#abstraction-and-layering): abstraction hides harms as well as details, spreading responsibility across many hands.
- [Feedback and control](../CROSS-CUTTING.md#feedback-and-control): regulation and public response act as a slow feedback loop on technology.
