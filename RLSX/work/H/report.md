CHARTER_ACK: R1,R2,R3,R4

# Agent H — Data, Experimental Infrastructure and Automation (B9 / B10)

Evidence block: **E-7001 … E-7107** (71 records) in `RLSX/evidence/parts/H.jsonl`.
Structured data: `RLSX/data/dbtl_throughput.csv` (76 rows).
Unresolved ledger: `RLSX/work/H/unresolved.csv`.

---

## 0. Methodology

**Scope.** Two bottleneck candidates from the common catalog: **B10** (scarcity/quality of experimental training data) and **B9** (wet-lab DBTL throughput), plus the ratio that connects them — design generation capacity divided by experimental validation capacity.

**Rules applied.**
1. Every factual sentence carries an `[E-####]` chip. My own reasoning carries `[INFER]`.
2. Every computed quantity is logged as a `type:"derived"` record with the formula and its input evidence IDs (E-7100 … E-7107). No derived number appears in this report without a matching ledger record.
3. **Nominal vs effective throughput are never merged.** A well read on a screening line is a nominal unit. A design that receives an experimental readout capable of changing a go/no-go decision is an effective unit. The CSV `ratio_role` column marks which figures feed the ratio, and every vendor/company figure is typed `company_reported` in the CSV and `secondary` in the ledger with the company named in `authors_or_org`, so Agent R can apply S4.
4. **Demonstration vs production is treated as a first-class distinction** throughout Part 2. The `setting` column carries it row by row. Every autonomous-lab throughput number found in the literature comes from a demonstration run of days-to-weeks duration; none of them is a measured routine operating rate of a production pipeline, and I say so wherever the number appears.
5. Basal state: H0 is not assumed. Agent C's B9/B10 rankings and Agent B's pass-rate finding were treated as claims to re-test, not inputs to inherit. Where my finding agrees with C, it is because independent evidence points that way; where it does not, Section 6 says so.
6. 30 WebSearch/WebFetch calls were made. Four fetches were blocked (ACS 403, Nature IdP redirect, bioRxiv 429, Chemistry World 405) and were routed to alternative sources; the one item that could not be fully recovered is in UNRESOLVED.

**Definition used for "meaningfully tested".** A design counts in the denominator only when the experiment produces a per-design quantitative readout on the property being optimised. A pooled selection that returns an enrichment score for a library is counted separately from per-variant biophysical measurement, because the two carry very different information per design. This distinction turns out to drive the whole result.

---

## 1. Part 1 — the upstream data constraint (B10)

### 1.1 Scale of usable public data

| Resource | Size | Growth / note |
|---|---|---|
| PDB, cumulative released experimental structures | 258,403 [E-7001] | 12,584–17,610 released per year 2021–2025 [E-7002] |
| Human proteome residue coverage, experimental only | 17% [E-7003] | rose to 76% including AlphaFold models [E-7004] |
| AlphaFold confident residue coverage of human proteome | 58% (36% very high) [E-7005] | 98.5% of proteins covered at some confidence [E-7005] |
| ChEMBL v35 | 21.1M activities, 2.5M compounds, 1.7M assays, 16k targets [E-7006] | curated from literature |
| PubChem | 295M bioactivities, 1.67M assays, 119M compounds [E-7007] | dominated by qualitative HTS active/inactive flags [E-7007] |
| BindingDB | 3.2M binding measurements, 1.4M compounds, 11.5k targets [E-7008] | 1.6M curated in house [E-7008] |
| MELLODDY private corpus (10 pharma) | 2.6B activity datapoints, 21M compounds, 40k assays [E-7009] | private |

The PDB's growth is worth stating precisely, because it is often described as exponential. Annual releases moved from 14,000 (2020) to 17,610 (2025) [E-7002] — roughly 4–5% compound annual growth, not doubling. [INFER] The structural-biology data supply is therefore expanding on a timescale of decades, not of model generations; any structure-hungry method that needs an order of magnitude more experimental structures will not get it from deposition growth.

**Private versus public.** The proprietary pool is roughly **123x the public curated pool in aggregate and about 12x per individual pharma company** (2.6e9 / 2.11e7) [E-7101, from E-7009 + E-7006]. On compounds the ratio is 8.4x [E-7101]. The caveat is logged in the derivation: MELLODDY counts every measurement including replicates and routine PK/PD panels while ChEMBL counts curated literature extractions, so the ratio bounds rather than measures the gap [E-7101].

### 1.2 Negative and null data — how little is published

