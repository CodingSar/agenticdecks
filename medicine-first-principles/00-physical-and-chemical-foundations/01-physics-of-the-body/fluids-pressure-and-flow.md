# Fluids, Pressure and Flow

> **Layer:** [00 Physical and Chemical Foundations](../README.md) › [Physics of the Body](README.md)
> **Builds on:** [Energy and thermodynamics](energy-and-thermodynamics.md), [Mechanics and materials](mechanics-and-materials.md)
> **Enables:** [Haemodynamics and blood pressure regulation](../../06-physiology/03-cardiovascular-system/hemodynamics-and-blood-pressure-regulation.md), [Ventilation and lung mechanics](../../06-physiology/04-respiratory-system/ventilation-and-lung-mechanics.md), [Microcirculation and capillary exchange](../../06-physiology/03-cardiovascular-system/microcirculation-and-capillary-exchange.md), [Hypertension and vascular disease](../../12-organ-system-specialties/01-cardiology/hypertension-and-vascular-disease.md)

## Essence

Blood, air, urine, lymph and cerebrospinal fluid all move because something pushes them down a pressure gradient against a resistance. One relation, flow equals pressure difference divided by resistance, organises the whole circulation and the airways, and the resistance of a tube depends on the fourth power of its radius, so small changes in vessel or airway calibre produce enormous changes in flow. A second relation, Laplace's law, links the pressure inside a curved wall to the tension the wall must bear, and explains why aneurysms grow, why a dilated heart struggles and why small alveoli would collapse without surfactant. Pressure is energy per unit volume; the circulation is a pump charging a pressure reservoir that drains through adjustable resistors.

## Core tenets

1. **Flow is driven by pressure difference and limited by resistance.** `Q = ΔP / R`, the hydraulic analogue of Ohm's law. Cardiac output (~5 L/min at rest) times total peripheral resistance gives the mean arterial pressure drop from aorta to right atrium (~90 mmHg). Raise resistance (arteriolar constriction) at the same output and pressure rises; lose resistance (sepsis, anaphylaxis) and pressure collapses unless output climbs.

2. **Resistance scales with the inverse fourth power of radius.** For steady laminar flow of a Newtonian fluid, Poiseuille's law gives `R = 8ηL / (πr⁴)`. Halving a vessel's radius multiplies its resistance by 16. Arterioles can change calibre several-fold under neural and local control, so they set regional blood flow and systemic pressure; a 30% narrowing of an airway in asthma roughly quadruples its resistance.

3. **Pressure in a curved wall is held by wall tension: Laplace's law.** For a thin-walled cylinder, `T = P·r`; for a sphere, `T = P·r/2`, where T is tension per unit length. At the same pressure, a wider vessel needs more wall tension, so an aneurysm that has begun to widen is loaded ever harder and tends to widen further. A dilated left ventricle must generate more wall stress for the same chamber pressure, which is part of why dilatation is costly. Capillaries survive high pressure with walls one cell thick because their radius is tiny.

4. **Surface tension would collapse small alveoli; surfactant prevents it.** In a bubble, `P = 2T/r`: smaller bubbles have higher internal pressure and empty into larger ones. Alveoli (radius ~0.1 mm) lined with pure water would behave like this and the lung would collapse to a few large air spaces. Surfactant lowers surface tension more in small alveoli (where its molecules are packed closer), equalising pressures. Premature infants lacking surfactant develop respiratory distress; the physics predicts the disease.

5. **Flow can be laminar or turbulent, and turbulence makes noise.** The Reynolds number `Re = ρvd/η` predicts the transition at roughly 2,000 in a straight tube. High velocity through a narrowed valve, a constricted artery or a compressed brachial artery under a blood-pressure cuff produces turbulence, which is audible as murmurs, bruits and Korotkoff sounds. Anaemia (lower viscosity) and high output also push flow toward turbulence.

