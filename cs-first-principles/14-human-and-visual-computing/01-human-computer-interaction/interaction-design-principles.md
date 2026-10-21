# Interaction Design Principles

> **Layer:** [14 Human and Visual Computing](../README.md) › [Human-computer interaction](README.md)
> **Builds on:** [Perception and cognition](perception-and-cognition.md), [Abstraction and interfaces](../../12-software-engineering/01-design/abstraction-and-interfaces.md), [Feedback and control](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md)
> **Enables:** [Usability evaluation](usability-evaluation.md), [Web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md), [Ethics and professional responsibility](../../15-computing-in-context/ethics-and-professional-responsibility.md)

## Essence

Interaction design decides how people tell a computer what they want and how the computer shows what it did. A user starts with a goal, must translate it into actions the system accepts, and must interpret the system's response to judge whether the goal was met. Norman called the two gaps in this loop the **gulf of execution** and the **gulf of evaluation**; nearly every design principle exists to narrow one of them. Good interfaces make possible actions visible, give immediate feedback, behave consistently, match the user's mental model, and make errors hard to commit and easy to recover from. These are not matters of taste: they follow from the perceptual and cognitive limits described in [perception and cognition](perception-and-cognition.md).

## Core tenets

1. **Interaction is a feedback loop across two gulfs.** Execution: can the user figure out what to do? Evaluation: can the user tell what happened? A system that offers the right commands but no visible confirmation fails on evaluation; one that shows its state clearly but hides how to change it fails on execution. Diagnosing which gulf is wide is the first step in fixing a design.

2. **Make actions visible: affordances and signifiers.** An affordance is an action the object permits; a signifier is the perceptible cue that tells the user about it (a button's raised look, an underlined link). Hidden gestures and unlabelled icons have affordances but no signifiers, so users never find them. Because recognition is easier than recall, visible options beat memorised commands for occasional users.

3. **Give immediate, proportionate feedback.** Every action needs a response within perceptual budgets: under about 100 ms for direct manipulation, a progress indicator for anything over about a second. Without feedback, users repeat the action (double-submitting a payment) or assume failure.

4. **Direct manipulation shrinks both gulfs.** Shneiderman's direct manipulation means continuous representation of objects, physical actions (drag, pinch) instead of typed syntax, and rapid, reversible, immediately visible results. The Graphical User Interface (GUI) of the Xerox Alto (1973) and Apple Macintosh (1984) is its canonical form. It works because users act on what they see and see the result at once; it scales poorly to bulk or abstract operations, where scripts and commands win.

5. **Consistency lets knowledge transfer.** When the same action does the same thing everywhere, users learn it once. Platform conventions (where the close button is, what Ctrl-Z does) are an external consistency that design should not break without strong reason. Mappings should follow natural spatial or cultural correspondences: a control on the left affects the thing on the left.

6. **Design for error: prevent, then recover.** Humans make *slips* (right intention, wrong action) and *mistakes* (wrong intention from a wrong mental model). Constraints prevent slips (greying out invalid options, type-safe inputs), confirmations catch irreversible actions, and undo makes almost everything safe to try. Undo is the most powerful of these, because it turns exploration from risky to cheap.

7. **Defaults and friction shape behaviour.** Most users keep defaults, so the default is the decision for most people. Friction placed deliberately (confirming a deletion) protects; friction placed to discourage cancelling a subscription or to push sharing of personal data ("dark patterns") manipulates. Interface design is therefore an ethical and, increasingly, a regulatory matter.

8. **Accessibility is design for the full range of humans.** Users differ in vision, hearing, motor control and cognition, permanently or situationally (bright sunlight, one hand busy). Semantic structure readable by screen readers, keyboard operability, sufficient contrast and captions follow the Web Content Accessibility Guidelines (WCAG). Accessible designs usually improve usability for everyone.

9. **Language interfaces reopen the gulf of execution in a new form.** Conversational interfaces built on large language models, common as of the mid-2020s, remove the need to learn syntax, but users cannot see what the system can do or reliably predict its output. Showing capabilities, confidence and sources, and keeping humans in control of consequential actions, are the design responses.

## Key concepts

| Term | Meaning |
|---|---|
| Gulf of execution | Gap between a user's goal and the actions the system requires |
| Gulf of evaluation | Gap between the system's state and the user's ability to perceive and interpret it |
| Affordance | Action an object makes possible for a given user |
| Signifier | Perceptible cue indicating where and how to act |
| Mapping | Relationship between controls and their effects |
| Direct manipulation | Acting on visible objects with immediate, reversible feedback |
| Slip / mistake | Execution error with a correct goal / error from a wrong goal or model |
| Dark pattern | Interface design that steers users against their own interests |
| Accessibility | Usability by people with the full range of abilities |

## How it fits

- **Below:** Principles derive from [perception and cognition](perception-and-cognition.md); the interface is an [abstraction](../../12-software-engineering/01-design/abstraction-and-interfaces.md) over the system's internals; the interaction loop is a human-in-the-loop [feedback system](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md); response-time goals depend on [operating-system scheduling](../../07-operating-systems/02-process-management/scheduling.md) and [network latency](../../08-networking/01-principles/latency-bandwidth-and-queueing.md).
- **Above:** Security warnings, phishing resistance and [authentication](../../11-security-and-cryptography/04-network-and-application-security/authentication.md) flows succeed or fail on interaction design; dark patterns and accessibility are topics of [ethics](../../15-computing-in-context/ethics-and-professional-responsibility.md) and [law](../../15-computing-in-context/law-privacy-and-policy.md).
- **Siblings:** [Perception and cognition](perception-and-cognition.md) supplies the limits these principles respect; [usability evaluation](usability-evaluation.md) tests whether a design actually follows them for real users; [information visualization](information-visualization.md) applies direct manipulation and feedback to exploring data (overview, zoom, filter, details on demand).

## Common misconceptions

- **"Good design is about how it looks."** Visual polish helps, but most usability failures are in structure, feedback and mapping, not appearance.
- **"Users who make errors are careless."** Repeated errors at the same place are evidence of a design problem; blaming users hides it.
- **"Natural-language interfaces need no design."** They move the design problem to discoverability, trust calibration and error recovery.

## Go deeper

- Don Norman, *The Design of Everyday Things* (revised ed., 2013): the gulfs, affordances, signifiers and error.
- Ben Shneiderman et al., *Designing the User Interface* (6th ed., 2016): direct manipulation and interface guidelines.
- Jakob Nielsen, *Usability Engineering* (1993): response-time limits and practical heuristics.
