#!/usr/bin/env python3
"""RLSX quality gates G1-G9. Standard library only. exit 0 = all gates pass."""
import csv
import io
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ROOT = os.path.normpath(ROOT)

FAILURES = []
NOTES = []


def fail(gate, msg):
    FAILURES.append("[%s] %s" % (gate, msg))


def note(msg):
    NOTES.append(msg)


def p(*parts):
    return os.path.join(ROOT, *parts)


def read(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def read_lines(path):
    return read(path).splitlines()


def load_jsonl(path):
    recs = []
    if not os.path.exists(path):
        return recs
    with open(path, "r", encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                recs.append((i, json.loads(line)))
            except Exception as exc:
                fail("JSONL", "%s line %d not valid JSON: %s" % (os.path.relpath(path, ROOT), i, exc))
    return recs


def load_csv(path):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def md_files():
    out = []
    for base, dirs, files in os.walk(p()):
        dirs[:] = [d for d in dirs if d not in (".git",)]
        for f in files:
            if f.endswith(".md"):
                out.append(os.path.join(base, f))
    return sorted(out)


# ---------------------------------------------------------------- G1 CHARTER
REQUIRED_AGENT_REPORTS = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
CHARTER_LINE = "CHARTER_ACK: R1,R2,R3,R4"


def g1():
    workdir = p("work")
    if not os.path.isdir(workdir):
        fail("G1", "RLSX/work/ missing")
        return
    for agent in REQUIRED_AGENT_REPORTS:
        rp = p("work", agent, "report.md")
        if not os.path.exists(rp):
            fail("G1", "missing work/%s/report.md" % agent)
            continue
        lines = read_lines(rp)
        first = lines[0].strip() if lines else ""
        if first != CHARTER_LINE:
            fail("G1", "work/%s/report.md first line is %r, expected %r" % (agent, first[:80], CHARTER_LINE))
    # optional agents: if the report exists it must carry the ack too
    for agent in ("R", "X", "W"):
        rp = p("work", agent, "report.md")
        if os.path.exists(rp):
            lines = read_lines(rp)
            if not lines or lines[0].strip() != CHARTER_LINE:
                fail("G1", "work/%s/report.md exists but lacks CHARTER_ACK first line" % agent)


# --------------------------------------------------------------- G2 DEFERRAL
DEFERRAL_PATTERNS = [
    "추후", "향후 조사", "더 조사가 필요", "시간 관계상", "샘플로", "생략",
]
# Files that legitimately enumerate the forbidden lexicon itself.
G2_EXEMPT_BASENAMES = {"_COMMON_BRIEF.md"}
G2_ESCAPE = "<!--ALLOW-DEFERRAL-LEXICON-->"


def g2():
    for path in md_files():
        rel = os.path.relpath(path, ROOT)
        if os.path.basename(path) in G2_EXEMPT_BASENAMES:
            continue
        for n, line in enumerate(read_lines(path), 1):
            if G2_ESCAPE in line:
                continue
            for pat in DEFERRAL_PATTERNS:
                if pat in line:
                    fail("G2", "%s:%d contains deferral expression %r" % (rel, n, pat))


# --------------------------------------------------------------- G3 COVERAGE
def g3(ev_by_bottleneck):
    mpath = p("data", "bottleneck_matrix.csv")
    rows = load_csv(mpath)
    if rows is None:
        fail("G3", "data/bottleneck_matrix.csv missing")
        return
    ids = set()
    for r in rows:
        bid = (r.get("bottleneck_id") or "").strip()
        if bid:
            ids.add(bid)
    for i in range(1, 15):
        bid = "B%d" % i
        if bid not in ids:
            fail("G3", "bottleneck_matrix.csv has no row for %s" % bid)
    # >=3 evidence per candidate
    for i in range(1, 15):
        bid = "B%d" % i
        cnt = ev_by_bottleneck.get(bid, 0)
        if cnt < 3:
            fail("G3", "%s has %d evidence records in evidence.jsonl, need >=3" % (bid, cnt))
    # top bottlenecks need >=5 breakthrough technologies
    bpath = p("data", "breakthrough_candidates.csv")
    brows = load_csv(bpath)
    if brows is None:
        fail("G3", "data/breakthrough_candidates.csv missing")
        return
    ranked = []
    for r in rows:
        try:
            rank = int(float((r.get("provisional_rank") or "").strip()))
        except Exception:
            continue
        ranked.append((rank, (r.get("bottleneck_id") or "").strip()))
    ranked.sort()
    top = [b for _, b in ranked[:5]]
    if not top:
        fail("G3", "bottleneck_matrix.csv has no parseable provisional_rank values")
        return
    per = {}
    for r in brows:
        bid = (r.get("bottleneck_id") or "").strip()
        for tok in re.split(r"[;,\s]+", bid):
            tok = tok.strip()
            if tok:
                per[tok] = per.get(tok, 0) + 1
    for bid in top:
        if per.get(bid, 0) < 5:
            fail("G3", "top bottleneck %s has %d breakthrough candidates, need >=5" % (bid, per.get(bid, 0)))
    note("G3 top-5 bottlenecks: %s" % ", ".join(top))


# --------------------------------------------------------------- G4 CITATION
EVID_RE = re.compile(r"\[E-\d{4}\b")
SKIP_PREFIXES = ("#", "|", ">", "```", "---", "===", "<!--", "<a ", "<div", "</")
ALLOW_TOKENS = ("[INFER]", "[ASSUMPTION-UNSUPPORTED]", "[UNRESOLVED]", "⚠", "LOW-EVIDENCE")
G4_ESCAPE = "<!--NO-CITATION-REQUIRED-->"


# Charter P1 gives every section a plain-language layer. Those lines restate
# cited material in everyday words and are deliberately chip-free, so they are
# exempt from the citation requirement — but only while they stay qualitative.
# The moment such a line asserts a figure it must carry a chip like any other,
# which keeps every quantitative claim in the report traceable.
PLAIN_HEADING = re.compile(r"^#{2,6}\s*(쉽게 말하면|한 문장으로|이 표에서 볼 것|용어 풀이)")
PLAIN_QUOTE = re.compile(r"^>\s*\*\*한 문장으로\*\*")
NUMERIC_CLAIM = re.compile(r"\d")


def _citation_scan(path):
    """Return (cited, infer, uncited, plain) for prose lines in a markdown file."""
    cited = 0
    infer = 0
    plain = 0
    uncited = []
    in_code = False
    skip_block = False
    in_plain = False
    for n, raw in enumerate(read_lines(path), 1):
        line = raw.strip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if G4_ESCAPE in line:
            skip_block = not skip_block
            continue
        if skip_block:
            continue
        if line.startswith("#"):
            in_plain = bool(PLAIN_HEADING.match(line))
            continue
        if not line:
            continue
        if PLAIN_QUOTE.match(line):
            plain += 1
            continue
        if line.startswith(SKIP_PREFIXES):
            continue
        body = re.sub(r"^([-*+]|\d+\.)\s+", "", line)
        if not body:
            continue
        if not re.search(r"[0-9A-Za-z가-힣]", body):
            continue
        has_ev = bool(EVID_RE.search(body))
        has_allow = any(tok in body for tok in ALLOW_TOKENS)
        if has_ev:
            cited += 1
        if "[INFER]" in body:
            infer += 1
        if has_ev or has_allow:
            continue
        if in_plain:
            # exempt as plain language, unless it smuggles in a figure
            stripped = re.sub(r"`[^`]*`", "", body)
            if NUMERIC_CLAIM.search(stripped):
                uncited.append((n, "[풀이 층의 수치 주장은 근거 필요] " + body[:90]))
            else:
                plain += 1
            continue
        uncited.append((n, body[:110]))
    return cited, infer, uncited, plain


def g4():
    rpath = p("RLSX_report.md")
    if not os.path.exists(rpath):
        fail("G4", "RLSX_report.md missing")
        return
    cited, infer, uncited, plain = _citation_scan(rpath)
    if uncited:
        for n, txt in uncited[:25]:
            fail("G4", "RLSX_report.md:%d factual line without evidence ID: %s" % (n, txt))
        if len(uncited) > 25:
            fail("G4", "RLSX_report.md: %d more uncited lines suppressed" % (len(uncited) - 25))
    total = cited + infer
    if total:
        ratio = infer / float(total)
        if ratio > 0.20:
            fail("G4", "[INFER] line ratio %.1f%% exceeds 20%% (%d INFER / %d claim lines)" % (ratio * 100, infer, total))
        note("G4 citation lines=%d, INFER=%d (%.1f%%), plain-language lines=%d" % (cited, infer, ratio * 100, plain))
    else:
        fail("G4", "RLSX_report.md contains no citable claim lines at all")


# --------------------------------------------------------------- G5 GRADING
VALID_GRADES = {"상", "중", "하"}


def g5(records):
    if not records:
        fail("G5", "evidence/evidence.jsonl is empty or missing")
        return
    for lineno, rec in records:
        rid = rec.get("id", "?")
        if rec.get("graded_by") != "R":
            fail("G5", "%s graded_by=%r, expected 'R'" % (rid, rec.get("graded_by")))
        if rec.get("confidence") not in VALID_GRADES:
            fail("G5", "%s confidence=%r, expected 상/중/하" % (rid, rec.get("confidence")))
        if rec.get("collected_by") and rec.get("collected_by") == rec.get("graded_by"):
            fail("G5", "%s collected_by == graded_by (%r) — self-grading forbidden" % (rid, rec.get("collected_by")))


# --------------------------------------------------------------- G6 REDTEAM
def g6():
    fpath = p("audit", "redteam_findings.md")
    mpath = p("audit", "redteam_mapping.csv")
    if not os.path.exists(fpath):
        fail("G6", "audit/redteam_findings.md missing")
        return
    rows = load_csv(mpath)
    if rows is None:
        fail("G6", "audit/redteam_mapping.csv missing (mapping table required)")
        return
    need = {"finding_id", "verdict", "report_section", "reflected_text_locator"}
    if rows and not need.issubset(set(rows[0].keys())):
        fail("G6", "redteam_mapping.csv needs columns %s, has %s" % (sorted(need), sorted(rows[0].keys())))
        return
    txt = read(p("RLSX_report.md")) if os.path.exists(p("RLSX_report.md")) else ""
    adopted = [r for r in rows if (r.get("verdict") or "").strip().lower() in ("adopted", "채택", "partial", "부분채택", "partially_adopted")]
    if not adopted:
        fail("G6", "redteam_mapping.csv lists no adopted/partially-adopted findings; red team must produce at least one")
    for r in adopted:
        loc = (r.get("reflected_text_locator") or "").strip()
        if not loc:
            fail("G6", "finding %s adopted but reflected_text_locator empty" % r.get("finding_id"))
        elif loc not in txt:
            fail("G6", "finding %s locator not found in RLSX_report.md: %r" % (r.get("finding_id"), loc[:70]))
    # every finding id in the mapping must appear in the findings doc
    ftxt = read(fpath)
    for r in rows:
        fid = (r.get("finding_id") or "").strip()
        if fid and fid not in ftxt:
            fail("G6", "mapping references %s which is absent from redteam_findings.md" % fid)


# ------------------------------------------------------------ G7 PROVENANCE
def g7(records):
    for lineno, rec in records:
        rid = rec.get("id", "?")
        figs = rec.get("figures") or {}
        val = figs.get("value") if isinstance(figs, dict) else None
        hops = rec.get("provenance_hops") or []
        if val is not None:
            if not isinstance(hops, list) or len(hops) < 1:
                fail("G7", "%s carries a quantitative value but provenance_hops is empty" % rid)
        if rec.get("circular_risk") is True and rec.get("confidence") != "하":
            fail("G7", "%s has circular_risk=true but confidence=%r (must be 하)" % (rid, rec.get("confidence")))


# --------------------------------------------------------------------- G8 UI
def g8(records):
    hpath = p("RLSX_evidence.html")
    if not os.path.exists(hpath):
        fail("G8", "RLSX_evidence.html missing")
        return
    html = read(hpath)
    m = re.search(r'<script[^>]*type=["\']application/json["\'][^>]*>(.*?)</script>', html, re.S)
    # Source URLs inside the embedded ledger are data, not page dependencies.
    # Scan the markup only, or every evidence record hosted on a CDN trips this.
    markup = (html[:m.start()] + html[m.end():]) if m else html
    for bad in ("http://cdn", "https://cdn", "cdnjs", "unpkg.com", "jsdelivr", "fonts.googleapis", "fonts.gstatic"):
        if bad in markup:
            fail("G8", "RLSX_evidence.html references external resource %r (single-file requirement)" % bad)
    if not m:
        fail("G8", "RLSX_evidence.html has no <script type=\"application/json\"> embedded ledger")
        return
    try:
        data = json.loads(m.group(1).strip())
    except Exception as exc:
        fail("G8", "embedded ledger JSON does not parse: %s" % exc)
        return
    if isinstance(data, dict):
        data = data.get("evidence", [])
    embedded = set()
    for rec in data:
        if isinstance(rec, dict) and rec.get("id"):
            embedded.add(rec["id"])
    ledger_ids = set(rec.get("id") for _, rec in records)
    missing = ledger_ids - embedded
    if missing:
        fail("G8", "%d ledger records not embedded in HTML (e.g. %s)" % (len(missing), sorted(missing)[:5]))
    # report anchors must resolve
    rpath = p("RLSX_report.md")
    if os.path.exists(rpath):
        refs = set(re.findall(r"\[(E-\d{4})", read(rpath)))
        broken = sorted(r for r in refs if r not in embedded)
        if broken:
            fail("G8", "%d evidence IDs cited in report have no card in HTML: %s" % (len(broken), broken[:10]))
        note("G8 report cites %d distinct evidence IDs; ledger holds %d" % (len(refs), len(ledger_ids)))


# ------------------------------------------------------------------ G9 QUOTE
def g9(records):
    for lineno, rec in records:
        q = rec.get("quote") or ""
        if not isinstance(q, str):
            fail("G9", "%s quote is not a string" % rec.get("id"))
            continue
        w = len(q.split())
        if w > 15:
            fail("G9", "%s quote is %d words (max 15)" % (rec.get("id"), w))


# ------------------------------------------------------------ G10 LANGUAGE
# Charter rule L1: every reporting artifact must be written in Korean.
# Proper nouns, identifiers, code, CSV/JSON payloads and short quotes stay
# in their original language, so the test is on prose density rather than
# on the absence of Latin characters.
KOREAN_REQUIRED = [
    "RLSX_report.md",
    "RLSX_executive_brief.md",
    os.path.join("evidence", "grade_summary.md"),
    os.path.join("audit", "redteam_findings.md"),
]
HANGUL = re.compile(r"[\uac00-\ud7a3]")
G10_MIN_RATIO = 0.60


def _prose_lines(path):
    out = []
    in_code = False
    for raw in read_lines(path):
        line = raw.strip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not line:
            continue
        if line.startswith(("#", "|", ">", "---", "===", "<!--", "<a ", "<div", "</")):
            continue
        body = re.sub(r"^([-*+]|\d+\.)\s+", "", line)
        body = re.sub(r"\[E-\d{4}[^\]]*\]", "", body)      # evidence chips
        body = re.sub(r"`[^`]*`", "", body)                  # inline code
        body = re.sub(r"https?://\S+", "", body)             # urls
        if len(body) < 25:
            continue
        if not re.search(r"[A-Za-z\uac00-\ud7a3]", body):
            continue
        out.append(body)
    return out


def g10():
    for rel in KOREAN_REQUIRED:
        path = p(rel)
        name = rel.replace(os.sep, "/")
        if not os.path.exists(path):
            fail("G10", "missing reporting artifact RLSX/%s" % name)
            continue
        lines = _prose_lines(path)
        if not lines:
            fail("G10", "RLSX/%s has no scannable prose" % name)
            continue
        ko = [l for l in lines if HANGUL.search(l)]
        ratio = len(ko) / float(len(lines))
        if ratio < G10_MIN_RATIO:
            fail("G10", "RLSX/%s is %.0f%% Korean prose, charter L1 requires >=%.0f%% (%d of %d lines)"
                 % (name, ratio * 100, G10_MIN_RATIO * 100, len(ko), len(lines)))
            for l in [x for x in lines if not HANGUL.search(x)][:6]:
                fail("G10", "  non-Korean line in %s: %s" % (name, l[:100]))
        else:
            note("G10 %s: %.0f%% Korean prose (%d/%d lines)" % (name, ratio * 100, len(ko), len(lines)))


# ---------------------------------------------------------- G11 READABILITY
# Charter P1-P6. The report is written to be understood, not only audited.
# A dense wall of inline citations is technically traceable and practically
# unreadable, so these limits are enforced rather than recommended.
G11_TARGETS = ["RLSX_report.md", "RLSX_executive_brief.md"]
MAX_CHIPS_PER_LINE = 3
MAX_SENTENCE_CHARS = 150
MAX_LONG_SENTENCE_RATIO = 0.10
CHIP_RE = re.compile(r"\[E-\d{4}[^\]]*\]")


def _sentences(text):
    text = CHIP_RE.sub("", text)
    text = re.sub(r"`[^`]*`", "", text)
    parts = re.split(r"(?<=[.!?。])\s+|(?<=다\.)\s*|(?<=음\.)\s*", text)
    return [x.strip() for x in parts if len(x.strip()) > 10]


def g11():
    for rel in G11_TARGETS:
        path = p(rel)
        if not os.path.exists(path):
            fail("G11", "missing %s" % rel)
            continue
        lines = read_lines(path)
        text = "\n".join(lines)

        # P1: every numbered top-level section needs its plain-language layer
        sections = []
        cur = None
        in_code = False
        for line in lines:
            st = line.strip()
            if st.startswith("```"):
                in_code = not in_code
            if in_code:
                continue
            m = re.match(r"^##\s+(\d+)[.．]\s*(.+)$", st)
            if m:
                cur = {"no": m.group(1), "title": m.group(2)[:40], "body": []}
                sections.append(cur)
            elif cur is not None:
                cur["body"].append(st)
        if rel == "RLSX_report.md":
            if len(sections) < 9:
                fail("G11", "%s has %d numbered sections, expected 9" % (rel, len(sections)))
            for sec in sections:
                body = "\n".join(sec["body"])
                if "쉽게 말하면" not in body:
                    fail("G11", "%s §%s '%s' lacks a '쉽게 말하면' plain-language layer (charter P1)"
                         % (rel, sec["no"], sec["title"]))
                if "한 문장으로" not in body:
                    fail("G11", "%s §%s '%s' lacks a '한 문장으로' one-line summary (charter P1)"
                         % (rel, sec["no"], sec["title"]))

        # P3: chip density per line
        dense = []
        for n, line in enumerate(lines, 1):
            st = line.strip()
            if st.startswith(("|", "#", "```")):
                continue
            c = len(CHIP_RE.findall(st))
            if c > MAX_CHIPS_PER_LINE:
                dense.append((n, c))
        if dense:
            fail("G11", "%s: %d lines carry more than %d evidence chips (charter P3); worst: %s"
                 % (rel, len(dense), MAX_CHIPS_PER_LINE,
                    ", ".join("line %d has %d" % d for d in sorted(dense, key=lambda x: -x[1])[:5])))

        # P2: sentence length
        prose = []
        in_code = False
        for line in lines:
            st = line.strip()
            if st.startswith("```"):
                in_code = not in_code
                continue
            if in_code or not st or st.startswith(("#", "|", ">", "---")):
                continue
            prose.append(re.sub(r"^([-*+]|\d+\.)\s+", "", st))
        sents = _sentences(" ".join(prose))
        if sents:
            long_ones = [x for x in sents if len(x) > MAX_SENTENCE_CHARS]
            ratio = len(long_ones) / float(len(sents))
            if ratio > MAX_LONG_SENTENCE_RATIO:
                fail("G11", "%s: %.0f%% of sentences exceed %d chars, limit %.0f%% (charter P2); %d of %d"
                     % (rel, ratio * 100, MAX_SENTENCE_CHARS, MAX_LONG_SENTENCE_RATIO * 100,
                        len(long_ones), len(sents)))
                for x in sorted(long_ones, key=len, reverse=True)[:3]:
                    fail("G11", "  overlong (%d chars): %s…" % (len(x), x[:90]))
            avg = sum(len(x) for x in sents) / float(len(sents))
            note("G11 %s: %d sentences, avg %.0f chars, %d over limit"
                 % (rel, len(sents), avg, len(long_ones)))


# ------------------------------------------------------------------- extras
def structural():
    required = [
        "RLSX_report.md",
        "RLSX_executive_brief.md",
        "RLSX_evidence.html",
        "run_state.json",
        os.path.join("evidence", "evidence.jsonl"),
        os.path.join("evidence", "evidence_grades.jsonl"),
        os.path.join("evidence", "grade_summary.md"),
        os.path.join("model", "constraint_model.py"),
        os.path.join("model", "model_assumptions.md"),
        os.path.join("audit", "redteam_findings.md"),
        os.path.join("audit", "circular_audit.csv"),
        os.path.join("audit", "unresolved.csv"),
    ]
    for rel in required:
        if not os.path.exists(p(rel)):
            fail("STRUCT", "missing required artifact RLSX/%s" % rel.replace(os.sep, "/"))
    for name in ("stage_economics", "ai_track_record", "bottleneck_matrix", "regulatory_landscape",
                 "trial_ops", "cmc_capacity", "dbtl_throughput", "breakthrough_candidates",
                 "scenario_results"):
        rel = os.path.join("data", name + ".csv")
        if not os.path.exists(p(rel)):
            fail("STRUCT", "missing required dataset RLSX/data/%s.csv" % name)


def duplicate_ids(records):
    seen = {}
    for lineno, rec in records:
        rid = rec.get("id")
        if rid in seen:
            fail("LEDGER", "duplicate evidence id %s (lines %d and %d)" % (rid, seen[rid], lineno))
        else:
            seen[rid] = lineno


def main():
    records = load_jsonl(p("evidence", "evidence.jsonl"))
    ev_by_bottleneck = {}
    for _, rec in records:
        b = (rec.get("bottleneck") or "").strip()
        for tok in re.split(r"[;,\s]+", b):
            tok = tok.strip()
            if tok:
                ev_by_bottleneck[tok] = ev_by_bottleneck.get(tok, 0) + 1

    structural()
    duplicate_ids(records)
    g1()
    g2()
    g3(ev_by_bottleneck)
    g4()
    g5(records)
    g6()
    g7(records)
    g8(records)
    g9(records)
    g10()
    g11()

    out = sys.stdout
    out.write("RLSX validate.py — %d evidence records\n" % len(records))
    for n in NOTES:
        out.write("  note: %s\n" % n)
    if FAILURES:
        sys.stderr.write("\n=== GATE FAILURES (%d) ===\n" % len(FAILURES))
        for f in FAILURES:
            sys.stderr.write(f + "\n")
        sys.stderr.write("=== exit 1 ===\n")
        return 1
    out.write("ALL GATES PASS (G1-G11)\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
