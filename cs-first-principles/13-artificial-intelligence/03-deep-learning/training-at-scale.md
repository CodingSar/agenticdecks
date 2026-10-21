# Training at Scale

> **Layer:** [13 Artificial Intelligence](../README.md) › [Deep learning](README.md)
> **Builds on:** [Data and task parallelism](../../10-distributed-and-parallel-computing/01-parallel-computing/data-and-task-parallelism.md), [SIMD and GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md), [Domain-specific accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md), [Floating point](../../03-digital-logic/01-number-representation/floating-point.md), [Learning as optimization](../02-machine-learning-foundations/learning-as-optimization.md)
> **Enables:** [Large language models](../04-advanced-paradigms/large-language-models.md), [Generative models](../04-advanced-paradigms/generative-models.md), [Cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md)

## Essence

The largest neural networks as of the mid-2020s have hundreds of billions to trillions of parameters and are trained on tens of trillions of tokens, needing on the order of 10^24 to 10^26 floating-point operations. No single chip holds such a model or finishes such a computation in a lifetime, so training is spread across thousands to tens of thousands of accelerators for weeks or months. Training at scale is the systems discipline of splitting one gradient-descent loop across that many devices while keeping them busy, keeping the numbers stable in low precision, and surviving hardware failures. Its scientific counterpart is **scaling laws**: smooth, empirical power laws relating loss to compute, data and parameters, which let practitioners predict a large run's outcome from small ones.

## Core tenets

1. **Loss falls predictably as a power law in scale.** Kaplan et al. (2020) and Hoffmann et al. (2022, "Chinchilla") found test loss roughly follows L(N, D) ≈ E + A/N^α + B/D^β for N parameters and D training tokens, over many orders of magnitude. Training compute is about C ≈ 6ND floating-point operations (2 for the forward pass, 4 for the backward pass, per parameter per token). Chinchilla's compute-optimal recipe is roughly 20 tokens per parameter; models meant for cheap inference are often trained on many more.

2. **Data parallelism replicates the model and splits the batch.** Each of k devices computes gradients on its shard of the mini-batch, then all devices average gradients with an all-reduce collective and take identical steps. It is mathematically the same as training with a k-times larger batch. Communication per step is proportional to model size, so fast interconnects matter, and very large batches eventually stop helping (the "critical batch size").

3. **Models too big for one device must be split.** Tensor parallelism splits each weight matrix across devices so they jointly compute one layer; it needs very high bandwidth and stays within a tightly connected group. Pipeline parallelism places different layers on different devices and streams micro-batches through them, with idle "bubbles" at the start and end. Sharded data parallelism (the Zero Redundancy Optimizer (ZeRO), Fully Sharded Data Parallel (FSDP)) partitions optimiser states, gradients and parameters across data-parallel workers and gathers them on demand. Production runs combine all of these ("3D parallelism").

4. **Low precision doubles throughput if you guard the numerics.** Training uses 16-bit formats (bfloat16, which keeps float32's 8-bit exponent range) and increasingly 8-bit floating point (FP8) for matrix multiplications, while keeping a float32 master copy of weights and accumulating sums in higher precision. Halving the bits roughly doubles arithmetic throughput and halves memory traffic. Loss scaling and careful normalisation prevent underflow and overflow.

5. **Memory, not compute, sets the shape of the job.** With Adam in mixed precision, each parameter needs about 16 bytes (weights, gradients, two optimiser moments, master copy) before activations: a 70-billion-parameter model needs over 1 TB just for that state, versus 80–192 GB of High Bandwidth Memory (HBM) per accelerator (circa 2024–2025). Sharding, activation checkpointing and offloading exist to fit within this budget.

6. **At scale, failure is routine and stability is fragile.** With 10,000+ devices, some hardware fails every few hours, so jobs checkpoint frequently and restart automatically. Training can also diverge as loss spikes; practitioners use learning-rate warm-up and decay, gradient clipping and normalisation choices, and roll back to an earlier checkpoint when it happens.

7. **The goal is high utilisation of very expensive hardware.** Model FLOPs Utilisation (MFU), where FLOPs means floating-point operations,, the fraction of peak floating-point throughput spent on useful model arithmetic, is typically 30–60% in well-tuned large runs. The rest is lost to communication, pipeline bubbles, memory stalls and recomputation. Overlapping communication with computation is the main lever.

## Key concepts

| Term | Meaning |
|---|---|
| Scaling law | Empirical power law linking loss to parameters, data and compute |
| Compute-optimal | Allocation of a fixed compute budget between model size and data that minimises loss |
| All-reduce | Collective operation leaving every device with the sum of all devices' values |
| Data parallelism | Replicate the model, split the batch, average gradients |
| Tensor parallelism | Split individual layers' matrices across devices |
| Pipeline parallelism | Place consecutive layers on different devices and stream micro-batches |
| Mixed precision | Low-precision arithmetic with higher-precision accumulation and master weights |
| Checkpointing | Periodically saving full training state to resume after failure |
| MFU | Achieved useful floating-point operations per second divided by hardware peak |

## How it fits

- **Below:** Throughput comes from [Graphics Processing Units (GPUs)](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) and [tensor accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md); low-precision formats from [floating point](../../03-digital-logic/01-number-representation/floating-point.md); the parallel decomposition from [data and task parallelism](../../10-distributed-and-parallel-computing/01-parallel-computing/data-and-task-parallelism.md) and [parallel programming models](../../10-distributed-and-parallel-computing/01-parallel-computing/parallel-programming-models.md); failure handling from [system models and failures](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md); limits from [Amdahl's law](../../04-computer-architecture/06-performance/amdahls-law.md) and [power](../../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md).
- **Above:** Every frontier [large language model](../04-advanced-paradigms/large-language-models.md) and large [generative model](../04-advanced-paradigms/generative-models.md) is a product of these techniques; the hardware runs in [cloud](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) data centres whose energy use raises questions in [computing in context](../../15-computing-in-context/ethics-and-professional-responsibility.md).
- **Siblings:** It scales the loop defined in [backpropagation](neural-networks-and-backpropagation.md); [transformers](attention-and-transformers.md) won partly because their dense, parallel structure suits it.

## Common misconceptions

- **"Scaling laws predict capabilities."** They predict loss well. Specific capabilities on downstream tasks can improve smoothly or appear abruptly depending on the metric used, and are much harder to forecast.
- **"More GPUs means proportionally faster training."** Communication, synchronisation and the critical batch size bound the speed-up, as Amdahl's law predicts.
- **"Bigger is always better."** For a fixed compute budget, a smaller model trained on more data can beat a larger undertrained one, and smaller models are cheaper to serve.

## Go deeper

- Jared Kaplan et al., "Scaling Laws for Neural Language Models" (2020): the original power-law measurements.
- Jordan Hoffmann et al., "Training Compute-Optimal Large Language Models" (2022): the Chinchilla correction on balancing data and parameters.
- Deepak Narayanan et al., "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM" (2021): tensor, pipeline and data parallelism combined.
- Samyam Rajbhandari et al., "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models" (2020): sharding optimiser state.
