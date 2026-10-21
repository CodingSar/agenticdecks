# UDP and TCP

> **Layer:** [08 Networking](../README.md) › [Transport Layer](README.md)
> **Builds on:** [IP Addressing and Forwarding](../03-network-layer/ip-addressing-and-forwarding.md), [Layering and the End-to-End Principle](../01-principles/layering-and-the-end-to-end-principle.md), [IO Models](../../07-operating-systems/06-io-and-devices/io-models.md), [Finite State Machines](../../03-digital-logic/03-sequential-logic/finite-state-machines.md)
> **Enables:** [Reliable Delivery](reliable-delivery.md), [HTTP and the Web](../05-application-layer/http-and-the-web.md), [Naming and DNS](../05-application-layer/naming-and-dns.md), [Secure Protocols and TLS](../../11-security-and-cryptography/02-cryptography/secure-protocols-and-tls.md)

## Essence

The Internet offers two classic transport services on top of the Internet Protocol (IP). The User Datagram Protocol (UDP) adds only port numbers and a checksum: each message is an independent datagram that may be lost, duplicated or reordered. The Transmission Control Protocol (TCP) builds a connection between two processes and delivers a reliable, ordered, flow-controlled and congestion-controlled stream of bytes. Most applications use TCP because it hides the network's failures; applications that care more about timeliness than completeness, or that want to build their own reliability, use UDP. QUIC, now the transport under version 3 of the Hypertext Transfer Protocol (HTTP/3), is a modern reliable transport built on UDP in user space.

## Core tenets

1. **Ports turn host-to-host delivery into process-to-process delivery.** IP gets a packet to a host. A 16-bit port number in the transport header tells the Operating System (OS) which socket should receive it. A TCP connection is identified by the 4-tuple (source IP, source port, destination IP, destination port), so one server port (443) can hold millions of distinct connections.

2. **UDP is a thin veneer over IP.** Its 8-byte header holds source port, destination port, length and checksum. No connection setup, no acknowledgement, no retransmission, no rate control. That makes it right for small request/response exchanges (Domain Name System (DNS) lookups), for real-time media where late data is useless, and as a substrate for new protocols that cannot get through middleboxes any other way.

3. **TCP provides a byte stream, not messages.** The sender writes bytes; TCP chooses how to split them into segments; the receiver reads bytes, possibly in different chunk sizes. Applications must frame their own messages (length prefixes, delimiters). Treating one `send()` as one `recv()` is a classic bug.

4. **Connections start with a three-way handshake.** Client sends SYN (synchronise) with an initial sequence number; server replies SYN-ACK with its own; client sends an acknowledgement (ACK). This synchronises both sides' sequence numbers and confirms each can hear the other. It costs one Round-Trip Time (RTT) before data flows. Random initial sequence numbers stop old packets from earlier connections and blind attackers from being accepted as current data.

5. **Connection teardown is per direction and leaves a residue.** Each side sends FIN to close its half; the connection is fully closed after both. The side that closes first waits in TIME_WAIT for twice the maximum segment lifetime (often 60 seconds in total) so that late duplicates of old segments die out before the same 4-tuple can be reused. Busy servers that close connections can accumulate many TIME_WAIT entries.

6. **TCP is a state machine in each endpoint.** States such as LISTEN, SYN_SENT, ESTABLISHED, FIN_WAIT, CLOSE_WAIT and TIME_WAIT govern how each arriving segment is treated. The state lives only in the two endpoints; routers keep none, which is the end-to-end design. Middleboxes such as Network Address Translators (NATs) and firewalls do track it, which is why long-idle connections through them get silently dropped.

7. **In-order delivery causes head-of-line blocking.** If one segment is lost, all bytes after it wait in the receiver's buffer until it is retransmitted, even if they belong to logically independent requests. HTTP/2 multiplexes many streams over one TCP connection, so one loss stalls every stream.

8. **QUIC moves transport into user space over UDP.** QUIC provides multiple independent streams (loss in one does not block others), integrates Transport Layer Security (TLS) 1.3 so a new connection needs one RTT and a resumed one can send data immediately, encrypts most of its headers so middleboxes cannot ossify it, and identifies connections by an ID so they survive address changes. Running in user space lets applications deploy new versions without operating-system upgrades.

9. **Sockets are the interface.** The Berkeley sockets Application Programming Interface (API) (`socket`, `bind`, `listen`, `accept`, `connect`, `send`, `recv`) exposes both protocols as file descriptors, so the OS's Input/Output (I/O) models (blocking, non-blocking with `epoll`/`kqueue`, asynchronous) apply directly to network connections.

## Key concepts

| Term | Meaning |
|---|---|
| Port | 16-bit number identifying a socket on a host |
| Socket | OS endpoint object for sending and receiving; a file descriptor |
| 4-tuple | (src IP, src port, dst IP, dst port), identifying a TCP connection |
| Datagram | Independent message with no delivery guarantee (UDP) |
| Segment | Unit of TCP data with header |
| Three-way handshake | SYN, SYN-ACK, ACK: connection establishment |
| TIME_WAIT | Post-close state that absorbs delayed duplicates |
| Head-of-line blocking | Later data stalled behind a missing earlier piece |
| QUIC | Encrypted, multi-stream reliable transport over UDP |

## How it fits

- **Below:** relies on [IP](../03-network-layer/ip-addressing-and-forwarding.md) for host-to-host delivery. The kernel implements both protocols and exposes them through [I/O models](../../07-operating-systems/06-io-and-devices/io-models.md); TCP endpoints are [finite-state machines](../../03-digital-logic/03-sequential-logic/finite-state-machines.md).
- **Above:** [HTTP](../05-application-layer/http-and-the-web.md) runs over TCP or QUIC; [DNS](../05-application-layer/naming-and-dns.md) over UDP with TCP fallback; [TLS](../../11-security-and-cryptography/02-cryptography/secure-protocols-and-tls.md) secures TCP streams. Database clients and Remote Procedure Call (RPC) frameworks use TCP connections.
- **Siblings:** [reliable delivery](reliable-delivery.md) explains how TCP's guarantees are achieved; [congestion control](congestion-control.md) explains how it decides its rate.

## Common misconceptions

- **"UDP is unreliable, so it is worse."** UDP is minimal. Applications that need custom reliability (games, video, QUIC) build exactly what they need on it.
- **"TCP guarantees the data reached the application."** An ACK means the peer's kernel received the bytes, not that the application read or processed them; end-to-end application acknowledgement is still needed.
- **"TCP preserves message boundaries."** It delivers a stream; boundaries are the application's job.

## Go deeper

- J. Postel, *RFC 793: Transmission Control Protocol* (1981), now superseded by *RFC 9293* (2022): the specification.
- W. R. Stevens, *TCP/IP Illustrated, Volume 1* (1994; 2nd ed. 2011 with K. Fall): packet-level walk-through of real behaviour.
- A. Langley et al., *The QUIC Transport Protocol: Design and Internet-Scale Deployment* (SIGCOMM 2017): why QUIC was built and what it fixed.
