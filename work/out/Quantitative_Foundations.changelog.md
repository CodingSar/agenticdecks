# Quantitative Foundations — changelog

**Inputs:** `quantitative_foundations` (99) + `statistics-bayes-ml-rl-geometric` (176) = 275 notes.
**Output:** 350 notes (326 basic, 24 cloze) in 11 concept subdecks: 01 Probability & Distributions, 02 Statistical Inference, 03 Regression & GLMs, 04 Causal Inference, 05 Bayesian Reasoning, 06 Machine Learning, 07 Deep Learning, 08 Reinforcement Learning, 09 Queueing & Performance, 10 Linear Algebra & Calculus, 11 Information Theory.

## Summary
- Deleted: 1. Fully merged: 3. Moved to LLMs & Agentic Engineering: 3 (they keep their guids there).
- Splits: 79 source notes split, giving 80 extra cards. Most source answers were ~730 characters; the mean answer is now ~22 words and the longest is 44.
- New cards: 2 contrast cards (confounder vs collider; bagging vs boosting).
- Analogies: 68 added (19%). The sources had none. About 20 are geometric intuitions moved from "Geometry:" into `analogy`, e.g. OLS as a shadow, the soap-bubble Gaussian, the frictionless HMC puck, origami ReLU, photocopy contraction. The rest are new, e.g. smoke alarm for Type I/II, Texas sharpshooter, ring-toss CI, fishing net for precision/recall.
- Geometric intuitions: kept. Each stats-sourced card keeps its original "Geometry:" text in `extra` unless it moved to `analogy`, went into a split sibling's answer, or was folded into the answer. All 17 SVG figures are kept (`attention_hull.svg` moved with the attention card to the LLM deck). MathJax is unchanged.
- Formatting: inline `<span class="ex">` examples were moved out of `back` into `extra` as `<b>Example:</b>`.

## Full merges
- S39 (F-test for nested models) → S12 (geometric F-statistic): same statement.
- S74 (Simpson's paradox, geometric) → A26 (Simpson's paradox): the staircase picture became the analogy.
- S34 (bias–variance formula) → A86 (bias–variance decomposition): the formula moved to `extra`.

## Overlaps between the two decks, resolved by giving each guid a different angle
- Bayes: A0 is the four-part cloze, S78 the geometric update, S80 precisions add.
- CLT: A9 statement, +A9 consequence/failure, S9 why the Gaussian.
- p-value: A18 definition, S49 three things it is not.
- Intervals: A21 confidence-interval meaning, S50 confidence vs credible.
- Power: A20 winner's curse, S56 determinants and n ∝ σ²/δ².
- Multiple testing: A22 the problem, S54 FWER vs FDR, +S54 Benjamini–Hochberg.
- Regression to the mean: A25 the fallacy, S37 why (slope r), +S37 ellipse tangents.
- Collider: A29 + the collider part of S75 → one card; S75 keeps confounder; mediator split out.
- Counterfactuals: A31 fundamental problem, S76 selection-bias decomposition, +S76 ignorability/overlap.
- Instrumental variables: the IV part of A32 merged into S41; A32 keeps diff-in-diff; regression discontinuity split out.
- PCA: A54 / S115. SVD: A55 / S116. L1 vs L2: A56 norms / S31 why lasso gives zeros.
- KL: A70 definition / S16 why not a distance. Cross-entropy: A69 definition / S17 relation to KL / S124 as a classification loss.
- Max entropy: A76 principle / S18 cloze. Convexity: A62 / S111.
- SGD: A81 why mini-batches / S109 noise ball. Gradient descent: A80 update / S107 condition number.
- Leakage: A85 (+ cloze of forms) / S129 nested CV.
- AUC: A93 / S125 imbalance. Calibration: A94 / S126 vs discrimination.
- Distribution shift: A95 / S130 shift types. Double descent: A97 / S105 why.
- Softmax temperature: A57 + S124 → +A57.
- Fan-out example moved from A16 to A46. Vanishing gradients taken off the chain-rule card (A60) and left to S134. The typical-set figure is used once (S13); S91 covers its Bayesian consequence.

## Deletions
- A47 "What is a vector in ML": too elementary; the dot-product, embedding and matrix cards carry the useful content.

## Moved to `LLMs_and_Agentic_Engineering` (ownership: transformers/LLMs)
- S141 scaled dot-product attention (+ attention_hull.svg), S149 scaling laws/Chinchilla, S173 RLHF/DPO.

## Other edits
- Long enumerations became clozes: Kendall notation, hat-matrix properties, GLM components, regularisation techniques, leakage forms, MCMC diagnostics, deadly triad, CNN biases, curse of dimensionality, likelihood-test trinity, max-entropy distributions.
- Prompts reworded to "why/when/what breaks" where possible, e.g. "Why do connection pools exhaust in cascades?", "How can you cut queueing delay without adding capacity?".

## Product-content review

Reviewed all cards for product-catered content (vendor feature lists, tool plugs, certification marketing, dated news, promotional phrasing): nothing applied, no changes made.
