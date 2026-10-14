#!/usr/bin/env python3
"""Check a skill folder against claude.ai upload rules before zipping.
Usage: python3 validate-skill.py path/to/skill-folder"""
import re, sys, pathlib
d = pathlib.Path(sys.argv[1]); f = d / "SKILL.md"; errs = []
if not f.exists(): sys.exit(f"FAIL: no SKILL.md in {d}")
m = re.match(r"^---\n(.*?)\n---\n", f.read_text(), re.S)
if not m: sys.exit("FAIL: SKILL.md must start with --- frontmatter ---")
fm = m.group(1)
name = (re.search(r"^name:\s*(.+)$", fm, re.M) or [None, ""])[1].strip().strip('"')
desc = (re.search(r'^description:\s*"?(.*?)"?\s*$', fm, re.M | re.S) or [None, ""])[1]
if not re.fullmatch(r"[a-z0-9-]{1,64}", name): errs.append(f"name '{name}' must be 1-64 chars of lowercase letters, digits, hyphens")
for w in ("claude", "anthropic"):
    if w in name: errs.append(f"name contains reserved word '{w}'")
if not desc: errs.append("description is missing")
if len(desc) > 1024: errs.append(f"description is {len(desc)} chars (max 1024)")
if re.search(r"<[^>]+>", desc): errs.append("description contains XML/HTML tags")
if d.name != name: errs.append(f"folder name '{d.name}' should match name '{name}'")
print("\n".join("FAIL: " + e for e in errs) if errs else f"PASS: {name} ({len(desc)}-char description)")
sys.exit(1 if errs else 0)
