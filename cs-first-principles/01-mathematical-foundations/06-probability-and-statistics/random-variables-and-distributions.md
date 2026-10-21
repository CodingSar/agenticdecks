# Random Variables and Distributions

> **Layer:** [01 Mathematical Foundations](../README.md) › [Probability and Statistics](README.md)
> **Builds on:** [Probability](probability.md), [Calculus](../05-continuous-mathematics/calculus.md)
> **Enables:** [Statistical Inference](statistical-inference.md), [Latency, Bandwidth and Queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md), [Randomized Algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md), [Generative Models](../../13-artificial-intelligence/04-advanced-paradigms/generative-models.md), [Reliability Engineering](../../12-software-engineering/04-operations/reliability-engineering.md)

## Essence

A random variable is a function that assigns a number to each outcome of a random experiment: the latency of a request, the number of collisions in a hash table, the bit error count in a frame. Its *distribution* says how likely each value is, and summaries such as the mean (expectation) and variance compress that into a centre and a spread. A small family of standard distributions (Bernoulli, binomial, geometric, Poisson, exponential, normal, and heavy-tailed ones such as Pareto) arises again and again because they are the natural results of simple mechanisms: independent trials, memoryless waiting, sums of many small effects, and multiplicative or rich-get-richer growth. Knowing which mechanism produced your data tells you which distribution to expect and which summaries can be trusted.

## Core tenets

1. **A random variable is a function, and its distribution is what matters.** X: Ω → ℝ. Two different experiments can produce variables with the same distribution, and for most purposes they are interchangeable. A discrete variable has a probability mass function; a continuous one has a density whose integral over an interval gives a probability ([calculus](../05-continuous-mathematics/calculus.md)). The Cumulative Distribution Function (CDF), P(X ≤ x), works for both.

2. **Expectation is linear, even without independence.** E[X + Y] = E[X] + E[Y] always. Writing a complicated count as a sum of simple 0/1 indicator variables and adding their expectations is the single most powerful trick in algorithm analysis. For example, the expected number of colliding pairs when *n* keys hash into *m* slots is C(n, 2)/m, with no need to understand the joint distribution of collisions.

3. **Variance measures spread, and adds only for independent variables.** Var(X) = E[(X − E[X])²]. For independent variables, Var(X + Y) = Var(X) + Var(Y), so the standard deviation of a sum of *n* independent copies grows like √n while the mean grows like *n*. Averages therefore become relatively more precise as *n* grows, which is why sampling-based estimates, load balancing over many requests and statistical multiplexing in networks work.

4. **Tail bounds turn means into guarantees.** Markov's inequality P(X ≥ a) ≤ E[X]/a needs only non-negativity. Chebyshev's uses variance: P(|X − μ| ≥ kσ) ≤ 1/k². Chernoff bounds, for sums of independent bounded variables, give tails that fall *exponentially* in the deviation. Chernoff bounds are what prove "with high probability" statements about randomized algorithms, load balance and sketches.

5. **Standard distributions come from standard mechanisms.** Repeated independent yes/no trials give the binomial; waiting for the first success gives the geometric. Many rare independent events in a fixed window (requests per second from many users) give the Poisson. The waiting time between Poisson events is exponential, which is *memoryless*: having waited does not shorten the remaining wait. These assumptions underpin classical [queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) models such as M/M/1, whose mean time in the system 1/(μ − λ) explodes as utilisation λ/μ approaches 1.

6. **Sums of many small independent effects are approximately normal.** The Central Limit Theorem (CLT) says the standardised sum of *n* independent, identically distributed variables with finite variance approaches a normal (Gaussian) distribution. That is why measurement noise, averaged benchmark results and aggregated traffic often look bell-shaped, and why confidence intervals use the normal distribution. The finite-variance condition is essential.

7. **Heavy tails break averages, and systems are full of them.** In a heavy-tailed distribution (Pareto, log-normal), extreme values are far more likely than a normal distribution predicts, and for some Pareto parameters the variance or even the mean is infinite. File sizes, flow sizes on the Internet, request latencies and popularity of web pages are heavy-tailed. Consequences: the mean latency hides the tail, so engineers report percentiles (p99, p99.9); a request that fans out to 100 servers and waits for all of them exceeds one server's 99th-percentile latency about 63% of the time (1 − 0.99^100); and a few elephant flows carry most of the bytes.

8. **Sampling from distributions is a computational primitive.** Inverse-transform sampling turns a uniform random number *U* into any distribution by computing CDF⁻¹(U). Monte Carlo methods estimate integrals and expectations by averaging samples, with error shrinking like 1/√n regardless of dimension, which is why [ray tracing](../../14-human-and-visual-computing/02-computer-graphics/ray-tracing-and-global-illumination.md) and many [generative models](../../13-artificial-intelligence/04-advanced-paradigms/generative-models.md) rely on sampling rather than exact integration.

## Key concepts

| Term | Meaning |
|---|---|
| Random variable | Function from outcomes to numbers |
| PMF / PDF | Probability mass function (discrete) / probability density function (continuous) |
| CDF | F(x) = P(X ≤ x) |
| Expectation E[X] | Probability-weighted average value |
| Variance / standard deviation | Expected squared deviation from the mean / its square root |
| Indicator variable | Equals 1 if an event occurs, else 0; E[I] = P(event) |
| Chernoff bound | Exponentially small tail bound for sums of independent variables |
| Poisson / exponential | Count of rare events in a window / waiting time between them |
| Normal (Gaussian) | Bell-shaped limit of sums of many independent effects |
| Heavy tail | Tail decaying slower than exponential, e.g. power law |
| Percentile (p99) | Value below which 99% of observations fall |

## How it fits

- **Below:** Random variables are [functions](../02-sets-relations-functions/functions-and-cardinality.md) on a [probability space](probability.md); continuous ones need integrals from [calculus](../05-continuous-mathematics/calculus.md).
- **Above:** [Queueing and latency](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) models use Poisson arrivals and exponential service. [Randomized algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md) and [hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) use linearity of expectation and Chernoff bounds. [Observability](../../12-software-engineering/04-operations/observability.md) and [reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md) reason in percentiles because of heavy tails. [Generative models](../../13-artificial-intelligence/04-advanced-paradigms/generative-models.md) learn and sample distributions; [entropy](../../02-theory-of-computation/01-information-theory/entropy-and-information.md) is an expectation.
- **Siblings:** [Probability](probability.md) supplies events and conditioning; [statistical inference](statistical-inference.md) estimates a distribution's parameters from samples.

## Common misconceptions

- **"The average latency describes user experience."** With heavy tails, the mean can look fine while 1% of requests take seconds; tails dominate fan-out systems.
- **"Everything is normally distributed."** The CLT needs independence and finite variance; heavy-tailed data violates it and averages converge slowly or not at all.
- **"Linearity of expectation requires independence."** It never does; only the variance-addition rule does.

## Go deeper

- Joseph Blitzstein and Jessica Hwang, *Introduction to Probability* (2nd ed., 2019): distributions and their stories.
- Mor Harchol-Balter, *Performance Modeling and Design of Computer Systems: Queueing Theory in Action* (2013): distributions applied to systems performance.
- Jeffrey Dean and Luiz André Barroso, "The Tail at Scale" (Communications of the ACM, 2013): why percentiles dominate large services.
