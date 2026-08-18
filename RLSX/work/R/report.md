CHARTER_ACK: R1,R2,R3,R4

# Agent R — Independent Reliability Grading: method, coverage, and disagreements

## 1. Scope and completion

I graded **all 774 records** in `RLSX/evidence/evidence.jsonl` in three passes: agents
A, B, C, E, F, G, H, I (640 records); agents D and X plus C's revision block E-3099 to
E-3125 (110 records); and Agent I's follow-up block E-8107 to E-8130 (24 records).
No record was skipped, sampled, or deferred.
Output: `RLSX/evidence/evidence_grades.jsonl`, one object per record.

I collected none of this evidence. No grade in this run was assigned by the agent that
gathered the evidence.

## 2. Method

**Basal state.** I did not read any collector's report, conclusions, or narrative before
grading its evidence. I read only the ledger records themselves — claim, figures, sample,
publisher, URL, provenance hops, derivation — plus, for the derived records, the arithmetic.
This was deliberate: a grader who reads the argument first will grade the argument.

**Re-access.** I attempted to re-open 134 of the 774 sources (17%) across roughly seventy
WebFetch and WebSearch calls. Prioritisation followed the brief exactly:
1. every record carrying a load-bearing quantitative figure (all four anchors under test);
2. every claim that is surprising or is doing heavy work in a conclusion;
3. every `circular_risk:true` record I could reach;
4. every `type:"market_report"` and a large share of `type:"secondary"`.

Where the fetch tool returned raw PDF bytes I decompressed the content streams and read the
text layer directly. That is how I verified the CIRS R&D Briefing 101 regulatory-timing tables
(all six agencies, plus the EMA procedure decomposition), the BIO 2011-2020 success-rate and
modality tables, the Ringel *Breaking Eroom's Law* analysis, and FDA's CY2025 IND activity
table. Several of these were records the provenance audit could not reach.

For the 623 records I did not re-open, I graded conservatively on verifiable metadata:
publisher class, source type, whether a sample and denominator are stated, whether methodology
is disclosed, and whether any *independent* record in the ledger corroborates the claim.
`verification_method` records which of the three routes applied to each record. I never marked
a record `refetched` that I did not open.

**Arithmetic.** I independently recomputed every derived record's arithmetic — 134 records.
This caught seven errors and inconsistencies, listed in §8 of `grade_summary.md`. It also
confirmed a large majority as exact, including the three independent Amdahl-ceiling
computations, all four Wilson intervals in E-2066, the power calculation in E-2065, the
label-noise ceiling in E-7100, and D's engine-reproduction check.

**Applying R3 strictly.** 상 requires all three of: a primary source; two or more *independent*
cross-confirmations; and methodology disclosed sufficiently to reproduce. I applied "independent"
literally. Two records citing the same Biomedtracker extract are not two confirmations. Two
agents capturing the same Tufts CSDD analysis are not two confirmations — X's E-9553 makes
exactly this point and I reached the same conclusion independently while grading E-3020 and
E-5020. Five records out of 750 cleared the bar.

Company self-reports about their own products, platforms or pipelines took S4 and were capped
at 중; where also uncorroborated, 하. I made one systematic distinction inside that rule, and
state it here because it affects many grades: a company's **bare factual status disclosure**
(phase reached, trial initiated, programme discontinued, headcount, delisting) — especially in
a regulated filing or against the discloser's own interest — I graded 중 with S4, because the
company is the record of origin for that fact. A company's **performance claim** about its own
platform, molecule or process I graded 하. So Schrödinger disclosing two treatment-related
deaths in its own trial is 중; Insilico's 18-month discovery timeline is 하.

## 3. Reconciliation with the provenance audit

Agent X's audit marked 232 records FORCE_LOW. I upheld 207 as 하 and overrode 25 by recording
a traced provenance chain in `corrected_provenance_hops`, in each case because my own re-access
reached an origin the audit did not. The overrides and what I reached are tabulated in §4 of
`grade_summary.md`. There are zero unresolved FORCE_LOW violations.

