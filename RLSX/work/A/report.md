CHARTER_ACK: R1,R2,R3,R4

# Agent A — Stage Economics Quantification (S1–S9, T/C/P)

Deliverables: `RLSX/data/stage_economics.csv` (141 rows), `RLSX/evidence/parts/A.jsonl` (64 records, E-1001–E-1100), this report, `RLSX/work/A/unresolved.csv` (12 records).
Evidence grading is not performed here. Every record carries `confidence: null`, `graded_by: null`, `grade_reason: []` for Agent R (R3).

---

## 1. Methodology

**Sources.** Every number in the CSV traces to a URL that was actually fetched in this session. Where a publisher wall or a raster-only PDF blocked the original, the fetch chain is written into `provenance_hops` and the shortfall is written into `unresolved.csv` with the full query list, the failure code, the alternative sources attempted, and the best estimate that survives.

**Three cost bases are never mixed (M1).** Every C row carries `cost_basis` ∈ {out_of_pocket, risk_adjusted, capitalized} and `coc_included`, and every capitalized row carries the discount rate. This matters more than any single number: Sertkaya et al. report 172.7, 515.8 and 879.3 USD million for the *same drug in the same model* depending only on whether failures and cost of capital are loaded in [E-1011]. A figure quoted without its basis is not a measurement.

**No averaging across methodologies.** Section 3 presents seven whole-programme cost estimates side by side with the mechanical reason each differs. They are never combined.

**Denominators are recorded, not assumed (M3).** The published success rates disagree mainly because they count different things. Path-by-path counts every drug–indication–sponsor path separately [E-1020]; the BIO family counts registration-enabling programmes [E-1023]; Hay weights lead indications [E-1022]; Zhou merges all trials for one drug–indication into one programme [E-1027]. Each CSV row states which.

**Modality and region (M5, M6).** Where a source decomposes, the row carries the modality or region. Where it does not, the row says `not_decomposed` and the notes column says the source does not decompose. No split has been invented.

**Derived rows.** Ten derived records (E-1090–E-1100) carry `type:"derived"`, the arithmetic written out, and every input evidence ID.

---

## 2. Stage-by-stage T / C / P

### T — duration

| Stage | Duration | Source |
|---|---|---|
| S1 target-to-hit | 12 months | Paul 2010 [E-1017] |
| S2 hit-to-lead | 18 months | Paul 2010 [E-1017] |
| S3 lead optimisation | 24 months | Paul 2010 [E-1017] |
| S4 preclinical (Paul, narrow) | 12 months | [E-1017] |
| S4 synthesis → first-in-human (DiMasi) | 31.2 months | [E-1005] |
| S4 nonclinical (Sertkaya) | 31.2 months | [E-1014] |
| S5 Phase I | 33.1 mo (DiMasi) / 27.8 mo (Sertkaya) / 1.6 y median trial (Wong) / 2.3 y interval (BIO) | [E-1005][E-1014][E-1021][E-1025] |
| S6 Phase II | 37.9 / 34.0 mo; 2.9 y median trial; 3.6 y interval | [E-1005][E-1014][E-1021][E-1025] |
| S7 Phase III | 45.1 / 38.0 mo; 3.8 y median trial; 3.3 y interval | [E-1005][E-1014][E-1021][E-1025] |
| S8 review | 16.0 / 16.2 mo model; FDA 356 d, EMA 430 d, PMDA 290 d observed 2024 | [E-1005][E-1014][E-1032] |
| S9 Phase 4 | 36.6 months | [E-1014] |

Whole-programme: about 128 months synthesis-to-approval on the DiMasi clock [E-1005]; about 13.1 years on the DiMasi pre-IND clock plus the BIO clinical intervals [E-1100]; and about 8 years from IND authorisation to approval, essentially unchanged 1983–2018 [E-1029].

**Cycle time between phases (the under-reported part).** Tufts CSDD found 82 percent of non-expedited programmes approved 2008–2018 carried an average 17 months of white space between Phase II and Phase III, with the other 18 percent overlapping the two phases; the Phase I-to-II gap was not reliably measurable [E-1036]. The BIO inter-phase intervals already contain this white space, which is why they exceed the median trial durations from Wong/Siah/Lo [E-1025][E-1021]. One industry analysis puts mean clinical cycle time at 100 months in 2024, seven months longer than 2020 [E-1037]. ⚠ LOW-EVIDENCE CLAIM — E-1037 is sponsored content with an undisclosed sample and is used here only as a direction indicator, never as a load-bearing input.

