# Usability Evaluation

> **Layer:** [14 Human and Visual Computing](../README.md) › [Human-computer interaction](README.md)
> **Builds on:** [Statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md), [Interaction design principles](interaction-design-principles.md), [Measurement and modeling](../../00-engineering-foundations/05-engineering-method/measurement-and-modeling.md)
> **Enables:** [Requirements](../../12-software-engineering/02-process/requirements.md), [Development lifecycles](../../12-software-engineering/02-process/development-lifecycles.md), [Evaluation and experimentation](../../13-artificial-intelligence/02-machine-learning-foundations/evaluation-and-experimentation.md)

## Essence

Designers cannot judge the usability of their own work: they know how it is supposed to work, so they cannot see it as a newcomer does. Usability evaluation replaces opinion with evidence by observing or measuring real users doing real tasks. Usability itself is defined operationally (by International Organization for Standardization (ISO) standard 9241-11) as the effectiveness, efficiency and satisfaction with which specified users achieve specified goals in a specified context. Methods range from cheap expert inspections to qualitative think-aloud studies that find problems, to controlled experiments and live A/B tests that measure effects. The core principle is iterative: test early and often, because problems found in a sketch cost minutes to fix and problems found after launch cost far more.

## Core tenets

1. **You are not the user.** Expertise in a system blinds you to what newcomers find confusing; this "curse of knowledge" is why internal reviews pass designs that users fail. The only reliable corrective is watching people who match the target users attempt representative tasks without help.

2. **Usability is measured on tasks, not opinions.** The standard measures are effectiveness (task success rate, errors), efficiency (time on task, number of actions) and satisfaction (questionnaires such as the System Usability Scale (SUS), a 10-item instrument scored 0–100). What users say they prefer and how well they perform often disagree, so measure both and trust behaviour for performance claims.

3. **Formative and summative evaluation answer different questions.** Formative studies, run during design, aim to *find* problems and explain why they occur; small samples and qualitative observation suffice. Summative studies, run on a finished design, aim to *measure* performance or compare alternatives; they need larger samples and statistics. Confusing the two leads either to under-powered comparisons or to over-engineered problem-finding.

4. **Small qualitative tests find most problems cheaply.** Nielsen and Landauer's model suggests that about five users find roughly 85% of the problems that a given task set and user group expose, because common problems recur quickly (the model assumes each user reveals about 31% of the problems, an average across their projects). The point is not that five is always enough, but that several small rounds of testing and fixing beat one large study. Different user groups and tasks need their own rounds.

5. **Think-aloud reveals the mental model.** Asking participants to verbalise while they work exposes what they expected, where they looked and why they chose an action. It turns an observed error into an explanation of which gulf, execution or evaluation, caused it. The facilitator must not lead or help, or the data reflects the facilitator's model.

6. **Inspection methods are cheap filters, not substitutes.** Heuristic evaluation has a few experts check a design against principles such as Nielsen's ten heuristics; cognitive walkthroughs step through a task asking whether a new user would know what to do. They catch many obvious problems before users see them, but they miss problems specific to real users' knowledge and produce some false alarms.

7. **Controlled experiments and A/B tests measure causal effects.** To claim design A is faster than B, randomise participants (or live traffic) between conditions, control confounds, and test for statistical significance with adequate power. Within-subject designs need counterbalancing for learning effects. Large online A/B tests detect small effects reliably, but only on the metric measured, which may not be the outcome that matters (clicks are not satisfaction).

8. **Context changes everything.** Lab studies remove interruptions, real data and real stakes. Field studies, diary studies and analytics on deployed systems reveal problems a lab cannot, at the cost of control. Mature practice combines both.

## Key concepts

| Term | Meaning |
|---|---|
| Usability | Effectiveness, efficiency and satisfaction for specified users, goals and context |
| Task success rate | Fraction of attempts in which users complete the task correctly |
| Time on task | Time a user takes to complete a task |
| SUS | Standard 10-item usability questionnaire scored 0–100 |
| Formative evaluation | Testing during design to find and understand problems |
| Summative evaluation | Testing a finished design to measure or compare |
| Think-aloud protocol | Participants verbalise their thoughts while performing tasks |
| Heuristic evaluation | Expert inspection against a list of usability principles |
| A/B test | Randomised comparison of two variants with live users |

## How it fits

- **Below:** Experimental design, significance and power come from [statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md); the discipline of controlled measurement from [engineering method](../../00-engineering-foundations/05-engineering-method/measurement-and-modeling.md).
- **Above:** Findings feed [requirements](../../12-software-engineering/02-process/requirements.md) and iterative [development lifecycles](../../12-software-engineering/02-process/development-lifecycles.md); production analytics connect to [observability](../../12-software-engineering/04-operations/observability.md). Evaluating Artificial Intelligence (AI) systems with people, such as whether users over-trust model advice, extends [machine-learning evaluation](../../13-artificial-intelligence/02-machine-learning-foundations/evaluation-and-experimentation.md).
- **Siblings:** [Interaction design principles](interaction-design-principles.md) generate hypotheses; [perception and cognition](perception-and-cognition.md) explain observed failures; evaluation decides which designs survive, including whether an [information visualization](information-visualization.md) lets readers find the intended insight.

## Common misconceptions

- **"Five users are enough for any study."** Five is a rule of thumb for finding common problems in one formative round, not for measuring or comparing designs.
- **"Ask users what they want."** Users are good at reporting problems they experienced and poor at predicting what they would use; observe behaviour.
- **"Usability testing happens at the end."** Late testing finds problems when they are most expensive to fix; paper prototypes can be tested on day one.

## Go deeper

- Jakob Nielsen, *Usability Engineering* (1993): the discount usability approach and heuristics.
- Steve Krug, *Don't Make Me Think* (3rd ed., 2014): short, practical guide to lightweight testing.
- Jonathan Lazar, Jinjuan Heidi Feng and Harry Hochheiser, *Research Methods in Human-Computer Interaction* (2nd ed., 2017): experimental design and statistics for interaction research.
