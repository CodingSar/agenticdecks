# Symmetric Encryption

> **Layer:** [11 Security and Cryptography](../README.md) › [Cryptography](README.md)
> **Builds on:** [Foundations of modern cryptography](foundations-of-modern-cryptography.md), [Abstract algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md), [Logic gates](../../03-digital-logic/02-combinational-logic/logic-gates.md)
> **Enables:** [Secure protocols and Transport Layer Security](secure-protocols-and-tls.md), [Public-key cryptography](public-key-cryptography.md), [File system implementation](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md)

## Essence

Symmetric encryption protects confidentiality when sender and receiver share a secret key. It is fast (gigabytes per second per core with hardware support) and does nearly all bulk encryption in practice; public-key methods are used mainly to agree on symmetric keys. The building blocks are **block ciphers**, which are keyed permutations on fixed-size blocks (the Advanced Encryption Standard (AES) uses 128-bit blocks), and **stream ciphers**, which generate a keystream to XOR (exclusive-or) with the message. A block cipher alone encrypts only one block, so a **mode of operation** turns it into an encryption scheme for long messages. The modern rule is simple: always use **authenticated encryption** such as AES-GCM or ChaCha20-Poly1305, which provides confidentiality and integrity together, and never reuse a nonce with the same key.

## Core tenets

1. **A block cipher should be a pseudorandom permutation.** For each key, AES is a permutation of the 2¹²⁸ possible blocks, and without the key it should be indistinguishable from a randomly chosen permutation. It is built from repeated rounds of substitution (non-linear S-boxes, for confusion) and linear mixing (for diffusion), so every output bit depends on every input and key bit in a complex way. AES (Rijndael, standardised in 2001) has 10, 12 or 14 rounds for 128-, 192- and 256-bit keys, and after more than two decades of analysis no practical attack on the full cipher is known.

2. **Key length sets the brute-force cost, and 128 bits is enough classically.** Trying all 2¹²⁸ keys is beyond any conceivable classical computation. Grover's quantum search algorithm gives only a quadratic speed-up, reducing a 128-bit key to about 2⁶⁴ quantum operations in theory, and those operations are far more expensive and harder to parallelise than classical ones; 256-bit keys are used where a wide margin against future quantum computers is wanted. The Data Encryption Standard (DES), with 56-bit keys, was brute-forced in 1998 and must not be used.

3. **Electronic Codebook (ECB) mode is insecure.** ECB encrypts each block independently with the same key, so identical plaintext blocks give identical ciphertext blocks, and patterns in the data show through (the well-known encrypted penguin image). It is deterministic and fails IND-CPA (indistinguishability under chosen-plaintext attack). It should never be used for more than one block of data.

4. **Secure modes randomise with an initialisation vector or nonce.** Cipher Block Chaining (CBC) XORs each plaintext block with the previous ciphertext block before encrypting, starting with a random, unpredictable initialisation vector (IV). Counter (CTR) mode encrypts successive counter values (nonce ‖ counter) and XORs the result with the plaintext, turning a block cipher into a stream cipher that is parallelisable and needs no padding. Both are IND-CPA secure when used correctly, but neither provides integrity.

5. **Unauthenticated encryption invites active attacks.** In CTR mode, flipping a ciphertext bit flips the corresponding plaintext bit, so an attacker can change "pay $100" to "pay $900" without knowing the key. In CBC mode with padding, a server that reveals whether decrypted padding was valid (a padding oracle) lets an attacker decrypt entire messages (Vaudenay, 2002); this broke real systems for a decade. The lesson: always authenticate ciphertexts, and verify the tag before acting on any decrypted data.

6. **Authenticated encryption is the correct default, and encrypt-then-MAC is the right composition.** Authenticated Encryption with Associated Data (AEAD) encrypts the message, authenticates both ciphertext and unencrypted associated data (such as headers), and returns either the plaintext or a failure. AES in Galois/Counter Mode (GCM) combines CTR encryption with a polynomial MAC (message authentication code) over a finite field; ChaCha20-Poly1305 combines the ChaCha20 stream cipher with the Poly1305 MAC and is fast in software without AES hardware instructions. When building from parts, the generically secure order is encrypt-then-MAC: compute the MAC over the ciphertext.

7. **Nonce reuse can be catastrophic.** In CTR-based modes, reusing a nonce with the same key reuses the keystream, so XORing two ciphertexts gives the XOR of the two plaintexts, often enough to recover both. In AES-GCM, nonce reuse also leaks the authentication key, allowing forgeries. With 96-bit random nonces, NIST (the US National Institute of Standards and Technology) limits a single GCM key to about 2³² random-nonce encryptions to keep collision probability negligible, a birthday-bound effect. Nonce-misuse-resistant modes such as AES-GCM-SIV degrade gracefully when nonces repeat.

8. **Ciphertext length and metadata still leak.** Encryption hides content, not size, timing or who talks to whom. Compressing before encrypting can leak secrets through ciphertext length when attacker-controlled and secret data are compressed together (the CRIME and BREACH attacks on web traffic). Padding and traffic shaping hide some of this, at a cost.

## Key concepts

| Term | Meaning |
|---|---|
| Block cipher | Keyed permutation on fixed-size blocks; ideally a PRP (pseudorandom permutation) |
| Stream cipher | Generates a keystream XORed with the plaintext |
| AES | Standard 128-bit block cipher with 128-, 192- or 256-bit keys |
| Mode of operation | Rule for using a block cipher on multi-block messages |
| ECB | Insecure mode encrypting each block independently |
| CBC | Chains blocks via XOR with previous ciphertext; needs an unpredictable IV |
| CTR | Encrypts counters to make a keystream |
| Nonce | Value that must never repeat under one key |
| AEAD | Encryption that also authenticates ciphertext and associated data |
| AES-GCM / ChaCha20-Poly1305 | The two dominant AEAD schemes |

## How it fits

- **Below:** AES's S-box is inversion in the finite (Galois) field GF(2⁸), and GCM's MAC is polynomial evaluation over GF(2¹²⁸), both from [abstract algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md); rounds are built from XOR and table lookups that map onto [logic gates](../../03-digital-logic/02-combinational-logic/logic-gates.md) and dedicated processor instructions; definitions come from [foundations](foundations-of-modern-cryptography.md).
- **Above:** [Transport Layer Security (TLS)](secure-protocols-and-tls.md) uses AEAD for every record; [file systems](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md) and disks use block-cipher modes for encryption at rest; [digital media](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md) protection uses it for content.
- **Siblings:** [hash functions and MACs](hash-functions-and-macs.md) supply integrity; [public-key cryptography](public-key-cryptography.md) agrees on the symmetric keys; [side channels](../03-system-security/side-channels.md) attack table-based AES implementations.

## Common misconceptions

- **"AES-256 is always better than AES-128."** Both are far beyond brute force; misuse (nonce reuse, no authentication) breaks systems, not key length.
- **"Encryption detects tampering."** Only authenticated encryption does; plain CBC or CTR accept modified ciphertexts silently.
- **"Using AES means the system is secure."** AES in ECB mode, or with a hard-coded key, is AES and is insecure.

## Go deeper

- Katz and Lindell, *Introduction to Modern Cryptography* (3rd ed., 2020): block ciphers, modes and their proofs.
- Daemen and Rijmen, *The Design of Rijndael* (2002): AES from its designers.
- Ferguson, Schneier and Kohno, *Cryptography Engineering* (2010): practical use and misuse.
- Rogaway, "Authenticated-Encryption with Associated-Data", ACM CCS (2002): the AEAD notion.
