# Models of Computation

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Foundations](README.md)
> **Builds on:** [Turing Machines](../../02-theory-of-computation/03-computability/turing-machines.md), [Asymptotic Analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md), [Locality and Caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md)
> **Enables:** [Comparison Sorting](../04-sorting-and-searching/comparison-sorting.md), [External Memory and Cache-Oblivious Algorithms](../07-advanced-topics/external-memory-and-cache-oblivious.md), [Work, Span and Parallel Models](../../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md)

## Essence

To say an algorithm "takes O(n log n) time" you must first say what one unit of time is. A model of computation fixes this: which operations cost one step, how big a memory word is, and what is free. The standard choice is the Random Access Machine (RAM): a processor that reads or writes any memory cell in one step and does arithmetic on word-sized integers in one step. The RAM is an idealised von Neumann computer, chosen because it is simple enough to analyse and close enough to real hardware that its predictions usually rank algorithms correctly. Other models (comparison, word RAM, I/O, parallel) change what is counted, and each answers a question the RAM cannot.

## Core tenets

1. **Every complexity bound is relative to a model.** The Ω(n log n) lower bound for sorting holds in the *comparison model*, where the only way to learn about keys is to compare two of them. Radix sort escapes it by reading key bits directly, which the comparison model forbids. A bound with no stated model is ambiguous, and arguments that "beat" a known lower bound almost always changed the model.

2. **The RAM charges unit cost for memory access and word arithmetic.** Instructions such as load, store, add, compare and branch each cost 1. This mirrors a processor executing one instruction per cycle on registers and memory. It deliberately ignores the cache hierarchy, pipelining and instruction-level parallelism, which is why the RAM gives correct asymptotic rankings but poor absolute predictions.

3. **Word size must be bounded, or the model becomes absurdly strong.** If a word could hold an arbitrarily large integer in unit time, you could pack an entire array into one number and sort it with a few multiplications. The *word RAM* fixes words at w bits with w ≥ log₂ n, so a word can hold an index or pointer into the input but not the input itself. Many fast integer algorithms (radix sort, van Emde Boas trees, fusion trees) are word-RAM results.

4. **Turing machines and RAMs agree on what is polynomial.** A RAM running in time T(n) can be simulated by a multi-tape Turing machine in time polynomial in T(n) (roughly O(T(n)³) for a straightforward simulation with logarithmic-cost memory). So the class P is the same in both models, which is why complexity theory can use Turing machines while algorithm design uses RAMs. The models disagree on exponents: an O(n) RAM algorithm may be O(n²) on a single-tape Turing machine.

5. **The I/O model counts block transfers, not instructions.** Real memory is a hierarchy: a Level 1 (L1) cache hit costs ~1 ns, a Dynamic Random-Access Memory (DRAM) access ~100 ns, a Solid-State Drive (SSD) random read ~10–100 µs, a disk seek ~5–10 ms (circa 2020s). The external-memory model has a fast memory of M words and a slow memory accessed in blocks of B words; cost is the number of block transfers. Scanning n items costs Θ(n/B) transfers and sorting costs Θ((n/B) log_{M/B}(n/B)), bounds that the RAM cannot express. B-trees exist because of this model.

6. **Parallel models measure work and span.** The Parallel RAM (PRAM) lets p processors share memory. The more practical work–span view charges total operations (work W) and the longest dependency chain (span S); a greedy scheduler on p processors finishes in at most W/p + S steps (Brent's bound). An algorithm with small work but long span cannot use many processors.

7. **Worst-case, average-case, expected and amortized are different questions.** Worst case bounds the slowest input. Average case assumes a distribution over inputs, which is fragile because real inputs are rarely random. Expected time averages over the algorithm's own coin flips on a worst-case input, which is robust. Amortized time averages over a worst-case sequence of operations. Quicksort is Θ(n²) worst case but Θ(n log n) expected with random pivots.

8. **Constant factors and memory behaviour decide practice.** Asymptotics hide constants and ignore which accesses are sequential. Insertion sort beats merge sort below roughly 10–50 elements, which is why real libraries switch to it for small subarrays. Pointer-chasing structures often lose to arrays with a worse bound, because each cache miss costs about a hundred instructions' worth of time.

## Key concepts

| Term | Meaning |
|---|---|
| RAM model | Unit-cost access to any memory cell and unit-cost basic operations |
| Word RAM | RAM with w-bit words, w ≥ log n, and unit-cost bitwise and arithmetic operations on words |
| Comparison model | Algorithms learn about keys only through pairwise comparisons; cost is the number of comparisons |
| Decision tree | A tree of comparisons whose leaves are outputs; its height is a worst-case lower bound |
| I/O (external-memory) model | Fast memory of size M, slow memory moved in blocks of size B; cost is block transfers |
| PRAM | Synchronous shared-memory parallel RAM with p processors |
| Work / span | Total operations / length of the longest dependency chain |
| Uniform vs logarithmic cost | Unit cost per operation vs cost proportional to operand bit length |

## How it fits

- **Below:** the RAM idealises the [Instruction Set Architecture (ISA) contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md) and assumes flat memory, which [the memory hierarchy](../../04-computer-architecture/03-memory-hierarchy/README.md) violates. Its equivalence to [Turing machines](../../02-theory-of-computation/03-computability/turing-machines.md) up to polynomial factors is what lets [complexity classes](../../02-theory-of-computation/04-complexity/complexity-classes.md) be machine-independent.
- **Above:** every bound in this layer, [query cost models](../../09-data-management/03-query-processing/query-optimization.md) in databases (which count page I/Os), and the [work–span model](../../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md) for parallel programs.
- **Siblings:** [correctness and invariants](correctness-and-invariants.md) says *whether* the answer is right; this file says *what it costs*. [Amortized analysis](amortized-analysis.md) is a way of counting within a model.

## Common misconceptions

- **"Big-O tells you which program is faster."** It tells you which grows slower for large enough n, in a given model. For realistic sizes, constants and cache behaviour often dominate.
- **"The RAM model is the computer."** It is a deliberate fiction of uniform memory. A random access into a large array can be ~100 times slower than a sequential one.
- **"Radix sort disproves the n log n sorting bound."** The bound is for the comparison model; radix sort uses a different model.

## Go deeper

- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (4th ed., 2022): chapter 2 defines the RAM model used throughout the field.
- Aho, Hopcroft, Ullman, *The Design and Analysis of Computer Algorithms* (1974): the classic careful treatment of RAM cost measures.
- Aggarwal and Vitter, "The Input/Output Complexity of Sorting and Related Problems" (1988): defines the external-memory model and its sorting bound.