6. **Energy in a moving fluid is shared between pressure, kinetic and gravitational terms: Bernoulli.** Where a vessel narrows, velocity rises and lateral pressure falls, so a stenosed aortic valve shows a pressure drop proportional to the square of the jet velocity (echocardiography uses `ΔP ≈ 4v²`, with v in m/s and ΔP in mmHg). Gravity matters too: standing shifts about 500 mL of blood into the legs and raises foot venous pressure to ~90 mmHg, which is why ankles swell and why venous valves and the muscle pump exist.

7. **Compliance stores volume; the arterial tree is a pressure reservoir.** Compliance `C = ΔV/ΔP`. Elastic arteries absorb each stroke volume and release it during diastole, converting pulsatile ejection into near-continuous capillary flow. Stiffening with age lowers compliance, so the same stroke volume produces a higher systolic and lower diastolic pressure: isolated systolic hypertension is a materials problem. Veins are about 20 times more compliant than arteries and hold ~60–70% of blood volume, which makes them the circulation's adjustable reservoir.

## Key concepts

| Term | Meaning |
|---|---|
| Pressure | Force per unit area; energy per unit volume (1 mmHg ≈ 133 Pa) |
| Resistance | Pressure drop per unit flow; set mainly by radius |
| Poiseuille's law | `R = 8ηL/(πr⁴)` for laminar flow in a tube |
| Viscosity (η) | A fluid's internal friction; blood's rises steeply with haematocrit |
| Laplace's law | Wall tension = pressure × radius (cylinder) or half that (sphere) |
| Surface tension | Energy per unit area of a liquid interface; surfactant lowers it |
| Reynolds number | Dimensionless ratio of inertial to viscous forces; high means turbulent |
| Bernoulli principle | Faster flow has lower lateral pressure, energy being conserved |
| Compliance | Volume change per unit pressure change; the inverse of stiffness |
| Hydrostatic pressure | Pressure from the weight of a fluid column, `ρgh` |

## How it fits

- **Below:** pressure is [energy](energy-and-thermodynamics.md) per unit volume; wall tension and compliance are properties of [materials](mechanics-and-materials.md).
- **Above:** [haemodynamics](../../06-physiology/03-cardiovascular-system/hemodynamics-and-blood-pressure-regulation.md) is tenets 1, 2 and 7 with control added; [lung mechanics](../../06-physiology/04-respiratory-system/ventilation-and-lung-mechanics.md) is tenets 2, 4 and 7 for air; [capillary exchange](../../06-physiology/03-cardiovascular-system/microcirculation-and-capillary-exchange.md) combines hydrostatic pressure with [osmosis](diffusion-osmosis-and-transport.md). Aneurysms, [atherosclerosis](../../08-pathology/02-hemodynamic-disorders/atherosclerosis.md), valve disease and [shock](../../13-acute-perioperative-and-procedural-care/03-critical-care/shock-and-haemodynamic-support.md) are failures of one term in these equations.
- **Siblings:** [diffusion and osmosis](diffusion-osmosis-and-transport.md) governs movement across walls; this leaf governs movement along tubes. [Mechanics and materials](mechanics-and-materials.md) supplies the wall properties.

## Common misconceptions

- **"Blood pressure is set by the heart."** The heart sets output; pressure is output times resistance, and resistance (arteriolar tone) is the more adjustable term minute to minute.
- **"Narrow vessels have high pressure."** A narrowing raises resistance and the pressure *upstream* of it; pressure *within and beyond* the narrowing falls (Bernoulli and the drop across the resistance).

## Go deeper

- Steven Vogel, *Life in Moving Fluids* (2nd ed., 1994): fluid mechanics for biologists, with the circulation as a running example.
- Robert M. Berne and Matthew N. Levy, *Cardiovascular Physiology* (various editions; current as Pappano and Wier): the haemodynamics chapters apply every law here.
- John B. West, *Respiratory Physiology: The Essentials* (10th ed., 2015): surface tension and airway resistance in the lung.
