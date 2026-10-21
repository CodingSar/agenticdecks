# Generative Models

> **Layer:** [13 Artificial Intelligence](../README.md) › [Advanced paradigms](README.md)
> **Builds on:** [Unsupervised learning](../02-machine-learning-foundations/unsupervised-learning.md), [Probabilistic reasoning](../01-classical-ai/probabilistic-reasoning.md), [Random variables and distributions](../../01-mathematical-foundations/06-probability-and-statistics/random-variables-and-distributions.md), [Convolutional networks](../03-deep-learning/convolutional-networks.md), [Attention and transformers](../03-deep-learning/attention-and-transformers.md)
> **Enables:** [Large language models](large-language-models.md), [Digital media and compression](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md), [Ray tracing and global illumination](../../14-human-and-visual-computing/02-computer-graphics/ray-tracing-and-global-illumination.md)

## Essence

A generative model learns the probability distribution p(x) that a dataset was drawn from, so that it can produce new samples that look like the data: images, audio, text, molecules. Directly writing down p(x) over, say, a million pixel values is hopeless, so every generative model family is a trick for representing a very high-dimensional distribution with a neural network in a form that can be both **trained** from samples and **sampled** from. The families differ in which of three properties they give up: exact likelihoods, fast sampling, or stable training. As of the mid-2020s, two families dominate: **autoregressive** models (the basis of language models) and **diffusion** models (the basis of most image, video and audio generators).

## Core tenets

1. **Generation is sampling from a learned distribution.** Training fits p_θ(x) to data, usually by maximising likelihood or a bound on it, equivalent to minimising the Kullback–Leibler (KL) divergence KL(p_data ‖ p_θ) between the data distribution and the model. Generation draws x ~ p_θ. Conditioning on an input c (a caption, a prompt, a class) gives p_θ(x | c), which is how text-to-image and text-to-speech work.

2. **Autoregressive models factorise by the chain rule.** Any joint distribution can be written exactly as p(x) = ∏_t p(x_t | x_<t). A network predicts each element from those before it, giving exact likelihoods and simple training (supervised prediction of the next element). Sampling is sequential: one network evaluation per element, which is slow for millions of pixels but natural for text.

3. **Latent-variable models generate through a hidden code.** Sample a simple latent z ~ N(0, I) and map it through a decoder to x. The Variational Autoencoder (VAE, 2013) trains the decoder jointly with an encoder q(z | x) by maximising the Evidence Lower Bound (ELBO): reconstruction quality minus the KL divergence of q(z | x) from the prior. VAEs train stably and give a useful latent space but tend to produce blurry samples.

4. **Adversarial training replaces likelihood with a learned critic.** A Generative Adversarial Network (GAN, 2014) pits a generator against a discriminator that tries to tell real from generated samples; the generator learns to fool it. GANs were the first models to generate high-resolution photorealistic faces (Progressive GAN, 2017; StyleGAN, 2019) and sample in one pass, but the two-player game is unstable and prone to mode collapse, where the generator covers only part of the data distribution.

5. **Diffusion models learn to reverse gradual noising.** A fixed forward process adds Gaussian noise to data over many steps until only noise remains. A network ε_θ(x_t, t) is trained to predict the noise added at each step, a simple regression loss:

   L = E_{x, t, ε} ‖ε − ε_θ(√ᾱ_t x + √(1 − ᾱ_t) ε, t)‖²

   Sampling starts from pure noise and repeatedly denoises. This decomposes one impossible jump (noise to image) into many small, learnable steps. Training is stable, coverage of the data distribution is good, and quality is high; the cost is tens to hundreds of network evaluations per sample, reduced by better samplers and distillation.

6. **Work in a compressed space when the data is huge.** Latent diffusion (Stable Diffusion, 2022) first trains an autoencoder that compresses images about 8× per side, then runs diffusion in that latent space, cutting compute by more than an order of magnitude. Image and video tokenisers likewise let autoregressive transformers generate media as sequences of discrete codes.

7. **Guidance trades diversity for fidelity.** Classifier-free guidance runs the denoiser with and without the condition and extrapolates toward the conditioned prediction. Higher guidance makes outputs match the prompt more closely and look sharper, but less varied. Temperature plays the same role in autoregressive sampling.

8. **Fluent output is not truthful output.** A generative model is rewarded for samples that are probable under the training distribution, not for factual accuracy. Generated images, voices and text can be indistinguishable from real ones, which raises provenance, misinformation and consent problems that watermarking and content-credential standards address only partially.

## Key concepts

| Term | Meaning |
|---|---|
| Density p(x) | Probability the model assigns to a data point |
| Likelihood training | Fitting parameters to maximise the probability of the observed data |
| KL divergence | Asymmetric measure of how one distribution differs from another |
| Latent variable | Unobserved variable z from which data is generated |
| ELBO | Tractable lower bound on log-likelihood used to train VAEs |
| Mode collapse | Generator producing only a few kinds of output |
| Forward / reverse diffusion | Adding noise step by step / learned removal of it |
| Classifier-free guidance | Steering samples toward a condition by contrasting conditioned and unconditioned predictions |
| Temperature | Scaling of logits before sampling; lower is more deterministic |

## How it fits

- **Below:** Generative models are [density estimation](../02-machine-learning-foundations/unsupervised-learning.md) from unsupervised learning, built from [probability distributions](../../01-mathematical-foundations/06-probability-and-statistics/random-variables-and-distributions.md) and latent-variable ideas in [probabilistic reasoning](../01-classical-ai/probabilistic-reasoning.md). Their networks are [convolutional networks](../03-deep-learning/convolutional-networks.md) and [transformers](../03-deep-learning/attention-and-transformers.md); their likelihood is a code length in the sense of [information theory](../../02-theory-of-computation/01-information-theory/entropy-and-information.md).
- **Above:** [Large language models](large-language-models.md) are autoregressive generative models of text. Generative models feed learned codecs in [media compression](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md), denoising and neural rendering in [graphics](../../14-human-and-visual-computing/02-computer-graphics/ray-tracing-and-global-illumination.md), and synthetic data for [vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md). Their misuse is a topic for [law and policy](../../15-computing-in-context/law-privacy-and-policy.md).
- **Siblings:** [Reinforcement learning](reinforcement-learning.md) fine-tunes generative models toward preferences; [alignment](alignment-and-safety.md) studies how to make their outputs safe.

## Common misconceptions

- **"Generative models copy and paste training data."** They learn a distribution and usually produce novel combinations, but they can and sometimes do memorise and reproduce rare or duplicated training items.
- **"Diffusion is only for images."** Diffusion and related flow-matching methods are used for audio, video, molecules and robot actions.
- **"Higher likelihood means better-looking samples."** Likelihood and perceptual quality can diverge; a model can spend most of its likelihood on imperceptible detail.

## Go deeper

- Diederik Kingma and Max Welling, "Auto-Encoding Variational Bayes" (2013): the VAE.
- Ian Goodfellow et al., "Generative Adversarial Nets" (2014): the GAN.
- Jonathan Ho, Ajay Jain and Pieter Abbeel, "Denoising Diffusion Probabilistic Models" (2020): the simple noise-prediction loss that made diffusion practical.
- Robin Rombach et al., "High-Resolution Image Synthesis with Latent Diffusion Models" (2022): diffusion in a learned latent space.
