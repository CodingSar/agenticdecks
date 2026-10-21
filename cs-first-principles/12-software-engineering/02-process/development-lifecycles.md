# Development Lifecycles

> **Layer:** [12 Software Engineering](../README.md) › [Process](README.md)
> **Builds on:** [Requirements](requirements.md), [Feedback and control](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md), [Latency, bandwidth and queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md)
> **Enables:** [Build and continuous delivery](../04-operations/build-and-continuous-delivery.md), [Version control](version-control.md), [Testing](../03-quality/testing.md)

## Essence

A development lifecycle is the order in which a team specifies, designs, builds, tests and releases software, and how often it repeats. The core variable is **the length of the feedback loop**: how long between making a decision and learning whether it was right. Plan-driven models (the "waterfall") do each activity once, in sequence, which suits work whose requirements are stable and whose mistakes are very costly to ship. Iterative and agile models repeat the whole cycle in short increments, which suits work where requirements are discovered by using the product. The history of software process since the 1970s is largely the shortening of that loop, from years to weeks to hours.

## Core tenets

1. **The waterfall was described as a risk, not a recommendation.** Winston Royce's 1970 paper "Managing the Development of Large Software Systems" presented the sequential diagram, said it "is risky and invites failure" because testing comes last, and recommended feedback between phases, prototyping ("do it twice") and customer involvement. Later standards adopted the diagram without the caveats.
2. **Sequential processes find requirement and design errors late.** If testing and user contact happen only at the end, a misunderstanding made in month one is discovered in month twelve, after much work depends on it. The cost of a mistake grows with the amount of work built on top of it, so long loops make mistakes expensive.
3. **Iteration manages risk by building the riskiest parts first.** Barry Boehm's spiral model ("A Spiral Model of Software Development and Enhancement", 1988) organises each cycle around identifying and reducing the largest remaining risk, by prototype, simulation or analysis. The cycle length then follows from how uncertain the work is.
4. **Agile methods make change cheap instead of preventing it.** The Agile Manifesto (2001) values working software, customer collaboration and responding to change. Extreme Programming (Beck, *Extreme Programming Explained*, 1999) supplied the engineering practices that make frequent change safe: automated tests, continuous integration, refactoring, small releases. Scrum supplies a management cadence (sprints of one to four weeks, review, retrospective). Without the engineering practices, the cadence alone tends to accumulate debt.
5. **Small batches shorten feedback and reduce risk.** By Little's law (average work in progress = arrival rate × time in system), a team with much unfinished work has long lead times. A small change is easy to review, test, understand and roll back; a large one is not. Continuous delivery (Humble and Farley, 2010) applies this to releases: every change that passes the pipeline is releasable.
6. **Speed and stability go together at the level of the whole process.** Forsgren, Humble and Kim (*Accelerate*, 2018), from several years of survey data, found that teams with high deployment frequency and short lead time also had lower change failure rates and faster recovery. Small, frequent, automated changes are both faster and safer than large, rare, manual ones.
7. **Plan-driven processes still fit some domains.** Where releases are physically or legally costly (flight software, medical devices, chips), more up-front specification, formal review and verification pay off, because a field fix may be impossible. Even there, iteration happens inside phases, through simulation and prototypes. The right loop length depends on the cost of a mistake reaching users.

## Key concepts

| Term | Meaning |
|---|---|
| Waterfall | A sequential lifecycle: requirements, design, implementation, verification, maintenance, each done once |
| Iterative development | Repeating the full cycle in increments, each producing working software |
| Spiral model | Boehm's risk-driven iterative model |
| Agile | A family of methods valuing short iterations, collaboration and adapting to change (Agile Manifesto, 2001) |
| Scrum | An agile framework with fixed-length sprints, a backlog and defined roles |
| Extreme Programming (XP) | An agile method centred on engineering practices: tests first, pairing, continuous integration |
| Lead time | Time from starting (or committing) a change to having it in production |
| Work in progress (WIP) | Work started but not finished; high WIP lengthens lead time |

## How it fits

- **Below:** a lifecycle is a [feedback control loop](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md) on the product: long delays in a feedback loop cause overshoot and oscillation, the same as in control systems. Lead time obeys the [queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) relation L = λW.
- **Above:** short lifecycles depend on [continuous delivery](../04-operations/build-and-continuous-delivery.md) and automated [testing](../03-quality/testing.md); production signals from [observability](../04-operations/observability.md) close the loop.
- **Siblings:** iteration revisits [requirements](requirements.md) each cycle; [version control](version-control.md) makes small, frequent changes cheap and reversible; [team structure](conways-law-and-teams.md) decides how many teams must coordinate per iteration.

## Common misconceptions

- **"Agile means no planning or documentation."** Agile methods plan continuously and at shorter horizons. They value working software *more than* comprehensive documentation, not instead of it.
- **"Moving fast means breaking things."** The evidence in *Accelerate* points the other way: the practices that enable speed (automation, small changes, fast recovery) also reduce failure.
- **"Waterfall is how engineering is done elsewhere, so software should copy it."** Other engineering fields iterate heavily in design (models, prototypes, simulation) and go sequential only for costly manufacture. Software's "manufacture" (build and copy) is nearly free.

## Go deeper

- Winston W. Royce, "Managing the Development of Large Software Systems" (1970): read what the waterfall paper actually says.
- Kent Beck, *Extreme Programming Explained* (1999): the engineering practices behind agile.
- Nicole Forsgren, Jez Humble and Gene Kim, *Accelerate* (2018): evidence on which practices predict delivery performance.
