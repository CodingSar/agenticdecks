# Channel Capacity and Error Correction

> **Layer:** [02 Theory of Computation](../README.md) › [Information Theory](README.md)
> **Builds on:** [Entropy and Information](entropy-and-information.md), [Abstract Algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md), [Noise and Signal Integrity](../../00-engineering-foundations/02-electrical-circuits/noise-and-signal-integrity.md)
> **Enables:** [Encoding and Framing](../../08-networking/02-link-layer/encoding-and-framing.md), [Wireless Networks](../../08-networking/02-link-layer/wireless-networks.md), [DRAM and Storage Devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md), [Reliable Delivery](../../08-networking/04-transport-layer/reliable-delivery.md)

## Essence

Every physical channel (a wire, a radio link, a flash cell, a disk sector) corrupts some of what passes through it. Shannon's channel coding theorem says that, despite this, reliable communication is possible: each channel has a capacity C, and at any rate below C there exist codes whose error probability can be made as small as you like, while above C it cannot. The price of reliability is not a slower rate approaching zero, as engineers before 1948 assumed, but only longer blocks and more computation. Error-correcting codes realise this by adding structured redundancy, so that valid codewords sit far apart and noise rarely pushes one into another's neighbourhood.

## Core tenets

1. **A channel is a conditional distribution p(y | x), and its capacity is C = max over p(x) of I(X; Y).** Capacity is the most mutual information per use that any input distribution can push through. For the binary symmetric channel that flips each bit with probability p, C = 1 − H(p) bits per use; at p = 0.11, C ≈ 0.5. For the binary erasure channel that loses bits with probability ε (and says so), C = 1 − ε.

2. **Shannon's channel coding theorem.** For every rate R < C and every ε > 0, for large enough block length n there is a code of 2^(nR) codewords whose maximum decoding error probability is below ε. Conversely, for R > C the error probability is bounded away from zero (and for many channels tends to 1). Below capacity, reliability is free in rate and paid for in delay and complexity.

3. **Why it works: random codes and sphere packing.** Each transmitted codeword, after noise, lands in a "noise ball" of about 2^(nH(Y|X)) typical outputs. The output space has about 2^(nH(Y)) typical sequences. So at most 2^(n(H(Y) − H(Y|X))) = 2^(nI(X;Y)) balls fit without overlapping. Shannon showed that codewords chosen *at random* already achieve this packing on average, so good codes must exist. The proof is non-constructive; finding efficient ones took about 50 years.

4. **The Shannon–Hartley formula gives capacity for band-limited noisy analogue links.** For bandwidth B hertz and signal-to-noise ratio S/N with additive white Gaussian noise, C = B log₂(1 + S/N) bits per second. Capacity grows linearly with bandwidth but only logarithmically with power, which is why wireless standards fight for spectrum and use many antennas (parallel spatial channels) rather than just shouting louder.

5. **Distance determines correction power.** A block code's minimum Hamming distance d is the smallest number of bit positions in which two codewords differ. It can detect up to d − 1 errors and correct up to ⌊(d − 1)/2⌋, because a received word within that radius of a codeword is closer to it than to any other. The Hamming(7,4) code has d = 3: 3 parity bits per 4 data bits correct any single flipped bit, and its parity checks point directly at the bad position.

6. **Algebra makes codes efficient to encode and decode.** Linear codes are subspaces of a vector space over a finite field: encoding is a matrix multiply and decoding starts by computing a syndrome. Reed–Solomon codes treat data as polynomial coefficients over GF(2⁸) and correct burst errors, which is why they protect CDs, QR codes and many storage systems. Low-density parity-check (LDPC) codes and turbo codes, decoded iteratively by belief propagation, operate within a fraction of a decibel of capacity and are used in Wi-Fi, 5G and SSDs; polar codes provably achieve capacity.

7. **Detection is cheaper than correction, so systems mix them.** A Cyclic Redundancy Check (CRC) uses polynomial division to detect bursts with a few bytes of overhead, but cannot fix them. When a return path exists, it is often cheaper to detect and retransmit (Automatic Repeat reQuest, ARQ) than to correct. When it does not (deep-space probes, storage read back years later, real-time streams), Forward Error Correction (FEC) is the only option.

8. **Feedback does not increase the capacity of a memoryless channel.** Shannon proved that letting the sender see what the receiver got leaves C unchanged; it only makes good codes simpler. Retransmission protocols therefore buy simplicity, not extra capacity.

## Key concepts

| Term | Meaning |
|---|---|
| Channel | Conditional distribution of output given input |
| Capacity C | Max mutual information per channel use (or per second) |
| Code rate | Data bits per transmitted bit, k/n for a block code |
| Hamming distance | Number of positions in which two words differ |
| Minimum distance d | Smallest distance between distinct codewords; sets correction power |
| Syndrome | Parity-check result that identifies the error pattern in a linear code |
| CRC | Polynomial-remainder checksum for burst error detection |
| FEC vs ARQ | Correct errors at the receiver vs ask for retransmission |
| SNR | Signal-to-noise ratio, usually in decibels |

## How it fits

- **Below:** Noise is a physical fact ([noise and signal integrity](../../00-engineering-foundations/02-electrical-circuits/noise-and-signal-integrity.md)); the digital abstraction itself is a crude error-correcting code that snaps voltages to 0 or 1 ([analog vs digital](../../00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md)). The algebra of codes is finite-field and linear algebra ([abstract algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md), [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md)).
- **Above:** Physical layers modulate and code bits near capacity ([encoding and framing](../../08-networking/02-link-layer/encoding-and-framing.md), [wireless](../../08-networking/02-link-layer/wireless-networks.md)). Error-Correcting Code (ECC) memory and SSD controllers apply these codes ([DRAM and storage](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md)). Transport protocols use checksums plus retransmission ([reliable delivery](../../08-networking/04-transport-layer/reliable-delivery.md)), and distributed storage uses erasure codes for durability ([replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md)).
- **Siblings:** [Source coding](source-coding-and-compression.md) strips redundancy, and channel coding adds it back in a controlled form. Both limits are expressed with the measures from [entropy and information](entropy-and-information.md).

## Common misconceptions

- **"More reliability always means a lower data rate."** Below capacity, error probability can be driven toward zero at a *fixed* rate by using longer codes. The real costs are latency and decoder complexity.
- **"Capacity is the raw signalling rate."** A 1 Gbaud link carrying noisy symbols has a capacity set by its noise, not its symbol rate; real throughput is lower still once protocol overhead is counted.
- **"A checksum makes data correct."** Detection codes only flag corruption, and with probability about 2^(−k) for a k-bit check they miss it. Something else must repair the data.

## Go deeper

- Claude E. Shannon, "A Mathematical Theory of Communication" (1948): Part II proves the noisy channel theorem.
- Richard W. Hamming, "Error Detecting and Error Correcting Codes" (1950): the first practical correcting codes.
- David J. C. MacKay, *Information Theory, Inference, and Learning Algorithms* (2003): capacity, LDPC codes and belief propagation explained intuitively.
- Shu Lin and Daniel J. Costello, *Error Control Coding* (2nd ed., 2004): engineering reference for real codes.
