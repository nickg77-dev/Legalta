#!/usr/bin/env python3
"""Legalta hook generator (DACH rules, 6 Oct 2026).

Reads a lead tab exported as JSON (list of rows, first row = headers, as returned by the
Google Sheets get_values tool) or CSV, and writes one result per row:
  row, organisation, hook_en, hook_de, reason
reason is a hook type (count, year+count, types, ...) or a blank-hook reason that the
caller appends to Research notes as "Hook blank: <reason>."

Rules come from Legalta Fixed Facts and the Master Template Letter:
- one sentence, ending with the fixed consequence clause; no amounts or cartel dates
- founding year only if 1997 or earlier; founded 2012 or later -> hold (company tabs)
  Founding year is read from the Founded column, or from notes only next to
  "founded / established / gegründet" (never from "since").
- counts: current, or dated before 2012; thousands separators parsed (1,800 / 1.800 / 2'500)
- trucks by chassis only; never trailers, low-beds, excavators, telehandlers, vans
- German: "Sie" / "Ihr Unternehmen", never the company name; DE/AT "da", CH "Da", Lastwagen, ss
Usage: python3 hooks.py rows.json --tab Private|Municipalities --out hooks.json
"""
import json, re, sys, csv, argparse

SUF_EN = ", you are likely to have bought from the manufacturers involved in the EU truck cartel."
def suf_de(ch): return ", haben Sie wahrscheinlich bei Herstellern gekauft, die am %s beteiligt waren." % ("EU-Lastwagenkartell" if ch else "EU-Lkw-Kartell")

TRUCK = r"(heavy (?:goods )?vehicles|truck-chassis vehicles|trucks?|lorries|lorry|HGVs?|tippers?|dump trucks?|truck mixers?|concrete mixers?|mixer trucks?|refuse trucks?|refuse collection vehicles?|collection vehicles?|tankers?|tank trucks?|tractor units?|traction units?|rigids?)"
VEH = r"(vehicles)"
QUAL = r"(about |around |approx\.? |approximately |c\. |over |more than |nearly |almost |some |~)?"
ADJ = r"(?:(?!(?:trailers?|semi-trailers?|and|plus|with|incl\.?|containers?)\b)[A-Za-z-]+\s){0,2}?"
NUM = r"(\d{1,3}(?:[,.']\d{3})+|\d{1,4})"
MODEL = r"(eactros|e-actros|econic|euro|volvo|scania|man|daf|iveco|mercedes|mercedes-benz|renault|actros|atego|arocs|axor|tgs|tgx|tgm|tgl|fh|fm|fmx|fl|fe|cf|xf|lf|stralis|magirus|unimog|saurer|steyr|l|p|g|r|s|tlf|hlf|dlk|v8)$"
TYPES = [  # regex on notes, EN, DE, CH
 (r"refuse|waste collection (?:vehicles?|trucks?|fleet)", "refuse trucks", "Müllfahrzeuge", "Kehrichtfahrzeuge"),
 (r"tipper|dump truck", "tippers", "Kipper", "Kipper"),
 (r"(?:concrete|truck) mixer|mixer truck|ready-mix", "concrete mixers", "Fahrmischer", "Betonmischer"),
 (r"(?<!fire )tanker|tank truck|fuel truck", "tankers", "Tankwagen", "Tankwagen"),
 (r"refrigerated truck|reefer truck|refrigerated lorr", "refrigerated trucks", "Kühlfahrzeuge", "Kühlfahrzeuge"),
 (r"tractor unit|semi-trailer tractor|traction unit", "tractor units", "Sattelzugmaschinen", "Sattelschlepper"),
 (r"crane truck|truck-mounted crane|loader crane|loading crane", "crane trucks", "Kran-Lkw", "Kranlastwagen"),
 (r"fire (?:engine|tanker|vehicle|truck)|aerial ladder|rescue truck", "fire engines", "Feuerwehrfahrzeuge", "Feuerwehrfahrzeuge"),
 (r"gritter|winter service|snow plough|salt spread", "gritters", "Winterdienstfahrzeuge", "Winterdienstfahrzeuge"),
]
LEGAL = r"[\s,]+(GmbH\s*&\s*Co\.?\s*(KG|OHG)?|GmbH|mbH|AG|KG|OHG|e\.?\s?K\.?|e\.?\s?V\.?|eG|eGen|SE|GbR|GBR|Ges\.?m\.?b\.?H\.?|GesmbH|Gesmbh|& Co\.? KG|Co\.? KG|Nfg\.?|BV)\.?$"

