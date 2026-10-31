# Distributions

> **Layer:** [09 Advanced Analysis](../README.md) › [Harmonic Analysis](README.md)
> **Builds on:** [The Fourier Transform](the-fourier-transform.md), [Banach Spaces](../03-functional-analysis/banach-spaces.md), [The Lebesgue Integral](../01-measure-and-integration/the-lebesgue-integral.md), [The Fundamental Theorem of Calculus](../../06-real-analysis/02-calculus-of-one-variable/the-fundamental-theorem-of-calculus.md)
> **Enables:** [Weak Solutions and Sobolev Spaces](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md), [Laplace's Equation and Harmonic Functions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md), [The Wave Equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-wave-equation.md), [The Mathematics of Quantum Mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md)

## Essence

Physicists and engineers used the Dirac delta, a "function" that is zero except at one point yet has integral 1, long before anyone could say what it was. Laurent Schwartz's theory of distributions, developed in the late 1940s, made it rigorous by changing the question: instead of asking for the value of a generalised function at a point, ask only how it acts on smooth test functions. In that world every locally integrable function, every measure and the delta are all distributions, every distribution can be differentiated infinitely often, and the Fourier transform applies to constants and polynomials. The price is that distributions cannot in general be multiplied.

## Core tenets

1. **A distribution is a continuous linear functional on test functions.** The test functions D(ℝⁿ) are the smooth functions with compact support, with a notion of convergence demanding uniform convergence of every derivative on a fixed compact set. A distribution is a linear map T : D → ℂ that is continuous in this sense. A locally integrable f defines the distribution φ ↦ ∫ f·φ, and two functions define the same distribution only if they agree almost everywhere, so functions sit inside distributions. The Dirac delta is δ(φ) = φ(0); no function f has ∫ f·φ = φ(0) for all φ, since such an f would vanish almost everywhere away from 0.

2. **Differentiation is defined by moving the derivative onto the test function.** For a smooth f, integration by parts gives ∫ f′·φ = −∫ f·φ′, since φ vanishes outside a bounded set. So one defines T′(φ) = −T(φ′) for every distribution, and that is again a distribution. Examples: the Heaviside step H, equal to 1 for x > 0 and 0 otherwise, has derivative δ, because −∫₀^∞ φ′ = φ(0). The function ∣x∣ has derivative sign x, and sign x has derivative 2δ. The derivative of δ is φ ↦ −φ′(0). Locally, every distribution is a derivative of some continuous function.

3. **Weak derivatives give equations a meaning for rough solutions.** A function u is a weak solution of a linear differential equation Lu = f if the identity holds as distributions, that is, after integration against every test function. The wave equation u_tt = u_xx has the solution u = H(x − t), a travelling step, which satisfies the equation weakly though it is not differentiable. [Sobolev spaces](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md), introduced by Sergei Sobolev in the 1930s, consist of functions whose distributional derivatives up to some order are in Lᵖ, and they are where modern existence theory for partial differential equations takes place.

4. **Fundamental solutions turn equations into convolutions.** A fundamental solution of an operator L is a distribution E with LE = δ. Then u = E ∗ f solves Lu = f, because L commutes with convolution and δ ∗ f = f. For the Laplacian, E(x) = (1/2π)·log ∣x∣ in ℝ² and E(x) = −1/(4π∣x∣) in ℝ³: the Newtonian potential of a point mass or charge. That is why the potential of any mass distribution is a convolution with 1/∣x∣, the basis of [Laplace's equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md). The Malgrange–Ehrenpreis theorem of the mid-1950s says every non-zero linear differential operator with constant coefficients has a fundamental solution. Constant coefficients matter: Hans Lewy found in 1957 a simple operator with variable coefficients for which Lu = f has no solution, even as a distribution, for most smooth f.

5. **Tempered distributions carry the Fourier transform.** The Schwartz space 𝒮 consists of smooth functions which, with all derivatives, decay faster than any power of ∣x∣; the Fourier transform maps 𝒮 bijectively onto itself. Its dual, the tempered distributions, includes all polynomials, all Lᵖ functions and δ. The transform extends by duality, T̂(φ) = T(φ̂), justified by ∫ f̂·φ = ∫ f·φ̂ for functions. Then δ̂ = 1 and 1̂ = δ: a perfect spike contains all frequencies equally, and a constant has only frequency 0. The function e^(x) is not tempered, because it grows too fast to pair with every element of 𝒮.

6. **Distributions cannot in general be multiplied.** The product of a smooth function and a distribution is fine: (gT)(φ) = T(gφ). But no extension of multiplication to all distributions can be associative, commutative and compatible with differentiation and the ordinary product of continuous functions; Schwartz gave this impossibility result in the 1950s. The obstruction is concrete: δ² has no sensible meaning, since the squares of approximations to δ have integrals tending to infinity. This is why nonlinear equations with rough data are hard, and why quantum field theory, which needs products of distributions at the same point, requires renormalisation.

7. **The theory unified analysis and was quickly rewarded.** Schwartz received the Fields Medal in 1950 for it. Its language now pervades partial differential equations, harmonic analysis and mathematical physics: Green's functions are fundamental solutions, impulse responses in engineering are responses to δ, and the idealised [quantum states](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) of definite position are δ-like distributions outside L².

## Key concepts

| Term | Meaning |
|---|---|
| Test function | A smooth function with compact support |
| Distribution | A continuous linear functional on test functions |
| Dirac delta δ | The distribution φ ↦ φ(0) |
| Distributional derivative | T′(φ) = −T(φ′) |
| Weak solution | A solution of an equation in the sense of distributions |
| Fundamental solution | A distribution E with LE = δ |
| Schwartz space 𝒮 | Smooth functions decaying rapidly with all derivatives |
| Tempered distribution | A continuous linear functional on 𝒮; it has a Fourier transform |

## How it fits

- **Below:** [integration by parts](../../06-real-analysis/02-calculus-of-one-variable/the-fundamental-theorem-of-calculus.md) from 06 motivates the definition; the [Lebesgue integral](../01-measure-and-integration/the-lebesgue-integral.md) embeds functions; [dual spaces](../03-functional-analysis/banach-spaces.md) supply the framework; the [Fourier transform](the-fourier-transform.md) extends to tempered distributions.
- **Above:** [weak solutions and Sobolev spaces](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md), [Laplace's equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md) and the [wave equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-wave-equation.md) in 10; [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) in 14.
- **Siblings:** [Fourier series](fourier-series.md) of distributions converge in the distributional sense even when they diverge pointwise; [Fourier analysis on groups](fourier-analysis-on-groups.md) has a distributional version for the Poisson summation formula, ∑ δₙ having transform ∑ δₖ.

## Common misconceptions

- **"The delta function is a function that is infinite at 0"**: no function does what δ does; it is a functional.
- **"Distributions are just limits of functions"**: they are limits of smooth functions, but the definition is by action on test functions, which is what makes calculus work.
- **"Any two distributions can be multiplied"**: only special pairs; δ² is meaningless.

## Go deeper

- Robert S. Strichartz, *A Guide to Distribution Theory and Fourier Transforms* (1994): a short, intuitive introduction.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (1983): the definitive treatment.
- Gerd Grubb, *Distributions and Operators* (2009): a careful modern textbook linking distributions to differential operators.
