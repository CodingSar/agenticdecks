# 14 Human and Visual Computing

> **Layer:** 14 Human and Visual Computing
> **Children:** [Human-computer interaction](01-human-computer-interaction/README.md) · [Computer graphics](02-computer-graphics/README.md) · [Media and vision](03-media-and-vision/README.md)

## What this area is about

Every computation that matters to a person eventually passes through human senses: light from a screen, sound from a speaker, a touch or a keystroke going back in. This layer covers the boundary where computation meets human perception. **Human-Computer Interaction (HCI)** asks how people and programs exchange intent and information without error or frustration. **Computer graphics** asks how to turn a description of a scene into the image a viewer would see. **Media and vision** asks how to store images, audio and video compactly for human senses, and how to let machines see in turn.

The unifying idea is that the human perceptual and cognitive system is a fixed component with measurable properties: three cone types, a sharp but tiny fovea, about 100 ms before a delay feels sluggish, a working memory of a few items. Lower layers are designed against physics and logic; this layer is designed against people. Colour models, frame rates, latency budgets, codec designs and interface conventions all come from fitting computation to that component.

## Why this layer sits here

This layer draws on nearly the whole stack below it.

- **Graphics** is applied [linear algebra](../01-mathematical-foundations/04-algebra/linear-algebra.md) (4×4 matrices move every vertex) and [calculus](../01-mathematical-foundations/05-continuous-mathematics/calculus.md) (the rendering equation is an integral), executed on [Graphics Processing Units (GPUs)](../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) in [floating point](../03-digital-logic/01-number-representation/floating-point.md). Graphics is the reason GPUs exist.
- **Media compression** is applied [information theory](../02-theory-of-computation/01-information-theory/README.md): entropy bounds lossless coding, and rate-distortion theory frames lossy coding. Digitisation itself is [sampling and quantisation](../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md).
- **Interaction** depends on [operating-system scheduling](../07-operating-systems/02-process-management/scheduling.md) and [network latency](../08-networking/01-principles/latency-bandwidth-and-queueing.md) meeting perceptual deadlines, and on [software engineering](../12-software-engineering/README.md) processes that build and test with users.
- **Vision** now overlaps heavily with [Layer 13 Artificial Intelligence](../13-artificial-intelligence/README.md): recognition is deep learning, and the frontier is multimodal models.

The abstraction this layer contributes is the **perceptual interface**: the screen, sound and input devices through which a person sees and controls the whole stack, designed so that what the machine presents matches what a human can perceive and understand. Above it, [Layer 15](../15-computing-in-context/README.md) asks what those interfaces do to individuals and society.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Human-computer interaction](01-human-computer-interaction/README.md) | The human side: perception, cognition, design principles, evaluation with users, visualization of data | Statistics, signals; informs the other two |
| [Computer graphics](02-computer-graphics/README.md) | Scene to image: geometry, rasterisation, ray tracing | Linear algebra, GPUs |
| [Media and vision](03-media-and-vision/README.md) | Signals as data: compression for people, understanding for machines | Information theory, deep learning |

```
                         human perception & cognition (HCI)
                        /            |                    \
              sets targets      sets what to keep     sets interaction budgets
                      /              |                      \
     scene --graphics--> image --compression--> bits --> display --> eye/ear
                                     ^                                  |
     world --camera--> image --------+--vision--> meaning          hands/voice
                                                                        |
                                                  input --> program <---+
```

Read HCI first: it supplies the numbers about human perception that the other two use as design targets, and its visualization leaf shows those numbers applied to presenting data, drawn by the graphics pipeline. Graphics and media and vision can be read in either order. Graphics goes forward from scene to pixels; vision goes backward from pixels to scene; compression sits between them, carrying pixels efficiently from where they are made to where they are seen. All three share the camera model, colour representation and sampling theory.

## Connections to neighbouring layers

- **[00 Engineering foundations](../00-engineering-foundations/README.md):** Sampling, quantisation and filtering from [signals and systems](../00-engineering-foundations/04-signals-and-systems/README.md) underlie digital media, anti-aliasing and human-in-the-loop feedback.
- **[01 Mathematical foundations](../01-mathematical-foundations/README.md):** Linear algebra for transformations and cameras, calculus for light transport, probability and statistics for Monte Carlo rendering and usability experiments.
- **[02 Theory of computation](../02-theory-of-computation/README.md):** Entropy and source coding set the limits that codecs approach.
- **[04 Computer architecture](../04-computer-architecture/README.md):** GPUs were created for the rasterisation pipeline, and ray-tracing cores and video codec blocks are domain-specific accelerators shaped by this layer's workloads.
- **[08 Networking](../08-networking/README.md):** Video is the majority of internet traffic, so codecs, adaptive streaming and content delivery are designed together; interactive latency budgets meet network round-trip times.
- **[13 Artificial intelligence](../13-artificial-intelligence/README.md):** Computer vision is now largely deep learning; neural denoising and upscaling are standard in graphics; generative models create images and video; language models change how people interact with software.
- **[15 Computing in context](../15-computing-in-context/README.md):** Accessibility, dark patterns, surveillance through face recognition and synthetic media raise ethical and legal questions.

## Cross-cutting threads

- [Abstraction and layering](../CROSS-CUTTING.md#abstraction-and-layering): the user interface is the topmost abstraction over the entire stack.
- [Encoding and representation](../CROSS-CUTTING.md#encoding-and-representation): colour spaces, homogeneous coordinates and transform coding decide what is cheap.
- [Pipelining and parallelism](../CROSS-CUTTING.md#pipelining-and-parallelism): the graphics pipeline and per-pixel parallelism on GPUs.
- [Limits and impossibility](../CROSS-CUTTING.md#limits-and-impossibility): perceptual thresholds, entropy bounds, and the ill-posedness of seeing depth from one image.
- [Tradeoffs](../CROSS-CUTTING.md#tradeoffs): physical accuracy versus frame time; rate versus distortion; learnability versus efficiency.
- [Feedback and control](../CROSS-CUTTING.md#feedback-and-control): the interaction loop of action, feedback and evaluation.
