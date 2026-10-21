# Processes

> **Layer:** [07 Operating Systems](../README.md) › [Process management](README.md)
> **Builds on:** [Kernel mode and system calls](../01-kernel-and-abstractions/kernel-mode-and-system-calls.md), [Linking and loading](../../06-programming-languages/04-runtime-systems/linking-and-loading.md), [Datapath and control](../../04-computer-architecture/02-processor-microarchitecture/datapath-and-control.md)
> **Enables:** [Threads](threads.md), [Scheduling](scheduling.md), [Address spaces and paging](../04-memory-management/address-spaces-and-paging.md), [Containers](../07-virtualization/containers.md), [System models and failures](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md)

## Essence

A process is a program in execution: an isolated address space holding code, data, heap and stack, plus one or more threads of control, plus kernel-held resources such as open files, credentials and signal handlers. It is the Operating System's (OS's) unit of **isolation and resource ownership**: one process cannot read another's memory or use its file descriptors unless the kernel allows it. The kernel represents each process with a control block and multiplexes the Central Processing Unit (CPU) among processes by saving one's register state and restoring another's, a **context switch**. Because a paused process is just saved data, the kernel can run far more processes than there are cores.

## Core tenets

1. **A process is defined by its state, and all of that state can be saved and restored.** The CPU context (program counter, stack pointer, general registers, flags), the address space (a page-table root), and the kernel bookkeeping (open files, current directory, user ID, signal mask, parent) together are the process. The kernel keeps the bookkeeping in a Process Control Block (PCB) (`task_struct` in Linux, `EPROCESS` in Windows NT). Anything not in that state is not part of the process, which is why a process can be stopped, resumed, migrated or checkpointed.

2. **Context switching is how one core runs many processes.** On a timer interrupt, a blocking system call or a yield, the kernel saves the current registers into the PCB, picks the next process, loads its page-table root and registers, and returns to user mode. The direct cost is around a microsecond; the indirect cost (cold caches and, without address-space tags, a flushed Translation Lookaside Buffer (TLB)) is often larger. This cost is the floor on how finely the OS can time-slice.

3. **Processes move through a small state machine.** A process is *running* on a core, *ready* (runnable, waiting for a core), or *blocked* (waiting for an event such as I/O or a lock). Blocking happens when a process asks for something not yet available; waking happens when an interrupt or another process supplies it. After exit, it is a *zombie* until its parent collects the exit status.

   ```
   new -> ready <--schedule/preempt--> running -> exit -> zombie -> reaped
            ^                             |
            +--- event occurs --- blocked <+ (wait for I/O, lock, child)
   ```

4. **Unix separates creating a process from loading a program.** `fork()` creates a near-identical child; `exec()` replaces the caller's memory image with a new program; `wait()` lets the parent collect the child's result. The gap between `fork` and `exec` is where a shell sets up redirection and pipes by rearranging file descriptors, without any special system call. `fork` is cheap because pages are shared copy-on-write rather than copied. Windows NT instead offers `CreateProcess`, which builds the new process and loads the program in one call; Linux also offers `posix_spawn` and `clone` for finer control.

5. **Isolation comes from separate address spaces; sharing must be explicit.** Each process has its own page table, so the same virtual address in two processes refers to different physical memory. Processes communicate only through kernel-mediated channels: pipes, sockets, signals, files, or shared memory regions they both map deliberately. This default of isolation is why a crash in one browser tab's process does not take down the others, which is the design behind Chrome's multi-process architecture.

6. **Processes form a tree, and the kernel tracks parentage for cleanup and control.** Every process except the first has a parent; on Linux the first user process (`init`, usually systemd) adopts orphans and reaps them. Signals, process groups and sessions build job control on this tree (Ctrl-C sends `SIGINT` to the foreground group). Resource accounting and limits in modern kernels attach to groups of processes (control groups, or cgroups), the basis of containers.

7. **A process is the natural unit of failure.** When a process faults, the kernel kills it and reclaims its memory, files and locks held in the kernel; other processes are unaffected. Robust systems exploit this: Erlang supervisors, PostgreSQL's process-per-connection model and microservices treat a process as something that may crash and be restarted.

## Key concepts

| Term | Meaning |
|---|---|
| Process | A running program: address space, threads and kernel-held resources |
| PCB | Process Control Block, the kernel's record of a process's state |
| Context switch | Saving one execution context and restoring another |
| Address space | The set of virtual addresses a process can use and their mappings |
| `fork` / `exec` / `wait` | Unix calls to duplicate a process, replace its image, and collect a child |
| Copy-on-write | Sharing pages read-only until one side writes, then copying |
| Zombie | An exited process whose status has not yet been collected by its parent |
| Inter-Process Communication (IPC) | Kernel-mediated channels between processes (pipes, sockets, shared memory) |
| Signal | An asynchronous notification delivered to a process by the kernel |

## How it fits

- **Below:** a process is a [loaded program image](../../06-programming-languages/04-runtime-systems/linking-and-loading.md) run under the [protection boundary](../01-kernel-and-abstractions/kernel-mode-and-system-calls.md); its context is the register file of the [datapath](../../04-computer-architecture/02-processor-microarchitecture/datapath-and-control.md).
- **Above:** containers are process groups with private namespaces ([containers](../07-virtualization/containers.md)); distributed systems model nodes as processes that crash ([system models and failures](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md)); sandboxing builds on process isolation ([isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md)).
- **Siblings:** [threads](threads.md) split execution from ownership; [scheduling](scheduling.md) decides which ready process or thread runs.

## Common misconceptions

- **"A process and a program are the same thing."** A program is a passive file; a process is one execution of it. Ten shells running the same `/bin/bash` are ten processes sharing one program's code pages.
- **"`fork` copies all of memory, so it is expensive."** With copy-on-write it copies page tables, not pages; cost grows with address-space size, not with data written.
- **"A killed process always releases everything."** The kernel reclaims kernel-held resources, but external state (a half-written file, a lock in a database, a remote session) needs application-level recovery.

## Go deeper

- Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (2018), chapters "The Abstraction: The Process" and "Process API".
- Dennis M. Ritchie and Ken Thompson, "The UNIX Time-Sharing System" (1974): the origin of `fork`/`exec`.
- Andrew Baumann et al., "A fork() in the road" (HotOS 2019): a critique of `fork` in modern systems.
