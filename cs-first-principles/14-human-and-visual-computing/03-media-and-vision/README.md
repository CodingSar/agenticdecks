# Media and Vision

> **Layer:** [14 Human and Visual Computing](../README.md) › Media and vision
> **Children:** [Digital media and compression](digital-media-and-compression.md) · [Computer vision](computer-vision.md)

## What this area is about

This area deals with images, audio and video as data: how to capture and store them efficiently, and how to make machines understand them. Its two children face opposite directions. **Compression** serves human senses: it keeps what people can perceive and discards the rest, so the bits that remain look and sound right. **Computer vision** serves machines: it throws away appearance and keeps meaning (objects, positions, 3D structure), so a program can act on what a camera sees.

The unifying idea is that natural signals are highly structured and far from random. Neighbouring pixels are correlated, consecutive frames are nearly identical, and the world contains recurring objects seen under consistent geometry. Compression exploits that structure to describe signals in fewer bits; vision exploits it to infer the scene behind the signal. Both, as of the mid-2020s, increasingly learn that structure with neural networks instead of encoding it by hand.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Digital media and compression](digital-media-and-compression.md) | Digitising signals and encoding them compactly for human perception | Information theory, sampling, perception |
| [Computer vision](computer-vision.md) | Recovering objects, geometry and meaning from images | Projective geometry, deep learning |

```
   world --camera (sample, quantise)--> pixels --codec--> bits --decoder--> pixels --> human eye
                                           |
                                           +--> computer vision --> objects, depth, pose --> machine action
```

Read compression first: it explains what an image *is* as data (samples, colour channels, transforms) and how it reaches a program, usually already compressed. Computer vision then treats those pixels as evidence about a scene. The two are linked in practice: vision models are trained and run on compressed images and inherit their artefacts, and learned image codecs and vision networks use the same convolutional and transformer building blocks.

## Connections to sibling areas

- **[Human-computer interaction](../01-human-computer-interaction/README.md):** Perceptual codecs are designed directly from the visual and auditory limits that human-computer interaction studies: chroma subsampling, frequency masking, frame rates. Vision lets interfaces sense users through gesture, gaze, faces and handwriting.
- **[Computer graphics](../02-computer-graphics/README.md):** Vision is inverse graphics, and both share the camera model and projective geometry. Rendered frames are what codecs compress in streaming and cloud gaming; rendered images supply synthetic training data for vision; neural rendering blends the two.

## Connections across layers

Compression is applied [information theory](../../02-theory-of-computation/01-information-theory/README.md) and [signals and systems](../../00-engineering-foundations/04-signals-and-systems/README.md); its transforms are [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md), and dedicated encoder and decoder blocks are [accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md) in every phone. Because video dominates internet traffic, codecs shape [content delivery](../../08-networking/05-application-layer/content-delivery-and-caching.md) and [congestion control](../../08-networking/04-transport-layer/congestion-control.md). Vision now overlaps heavily with [Layer 13](../../13-artificial-intelligence/README.md): its recognition methods are [convolutional networks](../../13-artificial-intelligence/03-deep-learning/convolutional-networks.md) and [transformers](../../13-artificial-intelligence/03-deep-learning/attention-and-transformers.md), and its frontier is multimodal [large language models](../../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md). Surveillance, deepfakes and biometric data connect it to [law, privacy and policy](../../15-computing-in-context/law-privacy-and-policy.md).

## Cross-cutting threads

- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): colour spaces and transforms decide which information is cheap to keep or drop.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): entropy bounds lossless coding; projection makes single-image depth ill-posed.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): rate versus distortion; encoder effort versus bitrate; robustness versus accuracy.
- [Interface vs implementation](../../CROSS-CUTTING.md#interface-vs-implementation): codec standards fix the decoder and bitstream while leaving encoders free to improve.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): compression removes redundancy that error-resilient streaming must partly add back.
