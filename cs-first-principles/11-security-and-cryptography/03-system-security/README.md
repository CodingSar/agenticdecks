# System Security

> **Layer:** [11 Security and Cryptography](../README.md) › System security
> **Children:** [Access control](access-control.md) · [Memory safety vulnerabilities](memory-safety-vulnerabilities.md) · [Isolation and sandboxing](isolation-and-sandboxing.md) · [Side channels](side-channels.md)

## What this area is about

System security asks how a single computer, shared by many programs and users who do not fully trust each other, keeps each from reading or corrupting what belongs to the others. Cryptography protects data that leaves your control; system security protects computation that runs on hardware you control at least in part. Its subject is the machinery of the lower layers, the processor's privilege modes, virtual memory, the kernel, the language runtime, viewed as an enforcement mechanism that an attacker is actively probing.

The unifying idea is **enforcing boundaries between principals**. Access control decides what each principal may do. Isolation makes the boundary hold in hardware and software. Memory-safety bugs and side channels are the two main ways boundaries fail: the first lets an attacker hijack code inside the boundary, the second lets information leak across it without breaking any rule the system checks.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Access control](access-control.md) | The policy: who (subject) may do what (right) to which object; how policies are stored and checked | Design principles, OS abstractions |
| [Isolation and sandboxing](isolation-and-sandboxing.md) | The enforcement: processes, virtual machines, containers, sandboxes and enclaves that confine code | Virtual memory, kernel mode, virtualization |
| [Memory safety vulnerabilities](memory-safety-vulnerabilities.md) | The most common way code inside a boundary is subverted, and the mitigations | Languages, compilers, memory layout |
| [Side channels](side-channels.md) | Leaks across boundaries through timing, caches, power and speculation | Microarchitecture, caches |

```
     policy:        access control (who may do what)
                          |
     enforcement:   isolation (kernel, hypervisor, sandbox, enclave)
                    /                                  \
     failure modes: memory corruption              side channels
                    (attacker runs code            (secrets leak through
                     inside the boundary)           shared hardware)
```

Read access control first, since it states what the system is trying to enforce, then isolation, which is how enforcement is built. The last two are complementary failure modes. Memory-safety bugs subvert a program from within, so that the program uses its own legitimate privileges for the attacker. Side channels leave every check intact but reveal secrets through physical effects of computation. Defending against both drives much of current hardware and language design.

## Connections to sibling areas

- **[Security principles](../01-security-principles/README.md):** least privilege, complete mediation and a minimal trusted computing base are realised here as access-control policies, reference monitors and small kernels.
- **[Cryptography](../02-cryptography/README.md):** keys must be protected by isolation (hardware security modules, enclaves), and cryptographic code must be constant-time to resist side channels.
- **[Network and application security](../04-network-and-application-security/README.md):** a browser is an operating system for web content, and the same-origin policy is an access-control policy enforced by process sandboxing; authentication supplies the identities that access control checks.

## Connections across layers

The enforcement mechanisms come from [04 Computer Architecture](../../04-computer-architecture/README.md) ([virtual memory hardware](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md), privilege modes), [07 Operating Systems](../../07-operating-systems/README.md) ([kernel mode](../../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md), [address spaces](../../07-operating-systems/04-memory-management/address-spaces-and-paging.md), [virtual machines](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md), [containers](../../07-operating-systems/07-virtualization/containers.md)), and [06 Programming Languages](../../06-programming-languages/README.md) ([type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md), [garbage collection](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md)). The failure modes come from the same places: [caches](../../04-computer-architecture/03-memory-hierarchy/cache-design.md) and [speculative execution](../../04-computer-architecture/02-processor-microarchitecture/superscalar-and-out-of-order.md) leak; C's [manual memory management](../../07-operating-systems/04-memory-management/memory-allocation.md) corrupts. Upward, [cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) depends on isolation between tenants, and [static analysis](../../12-software-engineering/03-quality/static-analysis-and-code-review.md) and fuzz [testing](../../12-software-engineering/03-quality/testing.md) find memory-safety bugs.

## Cross-cutting threads

- [Virtualization](../../CROSS-CUTTING.md#virtualization): isolation by giving each principal its own virtual machine.
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): side channels and undefined behaviour are leaks in abstractions.
- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): capabilities are unforgeable names that carry authority.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): shared caches are the classic side channel.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): the trusted computing base should be small enough to verify.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): memory safety is an invariant that unsafe languages leave to the programmer.
