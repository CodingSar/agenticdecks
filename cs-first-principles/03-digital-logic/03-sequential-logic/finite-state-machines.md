# Finite State Machines

> **Layer:** [03 Digital Logic](../README.md) › [Sequential Logic](README.md)
> **Builds on:** [Finite Automata and Regular Languages](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md), [Latches and Flip-Flops](latches-and-flip-flops.md), [Clocking and Synchronous Design](clocking-and-synchronous-design.md)
> **Enables:** [Datapath and Control](../../04-computer-architecture/02-processor-microarchitecture/datapath-and-control.md), [Hardware Description Languages](../04-hardware-design/hardware-description-languages.md), [Model Checking](../../06-programming-languages/05-formal-methods/model-checking.md), [UDP and TCP](../../08-networking/04-transport-layer/udp-and-tcp.md)

## Essence

A finite state machine (FSM) is the hardware realisation of a finite automaton: a register holding the current state, combinational logic that computes the next state from the current state and inputs, and logic that computes outputs. Every synchronous digital circuit is an FSM, because its flip-flops hold some state and the logic between them computes the next state on each clock edge. Designing with FSMs means choosing the states first (what the circuit must remember), then deriving the logic. This is where theory meets hardware most directly: the same abstraction that defines regular languages in the theory of computation is what controls a traffic light, a bus protocol or the control unit of a processor.

## Core tenets

1. **An FSM is state register plus next-state logic plus output logic.** On each clock edge the register loads `next = f(state, input)`; outputs are `g(state)` or `g(state, input)`. With `n` flip-flops a machine has at most `2ⁿ` states, so the state register is the circuit's entire memory of the past. Everything else is a pure function, built from combinational logic.

```
             inputs ──────────────┐
                                  ▼
          ┌──────────┐      ┌───────────┐
          │  state   │─────►│ next-state│──┐
          │ register │      │   logic   │  │
          └──────────┘      └───────────┘  │
             ▲    │                         │
     clock ──┘    └─────► output logic ──► outputs
             ▲                              │
             └──────────────────────────────┘ (next state)
```

2. **Moore and Mealy machines differ in when outputs react.** In a Moore machine (Edward Moore, 1956) outputs depend only on the state, so they change only after a clock edge and are glitch-free. In a Mealy machine (George Mealy, 1955) outputs depend on state and current inputs, so they react within the same cycle and often need fewer states, but inputs can ripple straight through to outputs. The choice trades latency against timing cleanliness.

3. **A synchronous FSM is a finite automaton with outputs.** Mathematically, it is a deterministic finite automaton whose transitions fire once per clock. This means everything known about finite automata applies: FSMs recognise exactly the regular languages, can be minimised to a unique smallest equivalent machine, and cannot count without bound. Anything needing unbounded memory, such as matching arbitrarily nested parentheses, needs an external memory, which is how a processor (FSM plus memory) escapes the finite-state limit.

4. **State encoding is a design choice with real costs.** The same abstract machine can be encoded in binary (`⌈log₂ k⌉` flip-flops for `k` states), one-hot (one flip-flop per state, exactly one set), or Gray code (adjacent states differ in one bit). Binary minimises flip-flops; one-hot simplifies and speeds the next-state logic and is favoured on Field-Programmable Gate Arrays (FPGAs) with abundant flip-flops; Gray code reduces switching power and is safe for signals crossing clock domains.

5. **Complex designs split into controller and datapath.** Rather than one enormous FSM, real systems pair a datapath (registers, adders, multiplexers that hold and transform data) with a small control FSM that sequences it by setting multiplexer selects and register enables. The datapath's registers are technically state too, but separating "data state" from "control state" keeps the controller small and understandable. A processor's control unit is exactly such an FSM.

6. **States grow multiplicatively when machines combine.** Two independent FSMs with `a` and `b` states form a combined machine of `a × b` states. This state explosion makes exhaustive reasoning about composed systems expensive and is the central difficulty in verifying hardware and protocols by model checking.

7. **FSMs are the right model whenever behaviour depends on history in a bounded way.** Protocol handlers (the Transmission Control Protocol (TCP) connection states), lexical analysers, vending machines, user-interface modes and game logic are naturally FSMs in software too. Drawing the state diagram first, and checking every state handles every input, catches missing cases that ad hoc flags hide.

## Key concepts

| Term | Meaning |
|---|---|
| State | What the machine remembers about past inputs. |
| State register | Flip-flops holding the encoded current state. |
| Next-state function | Combinational logic computing the next state from state and inputs. |
| Moore machine | FSM whose outputs depend only on state. |
| Mealy machine | FSM whose outputs depend on state and current inputs. |
| State encoding | Assignment of bit patterns to abstract states (binary, one-hot, Gray). |
| State diagram | Graph of states and labelled transitions. |
| Controller / datapath | Control FSM sequencing a separate data-processing structure. |
| State explosion | Multiplicative growth of states when machines are composed. |

## How it fits

- **Below:** The formal model is the deterministic automaton of [finite automata and regular languages](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md); the hardware is [flip-flops](latches-and-flip-flops.md) under [synchronous clocking](clocking-and-synchronous-design.md) plus [combinational logic](../02-combinational-logic/logic-gates.md).
- **Above:** A processor's control unit is an FSM over a datapath ([datapath and control](../../04-computer-architecture/02-processor-microarchitecture/datapath-and-control.md)); adding unbounded memory turns the finite controller into the stored-program machine that approximates a [Turing machine](../../02-theory-of-computation/03-computability/turing-machines.md). FSMs are written in [hardware description languages](../04-hardware-design/hardware-description-languages.md), verified with [model checking](../../06-programming-languages/05-formal-methods/model-checking.md), and reappear as lexers in [lexing and parsing](../../06-programming-languages/03-compilers/lexing-and-parsing.md) and connection state in [UDP and TCP](../../08-networking/04-transport-layer/udp-and-tcp.md).
- **Siblings:** [Latches and flip-flops](latches-and-flip-flops.md) store the state; [clocking](clocking-and-synchronous-design.md) defines when it changes; this leaf defines what it means.

## Common misconceptions

- **"FSMs are a niche controller technique."** Every synchronous circuit is an FSM; the term just names the design view that makes this explicit.
- **"A computer is an FSM, so it is no more powerful than a regular expression."** Strictly, any physical computer has finitely many states, but it is designed and analysed as a controller with a large, extensible memory, which behaves like a Turing machine for all practical purposes.
- **"Fewer flip-flops always means a better FSM."** Dense binary encodings often need slower, larger next-state logic than one-hot.

## Go deeper

- David Harris and Sarah Harris, *Digital Design and Computer Architecture* (2007): FSM design and encoding in hardware.
- George Mealy, "A Method for Synthesizing Sequential Circuits" (1955), and Edward Moore, "Gedanken-Experiments on Sequential Machines" (1956): the two founding machine models.
- John Hopcroft, Rajeev Motwani and Jeffrey Ullman, *Introduction to Automata Theory, Languages, and Computation* (2001 edition): the theory behind FSMs, including minimisation.