- Only about 60% of approved animal study protocols yield any publication, and about 62% of animal-research abstracts are later published [E-7012].
- Researchers themselves estimate ~50% of animal experiments are published; respondents from **for-profit** organisations estimated **10%** [E-7013]. Lack of statistical significance was a leading stated reason for non-publication [E-7013].
- In synthetic chemistry, low-yielding and failed reactions are rarely published at all; the Open Reaction Database was built partly to eliminate the positive/negative reporting distinction [E-7014].
- The cost of that omission is now measured: a reaction-outcome model reached state-of-the-art from as few as 20 positive datapoints when supported by a negative set at least **40x larger** [E-7015]. [INFER] That is the sharpest available statement that the missing data are not marginal — the negative set carried more of the learning signal than the positive set in that setting.

**MELLODDY — what it actually demonstrated.** MELLODDY completed and published. It ran federated QSAR training across 10 pharma partners on 2.6B confidential datapoints, 21M compounds and 40k assays [E-7009]. Federated multi-partner models beat single-partner models in almost all cases, but the magnitude was small: for the majority of tasks the relative improvement of proximity-to-perfection exceeded **4% in AUC-PR and 2% in R2**, with the best-served partner reaching 12.5% AUC-PR and 4.8% R2 [E-7010]; median conformal-efficiency (applicability-domain) gain was **5.5%**, maximum 9.7% [E-7011].

[INFER] The correct reading of MELLODDY is a **negative result for the data-quantity hypothesis and a mildly positive result for the data-coverage hypothesis**. Pooling a 100x-larger corpus than all of ChEMBL, across ten of the world's largest compound collections, bought single-digit percentage-point relative improvements in predictive metrics. If access to ~10x more proprietary data per partner yields ~4% relative metric improvement, then the marginal return to bioactivity data volume in this domain is very low. The applicability-domain gain (5.5% conformal efficiency [E-7011]) is the more meaningful part: what federation bought was slightly wider chemical coverage, not better prediction inside the covered region.

### 1.3 Assay standardization and reproducibility

Industry replication attempts:
- Amgen confirmed 6 of 53 landmark preclinical oncology papers — 11% [E-7016].
- Bayer found 43 of 67 in-house target-validation projects (64%) inconsistent with the publications [E-7017].

Both are flagged `circular_risk: true` in the ledger [E-7016, E-7017]: neither disclosed which papers were selected, by what criteria, or the replication protocols, so the numbers cannot be independently re-derived. They are widely re-cited without that caveat.

The peer-reviewed replacement is the Reproducibility Project: Cancer Biology:
- Across 136 positive original effects the **median replication effect size was 85% smaller** than the original, and 92% of replication effects were smaller [E-7018].
- Editors classified 17 completed Replication Studies as 5 reproducing, 6 equivocal, 2 uninterpretable, 4 failing — implying a positive predictive value of about **47%** under a favourable assumption and **16%** on an intention-to-treat basis over the 50 originally selected papers [E-7020].

The published critique of these numbers is structural rather than arithmetic: the project **could not execute most of what it planned**. 50 papers were selected but only 17 full Replication Studies were completed; 12 Registered Reports were abandoned; 26% of original authors were extremely helpful but **32% were unhelpful or did not respond**, and missing methodological detail and unavailable reagents made some attempts impossible [E-7019]. [INFER] This is a survivorship problem that cuts in the pessimistic direction: the papers that *could* be replicated were the ones with the most complete methods and the most cooperative authors, which is a positively selected subset. The 16% intention-to-treat figure [E-7020] is the honest denominator; the 47% figure is conditional on completion.

**Assay variability.** A five-centre LINCS study found conventional IC50 measures confounded by inter-lab variation in plating density, media composition and intrinsic cell division rates [E-7025]. Liquid handling alone shifts measured potency by up to **100-fold** — tip-based serial dilution versus acoustic dispensing on the same compounds [E-7026]. The NCI-60, run under strict SOPs since 1985 across 52,585 compounds and ~2.8M compound/cell-line combinations, still shows high variability [E-7027]. Pooling IC50/Ki values across sources is itself an additional documented noise source [E-7024].

### 1.4 The crucial point — label noise bounds achievable model accuracy

Measured label noise in public bioactivity data:
- Public Ki: mean error 0.44 pKi, **SD 0.54**, median 0.34, after removing unit-transcription errors and repeated citation of a single measurement (90% of matched pairs) [E-7021].
- Heterogeneous public pIC50: **SD 0.68 log units** [E-7022].

**Derivation [E-7100].** Under the standard measurement-error model y = t + e with e independent of t:

> R2_max = 1 − sigma_e^2 / sigma_y^2   and   r_max = sqrt(R2_max);   RMSE floor = sigma_e

With sigma_e = 0.68 [E-7022]:

| label spread sigma_y (log units) | 1.0 | 1.2 | 1.5 | 2.0 |
|---|---|---|---|---|
| **max achievable R2** | 0.538 | 0.679 | 0.794 | 0.884 |
| **max achievable r** | 0.733 | 0.824 | 0.891 | 0.940 |

