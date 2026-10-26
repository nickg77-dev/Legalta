#!/usr/bin/env python3
"""Check every hook in a lead tab before anything is printed (Legalta QA gate).
Usage: python3 validate_hooks.py rows.json [--tab Municipalities]
Prints one line per problem. Exit code 1 if any problem is found.
Checks: suffixes and German opening per country; one sentence; no amounts, eligibility or
cartel dates; founding year <= 1997 and Founded column < 2012; dated counts < 2012;
trucks by chassis only (no trailers, low-beds, vans, excavators, telehandlers);
no legal form in the name; EN and DE carry the same numbers; every number in the hook
appears in Research notes next to a vehicle word and is not a weight (26t), an emission
class (Euro 6) or a model number (Volvo L 385); blank batch rows give a reason in notes;
no stale "Hook blank" note where a hook exists; Entity short name filled for batch rows."""
import json, re, sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from hooks import load, SUF_EN, suf_de
BAD = r"\b(trailers?|semi-trailers?|low-?beds?|low-loaders?|excavators?|telehandlers?|forklifts?|vans?|Sprinter|Unimog|Anhänger|Auflieger|Tieflader|Bagger|Teleskoplader|Stapler|Transporter)\b"
UNIT = r"(trucks?|lorr|vehicles?|units?|tippers|tankers|HGVs)"
def norm(x): return re.sub(r"[,.']", "", x)
def main(path, municipal):
    rows = load(path); bad = 0
    for n, r in enumerate(rows, start=2):
        g = lambda k: (r.get(k) or "").strip()
        en, de, notes = g("Hook sentence EN"), g("Hook sentence DE"), g("Research notes")
        if g("In batch") not in ("Lion claim", "Legalta", "Yes"): continue
        P = []
        if not g("Entity short name"): P.append("Entity short name blank (subject line breaks)")
        if not en and not de:
            if "Hook blank:" not in notes: P.append("blank hook, no reason in Research notes")
        else:
            if "Hook blank:" in notes: P.append("stale 'Hook blank' note but hook exists")
            ch = g("Country").lower().startswith(("swi", "sch", "ch"))
            if not en.endswith(SUF_EN): P.append("EN suffix wrong")
            if not de.endswith(suf_de(ch)): P.append("DE suffix wrong for country")
            if not de.startswith("Da " if ch else "da "): P.append("DE must start 'Da' (CH) or 'da' (DE/AT)")
            if ch and ("Lkw" in de or "ß" in de): P.append("Swiss DE uses Lkw or ß")
            body = en[:-len(SUF_EN)] if en.endswith(SUF_EN) else en
            dbody = de[:-len(suf_de(ch))] if de.endswith(suf_de(ch)) else de
            if any(len(re.findall(r"[\w-]+$", body[:m.start()])[-1:] and re.findall(r"[\w-]+$", body[:m.start()])[-1] or "") > 4 for m in re.finditer(r"\.\s", body)): P.append("possibly more than one sentence")
            if re.search(r"€|CHF|compensat|Schaden|eligib|\b1998\b|\b2012\b|1997-2011", en + de): P.append("amount, eligibility or cartel-date wording")
            if re.search(BAD, body, re.I) or re.search(BAD, dbody): P.append("non-truck vehicle named")
            if re.search(r"\b(GmbH|mbH|AG|KG|e\.K\.|eG|GesmbH)\b|\([^)]*$", body) and "LINZ AG" not in body: P.append("legal form or broken bracket in name")
            for y in re.findall(r"since (\d{4})", body):
                if int(y) > 1997: P.append(f"founding year {y} after 1997")
            for y in re.findall(r"in (\d{4})", body):
                if int(y) >= 2012: P.append(f"dated count {y} not before 2012")
            m = re.match(r"^(\d{4})", g("Founded"))
            if m and int(m.group(1)) >= 2012 and not municipal: P.append(f"Founded {m.group(1)} but hook present")
            name_nums = set(re.findall(r"\d+", g("Organisation") + " " + g("Entity short name")))
            ne = [x for x in re.findall(r"\b\d[\d,]*\b", body) if x not in name_nums]
            nd = [x for x in re.findall(r"\b\d[\d.']*\b", dbody) if x not in name_nums]
            if sorted(map(norm, ne)) != sorted(map(norm, nd)): P.append(f"EN/DE numbers differ {ne} vs {nd}")
            years = set(re.findall(r"since (\d{4})", body)) | set(re.findall(r"in (\d{4})", body))
            for x in ne:
                if x in years: continue
                if re.search(re.escape(x) + r"[- ]?(?:tonne|t\b)", body): continue  # stated weight, e.g. 18-tonne tipper
                pat = r"(?<![\d,.])" + re.escape(x) + r"\+?(?![\d,.])"
                hits = [mm for mm in re.finditer(pat, notes)]
                ok = False
                for mm in hits:
                    after = notes[mm.end():mm.end()+45]; before = notes[max(0, mm.start()-8):mm.start()]
                    if re.match(r"\s?t\b|\s?-?tonne", after, re.I) or re.search(r"Euro\s*$", before, re.I): continue
                    first = re.search(r"(trailer|semi)|" + UNIT, after, re.I)
                    if first and not first.group(1) and first.start() <= 40: ok = True
                if not ok: P.append(f"number {x} not tied to vehicles in notes (weight, Euro class, model or trailer?)")
        if P:
            bad += 1; print(f"row {n} | {g('Organisation')[:40]} | " + "; ".join(P))
    print(f"{bad} rows with problems"); return bad
if __name__ == "__main__":
    tab = sys.argv[sys.argv.index("--tab")+1] if "--tab" in sys.argv else "Private"
    sys.exit(1 if main(sys.argv[1], tab.lower().startswith("munic")) else 0)
