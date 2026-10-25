# Diffusion, Osmosis and Transport

> **Layer:** [00 Physical and Chemical Foundations](../README.md) › [Physics of the Body](README.md)
> **Builds on:** [Energy and thermodynamics](energy-and-thermodynamics.md), [Scale and allometry](scale-and-allometry.md), [Water, solutions and concentration](../02-chemistry-of-life/water-solutions-and-concentration.md)
> **Enables:** [Gas exchange and transport](../../06-physiology/04-respiratory-system/gas-exchange-and-transport.md), [Membrane transport and ion gradients](../../02-biochemistry-and-molecular-biology/04-cell-signalling/membrane-transport-and-ion-gradients.md), [Body fluid compartments and electrolytes](../../06-physiology/01-integrative-principles/body-fluid-compartments-and-electrolytes.md), [Oedema and fluid imbalance](../../08-pathology/02-hemodynamic-disorders/edema-and-fluid-imbalance.md)

## Essence

Molecules move at random, and random motion carries more of them from where they are concentrated to where they are not. This is diffusion, and it needs no energy, no pump and no intention; it is the second law acting on matter. It is fast over micrometres and hopeless over millimetres, which is why cells are small, why every tissue is within a few cell widths of a capillary, and why the lung and gut are built as vast thin membranes. When a membrane lets water through but holds back solute, the same statistics draw water toward the solute: osmosis. Anything the body wants to move *against* a gradient must be pumped, at a cost in Adenosine Triphosphate (ATP), and every pump creates a gradient that other processes then ride.

## Core tenets

1. **Diffusive flux is proportional to the concentration gradient: Fick's law.** `J = −D · A · (ΔC / Δx)`: flux rises with the diffusion coefficient D, the area A and the concentration difference, and falls with distance Δx. The lung obeys this exactly: about 70 m² of alveolar surface, a membrane ~0.5 µm thick, and a partial pressure difference for oxygen of ~60 mmHg between air and venous blood. Thicken the membrane (fibrosis, oedema) or lose area (emphysema) and oxygen transfer falls while carbon dioxide, twenty times more soluble, is barely affected.

2. **Diffusion time grows with the square of distance.** The mean time for a molecule to diffuse a distance x is about `x² / 2D`. For a small solute in water (D ≈ 10⁻⁹ m²/s) that is ~0.5 ms across a 1 µm cell, ~0.5 s across 30 µm, and ~14 hours across 1 cm. So capillaries lie within ~100–200 µm of every cell, and a tumour larger than 1–2 mm must recruit vessels or starve.

3. **Gases diffuse by partial pressure, and solubility sets how much is carried.** Henry's law: the dissolved concentration of a gas is its partial pressure times a solubility coefficient. Blood plasma dissolves only ~3 mL of oxygen per litre at arterial partial pressure, far below the ~200 mL/L the body needs, which is why haemoglobin exists and why carbon monoxide, which outcompetes oxygen for it, is lethal at low partial pressure.

