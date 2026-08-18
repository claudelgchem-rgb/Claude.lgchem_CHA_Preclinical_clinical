CHARTER_ACK: R1,R2,R3,R4

# Agent F — Clinical Operations, Patients and Trial Design

Evidence block: **E-5001 … E-5076** (69 records) in `./RLSX/evidence/parts/F.jsonl`.
Structured data: `./RLSX/data/trial_ops.csv` (81 rows).
Confidence grading is deliberately absent from every record I created (`confidence: null`, `graded_by: null`) per R3; Agent R grades.

---

## 0. Methodology

**Scope.** Bottlenecks B3 (recruitment / site capacity) and B4 (precision-medicine patient-pool fragmentation), with spillover records into B5 where regulatory acceptance of a mitigation technology is the binding fact.

**Source hierarchy applied.** Registry-derived peer-reviewed analyses (AACT / ClinicalTrials.gov) first; then regulator documents; then Tufts CSDD and CTTI-class benchmarking; then trade and vendor material, which is recorded as `secondary` or `market_report` with the vendor named in `authors_or_org` so Agent R can apply S4. No effect-size claim originating from a vendor is presented anywhere in this report as a measured effect; each is labelled in `effect_confidence_basis`.

**Search record.** 33 WebSearch/WebFetch calls. Four primary sources were unreachable by the available tooling and are logged in `unresolved.csv` with the queries tried, the alternate routes attempted, and a best estimate.

**Trial-level vs programme-level.** Every mitigation row in the CSV carries an explicit note distinguishing the two. A platform trial that halves time-per-arm shortens a *portfolio's* aggregate timeline only if ten candidates are simultaneously ready for the same platform; it does not shorten one sponsor's single-asset programme [INFER, reasoning on E-5034].

**Denominator discipline (M3).** Where I combine medians drawn from different samples — which I do twice, for the Amdahl bound and for the site-skew figure — the derived record states the mismatch explicitly and labels the result an order-of-magnitude bound rather than a within-sample ratio (E-5060, E-5073).

**Bias control (R4).** I did not treat H0 as true. H0 predicts clinical becomes rate-limiting *after* AI compresses discovery. My assignment tests one necessary condition of that prediction — whether clinical operations capacity can absorb increased candidate flow — and I report below that the answer is unfavourable to system throughput regardless of whether H0's discovery premise holds. That is a finding about capacity, not a validation of H0's historical claim, which is Agent D's territory.

---

## 1. Enrollment delay: the actual numbers

**Duration and its trend.** Median recruitment duration for industry-sponsored phase III drug trials was 13 months in 2008–2011, 13 months in 2012–2015 and 18 months in 2016–2019 (p = 0.0068) — a 38% lengthening [E-5001]. Over the same window median sites per trial went 51 → 43 → 64 [E-5002], median participants per site per month halved from 0.8 to 0.4 [E-5003], and enrollment rate per trial drifted from 26 to 20 patients/month, non-significantly [E-5004]. The authors' own summary is that phase III recruitment is less effective than twelve years earlier [E-5001].

The internal structure of that finding matters more than the headline. Sponsors did not lose the ability to enroll patients; they bought the same throughput by activating 49% more sites, each of which produced half as much [INFER on E-5002, E-5003]. That is capacity purchased through extensive rather than intensive margin — and the extensive margin is the one that runs out.

**Failure to meet targets.** In 2,542 randomised trials registered 2010–2014, roughly one in five completed within the planned timeframe, the median delay was 12.2 months, and fewer than half met the prespecified enrollment target [E-5010].

**Termination attributed to accrual.** Of 7,646 ClinicalTrials.gov records with posted results, about 12% (905) were terminated, and insufficient accrual was the single largest stated cause: 39% of all terminations (350/905) and 57% of the "other reasons" subgroup [E-5007]. Cardiovascular trials registered 2006–2015 replicate this independently at 41% of non-completions [E-5008]. In the NCI network, 145 of 787 phase II/III trials (18%) closed under-accrued or were still below 50% of target three years after opening, after excluding closures for toxicity or interim results [E-5009]. Recruitment therefore destroys trials as well as delaying them, which means B3 carries a probability-of-success component and not only a time component [E-5076].

**Counter-evidence, recorded rather than suppressed.** Tufts CSDD benchmarking comparing 2012, 2019 and 2023 sponsor-contributed data found that in the most recent cycle actual enrollments *exceeded* planned enrollments for a majority of studies and timelines were *shorter* than expected [E-5026]. This directly contradicts the registry trend. The most likely reconciliation is selection: sponsor-contributed benchmarking samples the studies sponsors choose to submit, and "planned" is a sponsor-set target that can be revised downward, whereas the registry series measures elapsed calendar time against a fixed clock [INFER]. I flag the tension rather than resolving it in favour of my other data.