With curated Ki data (sigma_e = 0.54 [E-7021]) the ceilings rise to 0.709 / 0.797 / 0.870 / 0.927 for the same spreads [E-7100]. The **RMSE floor is 0.68 log units, about 4.8-fold in potency** [E-7100] — no model, of any architecture, trained on any amount of data, can score better than that against heterogeneous public pIC50 labels.

An important qualification, and one the source makes explicitly: apparent error against noisy labels rises **2.9 to 55 times faster** than true error as noise is added, so models can be more accurate than their own training labels, and evaluation on error-laden test sets misstates real performance [E-7023]. [INFER] The correct conclusion is therefore two-sided. The ceiling binds *measured benchmark scores* hard — benchmark leaderboards in this domain have a low, computable saturation point and are already near it. It binds *real-world utility* less tightly, because a model can learn the underlying signal through the noise. But it binds *decision quality in the lab* fully, because when the experiment that adjudicates the model is itself the noisy assay, neither the model nor the experimenter can tell a correct prediction from a lucky one. Noise in the label is noise in the referee.

### 1.5 Data scaling and diminishing returns

Chemical foundation models show diminishing returns with scale: loss approaches a plateau under the current data regime, and each doubling of data or parameters yields progressively smaller improvements [E-7028]. Combined with MELLODDY's single-digit gains from a ~100x data increase [E-7010, E-7011] and the computed noise ceiling [E-7100], the three lines of evidence agree. [INFER] **The binding constraint on bioactivity models is the noise floor of the labels, not the count of the labels.** Adding data of the same quality moves a model asymptotically toward a ceiling that is set by sigma_e, and the measured sigma_e has not improved — the Ki figure is from 2012 [E-7021] and the pIC50 figure from 2021 [E-7022], and the inter-lab and dispensing effects [E-7025, E-7026] are unaddressed at scale.

---

## 2. Part 2 — DBTL cycle throughput (B9)

**Reading rule for this section:** every figure below is tagged demonstration / production / benchmark / survey, matching the `setting` column of the CSV. Conflating a demonstration rate with a production rate is the standard error in this literature, and the gap is large.

### 2.1 Design — effectively unbounded

Diffusion backbone generators need on the order of 1000 forward passes per sample; a flow-matching alternative produced 1040 backbones of length 60–320 in 1.9 GPU-hours [E-7029] — **547 backbones per GPU-hour**. One 8-GPU node at 60% duty gives **2.3e7 designs/year** [E-7103, arithmetic 547 x 8 x 0.6 x 8760].

On the small-molecule side the enumerated make-on-demand space is 94.5 billion molecules [E-7032, vendor-stated], and a single V-SYNTHES2-class campaign addresses 36 billion compounds while physically docking under 0.1% of them, at over 1000x acceleration [E-7057].

[INFER] Design capacity is bounded only by the compute budget and is therefore not a constraint at any level of the pipeline. Its order of magnitude is 1e7/year per modest GPU node for protein designs and 1e10–1e11/year for scored small-molecule designs.

### 2.2 Build

| Item | Value | Setting | Source type |
|---|---|---|---|
| Gene fragment list price | $0.07/bp [E-7030] | production | vendor |
| Same, 2017 | $0.25–0.60/bp [E-7031] | production | vendor |
| **Annualised list-price decline 2017 to 2025** | **14.8–23.8%/yr; 3.6–8.6x total** [E-7102] | derived | derived |
| Gene fragment express turnaround | from 2 business days [E-7030] | production | vendor |
| Make-on-demand compound delivery | 3–4 weeks, >80% success [E-7032] | production | vendor |
| Automated/HT library synthesis success rate | 50–80% [E-7046] | demonstration | peer-reviewed |
| Automated stopped-flow reaction throughput | 112 reactions/day [E-7047] | demonstration | peer-reviewed |
| Parallel protein expression + purification | 96 in parallel; hundreds/week/operator; yields to 400 ug [E-7048] | production | peer-reviewed |
| Expression screening from plasmid receipt | 96 constructs/week [E-7049] | production | peer-reviewed |

Both gene-synthesis endpoints are vendor list prices [E-7030, E-7031], so [E-7102] measures list-price trend, not realised cost of goods — stated in the derivation record.

The **automated-versus-manual synthesis comparison** is the load-bearing one. AI-planned robotic flow synthesis exists and works for multistep routes [E-7046], but the reported average library success rate of 50–80% [E-7046] is *below* the 80%+ that a purely combinatorial make-on-demand catalogue achieves on pre-validated protocols [E-7032]. [INFER] Automation has not raised per-compound success on genuinely novel chemotypes; what it has done is make *pre-validated* chemistry cheap and fast. The novel-chemotype build leg remains manual-rate.