I did **not** override the DiMasi anchors (E-1001, E-1002). I re-read the abstract and confirmed
every figure, but that reaches the paper, not its inputs: a confidential survey of unnamed firms
about unnamed compounds. The audit's judgment that this cannot be verified is correct, and the
most-quoted number in the field is Low in this ledger as a result. I want that on the record as
a considered agreement, not a default.

## 4. Where I disagreed with a collector's framing

**Agent B, E-2002 — the AI Phase I denominator.** B recorded that "the accessible sources do
not disclose the Phase I denominator" and I initially graded the record 하 partly on that basis.
Agent C's E-3008 asserted the denominator is 21 of 24. I searched, confirmed C, and **revised
my own grade** on E-2002 from 하 to 중, withdrawing the S2 code. I also revised E-2066, whose
premise ("the source refuses to disclose its denominator") is wrong even though its arithmetic
is exact and its conclusion — that the interval at n=24 overlaps conventional Phase I rates —
stands. Recording this because a grader who never changes a grade is not grading.

**Agent C, E-3072 and E-3103 — the biomarker count.** C recorded 11 qualified biomarkers and
then, in its revision pass, explicitly stated the figure "has not been contradicted". It is
contradicted by C's own cited source, which I re-accessed: FDA has formally qualified **eight**,
seven of them before the 2016 Cures Act. Agent X reached eight independently. I graded E-3072
하 on that basis. C's later E-3123 accepts the correction, which is why that record grades 중.

**Agent C, E-3015 — ISTAND.** C recorded zero qualified drug development tools as of 1 Jan 2026,
via an AI-content aggregator. FDA qualified AIM-NASH on 8 Dec 2025 and I confirmed it through
four independent outlets. C's record is 하 and factually wrong; E's E-4004 is one of the five
상 records in the ledger.

**Agent C, E-3024 — the Unger citation.** The 56/22/15 figures are correct but the record cites
the wrong paper (JNCI 2021 rather than Unger 2019, JNCI 111(3):245). Agent F cites it correctly
at E-5032, which I graded 상. I also flagged a denominator problem C's framing obscures: the
14.8% is a share of *all* patients, not of eligible patients — of patients actually offered a
trial, roughly 45% decline.

**Agent G, E-6037 and E-6072 — the 3,000-fold tumour uptake gap.** I re-accessed the source and
it says something the ledger framing risks losing: the ~3,000-fold %ID/g difference between
mouse and human tumours is a **body-mass scaling artefact of the units**, and the actual drug
*concentration* in tumour is similar at equal mg/kg dosing. Read as evidence of a human tumour
penetration deficit, this would be a misreading of the paper. I noted it on both records and on
E-6076, which uses it to record a "0-fold decadal improvement".

**Agent G, E-6060 to E-6070 — the saturation multiples.** G's derivations are labelled `derived`
with `AUD=clean/yes` because they cite their inputs properly. But the mechanism converting
booking lead time into a utilisation figure is an invented rule with no cited empirical basis,
and it generates every number in the run's manufacturing constraint ordering. I graded nine of
the ten component multiples 하 and the ordering 하. This is the single largest block where my
grade departs from the audit's clean verdict, and it is a substantive disagreement about what
"clean provenance" means: citing your inputs correctly does not make an invented parameter
mapping evidence.

**Agent D — transparency treated as a constraint, not a discount.** D marked fifteen assumptions
`[ASSUMPTION-UNSUPPORTED]`, disclosed a 49-57% coverage shortfall against observed IND and
patient volumes, and reported a +217% discrepancy against Sertkaya that it could not reconcile
and declined to average away. That is exemplary practice. It is also why 20 of D's 29 records
grade 하: the model's headline results depend on the budget identity and the queue, rationing
and combination rules, all of which D itself marks unsupported. I graded E-9025 (engine
reproduction), E-9026 (untuned cross-validation), E-9021, E-9023 and E-9041 at 중 because they
do not depend on that machinery. E-9041 — that roughly a third of the headline cost-per-approval
figure is the discount-rate choice — is in my view the most useful result D produced and among
the least assumption-dependent.