### The Amdahl bound on B3 — the ceiling on what fixing recruitment can buy

This is the number the assignment asks for, and it constrains every claim anyone makes about recruitment being "the" bottleneck.

Median completed phase 3 elapsed length on ClinicalTrials.gov across 2016–2019 was (882 + 864 + 921.5 + 937)/4 = 901.1 days = **29.6 months** [E-5011]. Median recruitment duration over the identical window was **18 months** [E-5001].

> **18 / 29.6 = 60.8%** of a median phase III trial's elapsed calendar time is spent recruiting [E-5060].

Caveat carried in the record: the two medians come from different samples (E-5001 restricts to industry phase III drug trials with usable recruitment dates, n = 606; E-5011 covers all completed phase 3 registrations), so this is an order-of-magnitude bound, not a within-sample ratio [E-5060].

Scaling to the clinical programme. Registry medians for 2018–2019 give phase 1 ≈ 368.75 d, phase 2 ≈ 983.5 d, phase 3 ≈ 929.25 d; strictly sequential that is 2,281.5 days = **6.25 years** of clinical elapsed time [E-5011].

- **Lower bound.** Eliminate phase III recruitment only: 0.608 × 929.25 = 565 d = 1.55 yr saved = **24.8% of clinical elapsed time**, or **14.7%** of a 10.5-year total programme [E-5071].
- **Upper bound.** Assume the same 60.8% enrollment share in phases I and II: 3.80 yr saved = **60.8% of clinical elapsed time**, or **36.2%** of a 10.5-year programme [E-5071].

So instantaneous, costless, perfect recruitment — a physical impossibility — removes somewhere between 15% and 36% of total development time. That is a large number, but it is bounded, and it is a *time* effect. It does not raise the probability that a molecule works. This is the Amdahl discipline B3 must be held to [INFER].

Note also that phase 2 median elapsed length exceeds phase 3 in every year 2015–2023 [E-5011], which cuts against the common framing of phase III as the long pole.

---

## 2. Screen failure and eligibility

**Screen-failure rates.** Early-phase oncology units at three French cancer centres reported 21.7%, 21.4% and 26.4% screen failure, with causes distributed radiological 29.2%, biological 23.8%, clinical 22.3%, performance-status deterioration 11.9%, administrative 10.9% [E-5013]. Compiled operations benchmarks put the typical oncology range at 20–30%, with phase III prostate ≈ 26% (12–45%), kidney ≈ 25%, bladder ≈ 19% [E-5014] — that last record is flagged `circular_risk: true` because its primary samples are not traceable.

Note what the failure-cause distribution implies: over half of early-phase screen failures are radiological or biological, i.e. the patient's disease state moved between consent and treatment. That is not a criteria-design problem and eligibility broadening will not touch it [INFER on E-5013].

**Criteria restrictiveness over time.** Median unique eligibility-criteria content words in NCI-affiliated phase II/III trials grew 95%, from 214 words (2008) to 416 words (2018), r² = 0.732, p = 0.0008 [E-5012]. Accrual failure rose monotonically across complexity deciles, from 11.8% in the least complex to 29.4% in the most, with an independent odds ratio of 1.09 per decile (95% CI 1.03–1.15, p = 0.004) and 1.74 for phase III designs [E-5012]. Overall 19.3% of those 1,197 trials failed for low accrual. Eighteen medical exclusion categories — renal, pulmonary, diabetic, neuropsychiatric among them — were significantly associated with accrual failure at Bonferroni-corrected p < 0.001 [E-5012]. These are precisely the criteria most often carried forward without disease-specific scientific justification.

**Broadening initiatives and their measured effect.** Applying common strict cut-offs to 235,234 real-world US oncology patients across 22 cancer types, 48% were trial-eligible; broadening performance-status, hepatic, renal and haematologic criteria raised the eligible count by **78%**, with the largest gains for older, female, non-Latinx Black and lower-socioeconomic-status patients [E-5015]. At the 2019 ASCO meeting, applying ASCO–Friends criteria to 10,500 advanced NSCLC patients was reported to avoid excluding roughly half the cohort [E-5017]. FDA has finalised guidances to widen cancer trial participation, stating that unnecessarily restrictive criteria slow accrual [E-5016].

**The honest reading.** Both the 78% and the ~50% figures are *simulated eligibility on retrospective cohorts*, not observed accrual [E-5015, E-5017]. I found no published measurement of a realised accrual increase attributable to the FDA/ASCO broadening initiatives [see UNRESOLVED U-3]. And the same study that produced the 78% figure found newly eligible patients had worse real-world overall survival, HR 1.31 (95% CI 1.27–1.34) [E-5015] — broadening changes the population, not merely its size, which is exactly why sponsors resist it and why the eligibility gain will not convert one-for-one into accrual.

---

## 3. Site capacity and site economics