### 2.3 Test — where nominal and effective diverge hardest

| Assay | Nominal throughput | Setting |
|---|---|---|
| Industrial HTS | 1e4–1e5 compounds/day; 2e5/day at 1536-well [E-7033] | production |
| DEL selection | ~1e9 library members per selection, one tube [E-7034] | production |
| Phenomic imaging | 2.2M "experiments"/week, company-reported [E-7035] | production, vendor |
| Display selection (antibody) | ~1e9 variants per selection [E-7054] | production, vendor |
| Frontier binder-design campaigns | 20 designs/target [E-7050]; 30–100/target across methods [E-7053] | demonstration |
| Independent RFdiffusion evaluation | 30 designs total (5 x 6 targets) [E-7052] | benchmark |
| Microphysiological systems | 96 chips/plate maximum [E-7055] | production |

Three of those rows are not what they appear:
- Recursion's 2.2M/week [E-7035] counts one imaged well/perturbation as one "experiment". It is a company-reported figure and is a **data-generation** rate, not a candidate-decision rate.
- DEL [E-7034] and display [E-7054] interrogate 1e9 members but return a **pooled enrichment score**, confounded by expression bias and avidity. Only sorted leads receive individual SPR/BLI [E-7054].
- Organ-chips and other assays with plausibly higher clinical predictivity sit at **96 units per plate maximum** [E-7055] — four orders of magnitude below nominal uHTS [E-7033].

[INFER] **The throughput of an assay and its predictive validity are inversely ordered across this table.** The 1e9-per-tube assays give the least information per design; the assays most likely to predict a clinical outcome are the ones capped near 1e2 per plate.

### 2.4 Learn — cycle latency, demonstration versus production

**Demonstration figures** (all are days-to-weeks single runs, none is a routine operating rate):
- A-Lab: 41 of 58 targets over 17 days, **21 experiments/day** [E-7042]. An independent reanalysis by Palgrave and colleagues concluded the XRD evidence did not support the claim of 41 novel compounds, with materials already in the ICSD, and the Nature paper was subsequently corrected [E-7043].
- Mobile robotic chemist: 688 experiments in 8 days, **86/day**, on a single ten-variable optimisation, finding a 6x more active photocatalyst mixture [E-7044].
- Chai-2: design-to-wet-lab-validation in under two weeks per target, 24-well-plate scale, company-reported [E-7050].
- A 2025 peer-reviewed SDL review characterises today's systems as producing reliable data over days-to-weeks of continuous operation **in narrow, well-defined domains**, with the fully autonomous scientist still aspirational [E-7056].

**Production figures:**
- Aspirational medicinal-chemistry DMTA cycle: about 5 working days; real cycles are reported in weeks [E-7045].
- Ginkgo's Nebula: 168 scheduled instrument-hours/week across 100+ devices [E-7037] — an *availability* figure, company-reported, not a completed-experiment count.
- Insilico Medicine: 18 months project-start to development candidate at ~$2.6M, under 30 months to Phase I, 12–18 months average across 20 candidates 2021–2024 [E-7058] — company-reported, no independent audit.

[INFER] **The demonstration-to-production gap is roughly one to two orders of magnitude in sustained rate.** A-Lab's 21 experiments/day [E-7042] and the mobile chemist's 86/day [E-7044] are single-problem, single-assay, short-horizon runs on tightly bounded parameter spaces; the production analogue is a medicinal-chemistry program on a weeks-long DMTA cycle [E-7045]. Nothing in the surveyed literature reports a production pipeline sustaining a demonstration-grade rate across a full year and a heterogeneous problem set. The A-Lab correction [E-7043] is the cautionary case: the headline demonstration number survived, the scientific claim it supported did not.

**Queueing versus processing.** The best available characterisation of where the latency sits is the cloud-lab post-mortem: unpredictable scheduling on shared instruments and sample-handling steps that still require humans are named as core failure modes, alongside ~$5M of capital equipment per automated pipeline [E-7041]. Ginkgo's own framing of Nebula as a **fourfold increase in available laboratory hours** by moving to 168 h/week [E-7037] is itself an admission that the prior binding factor was instrument availability (queue), not instrument speed (processing). [INFER] Both data points point the same way — the dominant term in DBTL latency is waiting, not running — but neither is a measured queue-time decomposition, and I could not find one. That item is in UNRESOLVED with a quantified best estimate.

### 2.5 Self-driving labs and cloud labs — the real installed base, verified as of 2026

