CHARTER_ACK: R1,R2,R3,R4

# Agent B — AI 실증 트랙레코드 / AI Reality Check

**Scope**: adversarial-neutral measurement of whether AI in protein structure prediction, de novo sequence design and generative chemistry has produced *pipeline output* — INDs, clinical entry, clinical readouts — as distinct from benchmark scores.
**Evidence block**: `E-2001`–`E-2075` (74 records; `E-2063` unused). Ledger: `RLSX/evidence/parts/B.jsonl`. Asset table: `RLSX/data/ai_track_record.csv` (76 rows). Open items: `RLSX/work/B/unresolved.csv` (10 rows).
**Grading**: every record carries `confidence: null`, `graded_by: null`. Agent R grades independently (R3).

---

## 1. Methodology

**Evidence tiers, ranked before collection began.** Tier 1 = clinical readouts in peer-reviewed journals, trial registry records, and regulatory/exchange filings. Tier 2 = peer-reviewed benchmark and validation studies with disclosed protocols. Tier 3 = company press releases and technical reports, admitted but recorded as `type:"secondary"` with the company as `authors_or_org` so that Agent R can apply an S4 conflict-of-interest downgrade. Tier 4 = trade press and aggregator censuses, admitted only where they are the sole carrier of a datum and flagged `circular_risk: true`.

**Two axes held strictly apart (H0-b).** Every row in `ai_track_record.csv` carries `axis_tested ∈ {duration, PoS, both, neither}`. No duration evidence is permitted to stand in for PoS evidence at any point in this report.

**Symmetric search for failures.** Discontinuations were searched with the same effort as successes, company by company, using termination-specific query terms. The resulting table contains 19 `active` rows against 16 `discontinued` rows and 14 rows typed `claim_type=failure`. This near-parity is the survivorship-bias control.

**Denominator discipline (M3).** Where a source states a rate without a denominator, the record's `figures.denominator_def` says so explicitly and the number is not used to support a conclusion without an accompanying confidence-interval or power calculation.

**Derived values.** Seven records are `type:"derived"` (E-2057, E-2058, E-2065, E-2066, E-2070, E-2074, plus the share calculation embedded in E-2057). Each carries the full formula and every input evidence ID in its `derivation` field. Computation used the Python standard library only.

**Search volume.** 32 WebSearch/WebFetch calls. No fact in this report is written from model memory.

**Limits of this report.** It measures AI's discovery-stage output. It does not attempt to price capital cost, does not adjudicate the DiMasi cost anchor, and does not decompose regional regulatory capacity beyond noting where the only clinical evidence is Chinese. [INFER] Those belong to other agents' blocks; nothing here presumes their findings.

---

## 2. Axis (i) — Duration: is there quantitative evidence that AI shortened discovery-stage elapsed time?

### 2.1 What the claims say

| Claim | Source type | Value | Comparator | Verified independently |
|---|---|---|---|---|
| DSP-1181: design to Phase I | company-issued | ~12 months vs stated 4–6 yr [E-2008] | stated norm, no matched cohort | no |
| Rentosertib: target ID to preclinical candidate | company-issued | ~18 months vs stated 4–5 yr [E-2008][E-2031] | stated norm, no matched cohort | no |
| Insilico platform-wide | company-issued | 12–18 months to candidate; 60–200 molecules synthesised per programme [E-2030] | industry norms cited without source | no |
| Rentosertib preclinical spend | company-issued | USD 2.6M, out-of-pocket, no cost of capital [E-2031] | none | no |
| AI-assisted lead optimisation, 20 programmes 2018–2023 | peer-reviewed review | 30–50% reduction in candidate screening time [E-2010] | unspecified | partially |
| Preclinical timelines generally | peer-reviewed review | 30–50% reduction in specific applications [E-2009] | stated norms | partially |

### 2.2 Effect size, and the counter-measurement that constrains it

Taking the company claims at face value, discovery-stage compression is **2.5 to 4.5 years per programme, midpoint 3.5 years** [E-2070]. That is a large effect if real.

It is contradicted at the organisational level. An ASCO/JCO 2026 landscape analysis of 117 AI-enabled candidates across 63 companies found a **median time from company founding to first Phase 1 entry of 6.5 years** [E-2054]. Isomorphic Labs, founded 2021 and holding the AlphaFold3 franchise plus USD 600M raised, had **zero registered studies on ClinicalTrials.gov when queried on 18 August 2026** [E-2048], and its own first-in-human guidance slipped from end-2025 to end-2026 [E-2049]. DSP-0038, publicised as an AI-designed molecule entering the clinic in 2021, was still in Phase 1 in 2026 [E-2069].

