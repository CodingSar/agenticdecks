# Hash Functions and MACs

> **Layer:** [11 Security and Cryptography](../README.md) › [Cryptography](README.md)
> **Builds on:** [Foundations of modern cryptography](foundations-of-modern-cryptography.md), [Combinatorics](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md), [Hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md)
> **Enables:** [Public-key cryptography](public-key-cryptography.md), [Authentication](../04-network-and-application-security/authentication.md), [Version control](../../12-software-engineering/02-process/version-control.md), [Byzantine fault tolerance](../../10-distributed-and-parallel-computing/03-consensus-and-replication/byzantine-fault-tolerance.md)

## Essence

A cryptographic hash function maps input of any length to a short fixed-length digest (256 bits for SHA-256, a member of the Secure Hash Algorithm 2 (SHA-2) family) such that no one can feasibly find two inputs with the same digest, or an input matching a given digest. A digest is a fingerprint: if it matches, the data is the same. A message authentication code (MAC) adds a secret key: only parties holding the key can compute a valid tag, so a matching tag proves the message came from a key holder and was not altered. Hashes give integrity against accidental and adversarial change *if the digest itself is trusted*; MACs give integrity and origin authentication between parties sharing a key; [signatures](public-key-cryptography.md) give it publicly. Password storage needs a third tool, a deliberately slow hash.

## Core tenets

1. **Three security properties, of increasing strength.** *Preimage resistance*: given a digest h, finding any x with H(x) = h is infeasible. *Second-preimage resistance*: given x, finding a different x′ with the same digest is infeasible. *Collision resistance*: finding any pair x ≠ x′ with H(x) = H(x′) is infeasible. Collisions must exist, because inputs outnumber outputs; the claim is only that they cannot be found efficiently.

2. **The birthday bound halves the security level against collisions.** Among about 2^(n/2) random n-bit digests, two will probably match, just as 23 people probably include a shared birthday. So an n-bit hash gives at most n/2 bits of collision resistance: SHA-256 gives about 128 bits. This bound governs digest sizes, nonce sizes and tag sizes throughout cryptography.

3. **MD5 and SHA-1 are broken and must not be used for security.** Practical MD5 (Message Digest 5) collisions were found in 2004 and exploited in 2008 to forge a certificate authority certificate. A practical SHA-1 collision was published in 2017 (SHAttered), and chosen-prefix SHA-1 collisions became practical by 2020. Current choices are SHA-256 or SHA-512 (SHA-2), SHA-3 (Keccak, standardised in 2015) and BLAKE2/BLAKE3.

4. **Merkle–Damgård hashes allow length extension; HMAC fixes it.** MD5, SHA-1 and SHA-2 process input block by block, chaining an internal state, and output that state. Given H(secret ‖ m) and the length, an attacker can compute H(secret ‖ m ‖ padding ‖ m′) without knowing the secret. So the naive MAC H(key ‖ message) is insecure with these functions. HMAC (Hash-based Message Authentication Code; Bellare, Canetti and Krawczyk, 1996) computes H((K ⊕ opad) ‖ H((K ⊕ ipad) ‖ m)), and is a secure pseudorandom function if the hash's compression function is. SHA-3's sponge construction is not vulnerable to length extension.

5. **MACs need careful verification.** A MAC is secure if it is unforgeable under chosen-message attack: seeing tags on chosen messages does not help forge a tag on a new one. Implementations must compare tags in constant time, since a byte-by-byte comparison that exits early reveals through timing how many leading bytes are correct. A MAC also does not prevent replay: a valid message can be resent, so protocols add sequence numbers or timestamps.

6. **Hash structures turn one trusted digest into trust in a large dataset.** A Merkle tree hashes data blocks, then hashes pairs of hashes up to a single root; proving that one block belongs to the set needs only a logarithmic number of sibling hashes. Git commit identifiers, certificate transparency logs, blockchains and content-addressed storage all rely on this: if the root is authentic, every block it covers can be verified. The root must still come from a trusted source.

7. **Passwords need slow, salted, memory-hard hashing.** Passwords have little entropy, so an attacker who steals a database of fast hashes can try billions of guesses per second on graphics processors. Defences: a unique random *salt* per password (defeats precomputed tables and makes identical passwords hash differently), and a deliberately expensive function such as Argon2 (winner of the 2015 Password Hashing Competition), scrypt, or bcrypt, tuned to take tens to hundreds of milliseconds. Memory-hard functions also blunt specialised hardware.

8. **Non-cryptographic hashes are not substitutes.** Hash functions for [hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) and checksums such as Cyclic Redundancy Checks (CRCs) are designed for speed and spreading, not adversarial resistance. CRCs detect random errors but an attacker can trivially craft data with any chosen CRC; even hash-table hashes need keyed variants (SipHash) when attackers choose keys, to prevent collision-based denial of service.

## Key concepts

| Term | Meaning |
|---|---|
| Digest | Fixed-length output of a hash function |
| Preimage resistance | Cannot find an input for a given digest |
| Collision resistance | Cannot find any two inputs with the same digest |
| Birthday bound | Collisions appear after about 2^(n/2) n-bit outputs |
| SHA-2 / SHA-3 | Current standard hash families |
| Length extension | Computing H(s ‖ m ‖ pad ‖ m′) from H(s ‖ m) without s |
| MAC | Keyed tag proving integrity and origin to key holders |
| HMAC | Standard MAC built from a hash with two nested keyed calls |
| Merkle tree | Tree of hashes allowing logarithmic-size membership proofs |
| Salt | Per-password random value mixed into the hash |
| Argon2 / bcrypt / scrypt | Slow, tunable password-hashing functions |

## How it fits

- **Below:** the birthday bound is [combinatorics](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md) and [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md); hashing for lookup is in [hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md); error-detecting codes are in [channel coding](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md); security notions come from [foundations](foundations-of-modern-cryptography.md).
- **Above:** signatures hash the message first ([public-key cryptography](public-key-cryptography.md)); [Transport Layer Security (TLS)](secure-protocols-and-tls.md) uses HMAC-based key derivation; [authentication](../04-network-and-application-security/authentication.md) stores password hashes; [version control](../../12-software-engineering/02-process/version-control.md) names objects by hash; [Byzantine protocols](../../10-distributed-and-parallel-computing/03-consensus-and-replication/byzantine-fault-tolerance.md) authenticate messages with MACs.
- **Siblings:** [symmetric encryption](symmetric-encryption.md) needs a MAC (or authenticated encryption) for integrity; [public-key](public-key-cryptography.md) signatures are the public counterpart of MACs.

## Common misconceptions

- **"Hashing a password is enough."** A fast unsalted hash such as SHA-256 is cracked quickly by brute force; use a salted, slow password hash.
- **"Hashing is encryption."** Hashing is one-way and keyless; nothing is decrypted.
- **"H(key ‖ message) is a fine MAC."** With Merkle–Damgård hashes it is vulnerable to length extension; use HMAC or a dedicated MAC.

## Go deeper

- Katz and Lindell, *Introduction to Modern Cryptography* (3rd ed., 2020): hash and MAC definitions and constructions.
- Bellare, Canetti and Krawczyk, "Keying Hash Functions for Message Authentication", CRYPTO (1996): HMAC.
- Stevens et al., "The First Collision for Full SHA-1", CRYPTO (2017).
- Merkle, "A Digital Signature Based on a Conventional Encryption Function", CRYPTO (1987): Merkle trees.
