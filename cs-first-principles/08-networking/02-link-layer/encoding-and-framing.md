# Encoding and Framing

> **Layer:** [08 Networking](../README.md) › [Link Layer](README.md)
> **Builds on:** [Analog vs Digital](../../00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md), [Noise and Signal Integrity](../../00-engineering-foundations/02-electrical-circuits/noise-and-signal-integrity.md), [Channel Capacity and Error Correction](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md), [Abstract Algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md)
> **Enables:** [Media Access and Ethernet](media-access-and-ethernet.md), [Wireless Networks](wireless-networks.md), [Reliable Delivery](../04-transport-layer/reliable-delivery.md)

## Essence

A link is a physical channel that carries a continuous signal. To use it for data, the sender must map bits to signal shapes (encoding), the receiver must recover both the bits and the sender's clock from the signal, and both must agree where one message ends and the next begins (framing). Because noise flips bits, each frame also carries redundant bits computed from its contents, so the receiver can detect damage and discard the frame. These three steps convert an analog, noisy medium into a service that delivers whole, checked frames or nothing.

## Core tenets

1. **Bits must be encoded so the receiver can recover the clock.** The receiver samples the signal at the sender's bit rate, but the two clocks drift. If the line stays at one level for a long run of identical bits, the receiver loses track of bit boundaries. Line codes guarantee frequent transitions: Manchester encoding puts a transition in every bit (costing double the signal rate), while block codes such as 8b/10b and 64b/66b map data blocks to code words with bounded run lengths at 25% and ~3% overhead respectively.

2. **Encoding also controls DC balance and spectrum.** Many links are coupled through transformers or capacitors that cannot pass a constant voltage, so long-run average signal must be near zero. Code words are chosen to keep ones and zeros balanced. Encoding is therefore a physical-layer engineering choice, not just a data format.

3. **Higher rates pack more bits per symbol, at the cost of noise margin.** Modulation schemes send several bits per symbol by using more amplitude or phase levels (for example 4-level Pulse Amplitude Modulation (PAM-4) in modern Ethernet, 1024-point Quadrature Amplitude Modulation (1024-QAM) in Wi-Fi). More levels mean closer spacing, so the same noise causes more errors. Shannon's capacity C = B log2(1 + S/N) bounds what any scheme can achieve on a channel of bandwidth B and signal-to-noise ratio S/N.

4. **Framing finds message boundaries in a bit stream.** Options include a length field in the header, a special flag pattern marking start and end, or a reserved code word that cannot appear in data. Flags need *stuffing*: if the flag pattern 01111110 appears in data, the sender inserts a 0 after every five consecutive 1s (High-Level Data Link Control (HDLC) bit stuffing), and the receiver removes it. Ethernet uses a preamble and start delimiter plus physical-layer idle symbols.

5. **Error detection adds redundancy computed from the data.** A Cyclic Redundancy Check (CRC) treats the frame as a polynomial over GF(2), the field with two elements, and appends the remainder of dividing it by a fixed generator polynomial. The receiver recomputes and compares. Ethernet's CRC-32 detects all single-bit errors, all double-bit errors within a standard-size frame, and all burst errors up to 32 bits long. It is cheap in hardware: a shift register with a few exclusive-or (XOR) gates.

6. **Detection is cheaper than correction, so the choice depends on the error rate.** Detection plus retransmission costs few bits but a full round trip per error. Forward Error Correction (FEC) adds enough redundancy to repair errors without asking again, which wins when errors are frequent or round trips long (wireless, deep space, high-speed optical links). Modern fast Ethernet links use Reed-Solomon FEC because at 100 Gbit/s even rare errors are frequent in absolute terms.

7. **Checksums at different layers protect against different failures.** The link CRC protects one hop's wire. It does not protect against corruption inside a router's memory. That is why the Internet Protocol (IP), the Transmission Control Protocol (TCP) and applications add their own checks (weaker 16-bit one's-complement sums in IP and TCP, cryptographic hashes in applications), a direct instance of the end-to-end argument.

## Key concepts

| Term | Meaning |
|---|---|
| Line code | Mapping from bits to physical signal levels and transitions |
| Clock recovery | Receiver deriving bit timing from transitions in the incoming signal |
| Manchester encoding | Each bit is a mid-bit transition; self-clocking but doubles signal rate |
| 8b/10b, 64b/66b | Block codes mapping data blocks to longer code words for transitions and DC balance |
| Symbol | One signal element; may carry several bits |
| Frame | Link-layer unit: header, payload, trailer |
| Bit stuffing | Inserting bits so a delimiter pattern never appears in data |
| CRC | Polynomial-division checksum detecting bursts and common error patterns |
| FEC | Forward Error Correction: redundancy that lets the receiver repair errors |

## How it fits

- **Below:** takes signal levels from [analog vs digital](../../00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md), noise from [signal integrity](../../00-engineering-foundations/02-electrical-circuits/noise-and-signal-integrity.md), the capacity bound and coding theory from [channel capacity and error correction](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md), and polynomial arithmetic over finite fields from [abstract algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md).
- **Above:** gives every higher layer the illusion of whole, checked frames; [reliable delivery](../04-transport-layer/reliable-delivery.md) handles the frames that are dropped.
- **Siblings:** [media access](media-access-and-ethernet.md) decides *when* a station may send a frame; [wireless networks](wireless-networks.md) use far more FEC because radio is much noisier.

## Common misconceptions

- **"A CRC guarantees data integrity."** It detects random errors well, but an adversary can trivially forge a matching CRC. Integrity against attackers needs a cryptographic Message Authentication Code (MAC).
- **"Bit rate equals baud rate."** Baud is symbols per second; with multi-level modulation each symbol carries several bits.
- **"If the link checks frames, applications do not need checksums."** Corruption can occur in memory, buses and software between links.

## Go deeper

- W. W. Peterson, D. T. Brown, *Cyclic Codes for Error Detection* (1961): the original CRC paper.
- C. E. Shannon, *A Mathematical Theory of Communication* (1948): capacity and why coding works.
- L. L. Peterson, B. S. Davie, *Computer Networks: A Systems Approach* (many editions): clear chapters on encoding, framing and error detection.
