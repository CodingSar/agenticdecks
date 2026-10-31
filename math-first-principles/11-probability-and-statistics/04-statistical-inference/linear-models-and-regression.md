# Linear Models and Regression

> **Layer:** [11 Probability and Statistics](../README.md) › [Statistical Inference](README.md)
> **Builds on:** [Inner Products and Orthogonality](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md), [Quadratic Forms and Positive Definiteness](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md), [Singular Value Decomposition](../../04-linear-algebra/03-inner-product-spaces/singular-value-decomposition.md), [Estimation and Likelihood](estimation-and-likelihood.md), [Conditional Expectation](../01-measure-theoretic-probability/conditional-expectation.md)
> **Enables:** [Numerical Linear Algebra](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-linear-algebra.md), [Statistical Learning Theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md), [Sampling and Compressed Sensing](../../14-applied-and-computational-mathematics/06-data-and-learning/sampling-and-compressed-sensing.md), [Regression Adjustment and Survival Analysis](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md), [Supervised Learning](../../../cs-first-principles/13-artificial-intelligence/02-machine-learning-foundations/supervised-learning.md)

## Essence

The linear model explains a response by a weighted sum of predictors plus noise: Y = Xβ + ε, where Y is a vector of n observations, X an n × p matrix of known predictors, β an unknown vector of p coefficients and ε random errors with mean 0. Least squares chooses β to minimise the squared length of Y − Xβ, and geometrically this is orthogonal projection of Y onto the column space of X. Almost every property follows from that picture: the normal equations, the decomposition of variance, the Gauss–Markov optimality theorem, and, with normal errors, exact tests. Regression is the most used tool in applied statistics and the prototype for much of machine learning.

## Core tenets

1. **Least squares is orthogonal projection.** The residual Y − Xβ̂ is shortest when it is orthogonal to every column of X, which gives the normal equations Xᵀ(Y − Xβ̂) = 0. When X has full column rank,

   ```
   β̂ = (XᵀX)⁻¹XᵀY,      Ŷ = Xβ̂ = HY   with   H = X(XᵀX)⁻¹Xᵀ.
   ```

   The hat matrix H is the orthogonal projection onto the column space: H² = H = Hᵀ, and its trace is p.

2. **Pythagoras splits the variation.** When X contains a column of ones, so that the model has an intercept, the vectors Ŷ − Ȳ·1 and Y − Ŷ are orthogonal, and with Ȳ the mean of Y:

   ```
   ∑(Yᵢ − Ȳ)²   =   ∑(Ŷᵢ − Ȳ)²   +   ∑(Yᵢ − Ŷᵢ)²
    total            explained        residual (RSS)
   ```

   The coefficient of determination R² is the explained share, the squared cosine of the angle between Y − Ȳ·1 and its projection. This is the analysis of variance, and the sample version of the conditional variance decomposition.

3. **The Gauss–Markov theorem: least squares is the best linear unbiased estimator (BLUE).** If the errors are uncorrelated with common variance σ², so that Cov(ε) = σ²I, then for any other linear unbiased estimator CY of β, Cov(CY) − Cov(β̂) is positive semi-definite. Proof: write C = (XᵀX)⁻¹Xᵀ + D; unbiasedness forces DX = 0, and then Cov(CY) = σ²(XᵀX)⁻¹ + σ²DDᵀ. Carl Friedrich Gauss proved it in his work on least squares of 1821–1823; normality is not assumed.

4. **The theorem's hypotheses are where practice goes wrong.** If Cov(ε) = σ²Σ for a known positive definite Σ, the best estimator is generalised least squares, (XᵀΣ⁻¹X)⁻¹XᵀΣ⁻¹Y, which is ordinary least squares after whitening by Σ^(−1/2) (Alexander Aitken, 1935). If a predictor correlated with those included is omitted, the estimates are biased, and the bias does not shrink with more data. If columns of X are nearly collinear, XᵀX is nearly singular and the variance of β̂ explodes.