def to_int(s): return int(re.sub(r"[,.']", "", s))
def fmt(n, lang, ch=False):
    if n < 1000: return str(n)
    s = f"{n:,}"
    return s if lang == "en" else s.replace(",", "'" if ch else ".")
def q_en(q, plus):
    q = (q or "").strip().lower()
    if plus or q in ("over", "more than"): return "more than "
    if q in ("about", "around", "approx.", "approx", "approximately", "c.", "~", "some", "nearly", "almost"): return "about "
    return ""
Q_DE = {"more than ": "mehr als ", "about ": "rund ", "": ""}
def lst(xs, a): return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + f" {a} " + xs[-1]

def clean_name(org, short):
    n = (short or "").strip()
    if not n or ":" in n: n = (org or "").strip()
    n = re.sub(r"\s*\([^)]*$", "", n)
    for _ in range(3): n = re.sub(LEGAL, "", n, flags=re.I).strip()
    n = re.sub(r"-GmbH$", "", n)
    n = re.sub(r",\s*(Kreisstadt|Hochschulstadt|Stadt|Große Kreisstadt|Hansestadt|Universitätsstadt).*$", "", n)
    n = re.sub(r"^(Stadt|Gemeinde|Marktgemeinde|Stadtgemeinde|Markt|Einwohnergemeinde|Politische Gemeinde)\s+", "", n)
    return n.strip(" ,-")

def dated(notes, m):
    pre = notes[max(0, m.start()-14):m.start()]; post = notes[m.end():m.end()+70]
    a = re.search(r"((?:19|20)\d\d)\s*[:,]?\s*$", pre)
    b = re.match(r"[^.;]{0,50}?\b(?:in|by|already in)\s+(?:[A-Z][a-z]{2,8}\.?\s+)?((?:19|20)\d\d)", post)
    y = a or b
    return int(y.group(1)) if y else None

def best_count(notes, noun_rx, noun_label):
    best = None
    for m in re.finditer(r"(?<![\w./-])" + QUAL + NUM + r"(\+)?(?![\d-])\s*" + ADJ + noun_rx + r"(?![\w-]*\s*(?:semi-?trailers?|trailers?|bodies|chassis))", notes, flags=re.I):
        n = to_int(m.group(2))
        after = notes[m.end(2):m.end(2)+3]
        if re.match(r"\s?t\b|\s?-?tonne", after, re.I): continue          # weight, not a count
        pre = notes[max(0, m.start()-12):m.start()].strip().split()
        if pre and re.match(MODEL, pre[-1].lower().strip("(,")): continue  # model number (Volvo L 385)
        if len(pre) >= 2 and pre[-1].lower() in ("and", "or", "und", "&") and re.match(r"\d+$", pre[-2]): continue  # Saurer 330 and 290
        if n < 5 or 1800 <= n <= 2030 and "," not in m.group(2) and "." not in m.group(2): continue
        yr = dated(notes, m)
        if yr and yr >= 2012: continue
        if best is None or n > best[0]: best = (n, q_en(m.group(1), m.group(3)), noun_label, yr)
    return best

