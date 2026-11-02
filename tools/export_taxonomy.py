"""Export a first-principles taxonomy as an agenticprofessor SPEC-615 TaxonomyBundle (v1).

Usage: python3 tools/export_taxonomy.py [taxonomy-dir ...]
       (default: cs-, medicine- and math-first-principles)

Reads, per taxonomy directory:
  _meta/TAXONOMY.md   the fixed path list: layer dirs -> area dirs -> topic .md (order = file order)
  */README.md, *.md   title (H1), essence, key terms, and the prerequisite edges:
                      the "> **Builds on:**" header links and the links in a README's
                      "Depends on" table column (from = the row's child, to = the linked node)
  DECK-MAP.csv        deck links, columns topicId,deckName,deckPath; deckPath is the deck's
                      segments joined by "::" and may be left blank (then deckName split on "::")
Writes <taxonomy-dir>/taxonomy-bundle.json. Standard library only; output is byte-stable.
"""
import csv, glob, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT = ["cs-first-principles", "medicine-first-principles", "math-first-principles"]
OUT_NAME = "taxonomy-bundle.json"
MAP_NAME = "DECK-MAP.csv"
REPO = "CodingSar/agenticdecks"
# Optional tour goal per taxonomy (a leaf); absent, the viewer picks its default (REQ-615-21).
TOUR_GOALS = {"cs-first-principles": "10-distributed-and-parallel-computing/03-consensus-and-replication/consensus"}
LEVEL_LABELS = [{"one": "Layer", "other": "Layers"}, {"one": "Area", "other": "Areas"}, {"one": "Topic", "other": "Topics"}]
RELATION_LABELS = {"requires": "Builds on", "enables": "Enables"}
MAX_TITLE, MAX_ESSENCE, MAX_TERM, MAX_TERMS, ESSENCE_BUDGET = 300, 600, 120, 16, 280
ESSENCE_HEADINGS = ("## Essence", "## What this area is about")
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9(\"“])")


def taxonomy_paths(tax_dir):
    """The fenced path list of _meta/TAXONOMY.md, in file order; dirs end with '/'."""
    text = open(os.path.join(tax_dir, "_meta", "TAXONOMY.md"), encoding="utf-8").read()
    block = text.split("```")[1]
    paths, stack = [], []
    for line in block.splitlines():
        if not line.strip():
            continue
        depth = (len(line) - len(line.lstrip())) // 2
        stack = stack[:depth] + [line.strip().rstrip("/")]
        paths.append("/".join(stack) + ("/" if line.strip().endswith("/") else ""))
    return paths


def source_file(tax_dir, path):
    """The markdown file that describes `path`: a dir's README.md, or the leaf itself."""
    return os.path.join(tax_dir, path, "README.md") if path.endswith("/") else os.path.join(tax_dir, path)


def plain(md):
    """Markdown inline text as plain text: link text kept, emphasis and code ticks dropped."""
    s = LINK.sub(r"\1", md)
    s = re.sub(r"(\*\*|__)(.+?)\1", r"\2", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"\1", s)
    s = s.replace("`", "")
    return re.sub(r"\s+", " ", s).strip()


def clip(s, limit):
    """`s` cut at a word boundary to at most `limit` characters, with an ellipsis when cut."""
    if len(s) <= limit:
        return s
    cut = s[: limit - 1].rsplit(" ", 1)[0].rstrip(" ,;:")
    return cut + "…"


def section(lines, headings):
    """The body lines of the first `## ` section whose heading is in `headings`."""
    out, inside = [], False
    for line in lines:
        if line.startswith("## "):
            if inside:
                break
            inside = line.strip() in headings
        elif inside:
            out.append(line)
    return out


def essence_of(lines):
    """The first paragraph of the essence section, whole sentences up to ESSENCE_BUDGET characters."""
    para = []
    for line in section(lines, ESSENCE_HEADINGS):
        if line.strip():
            para.append(line.strip())
        elif para:
            break
    sentences = SENTENCE_END.split(plain(" ".join(para)))
    text = sentences[0] if sentences else ""
    for s in sentences[1:]:
        if len(text) + 1 + len(s) > ESSENCE_BUDGET:
            break
        text += " " + s
    return text if len(text) <= MAX_ESSENCE else clip(text, ESSENCE_BUDGET)