On the regulator's side, 30 percent of the EU centralised procedure's 430 median days in 2024 is sponsor clock-stop time, not agency assessment: validation 24 days, CHMP assessment 216, company response 128, Commission decision 56 [E-1034]. [INFER] A material share of what is colloquially called "regulatory delay" is sponsor response latency, and would not move if the agency worked faster.

### C — cost

Per-stage cash outlay, pooled modalities, Sertkaya 2024: nonclinical 11.8, Phase 1 7.1, Phase 2 21.0, Phase 3 89.3, FDA review 2.6 USD million (2018) [E-1012]. DiMasi's per-compound clinical costs split by molecule size: Phase I 25.53 small / 23.93 large, Phase II 50.40 / 91.86, Phase III 245.80 / 281.13 USD million (2013) [E-1004]. ASPE per-study costs range 7.0–19.6 million for Phase 2 and 11.5–52.9 million for Phase 3 by therapeutic area [E-1052].

Where a year's actual industry cash goes, from PhRMA's 2022 functional split: pre-human 15.9 percent, Phase I 8.5, Phase II 11.1, Phase III 28.8, approval 4.3, Phase IV 11.5, uncategorised 20.0 [E-1042]. Excluding uncategorised, pre-human is 19.9 percent and Phase III alone is 36.0 percent [E-1099].

Therapeutic-area dispersion is larger than most modality effects: Sertkaya finds 378.7 million (anti-infectives) to 1756.2 million (pain and anaesthesia) capitalized, oncology 1209.2 [E-1016]; Wouters finds 2771.6 million median for antineoplastic/immunomodulating against 765.9 for nervous system [E-1008].

S9 unit economics by modality: autologous CAR-T cost of goods about 95,780 USD per dose with a 3–5 week vein-to-vein turnaround of which roughly 14 days is QC release [E-1046]; a 200-litre cGMP AAV batch about 2 USD million at a US CDMO [E-1047]. ⚠ LOW-EVIDENCE CLAIM — both are model-based industry figures with undisclosed samples.

### P — probability

Per-stage transition probabilities (S4→S8) and cumulative probability to approval are in the CSV for six independent studies. The consolidated picture:

| Stage | Transition range | Cumulative to approval |
|---|---|---|
| S4 preclinical → Ph I | 68–69 % [E-1015][E-1018] | 8.1–8.5 % [E-1097][E-1015] |
| S5 Phase I → II | 47–66.4 % [E-1026][E-1020] | 5.5–13.8 % [E-1027][E-1020] |
| S6 Phase II → III | 28–48.6 % [E-1027][E-1020] | 15.1–21.7 % [E-1096][E-1097] |
| S7 Phase III → filing | 55–65.5 % [E-1026][E-1015] | 52.4 % [E-1096] |
| S8 filing → approval | 88.3–92 % [E-1015][E-1026] | 88.3–92 % |

Phase II is the lowest-transition stage in every source examined, and the anchor holds [E-1023][E-1027][E-1015][E-1018][E-1022]. The regulatory step is the *highest*-transition stage in every source: about nine in ten filed dossiers are approved [E-1023][E-1015][E-1026].

Modality decomposition of Phase I likelihood of approval, BIO 2011–2020: CAR-T 17.3 (n=67), RNAi 13.5 (70), mAb 12.1 (2136), ADC 10.8 (184), gene therapy 10.0 (96), vaccine 9.7 (316), protein 9.4 (800), peptide 8.0 (619), small-molecule NME 5.7 (6803), antisense 5.2 (162) [E-1024]. Rare disease 17.0 versus chronic high-prevalence 5.9; oncology 5.3 versus non-oncology 9.3; biomarker-selected 15.9 versus 7.6 [E-1025]. Wong/Siah/Lo independently find oncology 3.4 versus non-oncology 20.9, and biomarker 10.3 versus 5.5 [E-1021].

[INFER] The modality cells with the highest success rates are the smallest and the most concentrated in rare and biomarker-defined indications, which is precisely the population where the BIO report separately shows 17.0 percent LOA. Reading CAR-T's 17.3 percent as evidence that the modality is intrinsically more developable confounds modality with indication selection.

---

## 3. Competing whole-programme cost estimates, presented in parallel

