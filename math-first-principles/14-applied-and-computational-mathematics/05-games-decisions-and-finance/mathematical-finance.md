# Mathematical Finance

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Games, Decisions and Finance](README.md)
> **Builds on:** [Martingales](../../11-probability-and-statistics/03-stochastic-processes/martingales.md), [Stochastic Calculus](../../11-probability-and-statistics/03-stochastic-processes/stochastic-calculus.md), [The Radon–Nikodym Theorem](../../09-advanced-analysis/01-measure-and-integration/the-radon-nikodym-theorem.md), [The Heat Equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md), [Convex Sets and Separation](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md)
> **Enables:** [Monte Carlo Methods](../01-numerical-analysis/monte-carlo-methods.md), [Mathematics and Society](../../15-mathematics-in-context/mathematics-and-society.md)

## Essence

Mathematical finance prices contracts whose payoff depends on an uncertain future, such as an option to buy a share at a fixed price later. Its founding principle is no arbitrage: in a sensible market no trading strategy turns nothing into a riskless profit. That one assumption fixes prices without knowing anyone's beliefs about the future. The fundamental theorem of asset pricing (FTAP) makes it precise: a market has no arbitrage if and only if there is a "risk-neutral" probability measure under which discounted prices are martingales, and then every price is a discounted expectation under that measure. The Black–Scholes model (1973) is the famous special case, in which the option can be replicated exactly by trading the share, and its price solves a version of the heat equation.

## Core tenets

1. **No arbitrage alone prices a derivative in a one-period model.** A share worth S now will be worth uS or dS, and cash grows by 1 + r. If 1 + r ≥ u, borrowing the share, selling it and banking the proceeds never loses and sometimes gains; similarly if 1 + r ≤ d. So no arbitrage requires d < 1 + r < u. A claim paying f_u or f_d can then be replicated by holding Δ = (f_u − f_d)/((u − d)S) shares plus cash, so its price must be the cost of that portfolio:

   ```
   price = [ q·f_u + (1 − q)·f_d ] / (1 + r),       q = (1 + r − d)/(u − d)
   ```

   The real probability p of an up-move never appears. The number q lies in (0, 1) and acts as a probability under which the share earns the riskless rate. Iterated, this is the Cox–Ross–Rubinstein tree (1979).

2. **The fundamental theorem: no arbitrage if and only if an equivalent martingale measure exists.** An equivalent measure Q has the same null sets as the real measure P; it is a martingale measure if discounted prices are Q-martingales. If such Q exists, every self-financing strategy's discounted value is a Q-martingale, so a strategy starting at 0 has Q-mean 0 at the end and cannot be nonnegative and sometimes positive. The converse is a separation argument: the gains achievable from zero cost form a subspace that meets the cone of nonnegative payoffs only at 0, and a separating hyperplane is a strictly positive linear functional, that is, a density dQ/dP. Harrison and Pliska (1981) proved this for finite probability spaces, Dalang, Morton and Willinger (1990) for general discrete time.

3. **In continuous time the theorem needs a sharper notion of free lunch.** With continuous trading, approximate arbitrages can exist without exact ones, so the right hypothesis is "no free lunch with vanishing risk". Freddy Delbaen and Walter Schachermayer (1994) proved it equivalent to the existence of an equivalent martingale measure, in the generality of semimartingale prices. A second theorem says the market is complete, every claim replicable, if and only if the martingale measure is unique.

4. **Black–Scholes: hedging removes the drift.** Model the share by geometric Brownian motion, dS = μS·dt + σS·dW. For an option value V(t, S), Itô's formula shows that the portfolio V − (∂V/∂S)·S has no dW term, so it is riskless and must earn the rate r:

   ```
   ∂V/∂t + ½σ²S² ∂²V/∂S² + rS ∂V/∂S − rV = 0
   call:  C = S·N(d₁) − K·e^(−rT)·N(d₂),   d₁ = [ln(S/K) + (r + σ²/2)T] / (σ√T),   d₂ = d₁ − σ√T
   ```

   Here K is the strike, T the time to expiry and N the standard normal distribution function. The expected return μ has vanished, as p did in the tree. Fischer Black and Myron Scholes, with Robert Merton, published this in 1973.

5. **The equation is the heat equation, and the price is an expectation.** Substituting x = ln S, running time backwards and removing exponential factors turns the Black–Scholes equation into the heat equation, which explains the normal distribution in the formula. Girsanov's theorem gives the same answer probabilistically: changing measure by a Radon–Nikodym density turns W into a Q-Brownian motion with a shifted drift under which S grows at rate r, and V equals e^(−rT) times the Q-expectation of the payoff.

6. **The assumptions are strong, and markets violate them.** The model assumes constant volatility, continuous price paths, frictionless continuous trading and unlimited borrowing at one rate. Real returns have jumps and heavy tails; since the crash of October 1987, implied volatility varies with the strike (the "smile"); transaction costs make continuous hedging infinitely expensive. When the hedging argument fails, the market is incomplete, many martingale measures fit, and no-arbitrage gives only an interval of prices. The hedge fund Long-Term Capital Management collapsed in 1998, a year after Merton and Scholes received the Nobel prize in economics.

## Key concepts

| Term | Meaning |
|---|---|
| Arbitrage | A strategy of zero cost whose final value is never negative and is positive with positive probability |
| Derivative | A contract whose payoff is a function of other prices, such as a call option paying max(S_T − K, 0) |
| Replication | A trading strategy whose final value equals a claim's payoff in every state |
| Equivalent martingale measure | A measure with the same null sets as P under which discounted prices are martingales |
| Complete market | Every claim can be replicated |
| Geometric Brownian motion | S with dS = μS·dt + σS·dW; log-returns are normal |
| Volatility σ | The standard deviation of log-returns per unit time |
| Implied volatility | The σ that makes the Black–Scholes formula match a market price |

## How it fits

- **Below:** martingales and Itô calculus from layer 11, Radon–Nikodym densities for change of measure, the heat equation, and separation of convex sets for the fundamental theorem.
- **Above:** [mathematics and society](../../15-mathematics-in-context/mathematics-and-society.md) asks how models shaped financial crises; [Monte Carlo methods](../01-numerical-analysis/monte-carlo-methods.md) compute prices when no formula exists.
- **Siblings:** [game theory](game-theory.md) shares the convex duality behind minimax; [social choice](social-choice-and-voting.md) aggregates by votes, markets by prices.

## Common misconceptions

- **"The option price is the expected payoff under real probabilities."** It is a discounted expectation under the risk-neutral measure, which can differ greatly from the real one.
- **"Black–Scholes predicts share prices."** It prices an option relative to the share, assuming the hedge works; it says nothing about where the share will go.
- **"Risk-neutral means investors do not care about risk."** Risk preferences are already in the share price; Q is a device implied by no arbitrage.

## Go deeper

- S. E. Shreve, *Stochastic Calculus for Finance I and II* (2004): the standard path from binomial trees to continuous time.
- F. Delbaen and W. Schachermayer, *The Mathematics of Arbitrage* (2006): the fundamental theorem in full generality.
- F. Black and M. Scholes, "The Pricing of Options and Corporate Liabilities" (1973): the original paper.