5. **With normal errors, the geometry gives exact distributions.** If ε is normal with covariance σ²I, then β̂ is normal with covariance σ²(XᵀX)⁻¹, the residual sum of squares RSS satisfies RSS/σ² ~ χ² with n − p degrees of freedom, and it is independent of β̂, because the residual lies in the orthogonal complement of the column space. Hence s² = RSS/(n − p) is unbiased for σ², each coefficient divided by its standard error has a t distribution, and comparisons of nested models use F tests. Least squares is then also the maximum likelihood estimator.

6. **Regression is named after a phenomenon, and it estimates a conditional expectation.** Francis Galton (1886) found that children of very tall parents are on average tall, but less extreme than their parents: "regression towards mediocrity". This is not a biological force but a property of any imperfect correlation, since the best linear predictor of standardised Y from standardised X is ρX with ∣ρ∣ < 1. In general, least squares in the population is the projection of Y onto linear functions of X, and E[Y ∣ X] is the projection onto all functions of X.

7. **Computation and regularisation make it usable at scale.** One should never form (XᵀX)⁻¹: a QR factorisation, or the singular value decomposition (SVD) X = UΣVᵀ, solves the problem stably, and the SVD also exposes collinearity as small singular values. Ridge regression (Arthur Hoerl and Robert Kennard, 1970) adds λ·∣β∣² to the criterion, giving (XᵀX + λI)⁻¹XᵀY, always well defined. The lasso (Robert Tibshirani, 1996) penalises the sum of absolute values instead and sets many coefficients exactly to 0, which makes regression possible when p exceeds n.

## Key concepts

| Term | Meaning |
|---|---|
| Design matrix X | The n × p matrix of predictor values |
| Normal equations | XᵀXβ = XᵀY, the condition that the residual is orthogonal to the columns |
| Hat matrix H | X(XᵀX)⁻¹Xᵀ, the projection that maps Y to fitted values |
| Residual sum of squares | ∑(Yᵢ − Ŷᵢ)², the squared length of the residual |
| R² | Explained variation divided by total variation |
| BLUE | Best linear unbiased estimator, smallest covariance among linear unbiased estimators |
| Generalised least squares | Least squares after transforming to uncorrelated errors |
| Ridge and lasso | Least squares penalised by the squared length or the sum of absolute values of β |

## How it fits

- **Below:** [orthogonal projection](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md), [positive definite forms](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md) and the [singular value decomposition](../../04-linear-algebra/03-inner-product-spaces/singular-value-decomposition.md) of 04 are the whole machinery; [conditional expectation](../01-measure-theoretic-probability/conditional-expectation.md) is the infinite-dimensional version.
- **Above:** stable solution of least squares is a core topic of [numerical linear algebra](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-linear-algebra.md); sparse regression underlies [compressed sensing](../../14-applied-and-computational-mathematics/06-data-and-learning/sampling-and-compressed-sensing.md); adjustment for confounders in medicine is [regression](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md).
- **Siblings:** with normal errors, least squares is [maximum likelihood](estimation-and-likelihood.md); its t and F tests are [Neyman–Pearson tests](hypothesis-tests-and-confidence-intervals.md); ridge is the posterior mode under a normal prior in [Bayesian inference](bayesian-inference.md); [the bootstrap](nonparametric-statistics-and-the-bootstrap.md) resamples cases or residuals.

## Common misconceptions

- **"A regression coefficient measures a causal effect"**: it measures association holding the other included predictors fixed. Omitted confounders bias it, and causal interpretation needs design or further assumptions.
- **"Least squares needs normal data"**: Gauss–Markov needs only uncorrelated errors of equal variance. Normality is needed for exact small-sample tests.
- **"A high R² means a good model"**: R² never falls when predictors are added, and a model can fit past data closely while predicting badly or being misspecified.

## Go deeper

- George Seber and Alan Lee, *Linear Regression Analysis* (2nd edition, 2003): the theory of the linear model in full.
- Trevor Hastie, Robert Tibshirani and Jerome Friedman, *The Elements of Statistical Learning* (2nd edition, 2009): regression, ridge and lasso as learning methods.
- Andrew Gelman, Jennifer Hill and Aki Vehtari, *Regression and Other Stories* (2020): regression as it is practised, with attention to causal pitfalls.
