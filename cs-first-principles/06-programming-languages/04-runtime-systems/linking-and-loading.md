# Linking and Loading

> **Layer:** [06 Programming Languages](../README.md) › [Runtime Systems](README.md)
> **Builds on:** [Code generation and register allocation](../03-compilers/code-generation-and-register-allocation.md), [Binding, scope and closures](../02-semantics-and-types/binding-scope-and-closures.md), [Virtual memory hardware](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md)
> **Enables:** [Processes](../../07-operating-systems/02-process-management/processes.md), [Build and continuous delivery](../../12-software-engineering/04-operations/build-and-continuous-delivery.md), [Isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md)

## Essence

Large programs are compiled one file at a time, so each object file refers to functions and variables it does not define and does not know the final addresses of its own code. Linking resolves these references: it matches every use of a symbol to exactly one definition, decides where each piece of code and data will sit, and patches every address-dependent instruction accordingly. Loading then maps the result into a process's memory and starts it. When linking is done at build time it is static; when part of it is deferred to load or run time it is dynamic, which lets many programs share one copy of a library and lets libraries be upgraded without recompiling programs. The single idea is **separate compilation with deferred binding of names to addresses**, made correct by relocation records that say exactly which bytes must be fixed up.

## Core tenets

1. **Separate compilation creates unresolved symbols on purpose.** Compiling `main.c`, which calls `printf`, produces an object file with an *undefined* reference to `printf` and a *defined* symbol `main`. Each object file has a symbol table (what it defines and needs) and sections (`.text` for code, `.data` for initialised data, `.bss` for zero-initialised data). This lets a million-line program rebuild only the files that changed.
2. **Symbol resolution enforces one definition per name.** The linker builds a global map from names to definitions. Two strong definitions of the same symbol are an error; an undefined symbol with no definition anywhere is an error ("undefined reference"). Static libraries (`.a` archives) are searched only for symbols still undefined, which is why the order of libraries on the command line can matter.
3. **Relocation patches addresses once layout is known.** The compiler cannot know where `printf` or even its own function will end up, so it emits placeholder bytes plus relocation entries ("put the address of symbol S plus offset A here, as a 32-bit value relative to the program counter"). After assigning every section an address, the linker walks the relocations and writes the real values.
4. **Position-independent code makes sharing possible.** A shared library loaded at different addresses in different processes must not contain absolute addresses in its code, or each process would need a patched private copy. Position-Independent Code (PIC) addresses its own data relative to the program counter and reaches external symbols through a Global Offset Table (GOT), a data table the loader fills in. The code pages stay identical and are shared by every process through [virtual memory](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md).
5. **Dynamic linking binds library calls late, often lazily.** Calls to shared-library functions go through stubs in the Procedure Linkage Table (PLT). On ELF (Executable and Linkable Format) systems the first call can jump into the dynamic linker, which looks up the symbol, writes its address into the GOT, and transfers control; later calls go straight through. This adds one indirect jump per call in exchange for shared memory, smaller binaries and library updates without relinking.

   ```
   call printf@plt  -->  PLT stub: jmp *GOT[printf]
                                   |-- first time: resolver finds printf, patches GOT
                                   '-- later: jumps directly to printf in libc.so
   ```

6. **The loader turns a file into a process.** The Operating System (OS) reads the executable's headers, creates an address space, maps code read-only and executable, maps data read-write, sets up the stack with arguments and environment, maps the dynamic linker if needed, and jumps to the entry point. Mapping is lazy: pages are read from disk only when first touched (demand paging), so starting a large program is fast.
7. **Address Space Layout Randomisation (ASLR) depends on relocatability.** Because code is position-independent, the loader can place the executable, libraries, heap and stack at random addresses each run. Attackers who exploit a [memory-safety bug](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md) then cannot hard-code addresses. The cost is a small amount of indirection, which is why PIC and position-independent executables became the default.
8. **Static versus dynamic linking is a real trade-off.** Static linking gives one self-contained file, no version conflicts and slightly faster calls, at the cost of larger binaries and having to rebuild to pick up a security fix. Dynamic linking shares memory and updates, at the cost of "dependency hell" when installed versions do not match. Containers and languages such as Go lean back towards static linking.

## Key concepts

| Term | Meaning |
|---|---|
| Object file | Compiler output: machine code and data with symbols and relocation entries |
| Symbol table | The list of names a module defines and the names it references |
| Relocation entry | A record telling the linker which bytes to patch with which symbol's address |
| Static linking | Copying all needed library code into the executable at build time |
| Shared library | A library loaded once and mapped into many processes (`.so`, `.dll`, `.dylib`) |
| Position-Independent Code (PIC) | Code that runs correctly at any load address |
| Global Offset Table (GOT) | A per-process table of addresses for external data and functions |
| Procedure Linkage Table (PLT) | Stubs that route calls to shared-library functions through the GOT |
| Loader | The OS component that maps an executable into memory and starts it |
| Address Space Layout Randomisation (ASLR) | Randomising load addresses to frustrate memory-corruption exploits |

## How it fits

- **Below:** Linkers consume the object files produced by [code generation](../03-compilers/code-generation-and-register-allocation.md) and rely on [instruction encoding](../../04-computer-architecture/01-instruction-set-architecture/instruction-encoding-and-addressing.md) to know how to patch addresses. Sharing and lazy loading depend on [virtual memory hardware](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md). Symbol resolution is [binding](../02-semantics-and-types/binding-scope-and-closures.md) at the scale of whole programs.
- **Above:** The loader is how the OS creates [processes](../../07-operating-systems/02-process-management/processes.md) and uses [address spaces and paging](../../07-operating-systems/04-memory-management/address-spaces-and-paging.md). Linking is a stage of every [build pipeline](../../12-software-engineering/04-operations/build-and-continuous-delivery.md). ASLR is a standard defence in [isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md).
- **Siblings:** [Interpreters](interpreters-and-virtual-machines.md) and [just-in-time compilers](jit-compilation.md) perform their own form of linking at run time, resolving class and method names lazily; the Java Virtual Machine loads and links classes on first use.

## Common misconceptions

- **"The compiler produces the executable."** The compiler produces object files; the linker produces the executable, and for dynamic executables the dynamic linker finishes the job at every start.
- **"Dynamic linking is just slower."** The per-call cost is an indirect jump; the benefit is shared physical memory across hundreds of processes and security patches without rebuilding.
- **"Link errors are compiler errors."** "Undefined reference" means every file compiled fine but some name has no definition in anything given to the linker.

## Go deeper

- John R. Levine, *Linkers and Loaders* (2000): the standard book on the subject.
- Randal E. Bryant and David R. O'Hallaron, *Computer Systems: A Programmer's Perspective* (3rd ed., 2015), chapter 7: linking explained from the programmer's side, with ELF examples.
- Ulrich Drepper, "How To Write Shared Libraries" (2011): the practical mechanics and costs of dynamic linking.
