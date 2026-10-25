# Waves, Sound, Light and Radiation

> **Layer:** [00 Physical and Chemical Foundations](../README.md) › [Physics of the Body](README.md)
> **Builds on:** [Energy and thermodynamics](energy-and-thermodynamics.md), [Mechanics and materials](mechanics-and-materials.md), [Information, signals and noise](../../01-quantitative-and-scientific-foundations/03-systems-and-models/information-signals-and-noise.md)
> **Enables:** [Sensory systems](../../06-physiology/02-nervous-system/sensory-systems.md), [Ultrasound](../../11-clinical-method-and-diagnostics/03-imaging-and-physiological-measurement/ultrasound.md), [Radiography and computed tomography](../../11-clinical-method-and-diagnostics/03-imaging-and-physiological-measurement/radiography-and-computed-tomography.md), [Radiotherapy and radiation biology](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md)

## Essence

Almost everything medicine knows about the inside of a living body without cutting it open comes from waves: sound reflected from tissue boundaries, X-rays attenuated by bone, radio waves emitted by hydrogen nuclei in a magnetic field, gamma rays from a tracer, and light absorbed by haemoglobin. The body's own senses work the same way, with the ear as a mechanical frequency analyser and the eye as a camera. Two properties of any wave decide what it can do: its wavelength sets the smallest detail it can resolve and how deep it penetrates, and its photon energy decides whether it merely warms tissue or breaks chemical bonds. The line between those two regimes, at about 10 electron volts, is the line between imaging that is safe to repeat and radiation that causes cancer and is also used to cure it.

## Core tenets

1. **Wavelength limits resolution and trades against penetration.** A wave cannot resolve structure much smaller than its wavelength. Diagnostic ultrasound at 2–15 MHz has wavelengths of 0.1–0.8 mm in soft tissue (speed ~1,540 m/s); higher frequency sharpens the image but is absorbed faster, so a superficial probe sees fine detail and an abdominal probe sees deep. Light (~0.5 µm) resolves cells but scatters within a millimetre of tissue, so optical imaging stops at the surfaces an endoscope can reach.

2. **Reflection happens at changes in acoustic impedance.** The fraction of sound reflected at a boundary depends on the mismatch in impedance (density × sound speed) across it. Soft tissues differ by a few percent, giving the faint echoes that build a grey-scale image; bone and air differ so much that nearly everything reflects, which is why ultrasound cannot see through ribs or gas-filled lung and why gel is needed to exclude air between probe and skin. Fluid reflects nothing and appears black.

3. **The Doppler shift measures velocity along the beam.** Sound reflected from a moving target returns with a frequency shifted by `Δf = 2 f v cosθ / c`. Blood moving at 1 m/s shifts a 5 MHz beam by ~6.5 kHz, giving velocity, direction and, through Bernoulli, pressure gradients across stenosed valves. The angle term means a beam perpendicular to flow measures nothing, a daily error in echocardiography.

4. **Ionising radiation deposits energy that breaks bonds; everything else does not.** Photons above ~10 eV (X-rays, gamma rays) and energetic particles eject electrons from atoms, producing free radicals and direct breaks in Deoxyribonucleic Acid (DNA). Radio waves, microwaves, infrared and visible light cannot; their only hazard is heating. This is why magnetic resonance imaging and ultrasound can be repeated without limit and why computed tomography carries a small but real cancer risk (roughly 1 in 2,000 additional lifetime cancers per 10 mSv scan is a commonly quoted order of magnitude, with higher risk in children).

5. **X-ray contrast comes from attenuation, which depends on density and atomic number.** A beam passing through tissue is attenuated exponentially, `I = I₀ e^(−µx)`, and the coefficient µ rises steeply with atomic number at diagnostic energies. Calcium in bone (Z = 20) absorbs far more than soft tissue (effectively Z ≈ 7), so bone is white and air black; iodine (Z = 53) and barium (Z = 56) are injected or swallowed as contrast for the same reason. Computed tomography reconstructs the map of µ from projections at many angles.