| Platform | Status verified 2026 | Throughput / cost | Source type |
|---|---|---|---|
| **Emerald Cloud Lab** | **Operating.** ~189 employees; cut ~30 jobs and closed South San Francisco in 2023, relocated facility to Austin [E-7039]. No 2025–2026 closure found. | 150+ remotely controllable instruments as of July 2020 [E-7040] — the most recent published instrument count located | company-reported |
| **Strateos** | **No longer an independent cloud lab.** Acquired by Multiply Labs, Dec 2023, after headcount fell 147 to 68 and a pivot from centralized labs to on-site consulting; the Eli Lilly Life Sciences Studio it ran in San Diego was sold to Arctoris in Sept 2024 and moved to Oxford [E-7038] | not disclosed | company-reported |
| **Ginkgo Bioworks Foundry** | **Operating but sharply contracted.** Q2 2026 revenue $20.2M, −48% YoY, GAAP net loss $57.3M; Foundry consolidated into a few core sites with up to 60% footprint reduction [E-7036] | Nebula: 168 scheduled h/week, 100+ devices [E-7037] | SEC filing + company-reported |
| **A-Lab** | Demonstration platform, published 2023 [E-7042]; central novelty claim contested and the paper corrected [E-7043] | 21 experiments/day, 17-day run [E-7042] | peer-reviewed + correction |
| **Chemputer / mobile robotic chemist** | Demonstration platform [E-7044] | 86 experiments/day, 8-day run [E-7044] | peer-reviewed |
| **Recursion** | Operating internal platform | 2.2M imaged experiments/week; 65 PB [E-7035] | company-reported |
| **Insitro** | Operating internal platform; acquired CombinAbleAI Jan 2026, TherML integrated with its automated labs [E-7060] | not disclosed | company-reported |
| **Arctoris** | Operating; launched a Biophysics Centre of Excellence March 2026 with a claimed 10x capacity increase (base undisclosed) [E-7059]; absorbed the ex-Lilly/Strateos San Diego automation [E-7038] | not disclosed in absolute units | company-reported |
| **Automata** | **Operating.** London integrator; Molecular Devices (Danaher) announced LINQ integration Jan 2026 [E-7064] | claimed 5x sample throughput and 95% fewer manual interactions vs an unspecified manual baseline; absolute samples/day not disclosed [E-7064] | company-reported |

Cost per experiment is not disclosed by any of these operators in a comparable unit. The one cost anchor found is a practitioner estimate of ~$5M capital per automated pipeline [E-7041].

[INFER] The installed base is smaller and more fragile in 2026 than the sector's rhetoric implies. One of the two flagship general-purpose cloud labs was absorbed [E-7038], the other survived a relocation and layoffs [E-7039], and the largest public foundry is halving its footprint against a 48% revenue decline [E-7036]. The platforms that are growing are **captive** ones inside AI-first drug companies (Recursion [E-7035], Insitro [E-7060]) — that is, automation is succeeding where it is vertically integrated with a specific decision problem and failing as a general-purpose utility.

---

## 3. Part 3 — the central test: 설계 과잉·검증 부족 (design surplus, validation deficit)

> **R = (AI design generation capacity, designs/year) / (experimental validation capacity, designs meaningfully tested/year)**

### 3.1 Workflow 1 — de novo protein binder design [E-7103]

**Numerator.** 547 backbones/GPU-hour [E-7029]. Group scale, one GPU at 60% duty: 547 x 0.6 x 8760 = **2.9e6/year**. Platform scale, one 8-GPU node: 547 x 8 x 0.6 x 8760 = **2.3e7/year**.

**Denominator.** Frontier campaigns test 20 designs/target [E-7050] and 30–100/target across methods [E-7053]; an independent evaluation tested 30 designs in total [E-7052]. Protein production supports 96 in parallel and hundreds per week per operator [E-7048, E-7049] -> 300/week x 48 weeks = **1.44e4/year** for a dedicated platform; **~5e2/year** for a single academic group.

**Arithmetic.**
- Group scale: 2.9e6 / 5e2 = **5.8e3**
- Platform scale: 2.3e7 / 1.44e4 = **1.6e3**

**R = 5e2 to 2e3 central, outer bound 1e2 to 1e4** [E-7103]. Uncertainty is dominated by the denominator: whether "tested" means expressed-and-screened (upper denominator) or fully characterised for affinity and specificity (lower denominator) moves R by ~30x.

### 3.2 Workflow 2 — small-molecule hit-to-lead [E-7104]

**Numerator.** One giga-scale campaign addresses 3.6e10 compounds [E-7057] against a 9.45e10-molecule enumerated space [E-7032]. Take one campaign per year as the unit: **3.6e10 designs scored/year**.

**Denominator (a), nominal.** Industrial HTS at 1e5 compounds/day x 200 operating days = **2.0e7 wells/year** [E-7033]. At 1536-well 2e5/day: 4.0e7.
-> R = 3.6e10 / 2.0e7 = **1.8e3** (900 at 1536-well).

