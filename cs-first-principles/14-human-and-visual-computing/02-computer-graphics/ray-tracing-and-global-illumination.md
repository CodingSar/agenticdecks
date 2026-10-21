# Ray Tracing and Global Illumination

> **Layer:** [14 Human and Visual Computing](../README.md) › [Computer graphics](README.md)
> **Builds on:** [Geometry and transformations](geometry-and-transformations.md), [Computational geometry](../../05-algorithms-and-data-structures/07-advanced-topics/computational-geometry.md), [Randomized algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md), [Calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md), [Random variables and distributions](../../01-mathematical-foundations/06-probability-and-statistics/random-variables-and-distributions.md)
> **Enables:** [Computer vision](../03-media-and-vision/computer-vision.md), [Generative models](../../13-artificial-intelligence/04-advanced-paradigms/generative-models.md)

## Essence

Ray tracing renders an image by following light backwards: from the camera through each pixel into the scene, finding the first surface hit, then asking where the light arriving at that point came from. Because each ray can query the whole scene, shadows, mirror reflections, refraction and light bouncing between surfaces fall out naturally rather than needing special tricks. The goal is to solve the **rendering equation**: light leaving a point equals light emitted plus all incoming light reflected toward the viewer. That integral has no closed form for real scenes, so path tracing estimates it by Monte Carlo sampling: average many random light paths per pixel. The two engineering problems are finding ray-scene intersections fast (solved by spatial hierarchies) and reducing the noise of random sampling (solved by importance sampling and, increasingly, learned denoisers).

## Core tenets

1. **Ray tracing is image-order visibility.** For each pixel, generate a ray r(t) = o + t·d and find the smallest t > 0 where it hits a surface. Ray-triangle intersection is a few dozen floating-point operations. Rays are independent, so the work is embarrassingly parallel, but each ray may touch any part of the scene, making memory access incoherent.

2. **The rendering equation defines correct images.** Kajiya (1986) wrote outgoing radiance at point x in direction ω_o as

   L_o(x, ω_o) = L_e(x, ω_o) + ∫_Ω f_r(x, ω_i, ω_o) L_i(x, ω_i) (ω_i · n) dω_i

   where L_e is emitted light, f_r is the surface's Bidirectional Reflectance Distribution Function (BRDF), L_i is incoming radiance, n is the surface normal, and the integral is over the hemisphere of incoming directions. L_i at x is L_o at some other surface, so the equation is recursive: light bounces. Every rendering method is an approximation of this equation.

3. **Whitted ray tracing handles mirrors and shadows, not diffuse bounces.** Whitted's 1980 algorithm traces shadow rays to each light, plus recursive rays for perfect reflection and refraction. It produces crisp mirrors and glass but treats indirect diffuse light as a constant ambient term, missing soft shadows and colour bleeding.

4. **Path tracing estimates the integral with random samples.** At each hit, choose one random incoming direction, trace it, and weight the result by f_r · cos θ / p(ω), where p is the sampling probability. Averaging N such paths gives an unbiased estimate whose error falls as 1/√N: halving noise costs four times the samples. Path tracing produces soft shadows, caustics and colour bleeding with no special cases, at the price of noise.

5. **Importance sampling puts samples where the integrand is large.** Variance falls when p(ω) resembles the integrand. Sampling directions according to the BRDF (glossy lobes), sampling lights directly (next-event estimation), and combining strategies with multiple importance sampling (Veach, 1997) cut noise by orders of magnitude for the same sample count.

6. **Acceleration structures make intersection logarithmic.** Testing every ray against every triangle is O(n) per ray. A Bounding Volume Hierarchy (BVH) groups triangles into nested boxes; a ray skips any subtree whose box it misses, giving roughly O(log n) tests per ray in practice. Build quality (for example by the surface area heuristic) matters as much as traversal. Since 2018, consumer Graphics Processing Units (GPUs) include dedicated hardware for BVH traversal and ray-triangle tests.

7. **Real-time ray tracing depends on denoising.** At 60 frames per second and high resolution, the budget is about one to a few rays per pixel, far too few for clean path tracing. Real-time engines combine sparse ray tracing with spatial and temporal denoisers, increasingly neural networks, that reconstruct a clean image from noisy samples. Offline film rendering still uses hundreds to thousands of samples per pixel.

8. **Physically based means measured units and energy conservation.** Radiance units, BRDFs that never reflect more energy than arrives, and measured materials let one renderer stay consistent across scenes, which is why path tracing became standard in film in the 2010s.

## Key concepts

| Term | Meaning |
|---|---|
| Radiance | Light power per unit area per unit solid angle; what a pixel measures |
| Rendering equation | Integral equation for outgoing radiance in terms of emission and reflected incoming light |
| BRDF | Ratio of reflected radiance in one direction to irradiance from another |
| Global illumination | Lighting that includes light reflected between surfaces, not just from lights |
| Path tracing | Monte Carlo solution of the rendering equation by random light paths |
| Importance sampling | Choosing samples with probability proportional to their expected contribution |
| BVH | Tree of nested bounding boxes used to cull ray-object tests |
| Denoising | Reconstructing a clean image from a noisy low-sample estimate |

## How it fits

- **Below:** Rays and camera models come from [geometry and transformations](geometry-and-transformations.md); BVHs are the bounding-box hierarchies of [computational geometry](../../05-algorithms-and-data-structures/07-advanced-topics/computational-geometry.md), pruned like a [search tree](../../05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md) but over overlapping regions of space; path tracing is a [randomised algorithm](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md) for an integral from [calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md) with variance analysed by [probability](../../01-mathematical-foundations/06-probability-and-statistics/random-variables-and-distributions.md); light itself is [electromagnetic radiation](../../00-engineering-foundations/01-physics-of-computation/electromagnetism-and-charge.md), modelled as rays because wavelengths are tiny next to scene features; performance depends on [GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) and [domain-specific accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md).
- **Above:** Rendering produces synthetic training data for [computer vision](../03-media-and-vision/computer-vision.md); differentiable rendering inverts it to recover scenes from photos; neural scene representations and denoisers link it to [generative models](../../13-artificial-intelligence/04-advanced-paradigms/generative-models.md).
- **Siblings:** [Rasterisation](rasterization-pipeline.md) is faster for primary visibility; ray tracing is general for light transport. Both consume [geometry](geometry-and-transformations.md). Modern real-time renderers combine them.

## Common misconceptions

- **"Ray tracing is automatically photorealistic."** Whitted-style ray tracing misses most indirect light; realism comes from solving the rendering equation with good materials and enough samples.
- **"Rays are traced from the lights to the eye."** Most rays go from the camera backwards, because only light reaching the camera matters; bidirectional methods trace from both ends for hard cases such as caustics.
- **"Noise means the renderer is wrong."** It is the variance of an unbiased estimator, and shrinks with more or better samples.

## Go deeper

- James Kajiya, "The Rendering Equation" (1986): the equation and the first path tracer.
- Matt Pharr, Wenzel Jakob and Greg Humphreys, *Physically Based Rendering: From Theory to Implementation* (4th ed., 2023): a complete renderer explained line by line, freely available.
- Eric Veach, *Robust Monte Carlo Methods for Light Transport Simulation* (PhD thesis, 1997): multiple importance sampling and bidirectional path tracing.
- Turner Whitted, "An Improved Illumination Model for Shaded Display" (1980): recursive ray tracing.
