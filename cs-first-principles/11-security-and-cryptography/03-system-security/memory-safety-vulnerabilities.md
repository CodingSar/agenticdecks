# Memory Safety Vulnerabilities

> **Layer:** [11 Security and Cryptography](../README.md) › [System security](README.md)
> **Builds on:** [Memory management and garbage collection](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md), [Type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md), [Memory allocation](../../07-operating-systems/04-memory-management/memory-allocation.md), [Instruction encoding and addressing](../../04-computer-architecture/01-instruction-set-architecture/instruction-encoding-and-addressing.md)
> **Enables:** [Isolation and sandboxing](isolation-and-sandboxing.md), [Static analysis and code review](../../12-software-engineering/03-quality/static-analysis-and-code-review.md), [Testing](../../12-software-engineering/03-quality/testing.md)

## Essence

In languages such as C and C++, the program is trusted to keep every memory access within the bounds and lifetime of the object it means to touch; the language and hardware do not check. A single mistake, writing past the end of a buffer or using memory after it has been freed, lets attacker-controlled data overwrite other data, including pointers and return addresses that decide what code runs next. That turns a bug into **arbitrary code execution** with the program's privileges. These bugs have dominated serious vulnerabilities for decades: Microsoft and the Chromium project have each reported that roughly 70% of their high-severity security bugs are memory-safety issues. Mitigations make exploitation harder; only **memory-safe languages** and hardware-enforced bounds remove the class.

## Core tenets

1. **Memory safety has two halves: spatial and temporal.** *Spatial* safety means every access stays within its object's bounds; violations are buffer overflows and out-of-bounds reads. *Temporal* safety means every access happens while the object is alive; violations are use-after-free, double free and use of uninitialised memory. C's pointers carry neither bounds nor lifetime information, so neither property can be checked at run time without extra machinery.

2. **Stack smashing shows how a bug becomes control.** A function's local buffer sits on the stack near its saved return address. Copying attacker input into the buffer without a length check (classically with `strcpy` or `gets`) overwrites the return address; when the function returns, the processor jumps where the attacker chose. Aleph One's "Smashing the Stack for Fun and Profit" (1996) popularised the technique; the Morris worm (1988) had already used a buffer overflow in `fingerd`.

3. **Use-after-free exploits the allocator.** When an object is freed and its memory reused for a different object, a stale pointer to the old object now reads or writes the new one. If the attacker controls what is allocated in the freed slot, they control the fields the program trusts, often a function pointer or a virtual-method table pointer. Use-after-free is now the leading bug class in browsers because their object lifetimes are complex.

4. **Mitigations raise cost but do not fix the bug.** *Stack canaries* place a random value before the return address and check it on return. *Non-executable memory* (often called DEP, Data Execution Prevention, or the no-execute (NX) bit) stops injected data from running as code. *Address space layout randomisation* (ASLR) moves code and data to unpredictable addresses. Each forced attackers to adapt rather than stopping them, because a memory-corruption primitive is usually powerful enough to leak secrets (defeating ASLR and canaries) and reuse existing code.

5. **Code-reuse attacks defeat non-executable memory.** Return-oriented programming (ROP; Shacham, 2007) chains short existing instruction sequences ending in `ret` ("gadgets") into arbitrary computation, so no new code is injected. Control-flow integrity (CFI) restricts indirect jumps and returns to targets allowed by the program's control-flow graph; hardware support now exists in the form of shadow stacks for return addresses and landing-pad instructions for indirect branches (Intel's Control-flow Enforcement Technology (CET), and ARM's Branch Target Identification (BTI) and pointer authentication).

6. **Undefined behaviour makes bugs worse than they look.** The C and C++ standards say an out-of-bounds access or signed overflow has undefined behaviour, so compilers may assume it never happens and optimise accordingly, sometimes deleting the very bounds check the programmer wrote. Security reasoning about C code must therefore consider the compiler, not just the source.

7. **Memory-safe languages remove the class at its root.** Languages with bounds checks and automatic memory management (Java, C#, Go, Python) or with compile-time ownership and borrowing rules (Rust) make spatial and temporal violations impossible in safe code. The cost is run-time checks, garbage-collection overhead, or a stricter type system. Unsafe escape hatches remain, but confine the audit to small regions. Government security agencies and major vendors now recommend memory-safe languages for new code for this reason.

8. **Finding bugs before attackers do is a numbers game.** Fuzzing (feeding mutated inputs and watching for crashes), especially coverage-guided fuzzers such as AFL and libFuzzer, combined with sanitisers such as AddressSanitizer that turn silent corruption into immediate crashes, finds thousands of memory bugs a year in widely used software. Hardware memory tagging (ARM's Memory Tagging Extension) and capability hardware (CHERI) aim to catch violations at run time with low overhead.

## Key concepts

| Term | Meaning |
|---|---|
| Spatial safety | Accesses stay within object bounds |
| Temporal safety | Accesses happen only during the object's lifetime |
| Buffer overflow | Writing past the end of an allocated buffer |
| Use-after-free | Accessing memory through a pointer after it is freed |
| Stack canary | Random guard value checked before a function returns |
| DEP / NX | Marking data pages non-executable |
| ASLR | Randomising memory layout so addresses are unpredictable |
| ROP | Chaining existing code fragments to compute without injecting code |
| CFI | Restricting indirect control transfers to valid targets |

## How it fits

- **Below:** stacks, return addresses and calling conventions come from [instruction encoding](../../04-computer-architecture/01-instruction-set-architecture/instruction-encoding-and-addressing.md) and [code generation](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md); heaps come from [memory allocation](../../07-operating-systems/04-memory-management/memory-allocation.md); safety guarantees come from [type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md) and [garbage collection](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md); non-executable pages and ASLR rely on [paging](../../07-operating-systems/04-memory-management/address-spaces-and-paging.md).
- **Above:** [static analysis](../../12-software-engineering/03-quality/static-analysis-and-code-review.md) and fuzz [testing](../../12-software-engineering/03-quality/testing.md) hunt these bugs; [formal methods](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md) can prove their absence; [isolation and sandboxing](isolation-and-sandboxing.md) contain the damage when one is exploited.
- **Siblings:** [access control](access-control.md) is bypassed from within when the privileged program is hijacked; [side channels](side-channels.md) are the other way to break isolation without breaking checks.

## Common misconceptions

- **"Careful programmers do not write memory bugs."** Decades of data from expert teams show a steady rate of memory-safety bugs in large C and C++ code bases.
- **"ASLR and canaries make overflows unexploitable."** Information leaks and code reuse routinely bypass them.
- **"Memory-safe languages are immune to vulnerabilities."** They remove memory corruption, not logic flaws, injection or misuse of unsafe blocks and foreign-function calls.

## Go deeper

- Aleph One, "Smashing the Stack for Fun and Profit", *Phrack* 49 (1996).
- Szekeres, Payer, Wei and Song, "SoK: Eternal War in Memory", IEEE Symposium on Security and Privacy (2013): a systematic map of attacks and defences.
- Shacham, "The Geometry of Innocent Flesh on the Bone", ACM CCS (2007): return-oriented programming.
- Abadi, Budiu, Erlingsson and Ligatti, "Control-Flow Integrity", ACM CCS (2005).
