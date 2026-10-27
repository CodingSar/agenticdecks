"""Write work/flags/<deck_id>.jsonl: {id, check, evidence}. Flags are leads, not verdicts."""
import os, re, json, collections
from common import *

CLOZE = re.compile(r"\{\{c(\d+)::(.*?)(?:::(.*?))?\}\}", re.S)
LABEL = re.compile(r"^(?:[A-Za-z]{1,4}[- ]?\d+|(?:step|phase|stage|layer|rule|tip|principle|law|level)\s*\d+|[A-Za-z]|\d+[.)]?|[ivxIVX]+[.)])$", re.I)
STOP = set("the a an of to in and or is are for on with by as at it its this that be from".split())

def toks(s): return {t for t in re.findall(r"[a-z0-9]+", strip_html(s).lower()) if t not in STOP}
def jac(a, b): return len(a & b) / len(a | b) if a and b else 0.0

def cloze_flags(text):
    out = []; ms = list(CLOZE.finditer(text))
    plain = strip_html(CLOZE.sub(lambda m: m.group(2), text)).lower()
    visible = strip_html(CLOZE.sub("", text)).lower()
    for m in ms:
        ans = strip_html(m.group(2)).strip(); a = ans.lower()
        if len(a) <= 2 or re.fullmatch(r"\d+", a):
            out.append(("TRIVIAL-CLOZE", f"short blank '{ans}'")); continue
        if a and a in visible:
            out.append(("TRIVIAL-CLOZE", f"blank '{ans[:40]}' also visible in card")); continue
        after = text[m.end():m.end() + 2]
        before = text[:m.start()].rstrip()
        if LABEL.match(ans) and (after.startswith(":") or after.startswith(".")):
            out.append(("TRIVIAL-CLOZE", f"label '{ans}' blanked, content visible")); continue
        if LABEL.match(ans):
            others = [strip_html(x.group(2)) for x in ms if x is not m]
            vis_labels = re.findall(r"\b(?:[A-Za-z]{1,4}\d+|[Ss]tep \d+)\b", visible)
            if vis_labels or others:
                out.append(("TRIVIAL-CLOZE", f"sequential label '{ans}' blanked among visible labels")); continue
    # over-cued sequence: many list items, few blanked
    items = re.findall(r"(?:<li>|<br>\s*|\n)\s*(?:\d+[.)]|[-•*]|[A-Za-z]{1,4}\d+:|Step \d+:)?", text)
    li = len(re.findall(r"<li>", text)) or len(re.findall(r"(?:<br>|\n)\s*(?:\d+[.)]|[-•*])", text))
    if li >= 4 and len(ms) / li <= 0.25:
        out.append(("OVER-CUED-SEQUENCE", f"{li} items, {len(ms)} blanked ({100 - 100 * len(ms) // li}% visible)"))
    arrows = text.count("→") + text.count("&rarr;") + text.count("->")
    if arrows >= 3 and len(ms) / (arrows + 1) <= 0.25:
        out.append(("OVER-CUED-SEQUENCE", f"{arrows + 1} chain steps, {len(ms)} blanked"))
    return out

REL = re.compile(r"^(how|why)\s+(does|do|is|are|can)\b.*\b(depend|relate|related|connect|connected|affect|influence|differ|relationship)\b", re.I)
SEQ_Q = re.compile(r"\b(steps?|stages?|phases?|sequence|order|lifecycle|process|flow)\b", re.I)

def main():
    fl = os.path.join(SCRATCH, "flags"); os.makedirs(fl, exist_ok=True)
    allcards = []; per = collections.defaultdict(list)
    for p in deck_files():
        d = load(p); did = deck_id_of(p)
        for i, n in enumerate(d["notes"]):
            cid = card_id(d["deck_name"], n); front = n["text"] if n["type"] == "cloze" else n["front"]
            back = "" if n["type"] == "cloze" else n["back"]
            def add(check, ev): per[did].append({"id": cid, "check": check, "evidence": ev})
            if n["type"] == "cloze":
                if not CLOZE.search(front): add("MALFORMED", "cloze without deletion")
                for c, e in cloze_flags(front): add(c, e)
            else:
                if not strip_html(front) or not strip_html(back): add("MALFORMED", "empty front or back")
                w = words(back)
                items = len(re.findall(r"<li>", back)) or len(re.findall(r"(?:<br>|\n)\s*(?:\d+[.)]|[-•*])", back))
                if w > 60: add("OVERLOADED", f"{w} words")
                elif items >= 4: add("OVERLOADED", f"{items} list items")
                elif len(re.findall(r";", strip_html(back))) >= 3: add("OVERLOADED", "3+ semicolon-separated items")
                if REL.search(strip_html(front)): add("OVER-CUED-RELATIONAL", strip_html(front)[:90])
                if SEQ_Q.search(strip_html(front)) and items >= 4 and re.search(r"(?i)\b(step|which|what comes|next|after)\b", front):
                    add("OVER-CUED-SEQUENCE", "front asks for a single step of a sequence")
            if n["type"] == "basic" and len(strip_html(front)) < 6: add("MALFORMED", "very short front")
            allcards.append((did, cid, toks(front + " " + (back if n["type"] == "cloze" else "")), strip_html(front).lower()))
    # duplicates (exact + near) via inverted index
    inv = collections.defaultdict(list)
    for k, (did, cid, ts, nf) in enumerate(allcards):
        cand = collections.Counter(j for t in ts for j in inv[t] if len(inv[t]) < 400)
        for j, c in cand.items():
            if c < 3: continue
            d2, c2, ts2, nf2 = allcards[j]
            exact = nf == nf2 and nf
            if exact or jac(ts, ts2) >= 0.8:
                scope = "within-deck" if did == d2 else "cross-deck"
                kind = "EXACT-DUP" if exact else "NEAR-DUP"
                per[did].append({"id": cid, "check": kind, "evidence": f"{scope} with {c2} ({d2})"})
                if did != d2: per[d2].append({"id": c2, "check": kind, "evidence": f"cross-deck with {cid} ({did})"})
        for t in ts: inv[t].append(k)
    for p in deck_files():
        did = deck_id_of(p)
        with open(os.path.join(fl, did + ".jsonl"), "w") as f:
            for r in per[did]: f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(did, dict(collections.Counter(r["check"] for r in per[did])))
main()
