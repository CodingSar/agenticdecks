# Human-Computer Interaction

> **Layer:** [14 Human and Visual Computing](../README.md) › Human-computer interaction
> **Children:** [Perception and cognition](perception-and-cognition.md) · [Interaction design principles](interaction-design-principles.md) · [Usability evaluation](usability-evaluation.md)

## What this area is about

Human-Computer Interaction (HCI) studies the boundary where a person and a computer exchange intent and information. The question it answers is: how do we build systems that people can actually use to reach their goals, quickly, correctly and without frustration? Its unifying idea is that the human is part of the system. A computer that is correct in isolation but invites the user to make errors, hides its state, or responds too slowly is a system that fails. HCI therefore treats human perception, memory, attention and motor control as engineering constraints with known magnitudes, just as architecture treats signal delay or memory bandwidth.

HCI is also an empirical discipline. Because human behaviour cannot be derived from first principles alone, its claims are tested by observing people, and its designs improve through iterative cycles of building, testing and revising.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Perception and cognition](perception-and-cognition.md) | The human "hardware specification": vision, colour, timing, memory, attention, movement | Signals, information theory |
| [Interaction design principles](interaction-design-principles.md) | Rules for shaping the interaction loop so the human side succeeds | Perception and cognition |
| [Usability evaluation](usability-evaluation.md) | Methods for measuring whether a design works for real users | Statistics; design principles |

```
     perception & cognition  --constrains-->  interaction design
               ^                                      |
               |                                      v
               +------ explains failures ----- usability evaluation
                                                      |
                                    redesign <--------+   (iterate)
```

Read perception and cognition first: it gives the numbers (100 ms feels instant, about four chunks of working memory, Fitts's law) that the design principles rely on. Interaction design turns those constraints into guidance: visibility, feedback, consistency, error prevention and recovery. Usability evaluation closes the loop: designs are hypotheses about human behaviour, and evaluation tests them. The three form a cycle rather than a stack.

## Connections to sibling areas

- **[Computer graphics](../02-computer-graphics/README.md):** Graphics produces the pixels that interfaces are made of, and its performance targets (frame rate, latency, colour accuracy) come from human perception. Interactive 3D, games and virtual reality are where HCI and graphics overlap most, and where perceptual shortcuts such as foveated rendering save the most work.
- **[Media and vision](../03-media-and-vision/README.md):** Perceptual codecs are designed around the same visual and auditory limits HCI studies. Computer vision lets interfaces perceive users in turn, through gesture, gaze, face and handwriting recognition.

## Connections across layers

HCI builds on [signals and systems](../../00-engineering-foundations/04-signals-and-systems/README.md) and [statistics](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md) from the bottom of the stack. Its latency budgets propagate downward into [operating-system scheduling](../../07-operating-systems/02-process-management/scheduling.md), [networking](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) and [content delivery](../../08-networking/05-application-layer/content-delivery-and-caching.md). It shares methods with [software engineering](../../12-software-engineering/02-process/README.md) (requirements, iterative development) and with [security](../../11-security-and-cryptography/04-network-and-application-security/authentication.md), where usable authentication and warnings decide real-world safety. As of the mid-2020s, [large language models](../../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md) are changing the dominant interaction style toward conversation. Dark patterns and accessibility connect to [ethics](../../15-computing-in-context/ethics-and-professional-responsibility.md) and [law](../../15-computing-in-context/law-privacy-and-policy.md).

## Cross-cutting threads

- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): the user interface is the topmost abstraction, hiding the whole stack behind a mental model.
- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): interaction is a human-in-the-loop control cycle of action and evaluation.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): perceptual and cognitive limits are fixed constraints design must respect.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): learnability versus efficiency; command lines versus menus; friction versus safety.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): usability evaluation checks designs against real behaviour rather than designer intuition.
