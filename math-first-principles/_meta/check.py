#!/usr/bin/env python3
"""Validate the knowledge base against TAXONOMY.md.

Checks: every taxonomy path exists, every directory has a README.md, files have
the required sections, relative links resolve (including #anchors into Markdown
headings), no files exist outside the taxonomy, and "Builds on" links never point
upward or form a cycle. Warns when a file is outside its length limits or uses
LaTeX instead of Unicode notation. Prints word-count stats.

Usage: python3 -B _meta/check.py [path-prefix ...]   e.g.  python3 -B _meta/check.py 07 08
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEAF_SECTIONS = ["## Essence", "## Core tenets", "## Key concepts", "## How it fits",
                 "## Common misconceptions", "## Go deeper"]
README_SECTIONS = ["## What this area is about", "## How the children fit together"]
LAYER_SECTIONS = ["## Why this layer sits here"]
ROOT_FILES = {"README.md", "CROSS-CUTTING.md"}
LIMITS = {"leaf": (500, 1100), "parent": (400, 900), "layer": (600, 1200)}
# CROSS-CUTTING.md is written last; until it exists, links into it are checked against this list.
CROSS_CUTTING_ANCHORS = {
    "abstraction-and-generalisation", "structure-and-morphism", "equivalence-and-quotients",
    "invariants", "symmetry", "duality", "linearisation", "approximation-and-limits",
    "completeness-and-compactness", "local-to-global", "decomposition-and-classification",
    "induction-and-recursion", "existence-and-construction", "infinity-and-size",
    "randomness-and-averaging", "extremal-principles-and-optimisation",
    "dictionaries-between-fields", "impossibility-and-obstruction",
}
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
LATEX = re.compile(r"\$\$|\\(?:frac|mathbb|mathcal|mathrm|sum|int|prod|lim|sqrt|infty|alpha|beta"
                   r"|epsilon|varepsilon|delta|lambda|cdot|times|leq?|geq?|neq|to|mapsto|partial"
                   r"|nabla|in|subseteq|forall|exists)\b"
                   r"|\$(?=\S)[^$\n]*[\\^_{][^$\n]*(?<=\S)\$")


def taxonomy():
    text = (ROOT / "_meta" / "TAXONOMY.md").read_text()
    block = text.split("```")[1]
    stack, dirs, leaves = [], set(), set()
    for line in block.splitlines():
        if not line.strip():
            continue
        depth = (len(line) - len(line.lstrip())) // 2
        name = line.strip()
        stack = stack[:depth]
        if name.endswith("/"):
            stack.append(name.rstrip("/"))
            dirs.add("/".join(stack))
        else:
            leaves.add("/".join(stack + [name]))
    return dirs, leaves


def kind(rel):
    if not rel.endswith("README.md"):
        return "leaf"
    return "layer" if rel.count("/") == 1 else "parent"


def count_words(text):
    # Table pipes, arrows and bullets are not words.
    return sum(1 for t in text.split() if any(c.isalnum() for c in t))


def slug(heading):
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def anchors(path):
    return {slug(m.group(1)) for m in re.finditer(r"^#+\s+(.*)$", path.read_text(), re.M)}


def builds_on(p):
    """Resolved targets of the "Builds on" line of file p."""
    for line in p.read_text().splitlines():
        if line.startswith("> **Builds on:**"):
            for target in LINK.findall(line):
                path_part = target.partition("#")[0]
                if path_part and not re.match(r"^[a-z]+:", target):
                    yield (p.parent / path_part).resolve()


def main():
    prefixes = sys.argv[1:]
    dirs, leaves = taxonomy()
    expected = {f"{d}/README.md" for d in dirs} | leaves
    planned = {(ROOT / rel).resolve() for rel in expected | ROOT_FILES}
    cross_cutting = (ROOT / "CROSS-CUTTING.md").resolve()

    def selected(rel):
        return not prefixes or any(rel.startswith(p) for p in prefixes)

    errors, warnings, words = [], [], {}
    for rel in sorted(expected):
        if not selected(rel):
            continue
        p = ROOT / rel
        if not p.exists():
            errors.append(f"MISSING  {rel}")
            continue
        text = p.read_text()
        k = kind(rel)
        words[rel] = count_words(text)
        required = LEAF_SECTIONS if k == "leaf" else README_SECTIONS
        if k == "layer":
            required = required + LAYER_SECTIONS
        for sec in required:
            if sec not in text:
                errors.append(f"SECTION  {rel}: lacks '{sec}'")
        lo, hi = LIMITS[k]
        if not lo <= words[rel] <= hi:
            warnings.append(f"LENGTH   {rel}: {words[rel]} words ({k} limit {lo}-{hi})")
        latex = [i for i, line in enumerate(text.splitlines(), 1) if LATEX.search(line)]
        if latex:
            warnings.append(f"NOTATION {rel}: LaTeX on {len(latex)} line(s), first at line {latex[0]}")

    actual = {str(p.relative_to(ROOT)) for p in ROOT.rglob("*.md")
              if not str(p.relative_to(ROOT)).startswith("_meta")}
    for extra in sorted(actual - expected - ROOT_FILES):
        if selected(extra):
            errors.append(f"EXTRA    {extra}")

    anchor_cache = {}
    for rel in sorted(actual):
        if not selected(rel) and rel not in ROOT_FILES:
            continue
        p = ROOT / rel
        for target in LINK.findall(p.read_text()):
            if re.match(r"^[a-z]+:", target):
                continue
            path_part, _, frag = target.partition("#")
            dest = (p.parent / path_part).resolve() if path_part else p
            if not dest.exists():
                if dest == cross_cutting:
                    if frag and frag not in CROSS_CUTTING_ANCHORS:
                        errors.append(f"ANCHOR   {rel} -> {target}")
                elif dest not in planned:
                    errors.append(f"LINK     {rel} -> {target}")
                # A planned file that is not written yet is reported once, as MISSING.
                continue
            if frag and dest.suffix == ".md":
                if dest not in anchor_cache:
                    anchor_cache[dest] = anchors(dest)
                if frag not in anchor_cache[dest]:
                    errors.append(f"ANCHOR   {rel} -> {target}")

    # "Builds on" must never point to a higher layer: that would break bottom-up reading.
    graph = {}
    for rel in sorted(actual - ROOT_FILES):
        if not rel[:2].isdigit():
            continue
        p = ROOT / rel
        src_layer = int(rel[:2])
        for dest in builds_on(p):
            try:
                dest_rel = str(dest.relative_to(ROOT))
            except ValueError:
                continue  # another tree: the checker of that tree owns it
            graph.setdefault(rel, set()).add(dest_rel)
            if not selected(rel):
                continue
            dst_layer = int(dest_rel[:2]) if dest_rel[:2].isdigit() else -1
            # 00 and 01 are twin roots: logic's semantics is written in sets.
            if dst_layer > src_layer and not (src_layer == 0 and dst_layer == 1):
                errors.append(f"UPWARD   {rel} builds on {dest_rel}")

    # Nor may "Builds on" links form a cycle: then neither file can be read first.
    state, stack, cycles = {}, [], set()

    def visit(node):
        state[node] = "open"
        stack.append(node)
        for nxt in sorted(graph.get(node, ())):
            if state.get(nxt) == "open":
                cycle = stack[stack.index(nxt):]
                i = cycle.index(min(cycle))
                cycles.add(tuple(cycle[i:] + cycle[:i]))
            elif nxt not in state:
                visit(nxt)
        stack.pop()
        state[node] = "done"

    sys.setrecursionlimit(10000)
    for node in sorted(graph):
        if node not in state:
            visit(node)
    for cycle in sorted(cycles):
        if any(selected(n) for n in cycle):
            errors.append("CYCLE    " + " -> ".join(cycle + (cycle[0],)))

    for e in errors:
        print(e)
    for w in warnings:
        print(w)
    if words:
        leaf_w = [w for r, w in words.items() if kind(r) == "leaf"]
        print(f"\n{len(words)} files checked, {sum(words.values()):,} words"
              + (f"; leaves avg {sum(leaf_w)//len(leaf_w)}, min {min(leaf_w)}, max {max(leaf_w)}" if leaf_w else ""))
    print(f"{len(errors)} problem(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
