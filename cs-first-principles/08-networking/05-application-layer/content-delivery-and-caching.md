# Content Delivery and Caching

> **Layer:** [08 Networking](../README.md) › [Application Layer](README.md)
> **Builds on:** [HTTP and the Web](http-and-the-web.md), [Naming and DNS](naming-and-dns.md), [Latency, Bandwidth and Queueing](../01-principles/latency-bandwidth-and-queueing.md), [Locality and Caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md), [Page Replacement](../../07-operating-systems/04-memory-management/page-replacement.md)
> **Enables:** [Replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md), [Cloud Computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md), [Network Attacks and Defenses](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md)

## Essence

Most Internet traffic is a small set of popular objects (videos, images, scripts, software updates) read by many people far from where they were published. Fetching each from the origin server would cross the same long, congested paths millions of times and pay a long round-trip time on every request. Content Delivery Networks (CDNs) place caches in hundreds of locations close to users, steer each user to a nearby cache, and serve repeated requests from there. It is the memory hierarchy applied to the planet: popularity follows a skewed distribution, so a modest cache near the reader absorbs most requests at a fraction of the latency and cost.

## Core tenets

1. **Distance, not bandwidth, limits most transfers.** A user in Sydney fetching from Virginia pays roughly 200 ms per round trip, and a small page needs several round trips (DNS, TCP, TLS, request). Moving a copy to a server 10 ms away cuts the load time far more than any bandwidth upgrade. CDNs exist because the speed of light cannot be optimised.

2. **Popularity is skewed, so caching works.** Requests for web objects roughly follow a Zipf-like distribution: a small fraction of objects receives most requests. Even a cache holding a small fraction of all content serves a large majority of requests ("hit ratio"). Long-tail objects miss and go back to the origin.

3. **Steering users to a nearby cache uses indirection.** Two main mechanisms: *DNS-based* steering, where the CDN's authoritative DNS server returns the address of a cache near the resolver that asked; and *anycast*, where many cache sites announce the same IP prefix via the Border Gateway Protocol (BGP) and routing delivers each user to the closest one. Both depend on naming and routing, not on the application.

4. **Correctness of cached copies is governed by HTTP semantics.** The Hypertext Transfer Protocol (HTTP) lets origins say how long a response stays fresh (Cache-Control: max-age), whether shared caches may store it (public vs private), and how to revalidate cheaply (ETag and If-None-Match: the cache asks "has it changed?" and gets a short 304 Not Modified if not). The origin, not the cache, decides the freshness policy.

5. **Invalidation is the hard part.** A cache cannot know that an origin changed an object before its freshness time expires. Options: short lifetimes (more origin load), explicit purge requests to every cache (fast but needs a control channel), or *versioned names* (`app.3f9a2c.js`): change the URL whenever content changes, so a name's content never changes and can be cached forever. Versioned names turn a consistency problem into a naming problem.

6. **Caches form hierarchies.** Browser cache, then a CDN edge, then a regional mid-tier, then an origin shield, then the origin. Each level filters requests for the next, the same structure as Level 1 (L1), Level 2 (L2) and Level 3 (L3) caches in a processor. Request collapsing at each level ensures that a sudden burst for a newly popular object sends only one request upstream.

7. **Eviction policy matters because capacity is finite.** Edge caches use Least Recently Used (LRU) variants and admission filters that avoid caching one-hit wonders, because a single scan of rarely requested objects can flush the popular ones. This is the page-replacement problem from operating systems, with object sizes that vary by six orders of magnitude.

8. **CDNs also terminate connections and absorb attacks.** By ending TCP and Transport Layer Security (TLS) at the edge, a CDN shortens handshake round trips even for uncacheable dynamic content, and then reuses warm long-lived connections to the origin. Its huge aggregate capacity and anycast distribution spread Distributed Denial-of-Service (DDoS) traffic across many sites, making CDNs a standard defence.

9. **Video and large files dominate the bytes.** Video streaming is the majority of Internet traffic by volume (circa 2020s). Streams are cut into small segments at several bitrates, each an ordinary cacheable HTTP object, and the player switches bitrate to match measured throughput (adaptive bitrate streaming). This reduces streaming to the same caching problem as static files.

## Key concepts

| Term | Meaning |
|---|---|
| CDN | Network of geographically distributed caches serving content on behalf of origins |
| Edge / PoP | Point of Presence: a CDN site close to users |
| Origin | The authoritative server that publishes the content |
| Hit ratio | Fraction of requests served from cache |
| Zipf distribution | Popularity of the k-th most popular item proportional to 1/k^s |
| Freshness lifetime | How long a cached response may be served without checking |
| Revalidation | Conditional request to check whether a cached copy is still current |
| Versioned URL | Content-addressed or versioned name so content never changes under a name |
| Anycast | Same prefix announced from many sites; routing picks the nearest |
| Adaptive bitrate | Player chooses segment quality based on measured throughput |

## How it fits

- **Below:** applies [locality and caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md) and [page replacement](../../07-operating-systems/04-memory-management/page-replacement.md) to a network; motivated by [propagation delay](../01-principles/latency-bandwidth-and-queueing.md); steered by [DNS](naming-and-dns.md) and anycast; kept correct by [HTTP](http-and-the-web.md) cache headers.
- **Above:** CDNs are read-mostly [replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md) with weak consistency; edge compute platforms extend [cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) to CDN sites; DDoS absorption is a key [network defence](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md).
- **Siblings:** [DNS](naming-and-dns.md) is itself a cached, replicated database and the first steering tool; [HTTP](http-and-the-web.md) defines the cache rules.

## Common misconceptions

- **"CDNs only help static content."** Terminating connections near users and reusing warm connections to the origin speeds up dynamic requests too.
- **"Cache invalidation can be made instant everywhere."** Purges take time to reach every edge, and browsers hold their own copies; versioned names are the only reliable instant change.
- **"Bigger caches always mean proportionally more hits."** Under Zipf popularity, hit ratio grows roughly logarithmically with cache size, so returns diminish.

## Go deeper

- L. Breslau, P. Cao, L. Fan, G. Phillips, S. Shenker, *Web Caching and Zipf-like Distributions: Evidence and Implications* (INFOCOM 1999): why caching works on the web.
- E. Nygren, R. K. Sitaraman, J. Sun, *The Akamai Network: A Platform for High-Performance Internet Applications* (2010): how a large CDN is built.
- D. Karger et al., *Consistent Hashing and Random Trees* (STOC 1997): the hashing scheme invented for distributing web caches.
