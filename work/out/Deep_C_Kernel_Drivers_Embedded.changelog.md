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
