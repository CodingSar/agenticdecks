# File System Abstractions

> **Layer:** [07 Operating Systems](../README.md) › [Storage and file systems](README.md)
> **Builds on:** [The role of the OS](../01-kernel-and-abstractions/the-role-of-the-os.md), [Kernel mode and system calls](../01-kernel-and-abstractions/kernel-mode-and-system-calls.md), [DRAM and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md)
> **Enables:** [File system implementation](file-system-implementation.md), [Storage layouts](../../09-data-management/02-storage-and-indexing/storage-layouts.md), [Naming and DNS](../../08-networking/05-application-layer/naming-and-dns.md)

## Essence

A file system gives programs two abstractions over raw storage. A **file** is a named, persistent, growable array of bytes, with no structure imposed by the Operating System (OS). A **directory** is a mapping from names to files (and other directories), which forms a hierarchical **namespace** addressed by paths like `/home/ana/notes.txt`. Programs reach files through system calls (`open`, `read`, `write`, `lseek`, `fsync`, `rename`, `unlink`) that return and use small integer **file descriptors**. The interface hides devices, block placement and caching, but its semantics, especially what is durable after a crash, are exactly what applications must understand to store data safely.

## Core tenets

1. **A file is just bytes; structure belongs to applications.** Unix deliberately made files untyped byte sequences, unlike earlier systems with record-oriented files. This lets one set of tools (`cat`, `grep`, `cp`) work on any file and lets each application define its own format. The cost is that every application must handle its own parsing, versioning and integrity.

2. **Names and files are separate objects.** In Unix file systems a file's identity is its *inode* (metadata plus block pointers); a directory entry merely maps a name to an inode number. So a file can have several names (hard links), and `unlink` removes a name, not the file: the file is freed only when its link count and open-descriptor count both reach zero. This is why a program can keep using a file someone else "deleted", and why log rotation works.

3. **File descriptors are capabilities handed out after a single check.** `open` resolves the path and checks permissions once, then returns an index into the process's descriptor table. Later `read` and `write` calls use the descriptor without rechecking the path. Descriptors are inherited across `fork` and can be passed between processes over Unix sockets, which makes them a simple form of capability. Because sockets, pipes, terminals and devices are also descriptors, the same `read`/`write` code works on all of them.

4. **Access control is attached to inodes.** Classic Unix permissions store an owner, a group, and read/write/execute bits for owner, group and others. Access Control Lists (ACLs) on Linux and Windows NT's richer security descriptors extend this. Directory permissions are separate: write permission on a directory lets you create or delete names in it, regardless of the files' own permissions.

5. **`write` returning means "accepted", not "durable".** By default `write` copies data into the page cache in memory and returns; the kernel writes it to the device later (Linux typically within about 30 seconds). Data that has not reached stable storage is lost on power failure. `fsync(fd)` forces the file's data and metadata to the device and waits; `fdatasync` skips non-essential metadata. Making a *new* file durable also requires `fsync` on its directory, so the name survives too.

6. **`rename` is the one atomic update primitive applications rely on.** POSIX (Portable Operating System Interface) requires `rename(old, new)` to replace `new` atomically: other processes see either the old file or the new one, never a mixture. The standard safe-update idiom is: write a temporary file, `fsync` it, `rename` it over the original, then `fsync` the directory. Skipping the first `fsync` has caused real data loss (the 2009 ext4 delayed-allocation episode, where renamed files appeared empty after crashes).

7. **The namespace can unify many file systems and non-files.** Mounting grafts one file system's tree onto a directory of another, so one path space covers disks, network shares (Network File System (NFS), Server Message Block (SMB)) and virtual file systems like `/proc` and `/sys` that expose kernel state as files. Plan 9 took "everything is a file" furthest. Per-process mount namespaces, the basis of containers, let different processes see different trees.

8. **Memory-mapped files make the file and memory abstractions meet.** `mmap` maps a file's pages into an address space, so loads and stores read and write the file through the page cache with no system calls per access. It suits random access to large files and is how executables and shared libraries are loaded. Durability still needs `msync`, and input/output (I/O) errors surface as signals rather than return codes.

## Key concepts

| Term | Meaning |
|---|---|
| File | Named, persistent, untyped sequence of bytes |
| Directory | A file mapping names to inode numbers |
| Inode | On-disk record of a file's metadata and data location, independent of its names |
| Hard link / symbolic link | Another directory entry for the same inode / a file containing a path |
| File descriptor | Per-process integer handle to an open file, socket, pipe or device |
| Mount | Attaching a file system's tree at a directory in the namespace |
| `fsync` | Block until a file's data and metadata are on stable storage |
| Atomic rename | Replacing a name's target so observers see only old or new |
| `mmap` | Mapping a file into a process's virtual address space |

## How it fits

- **Below:** implemented in the kernel behind [system calls](../01-kernel-and-abstractions/kernel-mode-and-system-calls.md), over [storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md); permissions are an instance of [access control](../../11-security-and-cryptography/03-system-security/access-control.md).
- **Above:** databases build tables and logs on files and `fsync` ([storage layouts](../../09-data-management/02-storage-and-indexing/storage-layouts.md), [recovery and logging](../../09-data-management/04-transactions/recovery-and-logging.md)); hierarchical naming reappears in the [Domain Name System (DNS)](../../08-networking/05-application-layer/naming-and-dns.md) and Uniform Resource Locator (URL) paths; [version control](../../12-software-engineering/02-process/version-control.md) is built on file trees.
- **Siblings:** [file system implementation](file-system-implementation.md) realizes these abstractions on blocks; [crash consistency and journaling](crash-consistency-and-journaling.md) explains what the durability promises cost.

## Common misconceptions

- **"After `write` returns, my data is safe."** Only after a successful `fsync` (and, for new files, a directory `fsync`) is it on stable storage, and only if the device honours flush commands.
- **"Deleting a file frees its space immediately."** Space is freed when the last name and the last open descriptor are gone.
- **"`close` flushes to disk."** `close` does not imply `fsync` on Linux; errors from delayed writeback may even surface only at `fsync`.

## Go deeper

- Dennis M. Ritchie and Ken Thompson, "The UNIX Time-Sharing System" (1974): the file and directory model.
- Thanumalayan Sankaranarayana Pillai et al., "All File Systems Are Not Created Equal: On the Complexity of Crafting Crash-Consistent Applications" (OSDI 2014): how applications misuse these semantics.
- Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (2018), "Files and Directories".