def build(row, municipal):
    g = lambda k: (row.get(k) or "").strip()
    notes = g("Research notes"); status = g("Status"); batch = g("In batch")
    grade = g("Evidence grade") or g("Research quality grade (A-C)")
    if batch not in ("Lion claim", "Legalta", "Yes"): return "", "", "not in batch"
    if status.startswith("Excluded"): return "", "", "excluded"
    if grade not in ("A", "B", "C") or not notes: return "", "", "no fleet evidence"
    notes = re.sub(r"\s*Hook blank:[^.]*\.", "", notes)
    ch = g("Country").lower().startswith(("swi", "sch", "ch"))
    name = clean_name(g("Organisation"), g("Entity short name"))
    low = notes.lower()
    # founding year
    fv = g("Founded"); m = re.match(r"^(1[2-9]\d\d|20[0-2]\d)", fv)
    fy = int(m.group(1)) if m else None
    if fy is None:
        ys = [int(x) for x in re.findall(r"(?:founded|established|gegründet)\D{0,14}(1[2-9]\d\d|20[0-2]\d)", low)]
        fy = min(ys) if ys else None
    if fy and fy >= 2012 and not municipal: return "", "", "founded in %d" % fy
    year = fy if (fy and fy <= 1997 and not municipal) else None
    best = best_count(notes, TRUCK, "trucks") or best_count(notes, VEH, "vehicles")
    blocker_waste = bool(re.search(r"blocker[^.]*waste|waste[^.]*(contracted|outsourced)", low))
    ty = []
    for rx, en, de, chn in TYPES:
        if en == "refuse trucks" and blocker_waste: continue
        if en == "tankers" and municipal: continue
        if re.search(rx, low): ty.append((en, chn if ch else de))
    ty = ty[:3]
    lkw = "Lastwagen" if ch else "Lkw"; da = "Da" if ch else "da"; SD = suf_de(ch)
    ss = (lambda s: s.replace("ß", "ss")) if ch else (lambda s: s)
    if municipal:
        if best and best[2] == "trucks":
            n, q, _, _ = best
            return (f"As {name} runs {q}{fmt(n,'en')} trucks of its own" + SUF_EN,
                    ss(f"{da} Sie {Q_DE[q]}{fmt(n,'de',ch)} eigene {lkw} betreiben" + SD), "count")
        if ty:
            return (f"As {name} runs its own {lst([t[0] for t in ty],'and')}" + SUF_EN,
                    ss(f"{da} Sie eigene {lst([t[1] for t in ty],'und')} betreiben" + SD), "types")
        return "", "", "no usable facts"
    if best:
        n, q, noun, yr = best
        acc = lkw if noun == "trucks" else "Fahrzeuge"; dat = lkw if noun == "trucks" else "Fahrzeugen"
        ne, nd = fmt(n, "en"), fmt(n, "de", ch)
        if yr and year and yr < year: year = None
        if yr:
            if year:
                return (f"As {name} has been trading since {year} and already ran {q}{ne} {noun} in {yr}" + SUF_EN,
                        ss(f"{da} Ihr Unternehmen seit {year} besteht und bereits {yr} {Q_DE[q]}{nd} {acc} im Einsatz hatte" + SD), "year+dated count")
            return (f"As {name} already ran {q}{ne} {noun} in {yr}" + SUF_EN,
                    ss(f"{da} Sie bereits {yr} {Q_DE[q]}{nd} {acc} im Einsatz hatten" + SD), "dated count")
        if year:
            return (f"As {name} has been trading since {year} and runs {q}{ne} {noun}" + SUF_EN,
                    ss(f"{da} Ihr Unternehmen seit {year} besteht und {Q_DE[q]}{nd} {acc} betreibt" + SD), "year+count")
        return (f"As {name} runs a fleet of {q}{ne} {noun}" + SUF_EN,
                ss(f"{da} Sie eine Flotte von {Q_DE[q]}{nd} {dat} betreiben" + SD), "count")
    if ty:
        te, td = lst([t[0] for t in ty], "and"), lst([t[1] for t in ty], "und")
        if year:
            return (f"As {name} has been trading since {year} and runs its own {te}" + SUF_EN,
                    ss(f"{da} Ihr Unternehmen seit {year} besteht und eigene {td} betreibt" + SD), "year+types")
        return (f"As {name} runs its own {te}" + SUF_EN, ss(f"{da} Sie eigene {td} betreiben" + SD), "types")
    if year and re.search(r"own (?:truck|lorr|fleet|delivery)", low):
        return (f"As {name} has been trading since {year} and runs its own trucks" + SUF_EN,
                ss(f"{da} Ihr Unternehmen seit {year} besteht und eigene {lkw} betreibt" + SD), "year")
    return "", "", "no usable facts"

def load(path):
    if path.endswith(".csv"):
        with open(path, newline="", encoding="utf-8") as f: rows = list(csv.reader(f))
    else:
        d = json.load(open(path, encoding="utf-8"))
        if isinstance(d, list) and d and isinstance(d[0], dict) and "text" in d[0]: d = json.loads(d[0]["text"])
        rows = d["values"] if isinstance(d, dict) else d
    h = rows[0]
    return [dict(zip(h, r + [""] * (len(h) - len(r)))) for r in rows[1:]]

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("--tab", default="Private")
    ap.add_argument("--out", default="hooks.json"); a = ap.parse_args()
    rows = load(a.src); municipal = a.tab.lower().startswith("munic")
    out = []
    for i, r in enumerate(rows, start=2):
        en, de, why = build(r, municipal)
        out.append({"row": i, "organisation": r.get("Organisation", ""), "hook_en": en, "hook_de": de, "reason": why})
    json.dump(out, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    from collections import Counter
    print(Counter(o["reason"] for o in out))
