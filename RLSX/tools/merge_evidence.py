#!/usr/bin/env python3
"""Merge ./RLSX/evidence/parts/*.jsonl into ./RLSX/evidence/evidence.jsonl.

Normalizes every record to the full schema, reports ID-block violations and
duplicates, and never silently drops a record.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
PARTS = os.path.join(ROOT, "evidence", "parts")
OUT = os.path.join(ROOT, "evidence", "evidence.jsonl")

BLOCKS = {"A": 1, "B": 2, "C": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "D": 9}

SCHEMA_DEFAULTS = {
    "id": "", "claim": "", "bottleneck": "", "type": "secondary", "source_title": "",
    "publisher": "", "authors_or_org": "", "url": "", "published_date": "",
    "accessed_date": "2026-08-18", "quote": "", "figures": None,
    "collected_by": "", "graded_by": None, "confidence": None, "grade_reason": [],
    "cross_refs": [], "provenance_hops": [], "circular_risk": False, "derivation": "",
}
FIG_DEFAULTS = {"metric": "", "value": None, "unit": "", "denominator_def": "", "sample": "", "coc_included": None}


def main():
    problems = []
    records = {}
    order = []
    for path in sorted(glob.glob(os.path.join(PARTS, "*.jsonl"))):
        agent = os.path.splitext(os.path.basename(path))[0]
        with open(path, "r", encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except Exception as exc:
                    problems.append("PARSE %s:%d %s" % (agent, n, exc))
                    continue
                rid = rec.get("id", "")
                if not re.match(r"^E-\d{4}$", rid or ""):
                    problems.append("BADID %s:%d %r" % (agent, n, rid))
                    continue
                expected = BLOCKS.get(agent)
                if expected is not None and int(rid[2]) != expected:
                    problems.append("BLOCK %s:%d id %s outside block E-%dxxx" % (agent, n, rid, expected))
                if rid in records:
                    problems.append("DUP  %s:%d id %s already seen" % (agent, n, rid))
                    continue
                merged = dict(SCHEMA_DEFAULTS)
                merged.update(rec)
                figs = merged.get("figures")
                fixed = dict(FIG_DEFAULTS)
                if isinstance(figs, dict):
                    fixed.update(figs)
                merged["figures"] = fixed
                for k in ("grade_reason", "cross_refs", "provenance_hops"):
                    if not isinstance(merged.get(k), list):
                        merged[k] = [] if merged.get(k) in (None, "") else [merged[k]]
                if not merged.get("collected_by"):
                    merged["collected_by"] = agent
                records[rid] = merged
                order.append(rid)

    order.sort()
    with open(OUT, "w", encoding="utf-8") as fh:
        for rid in order:
            fh.write(json.dumps(records[rid], ensure_ascii=False) + "\n")

    by_agent = {}
    for rid in order:
        a = records[rid]["collected_by"]
        by_agent[a] = by_agent.get(a, 0) + 1
    print("merged %d records -> RLSX/evidence/evidence.jsonl" % len(order))
    for a in sorted(by_agent):
        print("  %s: %d" % (a, by_agent[a]))
    if problems:
        print("\nPROBLEMS (%d):" % len(problems))
        for pb in problems:
            print("  " + pb)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