**Denominator (b), effective.** A hit-to-lead program on a ~1-week DMTA cycle [E-7045] ordering make-on-demand batches on a 3–4 week turnaround [E-7032] physically makes and tests on the order of **5e3 novel designed compounds/year**.
-> R = 3.6e10 / 5e3 = **7.2e6**.

**The two denominators differ by ~4000x** [E-7104]. This is the nominal-versus-effective gap made concrete: HTS wells re-test an existing deck; they do not test the molecules the model designed.

### 3.3 Workflow 3 — antibody affinity maturation [E-7105]

**Numerator.** Sequence-level generative models are far cheaper per sample than structure diffusion [E-7029]; take a conservative **1e8 designed sequences/year** for one group.

**Denominator (a), pooled display.** 1e9 variants interrogated per selection [E-7054].
-> R = 1e8 / 1e9 = **0.1**.

**Denominator (b), per-variant biophysics.** Only sorted leads receive individual SPR/BLI [E-7054]; 1e2–1e3 variants individually characterised per year.
-> R = 1e8 / 1e3 = **1e5**, to 1e8 / 1e2 = **1e6**.

**In this workflow, nominal validation capacity exceeds design capacity by 10x.** [E-7105]

### 3.4 Cross-workflow result

R spans **0.1 to 7.2e6 — roughly 7–8 orders of magnitude** across three workflows [E-7107]. [INFER] A single "design surplus" number for AI-driven discovery is not a meaningful quantity. What is real is a much narrower statement: **wherever validation requires per-design, per-molecule physical work, R is 1e3–1e7; wherever validation is pooled, R falls to or below 1.**

### 3.5 Verdict [INFER]

**The binding constraint is the predictive validity of the validation assays, not their throughput.** Five independent lines converge:

1. **The elasticity is measured and it favours validity.** A 0.1 absolute change in the correlation between a decision tool's output and clinical utility outweighs a 10x throughput change across much of the realistic parameter space [E-7061]. Converting to equal proportional effort [E-7106]: a 10% throughput gain is worth delta-r of about 0.0041, while a 10% relative validity gain from a base r of 0.3–0.6 is worth delta-r of 0.03–0.06 — **validity is 7–15x more elastic (central ~12x)**. Concretely, one classifier at r = 0.9 screens 14 candidates per true positive while a four-step cascade at r = 0.3 screens ~739, a 33x burden increase from a modest validity decline [E-7062].
2. **The workflow where throughput is already abundant did not become unblocked.** Antibody affinity maturation has R of about 0.1 [E-7105] — pooled display out-throughputs generative design by 10x — and it is not a solved problem. That is a direct falsification test of the throughput hypothesis, and the throughput hypothesis fails it. What display gives is 1e9 *low-information* readouts confounded by expression bias and avidity [E-7054].
3. **The assays that predict best have the least throughput, and adding robots does not change that ordering.** Microphysiological systems cap at 96 chips/plate [E-7055] against 2e5 wells/day for HTS [E-7033]. Buying more HTS capacity moves the wrong variable.
4. **The label-noise ceiling caps the model, and it is an assay property.** R2_max = 1 − sigma_e^2/sigma_y^2 gives 0.54–0.88 depending on label spread, with a hard RMSE floor of 0.68 log units [E-7100, from E-7022]. Robots do not reduce sigma_e; assay redesign and standardization do. Dispensing method alone moves measured potency 100-fold [E-7026].
5. **The 100x data experiment was run and it returned single-digit gains.** MELLODDY: ~4% AUC-PR RIPtoP for most tasks, 5.5% median conformal efficiency [E-7010, E-7011] from a corpus 123x the public one [E-7101].

**Quantifying the relative contribution.** Using the derived elasticity [E-7106] as the exchange rate: on a per-unit-of-proportional-improvement basis, validity contributes roughly **12x more** to system output than throughput. [INFER] Multiplying by the plausible headroom in each — throughput is improvable by perhaps 10x within a decade on existing automation trends [E-7037, E-7048], while predictive validity in preclinical models has a headroom of at most delta-r of about 0.2–0.3 given that only 16% of published preclinical findings survive intention-to-treat replication [E-7020] — the two are closer in *total* addressable gain than the per-unit elasticity suggests, but validity still dominates: a delta-r of 0.2 is worth roughly two 10x throughput gains stacked [E-7061].

**The honest qualifier.** This verdict does not say throughput is free. In de novo binder design R is 1e3 [E-7103] and in novel-compound medicinal chemistry R is 1e6–1e7 [E-7104]; at those ratios the model is generating vastly more hypotheses than can be adjudicated, and *some* throughput increase converts directly into more adjudicated hypotheses. What the evidence says is that this conversion has a low exchange rate [E-7061, E-7106] and that it saturates: once you can test 1e4/year instead of 1e2, you are still selecting which 1e4 using a scoring function whose correlation with clinical utility is unknown and probably low. **More robots buys you a bigger sample from the same badly-calibrated prior.**

