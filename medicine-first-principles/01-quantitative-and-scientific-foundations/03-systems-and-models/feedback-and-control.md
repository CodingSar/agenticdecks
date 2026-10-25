# Feedback and Control

> **Layer:** [01 Quantitative and Scientific Foundations](../README.md) › [Systems and Models](README.md)
> **Builds on:** [The scientific method and models](the-scientific-method-and-models.md), [Compartment models and exponential processes](compartment-models-and-exponential-processes.md)
> **Enables:** [Homeostasis and set points](../../06-physiology/01-integrative-principles/homeostasis-and-set-points.md), [Hormone classes, axes and feedback](../../06-physiology/07-endocrine-system/hormone-classes-axes-and-feedback.md), [Haemodynamics and blood pressure regulation](../../06-physiology/03-cardiovascular-system/hemodynamics-and-blood-pressure-regulation.md), [Compensation and decompensation](../../08-pathology/02-hemodynamic-disorders/hemorrhage-shock-and-sepsis.md)

## Essence

A body keeps its temperature, blood pressure, glucose, pH and a hundred other variables within narrow limits while the world outside and the demands inside change constantly. It does this not by being rigid but by measuring each variable, comparing it with a set point and adjusting an input to oppose any deviation: negative feedback. Control theory is the mathematics of such loops, and it explains their shared properties whether the loop is a thermostat, a hormone axis or a clinician titrating a drug: a loop reduces but does not abolish disturbance; its gain decides how tightly it holds the variable; delay makes it oscillate; and a loop that is working hides the disturbance it is correcting until it can correct no further. Positive feedback, in which deviation feeds deviation, is used by the body for switches (clotting, labour, the action potential) and is the shape of most catastrophes.

## Core tenets

1. **Negative feedback opposes deviation from a set point.** A sensor measures the controlled variable, a comparator subtracts it from the set point, and an effector acts on the system in the direction that reduces the error. A fall in blood pressure is sensed by baroreceptors, which raise sympathetic output, which raises heart rate and vascular tone, which raises pressure. The sign is what matters: the response must oppose the change, and a loop with the wrong sign runs away.

   ```
   set point ──►(compare)──► controller ──► effector ──► system ──► output
                   ▲                                                 │
                   └──────────────── sensor ◄────────────────────────┘
   ```