6. **Radioactive decay is exponential, and half-life is chosen to match the job.** A radionuclide's activity falls by half every half-life; the dose a patient receives is the integral of activity over time, shortened by biological excretion. Technetium-99m (6 h) suits imaging; iodine-131 (8 days) suits ablating thyroid tissue; cobalt-60 and linear accelerators supply the external beams of radiotherapy. Radiation kills dividing cells preferentially because damaged DNA cannot pass mitosis, which is why tumours, bone marrow, gut lining and hair are its main targets.

7. **Light absorption by pigments is a non-invasive chemical assay.** Oxygenated and deoxygenated haemoglobin absorb red and infrared light differently; a pulse oximeter shines both wavelengths through a finger and reads oxygen saturation from the ratio of pulsatile absorbances (Beer–Lambert law). The same law underlies every colorimetric laboratory test, skin colour changes in cyanosis and jaundice, and the laser's choice of wavelength to target a vessel or a pigment.

## Key concepts

| Term | Meaning |
|---|---|
| Wavelength and frequency | `c = f λ`; shorter wavelength resolves finer detail |
| Acoustic impedance | Density × sound speed; mismatch at a boundary causes reflection |
| Doppler shift | Frequency change from a moving reflector, proportional to velocity along the beam |
| Attenuation | Exponential loss of intensity with depth; `I = I₀e^(−µx)` |
| Ionising radiation | Photons or particles energetic enough to eject electrons (> ~10 eV) |
| Absorbed dose and effective dose | Energy per kilogram (gray) and its weighted cancer-risk equivalent (sievert) |
| Half-life | Time for activity (or anything decaying exponentially) to fall by half |
| Beer–Lambert law | Absorbance proportional to concentration × path length |

## How it fits

- **Below:** energy carried by waves and deposited as heat or chemistry follows [thermodynamics](energy-and-thermodynamics.md); tissue stiffness ([mechanics](mechanics-and-materials.md)) sets sound speed; extracting an image from echoes is a [signal-to-noise](../../01-quantitative-and-scientific-foundations/03-systems-and-models/information-signals-and-noise.md) problem.
- **Above:** the [ear and eye](../../06-physiology/02-nervous-system/sensory-systems.md) are mechanical and optical transducers obeying tenet 1; [ultrasound](../../11-clinical-method-and-diagnostics/03-imaging-and-physiological-measurement/ultrasound.md), [radiography and computed tomography](../../11-clinical-method-and-diagnostics/03-imaging-and-physiological-measurement/radiography-and-computed-tomography.md), [magnetic resonance imaging](../../11-clinical-method-and-diagnostics/03-imaging-and-physiological-measurement/magnetic-resonance-imaging.md) and [nuclear medicine](../../11-clinical-method-and-diagnostics/03-imaging-and-physiological-measurement/nuclear-medicine-and-molecular-imaging.md) are the clinical instruments; [radiotherapy](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md) and [environmental and toxic injury](../../08-pathology/04-genetic-metabolic-and-environmental-disease/environmental-and-toxic-injury.md) take tenet 4 to its therapeutic and harmful ends.
- **Siblings:** [electricity and excitable membranes](electricity-and-excitable-membranes.md) deals with the body's own electrical signals; this leaf deals with energy sent into or emitted from the body. [Redox and electron transfer](../02-chemistry-of-life/redox-and-electron-transfer.md) explains the free radicals that ionising radiation produces.

## Common misconceptions

- **"All radiation causes cancer."** Only ionising radiation does; radio waves, magnetic fields and ultrasound at diagnostic intensities do not break bonds.
- **"Ultrasound shows what tissue is made of."** It shows boundaries where impedance changes; a uniform liver and a uniform tumour of the same impedance look alike.

## Go deeper

- Jerrold T. Bushberg and colleagues, *The Essential Physics of Medical Imaging* (4th ed., 2020): the standard account of every imaging modality's physics.
- Eric J. Hall and Amato J. Giaccia, *Radiobiology for the Radiologist* (8th ed., 2018): what ionising radiation does to cells and why.
- Richard Feynman, *QED: The Strange Theory of Light and Matter* (1985): light, reflection and absorption at the deepest level, readable by anyone.
