# Computational Geometry

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Advanced Topics](README.md)
> **Builds on:** [Linear Algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md), [Comparison Sorting](../04-sorting-and-searching/comparison-sorting.md), [Divide and Conquer](../03-design-paradigms/divide-and-conquer.md), [Floating Point](../../03-digital-logic/01-number-representation/floating-point.md)
> **Enables:** [Geometry and Transformations](../../14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md), [Ray Tracing and Global Illumination](../../14-human-and-visual-computing/02-computer-graphics/ray-tracing-and-global-illumination.md), [Computer Vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md), [Search and Planning](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md)

## Essence

Computational geometry designs algorithms for points, segments, polygons and higher-dimensional shapes: convex hulls, line-segment intersections, nearest neighbours, triangulations, range searches and point location. Its problems underlie graphics, Geographic Information Systems (GIS), robotics, computer-aided design and machine learning. Two ideas recur. First, geometric problems often reduce to sorting plus a clever sweep or recursive split, giving O(n log n) algorithms that match lower bounds. Second, geometry runs on real numbers but computers use floating point, so a single wrong sign in an orientation test can make an algorithm crash or produce inconsistent output. Correctness therefore depends as much on *robust predicates* as on algorithmic ideas.

## Core tenets

1. **Most algorithms are built on a few primitive predicates.** The orientation test asks whether point c is left of, right of, or on the directed line from a to b; it is the sign of the 2×2 determinant (b − a) × (c − a). In-circle tests decide whether a point lies inside a circle through three others. Convex hull, segment intersection, triangulation and point location all reduce to sequences of such sign evaluations, so their correctness is only as good as the predicates.

2. **Convex hull is sorting in disguise, so it needs Ω(n log n).** The convex hull of n points is the smallest convex polygon containing them. Graham's scan sorts points by angle and walks them with a stack, popping any point that makes a right turn: O(n log n). Andrew's monotone chain does the same after sorting by x. Since sorting n numbers reduces to computing the hull of the points (x, x²), which lie on a parabola, the hull needs Ω(n log n) in the algebraic decision-tree model. Output-sensitive algorithms (Chan, 1996) achieve O(n log h), where h is the number of hull vertices.

3. **Plane sweep turns a 2D problem into a sequence of 1D problems.** Move a vertical line across the plane, stopping at events (endpoints, intersections) held in a priority queue, and maintain the objects crossing the line in a balanced search tree ordered by y. Only neighbours in that order can intersect next. Bentley–Ottmann finds all k intersections among n segments in O((n + k) log n), instead of checking all Θ(n²) pairs.

4. **Divide and conquer and duality give further O(n log n) algorithms.** The closest pair of n points is found by splitting at the median x, solving each half, and checking a narrow strip where only a constant number of neighbours per point need testing: O(n log n). Duality transforms swap points and lines, turning one problem into an easier equivalent.

5. **Voronoi diagrams and Delaunay triangulations are the fundamental proximity structures.** The Voronoi diagram partitions the plane into regions of points closest to each site; its dual, the Delaunay triangulation, connects sites whose regions touch and maximises the minimum angle among all triangulations. Both have O(n) size and are built in O(n log n) (Fortune's sweep, or randomized incremental construction). They answer nearest-neighbour queries, generate good meshes for simulation, and contain the Euclidean minimum spanning tree.

6. **Spatial data structures answer range and nearest-neighbour queries.** k-d trees split space alternately by coordinate at medians: O(n log n) to build, O(√n + k) for an orthogonal range query in 2D, good average nearest-neighbour queries in low dimension. Range trees reach O(log² n + k) at O(n log n) space. Quadtrees, R-trees (used in spatial databases) and Bounding Volume Hierarchies (BVHs, used in ray tracing) organise objects hierarchically by bounding boxes.

7. **High dimensions defeat exact methods.** In d dimensions, convex hulls can have Θ(n^⌊d/2⌋) facets, and k-d trees degrade towards linear scan once d exceeds roughly 10–20 (the *curse of dimensionality*). For the high-dimensional vectors of machine learning (embeddings with hundreds of dimensions), practice uses *approximate* nearest-neighbour methods: locality-sensitive hashing, graph-based indexes such as Hierarchical Navigable Small World (HNSW), and quantisation.

8. **Floating point breaks naive geometric code.** Rounding can make an orientation test report that a is left of bc, b left of ca, and c left of ab, an impossible configuration that can send a hull or triangulation algorithm into an infinite loop or yield crossing edges. Remedies are exact arithmetic for predicates (adaptive-precision floating point, as in Shewchuk's predicates, which are fast because they use extra precision only when the fast result is uncertain), exact rational or algebraic number types, and symbolic perturbation to handle degenerate inputs such as collinear points. The algorithm's combinatorial logic must never depend on an inconsistently rounded sign.

## Key concepts

| Term | Meaning |
|---|---|
| Orientation predicate | Sign of a determinant telling whether three points turn left, right, or are collinear |
| Convex hull | Smallest convex set containing a set of points |
| Plane sweep | Process events in order of a moving line while maintaining an ordered status structure |
| Voronoi diagram | Partition of the plane into regions nearest to each site |
| Delaunay triangulation | Dual of the Voronoi diagram; no site lies inside any triangle's circumcircle |
| k-d tree | Binary space partition alternating split coordinates |
| Output-sensitive algorithm | Running time depends on output size as well as input size |
| Robust predicate | Geometric test that returns the exact sign despite floating-point rounding |

## How it fits

- **Below:** coordinates, determinants and transformations from [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md); [floating-point](../../03-digital-logic/01-number-representation/floating-point.md) rounding causes the robustness problem; algorithms use [sorting](../04-sorting-and-searching/comparison-sorting.md), [search trees](../02-fundamental-data-structures/search-trees.md), [heaps](../02-fundamental-data-structures/heaps-and-priority-queues.md) and [divide and conquer](../03-design-paradigms/divide-and-conquer.md).
- **Above:** [graphics geometry](../../14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md), clipping in the [rasterization pipeline](../../14-human-and-visual-computing/02-computer-graphics/rasterization-pipeline.md), BVHs in [ray tracing](../../14-human-and-visual-computing/02-computer-graphics/ray-tracing-and-global-illumination.md), [computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md), robot motion [planning](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md) via configuration spaces, nearest-neighbour search over embeddings in [supervised](../../13-artificial-intelligence/02-machine-learning-foundations/supervised-learning.md) and [unsupervised learning](../../13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md), and spatial indexes in [databases](../../09-data-management/01-data-models/non-relational-models.md).
- **Siblings:** geometric structure (Euclidean distances) enables [approximation schemes](approximation-algorithms.md); large spatial datasets need [external-memory](external-memory-and-cache-oblivious.md) structures such as R-trees.

## Common misconceptions

- **"Geometry is just applying formulas."** The hard part is combinatorial consistency under rounding and degenerate inputs.
- **"k-d trees solve nearest neighbours."** In low dimensions; in high dimensions they approach linear scan, and approximate methods are needed.
- **"Using doubles with an epsilon tolerance makes it robust."** Epsilon comparisons are not transitive and can still yield inconsistent decisions; robust predicates or exact arithmetic are required.

## Go deeper

- Mark de Berg, Otfried Cheong, Marc van Kreveld, Mark Overmars, *Computational Geometry: Algorithms and Applications* (3rd ed., 2008): the standard text.
- Franco P. Preparata and Michael I. Shamos, *Computational Geometry: An Introduction* (1985): the founding textbook.
- Jonathan R. Shewchuk, "Adaptive Precision Floating-Point Arithmetic and Fast Robust Geometric Predicates" (1997).
