# Rasterization Pipeline

> **Layer:** [14 Human and Visual Computing](../README.md) › [Computer graphics](README.md)
> **Builds on:** [Geometry and transformations](geometry-and-transformations.md), [SIMD and GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md), [Pipelining](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md), [Sampling and quantization](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md)
> **Enables:** [Ray tracing and global illumination](ray-tracing-and-global-illumination.md), [Interaction design principles](../01-human-computer-interaction/interaction-design-principles.md), [Neural networks and backpropagation](../../13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md)

## Essence

Rasterisation draws a 3D scene by projecting each triangle onto the screen and filling in the pixels it covers. It answers the visibility question object by object: for each triangle, which pixels does it touch, and is it nearer than whatever is already drawn there? A depth buffer settles the second question with one comparison per pixel. Because every triangle and every pixel can be processed independently, the algorithm is a deep, wide pipeline that maps perfectly onto massively parallel hardware. The Graphics Processing Unit (GPU) was built for exactly this pipeline, and it renders millions of triangles at 60 frames per second or more. Its weakness: each triangle is shaded locally, so shadows, reflections and indirect light must be approximated.

## Core tenets

1. **Rasterisation is object-order rendering.** The outer loop is over triangles, the inner loop over the pixels each covers. Cost grows roughly with the number of triangles plus the number of covered pixels (fragments). This contrasts with ray tracing's image order (for each pixel, find the object), and it is why rasterisation is cheap for primary visibility but awkward for effects that need to know about the rest of the scene.

2. **The pipeline has fixed stages and programmable shaders.** Vertex processing (transform each vertex by the Model-View-Projection matrix) → primitive assembly and clipping → rasterisation (find covered pixel samples, interpolate vertex attributes) → fragment shading (compute colour per sample) → depth test and blending → framebuffer. Vertex and fragment stages run small programs called shaders, written in languages such as the OpenGL Shading Language (GLSL) or High-Level Shading Language (HLSL), executed in parallel by thousands of GPU lanes.

3. **Coverage is decided by edge functions.** For a triangle with edges defined by lines in screen space, each edge function E(x, y) = ax + by + c is positive on the inside. A sample is covered when all three are non-negative. The test is independent per pixel and needs only multiply-adds, so hardware evaluates it for many pixels at once. Edge function values also give barycentric coordinates for interpolation, with a perspective correction because linear interpolation in screen space is not linear in 3D.

4. **The depth buffer solves visibility with memory instead of sorting.** For each pixel, store the depth of the nearest surface so far; draw a new fragment only if it is nearer, then update. This "z-buffer" (Catmull, 1974) costs one buffer and one comparison per fragment and handles arbitrary intersecting geometry without sorting triangles. Transparency breaks it, because blending depends on order, so transparent objects are sorted or handled with approximations.

5. **Textures add detail without geometry, and need filtering.** A texture is an image mapped onto a surface by per-vertex coordinates. When a texture is minified (many texels per pixel), point sampling aliases into shimmering patterns. Mipmapping precomputes progressively half-resolution copies and samples from the level that matches the pixel's footprint, a direct application of the sampling theorem.

6. **Shading models approximate local light reflection.** A fragment shader computes reflected light from the surface normal, light directions, view direction and material. Modern engines use Physically Based Rendering (PBR) models with a microfacet Bidirectional Reflectance Distribution Function (BRDF) that conserves energy, so materials look consistent under any lighting. Shadows use shadow maps (render depth from the light, then compare), and indirect light is approximated with precomputed or screen-space techniques.

7. **Aliasing is undersampling.** A triangle edge is a step function with unbounded frequency content; one sample per pixel cannot represent it, giving jagged edges. Multisample anti-aliasing tests coverage at several points per pixel; temporal anti-aliasing accumulates jittered samples across frames. As of the mid-2020s, neural upscalers render at lower resolution and reconstruct high-resolution frames, trading some fidelity for large speed-ups.

8. **Performance is limited by bandwidth and overdraw.** Each pixel may be shaded several times when triangles overlap (overdraw), and every texture fetch and framebuffer write uses memory bandwidth. Early depth testing, deferred shading and tile-based rendering in mobile GPUs exist to shade each visible pixel about once and keep data on-chip.

## Key concepts

| Term | Meaning |
|---|---|
| Fragment | A candidate pixel sample produced by rasterising a triangle |
| Shader | Small program run per vertex or per fragment on the GPU |
| Depth buffer (z-buffer) | Per-pixel store of nearest depth used to resolve visibility |
| Edge function | Linear function whose sign tells which side of a triangle edge a point lies on |
| Texture / texel | Image applied to a surface / one element of that image |
| Mipmap | Pyramid of pre-filtered, successively half-resolution texture copies |
| BRDF | Function giving how much light arriving from one direction leaves in another |
| Shadow map | Depth image from the light's viewpoint used to test whether points are lit |

## How it fits

- **Below:** Vertex transforms come from [geometry and transformations](geometry-and-transformations.md); the pipeline is the [pipelining](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md) idea applied to graphics, executed on [GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md); aliasing and filtering are [sampling theory](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md); framebuffers and textures stress the [memory hierarchy](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md).
- **Above:** Every graphical user interface, game and visualisation is drawn this way, so frame-rate targets from [perception](../01-human-computer-interaction/perception-and-cognition.md) apply here. The GPUs built for this pipeline became the engines of [deep learning](../../13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md).
- **Siblings:** [Ray tracing](ray-tracing-and-global-illumination.md) answers the same visibility question in image order and handles global light transport; real-time engines as of the mid-2020s are hybrids that rasterise primary visibility and trace rays for shadows, reflections and indirect light.

## Common misconceptions

- **"GPUs were designed for AI."** They were designed for this pipeline; their throughput on dense, independent arithmetic later made them ideal for neural networks.
- **"More triangles is the main cost."** Pixel shading, overdraw and memory bandwidth usually dominate; tiny triangles are inefficient because hardware shades pixels in 2×2 groups.
- **"Rasterisation is physically accurate if the shaders are."** Local shading cannot capture light bouncing between surfaces without additional approximations.

## Go deeper

- Tomas Akenine-Möller et al., *Real-Time Rendering* (4th ed., 2018): the reference for the modern pipeline and its tricks.
- Edwin Catmull, *A Subdivision Algorithm for Computer Display of Curved Surfaces* (PhD thesis, 1974): origin of the z-buffer and texture mapping.
- Fabian Giesen, "A Trip through the Graphics Pipeline" (blog series, 2011): how the hardware really executes each stage.