| Estimate | Value | Basis | Discount rate | Sample | Why it differs |
|---|---|---|---|---|---|
| DiMasi 2016 [E-1001][E-1002] | 1395 OOP / 2558 capitalized / 2870 incl. post-approval (2013 $) | risk-adjusted and capitalized | 10.5 % | 106 compounds, 10 firms, confidential survey | Confidential self-reported survey; assumes preclinical is 42.9 % of capitalized cost [E-1090] |
| Paul 2010 [E-1019] | 873 OOP / 1778 capitalized | risk-adjusted and capitalized | 11 % | 13 large-pharma portfolios | Model of a work-in-process pipeline, not a per-drug audit |
| Wouters 2020 [E-1006] | 985.3 median / 1335.9 mean capitalized | capitalized | 10.5 % | 63 of 355 approvals 2009-18, 47 companies, SEC filings | Same discount rate as DiMasi, so cost of capital does not explain the gap. Public filings, and the observed preclinical share is 12.4 % not 42.9 % [E-1007] |
| Sertkaya 2024 [E-1011] | 172.7 OOP / 515.8 risk-adjusted / 879.3 capitalized (2018 $) | all three, reported separately | 11 % | model from trial-level costs × transition probabilities, 2000-18 | Bottom-up per-trial costing rather than firm-reported programme spend |
| Prasad & Mailankody 2017 [E-1009] | 648.0 median / 757.4 with opportunity cost | out-of-pocket and capitalized | 7 % | 10 single-product cancer companies | Lower discount rate and a sample whose portfolio failures are structurally limited |
| Sabatini & Chalmers 2023 [E-1045] | 1943 for cell/gene therapy | capitalized | not recoverable | 25 assets identified, 11 costed | Different modality entirely |
| Light & Warburton 2011 [E-1010] | 59.4 median | out-of-pocket, net of tax relief and public subsidy | none applied | reanalysis of DiMasi inputs | Median not mean; deducts tax relief and public subsidy; applies no cost of capital |

**Why they diverge, mechanically.** Four independent levers, none of which is a disagreement about biology: (i) *cost basis* — Sertkaya's own three figures span 5.1× on one dataset [E-1011]; (ii) *discount rate* — 7 percent versus 10.5–11 percent [E-1009][E-1001][E-1011]; (iii) *preclinical share assumption* — 42.9 percent assumed [E-1090] against 12.4 percent observed in filings [E-1007]; (iv) *sample frame* — a confidential 10-firm survey [E-1001] against public filings [E-1006], single-product companies [E-1009], or a bottom-up trial-cost model [E-1011].

**Verdict on the $2.558B anchor.** The figure is correctly attributed and internally consistent [E-1001], but its sample is a confidential survey of 106 compounds from 10 firms that cannot be independently reproduced, and its largest single structural assumption — that preclinical work is 42.9 percent of capitalized cost — is contradicted by the only study that measured the preclinical share directly from filings, which found a median of 12.4 percent across 19 products [E-1007][E-1090]. [INFER] The anchor should be reported as one estimate in a published range spanning roughly 0.06B to 2.9B depending on basis, discount rate and sample, not adopted as *the* cost of a drug.

---

## 4. Derived: pre-IND versus clinical share (feeds H0-c)

**Capitalized cost.** DiMasi: 1098 / 2558 = **42.9 %** pre-IND [E-1090]. Sertkaya: **40.2 %** [E-1013]. Two independent models agree.

**Out-of-pocket cost.** DiMasi: 430 / 1395 = **30.8 %** [E-1091]. Sertkaya: **6.8 %** [E-1013]. Wouters, observed in filings: **12.4 %** median, range 0.3–50.7 [E-1007]. PhRMA, single-year industry outlay: **15.9 %**, or 19.9 % of categorised spend [E-1042][E-1099]. Range 6.8–30.8 modelled, 12.4 observed.

**Elapsed time.** DiMasi: 31.2 / 128.0 = **24.4 %** [E-1093]. Sertkaya: 31.2 / 147.2 = **21.2 %** [E-1093]. Paul, whose clock uniquely starts at target selection: 66 / 162 = **40.7 %** [E-1093]. BIO clinical intervals plus the DiMasi pre-IND clock: about **19.8 %** [E-1100].

**Regulatory review share of elapsed time.** 16.0 / 128.0 = **12.5 %** (DiMasi) and 16.2 / 147.2 = **11.0 %** (Sertkaya) [E-1095].

**The Amdahl ceiling [E-1094].** If pre-IND work took zero time and zero money:
- maximum reduction in total elapsed development time: **21–41 %**;
- maximum reduction in capitalized cost per approval: **40–43 %**;
- maximum reduction in actual cash outlay per approval: **7–31 %**, and about 12 percent on the only directly observed measurement [E-1007].

