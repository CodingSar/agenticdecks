# Membrane potential and the action potential

> **Layer:** [06 Physiology](../README.md) › [Nervous system](README.md)
> **Builds on:** [Electricity and excitable membranes](../../00-physical-and-chemical-foundations/01-physics-of-the-body/electricity-and-excitable-membranes.md), [Membrane transport and ion gradients](../../02-biochemistry-and-molecular-biology/04-cell-signalling/membrane-transport-and-ion-gradients.md), [Nervous tissue](../../05-tissues-and-anatomy/01-tissues/nervous-tissue.md), [Body fluid compartments and electrolytes](../01-integrative-principles/body-fluid-compartments-and-electrolytes.md)
> **Enables:** [Cardiac electrophysiology](../03-cardiovascular-system/cardiac-electrophysiology.md), [Skeletal muscle contraction and energetics](../10-musculoskeletal-system-and-skin/skeletal-muscle-contraction-and-energetics.md), [Epilepsy](../../12-organ-system-specialties/10-neurology/epilepsy.md), [Demyelinating and neuromuscular disease](../../12-organ-system-specialties/10-neurology/demyelinating-and-neuromuscular-disease.md), [General and regional anaesthesia](../../13-acute-perioperative-and-procedural-care/02-anaesthesia-and-perioperative-medicine/general-and-regional-anaesthesia.md)

## Essence

Every cell holds a voltage across its membrane because ions are unequally distributed and the membrane is selectively permeable; a nerve or muscle cell can additionally fire an action potential, a stereotyped, self-propagating reversal of that voltage that carries information without decrement over a metre of axon. The resting potential (~−70 mV in neurons) is set mostly by potassium leaking out down its gradient; the action potential is sodium rushing in through voltage-gated channels that open in positive feedback, then inactivate, while potassium channels open to restore rest. Two equations carry the whole subject: Nernst gives the voltage at which one ion's gradient is balanced, and Goldman–Hodgkin–Katz gives the membrane potential as a permeability-weighted mix of them. Everything from hyperkalaemic cardiac arrest to local anaesthesia to multiple sclerosis is a change in one term of those equations or in the channels that set the permeabilities.

## Core tenets

1. **Each ion has an equilibrium potential set by its concentration ratio (Nernst), and the membrane potential sits where the permeable ions' currents sum to zero.** E = (RT/zF) ln([ion]out/[ion]in) ≈ (61.5/z) log10([out]/[in]) mV at 37 °C. With potassium 4 out and 140 in, E_K ≈ −95 mV; sodium 145 out, 12 in gives E_Na ≈ +67 mV; chloride ≈ −70 to −90 mV; calcium > +120 mV. No pump makes these voltages directly; the pump makes the gradients and the gradients make the voltages.

2. **The resting potential is near E_K because at rest the membrane is ~25–100 times more permeable to potassium than to sodium.** The Goldman–Hodgkin–Katz equation, Vm = 61.5 log[(P_K[K]o + P_Na[Na]o + P_Cl[Cl]i)/(P_K[K]i + P_Na[Na]i + P_Cl[Cl]o)], weights each equilibrium potential by its permeability. Open "leak" potassium channels dominate, a little sodium leak pulls Vm up to ~−70 mV, and Na+/K+-adenosine triphosphatase (Na+/K+-ATPase) keeps the gradients from running down (its 3:2 stoichiometry adds only a few millivolts directly). Change a permeability and Vm moves toward that ion's Nernst potential: this is the whole principle of excitability.

3. **The action potential is a positive-feedback loop in sodium conductance, terminated by inactivation and by potassium.** Depolarisation to threshold (~−55 mV) opens voltage-gated sodium channels; the inward current depolarises further, opening more channels, until Vm nears E_Na (peak ~+30 to +40 mV) within a millisecond. Sodium channels then inactivate (a separate gate closes and will not reopen until the membrane repolarises), and slower voltage-gated potassium channels open, driving Vm back toward E_K and briefly beyond (after-hyperpolarisation). Hodgkin and Huxley (1952) measured these conductances in squid axon and reconstructed the spike from them.

4. **The spike is all-or-none and refractory, so information is carried in timing and frequency, not amplitude.** Below threshold nothing happens; above it the shape is fixed. During the absolute refractory period (sodium channels inactivated) no stimulus can fire the cell; during the relative refractory period a stronger one can. Refractoriness caps firing rate (~several hundred per second), forces conduction one way, and in the heart prevents re-entry and tetany. Stimulus strength is coded as spike frequency and as the number of fibres recruited.

5. **Propagation is local circuit current, and speed is set by cable properties: diameter and myelin.** Inward current at the active patch flows along the axon and depolarises the next patch to threshold. Current spreads further before leaking out when axial resistance is low (large diameter) and membrane resistance is high and capacitance low (myelin); the length constant λ = √(r_m/r_i) grows accordingly. Unmyelinated C fibres conduct at ~0.5–2 m/s; myelinated Aα fibres at ~70–120 m/s, the spike jumping between nodes of Ranvier where the sodium channels are concentrated (saltatory conduction). Demyelination slows or blocks conduction without killing the axon, and the block is worse when warm, which is why multiple sclerosis symptoms fluctuate with temperature.