[INFER] These two families of measurement are reconcilable only under one of three readings: (a) the per-programme saving is real but is reabsorbed by platform build-out, target selection, IND-enabling toxicology and CMC, so it never reaches time-to-clinic; (b) the fast programmes are a selected minority and the median programme is not fast; or (c) the company figures start the clock later than a conventional programme would. The evidence does not discriminate among these, but it does establish that **the compression is not visible in the metric that matters for system output** — elapsed time to a dosed patient.

The one asset that combines a duration claim with genuine clinical progression is rentosertib: 18-month target-to-candidate [E-2031], Phase IIa published in *Nature Medicine* [E-2028], Phase III initiated 7 July 2026 [E-2029]. [INFER] This is the single strongest duration data point in the entire dataset, and it is n = 1.

Two structural caveats bound how much any of this proves. First, precedent: DSP-1181 targeted 5-HT1A, a target class with decades of medicinal chemistry behind it [E-2032], and a fast candidate against a heavily precedented target is not evidence that *discovery* was compressed. TNIK for IPF was genuinely novel, which is why rentosertib is the stronger case [E-2028]. Second, patenting behaviour: AI-native developers disclose measurably less in vivo and in-depth testing in their compound patents than traditional developers [E-2059][E-2060]. [INFER] Filing earlier with less evidence would produce exactly the appearance of a shorter target-to-candidate interval without any underlying compression of the science.

### 2.3 Verdict on axis (i)

**Duration: evidence exists and is directional, but it is company-issued, unmatched, and contradicted at the organisational level.** Peer-reviewed reviews independently report 30–50% reduction in preclinical/screening time [E-2009][E-2010], which is the most defensible figure in this section. The same reviews state that **clinical development timelines remain essentially unchanged** [E-2009]. Discovery-stage compression is therefore substantiated at roughly 30–50% on preclinical activities, and unsubstantiated at the level of elapsed time from company founding, or from programme start, to a dosed patient.

---

## 3. Axis (ii) — Probability of success: is there quantitative evidence that AI raised clinical PoS?

### 3.1 The 80–90% Phase I claim, traced to origin

The claim originates in Jayatunga MKP, Ayers M, Bruens L, Jayanth D, Meier C, *Drug Discovery Today* 29(6):104009, June 2024, DOI 10.1016/j.drudis.2024.104009 [E-2001]. All five authors are Boston Consulting Group, the work was funded by BCG's health care practice, and the underlying pipeline tracking was performed with Wellcome across roughly 73–75 AI-derived molecules in clinical pipelines as of 2023 [E-2004].

What it reports: Phase I success **80–90%** [E-2002]; Phase II success **~40%**, which the authors themselves describe as in line with historical industry averages [E-2003]; and a projection that cumulative clinical PoS rises from 5–10% to **9–18%** [E-2005].

What could not be extracted, despite five distinct query formulations and seven alternative access routes: **the Phase I denominator, the Phase II denominator, the company list, the operational definition of "AI-discovered", and the confidence intervals**. The article is paywalled; ScienceDirect returned HTTP 403 and no open-access deposit exists. Full query logs, failure reasons and best estimates are in `unresolved.csv` rows 1–3.

### 3.2 Why the Phase I number cannot carry the weight placed on it

Three independent problems, in ascending order of severity.

**(a) Denominator undisclosed.** Wilson 95% confidence intervals on an observed 85% success rate: n=8 → [50.4%, 96.9%]; n=10 → [54.1%, 96.5%]; n=24 → [66.1%, 94.3%]; n=73 → [75.1%, 91.4%] [E-2066]. At every plausible denominator below ~50 the interval overlaps the industry Phase I range that secondary sources put at 50–65% [E-2004 context]. The effect is in principle detectable — separating 55% from 85% at 80% power needs only ~33 per arm [E-2066] — but only if the two cohorts share a denominator definition, and they demonstrably do not.

**(b) Definitional breadth.** The ASCO/JCO 2026 landscape explicitly warns that aggregated AI counts mix candidates for which AI proposed both the target and the molecular structure with programmes where AI merely accelerated structure prediction, virtual screening or trial design [E-2054]. Niazi's independent 2025 review counts only **4 to 9** AI-derived molecules with publicly documented clinical outcomes [E-2007]. Those two facts cannot both be true of a 73-molecule cohort unless the inclusion rule is very broad.

**(c) Selection at the point of clinical entry.** [INFER] Phase I is where a company decides *which* molecule to advance. AI-native companies, most of which are venture-funded and hold one to three clinical assets, face far stronger incentives than large pharma to advance only the cleanest candidate and to define "success" as "no dose-limiting toxicity" rather than "progressed to Phase II". No accessible source states how the Jayatunga analysis handled this. Reviews published after it note likely survivorship and publication bias and the absence of controlled comparison with non-AI programmes.

### 3.3 The Phase II sample — the crux

This is where the claim resolves. The reported AI Phase II rate is ~40% [E-2003] against a conventional benchmark of ~37% [E-2011].

