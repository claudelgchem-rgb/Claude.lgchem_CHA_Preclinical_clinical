CHARTER_ACK: R1,R2,R3,R4

# Agent X — 반증 레드팀 / Falsification Red Team — methodology and residual doubt

Deliverables: `RLSX/audit/redteam_findings.md` (20 findings), `RLSX/audit/redteam_mapping.csv` (20 rows), `RLSX/evidence/parts/X.jsonl` (39 records, **E-9500 … E-9538**), this report, `RLSX/work/X/unresolved.csv` (6 records).
All evidence carries `confidence: null`, `graded_by: null` per R3. Agent R grades.

---

## 1. Methodology

**The failure mode I was hired to catch.** Seven agents shared one brief, one search tool and one literature, and reached agreement in a single pass. That is the exact configuration in which correlated error is most likely: the agents can be individually careful and jointly wrong in the same direction, because they inherited the same framing of the question and the same candidate answer set. So I did not audit their arithmetic. I attacked their *estimator* and their *scope*, on the theory that in a fast-converging multi-agent run the error is almost never in a number and almost always in what the number is conditioned on.

**Three rules I imposed on myself.**

1. *Build the case for the position the run rejected, before judging it.* Workstream 1 asked me to argue **for** H0-a. I did that for four findings (X-01 to X-04) before letting myself write a verdict, and one of those four (X-04) came out against the position I was constructing. That is the control: an adversary who only finds what the brief hinted at is a second consensus agent wearing a costume.
2. *Do not reuse the attacked agents' evidence to attack them.* Every quantitative claim in the findings document traces to a record in `X.jsonl` that I collected in this session. Where I agree with an upstream agent (X-15, X-17) I say so and cite their finding by description rather than importing their evidence IDs as if they were mine.
3. *A verdict of 기각 is a deliverable, not a failure.* Five attacks failed. Each has a stated reason, and two of them (X-04, X-06) produced evidence that makes the consensus stronger than the consensus itself had made it.

**Search record.** 38 WebSearch/WebFetch calls. Four fetches were blocked (BCG 403, Science 403, OECD 403, Nature IdP 303 redirect) and each was replaced by an independently reachable carrier of the same datum. One PDF that the fetch tool could not parse (L.E.K.) was extracted locally with Python `zlib` and `re` from the standard library, and the extracted figures were then confirmed against the publisher's own HTML page before being recorded, which is why E-9509 carries two provenance hops.

**Verdict discipline.** 채택 means the consensus is wrong and a named sentence must change. 부분채택 means the finding survives but its scope, comparator or trend statement is wrong. 기각 means the attack was genuine and failed. Totals: **채택 3, 부분채택 12, 기각 5.**

---

## 2. Which attacks I judge strongest, in order

**Strongest: X-08 — the base-rate ceiling is time-blind.** This is the only finding where the consensus is not merely under-qualified but produces a wrong answer to a question the mission explicitly asks. The mission asks for ranked bottlenecks at 2030, 2035 and 2040. The consensus caps AI's system effect using a 2026 share. The cumulative count of AI-derived clinical-stage molecules has a doubling time of 1.2-2.1 years across four independent anchors [E-9516][E-9517], which puts the share above 10 percent between 2029 and 2033 and above 50 percent between 2032 and 2039 [E-9518]. A ceiling argument that is correct in 2026 and silently applied to 2040 is the single most likely way this report ends up wrong in print.

**Second: X-14 — an internal contradiction the run did not notice.** Agent C ranks B15 fifth using the biomarker qualification queue. Agent E, in the same run, reports that FDA's public table lists over 200 surrogate endpoints that have already served as a basis of approval [E-9528]. Two agents measured two different resources and only one of them is the constraint. This is the clearest evidence that the run's convergence was partly nominal: the agents agreed on a ranking while holding incompatible views of what one of the ranked items is.

**Third: X-01 — the estimator is blind to the suppressed population.** Every H0-a test in the run is conditioned on a programme having started. About 85 percent of the druggable genome has never yielded an approved drug [E-9536][E-9501], and KRAS spent 39 years between validated target and first drug with no programme in the statistics for most of them [E-9502]. I cannot close this hole with evidence, because the counterfactual is not recorded anywhere, and that is precisely why the report must not state the H0-a rejection without it.

**Fourth: X-13 — the jurisdiction question, resolved in both directions.** The orchestrator flagged this as live and it is. China took 39 percent of global oncology trial starts in 2024 against the US at 32 percent, with Phase I trials about half as long and 43 percent cheaper on an 87-day trial-approval clock [E-9520], and its registrations grew about 16 percent per year to 4,900 in 2024 [E-9519]. That genuinely raises the early-phase ceiling above the US-derived figure. But the global aggregate is not growing — investigators down about 9 percent and coordinators down about 28 percent over six years [E-9524], flat registry inflow [E-9533] — and the pivotal gate did not move, since a China-only pivotal trial was rejected 14-1 on generalisability grounds [E-9523] and only 337 of 2,539 Chinese innovative-drug trials in 2024 were multiregional [E-9519]. The resolution is that the constraint is **pivotal multiregional trial capacity**, which is a sharper and more useful statement than either "US capacity binds" or "flow just routes east".

