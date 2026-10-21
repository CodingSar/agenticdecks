# Wireless Networks

> **Layer:** [08 Networking](../README.md) › [Link Layer](README.md)
> **Builds on:** [Media Access and Ethernet](media-access-and-ethernet.md), [Encoding and Framing](encoding-and-framing.md), [Electromagnetism and Charge](../../00-engineering-foundations/01-physics-of-computation/electromagnetism-and-charge.md), [Channel Capacity and Error Correction](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md)
> **Enables:** [Congestion Control](../04-transport-layer/congestion-control.md), [Network Attacks and Defenses](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md)

## Essence

Radio is a shared broadcast medium whose quality changes from moment to moment. Signal strength falls steeply with distance, reflects off walls, and fades as people move. A station cannot hear collisions at the receiver while it is transmitting, and two stations that both reach an access point may not hear each other. Wireless link layers therefore avoid collisions instead of detecting them, acknowledge every frame, retransmit locally, and constantly adapt their bit rate to the channel. Mobility adds a second problem: the same device keeps changing where it attaches to the network.

## Core tenets

1. **Signal strength decays fast and varies unpredictably.** In free space, received power falls with the square of distance; indoors, often with the third or fourth power. Multipath reflections arrive with different delays and interfere, causing deep fades that change over centimetres and milliseconds. Bit error rates on radio are many orders of magnitude worse than on copper or fibre.

2. **A transmitter cannot detect collisions.** Its own signal at the antenna is billions of times stronger than a distant station's, so it cannot listen while it sends. And what matters is interference at the *receiver*, which the sender cannot observe. So wireless uses Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA): sense the channel, wait a random backoff even when idle, send the whole frame, and treat a missing acknowledgement as a collision.

3. **Hidden and exposed terminals break carrier sense.** If A and C are both in range of access point B but not of each other, they each sense an idle channel and collide at B (hidden terminal). Conversely, a station may defer unnecessarily because it hears a transmission that would not interfere with its own receiver (exposed terminal). Wi-Fi offers optional Request-to-Send/Clear-to-Send (RTS/CTS) handshakes, where B's CTS reserves the channel for everyone who can hear B.

4. **Every frame is acknowledged and retransmitted at the link layer.** Because loss is common, waiting for end-to-end recovery would be far too slow and would mislead transport protocols. Wi-Fi retransmits a frame several times before giving up. This is the end-to-end argument's permitted performance optimisation, and it is essential for wireless to be usable.

5. **Rate adaptation trades speed for robustness.** Stations pick a modulation and coding scheme per frame: dense modulation with light coding when the signal is strong, sparse modulation with heavy Forward Error Correction (FEC) when weak. Shannon's capacity C = B log2(1 + S/N) makes the trade-off precise. A distant slow station also occupies the shared air longer per bit, reducing throughput for everyone nearby (the "performance anomaly" of 802.11).

6. **Spatial reuse and multiple antennas multiply capacity.** Because signals fade with distance, the same frequency can be reused in cells far apart; this is the core idea of cellular networks. Multiple-Input Multiple-Output (MIMO) antennas exploit multipath to send several independent streams at once on the same frequency, and Orthogonal Frequency-Division Multiplexing (OFDM) splits a channel into many narrow subcarriers that each see flat fading.

7. **Loss on wireless is not congestion.** Transmission Control Protocol (TCP) congestion control traditionally reads packet loss as a sign of queue overflow and halves its rate. On a radio link that drops frames because of interference, this is the wrong reaction. Link-layer retransmission hides most radio loss, and newer congestion controllers rely more on delay and rate measurements.

8. **Mobility separates identity from location.** When a phone moves between cells or access points, its point of attachment changes but open connections should survive. Within one Wi-Fi network the access points cooperate to hand over; cellular networks keep a stable Internet Protocol (IP) address via tunnels to an anchor gateway. Across networks the address changes, which is one reason QUIC identifies connections by an ID rather than by addresses and ports.

## Key concepts

| Term | Meaning |
|---|---|
| Path loss | Decline of received power with distance |
| Multipath fading | Constructive and destructive interference of reflected copies |
| SNR | Signal-to-Noise Ratio: received signal power over noise power, sets achievable rate |
| CSMA/CA | Carrier sense with random backoff and acknowledgements; Wi-Fi's Medium Access Control (MAC) |
| Hidden terminal | Two senders that cannot hear each other collide at a common receiver |
| RTS/CTS | Short reservation handshake to mitigate hidden terminals |
| Rate adaptation | Choosing modulation and coding to match channel quality |
| MIMO | Multiple antennas sending parallel spatial streams |
| OFDM | Splitting a channel into many orthogonal narrowband subcarriers |
| Handover | Moving an active connection between access points or cells |

## How it fits

- **Below:** radio propagation is [electromagnetism](../../00-engineering-foundations/01-physics-of-computation/electromagnetism-and-charge.md); rate limits and coding are [channel capacity and error correction](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md); framing and Cyclic Redundancy Checks (CRCs) come from [encoding and framing](encoding-and-framing.md).
- **Above:** wireless loss and variable delay challenge [congestion control](../04-transport-layer/congestion-control.md). Because anyone in range can receive frames, wireless needs link-layer encryption (Wi-Fi Protected Access, WPA2/WPA3) and is a prime venue for [network attacks](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md).
- **Siblings:** [media access and Ethernet](media-access-and-ethernet.md) solved contention by switching; radio cannot be switched into private wires, so contention remains.

## Common misconceptions

- **"Wi-Fi is just wireless Ethernet."** It shares the address and frame structure, but its MAC (avoidance, acknowledgements, rate adaptation) is fundamentally different.
- **"Advertised Wi-Fi rate is what you get."** Headline rates assume ideal signal, widest channels and maximum antennas; contention, overhead and retries typically halve real throughput or worse.
- **"More transmit power fixes coverage."** Raising one side's power does not help the weaker return direction and increases interference for neighbours.

## Go deeper

- D. Tse, P. Viswanath, *Fundamentals of Wireless Communication* (2005): fading, diversity and MIMO from first principles.
- V. Bharghavan, A. Demers, S. Shenker, L. Zhang, *MACAW: A Media Access Protocol for Wireless LANs* (1994): hidden terminals and RTS/CTS.
- M. Heusse et al., *Performance Anomaly of 802.11b* (2003): why one slow station slows everyone.