[INFER] The capitalized ceiling is not fully attainable even in principle. A large part of the pre-IND capitalized burden is compound interest accruing on money spent early and on the attrition that occurs later; that interest shrinks only if either the *total* timeline shortens or the downstream probability of success rises. Making discovery instantaneous removes the pre-IND *duration* from the compounding horizon but does nothing to the clinical attrition that the compounding is applied to. This is exactly the H0-b distinction: compressing discovery *duration* and raising *PoS* are separate levers, and only the second one attacks the dominant term.

---

## 5. Approvals and R&D spend, 2000–2025

**Approvals.** US novel drug approvals 2000–2024: 29, 29, 23, 27, 36, 20, 22, 18, 25, 26, 21, 30, 39, 27, 41, 45, 22, 46, 59, 48, 53, 50, 37, 55, 50 [E-1038]. CDER approved 46 novel drugs in 2025 (34 NMEs, 12 biologics) [E-1040]. The broader CDER-plus-CBER series for the same years runs 46, 35, 27, 36, 38, 27, 29, 24, 32, 34, 28, 37, 47, 37, 51, 57, 30, 58, 66, 55, 58, 60, 45, 72, 62 [E-1039]. Darrow et al. independently give decade means of 34 (1990s), 25 (2000s) and 41 (2010–2018) [E-1030].

**R&D spend.** PhRMA member company R&D, nominal: 26,030.8 (2000), 50,709.8 (2010), 91,126.3 (2020), 100,845.2 million (2022) [E-1041]; R&D as a share of sales rose from 16.2 percent in 2000 to 19.1 percent in 2022 [E-1043].

**The ratio.** Novel approvals per billion nominal PhRMA R&D dollars: 1.11 (2000), 0.41 (2010), 0.58 (2020), 0.37 (2022) [E-1098].

**What this does and does not show.** It shows that approval counts and R&D outlay both rose, and that the count rose far less than the outlay in nominal terms [E-1038][E-1041]. It shows the approval count in the 2010s and 2020s is materially above the 2000s trough [E-1038][E-1030]. It does **not** show productivity, for three reasons written into E-1098: the ratio is in nominal dollars with no deflator; the numerator counts approvals from all sponsors while the denominator covers PhRMA members only, and the non-member share of approvals has grown; and spend in year *t* does not produce the approval in year *t*, so a ratio of contemporaneous series has no causal reading. The Ringel "Breaking Eroom's Law" paper argues the exponential efficiency decline had already reversed, but its series are raster figures and no numeric values could be recovered, so no number from it is asserted here [E-1044].

**Regional context.** 2024 new active substance approvals: FDA 56, PMDA 53, Swissmedic 37, EMA 34, TGA 33, Health Canada 24 [E-1033]; NMPA approved 228 NDAs in 2024 on a broader denominator that includes traditional Chinese medicines [E-1049]. 2024 median approval times: PMDA 290 d, FDA 356, Health Canada 363, TGA 369, EMA 430, Swissmedic 444 [E-1032]. Korea's MFDS targets a cut from about 420 to about 295 days from January 2025 [E-1051].

---

## 6. Bearing on H0-a and H0-c

**H0-a — was discovery actually the historical rate-limiting step?** The evidence collected here points against it, and the strongest single item is a natural experiment on the regulatory step rather than the discovery step.

1. *Attrition is overwhelmingly clinical, not pre-clinical.* In the only model that resolves discovery explicitly, the three discovery stages together retain 51 percent of projects (0.80 × 0.75 × 0.85) while Phase II alone retains 34 percent [E-1018]. Cumulative probability from target selection is 4.1 percent and from Phase I entry is 11.7 percent [E-1097]: about 65 percent of all lifetime attrition happens after the molecule enters humans. Every other source agrees that Phase II is the low point [E-1023][E-1027][E-1015][E-1022].
2. *Cash is overwhelmingly clinical.* On PhRMA's measured 2022 outlays, pre-human work is 15.9 percent of member R&D and Phase III alone is 28.8 percent [E-1042]. On Sertkaya's bottom-up model, nonclinical is 6.8 percent of cash outlay [E-1013]. Wouters measured 12.4 percent median directly from filings [E-1007]. Only the capitalized basis makes pre-IND look large (40–43 percent), and that is an artefact of discounting and attrition loading, not of where cash is spent [E-1090][E-1013].
3. *Time is majority clinical.* Pre-IND is 21–41 percent of elapsed time depending on where the clock starts [E-1093].
4. *The decisive counter-evidence.* FDA review time fell from more than three years in 1983 to under one year in 2017, and total time from clinical-testing authorisation to approval did not move — it stayed at about eight years [E-1029]. [INFER] This is the closest thing the field has to a controlled test of the constraint definition in the brief. A very large, sustained improvement was delivered at one step (S8), and total system throughput in the time dimension did not respond. By the brief's own definition — a step whose improvement raises total output — S8 was demonstrably not the constraint, and the same logical test must be applied to S1–S3 before H0's premise can be accepted.
5. *Corroborating detail on S8 as a non-constraint.* Filing-to-approval probability is 88–92 percent [E-1015][E-1023][E-1026], review is 11.0–12.5 percent of elapsed time [E-1095], the approval phase is 4.3 percent of R&D outlay [E-1042] and 2.6 million per stage attempt [E-1012], and 30 percent of the EU procedure's clock is sponsor response time [E-1034]. On all four axes B5 has spare capacity rather than binding scarcity.

