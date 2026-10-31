# Games, Decisions and Finance

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › Games, Decisions and Finance
> **Children:** [Game Theory](game-theory.md) · [Social Choice and Voting](social-choice-and-voting.md) · [Mathematical Finance](mathematical-finance.md)

## What this area is about

Most of applied mathematics models systems that do not care about the outcome. This area models agents who do: players choosing strategies, voters ranking candidates, traders pricing risk. Each agent pursues its own goal, and the question is what follows when many of them interact. Can every player guarantee something? Is there a stable outcome? Can individual preferences be combined into a fair collective choice? What must a price be if no one can make money from nothing?

The answers rest on three kinds of mathematics. Fixed-point and separation theorems prove that equilibria and prices exist without constructing them. Impossibility theorems prove that some reasonable wishes cannot all be met at once. Probability, in the form of martingales, turns the absence of free money into a pricing rule. One idea links games and finance: a convex separation argument, which gives the minimax theorem in games and the fundamental theorem of asset pricing in finance.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Game theory](game-theory.md) | Strategic interaction: minimax for zero-sum games, Nash equilibrium in general, the prisoner's dilemma | Nothing in this area |
| [Social choice and voting](social-choice-and-voting.md) | Aggregating preferences: Condorcet cycles, Arrow's theorem, manipulation, May's theorem | Game theory, for strategic voting |
| [Mathematical finance](mathematical-finance.md) | Pricing by no arbitrage: martingale measures, Black–Scholes, the fundamental theorem | Nothing in this area |

Game theory comes first. It sets the language of agents, strategies and payoffs, and the existence of equilibria by fixed points. Social choice takes the opposite stance: instead of predicting what agents do, it asks what rule a society should use, and finds that the axioms people want are inconsistent. The two meet in the Gibbard–Satterthwaite theorem, which says that every reasonable voting rule invites strategic play. Mathematical finance is a game against a market rather than against a person. Its central principle, that no strategy yields a riskless profit, is the financial analogue of an equilibrium condition, and duality turns it into a probability measure.

```
         fixed points             separation of convex sets
              |                     /                 \
   Nash equilibrium        minimax theorem      no arbitrage ⇔ martingale measure
              \                  /                         |
              game theory                        mathematical finance
                   |
        strategic voting (Gibbard–Satterthwaite)
                   |
        social choice: Arrow, May
```

## Connections to sibling areas

- **[Numerical analysis](../01-numerical-analysis/README.md):** option prices are computed by finite differences for the Black–Scholes equation and by Monte Carlo simulation of risk-neutral paths.
- **[Optimisation](../02-optimisation/README.md):** a finite zero-sum game is a linear programme, and the minimax theorem is linear programming duality.
- **[Information, codes and cryptography](../03-information-codes-and-cryptography/README.md):** cryptographic protocols are games against adversaries, and their security definitions are stated as such.
- **[Mathematical modelling](../04-mathematical-modelling/README.md):** evolutionary game theory is population dynamics with strategies as species, and portfolio choice is stochastic control.
- **[Data and learning](../06-data-and-learning/README.md):** training a generative adversarial network is a two-player game, and online learning algorithms converge to equilibria of repeated games.

## Connections across layers

From below, the area uses [fixed-point theorems](../../07-topology/02-algebraic-topology/fixed-point-theorems.md) from topology, [convex sets and separation](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md) from geometry, [relations and orders](../../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md) for preferences, and the [stochastic processes](../../11-probability-and-statistics/03-stochastic-processes/README.md) of layer 11 (martingales, Brownian motion, Itô calculus). Upward, [mathematics and society](../../15-mathematics-in-context/mathematics-and-society.md) examines voting reform, financial crises and the use of models in public life. The computing tree's [reinforcement learning](../../../cs-first-principles/13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md) leaf treats agents that learn their strategies.

## Cross-cutting threads

- [Duality](../../CROSS-CUTTING.md#duality): minimax is linear programming duality, and arbitrage-free prices are dual to hedging strategies.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): Nash's theorem proves equilibria exist, while finding one is computationally hard.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): Arrow and Gibbard–Satterthwaite rule out ideal voting rules.
- [Extremal principles and optimisation](../../CROSS-CUTTING.md#extremal-principles-and-optimisation): every player optimises against the others.
- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): mixed strategies and risk-neutral expectations are both averages chosen to remove an advantage.
