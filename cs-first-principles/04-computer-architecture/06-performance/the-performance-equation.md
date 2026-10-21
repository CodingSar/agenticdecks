# The Performance Equation

> **Layer:** [04 Computer Architecture](../README.md) › [Performance](README.md)
> **Builds on:** [Datapath and control](../02-processor-microarchitecture/datapath-and-control.md), [Pipelining](../02-processor-microarchitecture/pipelining.md), [Measurement and modeling](../../00-engineering-foundations/05-engineering-method/measurement-and-modeling.md), [Statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md)
> **Enables:** [Amdahl's law](amdahls-law.md), [Compiler optimization](../../06-programming-languages/03-compilers/optimization.md), [Asymptotic analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md), [Observability](../../12-software-engineering/04-operations/observability.md)

## Essence

The only honest measure of a computer's speed is the time it takes to run the programs you care about. The performance equation, sometimes called the "iron law" of processor performance, breaks that time into three factors: Central Processing Unit (CPU) time = instruction count × Cycles Per Instruction (CPI) × clock period. Each factor is controlled by different layers: the algorithm, language and compiler decide how many instructions run; the Instruction Set Architecture (ISA) and microarchitecture decide how many cycles each takes on average; circuit design and process technology decide how short a cycle can be. Because the factors interact, improving one alone (for example, raising the clock rate) can make total time worse, and any single-number metric that leaves out a factor misleads.

## Core tenets

1. **Execution time is the measure; everything else is a proxy.** Clock frequency, instructions per second and peak floating-point rate are each one factor or a ratio of factors. A 4 GHz chip can be slower than a 3 GHz chip if it needs more cycles per instruction or more instructions. Only time on a representative workload captures all factors together.

2. **The three factors multiply.** CPU time = (instructions / program) × (cycles / instruction) × (seconds / cycle). A program of 10^10 instructions with CPI 0.5 on a 4 GHz (0.25 ns) clock takes 10^10 × 0.5 × 0.25 ns = 1.25 s. Halving any factor halves the time, but design choices usually move several at once.

3. **Each layer controls a different factor.** Instruction count depends on the algorithm (an O(n log n) sort runs far fewer instructions than an O(n²) one for large n), the language and compiler, and the ISA (complex instructions do more each). CPI depends on the microarchitecture (pipelining, superscalar width, branch prediction, cache misses) and on the instruction mix. Clock period depends on pipeline depth, circuit design and transistor speed.

4. **The factors trade against each other.** Deeper pipelines shorten the clock period but raise CPI through larger branch-misprediction penalties. Complex Instruction Set Computer (CISC) instructions lower instruction count but can raise CPI. Aggressive compiler optimisations may raise instruction count (loop unrolling, inlined code) while lowering CPI. The Pentium 4 era (2000–2006) is the cautionary tale: frequency rose, but CPI rose too, and power exploded.

5. **CPI is an average with structure.** CPI = base CPI + stall cycles per instruction from memory, branches and other hazards. On real workloads the memory term often dominates: a 1% rate of cache misses that go to Dynamic Random-Access Memory (DRAM) at 300 cycles each adds 3 cycles per instruction, more than the base CPI of a wide core (0.25–0.5). Its reciprocal, Instructions Per Cycle (IPC), is the more common modern figure: typically 1–4 on 2020s cores.

6. **Benchmarks must represent real work, and summaries must be honest.** Standard suites such as the Standard Performance Evaluation Corporation's SPEC CPU (since 1989) use real programs to resist tuning for toy kernels. Ratios to a reference machine should be combined with the geometric mean, because it gives the same ranking regardless of which machine is the reference. Measurements need repeated runs and attention to variance, warm-up and noise from other processes.

7. **Throughput and latency are different goals.** Latency is time for one task; throughput is tasks per unit time. A server may accept longer individual latencies to complete more requests per second; a Graphics Processing Unit (GPU) sacrifices single-thread latency for enormous throughput. The performance equation describes latency of one program on one core; throughput adds the dimension of parallel resources.

8. **The roofline model extends the equation to bandwidth limits.** For data-intensive code, attainable performance = min(peak compute, memory bandwidth × arithmetic intensity), where arithmetic intensity is operations per byte moved. Plotting this shows at a glance whether a kernel is memory-bound or compute-bound, and therefore whether to optimise data movement or arithmetic.

## Key concepts

| Term | Meaning |
|---|---|
| CPU time | Time the processor spends executing a program (excluding waiting for I/O or other programs) |
| Instruction count | Number of instructions executed (dynamic count, not lines of code) |
| CPI / IPC | Average cycles per instruction / its reciprocal, instructions per cycle |
| Clock period / frequency | Duration of one cycle / cycles per second |
| Iron law | CPU time = instruction count × CPI × clock period |
| Benchmark suite | Set of representative programs used to compare machines |
| Geometric mean | n-th root of a product of n ratios; the consistent way to summarise normalised results |
| Roofline model | Bound on performance from peak compute and memory bandwidth as a function of arithmetic intensity |

## How it fits

- **Below:** the clock period comes from [timing and power](../../03-digital-logic/04-hardware-design/timing-and-power.md); CPI from the [datapath](../02-processor-microarchitecture/datapath-and-control.md), [pipelining](../02-processor-microarchitecture/pipelining.md) and the [memory hierarchy](../03-memory-hierarchy/locality-and-caching.md); good measurement from [measurement and modeling](../../00-engineering-foundations/05-engineering-method/measurement-and-modeling.md) and [statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md).
- **Above:** [asymptotic analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md) governs instruction count as inputs grow, while this equation governs the constant factors; [compiler optimization](../../06-programming-languages/03-compilers/optimization.md) targets instruction count and CPI; [observability](../../12-software-engineering/04-operations/observability.md) applies the same discipline to production systems.
- **Siblings:** [Amdahl's law](amdahls-law.md) uses this equation to bound partial improvements; [power and the end of scaling](power-and-the-end-of-scaling.md) explains why the clock-period factor stopped shrinking.

## Common misconceptions

- **"Higher clock speed means a faster computer."** Clock rate is one factor of three; the "megahertz myth" of the early 2000s showed lower-clocked designs beating higher-clocked ones.
- **"MIPS measures performance."** Millions of Instructions Per Second (MIPS) ignores instruction count: a machine can score higher MIPS by executing more, simpler instructions to do the same work.
- **"Peak floating-point operations per second (FLOP/s) tells you how fast your program will run."** Most programs reach a small fraction of peak because they are limited by memory bandwidth or dependences, which the roofline model makes visible.

## Go deeper

- Hennessy and Patterson, *Computer Architecture: A Quantitative Approach* (6th ed., 2017), Chapter 1: the quantitative principles and the performance equation.
- Fleming and Wallace, *How Not to Lie with Statistics: The Correct Way to Summarize Benchmark Results* (CACM, 1986): why the geometric mean.
- Williams, Waterman and Patterson, *Roofline: An Insightful Visual Performance Model for Multicore Architectures* (CACM, 2009): the roofline model.
- Jain, *The Art of Computer Systems Performance Analysis* (1991): measurement, experimental design and statistics for systems.