**The investigator workforce shrank.** Unique investigators filing an FDA Form 1572 fell from 17,941 (1999) to 9,387 (2015), a 48% decline (nadir 7,509 in 2007) [E-5018] — a compound **−3.97%/yr** [E-5072]. Of 172,453 unique investigators across the period, 85,455 (49.6%) filed for a single study only, 21,768 (12.6%) were intermittent and 65,231 (37.8%) were continuous; **only the one-and-done category grew**, and that growth was driven by non-US investigators [E-5018]. The non-US share of continuously active investigators rose from 16.6% to 47.6%, while US-based continuous investigators collapsed from 9,003 to 697 [E-5018]. Tufts CSDD's 2010–2020 BMIS extract finds roughly half of investigators filing a single 1572 in a year never file again [E-5019].

**The enrollment distribution is the capacity story.** In a Tufts CSDD study of nearly 16,000 sites across 151 global phase II/III trials, 11% enrolled zero patients, 37% under-enrolled, 39% met target and 13% exceeded — so **48% of selected sites failed to deliver their plan** [E-5020]. A Phesi analysis of 11,826 oncology sites across 173 trials found 2,298 (19%) enrolled exactly one patient, with a per-trial range of 2% to 76%, and estimated cost per patient of ~$130,000 at those sites versus $14,167 at better performers [E-5021] — vendor analysis, recorded as `market_report`. Combining the two non-overlapping samples, roughly **30% of activated sites contribute at most one patient** [E-5073], stated as an order-of-magnitude claim about skew, not a within-sample sum.

**Staffing.** SCRS reports annual turnover of patient-facing site staff of 35–61%, up from a pre-crisis 10–37%, and 6–12 months of study recovery after a coordinator departs [E-5022]. A 2023 workforce review reported 95% of major US cancer centres had staffing shortages delaying trials [E-5023].

**Competition for the same patients — documented, not anecdotal.** The strongest evidence is Bennette et al.: in a multivariable model over 787 NCTN phase II/III trials, **the number of trials competing for eligible patients in the same population per year was an independent predictor of low accrual**, alongside phase III design, non-targeted drugs, multi-histology eligibility and major-cancer indications [E-5009]. Supporting density figures: >8,600 active US cancer drug trials including >1,000 PD-1/PD-L1 trials [E-5024]; >300 GLP-1 receptor agonist programmes in active development with 2024 a record year for obesity trial starts and 2025 higher [E-5025]. The oncology-checkpoint and obesity/GLP-1 crowding cases the assignment names are real; only the first is quantified in a peer-reviewed model.

---

## 4. Precision-medicine fragmentation (B4)

**NCI-MATCH — the best-measured natural experiment.** 5,954 patients had tumour specimens centrally sequenced at 1,117 accrual sites. Profiling succeeded in 93.0%. An actionable alteration was present in 37.6%. After clinical and molecular exclusions, **17.8% were assigned to a treatment sub-protocol** — 26.4% had all sub-protocols been open simultaneously. In total 1,593 patients were assigned across 38 sub-studies [E-5028].

Screen-to-enroll: **5.6 patients screened per patient assigned** at the 17.8% rate; 3.7 counting all 1,593 eventual assignments [E-5066].

The 17.8% versus 26.4% gap is the purest available measurement of fragmentation cost. Nearly a third of the matchable patients were lost purely because the right arm was not open at the right moment — a scheduling and slot-availability failure, not a biology failure [INFER on E-5028].

**Lung-MAP.** 1,407 screening registrations, 1,244 with biomarker results, 529 sub-study registrations = 37.6%, or **2.7 screened per sub-study registration** [E-5029, E-5066]. Lower than NCI-MATCH because non-match sub-studies absorb biomarker-negative patients — i.e. the master protocol architecture is itself the mitigation.

**TAPUR.** Close to 3,000 patients enrolled since 2016 at 260+ US locations, cohorts of up to 10 expanding to 28 on a disease-control signal [E-5030]. That is roughly 300 patients/year across an entire national basket study. ASCO does not publish a screening denominator on the accessible pages, so a match rate cannot be computed [logged in UNRESOLVED U-2].

**The worst observed ratio.** A deployed AI prescreening system processed 98,348 patients across 29 trials, flagged 825 eligible and produced 117 enrollments [E-5047]. That is **841 charts screened per patient enrolled**, 119 charts per eligible patient flagged, and only 14% of flagged-eligible patients actually enrolling [E-5067]. This is the sharpest single measure of matched-capacity scarcity available: automation removed the screening cost and the yield stayed at 0.12%.

**Rare disease and prevalence-limited enrollment.** AACT analysis shows mean sample size rises with prevalence, most markedly in phase 3; phase 3 trials in the rarest bands (<1 and 1–9 per million) had fitted mean sizes comparable to phase 2 trials, and some EU orphan approvals rested on as few as 12 patients [E-5031].