6. **Extracellular potassium sets the resting potential, so plasma potassium is the electrolyte that stops hearts.** Raising [K]o from 4 to 8 mmol/L moves E_K from −95 to −76 mV; the cell depolarises, sodium channels partly inactivate at the new resting level, conduction slows and eventually fails (flaccid paralysis, wide QRS complexes, arrest). Low potassium hyperpolarises and, in the heart, prolongs repolarisation and provokes arrhythmia. Extracellular calcium screens surface charge on the channels; hypocalcaemia lowers the effective threshold, producing spontaneous firing (tetany, paraesthesiae).

7. **Drugs and toxins act on the channels, and the state-dependence of their binding is the therapeutic principle.** Local anaesthetics (lidocaine, bupivacaine) enter from inside the cell and bind open or inactivated sodium channels preferentially, so rapidly firing, thin, unmyelinated pain fibres are blocked before thick motor fibres. Class I antiarrhythmics and several antiepileptics (carbamazepine, phenytoin) use the same use-dependence to silence cells firing abnormally fast while sparing normal ones. Tetrodotoxin blocks from outside; channel mutations cause epilepsies, periodic paralyses and long QT syndromes.

## Key concepts

| Term | Meaning |
|---|---|
| Equilibrium (Nernst) potential | Voltage at which an ion's electrical and concentration forces balance |
| Goldman–Hodgkin–Katz equation | Membrane potential as a permeability-weighted average of equilibrium potentials |
| Resting potential | ~−70 mV (neuron), ~−90 mV (skeletal and cardiac muscle); near E_K |
| Threshold | Depolarisation (~−55 mV) at which sodium influx exceeds potassium efflux and feedback takes over |
| Inactivation | Closure of a sodium channel's second gate during depolarisation; basis of refractoriness |
| Refractory period | Interval after a spike when a cell cannot (absolute) or only with difficulty (relative) fire again |
| Length constant (λ) | Distance over which a passive voltage change decays to 37%; larger with diameter and myelin |
| Saltatory conduction | Spike regeneration only at nodes of Ranvier in myelinated axons |
| Use-dependent block | Preferential drug binding to open or inactivated channels, silencing fast-firing cells |

## How it fits

- **Below:** charge, capacitance and the cable equation are in [electricity and excitable membranes](../../00-physical-and-chemical-foundations/01-physics-of-the-body/electricity-and-excitable-membranes.md); the pump and channel proteins in [membrane transport](../../02-biochemistry-and-molecular-biology/04-cell-signalling/membrane-transport-and-ion-gradients.md); myelin and glia in [nervous tissue](../../05-tissues-and-anatomy/01-tissues/nervous-tissue.md); the ion concentrations in [body fluids](../01-integrative-principles/body-fluid-compartments-and-electrolytes.md).
- **Above:** the [cardiac action potential](../03-cardiovascular-system/cardiac-electrophysiology.md) adds a calcium plateau; [skeletal muscle](../10-musculoskeletal-system-and-skin/skeletal-muscle-contraction-and-energetics.md) couples the spike to calcium release; [epilepsy](../../12-organ-system-specialties/10-neurology/epilepsy.md) is runaway synchronous firing; [demyelinating disease](../../12-organ-system-specialties/10-neurology/demyelinating-and-neuromuscular-disease.md) is tenet 5 failing; [regional anaesthesia](../../13-acute-perioperative-and-procedural-care/02-anaesthesia-and-perioperative-medicine/general-and-regional-anaesthesia.md) is tenet 7.
- **Siblings:** the spike ends at the [synapse](synaptic-transmission-and-neurotransmitters.md); [sensory](sensory-systems.md) and [motor](motor-control.md) systems are what the spikes encode.

## Common misconceptions

- **"The sodium pump generates the resting potential."** The pump maintains the gradients; the potential is generated by potassium leaking down its gradient. Block the pump and the potential decays over minutes to hours, not instantly.
- **"An action potential moves a lot of ions."** Each spike moves a few picomoles per square centimetre; the concentrations barely change, which is why a nerve can fire thousands of times with the pump off.
- **"Bigger stimuli give bigger action potentials."** Amplitude is fixed; stimulus strength is coded by frequency and recruitment.

## Go deeper

- Alan L. Hodgkin and Andrew F. Huxley, "A quantitative description of membrane current and its application to conduction and excitation in nerve" (*Journal of Physiology*, 1952): the model from which the field descends.
- Bertil Hille, *Ion Channels of Excitable Membranes* (3rd ed., 2001): the definitive account of the channels.
- Eric R. Kandel and colleagues (eds), *Principles of Neural Science* (6th ed., 2021), chapters 9–10: membrane potential and propagation for the general reader with equations.