2. **A feedback loop reduces a disturbance by a factor of (1 + gain), never to zero.** If a disturbance would change the output by Δ without control, a proportional controller of gain G leaves a residual error of `Δ / (1 + G)`. The baroreflex has an open-loop gain of roughly 2–4, so a disturbance that would drop pressure by 50 mmHg uncontrolled drops it by ~10–15 mmHg controlled. Steady-state error is intrinsic to proportional control, which is why a controlled variable drifts with sustained load and why biological loops add an integral component (the kidney's slow adjustment of volume) to remove it.

3. **Gain is a trade-off: high gain controls tightly but destabilises.** Raising gain shrinks the residual error but amplifies the response to every fluctuation, including noise and the loop's own delayed corrections. Beyond a critical gain the system overshoots, undershoots and oscillates. Tight glucose control by insulin infusion produces more hypoglycaemia for this reason, and an anxious clinician who adjusts a drug after every reading is a high-gain controller producing swings.

4. **Delay in the loop produces oscillation.** If the sensor or effector lags, the controller corrects an error that has already changed, and its correction arrives when the opposite correction is needed. Cheyne–Stokes breathing in heart failure is this: a long circulation time delays the arrival of blood from the lung to the chemoreceptors, and ventilation swings from apnoea to hyperventilation with a period of a minute. Any loop with a delay longer than its response time will oscillate if its gain is high enough; this is a theorem, not a pathology.

5. **A working loop conceals the disturbance; failure appears when the effector saturates.** Blood pressure stays normal while a patient bleeds a litre, because the baroreflex is compensating with tachycardia and vasoconstriction. The compensation is visible (fast pulse, cold hands) but the controlled variable is not, until the effectors reach their limit and pressure collapses abruptly. Compensation and decompensation are the two regimes of one loop, and reading a patient means reading the effectors, not just the variable. The same logic explains why serum calcium is normal until most of the parathyroid is gone and why creatinine rises only after half the kidney is lost.

6. **Set points can be moved, and a moved set point looks like a failed loop.** Fever is not a breakdown of thermoregulation but a raised set point, so the body shivers to reach a higher temperature and defends it there; chronic hypertension resets the baroreceptors so that a high pressure is defended as normal; persistent stress resets the cortisol axis. Distinguishing a moved set point from a failing controller is a recurring diagnostic question, and it decides whether to treat the variable or the setting.

7. **Positive feedback makes switches and avalanches.** When output increases the input that produces it, the system runs to a limit: sodium channels opening depolarise the membrane and open more (the action potential), oxytocin released by uterine stretch causes contractions that stretch the cervix further (labour), activated clotting factors activate more of themselves (haemostasis). Each is useful because it is fast and all-or-none, and each is bounded by a brake. Without the brake the same structure is a catastrophe: falling cardiac output reduces coronary perfusion, which reduces output further (cardiogenic shock); a panic that raises heart rate that raises panic.

8. **Nested loops with different speeds share the work.** Blood pressure is controlled in seconds by the baroreflex, in minutes to hours by the renin–angiotensin system and in days by renal sodium handling; glucose by insulin in minutes, by liver glycogen in hours, by fat and muscle over days. Fast loops handle transients and slow loops the steady state. A drug that blocks one loop is answered by the others, which is why single-agent blood-pressure treatment is often beaten by counter-regulation and why combinations act on different loops.

## Key concepts

| Term | Meaning |
|---|---|
| Controlled variable | The quantity the loop keeps near its set point |
| Set point | The target value; may itself be regulated |
| Sensor, comparator, effector | Measures the variable; computes the error; acts on the system |
| Negative feedback | Response opposes deviation; stabilises |
| Positive feedback | Response amplifies deviation; produces switches or runaway |
| Gain | Size of response per unit error; higher gain, tighter control, less stability |
| Steady-state error | Residual deviation `Δ/(1+G)` under sustained disturbance |
| Delay (lag) | Time between a change and the loop's response to it; cause of oscillation |
| Saturation | The effector's limit, beyond which the loop can no longer compensate |
| Integral control | Correction proportional to accumulated error; removes steady-state offset |

## How it fits

- **Below:** a loop is a [model](the-scientific-method-and-models.md) with a specific structure; its approach to steady state is an [exponential process](compartment-models-and-exponential-processes.md) with a time constant set by gain and delay.
- **Above:** [homeostasis and set points](../../06-physiology/01-integrative-principles/homeostasis-and-set-points.md) is this leaf as physiology; [hormone axes](../../06-physiology/07-endocrine-system/hormone-classes-axes-and-feedback.md) are nested negative loops; [blood pressure regulation](../../06-physiology/03-cardiovascular-system/hemodynamics-and-blood-pressure-regulation.md) and [control of breathing](../../06-physiology/04-respiratory-system/control-of-breathing.md) are tenets 2, 4 and 8; [haemostasis](../../06-physiology/08-blood/haemostasis-and-coagulation.md) is tenet 7 with a brake; [shock](../../08-pathology/02-hemodynamic-disorders/hemorrhage-shock-and-sepsis.md) is tenet 5 followed by tenet 7 without one; [pharmacokinetic steady state](../../09-pharmacology-and-therapeutics/01-pharmacokinetics/elimination-half-life-and-dosing.md) and clinical titration are feedback with the clinician in the loop.
- **Siblings:** [compartment models](compartment-models-and-exponential-processes.md) describe the system being controlled; [nonlinear dynamics](nonlinear-dynamics-oscillations-and-networks.md) takes over when gain and delay push a loop into sustained oscillation or when thresholds make the response discontinuous.

## Common misconceptions

- **"Homeostasis means the variable is constant."** It means deviations are opposed; the variable still moves, and the size of its movement is the disturbance divided by (1 + gain).
- **"A normal value means the system is normal."** It may mean the loop is compensating at full stretch; the effectors (heart rate, hormone levels) reveal the hidden load.
- **"Positive feedback is pathological."** The body uses it deliberately wherever it needs a fast, decisive switch; what makes it dangerous is the absence of a brake.

## Go deeper

- Norbert Wiener, *Cybernetics* (1948): the founding statement that feedback is common to machines and organisms.
- Arthur C. Guyton and John E. Hall, *Textbook of Medical Physiology* (various editions, 14th ed. 2020), chapter on the organisation of control systems: gain and the baroreflex as physiology teaches them.
- Karl Johan Åström and Richard M. Murray, *Feedback Systems* (2nd ed., 2021): the engineering treatment, freely available, with biological examples.
