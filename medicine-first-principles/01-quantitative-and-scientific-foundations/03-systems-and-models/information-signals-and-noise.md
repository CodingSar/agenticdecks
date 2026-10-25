# Information, Signals and Noise

> **Layer:** [01 Quantitative and Scientific Foundations](../README.md) › [Systems and Models](README.md)
> **Builds on:** [Probability](../01-probability-and-measurement/probability.md), [Distributions and descriptive statistics](../01-probability-and-measurement/distributions-and-descriptive-statistics.md), [Measurement error and biological variation](../01-probability-and-measurement/measurement-error-and-biological-variation.md)
> **Enables:** [Sensory systems](../../06-physiology/02-nervous-system/sensory-systems.md), [Receptors and ligands](../../02-biochemistry-and-molecular-biology/04-cell-signalling/receptors-and-ligands.md), [Electrocardiography and electrophysiological testing](../../11-clinical-method-and-diagnostics/03-imaging-and-physiological-measurement/electrocardiography-and-electrophysiological-testing.md), [Carbon chemistry and molecular recognition](../../00-physical-and-chemical-foundations/02-chemistry-of-life/carbon-chemistry-and-molecular-recognition.md)

## Essence

The body is run by messages: a hormone concentration, a train of nerve impulses, a sequence of bases, a cytokine gradient, and the clinician reads messages of her own, an electrocardiogram, an image, a history. Every message is a signal carried by a physical variable, and every physical variable fluctuates for reasons unrelated to the message. Information theory asks how much a signal can tell a receiver despite that noise, and gives answers that hold whether the channel is a nerve, a wire or a conversation: information is reduction of uncertainty; a channel has a capacity set by its signal-to-noise ratio and bandwidth; redundancy and averaging buy reliability at the cost of speed; and a receiver must set a threshold that trades missed signals against false alarms. These are the same ideas as sensitivity and specificity, reference ranges and likelihood ratios, seen from the sender's side.

## Core tenets

1. **Information is reduction of uncertainty, measured in bits.** A message carries one bit when it halves the receiver's uncertainty: the answer to one fair yes-or-no question. A test result that moves a diagnosis from 50% to 95% carries more information than one moving it from 1% to 2%, even if the second has the larger likelihood ratio; information depends on what the receiver did not already know. Shannon (1948) defined this quantity as entropy, and the same formula measures the diversity of a microbiome or the uncertainty of a diagnosis before testing.

2. **Every channel adds noise, and the signal-to-noise ratio sets what can be read.** A signal is the part of a measured variable that carries the message; noise is the rest, from thermal motion, from other processes sharing the variable, and from the receiver itself. The electrocardiogram is ~1 mV of cardiac signal against muscle artefact, mains interference and electrode movement; a hormone's message is its concentration against pulsatile release and assay error. When the signal-to-noise ratio falls below about 1 the message is lost for single readings, and no amplification recovers it, because amplification raises both.

3. **Averaging and redundancy recover signal from noise, at the price of time or capacity.** Noise that is random cancels when readings are added, so averaging n measurements improves the signal-to-noise ratio by `√n`; evoked potentials buried in the electroencephalogram become visible after a few hundred repetitions, and a diagnosis becomes firm as independent findings accumulate. Redundancy sends the message more than once or in a form with built-in checks: the genetic code assigns several codons to most amino acids so that many mutations are silent, and the clinician repeats a critical result before acting on it. Both cost: averaging takes time, redundancy takes channel capacity.

4. **Encoding decides what a signal can represent; biology uses rate, amplitude, frequency, pattern and identity.** A nerve carries intensity as firing rate (rate coding) and timing as the pattern of spikes; hormones carry messages as concentration but also as pulse frequency (gonadotrophin-releasing hormone pulses once an hour stimulates, continuous exposure suppresses, which is how one drug both induces and blocks puberty); the genome encodes in sequence; the immune system encodes identity in molecular shape. The same physical variable can carry different messages by different codes, and a receiver tuned to the wrong code reads nothing.

5. **Detection is a threshold decision, and every threshold trades two errors.** A receiver must decide whether a signal is present. Set the threshold low and faint signals are caught but noise is mistaken for signal (false alarms); set it high and false alarms fall but signals are missed. The receiver operating characteristic curve plots the two rates against each other as the threshold moves, and the area under it measures how separable signal and noise are regardless of threshold. This is exactly the sensitivity–specificity trade-off of a diagnostic test, and the right threshold depends on the costs of the two errors, not on the signal alone.

6. **Bandwidth limits how fast a signal can change and be followed, and sampling below twice the highest frequency loses it.** A channel passes only a range of frequencies; a nerve fibre, a hormone with a half-life of hours, or a monitor's filter cannot transmit changes faster than its bandwidth allows. A sampled signal must be sampled at least twice per cycle of its fastest component (the Nyquist criterion) or those components appear as spurious slower ones (aliasing). Hourly glucose readings cannot show post-meal spikes; a monitor filtered too narrowly loses the sharp deflections that diagnose a conduction block; a ventilation study sampled once a day misses nocturnal hypoventilation.