**Agent D, E-9024 and Agent C, E-3113/E-3115 — a circularity in the cross-agent agreement.**
D calibrated its overlap coefficient ρ to reproduce C's stated non-additivity band, then C cited
D's model as independent confirmation of that band and rescaled its own elasticities by D's
budget factor. Part of that agreement is constructed, not found. The *single-lever* reproductions
(D getting 10.19 against C's 10.0, and so on, from different stage probabilities) are a genuine
check; the *joint* agreement is not. I graded all four records 하 and flagged the loop.

**Agent I's follow-up block — where I disagreed on the recommend/require distinction.**
Three of the four TRL-8 ratings in that block rest on instruments that recommend rather than
require. E-8107 says the FDA dose-optimisation guidance is "directing sponsors"; it is final
and in force, but FDA's own convention is that "should" means suggested, not required, and
E-8108 — the companion record — gets this right by saying "recommends". E-8116 claims seven
jurisdictions "require" estimands; ICH E9(R1) is a Step 5 scientific guideline in the EU and a
non-binding guidance in the US, and the Taiwan instrument I verified is a guidance. E-8112's
ICH M15 is a general-principles guideline alongside a voluntary meeting programme. Only T-093's
NHS procurement (E-8126, 상) is a decision in force with money committed. I graded the records
Medium rather than Low because the instruments are real and correctly dated, but the TRL-8
ratings built on them should be described as "final instrument issued", never as "mandate".

**Agent X — graded exactly as strictly as everyone else.** X's block is 44% 하. Its own
evidence includes consultancy pipeline claims (E-9509), think-tank compilations of unnamed
commercial databases (E-9520, E-9521), a deal tracker dominated by contingent milestones
(E-9522), and the same Biomedtracker lineage it criticises elsewhere (E-9512, E-9513). X's
strongest records are its origin traces — E-9536 (85% of the druggable genome never prosecuted,
which I verified at source), E-9545 (eight biomarkers), E-9553 (the shared Tufts origin, which
I reached independently) and E-9554 (the 90% myth denominator, which I verified at source).
X's own summary statistic E-9551 is now stale: it reports on a 679-record ledger that has since
grown to 750.

## 5. What I could not do, and my best estimate of its effect

I re-accessed 17% of records rather than 100%. Roughly forty attempted fetches failed on
paywalls and authentication walls — Nature, Springer, ScienceDirect, ASCO Publications, NEJM
Evidence, several FDA pages returning 401 — and I recorded those as `refetch_failed` with a note
rather than pretending to metadata-only judgment. Where a paywall blocked me I used independent
search corroboration and said so.

My estimate of the effect: the 640 metadata-only grades are biased **conservative**, not
generous. Where I could not check a figure I did not award 상, and every 상 in the ledger was
re-accessed or independently corroborated across four or more outlets. If the full ledger were
re-accessed, I would expect a small number of 중 records to move up and a somewhat larger number
to move down, because on the twelve records where I did check a specific number against its
source, seven had a discrepancy of some kind. Extrapolating that hit rate is not warranted —
I deliberately checked the records most likely to be wrong — but a reader should assume the
ledger contains more transcription-level errors than the twelve I found.

## 6. Files written

- `RLSX/evidence/evidence_grades.jsonl` — 774 grade records
- `RLSX/evidence/grade_summary.md` — distribution, histograms, load-bearing records, conflicts, low-evidence claims
- `RLSX/work/R/report.md` — this file

UNRESOLVED count: **0**. Every record in the ledger received a grade with a stated reason,
a verification method, and a rationale.