**Power calculation** [E-2065]: detecting a 37% vs 40% difference at α = 0.05 two-sided and 80% power requires

    n = (z₀.₉₇₅ + z₀.₈₀)² · [p₁(1−p₁) + p₂(1−p₂)] / (p₂−p₁)²
      = (1.96 + 0.8416)² · [0.37·0.63 + 0.40·0.60] / 0.03²
      = **4,126 molecules per arm**

The observed AI Phase II sample is **8 assets that have completed Phase 2 field-wide as of mid-2026** [E-2055], five years *after* the Jayatunga data cut. The comparison is approximately **500-fold underpowered per arm**. The Wilson 95% CI on 40% at n = 8 is [15.2%, 71.3%] [E-2065], which contains every industry baseline ever published.

### 3.4 Verdict on axis (ii)

> ## **증거 없음 / NO EVIDENCE**
>
> **There is no statistically meaningful evidence that AI has raised clinical probability of success.**

The reasons, stated so they can be audited:

1. The only quantitative dataset offered — Jayatunga et al. — reports a Phase II rate its own authors call indistinguishable from the historical average [E-2003], and the comparison is ~500× underpowered [E-2065].
2. Total AI-derived molecules with publicly documented clinical outcomes: **4 to 9** [E-2007]. Total AI-enabled assets that have completed Phase 2: **8** [E-2055].
3. Total FDA approvals of AI-discovered drugs: **zero**, as of mid-2026, after roughly USD 8.9B invested in AI-native discovery [E-2053] and more than USD 100B invested in AI across life sciences 2022–2026 [E-2061]. The terminal outcome measure is empty.
4. Industry clinical attrition remains at approximately **90%**, unchanged [E-2061].
5. The most authoritative independent assessment located — *Nature Reviews Drug Discovery*, 7 August 2026, Bender, Thomas, Scannell et al. — concludes that evidence of clinically relevant impact is disappointingly limited and that improvement in probability of success or in development timelines remains unproven [E-2006].
6. The programme-level record points the other way. BEN-2293 was safe and missed both co-primary efficacy endpoints [E-2035]. REC-994 met its primary safety endpoint and delivered no meaningful clinical benefit [E-2039]. VRG50635 engaged its AI-nominated target in the correct cell types and the patients did not improve [E-2043][E-2044]. SGR-2921 killed two patients in dose escalation [E-2041].

**No proxy is substituted.** Benchmark accuracy, hit rates, binder success rates and time-to-candidate figures appear elsewhere in this report and are not offered as PoS evidence anywhere in it.

⚠ The one countervailing datum — rentosertib's positive Phase IIa [E-2028] and Phase III entry [E-2029] — is a single asset, in a single country, on a 71-patient trial. [INFER] It is a genuine existence proof that the pipeline can run end to end. It is not a rate.

---

## 4. The benchmark-versus-reality gap

### 4.1 Structure prediction: where predicted structures work and where they do not

**Both directions, measured.**

*Positive, prospective, peer-reviewed.* Docking 490 million and 1.6 billion molecule libraries against **unrefined AlphaFold2 models** gave hit rates statistically indistinguishable from experimental structures: σ2 receptor **54% (64/119) for AF2 vs 51% (70/138) for the crystal structure**; 5-HT2A **26% (42/161) for AF2 vs 23% (51/223) for cryo-EM** [E-2012]. Affinities were comparable, and AF2-derived hits included subtype-selective compounds the experimental-structure campaign did not produce [E-2012].

*The caveats the same authors attach.* Targets were chosen where the AF2 binding site was already close to the experimental structure, and **functional** hit rates were 1–5%, far below the 26–54% binding hit rates [E-2013].

*Negative, retrospective, peer-reviewed.* Using AF2 structures as rigid receptors produces a significant drop in enrichment against experimental holo structures, even when pockets differ by only two or three residues, because AF2 does not model ligand-induced side-chain relocation [E-2014]. Across **32 class A GPCRs**, mean top-5% enrichment factors were **X-ray 2.24, cryo-EM 2.42, AF2 1.82**, with hit rates 29.6%, 32.0% and 24.0% [E-2015]. A separate benchmark put mean EF at top 1% at **AF2 13.16, apo 11.56, holo 24.81** [E-2016].

**[INFER] The reconciliation.** AF2 produces an *apo-quality* model. Prospective large-library docking against apo-quality models works when the pocket is rigid and the library is large enough to absorb the enrichment penalty; retrospective enrichment benchmarks against holo structures penalise it because holo structures encode the answer. AlphaFold3 narrows but does not close this, degrading where binding involves conformational change beyond ~5 Å RMSD [E-2017]. The operational consequence is that structure prediction has changed *which projects can start*, not *how well a project converges*: predicted structures excel where the alternative is no structure, and remain insufficient for atomic-level binding-site chemistry decisions [E-2018].

