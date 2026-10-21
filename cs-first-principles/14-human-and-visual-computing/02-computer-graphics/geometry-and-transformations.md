# Geometry and Transformations

> **Layer:** [14 Human and Visual Computing](../README.md) › [Computer graphics](README.md)
> **Builds on:** [Linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md), [Floating point](../../03-digital-logic/01-number-representation/floating-point.md), [Computational geometry](../../05-algorithms-and-data-structures/07-advanced-topics/computational-geometry.md)
> **Enables:** [Rasterization pipeline](rasterization-pipeline.md), [Ray tracing and global illumination](ray-tracing-and-global-illumination.md), [Computer vision](../03-media-and-vision/computer-vision.md)

## Essence

Computer graphics turns a mathematical description of a 3D scene into a 2D image. Before any pixel is coloured, every object must be described as geometry and moved through a chain of coordinate systems: from the object's own frame into the world, into the camera's view, through a perspective projection, and onto the screen. The key idea is **homogeneous coordinates**: by adding a fourth coordinate, every one of these steps, including translation and perspective, becomes a 4×4 matrix. A whole chain of transformations then collapses into a single matrix product that hardware can apply to millions of vertices per frame. Representing shapes as triangle meshes keeps everything piecewise linear, so linear maps carry them exactly.

## Core tenets

1. **Surfaces are approximated by triangle meshes.** A triangle is the simplest polygon: always planar, always convex, and fully defined by three vertices. Any surface can be approximated to any precision by enough of them, and interpolation across a triangle is well-defined (barycentric coordinates). Meshes store shared vertex positions plus an index list of triangles, so each vertex is transformed once. Curved representations (splines, subdivision surfaces, implicit functions) are usually converted to triangles for rendering.

2. **Linear transformations are matrices; composing them is multiplying.** Rotation, scaling and shear of a 3D point are 3×3 matrices. Applying A then B equals applying the single matrix BA, so long chains cost one matrix per vertex. Order matters: matrix multiplication is not commutative, so "rotate then translate" differs from "translate then rotate".

3. **Homogeneous coordinates make translation and perspective linear.** Translation is not linear in 3D (it moves the origin), so points are written as (x, y, z, 1) and directions as (x, y, z, 0). A 4×4 matrix can then translate points while leaving directions unchanged. The perspective projection divides by depth; in homogeneous form the matrix copies z into the fourth coordinate w, and the hardware divides (x, y, z) by w afterwards. This "perspective divide" makes far objects smaller.

4. **Rendering is a chain of coordinate spaces.** Model matrix (object to world), view matrix (world to camera), projection matrix (camera to clip space), perspective divide (to normalised device coordinates, a cube from −1 to 1 on each axis), then viewport transform (to pixel coordinates). The combined Model-View-Projection (MVP) matrix is computed once per object per frame. Clipping against the view volume happens in clip space, before the divide, where it remains linear.

5. **Normals transform differently from points.** A surface normal must stay perpendicular to the surface. Under a non-uniform scale M, transforming the normal by M breaks perpendicularity; the correct transform is the inverse transpose (M⁻¹)ᵀ. Getting this wrong produces subtly wrong lighting.

6. **Rotations need care.** Euler angles (yaw, pitch, roll) are intuitive but suffer gimbal lock, where two axes align and a degree of freedom is lost, and they interpolate poorly. Unit quaternions represent rotations without singularities, compose cheaply, and interpolate smoothly by spherical linear interpolation, which is why animation systems and game engines use them.

7. **Precision is finite and depth precision is uneven.** Coordinates are 32-bit floating point. After perspective projection, stored depth is roughly proportional to 1/z, so precision concentrates near the camera and distant surfaces can "z-fight" (flicker as they swap order). Pushing the near clipping plane out, or storing reversed depth in floating point, redistributes precision. Large worlds re-centre coordinates near the camera to avoid jitter from large absolute values.

## Key concepts

| Term | Meaning |
|---|---|
| Vertex | A point with position and attributes (normal, colour, texture coordinates) |
| Triangle mesh | Surface made of vertices and triangles that index into them |
| Homogeneous coordinates | (x, y, z, w) representation where w = 1 for points and w = 0 for directions |
| Affine transformation | Linear map plus translation; preserves straight lines and parallelism |
| Perspective projection | Mapping that shrinks objects with distance by dividing by depth |
| Model, view, projection matrices | Object-to-world, world-to-camera, and camera-to-clip-space transforms |
| Normalised device coordinates | Cube [−1, 1]³ after the perspective divide |
| Barycentric coordinates | Weights (α, β, γ) summing to 1 that express a point inside a triangle |
| Quaternion | Four-component number system representing 3D rotations without singularities |

## How it fits

- **Below:** All of it is [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md): matrices, bases, dot and cross products. Numerical behaviour comes from [floating point](../../03-digital-logic/01-number-representation/floating-point.md). Intersection, convexity and spatial data structures connect to [computational geometry](../../05-algorithms-and-data-structures/07-advanced-topics/computational-geometry.md). [Graphics Processing Units (GPUs)](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) exist largely to apply these transforms in parallel.
- **Above:** The [rasterisation pipeline](rasterization-pipeline.md) applies these transforms in its vertex stage; [ray tracing](ray-tracing-and-global-illumination.md) uses the inverse transforms to generate rays from the camera. [Computer vision](../03-media-and-vision/computer-vision.md) runs the projection backwards to recover 3D structure from images.
- **Siblings:** This file supplies the geometric front end; the other two leaves are two different ways of deciding what colour each pixel should be.

## Common misconceptions

- **"Translation is a linear transformation."** In 3D it is affine, not linear; it becomes linear only in homogeneous coordinates.
- **"Transform normals like any other vector."** Only rotations and uniform scales preserve normals; general transforms need the inverse transpose.
- **"Depth buffers have uniform precision."** Standard perspective depth is highly non-uniform, concentrated near the camera.

## Go deeper

- Steve Marschner and Peter Shirley, *Fundamentals of Computer Graphics* (5th ed., 2021): transformations, viewing and meshes, clearly derived.
- John Hughes et al., *Computer Graphics: Principles and Practice* (3rd ed., 2013): the comprehensive reference.
- Ken Shoemake, "Animating Rotation with Quaternion Curves" (1985): quaternions and spherical interpolation for graphics.
