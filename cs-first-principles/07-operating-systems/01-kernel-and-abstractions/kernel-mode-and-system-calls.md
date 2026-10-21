# Kernel Mode and System Calls

> **Layer:** [07 Operating Systems](../README.md) › [Kernel and abstractions](README.md)
> **Builds on:** [The ISA contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md), [Buses and interrupts](../../04-computer-architecture/05-io-and-interconnect/buses-and-interrupts.md), [The role of the OS](the-role-of-the-os.md)
> **Enables:** [Processes](../02-process-management/processes.md), [I/O models](../06-io-and-devices/io-models.md), [Isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md), [Virtual machines and hypervisors](../07-virtualization/virtual-machines-and-hypervisors.md)

## Essence

The Central Processing Unit (CPU) has at least two privilege modes. In **kernel mode** it may execute every instruction and touch every address; in **user mode** privileged instructions fault and memory is limited to what the page tables allow. Control passes from user to kernel only through a **trap**: a system call, an exception (such as a page fault), or a hardware interrupt. Each trap switches to kernel mode and jumps to an address the kernel registered in advance, so user code can request services but cannot choose where in the kernel it lands. This "limited direct execution" lets programs run at full hardware speed while the kernel keeps control.

## Core tenets

1. **Limited direct execution: run user code natively, but keep a way back.** Interpreting every instruction would be safe but slow. Instead the OS lets the program run directly on the CPU in user mode, and relies on two hardware guarantees to regain control: sensitive actions trap, and a timer interrupt fires periodically regardless of what the program does. Without the timer, a program in an infinite loop would own the CPU forever.

2. **Entry points are fixed by the kernel, not chosen by the caller.** At boot the kernel fills a trap table (the Interrupt Descriptor Table on x86, the exception vector table on ARM, `stvec` on RISC-V) and sets the system-call entry register (`IA32_LSTAR` for x86-64 `syscall`). These registers are themselves privileged. So a user program can say "do system call 0 with these arguments" but can never jump into the middle of kernel code.

3. **A system call is a numbered request with arguments in registers.** On Linux x86-64, `rax` holds the call number (`read` is 0, `write` is 1), arguments go in `rdi`, `rsi`, `rdx`, `r10`, `r8`, `r9`, and `syscall` traps. The kernel saves user registers, switches to a per-thread kernel stack, dispatches through a table, and returns with `sysret`. Libraries like glibc wrap this so programmers call `read()` like an ordinary function.

   ```
   user:   mov rax, 1 ; rdi=fd ; rsi=buf ; rdx=len ; syscall
   kernel: save regs -> switch stack -> sys_call_table[rax](...) -> restore -> sysret
   ```

4. **Three kinds of trap share one mechanism.** *System calls* are deliberate and synchronous. *Exceptions* are synchronous but unintended (divide by zero, page fault, illegal instruction); the kernel may fix the cause and retry, or kill the process. *Interrupts* are asynchronous, raised by devices or timers, and unrelated to the running instruction. All three save state, raise privilege and vector to a kernel handler.

5. **The boundary has a real cost, so interfaces are designed to cross it rarely.** A bare system call costs on the order of 100 ns on modern x86 hardware, and more (often several hundred ns) with mitigations for Meltdown such as Kernel Page-Table Isolation (KPTI), which swaps page tables on every entry. The indirect cost is larger: polluted caches and Translation Lookaside Buffer (TLB). This is why `read` takes a buffer instead of one byte, why the virtual Dynamic Shared Object (vDSO) lets `gettimeofday` run without trapping, and why `io_uring` batches many requests per crossing.

6. **The kernel must never trust user pointers.** An argument like a buffer address could point into kernel memory or be unmapped. The kernel validates ranges and copies data with fault-tolerant routines (`copy_from_user`, `copy_to_user`), and hardware features such as Supervisor Mode Access Prevention (SMAP) make accidental direct access fault. Time-of-check-to-time-of-use bugs arise when the kernel reads user memory twice and another thread changes it in between.

7. **The system-call interface is the stable contract of the OS.** Linux has roughly 350–450 system calls depending on architecture, and its policy is never to break user space: binaries from decades ago still run. Windows NT keeps its raw system-call numbers private and changes them between releases; the stable contract there is the Win32 Application Programming Interface (API) in user-space Dynamic-Link Libraries (DLLs). Either way, the stable layer is what portable software targets.

## Key concepts

| Term | Meaning |
|---|---|
| Kernel mode / user mode | Privileged and unprivileged CPU states (rings 0 and 3 on x86; EL1 and EL0 on ARM) |
| Trap | Any synchronous or asynchronous transfer of control into the kernel |
| Trap table | Kernel-installed table mapping trap causes to handler addresses |
| Limited direct execution | Running user code natively with traps and timer interrupts as the leash |
| Context | The saved register state needed to resume interrupted code |
| Kernel stack | A per-thread stack the kernel uses while handling that thread's traps |
| vDSO | A kernel-provided page mapped into user space so some calls avoid trapping |
| KPTI | Kernel Page-Table Isolation: unmapping most kernel memory while in user mode, a Meltdown defence |

## How it fits

- **Below:** uses the privilege levels and trap mechanisms defined in [the ISA contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md) and the interrupt controller from [buses and interrupts](../../04-computer-architecture/05-io-and-interconnect/buses-and-interrupts.md).
- **Above:** processes, I/O, files and sockets are all reached through system calls. Sandboxes like seccomp ([isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md)) filter them; hypervisors add a still more privileged mode beneath.
- **Siblings:** [The role of the OS](the-role-of-the-os.md) explains why the boundary exists; [kernel architectures](kernel-architectures.md) decides how much code lives on the privileged side.

## Common misconceptions

- **"A system call is just a function call."** It changes privilege, stack and often page tables, and costs one to two orders of magnitude more than a function call.
- **"The kernel is a separate process."** In mainstream kernels, a system call runs in the context of the calling thread, on its kernel stack; the kernel is code that every process enters, not a peer it talks to.
- **"User mode protects memory by itself."** The mode only restricts instructions. Memory protection comes from page tables that the kernel sets per process; the two together form the boundary.

## Go deeper

- Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (2018), chapter "Limited Direct Execution": the clearest derivation of the mechanism.
- Livio Soares and Michael Stumm, "FlexSC: Flexible System Call Scheduling with Exception-Less System Calls" (OSDI 2010): measures the indirect cost of crossing the boundary.
- Intel, *Intel 64 and IA-32 Architectures Software Developer's Manual*, Volume 3: the authoritative description of x86 protection and traps.
