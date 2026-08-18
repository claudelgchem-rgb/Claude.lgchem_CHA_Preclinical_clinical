#!/usr/bin/env python3
"""Consolidate every agent's unresolved register into RLSX/audit/unresolved.csv.

Charter R1 allows an item to be left unresolved only with its query log,
failure reason, alternatives tried and a best estimate. This collects them
into one auditable register so the count cannot drift.
"""
import csv
import glob
import os
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
OUT = os.path.join(ROOT, "audit", "unresolved.csv")
COLS = ["agent", "item", "queries_tried", "failure_reason", "alt_sources_tried",
        "best_estimate", "best_estimate_basis"]


def main():
    rows = []
    paths = sorted(glob.glob(os.path.join(ROOT, "work", "*", "unresolved.csv")))
    for path in paths:
        agent = os.path.basename(os.path.dirname(path))
        with open(path, encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                if not any((v or "").strip() for v in r.values()):
                    continue
                out = {"agent": agent}
                for c in COLS[1:]:
                    out[c] = (r.get(c) or "").strip()
                if not out["item"]:
                    continue
                rows.append(out)

    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)

    per = {}
    for r in rows:
        per[r["agent"]] = per.get(r["agent"], 0) + 1
    print("consolidated %d unresolved items -> RLSX/audit/unresolved.csv" % len(rows))
    for a in sorted(per):
        print("  %s: %d" % (a, per[a]))
    incomplete = [r["item"][:50] for r in rows
                  if not r["best_estimate"] or not r["failure_reason"]]
    if incomplete:
        print("\nR1 VIOLATION — unresolved items missing a reason or a best estimate (%d):" % len(incomplete))
        for i in incomplete[:15]:
            print("  " + i)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