4. **Osmosis is diffusion of water, driven by solute that cannot follow.** Across a membrane permeable to water but not to a solute, water moves toward the higher solute concentration until the hydrostatic pressure built up balances the osmotic pressure, `π = RT · Σc` for dilute solutions (van 't Hoff). Each milliosmole per litre exerts about 19.3 mmHg at body temperature, so plasma (~290 mOsm/kg) has an osmotic pressure of several atmospheres against pure water; a red cell placed in water swells and bursts in seconds.

5. **Only impermeant solutes count: tonicity is not osmolality.** Urea crosses cell membranes freely, so a uraemic patient has high osmolality but normal tonicity and cells do not shrink. Sodium is kept outside cells and potassium inside by the sodium pump, so sodium and its anions are the effective osmoles of extracellular fluid; this is why serum sodium is read as a water-balance signal, and why correcting it too fast moves water into or out of brain cells with lethal effect.

6. **Across a capillary wall, hydrostatic and oncotic pressures compete: Starling.** The endothelium lets water and small solutes through but mostly retains proteins, so plasma albumin (~40 g/L) exerts an oncotic pressure of ~25 mmHg pulling fluid in while capillary hydrostatic pressure (~35 mmHg arterial end, ~15 venous end) pushes it out. Net filtration ≈ `K · [(Pc − Pi) − σ(πc − πi)]`. Raise venous pressure (heart failure), lower albumin (liver disease, nephrotic syndrome) or make the wall leaky (inflammation) and fluid accumulates: oedema has one equation.

7. **Moving solute against its gradient costs free energy, and the body spends it to create gradients it can later spend.** The minimum cost is `RT ln(C2/C1)` per mole plus any electrical work. Primary active transport uses ATP directly (the sodium–potassium pump alone consumes roughly a fifth to a third of resting ATP). Secondary active transport lets one solute run down its gradient to drag another up (glucose with sodium in gut and kidney).

## Key concepts

| Term | Meaning |
|---|---|
| Fick's law | Flux ∝ area × gradient / thickness |
| Diffusion coefficient (D) | How fast a solute spreads; ~10⁻⁹ m²/s for small molecules in water, ~10⁴ times higher in air |
| Partial pressure | The share of total gas pressure due to one gas; the driving force for gas diffusion |
| Henry's law | Dissolved gas concentration = solubility × partial pressure |
| Osmolality | Total solute particles per kilogram of water, ~290 mOsm/kg in plasma |
| Tonicity | Effective osmolality: only solutes that cannot cross the membrane |
| Oncotic pressure | Osmotic pressure due to plasma proteins, ~25 mmHg |
| Starling forces | The hydrostatic and oncotic pressures that set capillary filtration |
| Active transport | Movement against a gradient, paid for by ATP directly or by another gradient |

## How it fits

- **Below:** diffusion is entropy ([energy and thermodynamics](energy-and-thermodynamics.md)) acting on [solutions](../02-chemistry-of-life/water-solutions-and-concentration.md); the `x²` law is the reason for the surface-to-volume constraints in [scale and allometry](scale-and-allometry.md).
- **Above:** [membrane transport](../../02-biochemistry-and-molecular-biology/04-cell-signalling/membrane-transport-and-ion-gradients.md) names the pumps and channels; [gas exchange](../../06-physiology/04-respiratory-system/gas-exchange-and-transport.md) is Fick plus haemoglobin; [body fluid compartments](../../06-physiology/01-integrative-principles/body-fluid-compartments-and-electrolytes.md) and [tubular transport](../../06-physiology/05-renal-system/tubular-transport-and-the-countercurrent-system.md) apply tonicity and secondary transport; [oedema](../../08-pathology/02-hemodynamic-disorders/edema-and-fluid-imbalance.md) is tenet 6 failing.
- **Siblings:** [fluids, pressure and flow](fluids-pressure-and-flow.md) moves substance along tubes by convection; this leaf moves it across walls. [Electricity and excitable membranes](electricity-and-excitable-membranes.md) adds the electrical term to ionic gradients.

## Common misconceptions

- **"Osmosis pulls water by suction from the solute."** Nothing pulls; water molecules on the dilute side simply cross more often than those on the concentrated side, where some of the membrane's surface is occupied by solute.
- **"Carbon dioxide retention in lung disease means diffusion is blocked."** Carbon dioxide diffuses so readily that its retention almost always reflects inadequate ventilation, not a thickened membrane; oxygen is the gas that diffusion limits.

## Go deeper

- Howard C. Berg, *Random Walks in Biology* (1993): diffusion from first principles, short and exact.
- Walter F. Boron and Emile L. Boulpaep, *Medical Physiology* (3rd ed., 2016), chapters on transport and body fluids: the fullest quantitative treatment in a medical text.
- John B. West, *Respiratory Physiology: The Essentials* (10th ed., 2015): Fick's law applied to the lung.
