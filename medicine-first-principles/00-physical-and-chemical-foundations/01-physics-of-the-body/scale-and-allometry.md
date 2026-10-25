# Scale and Allometry

> **Layer:** [00 Physical and Chemical Foundations](../README.md) › [Physics of the Body](README.md)
> **Builds on:** [Distributions and descriptive statistics](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/distributions-and-descriptive-statistics.md), [Regression, adjustment and survival analysis](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md)
> **Enables:** [Diffusion, osmosis and transport](diffusion-osmosis-and-transport.md), [Growth, development and the child as patient](../../14-life-course-mind-and-integrative-care/01-paediatrics/growth-development-and-the-child-as-patient.md), [Elimination, half-life and dosing](../../09-pharmacology-and-therapeutics/01-pharmacokinetics/elimination-half-life-and-dosing.md), [Glomerular filtration and clearance](../../06-physiology/05-renal-system/glomerular-filtration-and-clearance.md)

## Essence

Size is not neutral. When a body doubles in every linear dimension, its surface area rises fourfold and its volume eightfold, so any process that happens at a surface (diffusion, heat loss, absorption) falls behind any process that scales with volume (metabolism, weight, heat production). This single geometric fact explains why cells are microscopic, why large animals need lungs, hearts and kidneys while small ones get by with diffusion, why a newborn chills and dehydrates faster than an adult, and why drug doses cannot simply be scaled by weight. The empirical regularities that result, metabolic rate rising as roughly the three-quarter power of mass across animals, are called allometry, and medicine uses them every time it normalises a measurement to body surface area or predicts a child's dose.

## Core tenets

1. **Surface scales as length squared, volume as length cubed.** For geometrically similar bodies, surface-to-volume ratio falls as `1/L`. A 1 µm bacterium has a surface-to-volume ratio a million times greater than a 1 m human. Everything that must cross a surface to serve a volume, oxygen, nutrients, heat, waste, becomes harder with size, and the body's internal architecture is a set of solutions to this: folded, branched and villous surfaces that pack area into volume.

2. **Diffusion alone supports only small, thin or slow organisms.** Because diffusion time grows with the square of distance, a sphere of metabolising tissue more than a fraction of a millimetre across cannot get oxygen to its centre fast enough. Above that size an organism needs a circulation to bring the supply within diffusion range of every cell, and specialised exchange organs with enormous internal surfaces: ~70 m² of alveoli, ~30 m² of small intestine (2014 estimates), ~1 m² of glomerular filter.

3. **Metabolic rate scales as about the ¾ power of body mass.** Across mammals from mouse to elephant, basal metabolic rate `B ≈ 70 · M^0.75` (kcal/day with M in kg; Kleiber, 1932). Per kilogram, a mouse burns energy about 20 times faster than a human and a human about 3 times faster than an elephant. The exponent is between the ⅔ expected from surface-area heat loss and the 1 expected from volume, and is usually explained by the geometry of the branching supply networks that deliver resources. Heart rate, breathing rate and drug clearance per kilogram follow similar fractional powers; lifespan and time scales rise with mass to about the ¼ power.

4. **Children are not small adults.** A newborn weighs ~3.5 kg and has a surface area of ~0.25 m², about 0.07 m²/kg against an adult's ~0.025 m²/kg. Heat loss, evaporative water loss and insensible fluid needs per kilogram are two to three times higher; cardiac output, metabolic rate and renal clearance per kilogram are higher too, though renal and hepatic function are immature at birth. Dosing by surface area or by allometric exponents fits this better than dosing by weight, which under-doses small patients, while immature enzymes can make the same child overdosed for drugs they cannot yet clear.

5. **Body surface area is the clinical normaliser for flow and clearance.** Cardiac output, glomerular filtration rate and cytotoxic drug doses are indexed to body surface area (~1.73 m² for a reference adult) because they scale closer to surface than to weight. A glomerular filtration rate of 60 mL/min means something different in a 45 kg woman and a 110 kg man; the index removes most of that difference. Surface area is estimated from height and weight by empirical formulae (Du Bois, 1916; Mosteller, 1987).

6. **Strength scales with cross-section, weight with volume, so large bodies are relatively weak and fragile.** Muscle force and bone strength rise with area (`L²`) while the load they carry rises with volume (`L³`). A child can hang from one arm; few adults can. The skeleton must therefore become disproportionately thick with size. Obesity imposes the same disproportion on a frame built for less.

7. **Scaling laws are statistical fits, with scatter that matters for the individual.** An allometric exponent summarises a population on a log–log plot; individuals deviate by tens of percent because of body composition, age and disease. Allometry gives the right order of magnitude and the right direction of correction, not a precise prediction for one patient, which is why drugs with a narrow safety margin are adjusted by measurement rather than by formula.

## Key concepts

| Term | Meaning |
|---|---|
| Surface-to-volume ratio | Falls as `1/L`; sets the limit on diffusion-supplied tissue |
| Allometry | Power-law relation `Y = a · M^b` between a trait and body mass |
| Isometric scaling | Exponent as predicted by geometry alone (area ⅔, length ⅓) |
| Kleiber's law | Basal metabolic rate ∝ `M^0.75` across mammals |
| Body surface area | Estimated from height and weight; ~1.73 m² reference adult |
| Indexing | Dividing a measurement by surface area or mass to compare bodies of different size |
| Fractal branching | Repeated subdivision of airways and vessels that packs exchange area into volume |

## How it fits

- **Below:** allometric exponents are [regression](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md) slopes fitted to log-transformed [distributions](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/distributions-and-descriptive-statistics.md), which is why they describe populations better than individuals.
- **Above:** the `x²` cost of [diffusion](diffusion-osmosis-and-transport.md) and the surface terms in [energy and thermodynamics](energy-and-thermodynamics.md) are the mechanisms behind these laws. Higher up, [paediatric dosing and development](../../14-life-course-mind-and-integrative-care/01-paediatrics/growth-development-and-the-child-as-patient.md), [renal clearance](../../06-physiology/05-renal-system/glomerular-filtration-and-clearance.md) and [pharmacokinetic dosing](../../09-pharmacology-and-therapeutics/01-pharmacokinetics/elimination-half-life-and-dosing.md) all normalise by size using these relations.
- **Siblings:** [mechanics and materials](mechanics-and-materials.md) gives the strength-versus-weight consequence; [fluids, pressure and flow](fluids-pressure-and-flow.md) describes the branching networks that scaling demands.

## Common misconceptions

- **"Dose per kilogram is the right way to scale a drug."** Clearance scales with a fractional power of mass, so per-kilogram dosing over-doses large adults and under-doses small children; surface area or an exponent of ~0.75 fits better.
- **"A mouse study at 10 mg/kg translates to 10 mg/kg in humans."** A mouse clears drugs roughly ten times faster per kilogram; allometric conversion divides the dose by a factor of about 12 for a 70 kg human.

## Go deeper

- Knut Schmidt-Nielsen, *Scaling: Why Is Animal Size So Important?* (1984): the classic short treatment.
- J. B. S. Haldane, "On Being the Right Size" (1926): an essay that fits in ten minutes and changes how you see bodies.
- Geoffrey B. West, *Scale* (2017): network explanations for the ¾ exponent and their reach beyond biology.