def key_terms_of(lines):
    """First-column terms of the "Key concepts" table, at most MAX_TERMS."""
    terms = []
    for row in section(lines, ("## Key concepts",)):
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if not row.startswith("|") or not cells[0] or set(cells[0]) <= set("-: ") or cells[0] == "Term":
            continue
        term = clip(plain(cells[0]), MAX_TERM)
        if term and term not in terms:
            terms.append(term)
    return terms[:MAX_TERMS]


def title_of(lines, is_dir):
    """The H1, with a dir's leading number ("10 Distributed ...") dropped."""
    h1 = next((l[2:].strip() for l in lines if l.startswith("# ")), "")
    if is_dir:
        h1 = re.sub(r"^\d+\s+", "", h1)
    return clip(plain(h1), MAX_TITLE)


def order_of(path, nth):
    """A dir's numeric prefix ("03-..." -> 3); otherwise the 1-based sibling position."""
    m = re.match(r"(\d+)-", os.path.basename(path.rstrip("/")))
    return int(m.group(1)) if path.endswith("/") and m else nth


def build_nodes(tax_name, tax_dir, paths):
    """One node per listed path that exists on disk; returns (nodes, {nodeId: lines})."""
    nodes, texts, sibling = [], {}, {}
    for path in paths:
        node_id, parent = path.rstrip("/").removesuffix(".md"), os.path.dirname(path.rstrip("/")) or None
        src = source_file(tax_dir, path)
        if not os.path.isfile(src) or (parent is not None and parent not in texts):
            print(f"  warn: {tax_name}/{path} listed in TAXONOMY.md but missing; skipped", file=sys.stderr)
            continue
        lines = open(src, encoding="utf-8").read().splitlines()
        sibling[parent] = sibling.get(parent, 0) + 1
        texts[node_id] = lines
        nodes.append({
            "nodeId": node_id,
            "parentId": parent,
            "order": order_of(path, sibling[parent]),
            "title": title_of(lines, path.endswith("/")) or os.path.basename(node_id),
            "essence": essence_of(lines),
            "keyTerms": [] if path.endswith("/") else key_terms_of(lines),
            "sourcePath": os.path.relpath(src, ROOT).replace(os.sep, "/"),
        })
    return nodes, texts


def resolve(tax_dir, from_file, href):
    """The node id a relative markdown link names, or None (external, anchor-only, outside the tree)."""
    target = href.split("#")[0]
    if not target or re.match(r"^[a-z]+:", target) or not target.endswith(".md"):
        return None
    rel = os.path.relpath(os.path.normpath(os.path.join(os.path.dirname(from_file), target)), tax_dir)
    rel = rel.replace(os.sep, "/")
    if rel.startswith(".."):
        return None
    return os.path.dirname(rel) if rel.endswith("README.md") else rel.removesuffix(".md")


def builds_on_links(lines):
    """Hrefs of the "> **Builds on:**" header line."""
    line = next((l for l in lines if l.startswith("> **Builds on:**")), "")
    return [href for _, href in LINK.findall(line)]


def depends_on_rows(lines):
    """(child href, [dependency hrefs]) per row of a "Child | ... | Depends on" table."""
    rows, col = [], None
    for line in lines:
        if not line.startswith("|"):
            col = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if "Depends on" in cells:
            col = cells.index("Depends on")
        elif col is not None and len(cells) > col and LINK.search(cells[0]):
            rows.append((LINK.search(cells[0]).group(2), [h for _, h in LINK.findall(cells[col])]))
    return rows


def build_edges(tax_dir, nodes, texts):
    """`from` builds on `to`, deduplicated in source order; returns (edges, unresolved link count)."""
    ids, edges, seen, unresolved = {n["nodeId"] for n in nodes}, [], set(), 0
    for n in nodes:
        src = os.path.join(ROOT, n["sourcePath"])
        pairs = [(n["nodeId"], h) for h in builds_on_links(texts[n["nodeId"]])]
        for child, deps in depends_on_rows(texts[n["nodeId"]]):
            frm = resolve(tax_dir, src, child)
            pairs += [(frm, h) for h in deps] if frm in ids else []
        for frm, href in pairs:
            to = resolve(tax_dir, src, href)
            if to not in ids:
                unresolved += 1
            elif to != frm and (frm, to) not in seen:
                seen.add((frm, to))
                edges.append({"from": frm, "to": to})
    return edges, unresolved