**What happens to a phase III when the eligible population is a few thousand worldwide.** The registry evidence says the phase III does not happen in recognisable form: it shrinks to phase-2 scale [E-5031], or it is replaced by a single-arm trial with an external control [E-5037, 80% of the 45 external-control approvals were rare-disease]. The constraint therefore does not manifest as an unenrollable phase III; it manifests as a *change of evidentiary regime*, which transfers the bottleneck from B4 to B5 (regulatory acceptance of non-randomised evidence). The documented refusals in §5 are what that transfer costs when it fails [INFER on E-5031, E-5037, E-5039].

**The countervailing effect, stated plainly.** Fragmentation cuts both ways. It multiplies screening burden per enrolled patient [E-5066, E-5067] but it *shrinks* the number of patients each trial needs [E-5031]. Its unambiguous cost is to screening and referral infrastructure — sequencing, molecular tumour boards, national referral networks — not to bed capacity. Any ranking of B4 that ignores this sign ambiguity is wrong in one direction or the other [INFER].

---

## 5. Mitigation technologies — uptake and measured effect

**Base rate first.** A Tufts CSDD review of more than 16,500 articles published since 2022 found only **6% contained empirical performance data** [E-5045]. Ninety-four percent of this literature is promissory. Every claim below should be read against that base rate.

### 5.1 Master protocols / platform trials
Regulatory acceptance: **accepted**. Measured effect: a JAMA Network Open economic evaluation (5,000-iteration simulation anchored on STAMPEDE, expert survey 16/146 responding = 11%) found running 10 interventions as ten independent two-group trials raises median total cost by 57.5% (IQR 43.1–69.9) and median cumulative duration by **311.9%** (IQR 282.0–349.1) versus one platform, while platform setup cost is 391.1% higher; platform base cost $104.95M (SD $32.51M) [E-5034]. This is a simulation with expert-elicited inputs at an 11% response rate, not an observed head-to-head.

GBM AGILE: 2,000+ screened against a 2,250 target, 133 sites in 3 countries, active sites averaging 0.75–1.0 patients/site/month, which the sponsor states is 3–4× traditional GBM trials [E-5035]. That sponsor claim is not reproducible from the public comparator; against the industry phase III median of 0.4 patients/site/month [E-5003] the observed multiple is ≈2.2×.

RECOVERY: >10,000 UK inpatients randomised in ~2 months, dexamethasone result within **100 days** [E-5036]. The enabling conditions — single-payer system, universal disease incidence, near-zero protocol burden, integration into existing care pathways — do not transfer to oncology or rare disease, and citing RECOVERY as evidence of what platform design can do generally is a category error [INFER].

**Programme-level caveat.** The 311.9% duration figure is an aggregate over ten interventions. For a single sponsor with one asset, joining a platform saves site start-up and control-arm cost but does not shorten that asset's own path [INFER on E-5034].

### 5.2 External / synthetic control arms
Regulatory acceptance: **case_by_case**.

Acceptances: a systematic review of FDA decisions identified **45 approvals over 2000–2019** whose pivotal evidence used an external control — about 2.25/year — comprising roughly one in three first-time orphan approvals in the period. Sources: retrospective natural history 44%, baseline control 33%, published data 11%, prior clinical study 11%. Therapeutic mix: non-malignant haematology 49%, GI/inborn errors 22%, endocrine 13%, neurology 9%. 80% rare disease; 87% objective endpoints [E-5037]. FDA issued draft guidance in February 2023 with bias as the stated central validity threat [E-5038].

**Rejections — the informative half.** REGENXBIO's Hunter syndrome gene therapy (external controls judged to lack comparability); Capricor's deramiocel for Duchenne cardiomyopathy (external control a major issue in the July 2025 complete response letter, despite FDA-funded natural history datasets); Replimune's RP1 in advanced melanoma (contribution of the drug not determinable against literature-based historical controls); ODAC's negative vote on Incyte's retifanlimab in anal canal carcinoma [E-5039]. Four documented cases; not an exhaustive census.

The pattern in those four is comparability and attributability of effect. Both fail hardest in exactly the fragmented, small-population settings where external controls are most wanted [INFER on E-5037, E-5039].

⚠ **LOW-EVIDENCE CLAIM** — An ISPOR 2025 conference poster reports the share of FDA approvals involving an RWD external control arm rising from 5–7% (2020) to 40–45% (2024) [E-5040]. This is an order of magnitude above the ~2.25 approvals/year implied by the peer-reviewed 2000–2019 census [E-5037]. The discrepancy is most plausibly a much broader inclusion rule counting any supportive RWD rather than a pivotal external control. I do not use this figure as an acceptance rate and no conclusion here rests on it.

