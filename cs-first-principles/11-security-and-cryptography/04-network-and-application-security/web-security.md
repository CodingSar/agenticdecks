# Web Security

> **Layer:** [11 Security and Cryptography](../README.md) › [Network and application security](README.md)
> **Builds on:** [Hypertext Transfer Protocol and the web](../../08-networking/05-application-layer/http-and-the-web.md), [Authentication](authentication.md), [Isolation and sandboxing](../03-system-security/isolation-and-sandboxing.md), [Lexing and parsing](../../06-programming-languages/03-compilers/lexing-and-parsing.md)
> **Enables:** [Software architecture](../../12-software-engineering/01-design/software-architecture.md), [Testing](../../12-software-engineering/03-quality/testing.md), [Law, privacy and policy](../../15-computing-in-context/law-privacy-and-policy.md)

## Essence

The web runs code from millions of mutually distrusting sources inside one program, the browser, which also holds the user's sessions for every site they use. Its security model rests on the **same-origin policy**: content from one origin (scheme, host and port, such as `https://bank.example:443`) may not read data belonging to another origin. Most web attacks either trick a site into treating attacker data as code (**injection**: SQL (Structured Query Language) injection on the server, cross-site scripting (XSS) in the browser) or trick the browser into using the user's authority for an attacker (**cross-site request forgery**, clickjacking). The defences follow one principle: keep data and code in separate channels, and make every state-changing request prove it came from the intended origin.

## Core tenets

1. **The same-origin policy is the browser's access-control rule.** Scripts may freely *send* requests to other origins (that is how links, images and forms work) but may not *read* responses from them unless the other origin opts in with Cross-Origin Resource Sharing (CORS) headers. Cookies, however, are attached to requests by destination, not by which page initiated them. That asymmetry, sending with credentials but not reading, is the root of request-forgery attacks.

2. **Injection happens when data is spliced into code.** Building a database query by concatenating user input, `"SELECT * FROM users WHERE name = '" + name + "'"`, lets input such as `' OR '1'='1` change the query's structure. The fix is not escaping by hand but separating channels: parameterised queries send the query structure and the data separately, so data can never be parsed as code. The same pattern applies to shell commands, file paths, Lightweight Directory Access Protocol (LDAP) filters and template engines.

3. **Cross-site scripting runs attacker code with the site's authority.** If a site inserts user-supplied text into a page without encoding it for its context, an attacker can inject a `<script>` that runs as the site's own code: it can read the page, act as the user and exfiltrate data. XSS can be stored (in a database and served to others), reflected (bounced from a crafted link) or DOM-based (introduced by client-side script manipulating the page's Document Object Model). Defences are contextual output encoding by default (modern template frameworks do this), avoiding raw HTML (HyperText Markup Language) insertion APIs (application programming interfaces), and a Content Security Policy (CSP) that restricts which scripts may run.

4. **Cross-site request forgery (CSRF) abuses ambient cookies.** A malicious page can submit a form to `bank.example/transfer`; the browser attaches the user's bank cookie, and the bank sees an authenticated request. This is a confused-deputy attack. Defences: `SameSite` cookies (which modern browsers default to `Lax`, withholding cookies on most cross-site subrequests), anti-forgery tokens that a cross-site page cannot read, and checking the `Origin` header on state-changing requests.

5. **Transport security must be enforced, not offered.** A site reachable over the plain Hypertext Transfer Protocol (HTTP) can be intercepted and rewritten before the user ever reaches the HTTPS (HTTP Secure) version (SSL stripping). HTTP Strict Transport Security (HSTS) tells browsers to use only HTTPS for a domain, and preload lists build that in. Cookies must carry the `Secure` flag so they never travel unencrypted. Mixed content, HTTPS pages loading HTTP scripts, would let a network attacker inject code.

6. **Server-side request forgery (SSRF) turns the server into a proxy.** If a server fetches a URL (Uniform Resource Locator) supplied by the user (to render a preview, import a file), an attacker can point it at internal addresses the attacker cannot reach directly, such as cloud metadata services that hand out credentials. Allow-lists of destinations and network-level blocking of internal ranges are the defences.

7. **Authorisation bugs are the most common serious flaws.** The OWASP (Open Worldwide Application Security Project) Top 10 list of 2021 ranks broken access control first: endpoints that check that a user is logged in but not that they own the record requested. These are logic errors no framework can fix automatically, which is why authorisation must be enforced centrally on the server and tested explicitly.

8. **Dependencies and the browser supply chain extend the trust boundary.** A typical web application includes hundreds of third-party packages and often loads scripts from other domains; any of them runs with the page's full authority. Subresource Integrity (a hash in the script tag), pinned and audited dependencies, and minimal third-party scripts limit what one compromised supplier can do.

## Key concepts

| Term | Meaning |
|---|---|
| Origin | Scheme, host and port triple that defines a security domain |
| Same-origin policy | Content may not read data from a different origin |
| CORS | Headers by which a server allows cross-origin reads |
| SQL injection | Input altering the structure of a database query |
| XSS | Attacker script executed in the context of a trusted site |
| CSRF | Cross-site request forgery: forged request carrying the victim's cookies |
| CSP | Header restricting which scripts and resources a page may load |
| HSTS | Header forcing browsers to use HTTPS for a domain |
| SameSite | Cookie attribute limiting when cookies attach to cross-site requests |
| SSRF | Server-side request forgery: making a server fetch attacker-chosen URLs |

## How it fits

- **Below:** built on [HTTP and the web](../../08-networking/05-application-layer/http-and-the-web.md), [Transport Layer Security (TLS)](../02-cryptography/secure-protocols-and-tls.md) for HTTPS, browser process [sandboxing](../03-system-security/isolation-and-sandboxing.md), [session authentication](authentication.md) and [access control](../03-system-security/access-control.md); injection is a [parsing](../../06-programming-languages/03-compilers/lexing-and-parsing.md) failure, and SQL injection targets [relational query languages](../../09-data-management/01-data-models/relational-algebra-and-sql.md).
- **Above:** shapes [software architecture](../../12-software-engineering/01-design/software-architecture.md) and [testing](../../12-software-engineering/03-quality/testing.md) practice; tracking and cookie rules are governed by [privacy law](../../15-computing-in-context/law-privacy-and-policy.md); prompt injection against [large language models](../../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md) is the same data-as-instructions failure in a new medium.
- **Siblings:** [authentication](authentication.md) creates the sessions attacked here; [network attacks](network-attacks-and-defenses.md) such as interception are why HTTPS and HSTS matter.

## Common misconceptions

- **"Input validation prevents injection."** Validation helps, but the reliable defence is keeping data out of the code channel (parameterised queries, contextual encoding).
- **"HTTPS makes a web application secure."** It protects the connection; XSS, CSRF and authorisation flaws work perfectly over HTTPS.
- **"CORS protects my server."** CORS relaxes the browser's read restriction; it does not stop requests from being sent, and non-browser clients ignore it.

## Go deeper

- Zalewski, *The Tangled Web* (2011): how browser security actually works, and why.
- OWASP Top 10 and OWASP Cheat Sheet Series (continuously updated): practical defences per vulnerability class.
- Barth, Jackson and Mitchell, "Robust Defenses for Cross-Site Request Forgery", ACM CCS (2008).
- Stuttard and Pinto, *The Web Application Hacker's Handbook* (2nd ed., 2011): attacks from the attacker's side.
