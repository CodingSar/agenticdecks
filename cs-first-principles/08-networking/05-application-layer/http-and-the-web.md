# HTTP and the Web

> **Layer:** [08 Networking](../README.md) › [Application Layer](README.md)
> **Builds on:** [UDP and TCP](../04-transport-layer/udp-and-tcp.md), [Naming and DNS](naming-and-dns.md), [Congestion Control](../04-transport-layer/congestion-control.md), [Character Encoding](../../03-digital-logic/01-number-representation/character-encoding.md)
> **Enables:** [Content Delivery and Caching](content-delivery-and-caching.md), [Web Security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md), [Software Architecture](../../12-software-engineering/01-design/software-architecture.md), [Scalability Patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md)

## Essence

The web is three inventions combined by Tim Berners-Lee in 1989–91: a way to name any resource anywhere (the Uniform Resource Locator, URL), a document format that links to other resources by name (the HyperText Markup Language, HTML), and a protocol to fetch a named resource (the Hypertext Transfer Protocol, HTTP). HTTP is a stateless request/response protocol: a client sends a method and a URL, a server returns a status code, headers and a body. Statelessness and a small, uniform set of methods with well-defined semantics are what let caches, proxies and load balancers sit transparently in the middle, and that is what let the web scale.

## Core tenets

1. **Everything is a resource named by a URL.** `https://example.com/users/42?fields=name` names a scheme (protocol), a host (resolved by DNS, the Domain Name System), a path and a query. Links are just URLs embedded in documents, so the web is a giant graph that anyone can extend without permission from anyone else.

2. **HTTP is request/response with a uniform interface.** A request is a method (GET, POST, PUT, DELETE, ...), a target, headers and an optional body. A response is a status code (200 OK, 301 Moved, 404 Not Found, 500 Server Error, ...), headers and a body. The same few methods apply to every resource, so generic software (browsers, crawlers, caches) can work with any site.

3. **Method semantics enable intermediaries.** GET is *safe* (no intended side effects) and *idempotent*; PUT and DELETE are idempotent; POST is neither. A cache may store and reuse a GET response; a proxy may retry an idempotent request after a dropped connection; neither may do so for POST. These guarantees are what make retries and caching correct.

4. **Statelessness pushes state to the edges.** Each request carries everything the server needs to process it. The server does not need to remember earlier requests, so any server in a pool can handle any request and failures do not lose conversation state. Where sessions are needed, state is carried explicitly: cookies the browser sends back, tokens in headers, or keys into a shared database.

5. **Headers carry the control plane.** Content-Type says how to interpret the body (with character encoding); Cache-Control and ETag govern caching and revalidation; Authorization carries credentials; Content-Encoding signals compression. Most of HTTP's evolution happened by adding headers, which old software can ignore.

6. **Performance is dominated by round trips.** Fetching a page needs a DNS lookup, a transport handshake, a TLS handshake and then the request, before any data. HTTP/1.1 added persistent connections so later requests skip setup. HTTP/2 (2015) multiplexes many requests on one connection with compressed headers. HTTP/3 (2022) runs over QUIC to remove head-of-line blocking across streams and merge transport and Transport Layer Security (TLS) handshakes.

7. **HTTPS is HTTP inside TLS, and it is now the default.** TLS authenticates the server by a certificate for its domain name and encrypts the exchange. Most browser traffic is HTTPS (well over 90% of page loads in major browsers, circa 2020s). Without it, any on-path party could read or alter pages.

8. **The browser turned HTTP into an application platform.** A page is HTML for structure, Cascading Style Sheets (CSS) for presentation and JavaScript for behaviour, plus dozens of sub-resources fetched in parallel. Browsers isolate pages from one another by *origin* (scheme, host, port). That same-origin policy is the foundation of web security.

9. **REST is HTTP's architecture made explicit.** Representational State Transfer (REST), as described by Fielding (2000), is the style the web follows: resources with identifiers, a uniform interface, stateless interactions, cacheable responses and layered intermediaries. Many service APIs (Application Programming Interfaces) adopt it; Remote Procedure Call (RPC) styles such as gRPC (on HTTP/2) trade uniformity for typed, efficient calls.

## Key concepts

| Term | Meaning |
|---|---|
| URL | Uniform Resource Locator: scheme, host, path, query identifying a resource |
| Method | Verb applied to a resource: GET, HEAD, POST, PUT, DELETE, PATCH, ... |
| Status code | Three-digit result class: 2xx success, 3xx redirect, 4xx client error, 5xx server error |
| Safe / idempotent | No side effects / repeating has the same effect as once |
| Stateless | Server needs no memory of past requests to process the current one |
| Cookie | Small state stored by the browser and sent with later requests to the same site |
| Persistent connection | Reusing one transport connection for many requests |
| Origin | (scheme, host, port), the browser's unit of isolation |
| REST | Architectural style based on resources, uniform interface and statelessness |

## How it fits

- **Below:** runs over [TCP or QUIC](../04-transport-layer/udp-and-tcp.md), starts with [DNS](naming-and-dns.md), and its speed for small objects is set by [congestion control](../04-transport-layer/congestion-control.md) slow start. Text protocols and bodies depend on [character encoding](../../03-digital-logic/01-number-representation/character-encoding.md) (UTF-8).
- **Above:** cache semantics enable [CDNs](content-delivery-and-caching.md); the browser's origin model and cookies are the battleground of [web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md); statelessness is the basis of horizontally scalable services in [scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md) and of service-oriented [software architecture](../../12-software-engineering/01-design/software-architecture.md).
- **Siblings:** [DNS](naming-and-dns.md) supplies the host part of every URL; [content delivery](content-delivery-and-caching.md) relies on HTTP's caching headers to keep copies correct.

## Common misconceptions

- **"The web and the Internet are the same thing."** The Internet is the packet network; the web is one application on it, alongside email, DNS, streaming and many others.
- **"Statelessness means web apps have no state."** It means state is not kept implicitly in the connection; it is carried explicitly or stored in a backing service.
- **"POST is for sending data, GET for receiving."** The real distinction is side effects: GET must be safe to repeat and cache; POST may change things.

## Go deeper

- T. Berners-Lee, *Information Management: A Proposal* (CERN, 1989): the original web proposal.
- R. T. Fielding, *Architectural Styles and the Design of Network-based Software Architectures* (PhD thesis, 2000): defines REST.
- I. Grigorik, *High Performance Browser Networking* (2013): how latency, TCP, TLS and HTTP versions shape real page loads.