### 5.3 Decentralised / hybrid trials
Regulatory acceptance: **accepted**. Adoption trajectory and the retrenchment: decentralisation elements in 20–25% of studies in 2021 rising to 40–45% in 2022, but a **9% year-on-year fall in DCT activity in 2022**, a projected 17% rebound in 2023, and ~1,450 DCTs in 2024 (+5.5%) [E-5043]. The retrenchment was element-specific: ePRO/eCOA/eConsent and home or alternative-site visits slowed 31% in 2022, and remote blood-pressure and glucose monitoring declined from 2021 [E-5043]. Source is a vendor tracker with unpublished element-tagging methodology.

Measured effect: a critical assessment reviewing 13 DCTs found 11 reported recruitment improvements, 7 reported positive retention and 6 indicated greater demographic heterogeneity [E-5044] — self-reported outcomes against historical comparators, no randomised head-to-head, and obvious publication bias since underperforming DCTs are unlikely to be written up [INFER].

Vendor/modelled claim, recorded for S4 application, **not** a measured effect: Tufts CSDD modelling with sponsor and technology-vendor data inputs puts expected NPV at $10M on a $2M investment (phase 2) and $39M on $3M (phase 3) [E-5046].

### 5.4 Digital twins / prognostic covariate adjustment
Regulatory acceptance: **qualified_opinion**. EMA's CHMP issued a qualification opinion in September 2022 for PROCOVA, qualifying AI-digital-twin-derived prognostic scores as prognostic covariate adjustment able to increase power or precision in randomised controlled trials **with continuous outcomes** [E-5041].

Statistical mechanism: variance reduction by adjusting for a covariate highly correlated with outcome. It shrinks the required sample size of a randomised trial; it does **not** remove the control arm [E-5041].

Realistic magnitude and limits: a PROCOVA-MMRM case study reported removing up to **15.3%** of participants at equivalent inference [E-5042] — method-developer authored, single case study, vendor conflict applies. Limits, stated plainly: (a) scope qualified only for continuous outcomes, so time-to-event and binary primary endpoints are outside it; (b) the gain scales with the prognostic model's correlation with outcome, which is low in exactly the novel-mechanism, poorly-characterised indications where sample size hurts most; (c) a 10–20% control-arm reduction is a second-order effect on system throughput; (d) it does nothing whatever for screening burden, which §4 shows is the dominant cost in fragmented indications [INFER on E-5041, E-5042, E-5067].

### 5.5 AI trial matching and site selection
Regulatory acceptance: **NA** (no regulatory gate).

Best available measurements, both observational, neither with a concurrent randomised manual-screening control:
- A real-time common-data-model prescreening system: 94% retrospective / 88% prospective accuracy, ~10-fold reduction in chart-review workload, screening time 3.1 → 1.8 min/chart (−41%); across 29 trials since September 2022 it screened 98,348 patients, flagged 825 eligible and produced **117 enrollments**, consent rates 9–37% [E-5047].
- A 12-month prospective evaluation in 3,804 consecutive solid-tumour patients: 23,912 candidate pairs, 17,912 oncologist-confirmed, screening 120 → 30 min/patient, F1 0.8246 (95% CI 0.81–0.83), sensitivity 0.8375, specificity 0.8359, versus GPT-4 zero-shot F1 0.47. **The study reports no downstream enrolment counts at all** [E-5048]. Largest demographic F1 gap ≈7 points (White vs Black patients).

**The verdict for this category.** The AI-matching literature measures matching accuracy and screening cost, not accrual. I found no controlled comparison establishing an accrual-rate effect [UNRESOLVED U-1]. Where enrolments were counted, the yield was 117 patients over ~3.5 years across 29 trials [E-5047]. AI made screening cheap; the binding limit remained the supply of matching open slots. That is a direct, quantified demonstration that the constraint is matched capacity and not screening effort [INFER on E-5047, E-5048].

### 5.6 Eligibility broadening and pragmatic designs
Covered in §2. Regulatory acceptance **accepted** [E-5016]; effect is +78% modelled eligible population [E-5015] with no published realised-accrual measurement.

---

## 6. The forward-looking question: does clinical operations capacity scale?

### Current system throughput

| Series | Value | Period | Source |
|---|---|---|---|
| CDER commercial IND receipts | 852 → 1,139 | 2018 → 2024 | E-5050 |
| CDER INDs with activity | 12,935 → 15,124 | 2020 → 2025 | E-5049 |
| Interventional trials with a US site | 7,673 (35.8% industry) | 2023 | E-5051 |
| Participants in completed industry phase III trials | 1,245,175 / 1,249,809 / 1,156,515 | 2008-11 / 2012-15 / 2016-19 | E-5006 |
| Unique FDA Form 1572 investigators | 17,941 → 9,387 | 1999 → 2015 | E-5018 |

### Growth rates (arithmetic shown)

