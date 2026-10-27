"""Shared helpers for the deck-simplification tooling."""
import glob, json, os, re, genanki
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "work", "out")
SCRATCH = os.path.join(ROOT, "work")

def deck_files(): return sorted(glob.glob(os.path.join(OUT, "*.json")))
def deck_id_of(path): return os.path.basename(path)[:-5]
def load(path): return json.load(open(path))
def save(path, d):
    with open(path, "w") as f:
        json.dump(d, f, indent=1, ensure_ascii=False); f.write("\n")

def computed_guid(deck_name, n):
    """The GUID tools/build.py derives when a note has no explicit guid."""
    if n["type"] == "cloze":
        f = [n["text"], n.get("image", "")]
    else:
        f = [n["front"], n["back"]]
    return genanki.guid_for(deck_name, *f)

def card_id(deck_name, n): return n.get("guid") or computed_guid(deck_name, n)
def strip_html(s): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s or "")).strip()
def words(s): return len(strip_html(re.sub(r"\\\(.*?\\\)", " ", s or "")).split())