**Fifth: X-09 — the comparator does the work.** Against the historical 37 percent benchmark the AI Phase II figure is +3 points; against the contemporaneous 28 percent it is +12 [E-9537][E-9513]. Agent B's power calculation is correct arithmetic on the wrong comparator. This does not make AI look good — it makes the evidentiary state indeterminate, which is a different and more defensible claim than "no evidence".

---

## 3. Where I think the consensus is most likely wrong even though I could not prove it

Three places. I state them as residual doubt rather than as findings, because in each case I built the attack, could not close it with evidence, and did not want to smuggle an unproven claim into the mapping file.

**(a) The elasticity framework may be measuring the wrong system.** The brief defines a rate-limiting step as one whose improvement raises *annual approved new drugs*. Every agent adopted this and computed elasticities against it. But approvals are a count of regulatory events, and the quantity the field actually cares about is health produced. A ranking optimised for approvals will systematically over-rank whatever raises the count of small, rare-disease, single-arm approvals and under-rank whatever raises the size of the effect in common disease. Agent E's own evidence points at this: two of Japan's five conditional approvals were withdrawn after confirmatory failure, so that route added approvals and then removed them. I could not find a published elasticity of health outcome to any pipeline factor — this is logged as UNRESOLVED X-U3 — so I could not quantify the distortion. My belief is that it is material and that it tilts the whole ranking toward B15, B4 and B5 and away from B1 and B8.

**(b) The run treats "AI" as one technology with one adoption curve, and it is at least two.** Structure prediction and generative chemistry are the ones the run measured. The larger near-term effect may be in the part nobody measured: AI applied to *clinical* decisions — patient selection, dose finding, endpoint construction, trial design. Agent F measured AI trial-matching and found it moves screening cost and not accrual, which is real but is a narrow slice. Nothing in the run tests whether AI raises the quality of the design decisions in my X-19 finding, where a 48 percent Phase III dose-modification rate [E-9531] says the decisions are currently poor. If the largest AI effect lands there, the run's Amdahl arithmetic — which caps AI by discovery's share of time and cost — is bounding the wrong quantity, because a clinical-design improvement is not subject to the discovery-share ceiling at all. I could not find a measurement, and it is logged as UNRESOLVED X-U2.

**(c) The consensus may be right about 2026 and wrong about the direction of travel.** Three independent series in my evidence point the same way and no agent assembled them together: cumulative likelihood of approval fell 10.4 to 6.7 percent between the 2014 and 2024 analyses [E-9512]; Phase I success fell from over 75 percent to below 40 [E-9513]; and novel targets entering the pipeline fell from about 100 a year to 30 in 2024 while the pipeline doubled and venture funding tripled [E-9509]. Read together these describe a system that is not merely constrained downstream but is *retreating upstream* — placing fewer novel bets, on more crowded targets, with falling returns per bet. If that is the operative dynamic, then the binding constraint by 2035 is neither discovery capability nor clinical capacity but **the industry's declining willingness to prosecute novel biology**, which is a behavioural and returns-driven variable that appears in the catalogue only as a fragment of B11. I flagged the B11 relabelling in X-10, but I could not establish causality between falling returns and falling novel-target entry, so I did not raise it to a finding. I regard it as the most likely single place the final report will look wrong in five years.

---

## 4. What I did not attack, and why that is a limitation

I did not attack Agents I and D, whose reports were not on disk when I ran; the orchestrator has scheduled that for a second pass together with the circular-reference provenance audit. Within the seven reports I did read, I processed every one of the four assigned workstreams in full: H0-a from the pro side (X-01 to X-04), the forward claim (X-05, X-06), AI compression from both directions (X-07, X-08, X-09), the spare-capacity test on B1, B8, B11, B2, B7, B15 and B3 (X-10, X-11, X-12, X-14, X-15, X-16, X-17), the reverse test for under-ranked candidates (X-18, X-19), and the jurisdictional-routing question the orchestrator added (X-13), plus one scope correction on the regulatory verdict (X-20). B8 is covered inside X-12 and X-19 rather than in an entry of its own: my spare-capacity attack on B8 failed at the first test, because the one documented case of a toxicity-adjacent attrition class being retired — pharmacokinetic failure, 40 percent to 10 percent between 1991 and 2000 [E-9506] — is a case of the class being *replaced* by safety and efficacy rather than of slack appearing, and the dose-optimisation evidence [E-9531] shows the surviving class is being actively worked and is not slack.

---

## 5. UNRESOLVED

Six items, fully recorded in `RLSX/work/X/unresolved.csv` with every query attempted, the failure reason, at least three alternative sources tried, and a best estimate with its basis. In summary: a year-by-year AI-derived IND series from a regulator rather than a census (X-U1); any measurement of AI's effect on clinical design decisions (X-U2); a published elasticity of health outcome, rather than approval count, to a pipeline factor (X-U3); a count of programmes started that would not have been started absent AI structure prediction (X-U4); the exact current entry count of FDA's surrogate endpoint table (X-U5); and a like-for-like China-versus-US comparison of registrational rather than total trial capacity (X-U6). None of the six changes any verdict in the findings document; X-U4 is the one that would most sharpen X-01, and X-U3 is the one that would most sharpen the residual doubt in section 3(a).
