# Sequential Logic

> **Layer:** [03 Digital Logic](../README.md) › Sequential Logic
> **Children:** [Latches and Flip-Flops](latches-and-flip-flops.md) · [Clocking and Synchronous Design](clocking-and-synchronous-design.md) · [Finite State Machines](finite-state-machines.md)

## What this area is about

Combinational logic computes functions; it cannot remember anything or do things in sequence. Sequential logic adds state, so that a circuit's output can depend on its history and a computation can proceed step by step. This area answers: *how does hardware remember, how do we keep billions of remembered bits changing in an orderly way, and how do we design with state?*

The unifying idea is **state plus a clock turns hardware into a step-by-step machine**. Memory comes from positive feedback (cross-coupled gates). A shared clock makes every bit of state change at the same instants, so the circuit moves from one well-defined state to the next, exactly like a finite automaton or a program executing one step at a time. This discretisation of time is to sequential circuits what the digital abstraction is to voltages: it hides a messy continuous reality (settling signals, glitches) behind a clean discrete model, at the price of a residual hazard at the boundary (metastability).

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Latches and Flip-Flops](latches-and-flip-flops.md) | The storage elements: bistable loops, edge triggering, setup and hold, metastability | Gates, positive feedback |
| [Clocking and Synchronous Design](clocking-and-synchronous-design.md) | The discipline: one clock, setup and hold constraints, critical paths, clock distribution, domain crossings | Flip-flops, RC delay |
| [Finite State Machines](finite-state-machines.md) | The design method: states, transitions, encodings, controller plus datapath | Flip-flops, clocking, automata theory |

Read in order. Flip-flops provide one bit of state with precise timing parameters. Synchronous design uses those parameters to make whole circuits behave as if all state updates at once on each clock edge. Finite state machines then supply meaning: the designer decides what the circuit must remember and how it moves between states, and the first two leaves guarantee that the hardware will behave as that abstract machine.

```
       ┌──────────── clock ─────────────┐
       ▼                                ▼
   flip-flops ──► combinational logic ──► flip-flops      (synchronous discipline)
       ▲                                     │
       └───────────── next state ────────────┘            (finite state machine)
```

## Connections to sibling areas

- **[Number Representation](../01-number-representation/README.md):** Registers hold fixed-width words, so number formats are register formats. State encodings (binary, one-hot, Gray) are representation choices with costs in logic and power.
- **[Combinational Logic](../02-combinational-logic/README.md):** The logic between registers is combinational; its longest path sets the clock period, and its glitches are made harmless by sampling only at clock edges.
- **[Hardware Design](../04-hardware-design/README.md):** Hardware description languages describe circuits at the register-transfer level, which is exactly this area's model; static timing analysis checks the setup and hold constraints defined here.

## Connections across layers

From below, storage is positive [feedback](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md) in CMOS (Complementary Metal-Oxide-Semiconductor) gates, clock period is bounded by [capacitance and timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md), and finite state machines are the hardware form of [finite automata](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md). Upward, registers and pipeline latches implement [pipelining](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md); a control FSM (finite state machine) sequences the [datapath](../../04-computer-architecture/02-processor-microarchitecture/datapath-and-control.md); Static Random-Access Memory (SRAM) cells form [caches](../../04-computer-architecture/03-memory-hierarchy/cache-design.md). The difficulty of agreeing on time without a shared clock is the central problem of [time, clocks and ordering](../../10-distributed-and-parallel-computing/02-distributed-foundations/time-clocks-and-ordering.md), and state-machine thinking reappears in protocols such as [UDP and TCP](../../08-networking/04-transport-layer/udp-and-tcp.md) and in [model checking](../../06-programming-languages/05-formal-methods/model-checking.md).

## Cross-cutting threads

- [State and time](../../CROSS-CUTTING.md#state-and-time): the clock defines "when"; flip-flops define "what was"; metastability is the cost of forcing continuous time into discrete steps.
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): the synchronous discipline hides settling and glitches behind clean cycles.
- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): inserting registers trades latency for throughput.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): setup and hold constraints are invariants checked on every path.