[INFER] Nothing collected here establishes that discovery *was* the historical constraint, and several independent lines establish that the clinical stages dominated cost, time and attrition throughout the period for which stage-resolved data exist (roughly 1990–2024). H0's premise should be treated as unsupported by the stage economics, pending the elasticity work in M2.

**H0-c — the Amdahl ceiling.** Quantified in section 4 and in E-1094: at most 21–41 percent of elapsed time, at most 40–43 percent of capitalized cost, and at most 7–31 percent of actual cash cost, with the only direct measurement of the cash share at 12.4 percent [E-1007]. [INFER] Under the highest-time-share model (Paul, 40.7 percent), instantaneous discovery would take a 13.5-year programme to about 8.0 years; under the DiMasi timeline it would take 128 months to about 97 months. In neither case does the pipeline become fast, and in neither case does the dominant attrition term (Phase II, 28–36 percent transition) change at all [E-1023][E-1027][E-1015]. The ceiling is real but bounded, and it binds hardest on the axis (capitalized cost) that is an accounting construct rather than on the axes (cash, time, PoS) that determine whether more drugs reach patients.

**Bearing on H0-d.** The stage economics point inside "preclinical/clinical" to Phase II efficacy attrition as the largest single term (B1, B2, B8), Phase III cash as the largest single cost term (B3), between-phase white space of 17 months as a pure-waste time term (B3), and modality-specific manufacturing unit economics as the S9 term (B6). They point away from B5 as a constraint on T or P.

---

## 7. UNRESOLVED

12 records in `RLSX/work/A/unresolved.csv`, each with the full query list, the failure reason, at least three alternative sources attempted, and a best estimate with its basis. Summary:

1. DiMasi 2016 full text — publisher 403, mirror 503 ×2. Headline figures verified from the Duke Scholars abstract record; per-stage split corroborated to the decimal by Wouters' independent statement of the 42.9 percent assumption.
2. Hay 2014 full text — Nature auth redirect, mirror 403. Figures recovered from a compilation and independently confirmed by Wong/Siah/Lo's citation of the 10.4 percent.
3. BIO 2011-2020 PDF — image-only text layer. All figures recovered from a page-by-page mirror.
4. Ringel 2020 numeric series — raster figures. No number asserted; the approvals-per-R&D ratio is built from two primary series instead.
5. Light & Warburton full text — Springer auth redirect. Objection verified; the 59.4 million figure is flagged `circular_risk` and used only as a range endpoint.
6. Sabatini & Chalmers full text — Springer auth redirect. Headline 1943 million recorded with `circular_risk`; discount rate left blank rather than guessed.
7. CBER annual series — FDA pages 403/401. Combined CDER+CBER series recovered in full; CBER implied by subtraction and flagged as arithmetic rather than asserted.
8. Korea MFDS annual counts — report is a Korean-language attachment. Korea represented by the verified 420→295 day reform target; PMDA carries the JP-KR quantitative anchor.
9. NMPA comparable median review time — Wiley 403, Nature auth redirect, NMPA outside the CIRS panel. The 12–18 month figure is labelled a target, not a median.
10. Per-stage cost by all seven modalities — no published source does this. Modality signal is established on the P axis (ten modalities, E-1024) and on unit manufacturing economics, not on stage cost. Nothing invented.
11. Phase I→II white space — Tufts states it is not reliably measurable. Implied bound of about 8 months given as a bound only; the measured 17-month Phase II→III value is what enters the CSV.
12. Sertkaya Phase 4 cost cell — did not extract; ASPE sources 403. Phase 4 duration (36.6 months) and PhRMA's 11.5 percent Phase IV outlay share carry the S9 cost signal.
