# Systems and Models

> **Layer:** [01 Quantitative and Scientific Foundations](../README.md) › Systems and Models
> **Children:** [The scientific method and models](the-scientific-method-and-models.md) · [Feedback and control](feedback-and-control.md) · [Compartment models and exponential processes](compartment-models-and-exponential-processes.md) · [Nonlinear dynamics, oscillations and networks](nonlinear-dynamics-oscillations-and-networks.md) · [Information, signals and noise](information-signals-and-noise.md)

## What this area is about

The body is a system: many parts, connected, exchanging substance and signal, holding itself steady and changing over time. This area answers: *what general patterns does any such system show, independent of what it is made of, and how does one build and judge a model of it?* The patterns are few, and they recur at every scale from a receptor to a health service: a pool filling and draining, a loop opposing change, a threshold being crossed, a rhythm sustaining itself, a message surviving noise. A reader who knows them sees drug dosing, homeostasis, epidemics, arrhythmias and diagnostic testing as five instances of four or five ideas.

The unifying idea is **dynamics: how a quantity changes over time depends on the state of the system, and the rules of that dependence are shared across substrates**. The scientific method leaf states what a model is and why it must predict something checkable. The remaining four are the four model families medicine uses most: compartment models for amounts moving between pools, feedback for regulated variables, nonlinear dynamics for thresholds, rhythms and cascades, and information theory for signals in noise.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [The scientific method and models](the-scientific-method-and-models.md) | What a model is, falsifiability, controls, replication, levels of description | [Probability](../01-probability-and-measurement/probability.md), [measurement](../01-probability-and-measurement/measurement-error-and-biological-variation.md) |
| [Compartment models and exponential processes](compartment-models-and-exponential-processes.md) | Pools and flows: first- and zero-order kinetics, half-life, clearance, steady state, exponential growth | Scientific method, probability |
| [Feedback and control](feedback-and-control.md) | Regulated variables: set point, gain, delay, oscillation, compensation, positive feedback | Scientific method, compartments |
| [Nonlinear dynamics, oscillations and networks](nonlinear-dynamics-oscillations-and-networks.md) | Thresholds, attractors, limit cycles, synchrony, bifurcations, cascades | Feedback, compartments |
| [Information, signals and noise](information-signals-and-noise.md) | Messages in noisy channels: bits, signal-to-noise, encoding, detection thresholds, bandwidth | Probability, distributions, measurement |

```
   the scientific method and models  (what a model is; how it is judged)
            │
            ├──► compartment models ──► feedback & control ──► nonlinear dynamics
            │    (pools, exponentials)   (loops, set points)    (thresholds, rhythms, networks)
            │
            └──► information, signals & noise  (what a measurement or message can tell)
```

Read the scientific method first; it is the frame for all the others. Then compartments, because the exponential approach to steady state is the simplest dynamic and the one feedback modifies. Feedback adds a controller and introduces gain, delay and compensation; nonlinear dynamics is what feedback becomes when gain is high, thresholds are present or many loops interact. Information, signals and noise can be read at any point after the probability leaves, and is the bridge from this area back to measurement and Bayesian reasoning: a test is a noisy channel and a diagnosis is a detection decision.

## Connections to sibling areas

- **[Probability and measurement](../01-probability-and-measurement/README.md):** noise in a signal is measurement error from the sender's side; the receiver operating characteristic curve of signal detection is the sensitivity–specificity curve of a test; the exponential arises because each molecule leaves a compartment with a fixed probability per unit time.
- **[Inference and causation](../02-inference-and-causation/README.md):** the scientific method leaf is the philosophy behind hypothesis testing and causal inference; constant hazard in survival analysis is a first-order compartment; nonlinear dynamics is the warning that a regression coefficient estimated in one state of a system may not predict the effect of intervening on it.

## Connections across layers

This area has nothing beneath it. [00 Physical and Chemical Foundations](../../00-physical-and-chemical-foundations/README.md) uses exponential decay for radioactivity, chemical kinetics and the nerve's cable, and signal-and-noise ideas for imaging and molecular recognition. [02 Biochemistry](../../02-biochemistry-and-molecular-biology/README.md) describes signalling cascades as amplification, feedback inhibition of pathways and bistable switches. [06 Physiology](../../06-physiology/README.md) is the largest consumer: homeostasis is feedback, hormone axes are nested loops, the heartbeat, breathing and circadian clock are limit cycles, sensory coding is information theory. [08 Pathology](../../08-pathology/README.md) describes compensation and decompensation, vicious circles and the cascade of shock. [09 Pharmacology](../../09-pharmacology-and-therapeutics/README.md) rests on compartment models for every dosing decision. [10 Epidemiology](../../10-epidemiology-and-evidence/README.md) models epidemics as compartments and judges evidence by the scientific method. [11 Clinical Method](../../11-clinical-method-and-diagnostics/README.md) reads electrical and imaging signals from noise. [12](../../12-organ-system-specialties/README.md), [13](../../13-acute-perioperative-and-procedural-care/README.md) and [14](../../14-life-course-mind-and-integrative-care/README.md) meet arrhythmias, multi-organ failure and frailty, each a nonlinear or network failure.

## Cross-cutting threads

- [Feedback and homeostasis](../../CROSS-CUTTING.md#feedback-and-homeostasis): stated here as mathematics before physiology instantiates it.
- [Compensation and decompensation](../../CROSS-CUTTING.md#compensation-and-decompensation): a loop hides the disturbance until its effector saturates; a network absorbs insults until its reserve is spent.
- [Time-courses](../../CROSS-CUTTING.md#time-courses): half-life, time to steady state, doubling time and delay are the units of tempo.
- [Signalling and information](../../CROSS-CUTTING.md#signalling-and-information): encoding, noise, redundancy and detection thresholds.
- [Cause and mechanism](../../CROSS-CUTTING.md#cause-and-mechanism): a model is a mechanism stated precisely enough to fail.
- [Redundancy and reserve](../../CROSS-CUTTING.md#redundancy-and-reserve): redundancy in codes and networks is what makes one failure survivable.
