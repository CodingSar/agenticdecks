# The Mathematics of Deep Learning

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Data and Learning](README.md)
> **Builds on:** [Statistical Learning Theory](statistical-learning-theory.md), [High-Dimensional Geometry and Random Matrices](high-dimensional-geometry-and-random-matrices.md), [Gradient Methods](../02-optimisation/gradient-methods.md), [The Derivative as a Linear Map](../../06-real-analysis/04-calculus-of-several-variables/the-derivative-as-a-linear-map.md), [Hahn–Banach and Baire Category](../../09-advanced-analysis/03-functional-analysis/hahn-banach-and-baire-category.md)
> **Enables:** [Computers and Proof](../../15-mathematics-in-context/computers-and-proof.md), [Mathematics and Society](../../15-mathematics-in-context/mathematics-and-society.md), [Neural Networks and Backpropagation (CS)](../../../cs-first-principles/13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md), [Training at Scale (CS)](../../../cs-first-principles/13-artificial-intelligence/03-deep-learning/training-at-scale.md)

## Essence

A neural network is a composition of simple maps: f(x) = W_L σ(⋯ σ(W₁x + b₁) ⋯) + b_L, where the W's are matrices, the b's vectors and σ a fixed nonlinear function applied coordinate by coordinate. Training fits billions of parameters to data by gradient descent. Three questions organise the mathematics: can such networks represent the functions we want (approximation), can gradient descent find good parameters (optimisation), and why do the results work on new data (generalisation)? The first is largely answered, the second partly, and the third is mostly open.

## Core tenets

1. **One hidden layer can approximate any continuous function on a compact set.** George Cybenko (1989) proved that sums ∑ aᵢ σ(wᵢ · x + bᵢ) with a sigmoidal σ are dense in the continuous functions on a compact K in ℝ^d; Kurt Hornik and coauthors gave a general version the same year. Proof idea: if the sums were not dense, the Hahn–Banach theorem would give a nonzero bounded linear functional vanishing on all of them; by the Riesz representation theorem it is a signed measure μ with ∫ σ(w · x + b) dμ = 0 for all w, b, and one shows this forces μ = 0. Moshe Leshno and coauthors (1993) showed that for continuous σ, density holds if and only if σ is not a polynomial: polynomials of bounded degree form a finite-dimensional, hence closed, space.

2. **Universal approximation says nothing about size, training or generalisation.** Approximating an arbitrary Lipschitz function in d variables to accuracy ε can need a number of neurons growing like ε^(−d), exponential in dimension. Andrew Barron (1993) identified a class, functions whose Fourier transform has a finite first moment, approximable with error of order 1/√n by n neurons regardless of d. Depth helps: there are functions computed by small deep networks that any shallow network needs exponentially many neurons to approximate.

3. **Backpropagation is the chain rule evaluated in the efficient order.** The derivative of a composition is the product of the layers' Jacobian matrices. For a scalar loss, multiplying from the output end means each step is a vector times a Jacobian, never a matrix product, so the whole gradient costs a small constant multiple of one forward evaluation, whatever the number of parameters. This is reverse-mode automatic differentiation; David Rumelhart, Geoffrey Hinton and Ronald Williams (1986) popularised it for training networks.

4. **The loss is non-convex, yet its landscape is more benign than feared.** For deep linear networks, f(x) = W_L ⋯ W₁x with squared loss and mild conditions on the data, every local minimum is global, although saddle points exist. For smooth losses, gradient descent with a small fixed step from a random start almost surely avoids strict saddles, points where the Hessian has a negative eigenvalue, because the set of starts converging to them has measure zero by the stable manifold theorem. For general nonlinear networks no complete description is known.

5. **Very wide networks train like kernel methods, but real networks do more.** In the neural tangent kernel (NTK) limit (Arthur Jacot, Franck Gabriel and Clément Hongler, 2018), as width tends to infinity with suitable scaling, parameters move so little that the network stays close to its linearisation at initialisation; training becomes kernel regression with a fixed kernel and provably reaches zero training loss. This "lazy" regime learns no new features, while practical networks do.

6. **Classical capacity bounds cannot explain generalisation, and double descent shows why.** Chiyuan Zhang and coauthors (2017) showed that standard image networks fit randomly relabelled data perfectly, so any bound depending only on the class's capacity is vacuous. Mikhail Belkin and coauthors (2019) described double descent: as the number of parameters p grows past the number of samples n, test error first falls, peaks at p ≈ n, then falls again. In linear regression the peak is explained exactly: the minimum-norm solution divides by the smallest singular value of the data matrix, which by the Marchenko–Pastur law tends to 0 when p/n tends to 1.

7. **Gradient descent has an implicit bias toward simple solutions.** On underdetermined least squares, gradient descent started at zero stays in the row space of the data and converges to the minimum-norm interpolant. On linearly separable data with logistic loss, its direction converges to the maximum-margin separator. Such biases, not the parameter count, control generalisation in these models.

8. **What remains open as of 2026.** There is no accepted theory that predicts the test error of practical networks, explains feature learning, or accounts for the success of stochastic gradient descent on real architectures. Scaling laws, in which loss falls as a power of model size, data and compute, are empirical regularities, not theorems.

## Key concepts

| Term | Meaning |
|---|---|
| Activation function σ | The fixed nonlinearity applied coordinate-wise between layers |
| Universal approximation | Density of network functions in the continuous functions on compact sets |
| Backpropagation | Reverse-mode computation of the gradient by the chain rule |
| Strict saddle | A critical point at which the Hessian has a negative eigenvalue |
| Neural tangent kernel | The kernel governing training of very wide networks near initialisation |
| Double descent | Test error that falls, peaks at the threshold, then falls again |
| Implicit bias | The preference of an optimiser among the many zero-loss solutions |

## How it fits

- **Below:** the derivative as a linear map gives backpropagation, Hahn–Banach gives approximation, gradient methods train, and random matrices explain double descent.
- **Above:** [computers and proof](../../15-mathematics-in-context/computers-and-proof.md) discusses networks used in mathematical research; [mathematics and society](../../15-mathematics-in-context/mathematics-and-society.md) discusses automated decisions.
- **Siblings:** [statistical learning theory](statistical-learning-theory.md) supplies bounds that overparameterised networks break; [compressed sensing](sampling-and-compressed-sensing.md) is the cleanest case of recovery by implicit norm minimisation; [optimal transport](optimal-transport.md) supplies Wasserstein losses for generative models.

## Common misconceptions

- **"Universal approximation explains why deep learning works."** It shows only that suitable parameters exist; polynomials have the same property.
- **"Backpropagation is a special learning algorithm."** It is the chain rule, computed in the cheap order; the learning algorithm is gradient descent.
- **"Overparameterised models must overfit."** Implicit bias and double descent show that models with more parameters than data can generalise well.

## Go deeper

- I. Goodfellow, Y. Bengio and A. Courville, *Deep Learning* (2016): the standard broad textbook.
- D. A. Roberts, S. Yaida and B. Hanin, *The Principles of Deep Learning Theory* (2022): an effective-theory treatment of wide networks.
- M. Belkin, D. Hsu, S. Ma and S. Mandal, "Reconciling Modern Machine-Learning Practice and the Classical Bias–Variance Trade-Off" (2019): the double-descent paper.
