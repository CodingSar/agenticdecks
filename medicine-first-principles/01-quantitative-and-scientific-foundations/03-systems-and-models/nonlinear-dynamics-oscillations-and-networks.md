# Nonlinear Dynamics, Oscillations and Networks

> **Layer:** [01 Quantitative and Scientific Foundations](../README.md) › [Systems and Models](README.md)
> **Builds on:** [Feedback and control](feedback-and-control.md), [Compartment models and exponential processes](compartment-models-and-exponential-processes.md)
> **Enables:** [Sleep and circadian rhythms](../../06-physiology/01-integrative-principles/sleep-and-circadian-rhythms.md), [Cardiac electrophysiology](../../06-physiology/03-cardiovascular-system/cardiac-electrophysiology.md), [Arrhythmias](../../12-organ-system-specialties/01-cardiology/arrhythmias.md), [Frailty, multimorbidity and polypharmacy](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md)

## Essence

Linear models, in which effects add and doubling the cause doubles the effect, describe the body well in small ranges and badly at the edges, where medicine does most of its work. Real physiological systems have thresholds, saturation, loops and many interacting parts, and from these come behaviours no linear model can show: sudden switches between states, self-sustaining rhythms, oscillations that are healthy or lethal depending on their pattern, and failures that spread through a network from one weak node. Nonlinear dynamics is the vocabulary for these behaviours (stable states, thresholds, limit cycles, bifurcations, synchrony) and network science is the vocabulary for how many parts connected together behave differently from any part alone. Together they explain why a heart beats, why it fibrillates, why an old person who tolerates each illness collapses under three at once, and why "a little more of a good thing" can be the step that tips a system over.

## Core tenets

1. **Nonlinearity means the response to a cause depends on the state the system is already in.** The same fall in oxygen barely changes saturation at the top of the haemoglobin curve and changes it steeply on the slope; the same stress is shrugged off at one point and provokes collapse at another. Superposition fails, so effects cannot be studied one at a time and added. This is the formal reason why drug interactions, multimorbidity and critical illness resist simple prediction.

2. **Stable states are attractors; recovery is a return to one, and disease can be another.** A system left alone settles into a state it returns to after small disturbances, like a ball in a valley. Health is such a state, made attracting by [feedback](feedback-and-control.md). Some disease states are also attractors: a vicious circle of heart failure (low output, fluid retention, higher filling pressure, worse output) or of obesity and insulin resistance holds the patient in a new valley, and treatment must push far enough to cross the ridge, not merely nudge toward health.

3. **Thresholds and bistability produce switches, and crossing them is abrupt and often irreversible.** Where positive feedback is bounded, a system has two stable states with a threshold between them. The action potential fires completely or not at all; a cell commits to division or death; a clot forms or does not; sepsis tips from a compensated inflammatory response to shock. Near a threshold small changes have large effects and noise alone can trigger the switch, so the moment to intervene is before it, when the system still looks stable.

4. **Sustained oscillations arise from feedback with delay or from mutually inhibiting elements; a limit cycle is a rhythm that restores itself.** A loop with enough gain and delay settles into a steady oscillation whose amplitude and period are properties of the system, not of what started it (a limit cycle). The sinoatrial node, the respiratory rhythm generator, the circadian clock (a transcription–translation loop with a ~24 h delay), the menstrual cycle and the pulsatile release of most hormones are limit cycles. Perturb the beat and it returns to its rhythm, which is what a pacemaker must be.

5. **Oscillators couple and synchronise, and the pattern of synchrony is itself a signal.** Cells that oscillate individually fall into step when connected: cardiac myocytes beat as one, neurons fire in rhythms seen on the electroencephalogram, the body's clocks follow the master clock in the hypothalamus, which follows light. Loss of synchrony is disease: atrial fibrillation is millions of cells oscillating out of step; jet lag and shift work are peripheral clocks out of phase with the master; a seizure is excessive synchrony across the cortex.

6. **Bifurcations are qualitative changes in behaviour at a critical parameter value, and most sudden clinical events are bifurcations.** As a parameter (potassium, conduction velocity, a drug level, a loop's gain) moves gradually, a system's behaviour can change discontinuously: a steady state becomes an oscillation, one rhythm becomes two, order becomes chaos. A slowly rising potassium produces nothing until the heart stops. The warning is rarely in the controlled variable; it is in the system's increasing slowness to recover from small perturbations (critical slowing down).

7. **Networks fail differently from chains: hubs, cascades and the loss of reserve.** The body's systems form a network in which organs, hormones and cells each have many connections. Such networks tolerate random loss of nodes but are vulnerable at hubs (the liver, the kidney, the hypothalamus), and a failure can cascade when one node's loss pushes neighbours past their thresholds: multi-organ failure in critical illness, a fall leading to a fracture leading to pneumonia leading to delirium in frailty. Frailty is a network whose redundancy has been spent, so that small insults propagate where once they were absorbed.

## Key concepts

| Term | Meaning |
|---|---|
| Nonlinearity | Output not proportional to input; effects do not add |
| Attractor (stable state) | A state a system returns to after small perturbations |
| Threshold | A boundary between states where a small change produces a qualitative switch |
| Bistability | Two stable states separated by a threshold; the basis of switches |
| Limit cycle | A self-sustaining oscillation with intrinsic amplitude and period |
| Synchronisation and entrainment | Coupled oscillators falling into step; an external rhythm setting the phase |
| Bifurcation | A qualitative change in behaviour as a parameter crosses a critical value |
| Critical slowing down | Lengthening recovery from perturbation as a system nears a bifurcation |
| Cascade | Failure spreading as each node's loss pushes neighbours past their thresholds |

## How it fits

- **Below:** this leaf begins where [feedback and control](feedback-and-control.md) and [compartment models](compartment-models-and-exponential-processes.md) stop: loops whose gain and delay make them oscillate, and rates that are not proportional to amounts.
- **Above:** [sleep and circadian rhythms](../../06-physiology/01-integrative-principles/sleep-and-circadian-rhythms.md), [cardiac electrophysiology](../../06-physiology/03-cardiovascular-system/cardiac-electrophysiology.md) and [control of breathing](../../06-physiology/04-respiratory-system/control-of-breathing.md) are limit cycles and coupled oscillators; [arrhythmias](../../12-organ-system-specialties/01-cardiology/arrhythmias.md) and [epilepsy](../../12-organ-system-specialties/10-neurology/epilepsy.md) are synchrony gone wrong; [sepsis and multi-organ failure](../../13-acute-perioperative-and-procedural-care/03-critical-care/sepsis-and-multi-organ-failure.md) and [frailty and multimorbidity](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md) are network cascades.
- **Siblings:** [information, signals and noise](information-signals-and-noise.md) treats a system's variability as signal rather than noise; [the scientific method](the-scientific-method-and-models.md) insists these models too are judged by prediction.

## Common misconceptions

- **"Gradual causes have gradual effects."** Near a threshold or bifurcation a gradual change produces a sudden event, and the controlled variable may show nothing until it does.
- **"If each disease is well treated, the patient is well treated."** In a depleted network, treatments interact and each additional drug or illness is a perturbation the whole can no longer absorb.

## Go deeper

- Steven H. Strogatz, *Nonlinear Dynamics and Chaos* (2nd ed., 2014): the standard introduction, with biological examples throughout.
- Leon Glass and Michael C. Mackey, *From Clocks to Chaos: The Rhythms of Life* (1988): oscillations and their pathologies in physiology.
- Steven H. Strogatz, *Sync* (2003): how oscillators synchronise, from heart cells to circadian clocks, for a general reader.