- Commercial IND receipts: (1139/852)^(1/6) − 1 = **+4.96%/yr** [E-5061]
- INDs with activity: (15124/12935)^(1/5) − 1 = **+3.18%/yr** [E-5062]
- Industry phase III participant throughput: (1156515/1245175)^(1/8) − 1 = **−0.92%/yr** [E-5063]
- FDA-regulated investigator workforce: (9387/17941)^(1/16) − 1 = **−3.97%/yr** [E-5072]

**The central finding.** Candidate flow into the clinic grew at ~5%/yr while the patient throughput of the industry phase III system *shrank* at ~1%/yr and the investigator workforce shrank at ~4%/yr. The gap is **5.88 percentage points per year** [E-5070] — indicative rather than within-sample, since the IND series is US filings 2018–2024 and the participant series is global registered phase III 2008–2019. Historically that gap was absorbed by adding 49% more sites per trial [E-5002], accepting a 50% fall in per-site productivity [E-5003, E-5065], extending recruitment by 5 months [E-5001], and letting 18–39% of trials fail or terminate on accrual [E-5009, E-5007].

**Clinical operations capacity, measured in patients enrolled per year, has not grown for over a decade** [E-5063]. It is not a system that scales with candidate flow; it is a system that has been absorbing a ~5%/yr candidate increase by degrading its own unit economics.

### Scale-up arithmetic: what 2×, 5×, 10× would require

*Time available at historical growth* [E-5068]:

| Multiplier | At 4.96%/yr (IND receipts) | At 3.18%/yr (INDs with activity) |
|---|---|---|
| 2× | ln(2)/ln(1.0496) = **14.3 yr** | ln(2)/ln(1.0318) = **22.1 yr** |
| 5× | ln(5)/ln(1.0496) = **33.2 yr** | ln(5)/ln(1.0318) = **51.4 yr** |
| 10× | ln(10)/ln(1.0496) = **47.6 yr** | ln(10)/ln(1.0318) = **73.6 yr** |

If AI compresses discovery such that IND flow multiplies over 5–10 years rather than 14–74, the increment arrives on a timescale the delivery system has never had to match.

*Patient-slot requirement* [E-5069]. Baseline = 1,156,515 / 4 = **289,129 industry phase III participants/year** [E-5064]. Holding trials-per-IND and patients-per-trial constant:

| Multiplier | Total ph III participants/yr | Additional/yr | Additional site-slots at 4.8 patients/site-year |
|---|---|---|---|
| 2× | 578,258 | +289,129 | **60,235** |
| 5× | 1,445,644 | +1,156,515 | **240,941** |
| 10× | 2,891,288 | +2,602,159 | **542,116** |

Site-slots use the observed median 0.4 patients/site/month × 12 = 4.8/site-year [E-5003].

*Two calibration points.* (i) The 5× increment alone (+1.16M patients/yr) approaches the entire estimated global annual trial enrolment of ~1.2M [E-5052 — low-quality aggregator, origin untraceable, used only as scale reference and load-bearing on nothing]. (ii) The 2× requirement of ~60,235 additional continuously enrolling site-slots is ≈**6.4×** the 9,387 unique investigators who filed a Form 1572 in 2015 [E-5075]. That ratio overstates the shortfall in level terms — a site-slot is a site-trial-year, a 1572 filer is an investigator-year, and 1572 filings cover only US-FDA-regulated studies while the participant denominator is global — and I use it only to establish that the required expansion is of a different order than the existing workforce, not to assert a precise multiple.

### Verdict on item 6

**Clinical operations capacity does not scale with candidate flow, and has not scaled at all for twelve years.** [E-5063, E-5070]

Three qualifications I will not omit:

1. **Precision medicine cuts the requirement.** If the incremental candidates are biomarker-defined, patients-per-trial falls [E-5031] and the linear scaling above overstates patient-slot demand. But the same shift raises screening burden per enrolled patient by 3–6× in master protocols [E-5066] and by ~840× in one real deployment [E-5067], so the load moves from beds to referral networks and sequencing rather than disappearing.
2. **Mitigations are real but bounded.** Platform trials cut per-arm cost and time materially in simulation [E-5034]; digital twins recover ~15% of a control arm in one case study [E-5042]; external controls remove the control arm entirely in ~2.25 approvals/year, 80% rare disease [E-5037]. None of these is a 2×, let alone 10×, capacity multiplier. Summed generously they might offset a decade of the observed 5.88 pp/yr gap [E-5070], not a step change [INFER].
3. **The obvious release valve is geographic.** The non-US share of continuously active investigators went from 16.6% to 47.6% in sixteen years [E-5018], which is the system already doing the only thing it has historically done at scale when capacity binds. That valve has finite width and carries its own regulatory and generalisability costs [INFER].

---

## Raw pool slack vs matched capacity

