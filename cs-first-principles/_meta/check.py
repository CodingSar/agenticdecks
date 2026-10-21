#!/usr/bin/env python3
"""Validate the knowledge base against TAXONOMY.md.

Checks: every taxonomy path exists, every directory has a README.md, leaves have
the required sections, relative links resolve (including #anchors into Markdown
headings), no files exist outside the taxonomy. Prints word-count stats.

Usage: python3 _meta/check.py [layer-prefix ...]   e.g.  python3 _meta/check.py 07 08
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEAF_SECTIONS = ["## Essence", "## Core tenets", "## Key concepts", "## How it fits",
                 "## Common misconceptions", "## Go deeper"]
README_SECTIONS = ["## What this area is about", "## How the children fit together"]
ROOT_FILES = {"README.md", "CROSS-CUTTING.md"}
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


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


def slug(heading):
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def anchors(path):
    return {slug(m.group(1)) for m in re.finditer(r"^#+\s+(.*)$", path.read_text(), re.M)}


def main():
    prefixes = sys.argv[1:]
    dirs, leaves = taxonomy()
    expected = {f"{d}/README.md" for d in dirs} | leaves

    def selected(rel):
        return not prefixes or any(rel.startswith(p) for p in prefixes)

    errors, words = [], {}
    for rel in sorted(expected):
        if not selected(rel):
            continue
        p = ROOT / rel
        if not p.exists():
            errors.append(f"MISSING  {rel}")
            continue
        text = p.read_text()
        words[rel] = len(text.split())
        required = README_SECTIONS if rel.endswith("README.md") else LEAF_SECTIONS
        for sec in required:
            if sec not in text:
                errors.append(f"SECTION  {rel}: lacks '{sec}'")

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
                errors.append(f"LINK     {rel} -> {target}")
                continue
            if frag and dest.suffix == ".md":
                if dest not in anchor_cache:
                    anchor_cache[dest] = anchors(dest)
                if frag not in anchor_cache[dest]:
                    errors.append(f"ANCHOR   {rel} -> {target}")

    # "Builds on" must never point to a higher layer: that would break bottom-up reading.
    for rel in sorted(actual - ROOT_FILES):
        if not selected(rel):
            continue
        p = ROOT / rel
        src_layer = int(rel[:2])
        for line in p.read_text().splitlines():
            if line.startswith("> **Builds on:**"):
                for target in LINK.findall(line):
                    dest = (p.parent / target.partition("#")[0]).resolve()
                    try:
                        dest_rel = str(dest.relative_to(ROOT))
                    except ValueError:
                        continue
                    dst_layer = int(dest_rel[:2]) if dest_rel[:2].isdigit() else -1
                    # 00 and 01 are twin roots: engineering is written in mathematics.
                    if dst_layer > src_layer and not (src_layer == 0 and dst_layer == 1):
                        errors.append(f"UPWARD   {rel} builds on {dest_rel}")

    for e in errors:
        print(e)
    if words:
        leaf_w = [w for r, w in words.items() if not r.endswith("README.md")]
        print(f"\n{len(words)} files checked, {sum(words.values()):,} words"
              + (f"; leaves avg {sum(leaf_w)//len(leaf_w)}, min {min(leaf_w)}, max {max(leaf_w)}" if leaf_w else ""))
    print(f"{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