ESMFold reaches a median TM-score of 0.95 against AlphaFold2's 0.96 [E-2019] — benchmark parity — while being unable to predict protein–protein or protein–ligand interfaces and unable to distinguish experimentally folded from misfolded de novo transmembrane β-barrel designs [E-2019]. [INFER] That is the benchmark-reality gap in a single sentence: near-identical CASP-style scores, zero utility for the design-validation task.

The AlphaFold database holds more than 200 million predicted structures [E-2018]. The number of drugs approved on the strength of them is zero [E-2053].

### 4.2 De novo design: the validation pass rates

These are the numbers usually buried in supplementary data, and they are the single most informative measurement in this report.

| Measurement | Who measured | Designs | Success rate |
|---|---|---|---|
| Pooled de novo binder success, 15 diverse targets | **independent meta-analysis** (DigBioLab) | **3,766** | **11.6%** [E-2020] |
| Independent replication of RFdiffusion IL-7Ra hits | **independent contract lab** (Adaptyv Bio) | 42 constructs | 27/32 reported binders confirmed = 84.4% concordance [E-2022] |
| Chai-2 zero-shot antibody/nanobody, 52 targets | **developer self-report** | ≤20 per target | 16% per design; ≥1 hit for 50% of targets [E-2023] |
| Chai-2 miniprotein | **developer self-report** | not stated | 68% [E-2023] |
| RFantibody VHH/scFv | peer-reviewed (Nature) | thousands; smallest successful set 95 VHHs | best affinity 78 nM, 1.45 Å cryo-EM RMSD [E-2024] |
| RFdiffusion, functional detection binders | independent | not retrievable | reported low; see `unresolved.csv` row 5 [E-2021] |

**The spread is 5.9-fold between the pooled independent figure (11.6%) and the highest developer self-report (68%)** [E-2074]. Per-target precision in the pooled analysis ranges from 0.1 to 1.0 [E-2020] — some targets yield essentially nothing.

[INFER] The Adaptyv replication is instructive about *what* independent validation actually tests: it confirmed 27 of 32 designs a developer had already labelled hits [E-2022], i.e. it validated the numerator. Neither that replication nor any developer technical report tests the denominator — how many designs were attempted and discarded before the reported set was assembled. The 11.6% pooled figure is the only number in this section that measures the denominator honestly, and it is the number this report carries forward.

### 4.3 De novo design's clinical track record

**One de novo designed protein has ever entered human testing: NL-201, Neoleukin's IL-2/IL-15 mimetic. It was discontinued in November 2022** because preliminary data suggested it would not be strongly differentiated from other IL-2 pathway agents [E-2025].

RFdiffusion, ProteinMPNN and RFantibody outputs: zero clinical entries located. Institute for Protein Design ecosystem clinical survivors: zero. AI Proteins has generated miniproteins against more than 150 targets with several in vivo proofs of concept and a Bristol Myers Squibb option deal worth up to USD 400M — and no IND [E-2051]. Generate Biomedicines' GB-0895 is at Phase 3 [E-2026], but it is an *engineered* long-acting anti-TSLP antibody against a precedented target, not a de novo designed protein against a novel one. [INFER] The distinction matters: half-life engineering of a known antibody class is a different and easier problem than designing a novel binder to a novel target, and conflating them is the most common inflation in this field's public accounting.

---

## 5. The AI-native pipeline census

Full asset-level table in `RLSX/data/ai_track_record.csv`. Field-wide totals: **117 AI-enabled clinical candidates across 63 companies** (ASCO/JCO 2026, December 2025 data cut) [E-2054]; **60 (51.3%) have completed Phase 1, 8 (6.8%) have completed Phase 2, 0 approved**, with 8+ named discontinuations [E-2055]. Earlier independent counts: 31 molecules in trials across 8 leading AI companies in April 2024 [E-2071]; >75 cumulative AI-derived molecules reaching clinical stage by end-2024 [E-2072].

**Companies with clinical assets**

| Company | Highest-phase asset | Phase | Status |
|---|---|---|---|
| Insilico Medicine | rentosertib (TNIK, IPF) | **III** | active [E-2029] |
| Generate Biomedicines | GB-0895 (anti-TSLP, asthma) | **III** | active [E-2026] |
| Relay Therapeutics | zovegalisib / RLY-2608 (PI3Kα) | Ph3 dose selected | active [E-2046] |
| Recursion (incl. ex-Exscientia) | REC-4881 (MEK1/2, FAP) | II | active [E-2067] |
| Iambic | IAM1363 (HER2) | I/1b | active [E-2045] |
| Schrödinger | SGR-1505 (MALT1) | I | active, being partnered out [E-2042] |
| Absci | ABS-201 (PRLR) | I/2a | active [E-2047] |
| XtalPi / Signet | SIGX1094 (TEAD) | I | active [E-2064] |
| Sumitomo / Exscientia | DSP-0038 | I | active since 2021 [E-2069] |

