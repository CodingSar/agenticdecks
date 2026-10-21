# Hash Tables

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Fundamental Data Structures](README.md)
> **Builds on:** [Arrays and Linked Lists](arrays-and-linked-lists.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Number Theory](../../01-mathematical-foundations/03-discrete-mathematics/number-theory.md), [Amortized Analysis](../01-foundations/amortized-analysis.md)
> **Enables:** [Join Algorithms](../../09-data-management/03-query-processing/join-algorithms.md), [Partitioning](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md), [Dynamic Programming](../03-design-paradigms/dynamic-programming.md), [Streaming and Online Algorithms](../07-advanced-topics/streaming-and-online-algorithms.md)

## Essence

A hash table stores key–value pairs so that lookup, insert and delete by exact key take O(1) expected time. It works by computing a *hash function* h(key) that maps any key to an index in an array of m slots, then storing the pair at (or near) that index. Because many keys can map to the same slot, the table needs a *collision resolution* strategy: chain colliding entries in a list, or probe for another free slot. The speed comes from turning a search into arithmetic; the price is that the table keeps no order, so "next larger key" or "all keys in a range" cost O(n).

## Core tenets

1. **Hashing converts search into address computation.** A search tree must compare against Θ(log n) keys. A hash table computes h(key), jumps to one slot, and compares against a constant number of keys on average. This bypasses the Ω(log n) comparison lower bound for search because it uses arithmetic on the key, not just comparisons.

2. **Collisions are unavoidable, so performance depends on the load factor.** By the pigeonhole principle, any function from a large key space to m slots sends many keys to the same slot. By the birthday paradox, with random hashing a collision is likely once about √m keys are inserted. Performance depends on the load factor α = n/m. With chaining and a good hash, an unsuccessful search inspects 1 + α entries on average. Keeping α bounded (say ≤ 1 for chaining, ≤ 0.5–0.9 for open addressing) by doubling the table and rehashing gives O(1) expected and amortized operations.

3. **Chaining and open addressing trade robustness for cache efficiency.** *Separate chaining* keeps a list per slot; it degrades gracefully as α grows. *Open addressing* stores entries in the array itself and probes a sequence of slots on collision. Linear probing (try h, h+1, h+2, …) is the most cache-friendly because probes hit consecutive memory, but it suffers from *clustering*: with load α, expected probes for an unsuccessful search grow like 1/(1 − α)². Fast modern tables (Google's SwissTable, Rust's hashbrown) use open addressing that checks 16 adjacent slots at once with vector instructions. Deletion in open addressing needs tombstones or backward-shift.

4. **No fixed hash function is good for every input.** For any deterministic h, an adversary who knows h can choose n keys that all collide, making every operation Θ(n). This is a real attack: in 2011, crafted Hypertext Transfer Protocol (HTTP) form parameters caused denial of service in many web frameworks by colliding in their hash tables. Defences are randomised (keyed) hash functions such as SipHash, chosen per process.

5. **Universal hashing gives provable expected bounds against any input.** A family H of hash functions is *universal* if for any two distinct keys, Pr[h(x) = h(y)] ≤ 1/m when h is drawn at random from H (Carter and Wegman, 1979). Example: h(x) = ((a·x + b) mod p) mod m for a prime p and random a, b. Then expected chain length is O(1 + α) for every input sequence, because the randomness is in the algorithm, not the data.

6. **Worst-case O(1) lookup is possible.** Cuckoo hashing uses two hash functions and guarantees each key is in one of two slots, so lookup inspects at most two locations; inserts may evict and relocate keys and occasionally rehash, giving O(1) expected amortized insert. Perfect hashing (Fredman, Komlós, Szemerédi, 1984) builds a collision-free table for a static set with O(n) space and O(1) worst-case lookup.

7. **Hash tables give up order, and with it range queries.** A good hash function scatters similar keys deliberately. So iterating in key order, finding the predecessor of a key, or answering "all keys between a and b" requires scanning everything. When you need order, use a [search tree](search-trees.md) or B-tree; databases offer both hash and tree indexes for this reason.

8. **Hashing generalises far beyond dictionaries.** The same idea, a fast function that spreads inputs uniformly, gives Bloom filters (approximate set membership with no false negatives), consistent hashing (assigning keys to k servers so adding one more moves only about 1/k of the keys), hash joins, deduplication, and sketches for counting in streams. Cryptographic hash functions add collision resistance against adversaries, which table hashes do not need.

## Key concepts

| Term | Meaning |
|---|---|
| Hash function | Function from keys to slot indices 0..m−1, ideally spreading keys uniformly |
| Load factor α | n / m: stored entries per slot |
| Separate chaining | Each slot holds a list of entries that hash there |
| Open addressing | Entries live in the array; collisions probe other slots |
| Linear probing | Probe consecutive slots; cache-friendly but prone to clustering |
| Universal hash family | Random choice of h makes any two keys collide with probability ≤ 1/m |
| Rehashing | Allocating a larger table and reinserting every key when α exceeds a threshold |
| Cuckoo hashing | Two candidate slots per key; insertion evicts occupants to their alternate slot |

## How it fits

- **Below:** modular arithmetic from [number theory](../../01-mathematical-foundations/03-discrete-mathematics/number-theory.md), collision probabilities from [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), and fast integer operations from the [processor](../../04-computer-architecture/02-processor-microarchitecture/datapath-and-control.md).
- **Above:** compiler [symbol tables](../../06-programming-languages/03-compilers/semantic-analysis.md), language dictionaries and objects, [hash joins](../../09-data-management/03-query-processing/join-algorithms.md), [consistent hashing](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md) in distributed stores, [content-addressed storage](../../12-software-engineering/02-process/version-control.md) in Git, and the [cryptographic hashes](../../11-security-and-cryptography/02-cryptography/hash-functions-and-macs.md) that share the name but not the requirements.
- **Siblings:** [search trees](search-trees.md) keep order at O(log n); hash tables drop order for O(1). Both are built on [arrays and linked lists](arrays-and-linked-lists.md).

## Common misconceptions

- **"Hash table operations are O(1)."** They are O(1) *expected* (and amortized, given resizing), assuming a good hash function. Worst case is Θ(n), and adversaries can force it against a fixed hash function.
- **"Any hash function will do."** Poor functions (for example, using the low bits of a pointer, which are always zero due to alignment) cluster keys and destroy performance.
- **"Table hashes and cryptographic hashes are the same thing."** Table hashes need speed and spread; cryptographic hashes need collision resistance against attackers and are much slower.

## Go deeper

- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (4th ed., 2022): hash tables chapter, including universal hashing and open addressing.
- J. Lawrence Carter and Mark N. Wegman, "Universal Classes of Hash Functions" (1979): the founding paper of universal hashing.
- Donald E. Knuth, *The Art of Computer Programming, Vol. 3: Sorting and Searching* (2nd ed., 1998): section 6.4, the classical analysis of probing.
- Rasmus Pagh and Flemming Friche Rodler, "Cuckoo Hashing" (2004): the worst-case O(1) lookup scheme.
