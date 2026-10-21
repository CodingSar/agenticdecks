# Supervised Learning

> **Layer:** [13 Artificial Intelligence](../README.md) › [Machine learning foundations](README.md)
> **Builds on:** [Learning as optimization](learning-as-optimization.md), [Generalization and bias-variance](generalization-and-bias-variance.md), [Linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md), [Search trees](../../05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md)
> **Enables:** [Neural networks and backpropagation](../03-deep-learning/neural-networks-and-backpropagation.md), [Computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md), [Evaluation and experimentation](evaluation-and-experimentation.md)

## Essence

Supervised learning learns a function from input to output using examples where the right answer is given: emails labelled spam or not, images labelled with objects, houses with sale prices. If the output is a category it is **classification**; if it is a number it is **regression**. The learner picks a function from a model family that minimises loss on the labelled data and should then predict well on new inputs. The families differ in their inductive bias: linear models assume the answer is a weighted sum of features, trees assume axis-aligned rules, nearest neighbours assume similar inputs have similar outputs, and neural networks learn their own features. Before deep learning, success depended mostly on hand-engineered features; the shift to learned features is the story of [deep learning](../03-deep-learning/README.md).

## Core tenets

1. **Labels define the task, and labels are expensive.** The model learns whatever the labels encode, including their errors and biases. Collecting labels is often the main cost of a supervised system, which is why self-supervised methods that manufacture labels from raw data (predict the next word, the masked patch) drive modern large models.

2. **Linear models are the baseline and the building block.** Linear regression predicts ŷ = wᵀx + b and has a closed-form least-squares solution. Logistic regression passes wᵀx + b through a sigmoid to get a probability and is trained with cross-entropy. Both are convex, fast and interpretable, and the final layer of almost every neural network is one of them applied to learned features.

3. **Feature maps and kernels make linear methods non-linear.** Mapping inputs through φ(x) (for example adding x² terms) lets a linear model draw curved boundaries. Kernel methods compute inner products φ(x)ᵀφ(x') = k(x, x') without forming φ, so Support Vector Machines (SVMs) can work in very high or infinite-dimensional feature spaces. SVMs maximise the margin between classes, which improves generalisation. Their training cost grows at least quadratically with the number of examples, limiting them to moderate datasets.

4. **Decision trees learn rules by recursive splitting.** At each node a tree picks the feature and threshold that best separate the labels (largest drop in impurity), then recurses. Single trees are interpretable but high-variance: small data changes produce different trees.

5. **Ensembles average away variance or iteratively remove bias.** Random forests train many trees on bootstrap samples with random feature subsets and average them, cutting variance. Gradient boosting fits each new tree to the residual errors of the ensemble so far, reducing bias step by step. As of the mid-2020s, gradient-boosted trees remain the strongest default for tabular data, often matching or beating neural networks there.

6. **Nearest neighbours store the data instead of fitting parameters.** k-Nearest Neighbours (k-NN) predicts from the k closest training examples. It needs no training but slow queries, and it suffers the curse of dimensionality: in high dimensions all points become nearly equidistant, so "nearest" carries little signal unless the representation is good. Modern vector search over learned embeddings revives the idea with good representations.

7. **Classifiers output scores, and decisions need thresholds.** Most classifiers produce a probability or score; turning it into a decision means choosing a threshold that trades false positives against false negatives. A well-calibrated model's 0.8 means right 80% of the time; many high-accuracy models are poorly calibrated and need recalibration.

## Key concepts

| Term | Meaning |
|---|---|
| Classification / regression | Predicting a category / a real number |
| Feature | A measurable input variable the model uses |
| Decision boundary | The surface in input space where the predicted class changes |
| Logistic regression | Linear model with a sigmoid output trained by cross-entropy |
| Kernel | Function computing an inner product in an implicit feature space |
| Margin | Distance from the decision boundary to the nearest training example |
| Random forest | Average of many decorrelated decision trees |
| Gradient boosting | Sequential ensemble where each tree fits the previous ensemble's errors |
| Calibration | Agreement between predicted probabilities and observed frequencies |

## How it fits

- **Below:** Linear models are [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md); training is [optimisation](learning-as-optimization.md); trees reuse the recursive partitioning of [search trees](../../05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md); nearest-neighbour search uses spatial structures from [computational geometry](../../05-algorithms-and-data-structures/07-advanced-topics/computational-geometry.md).
- **Above:** A neural network is a supervised learner whose features are learned too; [computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md), speech recognition and the fine-tuning stage of [large language models](../04-advanced-paradigms/large-language-models.md) are supervised.
- **Siblings:** [Unsupervised learning](unsupervised-learning.md) works without labels; [generalisation](generalization-and-bias-variance.md) explains model choice; [evaluation](evaluation-and-experimentation.md) explains how to compare them fairly.

## Common misconceptions

- **"Deep learning beats everything."** On small or tabular datasets, linear models and gradient-boosted trees are frequently better, cheaper and easier to explain.
- **"The model learns the concept we meant."** It learns whatever correlates with the labels. A pneumonia classifier can learn which hospital's scanner made the X-ray.
- **"High accuracy means a good model."** With 99% negatives, predicting "negative" always is 99% accurate and useless.

## Go deeper

- Christopher Bishop, *Pattern Recognition and Machine Learning* (2006): probabilistic treatment of linear models, kernels and classifiers.
- Trevor Hastie, Robert Tibshirani and Jerome Friedman, *The Elements of Statistical Learning* (2nd ed., 2009): trees, boosting and ensembles from the statisticians who shaped them.
- Leo Breiman, "Random Forests" (2001): the original paper, short and readable.