**Companies with zero clinical assets**, holding roughly USD 2B of capital between them: Isomorphic Labs (0 registered trials, direct registry query) [E-2048][E-2049]; Xaira (>USD 1B at launch) [E-2050]; AI Proteins [E-2051]; Genesis Therapeutics [E-2052]; Chai Discovery [E-2023]; EvolutionaryScale [E-2019]; Cradle Bio (tools vendor, absent from both field-wide censuses) [E-2055].

**Modality decomposition (M5).** Small molecule dominates: rentosertib, ISM6331, REC-4881/617/1245/4539, SGR-1505/3515, IAM1363, RLY-2608, SIGX1094, DSP-0038, DSP-1181, EXS-21546, VRG50635. Antibody: GB-0895, ABS-101, ABS-201. De novo protein: NL-201 only, discontinued. Cell therapy: GB-5267 (Phase 1). ADC-adjacent: GB-4362. **No AI-derived gene therapy, RNA therapeutic or vaccine asset was located in the clinical census.** [INFER] AI's clinical footprint is overwhelmingly small-molecule and antibody, i.e. concentrated in the two modalities where design–build–test cycles are cheapest, not in the modalities where delivery and manufacturing dominate.

**Region decomposition (M6).** The only positive Phase II efficacy readout in the dataset (rentosertib) was run entirely in China, 22 sites, 71 patients [E-2028], and its Phase III is 47 Chinese centres [E-2029]. US/EU AI-derived assets have produced Phase I safety data, oncology response rates without control arms, and a run of Phase II failures. [INFER] Any claim that AI-derived PoS is improving currently rests on a single-country dataset.

---

## 6. The failure census

Weighted equally with successes by design. 16 `discontinued` rows against 19 `active` rows.

| Asset | Company | Phase | Endpoint / failure mode | Was this a failure mode AI was supposed to fix? |
|---|---|---|---|---|
| **VRG50635** (PIKfyve, ALS) | Verge Genomics | 1b | Missed primary efficacy. Plasma NfL **rose** within 2 weeks instead of falling; ~1/3 of patients could not tolerate the lowest dose; trial terminated, no open-label extension; company dropped its only clinical asset [E-2043][E-2044] | **Yes — directly.** AI's contribution was *target nomination*. The company's own post-mortem attributes the failure to patient heterogeneity and biomarker-to-brain translation, not chemistry [E-2044] |
| **BEN-2293** (pan-Trk, atopic dermatitis) | BenevolentAI | IIa | Safe and well tolerated; missed **both** co-primary endpoints (EASI and NRS) in the ITT population [E-2035] | **Yes.** AI-derived target hypothesis; canonical Phase II efficacy failure |
| **REC-994** (CCM) | Recursion | II | Met primary safety endpoint; **no meaningful clinical benefit**; long-term extension failed to confirm earlier signals [E-2039] | **Yes.** Efficacy/target validity |
| **REC-2282** (NF2) | Recursion | II | Discontinued May 2025 on totality of data [E-2038] | Yes |
| **REC-3964** (C. difficile) | Recursion | II | De-prioritised May 2025, out-licensing explored [E-2038] | Partly (portfolio, not endpoint) |
| **SGR-2921** (CDC7) | Schrödinger | I | **Two treatment-related deaths** in dose escalation; programme abandoned [E-2041] | **Yes.** Physics-based/ML design did not predict the toxicity (B8) |
| **EXS-21546** (A2A) | Exscientia | 1/2 | Insufficient receptor coverage within the assumed therapeutic range; A2A target research stopped entirely [E-2033] | **Yes.** PK / target-coverage prediction is precisely what property models claim |
| **DSP-1181** (5-HT1A) | Exscientia/Sumitomo | I | Discontinued 2022. One review cites preclinical QT prolongation; others cite a favourable safety profile [E-2032] | Yes — and this was the flagship "12 months to clinic" asset [E-2008] |
| **NL-201** (de novo IL-2 mimetic) | Neoleukin | I | Insufficient differentiation from other IL-2 agents [E-2025] | Partly. The protein folded and bound; the *biology* was undifferentiated |
| **ABS-101** (TL1A) | Absci | I | De-prioritised in IBD despite favourable safety; partner sought [E-2047] | No (portfolio) |
| **Exscientia pipeline cut** | Exscientia | corporate | Reduced to 2 oncology programmes, Oct 2023 [E-2034] | n/a |
| **BenevolentAI restructuring** | BenevolentAI | corporate | ~180 layoffs May 2023 [E-2036]; **delisted from Euronext Amsterdam 13 March 2025**, merged into Osaka Holdings, ceased to exist as a listed entity [E-2037] | n/a |
| **Recursion downsizing** | Recursion | corporate | 20% workforce reduction post-merger [E-2040] | n/a |
| **Isomorphic Labs timing** | Isomorphic Labs | preclinical | First-in-human guidance slipped end-2025 → end-2026; zero registered trials at 2026-08-18 [E-2048][E-2049] | Duration claim, not clinical failure |
| SGR-1505 / SGR-3515 | Schrödinger | I | Both being shopped for partners; therapeutics pipeline reduced to two clinical assets [E-2042] | Soft de-prioritisation |

