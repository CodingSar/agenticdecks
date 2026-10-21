# Link Layer

> **Layer:** [08 Networking](../README.md) › Link Layer
> **Children:** [Encoding and Framing](encoding-and-framing.md) · [Media Access and Ethernet](media-access-and-ethernet.md) · [Wireless Networks](wireless-networks.md)

## What this area is about

The link layer moves a frame of bits from one device to a directly connected neighbour: across a cable, through a switch, or over a radio channel. It is the first layer that deals in *discrete messages* rather than raw signals, and the last layer that knows anything about the physical medium. Everything above it sees "send this packet to the next hop" and nothing more.

Two problems unify the children. First, a receiver must find where frames begin and end in a continuous stream of symbols, and detect when noise has damaged them. Second, when several senders share one medium, they must take turns without a central scheduler. Wired Ethernet solved the second problem with collision detection and later removed it with switches; wireless networks cannot remove it, because radio is inherently shared and lossy.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Encoding and Framing](encoding-and-framing.md) | Turns bits into signals and back; marks frame boundaries; detects errors with checksums | Signals (00), coding theory (02) |
| [Media Access and Ethernet](media-access-and-ethernet.md) | Shares a medium among many senders; addresses frames within a local network; switching | Framing |
| [Wireless Networks](wireless-networks.md) | Applies media access to radio, where collisions cannot be detected and loss is common | Media access, framing |

Read in order. Framing gives a single link the ability to carry checked frames. Media access adds many stations and local addresses, which turns a link into a Local Area Network (LAN). Wireless then shows how every assumption of wired Ethernet (reliable medium, detectable collisions, everyone hears everyone) breaks on radio, and what replaces it.

```
 bits --> line code --> framed bits --> MAC frame [dst|src|type|payload|CRC]
          (encoding)     (framing)      (addressing + error detection)
```

## Connections to sibling areas

- **[Principles](../01-principles/README.md):** media access is statistical multiplexing on a single shared channel; per-hop retransmission in Wi-Fi is the "performance exception" allowed by the end-to-end argument.
- **[Network Layer](../03-network-layer/README.md):** Internet Protocol (IP) packets ride inside link frames; the Address Resolution Protocol maps IP addresses to link-layer addresses for the next hop. Switches forward within a LAN; routers forward between Local Area Networks (LANs).
- **[Transport Layer](../04-transport-layer/README.md):** link-layer loss on wireless confuses loss-based congestion control, which assumes loss means congestion.
- **[Application Layer](../05-application-layer/README.md):** largely isolated from link details, which is the point of layering; it sees only the resulting rate, latency and loss.

## Connections across layers

The link layer is where [signals](../../00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md), [noise](../../00-engineering-foundations/02-electrical-circuits/noise-and-signal-integrity.md) and [error-correcting codes](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md) become engineering. Network interface cards connect to the host through [DMA and devices](../../04-computer-architecture/05-io-and-interconnect/dma-and-devices.md) and [device drivers](../../07-operating-systems/06-io-and-devices/device-drivers-and-interrupt-handling.md). Above, link-layer broadcast domains are the scope of many [network attacks](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md) such as address spoofing.

## Cross-cutting threads

- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): line codes choose signal shapes for clock recovery and direct-current (DC) balance.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): Cyclic Redundancy Checks (CRCs) and forward error correction add bits to detect or fix errors.
- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): exponential backoff adapts retry rate to observed contention.
- [The end-to-end argument](../../CROSS-CUTTING.md#the-end-to-end-argument): link-level retransmission is an optimisation, not a guarantee.