def deck_names():
    """Every deck and subdeck name in work/out/*.json."""
    names = set()
    for p in glob.glob(os.path.join(ROOT, "work", "out", "*.json")):
        for note in json.load(open(p, encoding="utf-8")).get("notes", []):
            parts = note.get("deck", "").split("::")
            names.update("::".join(parts[: i + 1]) for i in range(len(parts)))
    return names


def build_links(tax_name, tax_dir, ids, decks):
    """DECK-MAP.csv rows as bundle links; an unknown topicId is an error, an unknown deck a warning."""
    path = os.path.join(tax_dir, MAP_NAME)
    if not os.path.isfile(path):
        return []
    links = []
    with open(path, encoding="utf-8", newline="") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            topic, deck = (row.get("topicId") or "").strip(), (row.get("deckName") or "").strip()
            if topic not in ids:
                sys.exit(f"{tax_name}/{MAP_NAME}:{i}: topicId {topic!r} is not a node of this taxonomy")
            if deck not in decks:
                print(f"  warn: {tax_name}/{MAP_NAME}:{i}: deck {deck!r} not in work/out", file=sys.stderr)
            deck_path = (row.get("deckPath") or "").strip() or deck
            links.append({"deckName": deck, "deckPath": [s.strip() for s in deck_path.split("::")], "nodeId": topic})
    return links


def source_ref(tax_name):
    """`owner/repo@sha` of the last commit touching the taxonomy's content (not its export or deck map)."""
    cmd = ["git", "-C", ROOT, "log", "-1", "--format=%h", "--", tax_name,
           f":!{tax_name}/{OUT_NAME}", f":!{tax_name}/{MAP_NAME}"]
    sha = subprocess.run(cmd, capture_output=True, text=True).stdout.strip() or "unknown"
    return f"{REPO}@{sha}"


def export(tax_name, decks):
    """Write <tax_name>/taxonomy-bundle.json and print its counts."""
    tax_dir = os.path.join(ROOT, tax_name)
    nodes, texts = build_nodes(tax_name, tax_dir, taxonomy_paths(tax_dir))
    edges, unresolved = build_edges(tax_dir, nodes, texts)
    ids = {n["nodeId"] for n in nodes}
    parents = {n["parentId"] for n in nodes}
    bundle = {
        "bundleVersion": 1,
        "taxonomyId": tax_name,
        "name": title_of(open(os.path.join(tax_dir, "README.md"), encoding="utf-8").read().splitlines(), False),
        "sourceRef": source_ref(tax_name),
        "levelLabels": LEVEL_LABELS,
        "relationLabels": RELATION_LABELS,
    }
    goal = TOUR_GOALS.get(tax_name)
    if goal is not None:
        if goal not in ids or goal in parents:
            sys.exit(f"{tax_name}: tour goal {goal!r} is not a topic")
        bundle["tourGoal"] = goal
    bundle.update(nodes=nodes, edges=edges, links=build_links(tax_name, tax_dir, ids, decks))
    with open(os.path.join(tax_dir, OUT_NAME), "w", encoding="utf-8") as f:
        f.write(json.dumps(bundle, ensure_ascii=False, indent=1) + "\n")
    depth = lambda n: n["nodeId"].count("/")
    leaves = sum(1 for n in nodes if n["nodeId"] not in parents)
    print(f"{tax_name}: {sum(depth(n) == 0 for n in nodes)} layers, {sum(depth(n) == 1 and n['nodeId'] in parents for n in nodes)} areas, "
          f"{leaves} topics, {len(edges)} edges ({unresolved} links outside the tree), {len(bundle['links'])} deck links")


if __name__ == "__main__":
    decks = deck_names()
    for name in sys.argv[1:] or DEFAULT:
        export(name.rstrip("/"), decks)
