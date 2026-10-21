# Stacks and Queues

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Fundamental Data Structures](README.md)
> **Builds on:** [Arrays and Linked Lists](arrays-and-linked-lists.md), [Context-Free Grammars and Pushdown Automata](../../02-theory-of-computation/02-automata-and-formal-languages/context-free-grammars-and-pushdown-automata.md)
> **Enables:** [Graph Traversal](../05-graph-algorithms/graph-traversal.md), [Lexing and Parsing](../../06-programming-languages/03-compilers/lexing-and-parsing.md), [Scheduling](../../07-operating-systems/02-process-management/scheduling.md), [Latency, Bandwidth and Queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md)

## Essence

A stack and a queue are collections that restrict *which* element you may remove. A stack returns the most recently added element (Last In, First Out, LIFO). A queue returns the least recently added (First In, First Out, FIFO). The restriction is the point: by giving up arbitrary access, both achieve O(1) for every operation with tiny constants, and each order matches a fundamental pattern of computation. Stacks match nesting (function calls, brackets, backtracking, depth-first exploration). Queues match fairness and arrival order (buffers, schedulers, breadth-first exploration).

## Core tenets

1. **A stack is the natural structure for nested, recursive work.** When a computation must suspend one task, do a sub-task, and resume, the most recently suspended task is the one to resume next. That is LIFO. This is why every processor has a stack pointer register and every language runtime has a call stack holding return addresses, saved registers and local variables in frames.

2. **Recursion and an explicit stack are interchangeable.** Any recursive algorithm can be rewritten as a loop with an explicit stack, and vice versa. Explicit stacks avoid call-stack overflow (default thread stacks are often 1–8 MiB) and let you control memory. Depth-First Search (DFS), backtracking, expression evaluation and iterative tree traversals all work this way.

3. **Stacks recognise exactly the nesting that finite memory cannot.** A finite automaton cannot check balanced parentheses because it would need unbounded memory to count depth. Adding one stack gives a pushdown automaton, which recognises exactly the context-free languages. That is the theoretical reason parsers for programming languages use stacks ([pushdown automata](../../02-theory-of-computation/02-automata-and-formal-languages/context-free-grammars-and-pushdown-automata.md)).

4. **A queue is the natural structure for fairness and order of arrival.** If work must be served in the order it arrived (network packets, print jobs, requests, Breadth-First Search (BFS) frontier vertices), FIFO is the specification. BFS finds shortest paths in unweighted graphs precisely because the queue processes vertices in non-decreasing distance order.

5. **Both are O(1) per operation with either arrays or linked lists.** A stack is an array plus a top index. A queue on an array uses a *circular buffer*: head and tail indices that wrap modulo the capacity, so neither end ever shifts data. With geometric resizing, all operations are O(1) amortized. Array versions are usually faster than linked ones for the cache reasons in [arrays and linked lists](arrays-and-linked-lists.md).

6. **A deque generalises both.** A double-ended queue allows push and pop at both ends in O(1). Work-stealing schedulers (Cilk, Java's ForkJoinPool, Go's runtime, Rust's Rayon) give each worker a deque: the owner pushes and pops at one end (LIFO, good locality), and idle workers steal from the other end (FIFO, taking older and usually larger tasks).

7. **Bounded queues create back-pressure, unbounded queues hide overload.** In real systems a queue decouples a producer from a consumer running at different rates. If the producer is faster on average, an unbounded queue grows without limit and latency rises with it; a bounded queue forces the producer to slow down or drop work. Queueing theory says that as utilisation approaches 100%, mean waiting time grows without bound (for an M/M/1 queue, waiting time is proportional to ρ/(1 − ρ)).

8. **Concurrent queues are a hard synchronisation problem.** A single-producer, single-consumer ring buffer can be lock-free with just two indices and memory barriers. Multi-producer, multi-consumer queues need atomic compare-and-swap and careful handling of reclamation, as in the Michael–Scott queue (1996).

## Key concepts

| Term | Meaning |
|---|---|
| Stack (LIFO) | push and pop at the same end; peek at the top |
| Queue (FIFO) | enqueue at the tail, dequeue at the head |
| Deque | Double-ended queue: O(1) insert and remove at both ends |
| Circular (ring) buffer | Fixed array with wrapping head and tail indices |
| Call stack | Runtime stack of activation frames for active function calls |
| Stack overflow | Exceeding the memory reserved for a stack, typically by deep recursion |
| Back-pressure | Slowing a producer when a bounded queue is full |
| Monotonic stack / queue | A stack or deque kept sorted, used for sliding-window min/max in O(n) total |

## How it fits

- **Below:** the hardware stack pointer and call/return instructions are defined by the [Instruction Set Architecture (ISA)](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md); [pushdown automata](../../02-theory-of-computation/02-automata-and-formal-languages/context-free-grammars-and-pushdown-automata.md) give the theory.
- **Above:** [parsers](../../06-programming-languages/03-compilers/lexing-and-parsing.md) use stacks; [interpreters and virtual machines](../../06-programming-languages/04-runtime-systems/interpreters-and-virtual-machines.md) such as the Java Virtual Machine are stack machines; [schedulers](../../07-operating-systems/02-process-management/scheduling.md) use run queues; [routers](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) are networks of queues; [message brokers](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md) are durable distributed queues.
- **Siblings:** [heaps](heaps-and-priority-queues.md) generalise queues by serving the highest *priority* rather than the oldest; Dijkstra's algorithm is BFS with the queue replaced by a priority queue.

## Common misconceptions

- **"Recursion is free."** Each call pushes a frame. Deep recursion can overflow the stack long before memory is exhausted, which is why production code often uses explicit stacks.
- **"A queue just needs a list with remove-from-front."** Removing from the front of a plain array is O(n); you need a circular buffer or a linked list for O(1).
- **"An unbounded queue makes a system robust."** It converts overload into ever-growing latency and memory use instead of a visible error.

## Go deeper

- Donald E. Knuth, *The Art of Computer Programming, Vol. 1* (3rd ed., 1997): section 2.2.1 on stacks, queues and deques.
- Maged Michael and Michael Scott, "Simple, Fast, and Practical Non-Blocking and Blocking Concurrent Queue Algorithms" (1996): the standard lock-free queue.
- Robert Sedgewick and Kevin Wayne, *Algorithms* (4th ed., 2011): clear array and linked implementations with resizing.