---

## 4. Assay predictive validity vs throughput

These are two different constraints with two different remedies, and the literature routinely merges them.

| | **Throughput constraint** | **Predictive-validity constraint** |
|---|---|---|
| What is scarce | experiments per unit time and cost | correlation between assay readout and clinical utility |
| Measured today | 2e5 wells/day HTS [E-7033]; 1e9/selection DEL and display [E-7034, E-7054]; hundreds of proteins/week [E-7048] | r is unmeasured for nearly every assay in use; the concept is defined and modelled but the value is not routinely estimated [E-7063] |
| Symptom | designs queue; R = 1e3–1e7 [E-7103, E-7104] | high-throughput campaigns produce hits that fail downstream; PPV of published preclinical findings ~16% ITT [E-7020] |
| Remedy | more robots, more capital, longer instrument hours [E-7037, E-7041] | better disease models, assay standardization, orthogonal readouts, honest negative-data reporting [E-7014, E-7025, E-7026] |
| Elasticity | +10% -> delta-r equivalent 0.0041 [E-7106] | +10% from r=0.5 -> delta-r 0.05, i.e. ~12x larger [E-7106] |
| Does the other remedy help? | more validity does not raise throughput | **more robots does not raise validity at all** |

Scannell and colleagues state the asymmetry directly: industry has compensated for weak models by raising throughput, detectability of good candidates is extremely sensitive to predictive validity, and validity is systematically under-managed precisely because it cannot be measured until outcomes are known [E-7063].

[INFER] There is one mechanism by which automation *can* touch validity, and it should be stated rather than dismissed: automation reduces operator-to-operator variance, and operator variance is a documented component of sigma_e — plating density, media composition, dispensing method [E-7025, E-7026]. Removing the 100-fold dispensing artefact [E-7026] is a real validity gain achievable with hardware. But it addresses *precision*, not *relevance*. A perfectly precise measurement in a cell line that does not model the disease has r near zero, and no amount of robotic precision moves it. The two constraints are separable, and only one of them is being funded.

---

## 5. Where the constraint actually sits, by leg

| DBTL leg | Slack or tight | Evidence |
|---|---|---|
| Design | very large slack; 1e7/yr per GPU node [E-7029, E-7103] | not a constraint |
| Build (pre-validated chemistry / DNA) | large slack; $0.07/bp, 2-day turnaround, 94.5B enumerated space [E-7030, E-7032] | not a constraint |
| Build (novel chemotypes) | tight; 50–80% automated success, manual-rate [E-7046] | moderate constraint |
| Test (nominal, low-information assays) | large slack; 1e5–1e9 units per campaign [E-7033, E-7034, E-7054] | not a constraint |
| Test (high-predictive-validity assays) | very tight; 96 chips/plate [E-7055] | **constraint** |
| Learn (latency) | tight, dominated by queueing [E-7037, E-7041] | moderate constraint |
| Data (quantity) | slack; 123x more private data available, worth ~4% [E-7009, E-7010, E-7101] | not a constraint |
| Data (label noise / standardization) | very tight; R2 ceiling 0.54–0.88, RMSE floor 0.68 log [E-7100] | **constraint** |

---

## 6. B9/B10 ranking test — independent verdict on Agent C's placements

Agent C placed **B9 twelfth of sixteen** and **B10 eleventh of sixteen**, recording that screening throughput has slack. The verdict below is reached from the evidence above, not from C's reasoning.

### B9 (wet-lab / DBTL throughput) — **agree with 12th, conditional on the definition**

Elasticity argument [INFER, grounded in E-7061, E-7062, E-7106]: if B9 improves 10%, the change in annual approvals is worth about delta-r = 0.0041 in decision-tool validity [E-7106]. In the rare-positive regime that governs drug discovery, that is a very small movement in candidates-screened-per-true-positive [E-7062]. Independent confirmation comes from the market: the largest public foundry is cutting footprint up to 60% against a 48% revenue decline [E-7036], and one of the two flagship cloud labs was absorbed after a headcount collapse [E-7038]. A genuinely binding constraint does not have its suppliers going out of business for lack of demand — that is the signature of a step with spare capacity. **B9 at 12th is correct.**

**But the ranking hides a split.** B9 as *nominal* throughput has slack. B9 restricted to **throughput of assays with plausible clinical predictivity** does not: 96 chips/plate [E-7055], animal studies that are intrinsically low-throughput, and per-variant biophysics limited to 1e2–1e3/year [E-7054]. That sub-component sits with B1/B2 in the ranking, not at 12. Recommendation: **split B9 into B9a (nominal wet-lab throughput, rank ~12–13) and B9b (predictive-assay throughput, rank ~4–6).**

