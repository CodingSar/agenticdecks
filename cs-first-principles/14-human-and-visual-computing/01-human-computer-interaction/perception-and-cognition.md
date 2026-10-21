# Perception and Cognition

> **Layer:** [14 Human and Visual Computing](../README.md) › [Human-computer interaction](README.md)
> **Builds on:** [Sampling and quantization](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md), [Entropy and information](../../02-theory-of-computation/01-information-theory/entropy-and-information.md), [Latency, bandwidth and queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md)
> **Enables:** [Interaction design principles](interaction-design-principles.md), [Digital media and compression](../03-media-and-vision/digital-media-and-compression.md), [Rasterization pipeline](../02-computer-graphics/rasterization-pipeline.md)

## Essence

Every interactive system ends at a human, and the human is a fixed piece of hardware with known limits. The eye samples light with a few million colour-sensitive cones concentrated in a tiny central region; the ear resolves frequencies from about 20 Hz to 20 kHz; working memory holds only a handful of items; attention is a narrow, serial bottleneck; and reaction and perception happen on timescales of tens to hundreds of milliseconds. Human-Computer Interaction (HCI) treats these limits the way computer architecture treats physics: as constraints a design must respect. Much of computing above the hardware, from colour models and video codecs to frame rates, response-time budgets and menu design, is shaped by them.

## Core tenets

1. **Vision is high-resolution only at the centre.** The fovea, about 2 degrees of visual field (roughly a thumbnail at arm's length), holds most cones; acuity falls steeply outside it. The eye compensates by jumping (saccades) three or four times a second, and the brain stitches a stable-seeming scene. Consequences: people do not see what they are not looking at ("change blindness"), and eye-tracked foveated rendering in virtual reality can render the periphery at much lower resolution unnoticed.

2. **Colour is three numbers because we have three cone types.** Cones peak roughly at long, medium and short wavelengths, so any spectrum is perceived through three responses, and spectrally different lights can look identical (metamers). This is why displays mix only red, green and blue, and why colour spaces are three-dimensional. Luminance (brightness) is resolved much more finely than colour difference, which is why video codecs store colour at reduced resolution (chroma subsampling) with little visible loss.

3. **Perception is relative and nonlinear.** Perceived brightness is roughly a power or logarithmic function of physical intensity (Weber–Fechner and Stevens' laws), so equal steps in code values should be equal steps in perception. Gamma encoding in standard image formats spends bits where the eye can see differences. The same principle lets perceptual audio and image codecs discard what masking makes inaudible or invisible.

4. **Motion and responsiveness have hard thresholds.** Around 24–60 frames per second, separate images fuse into perceived motion; fast interaction and head-mounted displays need more (90 Hz or higher) to avoid judder and motion sickness. For responsiveness, classic guidance (Card, Moran and Newell; Nielsen) is: under about 100 ms feels instantaneous, about 1 second keeps the flow of thought, and over about 10 seconds loses attention. These budgets set latency targets all the way down the stack.

5. **Working memory is tiny; recognition beats recall.** People hold roughly four chunks in working memory (Cowan's revision of Miller's "seven plus or minus two"). Recognising an option on screen is far easier than recalling a command. Menus, autocomplete and visible state exist because of this limit; command lines trade it for speed once commands are memorised.

6. **Attention is selective and serial.** Pre-attentive features (colour, motion, orientation) pop out in parallel across the visual field in under about 250 ms; combinations of features need serial search. Good visual design uses pop-out for what matters and avoids competing signals; [information visualization](information-visualization.md) builds its channel choices on this. Interruptions cost time to recover the interrupted task.

7. **Movement time is predictable.** Fitts's law: the time to point at a target is T = a + b · log₂(D/W + 1), where D is distance and W is target width. Big, near targets are fast; screen edges and corners are effectively infinite in size because the pointer stops there. The Hick–Hyman law says choice time grows with the logarithm of the number of equally likely options.

8. **Humans build mental models and act on them.** Users predict a system's behaviour from an internal model formed by its appearance and past experience. When the system's real behaviour differs from that model, errors follow, and users blame themselves. Design aims to make the system image communicate an accurate model.

## Key concepts

| Term | Meaning |
|---|---|
| Fovea | Small central retinal region with high cone density and acuity |
| Saccade | Rapid eye movement between fixation points |
| Metamer | Physically different spectra perceived as the same colour |
| Luminance / chrominance | Brightness / colour-difference components of an image |
| Just-noticeable difference | Smallest change in a stimulus a person can detect |
| Working memory | Short-term store of a few chunks for active processing |
| Pre-attentive processing | Fast, parallel detection of basic visual features |
| Fitts's law | Pointing time grows with log of distance over target width |
| Mental model | A user's internal theory of how a system works |

## How it fits

- **Below:** Human senses are samplers and quantisers in the sense of [signals and systems](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md); perceptual limits set the information a channel must carry, connecting to [entropy](../../02-theory-of-computation/01-information-theory/entropy-and-information.md); responsiveness budgets meet [network latency](../../08-networking/01-principles/latency-bandwidth-and-queueing.md).
- **Above:** [Interaction design](interaction-design-principles.md) turns these limits into rules; [media compression](../03-media-and-vision/digital-media-and-compression.md) discards what perception cannot detect; [graphics](../02-computer-graphics/rasterization-pipeline.md) targets frame rates and colour spaces set here.
- **Siblings:** [Interaction design principles](interaction-design-principles.md) turn these limits into rules, [usability evaluation](usability-evaluation.md) measures how real people, with these limits, actually perform, and [information visualization](information-visualization.md) applies them to encoding data.

## Common misconceptions

- **"People see the whole screen at once."** Only a small foveal patch is sharp; the rest is inferred, which is why users miss obvious changes outside their focus.
- **"Faster is always noticed."** Below perceptual thresholds, latency improvements are invisible; above them, small increases (say 100 ms to 300 ms) are very noticeable.
- **"Seven plus or minus two is a design rule for menu length."** Miller's number concerns short-term recall, not scanning visible menus; on-screen options rely on recognition.

## Go deeper

- Stuart Card, Thomas Moran and Allen Newell, *The Psychology of Human-Computer Interaction* (1983): the model human processor and quantitative HCI.
- Colin Ware, *Information Visualization: Perception for Design* (4th ed., 2020): how visual perception shapes design.
- Stephen Palmer, *Vision Science: Photons to Phenomenology* (1999): the science of seeing, in depth.
