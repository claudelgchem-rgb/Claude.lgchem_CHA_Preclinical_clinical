#!/usr/bin/env python3
"""Merge R's independent grades into the consolidated evidence ledger.

Grading is done by agent R alone (charter R3). This script is the only
path by which a confidence value enters evidence.jsonl, so a record can
never carry a grade its collector assigned.
"""
import json
import os
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
LEDGER = os.path.join(ROOT, "evidence", "evidence.jsonl")
GRADES = os.path.join(ROOT, "evidence", "evidence_grades.jsonl")

VALID = {"상", "중", "하"}


def main():
    grades = {}
    with open(GRADES, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            g = json.loads(line)
            grades[g["id"]] = g

    recs = []
    with open(LEDGER, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                recs.append(json.loads(line))

    applied = 0
    ungraded = []
    selfgraded = []
    for r in recs:
        g = grades.get(r["id"])
        if not g:
            ungraded.append(r["id"])
            continue
        conf = g.get("confidence")
        if conf not in VALID:
            ungraded.append(r["id"])
            continue
        if g.get("graded_by") != "R":
            selfgraded.append(r["id"])
            continue
        r["graded_by"] = "R"
        r["confidence"] = conf
        r["grade_reason"] = g.get("grade_reason") or []
        r["verification_method"] = g.get("verification_method", "")
        r["verification_note"] = g.get("verification_note", "")
        r["grade_rationale"] = g.get("grade_rationale", "")
        # The grader's post-re-access provenance judgment supersedes the
        # collector's flag, but only when a chain was actually traced.
        corrected = g.get("corrected_provenance_hops") or []
        if corrected:
            r["provenance_hops"] = corrected
        if g.get("circular_risk_final") is not None:
            r["circular_risk"] = bool(g["circular_risk_final"])
        for xref in (g.get("cross_refs") or []):
            if xref not in r["cross_refs"]:
                r["cross_refs"].append(xref)
        applied += 1

    # Gate G7 invariant: a record still flagged circular must read 하.
    forced = 0
    for r in recs:
        if r.get("circular_risk") is True and r.get("confidence") != "하":
            r["confidence"] = "하"
            reasons = r.get("grade_reason") or []
            if "S3" not in reasons and "S7" not in reasons:
                reasons.append("S3")
            r["grade_reason"] = reasons
            r["grade_rationale"] = (r.get("grade_rationale", "") +
                                    " [orchestrator: forced 하 — circular_risk stands after grading]").strip()
            forced += 1

    with open(LEDGER, "w", encoding="utf-8") as fh:
        for r in recs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    dist = {}
    for r in recs:
        dist[r.get("confidence")] = dist.get(r.get("confidence"), 0) + 1
    print("ledger records : %d" % len(recs))
    print("grades applied : %d" % applied)
    print("forced 하 (G7) : %d" % forced)
    print("distribution   : %s" % dist)
    if selfgraded:
        print("SELF-GRADED (rejected): %s" % selfgraded[:10])
    if ungraded:
        print("UNGRADED (%d): %s" % (len(ungraded), ungraded[:20]))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