### B10 (training-data scarcity) — **partially disagree with 11th; it should be split and the quality half moved up**

- **B10a, data quantity.** C's placement is right, arguably generous. The decisive test was run: MELLODDY pooled 123x the public corpus [E-7101] and returned ~4% AUC-PR RIPtoP and 5.5% conformal efficiency [E-7010, E-7011]; chemical foundation models plateau under the current data regime [E-7028]. A 10% increase in data volume produces a change in approvals that rounds to zero. **Rank B10a 13th–14th, below C's 11th.**
- **B10b, label noise, standardization and negative-data reporting.** This should move **up to roughly 7th–9th**. The mechanism is direct and quantified: label noise sets a computable ceiling on every model trained or evaluated on the data (R2_max = 1 − sigma_e^2/sigma_y^2; RMSE floor 0.68 log units [E-7100]), and model quality *is* predictive validity, which is the highest-elasticity variable in the whole system [E-7061, E-7063]. A 10% reduction in sigma_e from 0.68 to 0.61 lifts the R2 ceiling from 0.679 to 0.741 at sigma_y = 1.2 [E-7100, same formula] — a 9% relative gain in the achievable ceiling, which by the elasticity exchange rate [E-7106] is worth roughly 12x what a 10% throughput gain delivers. Add the negative-data result: a 40x-larger negative set carried more signal than the positives in the reported setting [E-7015], and 10% is the for-profit estimate of how much animal work gets published [E-7013]. The remedies here are cheap relative to robots — reporting standards, assay SOPs, acoustic dispensing [E-7026], preregistration [E-7012].

**Why neither can rank higher than that [INFER].** Both act only on the discovery stage. Under the Amdahl constraint in the common brief (H0-c), the fraction of total development time and capital they can remove is capped by discovery's share, so however high their local elasticity, neither B9 nor B10 can be the top system constraint. Agent C's decision to keep both in the bottom third is directionally right; my correction is that **B10b is misplaced by about three ranks** because its effect propagates into every AI-mediated decision downstream, and that **B9 is two bottlenecks wearing one label**.

### On Agent B's finding

Agent B reports independently measured de novo design pass rates roughly an order of magnitude below developer self-reports. My evidence is consistent and adds the mechanism [INFER]: developer-run campaigns report 16–20% [E-7050], 10–100% [E-7051], 17–82% [E-7053] and >90% [E-7053], all on small, self-selected target panels of 20–100 designs per target; the one independent, non-developer evaluation located tested 30 designs across 6 targets and found most targets failing on expression, nonspecificity or undetectable affinity [E-7052]. The gap is not primarily a throughput problem — 20 designs per target [E-7050] is well within anyone's capacity to test. It is a **validation-design** problem: target selection, hit definition, and who runs the assay. That is the predictive-validity constraint appearing again, in the form the design field experiences it.

---

## 7. UNRESOLVED

Full records with all attempted queries, failure reasons, alternative sources and best estimates are in `RLSX/work/H/unresolved.csv`. Five items, summarised:

1. **Gene synthesis cost over a full 15-year window (2010 anchor).** A 2010-11 anchor was recovered only from a secondary relay of the Carlson series [E-7065], giving ~$1.30/base for simple genes and ~$0.10/base for raw oligos. The derived 15-year decline is therefore 18.6-fold (~18.7%/yr) on the gene anchor but only 1.4-fold on the oligo anchor [E-7108] — a wide band. The like-for-like 2017 to 2025 vendor window (14.8-23.8%/yr) is the defensible figure [E-7102].
2. **Queue-time versus processing-time decomposition of DBTL latency.** No published measurement located. Best estimate derived from the two available proxies [E-7037, E-7041] with the reasoning recorded.
3. **Absolute throughput in experiments/week for Automata, Arctoris, Insitro and Emerald Cloud Lab.** All four disclose only relative multiples or no figure at all [E-7064, E-7059, E-7060, E-7040]; operating status was verified for each, but comparable absolute rates were not published.
4. **Cost per experiment for cloud labs and foundries in a comparable unit.** Not disclosed by any operator surveyed; the only anchor is a capital-per-pipeline estimate [E-7041].
5. **Direct measurement of the correlation r between a named in vitro assay readout and clinical utility.** The predictive-validity literature defines and models this quantity but reports no measured value for any specific assay [E-7061, E-7063]; the source states the measurement is structurally hard because outcomes arrive years later [E-7063]. Best estimate and its basis are in the unresolved ledger. Every use of r in this report is either a source-supplied simulation parameter or an explicitly flagged `[INFER]`.