**The pattern.** [INFER] Of nine terminated therapeutic assets with an identifiable failure mode, **seven failed on target validity, efficacy, PK/target coverage or unpredicted toxicity** — B1, B7 and B8 in the catalogue. Not one failed because the molecule could not be found, designed or synthesised. **AI compressed the step that was not failing, and the failures are concentrated in the steps AI has not yet touched.** Two of the three original public AI-drug-discovery companies no longer exist in their original form: BenevolentAI was delisted and merged out [E-2037], Exscientia was absorbed into Recursion after cutting its pipeline to two programmes [E-2034].

---

## 7. Base rate and share — the Amdahl ceiling on AI's system-level effect

**Numerator.** 117 AI-enabled clinical candidates cumulative, across 63 companies, data cut December 2025 [E-2054]. Cross-check: >75 cumulative by end-2024 [E-2072]; 31 across 8 leading companies in April 2024 [E-2071].

**Denominator.** FDA CDER received **1,139 commercial and 716 research INDs in CY2024, total 1,855** [E-2056]. The FDA does not tag INDs by discovery method, and clinical registries carry no AI-provenance field, so an official AI-derived IND count does not exist (`unresolved.csv` row 9).

**Derived share** [E-2057]:

    share_low  = (117 / 10 years) / 1,139 = 1.03%
    share_high = (117 /  3 years) / 1,139 = 3.42%

**AI-derived candidates are 1.0%–3.4% of annual US commercial IND filings.** The estimate is generous to AI in the numerator (the 117-count uses a broad AI-enabled definition [E-2054]) and generous to AI in the denominator (CBER INDs are excluded; including them lowers the share).

**Ceiling on system output** [E-2058]:

    Δapprovals(relative) = share_AI × (PoS_AI − PoS_base) / PoS_base

| Scenario | PoS assumption | Δ annual approvals (relative) |
|---|---|---|
| Most AI-favourable published projection | 10% → 18% [E-2005] | **+0.8% to +2.7%** |
| Phase I advantage real, Phase II/III unchanged (the empirically supported case [E-2003][E-2011]) | 10% → 15.5% | **+0.6% to +1.9%** |
| Phase I advantage is selection bias | 10% → 10% | **0%** |

**This is the Amdahl ceiling, and it binds regardless of per-asset performance.** [INFER] Even if every claim made for AI-derived molecules were true, at current pipeline share the system-level effect on annual approvals is on the order of one to three percent relative. Nothing AI does *per asset* can exceed this until the share of INDs it produces rises by roughly an order of magnitude — and the rate-limiting factor on that share is not algorithmic capacity but the cost and duration of everything downstream of candidate nomination.

---

## 8. Bottleneck catalogue — what this agent's evidence does and does not say (B1–B14)

Every entry is evaluated. Where this block carries no direct evidence, that is stated as such rather than filled with inference.

