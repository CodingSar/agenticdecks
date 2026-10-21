# Reinforcement Learning

> **Layer:** [13 Artificial Intelligence](../README.md) › [Advanced paradigms](README.md)
> **Builds on:** [Dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md), [Probabilistic reasoning](../01-classical-ai/probabilistic-reasoning.md), [Search and planning](../01-classical-ai/search-and-planning.md), [Neural networks and backpropagation](../03-deep-learning/neural-networks-and-backpropagation.md), [Feedback and control](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md)
> **Enables:** [Large language models](large-language-models.md), [Alignment and safety](alignment-and-safety.md)

## Essence

Reinforcement Learning (RL) is learning to act from trial and error. An agent observes a state, takes an action, receives a numerical reward and a new state, and must learn a policy that maximises total reward over time. There are no labelled correct actions, only delayed, noisy feedback, so the agent must solve two problems supervised learning does not have: **credit assignment** (which earlier action earned this reward?) and **exploration** (should I try something new or exploit what I know?). The mathematical core is the Markov Decision Process (MDP) and the Bellman equation, which expresses the value of a state recursively in terms of the values of its successors. Combining that recursion with neural networks produced superhuman game players and, as of the mid-2020s, is a key stage in training large language models.

## Core tenets

1. **The problem is a Markov Decision Process.** An MDP has states S, actions A, transition probabilities P(s' | s, a), rewards R(s, a) and a discount γ ∈ [0, 1). The Markov property says the next state depends only on the current state and action, not on history. The agent seeks a policy π(a | s) maximising expected discounted return G_t = Σ_k γ^k r_{t+k+1}. Discounting keeps infinite sums finite and expresses preference for sooner rewards.

2. **The Bellman equation makes value recursive.** The optimal action value satisfies

   Q*(s, a) = E[ r + γ max_{a'} Q*(s', a') | s, a ]

   The value of acting now equals the immediate reward plus the discounted value of acting optimally afterwards. This is dynamic programming over time: a long-horizon problem is reduced to one-step look-ahead plus a stored value table. Once Q* is known, the optimal policy is simply argmax_a Q*(s, a).

3. **With a known model, planning solves the Bellman equation directly.** Value iteration repeatedly applies the Bellman update to every state until values converge; the update is a contraction by factor γ, so convergence is guaranteed. This is planning, not learning, and it needs the transition model and a state space small enough to enumerate.

4. **Without a model, learn from sampled experience.** Temporal-Difference (TD) learning updates estimates toward a bootstrapped target. Q-learning (Watkins, 1989) uses

   Q(s, a) ← Q(s, a) + α [ r + γ max_{a'} Q(s', a') − Q(s, a) ]

   after each transition. It converges to Q* in the tabular case if every state-action pair is visited infinitely often. The bracket, the TD error, is the "surprise" signal, and it closely resembles dopamine responses measured in animal brains.

5. **Policy gradients optimise the policy directly.** Instead of learning values and acting greedily, parameterise π_θ and climb the gradient of expected return: ∇J(θ) = E[ ∇ log π_θ(a | s) · A(s, a) ], where the advantage A says how much better the action was than average. This handles continuous actions and stochastic policies naturally. Proximal Policy Optimization (PPO, 2017) limits each update's size for stability and became a widely used default, including for language-model fine-tuning.

6. **Exploration versus exploitation has no free answer.** An agent that always takes its current best action may never discover a better one; one that explores too much wastes reward. Strategies range from ε-greedy (random action with probability ε) to optimism under uncertainty (bonus for rarely tried actions, as in the Upper Confidence Bound (UCB) rule used in Monte Carlo Tree Search). Sparse rewards make exploration the dominant difficulty.

7. **Deep RL is powerful but unstable and sample-hungry.** Using neural networks as function approximators lets RL handle huge state spaces, such as raw pixels (Deep Q-Network (DQN) on Atari games, 2015) and Go (AlphaGo, 2016; AlphaZero, 2017). But combining function approximation, bootstrapping and off-policy data can diverge, and agents often need millions to billions of interactions. That is why RL succeeds most where simulation is cheap (games, robotics in simulation) or where a strong pre-trained model supplies a good starting policy.

8. **The reward is the specification, and agents exploit its flaws.** An agent optimises exactly the reward it is given, not the intent behind it. Documented examples include a boat-racing agent circling to collect points instead of finishing the race. This "reward hacking" is a central concern of [alignment](alignment-and-safety.md).

## Key concepts

| Term | Meaning |
|---|---|
| Policy π | Mapping from states to (distributions over) actions |
| Return | Discounted sum of future rewards |
| Value function V(s) | Expected return from state s under a policy |
| Action value Q(s, a) | Expected return from taking a in s, then following the policy |
| Discount γ | Weight on future rewards; sets the effective horizon of about 1/(1 − γ) steps |
| Bootstrapping | Updating an estimate using other estimates rather than complete returns |
| TD error | r + γV(s') − V(s): the difference between predicted and observed one-step outcome |
| On-policy / off-policy | Learning from the current policy's own data / from data generated by another policy |
| Model-based RL | Learning a model of transitions and planning with it |

## How it fits

- **Below:** The Bellman equation is [dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md); MDPs extend the decision theory of [probabilistic reasoning](../01-classical-ai/probabilistic-reasoning.md); RL is a learned form of [feedback control](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md); value and policy networks are trained by [backpropagation](../03-deep-learning/neural-networks-and-backpropagation.md).
- **Above:** Reinforcement Learning from Human Feedback (RLHF) and RL on verifiable rewards (for example passing unit tests or checking maths answers) shape the behaviour of [large language models](large-language-models.md); RL is applied to robotics, chip floor-planning, data-centre cooling and recommendation systems.
- **Siblings:** [Generative models](generative-models.md) learn a distribution from data; RL learns behaviour from reward. [Alignment](alignment-and-safety.md) studies what happens when the reward is an imperfect proxy.

## Common misconceptions

- **"RL is how all AI learns."** Most deployed machine learning is supervised or self-supervised. RL is used where labelled actions do not exist and feedback is evaluative.
- **"The agent learns what the designer wants."** It learns what the reward rewards. Misspecified rewards produce competent but unintended behaviour.
- **"AlphaGo learned Go purely by RL."** The original AlphaGo bootstrapped from human games by supervised learning and relied on tree search at play time; AlphaZero removed human data but kept search.

## Go deeper

- Richard Sutton and Andrew Barto, *Reinforcement Learning: An Introduction* (2nd ed., 2018): the standard text, freely available.
- Volodymyr Mnih et al., "Human-Level Control through Deep Reinforcement Learning" (2015): DQN on Atari.
- David Silver et al., "Mastering the Game of Go without Human Knowledge" (2017): AlphaGo Zero, search plus self-play.
- John Schulman et al., "Proximal Policy Optimization Algorithms" (2017): the policy-gradient workhorse.
