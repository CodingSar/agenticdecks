# Ethics and Professional Responsibility

> **Layer:** [15 Computing in Context](README.md)
> **Builds on:** [History of computing](history-of-computing.md), [Reliability engineering](../12-software-engineering/04-operations/reliability-engineering.md), [Generalization and bias-variance](../13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md), [CIA and threat modeling](../11-security-and-cryptography/01-security-principles/cia-and-threat-modeling.md)
> **Enables:** [Law, privacy and policy](law-privacy-and-policy.md), [Requirements](../12-software-engineering/02-process/requirements.md), [Alignment and safety](../13-artificial-intelligence/04-advanced-paradigms/alignment-and-safety.md)

## Essence

Computing professionals build systems that act on people who never agreed to the design and often cannot see it. Ethics is the discipline of asking, before and during building, who is affected, how they could be harmed, and what the builder owes them. The Association for Computing Machinery (ACM) Code of Ethics and Professional Conduct (revised 2018) puts it first: computing professionals should "contribute to society and to human well-being" and "avoid harm", with the public good as the primary consideration. The field's characteristic problems come from scale (one decision copied to millions of users), opacity (harms hidden behind abstraction layers) and diffuse responsibility (many people each building a small part). Professional responsibility means doing the technical work competently and owning its foreseeable effects.

## Core tenets

1. **Software can kill, and the causes are usually systemic.** The Therac-25 radiation therapy machine gave six known massive overdoses between 1985 and 1987, several fatal. Leveson and Turner's investigation ("An Investigation of the Therac-25 Accidents", 1993) found a race condition, but also removed hardware interlocks, overconfidence in software, cryptic error messages operators learned to ignore, and poor incident reporting. The lesson is that safety is a property of the whole system and organisation, not of code alone.
2. **Professional codes state concrete duties.** The ACM Code (2018) has general principles (contribute to well-being, avoid harm, be honest, be fair and do not discriminate, respect creative work, respect privacy, honour confidentiality), professional responsibilities (high-quality work, competence, knowing and respecting the rules, accepting review, thorough evaluation of systems and their risks), and leadership duties. The joint Institute of Electrical and Electronics Engineers (IEEE) Computer Society and ACM Software Engineering Code (1999) puts the public interest first. Such codes give engineers grounds to refuse unsafe or deceptive work.
3. **Responsibility diffuses across many hands, so it must be assigned deliberately.** Helen Nissenbaum ("Accountability in a Computerized Society", 1996) named the barriers: many hands contribute, bugs are treated as inevitable, the computer is blamed, and owners disclaim liability. Each engineer can truthfully say their part was fine. Countering this takes explicit ownership, safety cases, review and postmortems that follow causes across team boundaries.
4. **Neutral-looking systems can encode bias.** A model trained on historical decisions learns their patterns, including discrimination; a proxy such as postcode can stand in for a protected attribute. In 2016 ProPublica reported that the COMPAS recidivism score had higher false-positive rates for Black defendants, while its vendor showed it was equally calibrated across groups. Both were true, and Kleinberg, Mullainathan and Raghavan (2016) and Chouldechova (2017) proved that when base rates differ, calibration and equal error rates cannot generally hold at once. Fairness requires choosing which criterion matters, which is an ethical choice, not a technical one.
5. **Foreseeable misuse and dual use are part of the design.** A face recogniser, a location Application Programming Interface (API) or a text generator built for one purpose can serve stalking, surveillance or fraud. Threat modeling, normally used against attackers ([CIA and threat modeling](../11-security-and-cryptography/01-security-principles/cia-and-threat-modeling.md)), applies equally to foreseeable abuse by users and operators. Designers should ask who could be harmed if the system works exactly as built.
6. **Values can be designed in, not only argued about.** Value Sensitive Design (Friedman and colleagues, from the 1990s) identifies direct and indirect stakeholders and the values at stake, then treats them as requirements to trade off like any other. Privacy by design, accessibility and meaningful consent are examples of values turned into engineering constraints.
7. **Ethics often has to act before the evidence is in.** David Collingridge (*The Social Control of Technology*, 1980) described the dilemma: early on, a technology is easy to change but its effects are unknown; once effects are known, it is entrenched. This argues for impact assessment, staged deployment with monitoring, and reversibility, the same habits as [reliability engineering](../12-software-engineering/04-operations/reliability-engineering.md).
8. **Speaking up is part of the job.** Engineers often know about risks before anyone else. The ACM Code asks members to report signs of risk and to avoid harm even under pressure. Cases such as the Volkswagen emissions "defeat device" software (revealed 2015), where engineers implemented deliberate deception, show the cost when that duty fails.

## Key concepts

| Term | Meaning |
|---|---|
| Problem of many hands | Harm results from many contributions, so no single person seems responsible |
| Algorithmic bias | Systematic unfair outcomes for groups, arising from data, objectives or deployment |
| Calibration | Among people given score s, the outcome rate equals s, in each group |
| Error-rate balance | Equal false-positive and false-negative rates across groups |
| Dual use | A technology that serves both beneficial and harmful purposes |
| Value Sensitive Design | A method that treats human values as explicit design requirements |
| Collingridge dilemma | Technologies are easiest to control when their effects are least known |

## How it fits

- **Below:** the harms come from every layer: [model generalization](../13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md) and [evaluation](../13-artificial-intelligence/02-machine-learning-foundations/evaluation-and-experimentation.md) choices create bias; [concurrency bugs](../07-operating-systems/03-concurrency/race-conditions-and-critical-sections.md) killed Therac-25 patients; [interaction design](../14-human-and-visual-computing/01-human-computer-interaction/interaction-design-principles.md) can manipulate. Engineering practice from [layer 12](../12-software-engineering/README.md) supplies the tools for acting on ethical duties.
- **Above:** nothing sits above this layer; ethics feeds back down as [requirements](../12-software-engineering/02-process/requirements.md) and constraints.
- **Siblings:** [history](history-of-computing.md) supplies the cases; [law and policy](law-privacy-and-policy.md) makes some duties enforceable, though it covers less than ethics and lags it; [environmental impact](environmental-impact.md) extends harm to energy, carbon and e-waste borne by people far from the system.

## Common misconceptions

- **"Technology is neutral; only its uses are good or bad."** Design decides which uses are easy, which are hard and who bears the risk. Defaults, in particular, shape behaviour at scale.
- **"If it's legal, it's ethical."** Law sets a floor, and in fast-moving areas it often does not yet address the harm at all.
- **"Removing the protected attribute removes bias."** Correlated features carry the same information, and removing the attribute can make bias harder to measure and correct.

## Go deeper

- ACM, *ACM Code of Ethics and Professional Conduct* (2018): short, concrete, and the field's reference point.
- Nancy G. Leveson and Clark S. Turner, "An Investigation of the Therac-25 Accidents", *IEEE Computer* (1993): the classic software-safety case study.
- Solon Barocas, Moritz Hardt and Arvind Narayanan, *Fairness and Machine Learning: Limitations and Opportunities* (2023): fairness criteria and their trade-offs, rigorously.
