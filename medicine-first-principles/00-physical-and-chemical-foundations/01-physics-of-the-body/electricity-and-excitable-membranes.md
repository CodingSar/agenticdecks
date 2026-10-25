# Electricity and Excitable Membranes

> **Layer:** [00 Physical and Chemical Foundations](../README.md) › [Physics of the Body](README.md)
> **Builds on:** [Diffusion, osmosis and transport](diffusion-osmosis-and-transport.md), [Energy and thermodynamics](energy-and-thermodynamics.md), [Compartment models and exponential processes](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md)
> **Enables:** [Membrane transport and ion gradients](../../02-biochemistry-and-molecular-biology/04-cell-signalling/membrane-transport-and-ion-gradients.md), [Membrane potential and the action potential](../../06-physiology/02-nervous-system/membrane-potential-and-the-action-potential.md), [Cardiac electrophysiology](../../06-physiology/03-cardiovascular-system/cardiac-electrophysiology.md), [Electrocardiography and electrophysiological testing](../../11-clinical-method-and-diagnostics/03-imaging-and-physiological-measurement/electrocardiography-and-electrophysiological-testing.md)

## Essence

The body's electricity is not electrons in wires but ions in water, separated by a membrane that is a few nanometres thick and almost impermeable. Because the membrane is thin and insulating it is a capacitor, and because it contains channels selective for particular ions it is also a set of switchable resistors in series with batteries, where each battery is the concentration gradient of one ion. A membrane's voltage is simply the weighted outcome of which ion batteries are connected at that moment. Opening sodium channels drives the voltage toward +60 mV; opening potassium channels drives it toward −90 mV. Every nerve impulse, heartbeat and muscle twitch is the membrane switching between these batteries, and every electrocardiogram and electroencephalogram is the far-field sum of such switching in millions of cells.

## Core tenets

1. **A concentration gradient of a permeant ion is a battery: the Nernst equation.** If a membrane is permeable only to ion X, ions diffuse down their gradient until the charge they carry builds a voltage that stops further net flow. That voltage is `E_X = (RT/zF) ln([X]out/[X]in)`, about `61 mV × log10` ratio per unit charge at 37 °C. Potassium (~5 mM outside, ~140 mM inside) gives ~−90 mV; sodium (~145 mM outside, ~12 mM inside) gives ~+65 mV; calcium (10⁴-fold gradient) gives well over +100 mV. These numbers set the ceiling and floor of every electrical event in the body.

2. **The resting potential is a weighted average set by relative permeability.** With several ions permeant, the Goldman–Hodgkin–Katz equation weights each Nernst potential by its permeability. At rest, potassium permeability dominates, so most cells sit at −60 to −90 mV. Raising extracellular potassium from 5 to 8 mM shifts the potassium battery by ~12 mV, depolarising cardiac cells enough to inactivate sodium channels: hyperkalaemia stops hearts through arithmetic.

3. **Vanishingly few ions need to move to change the voltage.** Membrane capacitance is ~1 µF/cm². Charging it by 100 mV moves about 10⁻¹² mol of charge per cm², a change of concentration too small to measure in the bulk. Action potentials therefore do not "use up" the gradients; the sodium–potassium pump restores a tiny debit, which is why a nerve can fire thousands of times after the pump is poisoned before it fails.

4. **Ion channels are gated conductances; excitability is positive feedback between voltage and sodium conductance.** Voltage-gated sodium channels open when depolarised, and the sodium that enters depolarises further. Past a threshold this loop runs away and the membrane swings toward E_Na within a millisecond. Channels then inactivate and slower potassium channels open, pulling the voltage back below rest.

5. **The membrane is a leaky cable: passive signals decay with distance and time.** Local currents spread along a fibre with a length constant `λ = √(r_m / r_i)` and charge the membrane with a time constant `τ = r_m · c_m`. Wider fibres (lower internal resistance) and myelin (higher membrane resistance, lower capacitance) lengthen λ and let the spike jump between nodes. Demyelination shortens λ until conduction fails; local anaesthetics block sodium channels so the loop in tenet 4 cannot close.

