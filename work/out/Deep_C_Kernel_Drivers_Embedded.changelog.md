# Deep C: Kernel, Drivers, Embedded: changelog

Source: `work/source/deep_c_kernel_drivers_embedded.json` (7 subdecks, average note ~950 chars)

- **Notes in → out:** 147 → 350
- **Deleted:** 0 whole notes (low-signal parts were trimmed inside splits, see below)
- **Merged:** 0 (no duplicate notes; overlapping facts were assigned to one card each, e.g. kernel UB flags appear only in the #61 cloze, addr2line/faddr2line only under the oops card #99)
- **Split:** 203 new cards from splitting. Every source note now gives 1–5 atomic cards: the first part keeps the guid and the others have `guid: null`
- **Analogies added:** 53 (~15%; source had none)
- **Subdecks (8, reorganised by concept):** 01 Undefined Behaviour & Integers, 02 Pointers, Qualifiers & Declarations, 03 Memory Layout & ABI, 04 Toolchain, Linking & Startup, 05 Concurrency & Interrupt Context, 06 Kernel C Idioms, 07 Linux Driver Programming, 08 Embedded & Bare Metal

## How the splitting worked (examples)
- #0 UB vs unspecified vs implementation-defined → one 3-deletion cloze.
- #6 `volatile` → three cards: what it guarantees, what it does not give, legitimate uses.
- #44/#45 kernel allocators and GFP flags → kmalloc vs vmalloc contrast, an allocator cloze, a GFP cloze, and a "GFP_KERNEL in atomic context" card.
- #109 (35-line platform-driver skeleton) → three cards: mapping registers and IRQ, the `of_device_id` match table, `platform_set_drvdata`. No code block is longer than 6 lines.
- #64 binary tools, #100 sanitizers, #102 attributes, #146 debug facilities → per-item clozes, plus "which tool for X" cards.
- #132 HardFault → stacked pc, fault status registers, common causes, IMPRECISERR.
- Long code examples (ring buffer, RCU, kref, ioctl, FreeRTOS ISR, bootloader jump) were reduced to the one or two lines that matter, or to a ≤6-line `<pre>` in `extra`.

## Trimmed or dropped content (signal filter)
- #101 kernel coding style: only checkpatch and the struct-typedef rule were kept. Tabs, line length and brace placement were dropped as low-signal.
- #145 MISRA: deck-meta wording ("hazards covered in this deck") removed; rule examples reduced to a 4-item cloze.
- #143 bootloader jump: the Cortex-M0 VTOR-less remapping detail was dropped (niche).
- #132 fault register hex addresses (0xE000ED28...) were dropped, keeping the register names.
- #94 printk level list (EMERG...DEBUG) was dropped, keeping the practical logging rules.

## Notes
- Contrast cards: kmalloc vs vmalloc, spinlock vs mutex, barrier() vs mb(), atomic_t vs refcount_t, coherent vs streaming DMA, MMIO vs port I/O, PRIMASK vs BASEPRI, reentrant vs thread-safe, hosted vs freestanding, arm-none-eabi vs aarch64-linux-gnu.
- Original tags and `source` labels kept. The deck was renamed to "Deep C: Kernel, Drivers, Embedded".

## Product-content review

- Reviewed card by card: no product-catered content found; nothing changed. Tool names present (Kubernetes, Argo CD, Cilium, MetalLB, FreeRTOS, CMSIS, k6, Playwright …) are open-source subjects or short examples.

## Abbreviations expanded

141 notes touched. First occurrence on each card written as "full name (ABBR)":
IRQ → interrupt request; DMA → direct memory access; UB → undefined behaviour; ISR → interrupt service routine; MCU → microcontroller unit; ABI → application binary interface; MMIO → memory-mapped I/O; IOMMU → input-output memory management unit; PM → power management; GPIO → general-purpose input/output; FPU → floating-point unit; RISC → reduced instruction set computer; I2C → Inter-Integrated Circuit; SPI → Serial Peripheral Interface; MMU → memory management unit; ELF → Executable and Linkable Format; DWT → data watchpoint and trace; KCSAN → Kernel Concurrency Sanitizer; RCU → read-copy-update; RTOS → real-time operating system; DRAM → dynamic random-access memory; SRAM → static random-access memory; TU → translation unit; VLA → variable-length array; PCI → Peripheral Component Interconnect; PCIe → Peripheral Component Interconnect Express; AAPCS → Arm Architecture Procedure Call Standard; GPL → GNU General Public License; UART → universal asynchronous receiver-transmitter; NMI → non-maskable interrupt; SPSC → single-producer single-consumer; ACPI → Advanced Configuration and Power Interface; SoC → system on chip; MSP → main stack pointer; PSP → process stack pointer; MPU → memory protection unit; SPL → secondary program loader; JTAG → Joint Test Action Group; SWD → serial wire debug; SWO → serial wire output; ITM → instrumentation trace macrocell; KASLR → kernel address space layout randomization; PAN → privileged access never; SMAP → supervisor mode access prevention; TOCTOU → time-of-check to time-of-use; RAID → redundant array of independent disks; SIMD → single instruction, multiple data; LMA → load memory address; VMA → virtual memory address; PC → program counter; EABI → Embedded Application Binary Interface; TSO → total store order; KASAN → Kernel Address Sanitizer; KMSAN → Kernel Memory Sanitizer; UBSAN → Undefined Behaviour Sanitizer; KFENCE → Kernel Electric Fence; DT → device tree; DTB → device tree blob; NAPI → New API; PHY → physical layer transceiver; IIO → industrial I/O; V4L2 → Video4Linux 2; BSP → board support package; UIO → userspace I/O; VFIO → virtual function I/O; NVIC → nested vectored interrupt controller; WFI → wait for interrupt; W1C → write-1-to-clear.
Left bare: ARM, NULL/NUL, EOF, GNU, GCC, ISO, IEC, CERT, MISRA, CVE ids, DWARF, AVR, CMSIS, DPDK/SPDK, RPMsg, RTT, ROM, FP, RX/TX, register names (PRIMASK, BASEPRI, CFSR...), part/size names (M4, STM32, Q15, ILP32).
