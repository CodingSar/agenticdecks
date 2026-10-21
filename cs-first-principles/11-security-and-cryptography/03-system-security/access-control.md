# Access Control

> **Layer:** [11 Security and Cryptography](../README.md) › [System security](README.md)
> **Builds on:** [Security design principles](../01-security-principles/security-design-principles.md), [File system abstractions](../../07-operating-systems/05-storage-and-file-systems/file-system-abstractions.md), [Kernel mode and system calls](../../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md)
> **Enables:** [Isolation and sandboxing](isolation-and-sandboxing.md), [Authentication](../04-network-and-application-security/authentication.md), [Web security](../04-network-and-application-security/web-security.md)

## Essence

Access control decides whether a **subject** (a user, process or service) may perform an **operation** on an **object** (a file, record, device or Application Programming Interface (API) endpoint). Lampson's **access matrix** (1971) is the model: rows are subjects, columns are objects, and each cell lists the permitted rights. Real systems store this sparse matrix either by column, as **access control lists** (ACLs) attached to objects, or by row, as **capabilities** held by subjects. On top of the storage choice sit policy models: discretionary (owners decide), mandatory (a central policy decides), role-based and attribute-based. Access control only works if identity is authenticated first and if every access passes through a mechanism that cannot be bypassed.

## Core tenets

1. **Authentication, authorisation and audit are distinct steps.** Authentication establishes who the subject is; authorisation decides whether that subject may do this operation; audit records what happened for later accountability. Confusing the first two is a common bug: knowing that a request comes from a logged-in user says nothing about whether that user may read *this* record. Insecure direct object references (changing an identifier in a URL, a Uniform Resource Locator, to read another customer's data) are exactly this failure.

2. **ACLs and capabilities make different questions cheap.** With ACLs, "who can access this file?" is easy (read the list) and revocation is easy (edit it), but "what can this process access?" requires scanning everything. With capabilities, unforgeable tokens that both name an object and grant rights to it, delegation is easy (pass the token) and least privilege is natural (a process holds only what it was given), but revocation and review are harder. Unix file permissions are a compressed ACL; file descriptors are capabilities.

3. **Ambient authority causes the confused deputy problem.** If a program acts with all of its own privileges whenever it accesses something (ambient authority), an attacker can trick it into misusing them on the attacker's behalf. Hardy's original example (1988) was a compiler with permission to write a billing file, given an output file name that pointed at that billing file. Capabilities fix this by making the caller pass the authority along with the name; web cross-site request forgery is a modern confused deputy.

4. **Discretionary control cannot stop information flow; mandatory control can, at a cost.** In discretionary access control (DAC), an owner can grant access, so a Trojan horse running as a user can copy that user's secret files anywhere the user can write. Mandatory access control (MAC) enforces system-wide rules users cannot override. The Bell–LaPadula model (1973) protects confidentiality with "no read up, no write down" between clearance levels; Biba (1977) is its dual for integrity. Such models resist leaks by malicious code but are rigid, so they are used mainly in military systems and in confinement frameworks such as Security-Enhanced Linux (SELinux).

5. **Role-based and attribute-based control make policy manageable at scale.** Assigning permissions to roles (clerk, auditor, administrator) and roles to people (role-based access control, RBAC) keeps policy comprehensible when there are thousands of users and objects, and supports separation of duties (no one holds both "create payment" and "approve payment"). Attribute-based access control (ABAC) evaluates rules over attributes of subject, object and context (department, data classification, time, device posture), as used in cloud identity policies.

6. **Privilege escalation is the attacker's central goal.** Most attacks begin with low privilege (a web request, a user account) and seek more. Vertical escalation gains a higher role (user to administrator, process to kernel); horizontal escalation gains a peer's rights. Set-user-ID programs, kernel interfaces and services that run as root are escalation targets, which is why they must be small and carefully validated.

7. **Policies must be enforced at one non-bypassable point.** Checking permission in the user interface but not on the server, or in one code path but not another, leaves holes. The reference monitor principle requires a single mechanism that every access passes through: the kernel for files, the database for rows, an authorisation service or middleware for every API call. Deny-by-default rules ensure new resources start out protected.

## Key concepts

| Term | Meaning |
|---|---|
| Subject / object / right | Who acts / what is acted on / what action is permitted |
| Access matrix | Table of rights for every subject–object pair |
| ACL | Access control list: the rights stored with each object |
| Capability | Unforgeable token naming an object and conferring rights |
| Ambient authority | Acting with all of one's privileges implicitly |
| Confused deputy | Privileged program tricked into misusing its authority |
| DAC / MAC | Discretionary (owner-controlled) / mandatory (system-enforced) access control; not to be confused with a message authentication code |
| Bell–LaPadula | Confidentiality model: no read up, no write down |
| RBAC / ABAC | Permissions via roles / via rules over attributes |
| Privilege escalation | Gaining rights beyond those granted |

## How it fits

- **Below:** enforcement lives in the [kernel](../../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md) for [files](../../07-operating-systems/05-storage-and-file-systems/file-system-abstractions.md) and [processes](../../07-operating-systems/02-process-management/processes.md); policies follow [design principles](../01-security-principles/security-design-principles.md); lattice-based models use [partial orders](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md); databases implement row and column [permissions](../../09-data-management/01-data-models/relational-algebra-and-sql.md) through views and grants.
- **Above:** [cloud](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) identity and access management, [web](../04-network-and-application-security/web-security.md) authorisation, and [software architecture](../../12-software-engineering/01-design/software-architecture.md) of authorisation services; [privacy law](../../15-computing-in-context/law-privacy-and-policy.md) demands audit and purpose limits.
- **Siblings:** [isolation](isolation-and-sandboxing.md) makes the policy enforceable; [memory-safety bugs](memory-safety-vulnerabilities.md) let attackers bypass it from within; [authentication](../04-network-and-application-security/authentication.md) supplies the identities.

## Common misconceptions

- **"Logged in means allowed."** Authentication is not authorisation; every object access needs its own check.
- **"Hiding a button secures the action."** Client-side checks are advisory; the server must enforce the policy.
- **"Root and administrator accounts are necessary for daily work."** Routine use of full privileges turns every mistake and every compromised program into a full compromise.

## Go deeper

- Lampson, "Protection" (1971; *ACM Operating Systems Review*, 1974): the access matrix.
- Hardy, "The Confused Deputy (or why capabilities might have been invented)", *ACM Operating Systems Review* (1988).
- Sandhu et al., "Role-Based Access Control Models", *IEEE Computer* (1996).
- Anderson, *Security Engineering* (3rd ed., 2020): chapters on access control and multilevel security.
