# Computer Graphics

> **Layer:** [14 Human and Visual Computing](../README.md) › Computer graphics
> **Children:** [Geometry and transformations](geometry-and-transformations.md) · [Rasterization pipeline](rasterization-pipeline.md) · [Ray tracing and global illumination](ray-tracing-and-global-illumination.md)

## What this area is about

Computer graphics answers the question: given a mathematical description of a scene (shapes, materials, lights, a camera), what image would a viewer see? It is the forward problem of vision. The unifying idea is **simulation of light reaching a camera**, approximated as cheaply as the application allows. A film frame may spend hours tracing billions of light paths to solve the rendering equation almost exactly; a game frame has about 16 ms and must approximate aggressively. Every technique in graphics sits somewhere on this curve between physical accuracy and speed.

Two sub-problems run through all of it. **Visibility**: which surface is seen at each pixel? **Shading**: how much light leaves that surface toward the eye? The two rendering children answer visibility in opposite orders and shading with different degrees of physical fidelity.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Geometry and transformations](geometry-and-transformations.md) | Representing shapes and moving them through coordinate spaces to the screen | Linear algebra |
| [Rasterization pipeline](rasterization-pipeline.md) | Object-order rendering: project triangles, fill pixels, resolve depth; real-time on graphics hardware | Geometry |
| [Ray tracing and global illumination](ray-tracing-and-global-illumination.md) | Image-order rendering: trace light paths to solve the rendering equation, accelerated by a Bounding Volume Hierarchy (BVH) | Geometry, Monte Carlo sampling |

```
                scene: meshes, materials, lights, camera
                                 |
                   geometry & transformations (4x4 matrices)
                     /                                \
     rasterisation (for each triangle,           ray tracing (for each pixel,
       which pixels?) + z-buffer                   which triangle?) + BVH
     local shading, fast                          global light transport, accurate
                     \                                /
                       hybrid real-time renderers (2020s)
                                 |
                          image -> display -> eye
```

Read geometry first: both renderers consume transformed triangles. Then read rasterisation, which dominates interactive graphics and explains why the Graphics Processing Unit (GPU) looks the way it does. Ray tracing comes last because it is best understood as the general solution that rasterisation approximates: it adds the rendering equation, Monte Carlo integration and spatial acceleration structures. As of the mid-2020s the two have converged in practice: games rasterise primary visibility and trace a few rays per pixel for shadows and reflections, with neural denoisers filling in the rest.

## Connections to sibling areas

- **[Human-computer interaction](../01-human-computer-interaction/README.md):** Graphics draws every graphical interface. Its targets (frame rates around 60–120 Hz, latency under perceptual thresholds, colour encoded for human vision) come from human perception, and techniques such as foveated rendering and perceptual anti-aliasing exploit perceptual limits to save work.
- **[Media and vision](../03-media-and-vision/README.md):** Vision is the inverse problem: from images, recover the scene graphics would have rendered. The two now meet in differentiable and neural rendering, where a renderer inside an optimisation loop reconstructs 3D scenes from photographs. Rendered frames are what video codecs compress for streaming and cloud gaming.

## Connections across layers

Graphics is built on [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md) and [calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md), on [floating point](../../03-digital-logic/01-number-representation/floating-point.md) arithmetic, and above all on [GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md), which it created. Its algorithms use [spatial data structures](../../05-algorithms-and-data-structures/07-advanced-topics/computational-geometry.md), [randomised algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md) and [sampling theory](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md). In return, the GPU hardware developed for graphics became the platform for [deep learning](../../13-artificial-intelligence/03-deep-learning/README.md), and deep learning now feeds back into graphics through neural upscaling, denoising and [generative models](../../13-artificial-intelligence/04-advanced-paradigms/generative-models.md).

## Cross-cutting threads

- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): the rasterisation pipeline and millions of independent rays.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): texture caches, mipmaps and tile-based rendering keep data on-chip.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): physical accuracy versus frame time; noise versus samples.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): homogeneous coordinates make every transform a matrix; depth encoding decides precision.
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): graphics Application Programming Interfaces (APIs) and shaders hide diverse GPU hardware.