7. **Noise is not always the enemy: it carries information about the system and can aid detection.** The variability of a heart rate, the spread of a hormone's pulses and the fluctuations of a cell's gene expression are signals about the state of the system that generates them, and their loss is as informative as their presence. Small amounts of noise added to a weak periodic signal can push it across a threshold it would otherwise never reach (stochastic resonance), which some sensory systems appear to exploit. Deciding what is signal and what is noise is a modelling choice, not a fact about the data.

8. **Biological signals are read by molecular recognition, so specificity and sensitivity are set by chemistry.** A receptor's discrimination between its ligand and look-alikes is the affinity difference between them, and the cell's amplification cascades raise a few binding events to a decisive response while also amplifying any erroneous ones. The fidelity of Deoxyribonucleic Acid (DNA) replication, the specificity of an antibody and the selectivity of a drug are each a signal-detection problem whose error rates are fixed by the energy gap between right and wrong binding, and whose proofreading and tolerance mechanisms are error correction.

## Key concepts

| Term | Meaning |
|---|---|
| Information (bit) | Reduction of uncertainty; one bit halves the possibilities |
| Entropy (Shannon) | The average uncertainty of a source; the information its messages can carry |
| Signal and noise | The component of a variable that carries the message, and everything else |
| Signal-to-noise ratio | Signal power over noise power; below ~1 single readings are unreliable |
| Averaging | Adding repeated readings; improves signal-to-noise ratio by `√n` for random noise |
| Redundancy | Repetition or built-in checks that make a message robust to errors |
| Encoding | The rule mapping message to physical variable: rate, amplitude, frequency, sequence, shape |
| Threshold detection | Deciding signal present or absent at a cut-off; trades misses against false alarms |
| Receiver operating characteristic (ROC) curve | True-positive rate against false-positive rate across thresholds |
| Bandwidth | The range of frequencies a channel passes; limits how fast a signal can change |
| Nyquist criterion | Sample at least twice the highest frequency present or alias it |

## How it fits

- **Below:** uncertainty is [probability](../01-probability-and-measurement/probability.md); noise has a [distribution](../01-probability-and-measurement/distributions-and-descriptive-statistics.md) and the `√n` rule is the standard error; the measurement half of this picture is [measurement error](../01-probability-and-measurement/measurement-error-and-biological-variation.md).
- **Above:** [molecular recognition](../../00-physical-and-chemical-foundations/02-chemistry-of-life/carbon-chemistry-and-molecular-recognition.md) and [receptors and ligands](../../02-biochemistry-and-molecular-biology/04-cell-signalling/receptors-and-ligands.md) are tenet 8; [signal amplification and termination](../../02-biochemistry-and-molecular-biology/04-cell-signalling/signal-amplification-integration-and-termination.md) is tenets 3 and 4 in the cell; [sensory systems](../../06-physiology/02-nervous-system/sensory-systems.md) and [hormone axes](../../06-physiology/07-endocrine-system/hormone-classes-axes-and-feedback.md) are encoding; [electrocardiography](../../11-clinical-method-and-diagnostics/03-imaging-and-physiological-measurement/electrocardiography-and-electrophysiological-testing.md) and every [imaging method](../../00-physical-and-chemical-foundations/01-physics-of-the-body/waves-sound-light-and-radiation.md) are signal extraction; [diagnostic accuracy studies](../../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md) draw the ROC curve; [health informatics](../../15-medicine-in-society/01-health-systems/health-informatics-and-artificial-intelligence.md) is tenets 1, 5 and 6 applied to records and algorithms.
- **Siblings:** [Bayesian reasoning](../01-probability-and-measurement/bayesian-reasoning.md) is the receiver's side of tenet 5; [nonlinear dynamics](nonlinear-dynamics-oscillations-and-networks.md) treats the variability of tenet 7 as the system's dynamics; [feedback](feedback-and-control.md) loops are channels whose noise and delay set their stability.

## Common misconceptions

- **"Amplifying a weak signal makes it readable."** Amplification raises noise equally; only averaging, filtering to the signal's bandwidth or a better sensor improves the ratio.
- **"More frequent monitoring is always more informative."** Sampling faster than the signal changes adds noise and alarms, not information; sampling slower than it changes aliases it. The rate should match the bandwidth.
- **"Noise is error to be removed."** Variability in heart rate, hormone pulses and gene expression is a signal about the system; removing it discards information.

## Go deeper

- Claude E. Shannon and Warren Weaver, *The Mathematical Theory of Communication* (1949): the founding text, short and readable in Weaver's introduction.
- James V. Stone, *Information Theory: A Tutorial Introduction* (2015): the mathematics at an accessible level with biological examples.
- John A. Swets, Robyn M. Dawes and John Monahan, "Psychological science can improve diagnostic decisions" (*Psychological Science in the Public Interest*, 2000): signal detection theory applied to medical diagnosis.
