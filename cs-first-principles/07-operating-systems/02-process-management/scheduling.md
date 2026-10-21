# Scheduling

> **Layer:** [07 Operating Systems](../README.md) › [Process management](README.md)
> **Builds on:** [Processes](processes.md), [Threads](threads.md), [Heaps and priority queues](../../05-algorithms-and-data-structures/02-fundamental-data-structures/heaps-and-priority-queues.md), [Latency, bandwidth and queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md)
> **Enables:** [Virtual machines and hypervisors](../07-virtualization/virtual-machines-and-hypervisors.md), [Containers](../07-virtualization/containers.md), [Cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md)

## Essence

A scheduler decides which runnable thread runs on each Central Processing Unit (CPU) core and for how long. It is pure policy over the context-switch mechanism, and it must balance goals that conflict: high **throughput** (finish many jobs), low **turnaround** (finish each job soon), low **response time** (react quickly to interactive input), and **fairness** (no thread starves). The scheduler does not know how long a job will run, so practical schedulers either predict the future from the past (multi-level feedback queues) or give up on prediction and divide time proportionally (fair-share schedulers such as Linux's). On multicores the scheduler must also decide *where*, trading load balance against cache affinity.

## Core tenets

1. **No single policy optimizes every metric.** Shortest Job First (SJF) and its preemptive form, Shortest Remaining Time First (SRTF), provably minimize average turnaround time, because running a short job first delays every long job by little while running a long job first delays every short job by a lot. Round Robin (RR), which gives each job a short time slice in turn, gives good response time but poor turnaround. First In, First Out (FIFO) suffers the convoy effect: short jobs queue behind a long one. The choice of metric decides the "best" scheduler.

2. **The scheduler does not know the future, so it learns from the past.** SJF needs job lengths in advance, which an Operating System (OS) does not have. The Multi-Level Feedback Queue (MLFQ), from Corbató's Compatible Time-Sharing System (CTSS, 1962), infers them: a new job starts at high priority; if it uses its whole slice it is moved down (it looks CPU-bound); if it blocks early it stays high (it looks interactive). Periodic priority boosts prevent starvation and let jobs that change behaviour move back up. Variants of this idea underlie the Windows NT and classic BSD schedulers.

3. **Proportional-share scheduling trades prediction for fairness.** Instead of guessing lengths, give each thread a share of CPU time proportional to its weight. Linux's Completely Fair Scheduler (CFS, 2007–2023) tracked each task's weighted *virtual runtime* in a red-black tree and always ran the task with the least, so CPU time converged to the weights; picking the next task is O(log n). Since kernel 6.6 (2023) Linux uses Earliest Eligible Virtual Deadline First (EEVDF), which keeps proportional shares but also gives latency-sensitive tasks earlier deadlines.

4. **The time slice sets the tradeoff between responsiveness and overhead.** Shorter slices make the system feel more responsive but spend a larger fraction of time switching and refilling caches. With switch costs of a few microseconds plus cache effects, slices of roughly 1–10 ms keep overhead small while staying below human perception thresholds (around 100 ms for interactive feedback).

5. **Threads that mostly wait for input/output (I/O) should run first when they wake.** A thread that runs briefly then blocks on I/O keeps devices busy; running it promptly overlaps device work with CPU work and improves total throughput. Both MLFQ (favouring jobs that block early) and fair schedulers (a sleeping task's virtual runtime falls behind, so it runs soon after waking) give this behaviour without special cases.

6. **Multicore scheduling is a tension between balance and affinity.** A single global run queue balances load perfectly but becomes a lock contention point and moves threads between cores, losing their cache contents. Per-core run queues (Linux, Windows) keep threads near their caches and scale, but need periodic load balancing and work stealing to keep cores busy. Non-Uniform Memory Access (NUMA) machines add a further reason to keep threads near their memory.

7. **Priority creates the risk of priority inversion.** If a low-priority thread holds a lock that a high-priority thread needs, and medium-priority threads keep the low one from running, the high one waits indefinitely. This hung the Mars Pathfinder lander's software in 1997 until priority inheritance (temporarily raising the lock holder's priority) was enabled. Real-time schedulers (Linux `SCHED_FIFO`, `SCHED_DEADLINE`) give hard priorities and need such protocols.

8. **Scheduling is a queueing system, so utilization near 100% means long waits.** When arrivals are random, average waiting time grows sharply as utilization approaches one; in the simplest single-server model it scales as 1/(1 − ρ) for utilization ρ ([latency, bandwidth and queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md)). Interactive systems therefore keep headroom, and control groups (cgroups) let administrators cap or reserve CPU shares for groups of processes.

## Key concepts

| Term | Meaning |
|---|---|
| Turnaround time | Completion time minus arrival time |
| Response time | Time from arrival until first run (or first output) |
| Time slice (quantum) | Maximum time a thread runs before being preempted |
| Preemptive scheduling | The OS may take the CPU from a running thread, usually on a timer interrupt |
| MLFQ | Multi-Level Feedback Queue; priorities adjusted from observed behaviour |
| Virtual runtime | CPU time used, scaled by weight; fair schedulers run the smallest |
| Load balancing | Moving threads between per-core run queues to keep cores busy |
| Processor affinity | Preferring to run a thread on the core whose cache it has warmed |
| Priority inversion | A high-priority thread waits on a lock held by a low-priority one |

## How it fits

- **Below:** uses the timer interrupt and context switch from [kernel mode and system calls](../01-kernel-and-abstractions/kernel-mode-and-system-calls.md) and the data structures of [priority queues](../../05-algorithms-and-data-structures/02-fundamental-data-structures/heaps-and-priority-queues.md) and [search trees](../../05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md). Scheduling without knowing the future is an [online problem](../../05-algorithms-and-data-structures/07-advanced-topics/streaming-and-online-algorithms.md).
- **Above:** hypervisors schedule virtual CPUs ([virtual machines and hypervisors](../07-virtualization/virtual-machines-and-hypervisors.md)); cgroups CPU controllers enforce container limits ([containers](../07-virtualization/containers.md)); cluster schedulers in [cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) reapply the same ideas across machines.
- **Siblings:** [processes](processes.md) and [threads](threads.md) are what gets scheduled; locks from [concurrency](../03-concurrency/locks-and-semaphores.md) interact with priority.

## Common misconceptions

- **"Fair means everyone gets an equal time slice."** Fair schedulers give time in proportion to weights, and a thread that sleeps gets to run sooner when it wakes; equal slices would penalize interactive work.
- **"Higher priority always means running sooner."** Priority inversion and starvation-prevention boosts can both make a lower-priority thread run first.
- **"A busy CPU at 100% is efficient."** It may be, for batch work, but queueing delay for any new arrival grows without bound as utilization nears 100%.

## Go deeper

- Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (2018), scheduling chapters (MLFQ, proportional share, multiprocessor).
- Fernando J. Corbató, Marjorie Merwin-Daggett and Robert C. Daley, "An Experimental Time-Sharing System" (1962): the origin of multilevel feedback.
- Carl A. Waldspurger and William E. Weihl, "Lottery Scheduling: Flexible Proportional-Share Resource Management" (OSDI 1994).
- Ion Stoica and Hussein Abdel-Wahab, "Earliest Eligible Virtual Deadline First" (technical report, 1995): the algorithm behind Linux's current scheduler.