Agent C's premise, restated fairly: cancer trial participation is ~8%, and 55.6% of non-enrolment is attributed to no trial being available at the patient's site rather than patient refusal [E-5032]; therefore the raw patient pool has slack and B3 ranks low.

The first half is correct. The inference is not.

**Raw pool — quantified.** In 13 studies covering 8,883 US cancer patients: 8.1% enrolled (95% CI 6.3–10.0), academic sites 15.9% versus community 7.0% [E-5032]. When patients are actually offered a trial they consent roughly half the time [E-5033]. Renormalising over the 91.9% who do not enrol: **60.5% fail at trial availability, 23.4% at eligibility, 16.1% at patient decision** [E-5074]. Patient willingness accounts for one sixth of the shortfall. On this measure the raw pool is enormous and largely untapped.

**Matched capacity — quantified.** Every one of the following is a measurement of what happens when you try to convert that raw pool into an enrolled patient:

| Measurement | Value | Source |
|---|---|---|
| No open protocol for the patient's disease at their site | 55.6% of patients | E-5032 |
| Ineligible even when a protocol is open | 21.5% of patients | E-5032 |
| NCI-MATCH: screened → assigned to a sub-protocol | 17.8% | E-5028 |
| NCI-MATCH: matchable but no arm open at that moment | 26.4% − 17.8% = 8.6 pp lost to slot unavailability | E-5028 |
| Lung-MAP: screened → sub-study registration | 37.6% | E-5029 |
| Real AI prescreening deployment: charts → enrolments | 117 / 98,348 = 0.12% | E-5047, E-5067 |
| Sites enrolling zero patients | 11% | E-5020 |
| Oncology sites enrolling exactly one patient | 19% | E-5021 |
| Sites failing to deliver their enrolment plan | 48% | E-5020 |
| Patients per site per month, industry phase III | 0.4, halved in four years | E-5003 |
| Annual site-staff turnover | 35–61% | E-5022 |
| Major cancer centres with trial-delaying staffing shortages | 95% | E-5023 |
| Unique FDA-regulated investigators | −48% 1999→2015 | E-5018 |

**Resolution.** The 55.6% figure is not evidence of slack. It is the *measurement of the constraint*. "No trial available at the patient's site" is precisely the definition of matched-capacity scarcity: a protocol that matches the patient's disease, molecular profile and clinical state, open at a site the patient can reach, with staff able to screen and consent them. Reading that number as slack is reading the size of the unserved queue as evidence that the server is idle [INFER].

The AI prescreening deployment is the decisive test, because it holds screening effort constant and removes it as an explanation. That system read 98,348 charts — an enormous slice of raw pool — and produced 117 enrollments [E-5047]. Screening cost was cut tenfold and per-chart time by 41% [E-5047]. The yield stayed at 0.12%. If raw-pool slack were the operative variable, cheap exhaustive screening would have converted it. It did not, because the missing resource was open matching slots at qualified sites, not identified patients [INFER on E-5047, E-5067].

The NCI-MATCH 17.8%-versus-26.4% gap makes the same point inside a single well-funded protocol with central sequencing and 1,117 sites: 8.6 percentage points of *already-matched* patients were lost purely because their arm was not open at that moment [E-5028]. That is a pure slot-availability loss with zero contribution from patient pool, biology, or willingness.

**Conclusion.** Raw pool slack is large and real. Matched capacity is scarce and has been shrinking on every measured dimension — investigators, per-site productivity, staff retention. These are not in tension; they are the same fact seen from two ends. A large untapped population is a *necessary* condition for scaling and not remotely a *sufficient* one. Agent C's finding is correct as data and inverted as inference.

---

## B3/B4 ranking test — independent verdict on Agent C's placements

Applying the brief's constraint definition — a step whose improvement actually increases annual approvals or approvals per dollar — and M2 elasticity.

### B3 (recruitment / site capacity), Agent C rank 7 of 16

**Elasticity at today's candidate flow.** A 10% improvement in recruitment speed shortens phase III elapsed time by 6.1% (0.10 × 60.8% [E-5060]) ≈ 1.8 months, or ~1.5% of a 10.5-year programme [E-5071]. Separately, a 10% reduction in accrual-driven terminations preserves ~3.9% of trials that would otherwise die [E-5076, E-5007] — but those preserved trials carry the ordinary base-rate probability of efficacy failure, so the approval yield is a fraction of 3.9%. Recruitment improvement buys time and reduces waste; **it does not raise the probability that a molecule works.**

**Verdict at current flow: Agent C's rank 7 is defensible.** I reach a similar place by different arithmetic. The system has spent a decade adapting to a ~5%/yr candidate increase, and it has succeeded, at the price of degraded unit economics [E-5002, E-5003]. A step whose capacity roughly matches current demand is by the brief's own definition not the binding constraint today.

