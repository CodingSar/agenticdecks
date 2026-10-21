# Linear Algebra

> **Layer:** [01 Mathematical Foundations](../README.md) › [Algebra](README.md)
> **Builds on:** [Abstract Algebra](abstract-algebra.md), [Functions and Cardinality](../02-sets-relations-functions/functions-and-cardinality.md)
> **Enables:** [Neural Networks and Backpropagation](../../13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md), [Geometry and Transformations](../../14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md), [SIMD and GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md), [Unsupervised Learning](../../13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md), [Qubits and Quantum Circuits](../../02-theory-of-computation/05-quantum-computation/qubits-and-quantum-circuits.md)

## Essence

Linear algebra studies vectors, and the functions between vector spaces that preserve addition and scaling: linear maps, represented by matrices. Its central fact is that a linear map is completely determined by what it does to a basis, so an infinite set of input-output pairs collapses to a finite grid of numbers. That makes linearity the one large class of problems that computers solve reliably and fast. Graphics transforms points with 4×4 matrices; a neural network is mostly matrix multiplications with simple nonlinearities in between; search engines rank pages with an eigenvector; quantum states are unit vectors. Modern hardware, from Single Instruction, Multiple Data (SIMD) units to Graphics Processing Units (GPUs) and tensor accelerators, is shaped around multiplying matrices.

## Core tenets

1. **Linear maps are determined by a basis, so matrices represent them exactly.** If `f(ax + by) = af(x) + bf(y)`, then knowing `f` on *n* basis vectors determines it everywhere. Writing those images as columns gives an *m×n* matrix, and applying `f` is matrix-vector multiplication. Composition of maps is matrix multiplication, which is why multiplication is defined row-by-column and why it is associative but not commutative (rotating then translating differs from translating then rotating).

2. **Rank and the null space say what is lost.** The rank of a matrix is the dimension of its image; the null space is the set of inputs mapped to zero. Rank + nullity = number of columns. A system *Ax = b* has a solution iff *b* is in the column space, and the solution is unique iff the null space is {0}. In machine learning (ML), a feature matrix with dependent columns has no unique least-squares fit, which is the reason for regularisation.

3. **Gaussian elimination solves linear systems in O(n³), but conditioning governs accuracy.** Row operations reduce *A* to triangular form (an LU factorisation), giving solutions, determinants and inverses. In floating point, the *condition number* κ(A) bounds how much input error is amplified: with κ ≈ 10^k you lose about *k* decimal digits. Numerical code therefore avoids forming inverses explicitly, pivots for stability, and prefers orthogonal methods (QR) when accuracy matters.

4. **Inner products give geometry: length, angle, projection.** The dot product `x·y = Σ xᵢyᵢ` gives length (√(x·x)) and angle (cosine similarity). Projecting *b* onto the column space of *A* gives the least-squares solution of *Ax ≈ b*, the basis of linear regression and curve fitting. Orthogonal matrices preserve lengths and angles, so they are numerically stable and describe rotations.

5. **Eigenvectors are directions a map only stretches.** If *Av = λv*, repeated application multiplies *v* by λ^k. So the long-run behaviour of any linear iteration is governed by its largest eigenvalue. PageRank is the dominant eigenvector of the web's link matrix, [Markov chains](../06-probability-and-statistics/markov-chains.md) converge to an eigenvector with eigenvalue 1, and the convergence rate of iterative solvers and of gradient descent on a quadratic depends on the ratio of extreme eigenvalues.

6. **The Singular Value Decomposition (SVD) factors every matrix into rotate–scale–rotate.** Any matrix is *A = UΣVᵀ* with *U*, *V* orthogonal and Σ diagonal and non-negative. Truncating to the *k* largest singular values gives the best rank-*k* approximation (Eckart–Young theorem). This is Principal Component Analysis (PCA), latent semantic indexing, low-rank compression of models, and the reason a few hundred dimensions can capture most of the structure of very high-dimensional data.

7. **Homogeneous coordinates make translation linear.** Translation `x ↦ x + t` is not linear in 3D, but adding a fourth coordinate fixed at 1 turns it into a 4×4 matrix. Rotation, scaling, translation and perspective projection then compose by matrix multiplication, so a whole scene transform is one matrix per object. This is the core of the [graphics pipeline](../../14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md).

8. **Matrix multiplication is the computational workhorse, and its cost structure shapes hardware.** Multiplying two *n×n* matrices does about 2n³ floating-point operations on 3n² data, so arithmetic per byte grows with *n*. That high arithmetic intensity is why blocked matrix multiply can approach peak hardware speed while most other code is memory-bound, and why [GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) and [accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md) dedicate most of their silicon to it. Asymptotically faster algorithms exist (Strassen, 1969, O(n^2.81)), but practical libraries mostly use the cubic algorithm with careful blocking.

## Key concepts

| Term | Meaning |
|---|---|
| Vector space | Set closed under addition and scalar multiplication over a field |
| Basis / dimension | Minimal spanning set / its size |
| Linear map | Function preserving addition and scaling; a matrix in coordinates |
| Rank | Dimension of the image (column space) |
| Null space | Inputs mapped to zero |
| Inner product | Gives lengths, angles and orthogonality |
| Eigenvalue / eigenvector | λ and v ≠ 0 with Av = λv |
| SVD | A = UΣVᵀ; singular values measure stretch along orthogonal axes |
| Condition number | Ratio of largest to smallest singular value; error amplification factor |
| Tensor | Multi-dimensional array; in ML, a batch of vectors or matrices |

## How it fits

- **Below:** Vector spaces are defined over a field from [abstract algebra](abstract-algebra.md) (real numbers for geometry and ML, complex numbers for quantum computing, GF(2), the two-element Galois field, for coding theory).
- **Above:** [Neural networks](../../13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md), [attention](../../13-artificial-intelligence/03-deep-learning/attention-and-transformers.md) and [unsupervised learning](../../13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md) are linear algebra plus nonlinearity. [Computer graphics](../../14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md) and [computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md) transform points with matrices. [Quantum circuits](../../02-theory-of-computation/05-quantum-computation/qubits-and-quantum-circuits.md) are unitary matrices acting on state vectors. Linear error-correcting codes are subspaces over GF(2). [Media compression](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md) uses orthogonal transforms such as the discrete cosine transform ([Fourier analysis](../05-continuous-mathematics/fourier-analysis.md)).
- **Siblings:** [Abstract algebra](abstract-algebra.md) supplies fields; [Boolean algebra](boolean-algebra.md) over GF(2) is linear algebra when exclusive OR (XOR) is the addition. [Calculus](../05-continuous-mathematics/calculus.md) linearises nonlinear functions with the Jacobian matrix, and [optimization](../05-continuous-mathematics/optimization.md) uses eigenvalues of the Hessian to describe curvature.

## Common misconceptions

- **"To solve Ax = b, compute A⁻¹ and multiply."** It is slower and less accurate than factorising; numerical libraries almost never form the inverse.
- **"Matrix multiplication is commutative."** AB and BA generally differ, and the order of transforms changes the result.
- **"High-dimensional data needs all its dimensions."** Real data often has rapidly decaying singular values, so a low-rank approximation keeps most of the information.

## Go deeper

- Gilbert Strang, *Introduction to Linear Algebra* (6th ed., 2023): the standard applied introduction.
- Sheldon Axler, *Linear Algebra Done Right* (4th ed., 2024): the structural, basis-free view.
- Lloyd Trefethen and David Bau, *Numerical Linear Algebra* (1997): conditioning, stability and the SVD as used in computation.