- **B1 Target validation / translational validity.** Directly implicated and the single largest failure source in this dataset. VRG50635 [E-2043][E-2044], BEN-2293 [E-2035], REC-994 [E-2039], REC-2282 [E-2038] all failed here. Only 3–9 of 67 clinical AI molecules involved AI-discovered *novel* targets [E-2004 context]. **Evidence: strong, and it points at B1 as a live constraint that AI has not relieved.**
- **B2 Preclinical→clinical translation.** Preclinical timelines compressed 30–50% [E-2009][E-2010] while clinical timelines and attrition did not move [E-2009][E-2061]. DSP-1181 cleared preclinical and died in Phase I [E-2032]. **Evidence: strong, indicates translation is untouched.**
- **B3 Trial recruitment / site capacity.** Indirect only. Rentosertib's Phase IIa took 71 patients across 22 sites [E-2028] and its Phase III needs 320 across 47 sites over 52 weeks [E-2029]; Isomorphic has no registered trial four-plus years after founding [E-2048]. **Evidence: weak from this block; recruitment duration is not measurable from the sources collected here.**
- **B4 Patient-pool fragmentation from precision medicine.** IAM1363 recruits HER2-altered patients across multiple rare histologies [E-2045]; REC-4881 targets FAP [E-2067]; REC-2282 targeted NF2 and was discontinued [E-2038]. **Evidence: suggestive that AI-native pipelines skew to rare/segmented populations, but no quantitative recruitment data was collected. Not resolvable from this block.**
- **B5 Regulatory review capacity and evidence standards.** Zero FDA approvals of AI-discovered drugs [E-2053]; regulators do not record AI provenance at all, so no AI-specific evidentiary pathway is being exercised [E-2056 and `unresolved.csv` row 9). **Evidence: moderate. Regulation is not currently the binding constraint because nothing has reached it.**
- **B6 CMC / manufacturing.** GB-0895 required a ~89-day half-life antibody at Phase 3 scale [E-2026]; GB-5267 is an armoured CAR-T at Phase 1 [E-2027]. **Evidence: this block collected no CMC failure data. Not evaluable from Agent B's sources; no claim made either way.**
- **B7 Delivery and biodistribution.** Directly implicated twice. EXS-21546 failed on inability to achieve receptor coverage in the therapeutic range [E-2033]; VRG50635 reached the brain and engaged its target yet produced no benefit [E-2044]. **Evidence: moderate, and it shows exposure/coverage prediction remains unsolved.**
- **B8 Toxicity and immunogenicity prediction.** Directly implicated. SGR-2921 caused two treatment-related deaths in Phase 1 dose escalation from a physics/ML-designed molecule [E-2041]; DSP-1181 is attributed by one review to preclinical QT prolongation [E-2032]; one third of VRG50635 patients could not tolerate the lowest dose [E-2044]. **Evidence: strong. AI toxicity prediction has not prevented clinical toxicity failures.**
- **B9 Wet-lab throughput / DBTL cycle.** This is where AI's measurable gains sit: 30–50% screening-time reduction [E-2010], 60–200 molecules synthesised per programme [E-2030], prospective docking hit rates of 26–54% [E-2012], de novo binder success of 11.6% pooled [E-2020]. **Evidence: strong, and it shows B9 has genuinely improved — which is precisely why it is no longer the constraint.**
- **B10 Scarcity of high-quality experimental training data.** Per-target precision in de novo binder prediction ranges 0.1–1.0 [E-2020]; ESMFold cannot separate folded from misfolded designs [E-2019]; AF2 models are apo-quality because they never saw the liganded state [E-2014][E-2016]; AI-native patents disclose less experimental data than traditional ones, degrading the public corpus [E-2059]. **Evidence: strong and convergent — data quality, not model capacity, bounds current performance.**
- **B11 Capital / reimbursement / investment cycle.** >USD 100B invested in AI across life sciences 2022–2026 with zero approvals [E-2061][E-2053]; Exscientia cut to two programmes [E-2034]; BenevolentAI laid off ~180 and delisted [E-2036][E-2037]; Recursion cut 20% of staff [E-2040]; Schrödinger is shopping both remaining clinical assets [E-2042]. **Evidence: strong. Capital discipline is already forcing pipeline contraction ahead of any clinical verdict.**
- **B12 IP / FTO congestion.** AI-native developers file compound patents disclosing less in vivo evidence than traditional developers, which the authors argue may push claims ahead of evidence and dampen downstream R&D [E-2059]; a 2026 follow-up documents new inventorship and disclosure challenges [E-2060]. **Evidence: moderate, from two peer-reviewed publications by the same independent authors.**
- **B13 Talent and organisational absorptive capacity.** Indirect. Median 6.5 years from company founding to first Phase 1 across 63 AI-native companies [E-2054]; Isomorphic was "staffing up" for trials four years after founding [E-2049]. [INFER] The gap between per-programme speed claims and organisation-level slowness is consistent with an absorptive-capacity constraint, but this block collected no direct workforce data. **Evidence: weak, suggestive only.**
- **B14 Biosecurity and model regulation.** No evidence collected in this block. Nothing in the clinical, benchmark or census record encountered a biosecurity or model-access constraint. **Evidence: none. This block makes no claim about B14 in either direction.**

---

## 9. Verdict on Q1, stated quantitatively

**Q1: To what extent is the claim that AI has actually compressed protein structure prediction / sequence design / molecular generation empirically substantiated?**

The claim decomposes into four sub-claims, which have four different answers.

**(1) AI compressed *computation* on structure and sequence — SUBSTANTIATED.**
AlphaFold2/3 and ESMFold produce structures at CASP-level accuracy (ESMFold median TM 0.95, AF2 0.96) [E-2019] across >200 million proteins [E-2018]. De novo binder design reaches a pooled 11.6% experimental success rate across 3,766 designs and 15 targets [E-2020], with the best methods reporting 16–68% on selected tasks [E-2023]. Prospective docking against unrefined AF2 models matches experimental structures (54% vs 51%; 26% vs 23%) [E-2012]. **This is real and it is measured.**

**(2) AI compressed *discovery-stage elapsed time* — PARTIALLY SUBSTANTIATED, at roughly 30–50% on preclinical activities.**
Two peer-reviewed reviews independently report 30–50% reduction in screening and candidate-selection time [E-2009][E-2010]. Company claims of 12–18 month target-to-candidate against a 4–6 year norm imply 2.5–4.5 years saved [E-2070], but are company-issued, unmatched to any control cohort, and in one flagship case (DSP-1181) run against a heavily precedented target [E-2032]. **Defensible figure: 30–50% on preclinical steps. Not defensible: the 4-year-per-programme framing.**