**Verdict under the constraint-shift scenario (Q3): rank 7 substantially understates it.** The elasticity of B3 is not a constant; it is a function of candidate flow. Below system capacity, marginal recruitment improvement buys time. Above it, marginal recruitment capacity buys *approvals*, because unenrolled candidates yield exactly zero. And the evidence says the system sits close to its ceiling already: throughput growth of −0.92%/yr [E-5063], a workforce shrinking at −3.97%/yr [E-5072], and per-site productivity halving in four years [E-5065]. At 2× candidate flow the required expansion is ~60,000 additional continuously enrolling site-slots [E-5069], which the historical record gives no basis to expect on any relevant timescale [E-5068]. **If the study's premise about AI-multiplied candidate flow is granted even partially, B3 belongs in the top three.** [INFER]

I flag this as conditional rather than asserting a rank, because whether candidate flow actually multiplies is Agents A–D's question, not mine. My contribution is the conditional: capacity does not scale, so B3's rank is a direct function of how much flow arrives.

### B4 (precision-medicine fragmentation), Agent C rank 10 of 16

**Elasticity depends entirely on which metric you pick, and this is why the rank is hard.**

- *Metric = total patient-slots.* B4 **reduces** demand: rarer strata mean smaller trials [E-5031]. Elasticity is near zero or negative. Rank 10 is right, arguably generous.
- *Metric = screening and referral infrastructure.* B4 raises the load by 3–6× in master protocols [E-5066] and by up to ~840× in a real deployment [E-5067]. A 10% improvement in match rate at NCI-MATCH's 17.8% would have converted ~106 additional of 5,954 screened patients into assignments — meaningful for a protocol, marginal for a system. Elasticity is moderate.
- *Metric = the evidentiary regime.* This is where B4 actually bites, and it is the reading Agent C's placement most likely misses. When the eligible population is a few thousand worldwide, the phase III does not get slower — it gets *replaced* by a single-arm design with an external control [E-5031, E-5037]. That transfers the binding constraint from patient supply to regulatory acceptance of non-randomised evidence, where the documented failure mode is comparability and attributability [E-5039]. B4's true elasticity is therefore partly booked under B5.

**Verdict: rank 10 is approximately right on total patient-slots and too low on screening infrastructure, but the correction is smaller than for B3.** I would place B4 around 8, and I would note explicitly that a portion of what looks like B4 pressure is B5 pressure wearing a B4 costume [INFER]. I do not have grounds to move it into the top five.

### Cross-check against my own bias

The finding most inconvenient to a B3-is-critical reading is Tufts CSDD's 2023 benchmark: enrollments exceeded plan for a majority of studies and timelines beat expectations [E-5026]. I have recorded it, given it a plausible selection explanation, and not resolved the tension in my favour. If Agent R grades E-5026 as High and the registry series lower, my B3 conclusion weakens accordingly and should be revised.

---

## UNRESOLVED

Four items. Full records in `./RLSX/work/F/unresolved.csv`.

- **U-1** — Measured effect of AI trial matching on *accrual rate* in a controlled comparison. No such study located. Every accessible evaluation measures matching accuracy or screening time; the one study reporting enrolments [E-5047] has no concurrent control. Best estimate: no credible controlled accrual effect exists as of August 2026; the honest current figure is 117 enrolments from 98,348 charts screened across 29 trials [E-5047, E-5067].
- **U-2** — TAPUR screening denominator and therefore its match rate. ASCO publishes enrolments (~3,000) but not screening volume on accessible pages. Best estimate: TAPUR's design (patient must already have a commercial genomic report and a matching marketed drug) implies a match rate materially higher than NCI-MATCH's 17.8%; a defensible bracket is 30–60%, bounded below by NCI-MATCH's 26.4% all-arms-open figure and above by Lung-MAP's 37.6% plus TAPUR's pre-selection [E-5028, E-5029, E-5030].
- **U-3** — Measured realised accrual change attributable to the FDA/ASCO eligibility-broadening initiatives. Only modelled eligibility gains published [E-5015, E-5017]. Best estimate: realised accrual gain is a small fraction of the 78% modelled eligibility gain, because over half of oncology screen failures are disease-state changes untouched by criteria [E-5013] and because sponsors retain discretion to keep criteria tight; a plausible bracket is 5–15% accrual improvement where recommendations are fully adopted.
- **U-4** — Full year-by-year CDER IND receipt series 2015–2025 in machine-readable form. fda.gov returns HTTP 401 to the available fetch tooling on every path attempted. Two anchor years (2018, 2024) were recovered via search-result snippets of the FDA tables and one secondary compilation, and the INDs-with-activity series 2020–2025 was recovered in full [E-5049, E-5050]. Best estimate: intervening years lie on a roughly log-linear path at 4.96%/yr; this affects only the precision of the CAGR, not its sign or order of magnitude.

No assignment item was reduced in scope, deferred, or sampled. All six items and both bottlenecks were processed in full.
