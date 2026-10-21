# Convolutional Networks

> **Layer:** [13 Artificial Intelligence](../README.md) › [Deep learning](README.md)
> **Builds on:** [Neural networks and backpropagation](neural-networks-and-backpropagation.md), [Sampling and quantization](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md), [Linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md)
> **Enables:** [Computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md), [Generative models](../04-advanced-paradigms/generative-models.md), [Domain-specific accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md)

## Essence

A Convolutional Neural Network (CNN) is a neural network built for data on a grid, such as images, audio spectrograms or video. Instead of connecting every input pixel to every unit, each layer slides a small learned filter (say 3×3) across the input and computes the same weighted sum at every position. This encodes two facts about natural signals: useful patterns are **local** (an edge depends on nearby pixels) and **position-independent** (an edge is an edge anywhere in the image). Weight sharing cuts parameters by orders of magnitude and makes the network respond to a pattern wherever it appears. Stacking convolutions with downsampling grows each unit's view of the input, so deep layers detect large, abstract structures built from small, simple ones.

## Core tenets

1. **Convolution is a linear layer with locality and weight sharing.** Output position (i, j) is Σ_{u,v} K[u, v] · X[i+u, j+v] over a small kernel K. (Deep-learning libraries compute cross-correlation and call it convolution; the difference is a kernel flip that learning absorbs.) A fully connected layer from a 224×224×3 image to a same-sized output would need about 2.3 × 10^10 weights; a 3×3 convolution with 64 input and 64 output channels needs 36,864, regardless of image size.

2. **Weight sharing gives translation equivariance.** Shifting the input shifts the output feature map by the same amount, because the same filter is applied everywhere. Pooling or global averaging then gives approximate translation *invariance* for classification. This is an inductive bias that matches images and saves the network from learning the same detector separately at every position.

3. **Depth grows the receptive field and builds a feature hierarchy.** Each 3×3 layer enlarges the region of input a unit sees by two pixels; strided convolution or pooling halves resolution and doubles the growth rate. Visualisations of trained CNNs show early layers learning edge and colour detectors (similar to those found in the mammalian visual cortex), middle layers textures and parts, and late layers object-level features.

4. **Channels are learned feature types.** Each layer maps C_in feature maps to C_out by applying C_out filters, each spanning all input channels. A 1×1 convolution mixes channels without spatial extent, a cheap way to change width. Typical designs halve resolution while doubling channels, keeping compute per layer roughly balanced.

5. **CNNs triggered the deep learning revolution.** LeNet (LeCun et al., 1989–1998) read handwritten digits for bank cheques. AlexNet (2012) cut the ImageNet top-5 error from about 26% to about 15% using Graphics Processing Units (GPUs), Rectified Linear Units (ReLU) and dropout. VGG, GoogLeNet and ResNet followed within three years, and by 2015 ResNet surpassed the commonly cited human-level estimate on that benchmark.

6. **Convolution maps efficiently onto hardware.** Convolutions are reorganised into matrix multiplications (im2col) or computed with fast algorithms (Winograd, Fast Fourier Transform (FFT)). High data reuse (each weight is used at every position) gives high arithmetic intensity, ideal for GPUs and systolic-array accelerators.

7. **Built-in bias helps with little data and hurts with a lot.** Vision Transformers (2020), which split images into patches and use attention with no convolutional prior, underperform CNNs on modest datasets but match or exceed them when pre-trained on hundreds of millions of images. As of the mid-2020s both are in wide use, often in hybrid designs, and convolutional U-Nets remain common inside diffusion image generators.

## Key concepts

| Term | Meaning |
|---|---|
| Kernel / filter | Small learned weight array slid across the input |
| Feature map | Output of one filter over all positions; one channel of a layer's output |
| Stride | Step between filter positions; stride 2 halves resolution |
| Padding | Extra border values so filters can be applied at edges |
| Receptive field | Region of the original input that influences one unit |
| Pooling | Downsampling by taking the max or average over a window |
| Equivariance | Transforming the input transforms the output the same way |
| Invariance | Transforming the input leaves the output unchanged |
| U-Net | Encoder-decoder CNN with skip connections, used for dense per-pixel output |

## How it fits

- **Below:** Images are [sampled and quantised](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md) signals; convolution is the linear-filtering operation of signal processing with learned instead of designed filters; training is [backpropagation](neural-networks-and-backpropagation.md); speed comes from [GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md).
- **Above:** CNNs are the workhorse of [computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md) (classification, detection, segmentation), appear in learned image and video codecs in [media compression](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md), and form the denoisers in many [generative models](../04-advanced-paradigms/generative-models.md).
- **Siblings:** [Recurrent networks](recurrent-networks-and-sequence-models.md) share weights across time as CNNs share them across space. [Attention](attention-and-transformers.md) replaces fixed local connectivity with content-dependent global connectivity; convolution is the stronger prior, attention the more flexible one. Both scale with the techniques in [training at scale](training-at-scale.md).

## Common misconceptions

- **"CNNs are fully translation invariant."** Convolution is equivariant; strides and pooling break even that slightly, and CNNs are not inherently invariant to rotation or scale, which must come from data augmentation.
- **"CNNs see shapes like people do."** Trained ImageNet CNNs rely heavily on texture; a cat-shaped object with elephant texture is often classified as an elephant (Geirhos et al., 2019).
- **"Transformers made CNNs obsolete."** They displaced CNNs at the largest scales but CNNs remain efficient and competitive, especially on edge devices and with limited data.

## Go deeper

- Yann LeCun, Léon Bottou, Yoshua Bengio and Patrick Haffner, "Gradient-Based Learning Applied to Document Recognition" (1998): the LeNet paper and the case for convolution.
- Alex Krizhevsky, Ilya Sutskever and Geoffrey Hinton, "ImageNet Classification with Deep Convolutional Neural Networks" (2012): AlexNet, the turning point.
- Ian Goodfellow, Yoshua Bengio and Aaron Courville, *Deep Learning* (2016), chapter 9: convolution as an inductive bias.
