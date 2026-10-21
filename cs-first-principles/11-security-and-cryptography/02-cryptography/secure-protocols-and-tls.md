# Secure Protocols and TLS

> **Layer:** [11 Security and Cryptography](../README.md) › [Cryptography](README.md)
> **Builds on:** [Public-key cryptography](public-key-cryptography.md), [Symmetric encryption](symmetric-encryption.md), [Hash functions and message authentication codes](hash-functions-and-macs.md), [User Datagram Protocol and Transmission Control Protocol](../../08-networking/04-transport-layer/udp-and-tcp.md)
> **Enables:** [Web security](../04-network-and-application-security/web-security.md), [Hypertext Transfer Protocol and the web](../../08-networking/05-application-layer/http-and-the-web.md), [Network attacks and defenses](../04-network-and-application-security/network-attacks-and-defenses.md)

## Essence

A secure channel protocol combines primitives into a connection that gives **confidentiality**, **integrity** and **authentication** of at least one endpoint over a network the attacker controls. Transport Layer Security (TLS), the successor of SSL (Secure Sockets Layer), is the most important one: it secures the web (HTTPS, the Hypertext Transfer Protocol Secure), email transfer, and most application traffic. Its structure is a **handshake**, which authenticates the server (and optionally the client) with certificates and agrees on fresh keys with ephemeral Diffie–Hellman, followed by a **record layer**, which protects application data with authenticated encryption. The central lesson of protocol design is that composing correct primitives is where things go wrong: most practical breaks have come from negotiation, state machines, error messages and implementation bugs, not from broken ciphers.

## Core tenets

1. **The handshake must authenticate the key exchange, not just perform it.** Unauthenticated Diffie–Hellman is open to a man-in-the-middle. In TLS 1.3 the server signs a hash of the entire handshake transcript with the private key in its certificate, so the client knows the ephemeral key share came from the holder of that certificate. Both sides then send a Finished message, a MAC (message authentication code) over the transcript, so any tampering with earlier messages is detected.

2. **Certificates bind the server's name to its key, and the name check is essential.** The client verifies a certificate chain up to a certificate authority (CA) in its trust store, checks validity dates and revocation where possible, and checks that the certificate's name matches the host it intended to reach. Skipping the name check, a common bug in client code, makes any valid certificate for any domain acceptable to an attacker. Certificate Transparency logs make mis-issued certificates publicly detectable.

3. **TLS 1.3 is a clean break that removed whole classes of attack.** Standardised in 2018 (Request for Comments (RFC) 8446), it removed static RSA key transport (so all handshakes have forward secrecy), removed cipher block chaining (CBC) mode and RC4 cipher suites and custom Diffie–Hellman groups, kept only AEAD (authenticated encryption with associated data) ciphers, encrypted most of the handshake, and cut the full handshake to one round trip. Earlier versions accumulated attacks: BEAST and Lucky Thirteen on CBC, RC4 keystream biases, and downgrade attacks such as FREAK and Logjam that forced weak export-grade cryptography.

4. **Negotiation is an attack surface: prevent downgrades.** When peers negotiate versions and algorithms, an active attacker can tamper with the offers to push both sides to the weakest common option. Defences are to authenticate the whole negotiation transcript, to remove weak options entirely rather than merely disfavour them, and to add explicit downgrade signals (TLS 1.3 servers embed a sentinel value in their random nonce when negotiating an older version).

5. **Keys are derived, separated and updated.** From the Diffie–Hellman secret, TLS 1.3 uses HKDF (the key derivation function built on the hash-based message authentication code, HMAC) to derive separate keys for each direction and each phase (handshake, application data, resumption). Using one key for two purposes can let an attack on one purpose spill into the other. Records carry implicit sequence numbers in their nonces, which detects reordering, replay and deletion within a connection.

6. **0-RTT resumption trades replay protection for latency.** TLS 1.3 lets a returning client send data in its first flight using a key from a previous session (zero round-trip time, 0-RTT). That early data can be replayed by an attacker, so it must only carry requests that are safe to repeat (idempotent), or the server must deduplicate. It is a deliberate, documented weakening.

7. **Protocols are state machines, and their analysis should be formal.** Bugs such as accepting messages in the wrong order (the 2015 SMACK and SKIP-TLS attacks) or Apple's 2014 "goto fail" bug, which skipped signature verification, came from implementations, not the specification. TLS 1.3 was designed alongside formal analysis with tools such as Tamarin and ProVerif, and verified implementations exist. For new needs, use an established protocol and library, such as the Noise framework or the Signal protocol.

8. **TLS protects the channel, not the endpoints or the metadata.** It hides contents from the network, but a compromised server sees everything, and the server name (unless Encrypted Client Hello is used), addresses, timing and sizes remain visible. End-to-end encrypted messaging moves the trust boundary from the server to the users' devices, which is the [end-to-end argument](../../08-networking/01-principles/layering-and-the-end-to-end-principle.md) applied to secrecy.

## Key concepts

| Term | Meaning |
|---|---|
| TLS | Protocol giving an authenticated, confidential channel over a byte stream |
| Cipher suite | Negotiated set of algorithms for a connection |
| Certificate chain | Sequence of certificates from the server's up to a trusted root |
| Forward secrecy | Recorded sessions stay safe if long-term keys later leak |
| Downgrade attack | Forcing peers to negotiate a weaker option |
| HKDF | Standard function to derive multiple keys from one secret |
| 0-RTT | Sending early data before the handshake completes; replayable |

## How it fits

- **Below:** runs over the Transmission Control Protocol ([TCP](../../08-networking/04-transport-layer/udp-and-tcp.md)) or, in QUIC, over the User Datagram Protocol (UDP); uses [public-key](public-key-cryptography.md), [symmetric](symmetric-encryption.md) and [hash/MAC](hash-functions-and-macs.md) primitives; placed according to [layering and the end-to-end principle](../../08-networking/01-principles/layering-and-the-end-to-end-principle.md).
- **Above:** HTTPS for the [web](../../08-networking/05-application-layer/http-and-the-web.md) and its [security model](../04-network-and-application-security/web-security.md); client certificates and token binding for [authentication](../04-network-and-application-security/authentication.md); virtual private networks and secure Domain Name System (DNS) lookups as [network defences](../04-network-and-application-security/network-attacks-and-defenses.md).
- **Siblings:** combines all other files in [Cryptography](README.md); its proofs use the [foundations](foundations-of-modern-cryptography.md); its implementations must resist [side channels](../03-system-security/side-channels.md).

## Common misconceptions

- **"HTTPS means the site is trustworthy."** It means your connection is to whoever controls that domain name; phishing sites have valid certificates too.
- **"Encryption is enough; authentication is optional."** Encryption to an unauthenticated peer may be encryption to the attacker.
- **"Rolling our own protocol on top of the Advanced Encryption Standard (AES) is fine."** Most broken protocols used sound primitives; the composition is the hard part.

## Go deeper

- Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.3", RFC 8446 (2018).
- Ristić, *Bulletproof TLS and PKI* (2nd ed., 2022): deployment and the history of attacks.
- Boyd, Mathuria and Stebila, *Protocols for Authentication and Key Establishment* (2nd ed., 2020).
- Cremers et al., "A Comprehensive Symbolic Analysis of TLS 1.3", ACM CCS (2017).