**(3) AI compressed *time to a dosed patient* — NOT SUBSTANTIATED.**
Median founding-to-Phase-1 across 63 AI-native companies is **6.5 years** [E-2054]. Clinical development timelines are explicitly reported as essentially unchanged [E-2009]. Isomorphic Labs: zero registered trials at 2026-08-18 [E-2048]. DSP-0038: five years in Phase 1 [E-2069]. **The compression does not propagate.**

**(4) AI raised clinical probability of success — 증거 없음 / NO EVIDENCE.**
Phase II ~40% vs conventional ~37% [E-2003][E-2011], on 8 completed Phase 2 assets [E-2055] against the ~4,126 per arm the comparison would require [E-2065]. Zero approvals [E-2053]. Attrition unchanged at ~90% [E-2061]. See §3.4.

### The system-level answer

**AI has compressed a step that is 1.0–3.4% of the IND base rate [E-2057], by 30–50% in duration [E-2010], with a probability-of-success effect that is statistically indistinguishable from zero [E-2065]. The resulting ceiling on annual approvals is +0.8% to +2.7% relative in the most AI-favourable published scenario, +0.6% to +1.9% in the empirically supported one, and 0% if the Phase I advantage is selection bias [E-2058].**

[INFER] Applying the common brief's definition — a rate-limiting step is one whose improvement actually increases total system output — **discovery-stage molecule generation does not currently satisfy it.** The step improved measurably and system output did not move. That is the operational signature of a non-constraint. The nine terminated assets in §6 failed on target validity, exposure, efficacy and toxicity [E-2033][E-2035][E-2039][E-2041][E-2043] — never on the inability to find or build a molecule.

**Bearing on H0.** H0 asserts that discovery *was* the historical rate-limiting step and that preclinical/clinical *will become* rate-limiting as AI advances. This block does not test the first half (that is H0-a, and it belongs to the historical evidence blocks). On the second half, the evidence here is that **preclinical/clinical is not becoming rate-limiting — on this dataset it already was, throughout the entire period AI has been active.** Every AI-derived asset that has failed, failed there. [INFER] The sequencing H0 proposes — discovery first, then clinical — is not visible in the data; what is visible is a constraint that never moved, in front of a step that got faster.

---

## 10. UNRESOLVED

Ten items, fully documented in `RLSX/work/B/unresolved.csv` with every query attempted, the failure reason, at least three alternative sources tried for each, and a current best estimate with its basis.

| # | Item | Blocker | Best estimate |
|---|---|---|---|
| 1 | Jayatunga Phase I denominator | Elsevier paywall, HTTP 403; no OA deposit | n ≈ 21–30; 95% CI at n=24 is 66.1–94.3% [E-2066] |
| 2 | Jayatunga Phase II denominator | same | n ≈ 5–12, most likely 8–10; CI at n=8 is 15.2–71.3% [E-2065] |
| 3 | Jayatunga company list and "AI-discovered" definition | same | Broad, self-report-based inclusion rule; cohort ≈ the 8–15 best-known AI-native firms plus pharma partners |
| 4 | Formal published rebuttal to Jayatunga | none exists | Critique is distributed across three post-hoc reviews [E-2006][E-2007][E-2061], not concentrated |
| 5 | Numeric rate in the "RFdiffusion low success" preprint | bioRxiv HTTP 429 on all attempts | Below the 11.6% pooled figure, plausibly 0–5% for functional binders |
| 6 | AlphaFold3 SBDD enrichment numbers | bioRxiv HTTP 429 on all attempts | Between AF2 apo-quality and experimental holo; qualitative 5 Å threshold recovered [E-2017] |
| 7 | Isomorphic Labs' first candidate ("ISM8969") | Only low-quality aggregators; "ISM" is Insilico's naming convention; registry returns zero | Unverified and probably erroneous; zero registered trials confirmed [E-2048] |
| 8 | Cradle Bio pipeline | No pipeline exists; tools vendor | Zero clinical assets; absent from both field-wide censuses [E-2054][E-2055] |
| 9 | Regulator-sourced AI-derived IND count | FDA does not tag INDs by discovery method; registries carry no AI-provenance field | 1.0–3.4% of commercial INDs, derived [E-2057] |
| 10 | Genesis Therapeutics named clinical asset | No company disclosure | Zero named clinical assets [E-2052] |

Items 1–3 are the most consequential: they are the reason the Phase I claim is carried in this report with confidence intervals rather than as a point estimate. Item 5 and item 6 do not affect any conclusion, because independent measurements with fully retrieved numbers were substituted in both cases — the 3,766-design pooled meta-analysis [E-2020] and three peer-reviewed AF2 screening benchmarks [E-2012][E-2015][E-2016].
