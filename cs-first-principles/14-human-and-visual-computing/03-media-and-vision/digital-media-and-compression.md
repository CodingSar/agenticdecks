# Digital Media and Compression

> **Layer:** [14 Human and Visual Computing](../README.md) › [Media and vision](README.md)
> **Builds on:** [Source coding and compression](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md), [Entropy and information](../../02-theory-of-computation/01-information-theory/entropy-and-information.md), [Sampling and quantization](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md), [Perception and cognition](../01-human-computer-interaction/perception-and-cognition.md), [Linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md)
> **Enables:** [Content delivery and caching](../../08-networking/05-application-layer/content-delivery-and-caching.md), [Computer vision](computer-vision.md), [HTTP and the web](../../08-networking/05-application-layer/http-and-the-web.md)

## Essence

Images, audio and video are continuous signals that must be sampled and quantised to become bits, and the raw result is enormous: one second of uncompressed 4K video at 60 frames per second is about 1.5 GB (gigabytes). Media compression makes streaming, video calls and photo libraries possible by shrinking this by factors of 100 to 1,000. It combines two ideas. **Lossless coding** removes statistical redundancy and is bounded by Shannon's entropy. **Lossy coding** goes further by discarding information that human perception cannot detect or barely notices, so the limit is not entropy but a perceptual rate-distortion trade-off. Every major codec has the same skeleton: predict what you can, transform the residual so energy concentrates in a few coefficients, quantise those coefficients coarsely where the eye or ear will not notice, and entropy-code what is left.

## Core tenets

1. **Digitisation is sampling plus quantisation.** By the Nyquist–Shannon theorem, a signal with no frequencies above B can be reconstructed from samples taken at more than 2B per second; Compact Disc (CD) audio samples at 44.1 kHz to cover hearing up to about 20 kHz. Quantising each sample to n bits adds noise roughly 6 dB lower for every extra bit. Images sample space (pixels) instead of time.

2. **Lossless compression is bounded by entropy.** Shannon's source coding theorem: no lossless code averages fewer bits per symbol than the source's entropy H. Huffman coding approaches H to within one bit per symbol; arithmetic coding and its variants approach it arbitrarily closely. The Portable Network Graphics (PNG) format and FLAC (Free Lossless Audio Codec) use prediction plus entropy coding and typically achieve 1.5–3× on natural images and audio. Lossless is the only option when every bit matters (text, medical images, archives).

3. **Lossy compression trades rate against distortion.** Rate-distortion theory gives, for a chosen distortion measure, the minimum bits needed to stay within a distortion level D. The practical question is which distortion measure to use: mean squared error is easy to compute but poorly matched to perception, so codecs are tuned with perceptual metrics and human viewing tests.

4. **Transforms concentrate energy so quantisation can discard it.** Natural images are smooth, so neighbouring pixels are correlated. The Discrete Cosine Transform (DCT), applied to small blocks in the Joint Photographic Experts Group (JPEG) standard, re-expresses each block as a few large low-frequency coefficients and many small high-frequency ones. Quantising high frequencies coarsely (the eye is less sensitive to fine detail) zeroes most of them, and entropy coding then stores the zeros almost for free. JPEG typically reaches about 10:1 with little visible loss.

5. **Perceptual models decide what to throw away.** Colour is converted to luminance plus two colour-difference channels, and the colour channels are stored at half resolution (chroma subsampling, 4:2:0) because vision resolves colour more coarsely than brightness. MP3 (MPEG-1 Audio Layer III) and Advanced Audio Coding (AAC) use psychoacoustic masking: a loud tone hides quieter nearby frequencies, so those need few or no bits.

6. **Video exploits redundancy across time.** Consecutive frames are mostly the same scene shifted. Motion-compensated prediction encodes each block of a new frame as a motion vector pointing into a previous frame plus a small residual, which is then transformed and quantised like an image. Intra frames (I-frames) are coded alone and allow seeking; predicted frames (P- and B-frames) reference others and are far smaller. This is the core of H.264/Advanced Video Coding (AVC), H.265/High Efficiency Video Coding (HEVC) and AV1, each newer standard saving roughly 30–50% bitrate at similar quality, at the cost of more encoder computation.

7. **Encoders are searches, decoders are specifications.** Standards define the bitstream and the decoder exactly, so any compliant decoder produces the same output. The encoder is free to choose motion vectors, block sizes and quantisation by any method, which is why encoder quality keeps improving within a fixed standard. Encoding is often 10–100× more expensive than decoding, which suits broadcast and streaming (encode once, decode millions of times).

8. **Rate adapts to the network.** Adaptive bitrate streaming stores each video at several quality levels in short segments; the player measures throughput and switches levels segment by segment. Real-time calls instead adjust encoder rate continuously and favour low latency over quality. As of the mid-2020s, learned (neural) codecs match or beat traditional ones on some image benchmarks, but decoding cost and standardisation have so far limited their deployment.

## Key concepts

| Term | Meaning |
|---|---|
| Sampling rate | Samples per second (or per unit length) taken from a continuous signal |
| Bit depth | Bits per sample; sets quantisation noise |
| Entropy coding | Lossless coding that assigns short codes to frequent symbols (Huffman, arithmetic) |
| Rate-distortion | Trade-off between bits used and error introduced |
| DCT | Transform expressing a block as a sum of cosines of increasing frequency |
| Quantisation step | Coarseness with which a coefficient is rounded; the main lossy knob |
| Chroma subsampling | Storing colour channels at lower resolution than brightness |
| Motion compensation | Predicting blocks from shifted blocks of previous frames |
| Group of pictures | Sequence of frames between independently coded I-frames |
| Bitrate | Bits per second of the encoded stream |

## How it fits

- **Below:** Digitisation is [sampling and quantisation](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md); limits come from [entropy](../../02-theory-of-computation/01-information-theory/entropy-and-information.md) and [source coding](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md); transforms are changes of basis from [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md); what can be discarded is set by [perception](../01-human-computer-interaction/perception-and-cognition.md). Hardware video encoders and decoders are [domain-specific accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md).
- **Above:** Video is the majority of internet traffic, so codecs shape [content delivery](../../08-networking/05-application-layer/content-delivery-and-caching.md), [the web](../../08-networking/05-application-layer/http-and-the-web.md) and [congestion control](../../08-networking/04-transport-layer/congestion-control.md); compressed images are the input to [computer vision](computer-vision.md).
- **Siblings:** [Computer vision](computer-vision.md) extracts meaning from images; compression preserves appearance for human eyes. Learned codecs and learned vision share the same neural machinery.

## Common misconceptions

- **"Higher resolution always means better quality."** At a fixed bitrate, more pixels means fewer bits per pixel and possibly worse artefacts; perceived quality depends on bitrate, codec and viewing distance together.
- **"Lossy compression just removes random detail."** It removes information selected by a perceptual model; artefacts appear exactly where that model is wrong (blocking, ringing, banding).
- **"Compressing twice saves more."** Already-compressed data is close to its entropy; recompressing lossily only adds damage.

## Go deeper

- Claude Shannon, "A Mathematical Theory of Communication" (1948): entropy and the source coding limit.
- Khalid Sayood, *Introduction to Data Compression* (5th ed., 2017): lossless and lossy techniques with derivations.
- Gregory Wallace, "The JPEG Still Picture Compression Standard" (1991): a readable account of the transform-quantise-code pipeline.
- Iain Richardson, *The H.264 Advanced Video Compression Standard* (2nd ed., 2010): how modern video coding works.