6. **Volume conduction turns cellular currents into skin potentials.** The body is a salt solution, so current loops around active cells produce small voltage differences at the surface: ~1 mV for the heart (electrocardiogram), tens of microvolts for the brain (electroencephalogram). A wave of depolarisation moving toward a positive electrode gives an upward deflection; the recorded shape depends on the direction and mass of tissue activating together. The electrocardiogram sees timing and direction, not contraction.

7. **Electrical gradients and concentration gradients add: the electrochemical gradient.** Whether an ion moves in or out depends on the difference between the membrane voltage and that ion's Nernst potential, `V_m − E_X`, the driving force. Calcium at rest faces a driving force of over 200 mV inward, so opening a calcium channel for a millisecond floods the cell and triggers contraction, secretion or death. Pumps and exchangers that move ions against this gradient are the main consumers of cellular Adenosine Triphosphate (ATP).

## Key concepts

| Term | Meaning |
|---|---|
| Nernst potential | The voltage at which diffusion and electrical forces on one ion balance |
| Goldman–Hodgkin–Katz equation | Membrane voltage as a permeability-weighted combination of ion gradients |
| Driving force | `V_m − E_X`; sets the direction and size of an ion's current |
| Membrane capacitance | ~1 µF/cm²; the charge stored per volt across the lipid bilayer |
| Threshold | The depolarisation at which sodium entry outpaces potassium exit |
| Length constant (λ) | Distance over which a passive signal falls to 37% of its size |
| Volume conduction | Spread of current through conducting tissue to a distant electrode |

## How it fits

- **Below:** the Nernst equation is [diffusion](diffusion-osmosis-and-transport.md) balanced against an electric field; gradients are stored [free energy](energy-and-thermodynamics.md); the cable's exponential decay is a [first-order process](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md).
- **Above:** [membrane transport](../../02-biochemistry-and-molecular-biology/04-cell-signalling/membrane-transport-and-ion-gradients.md) describes the pumps and channels as proteins; the [action potential](../../06-physiology/02-nervous-system/membrane-potential-and-the-action-potential.md) and [cardiac electrophysiology](../../06-physiology/03-cardiovascular-system/cardiac-electrophysiology.md) are what whole cells do with them; [electrocardiography](../../11-clinical-method-and-diagnostics/03-imaging-and-physiological-measurement/electrocardiography-and-electrophysiological-testing.md) reads tenet 6; [arrhythmias](../../12-organ-system-specialties/01-cardiology/arrhythmias.md) and [electrolyte disorders](../../12-organ-system-specialties/03-nephrology/electrolyte-and-acid-base-disorders.md) are tenets 2 and 7 going wrong.
- **Siblings:** [diffusion and transport](diffusion-osmosis-and-transport.md) supplies the gradients; [waves, sound, light and radiation](waves-sound-light-and-radiation.md) covers electromagnetic energy used for imaging rather than ionic electricity.

## Common misconceptions

- **"The sodium pump generates the resting potential."** Its direct electrogenic contribution is a few millivolts; the potential comes from potassium leaking down the gradient the pump maintains.
- **"An action potential exhausts the ion gradients."** Each spike moves a minute fraction of the ions; the gradients would take thousands of spikes to run down.
- **"The electrocardiogram measures the heart's pumping."** It records electrical activation only; a heart can have a normal rhythm and no output (pulseless electrical activity).

## Go deeper

- Bertil Hille, *Ion Channels of Excitable Membranes* (3rd ed., 2001): the definitive account of channels as physical devices.
- A. L. Hodgkin and A. F. Huxley, "A quantitative description of membrane current and its application to conduction and excitation in nerve" (*Journal of Physiology*, 1952): the model that made the action potential computable.
- Eric R. Kandel and colleagues, *Principles of Neural Science* (6th ed., 2021), chapters on membrane potential and propagated signalling: cable theory and channel biophysics for medicine.
