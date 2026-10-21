# Sampling and Quantization

> **Layer:** [00 Engineering Foundations](../README.md) › [Signals and Systems](README.md)
> **Builds on:** [Analog vs Digital](analog-vs-digital.md), [Calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md), [Linear Algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md)
> **Enables:** [Digital Media and Compression](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md), [Source Coding and Compression](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md), [Wireless Networks](../../08-networking/02-link-layer/wireless-networks.md)

## Essence

To compute on a real-world signal, a system must turn a continuous function of time into a finite list of numbers. Sampling discretises time: it records the signal's value at regular instants. Quantisation discretises value: it rounds each sample to one of a finite set of levels. The remarkable result is that sampling can be lossless. The Nyquist-Shannon theorem says a signal containing no frequencies above `B` is completely determined by samples taken faster than `2B` per second. Quantisation, by contrast, always loses information, but in a controlled way: each extra bit of resolution cuts the error by half, about 6 decibels (dB). Together these two steps define the interface between the physical world and every digital media format, sensor and radio.

## Core tenets

1. **Signals can be described by their frequency content.** The Fourier transform rewrites a signal as a sum of sinusoids of different frequencies. A system that is linear and time-invariant (LTI) treats each frequency independently, scaling and delaying it; its effect on any input is convolution with its impulse response. This frequency view makes sampling, filtering and compression tractable.

2. **A band-limited signal is fully captured by samples taken above twice its bandwidth.** If a signal has no energy above frequency `B`, samples at rate `fs > 2B` determine it exactly, and an ideal low-pass filter (sinc interpolation) rebuilds the continuous waveform. This is the Nyquist-Shannon sampling theorem. Compact disc audio samples at 44.1 kHz to cover human hearing up to about 20 kHz.

3. **Sampling too slowly causes aliasing, and it cannot be undone afterwards.** A frequency above `fs/2` produces exactly the same samples as some lower frequency, so it "folds" into the band and masquerades as a different signal. Wagon wheels that seem to spin backwards on film are the visual version. The only cure is to remove high frequencies *before* sampling with an analog anti-aliasing filter. In graphics, aliasing shows up as jagged edges and moiré, handled by the same idea (supersampling and filtering).

4. **Quantisation adds error bounded by half a step.** Rounding to levels spaced `Δ` apart gives error in `[-Δ/2, Δ/2]`. For busy signals this behaves like uniform noise with power `Δ²/12`. For an `N`-bit converter covering a full-scale sine wave, the signal-to-quantisation-noise ratio is about `6.02N + 1.76` dB, so 16-bit audio gives roughly 98 dB.

5. **Noise can be traded against resolution and rate.** Oversampling spreads quantisation noise over a wider band, most of which is then filtered away. Sigma-delta converters push this to the extreme, using a 1-bit quantiser at very high rate with feedback that shapes the noise out of the band of interest. Dithering adds small random noise before quantising to break up structured distortion. All three show that rate and resolution are interchangeable currencies.

6. **Converters bridge the analog and digital domains and set their limits.** An Analog-to-Digital Converter (ADC) samples and quantises; a Digital-to-Analog Converter (DAC) reconstructs. Their speed, resolution and power trade off against one another, and their imperfections (jitter in sampling time, nonlinearity) add error that no later digital processing can remove.

7. **Discrete-time signals are vectors, and processing them is linear algebra.** Once sampled, a signal is a sequence of numbers. Filters are convolutions, the Discrete Fourier Transform is a change of basis computed by the Fast Fourier Transform (FFT) in `O(n log n)`, and compression keeps the coefficients that matter perceptually. This is the bridge to digital signal processing, image processing and the convolutional layers of neural networks.

## Key concepts

| Term | Meaning |
|---|---|
| Sampling rate (`fs`) | Samples per second. |
| Nyquist frequency | `fs/2`, the highest frequency representable without aliasing. |
| Band-limited signal | A signal with no energy above some frequency. |
| Aliasing | High frequencies appearing as false low frequencies after sampling. |
| Anti-aliasing filter | Low-pass filter applied before sampling. |
| Quantisation step (`Δ`) | Spacing between adjacent representable levels. |
| Signal-to-Quantisation-Noise Ratio (SQNR) | Ratio of signal power to quantisation error power. |
| Linear Time-Invariant (LTI) system | A system whose response is linear and independent of when the input arrives. |
| Convolution | The operation by which an LTI system combines input with its impulse response. |

## How it fits

- **Below:** It formalises the boundary described in [analog vs digital](analog-vs-digital.md) using Fourier analysis from [calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md) and vector spaces from [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md).
- **Above:** Every audio, image and video format starts here ([digital media and compression](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md)); rate and resolution limits connect to [source coding](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md). Radios in [wireless networks](../../08-networking/02-link-layer/wireless-networks.md) sample and process signals digitally. Aliasing reappears in [the rasterization pipeline](../../14-human-and-visual-computing/02-computer-graphics/rasterization-pipeline.md), and convolution in [convolutional networks](../../13-artificial-intelligence/03-deep-learning/convolutional-networks.md).
- **Siblings:** [Analog vs digital](analog-vs-digital.md) explains why we discretise at all; [feedback and control](feedback-and-control.md) uses sampled measurements to steer systems, and sigma-delta converters are themselves feedback loops.

## Common misconceptions

- **"More samples always give a more faithful signal."** Above twice the bandwidth, extra samples add no information about a band-limited signal (though oversampling can ease filtering and noise).
- **"Sampling loses the waveform between samples."** For a band-limited signal, the samples determine the waveform between them exactly.
- **"Aliasing can be filtered out after sampling."** Once aliased, a false frequency is indistinguishable from a real one.

## Go deeper

- Claude Shannon, "Communication in the Presence of Noise" (1949): the sampling theorem stated and proved for engineers.
- Alan Oppenheim and Alan Willsky, *Signals and Systems* (1983): the standard introduction to LTI systems and Fourier analysis.
- Alan Oppenheim and Ronald Schafer, *Discrete-Time Signal Processing* (1989): sampling, quantisation and digital filtering in depth.
