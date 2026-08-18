CHARTER_ACK: R1,R2,R3,R4

# Agent C — Exhaustive Bottleneck Quantification (B1–B16)

Scope: all fourteen catalog candidates B1–B14, plus two new candidates surfaced by the search (B15, B16), each with current-state metric, ten-year trend, direct constraint evidence, modality variance (M5), region variance (M6), axis attribution (M1) and an improvement elasticity with an explicit uncertainty band (M2).

Evidence ledger: `RLSX/evidence/parts/C.jsonl`, IDs **E-3001 … E-3098** (96 records). Confidence grading is deliberately left null — that is Agent R's independent task under R3. Where I write `[INFER]` the sentence is my reasoning, not a sourced fact.

---

## 1. Methodology

### 1.1 Output definition
System output `Y` = annual approved new drugs, and the capital-efficiency variant `Y/$`. In steady state `Y = N × PoS`, where `N` is the number of programs entering clinical development per year and `PoS` is cumulative probability of success from Phase I. Anchors adopted after origin check: cumulative PoS 14.3% mean / 13.8% median across 18 large-cap firms on FDA approvals 2006–2022 [E-3002]; CDER cleared 46 novel drugs in CY2025 [E-3001]; median clinical development 9.1 years, 95% CI 8.2–10.0 [E-3004].

Anchor caution: reported phase-transition rates diverge sharply between datasets — one series reports 56.3 / 49.8 / 67.8 % for Phase I/II/III while another puts Phase II at 32.4 % [E-3003]. [INFER] The divergence is a denominator-definition artefact (trial-level vs program-level, and whether terminated-for-business programs count as failures). I therefore anchor elasticities on the **cumulative** LoA figure [E-3002], which has a disclosed sample and period, rather than on phase transitions.

### 1.2 The "constraint vs merely slow" test — how it was operationalized
A candidate was scored as an actual constraint only if at least one of four tests returned positive evidence:

- **T-Q (queueing)** — is there a waiting line with measured loss? (e.g. patients who never receive the product because a slot was unavailable)
- **T-U (utilization)** — is the resource operating at or near capacity, with capacity additions being absorbed rather than idling?
- **T-M (marginal return)** — is there a study or dataset showing that relaxing this factor moved output, or that a documented share of the resource is currently wasted?
- **T-N (natural experiment)** — has this factor been sharply relaxed or sharply tightened, and did output respond?

A candidate that is slow but **parallelizable** (add capacity in parallel and the queue clears) or that shows **idle capacity** fails all four and is scored non-binding regardless of how loudly it is complained about. Three candidates failed all four tests and are reported as negative findings: **B5 (regulatory review capacity), B13 (talent), B14 (biosecurity)**, with a partial negative on **B12 (IP)** and a split verdict on **B9 (wet-lab)** and **B6 (AAV suite capacity)**.

The single most informative negative is a genuine natural experiment: FDA lost roughly 3,500 staff in April 2025 [E-3031] and still cleared 46 CDER novel drugs [E-3001] / 53 including biologics while meeting nearly all goal dates [E-3029], with on-time performance slipping only from an 85–90 % band to 78 % [E-3030]. [INFER] A resource whose capacity can be cut that hard with that little output response was not the binding constraint.

### 1.3 Elasticity model (M2)
Elasticity is reported as **percent change in annual approvals per 10 % improvement in the named factor**, always as a range. Two channels, defined in derived record [E-3080]:

- **Probability channel** `ε_P = 10 × ((1−PoS)/PoS) × f × θ`, with PoS = 0.12 so `(1−PoS)/PoS = 7.33`; `f` = share of attrition attributable to the factor; `θ` = pass-through of a 10 % factor improvement into that attrition class.
- **Capital channel** `ε_C = 10 × c × τ × δ`, with `c` = share of capitalised cost the factor touches, `τ` = fraction of that cost responsive to the improvement, `δ` = marginal-program-quality discount (0.4–0.8).

Critical modelling rule: **time-only gains are credited to output only through the capital channel.** A step that gets faster but frees no capital and no scarce capacity produces a one-off level shift in when approvals arrive, not a change in the steady-state rate. This is the formal version of "slow ≠ constraint".

Two model caveats are logged as evidence rather than buried:
- **Non-additivity** [E-3097]: B1, B2, B8 and B10 act on overlapping attrition mass. Improving all four by 10 % yields at most 11–26 %, not the 21 % naive sum. Never sum these elasticities.
- **Amdahl ceiling** [E-3098]: setting discovery time to zero removes at most 23–37 % of total elapsed development time and leaves cumulative PoS unchanged. This is the direct quantitative answer to sub-test H0-c.

### 1.4 Cost-share assumptions
Phase-level capitalised cost shares (`c`) are treated as assumptions with stated bounds, not as sourced facts, because no per-phase cost decomposition with a disclosed methodology was recovered within this agent's search budget. One hard datum anchors the Phase III end: Tufts CSDD prices Phase III conduct at $55,716 per day [E-3021]. The assumption set is logged in UNRESOLVED item U-1 with its basis and its effect on the elasticity bands (roughly ±30 % on capital-channel terms only; probability-channel terms are unaffected).

### 1.5 What this agent did not do
Confidence grading (R3) is Agent R's. Origin-hop verification beyond three hops was not attempted where a source is flagged `circular_risk: true` in the ledger; nine records carry that flag and Agent R should treat them as origin-unverified pending independent check.

---

## 2. Candidate-by-candidate assessment

### B1 — Target validation / translational validity of target biology
**Axes: P (primary), C (secondary).**

**Current state.** Lack of clinical efficacy accounts for roughly 40–50 % of all drug development failures, the single largest attrition class [E-3012]. The upstream input quality is measurably poor: Amgen confirmed only 6 of 53 landmark preclinical oncology papers (11 %) [E-3010], and roughly two-thirds of Bayer's 2007–2010 in-house validation projects were inconsistent with the literature [E-3011]. A large multi-laboratory replication programme in cancer biology documents the same shortfall independently [E-3013].

**Trend.** Mixed to flat. Efficacy has remained the dominant failure class across reviews spanning 2015 [E-3046] to 2024 [E-3012], and no dataset recovered here shows the replication rate improving over the decade.

**Direct constraint evidence.** T-M positive. B1 acts on the largest attrition mass in the system, and target choice is not a capacity resource — it cannot be parallelized away, because running more programs on invalid targets multiplies failures rather than diluting them. There is no spare-capacity counter-evidence because the resource is selection quality, not throughput.

**Modality variance (M5).** Hardest on small molecule and antibody programs in CNS, immunology and metabolic disease, where target biology is the whole bet. Least binding for vaccines (antigen validity often known a priori) and for cell therapy in haematology, where CD19 and BCMA are clinically validated. ADC inherits antibody target risk plus payload-window risk. RNA and gene therapy in monogenic disease carry the lowest target risk, because human genetics supplies the validation before any program starts.

**Region variance (M6).** Low. Target literature is globally shared. [INFER] China-origin programs skew fast-follower on validated targets, which lowers their B1 exposure while raising commercial crowding — a shift of risk from B1 to B11, not a reduction in system risk.

**Elasticity: 5 – 10 – 15 %** per 10 % improvement [E-3081]. `ε_P = 10 × 7.33 × 0.45 × θ`, θ = 0.15–0.45. θ is bounded well below 1 because "10 % better target validity" is not directly observable ex ante; the sponsor cannot verify it until Phase II reads out. Highest elasticity in the set, and simultaneously the least purchasable.

### B2 — Preclinical→clinical translation (animal model predictivity, NAM validation)
**Axes: P (primary), T (secondary).**

**Current state.** Zero drug development tools have completed qualification under FDA's ISTAND pilot as of 1 January 2026, against 16 projects in the pipeline [E-3015]; a liver-chip DILI platform is the furthest advanced, with a reported 870-compound validation set at 87 % sensitivity and 100 % specificity [E-3016].

**Trend.** Improving, from a low base. FDA published a Roadmap to reduce animal testing in preclinical safety studies in April 2025 [E-3014], Congress advanced FDA Modernization Act 3.0 in 2025 [E-3018], and the first organ-chip reached final qualification stage by early 2026 [E-3015]. Ten years ago no such pathway existed.

**Direct constraint evidence.** T-N positive, historically: the ALS Therapy Development Institute retested more than 100 compounds reported active in the SOD1 mouse and found none effective, eight of which had already consumed clinical trials [E-3017]. That is a natural experiment showing model non-predictivity destroyed real clinical capacity. T-U positive on the replacement side: the constraint today is the *supply of validated replacement methods*, not sponsor willingness — 16 projects, zero completions.

The frequently repeated claim that 90–95 % of drugs passing animal tests fail in humans [E-3019] is advocacy-sourced with no disclosed denominator and is **not** used in the elasticity calculation. ⚠ Treat any conclusion resting on that figure alone as low-evidence.

**Modality variance.** Hardest on small molecules and ADCs, where rodent plus non-rodent tox is the gate. Moderate on antibodies, where species cross-reactivity forces NHP-only studies — which is why FDA named monoclonals as the first phase-down target. Least binding on cell and gene therapy, where animal models are already conceded to be weakly predictive and regulators accept mechanistic and ex vivo human data. Vaccines sit in between via challenge models.

**Region variance.** US fastest on NAM acceptance (roadmap plus FDAMA 3.0) [E-3014, E-3018]. EU driven by 3Rs policy but slower on drug-specific qualification. CN and JP-KR follow ICH, so a NAM-only package still faces rejection risk outside the US and global programs must run the animal package regardless. [INFER] This asymmetry means the effective near-term value of NAMs is capped by the least permissive region on a global filing.

**Elasticity: 2 – 4 – 7 %** [E-3082]. `f = 0.25` (portion of efficacy plus toxicity attrition attributable to model non-predictivity rather than to target choice), θ = 0.10–0.35 held low precisely because zero NAMs have completed qualification, plus ≈0.3 from the capital channel.

### B3 — Clinical trial patient recruitment / site capacity
**Axes: T, C.** Not P, except through terminations.

**Current state.** A Tufts CSDD analysis of nearly 16,000 investigative sites found about 1 in 10 enrolled no patient and 48 % either under-enrolled or enrolled nobody [E-3020]. In oncology, roughly 60 % of sites enrol fewer than five participants and over 20 % enrol none [E-3022]. Phase III conduct costs about $55,716 per day, so every day of enrollment delay is priced [E-3021].

**Trend.** Worsening. Enrollment interval lengthened 36.9 % between 2010 and 2020 [E-3077], and the industry-to-federal oncology enrollment ratio doubled from 4.8 to 9.6 between 2008–2012 and 2018–2022 [E-3025], meaning more sponsors chasing the same patients through the same sites.

**Direct constraint evidence.** T-Q and T-U both positive at the *site* level. But the more important finding is where the constraint is **not**: only about 7 % of cancer patients participate in any research study [E-3023], and 56 % of oncology non-enrollment is because no suitable trial existed at the patient's treatment location, versus 22 % ineligible and 15 % declining [E-3024]. [INFER] The raw patient pool therefore has large unused headroom; the binding sub-resource is **activated, matched site capacity**, not patients. This distinction matters operationally: adding sites and improving trial-to-patient matching relieves the constraint, whereas broadening eligibility alone would not.

**Modality variance.** Hardest on cell and gene therapy — tiny eligible pools, few qualified treatment centres, apheresis and ICU infrastructure required — and on rare-disease RNA and gene programs. Moderate on biomarker-selected oncology (small molecule, ADC, antibody). Least binding on vaccines and on large common-disease small molecule programs, where site networks are deep and accrual is fast.

**Region variance.** US sites are the least productive per site and the most expensive; EU is slower to activate but more consistent per site; CN can accrue large oncology trials several times faster at high-volume centres, which is a principal reason first-in-human work has migrated there; JP-KR sit between EU and CN, with strong per-site quality but small pools.

**Elasticity: 1.5 – 2.5 – 4.0 %** [E-3083]. Capital channel dominates (c = 0.30–0.40, τ = 0.5–0.7, δ = 0.6), plus a small program-rescue term (ρ = 0.03–0.08 probability that a program dies of enrollment failure) and a 1.3–1.6 queueing multiplier justified by the 48 % under-enrolment figure. Mid-pack despite being the industry's most-complained-about bottleneck — because it moves cost and schedule, not probability of success.

### B4 — Patient-pool fragmentation from precision medicine
**Axes: T, C** (and P in the *opposite* direction).

**Current state.** Biomarker-selected trials screen far more patients than they enrol: one oncology cell-therapy trial required HLA typing of ~2,500 blood samples plus IHC on ~750 tumour specimens to enrol 36–40 participants, a ratio near 65:1 [E-3027]. NCI-MATCH screened close to 6,000 patients with a 143-gene panel to fill roughly 40 arms [E-3026].

**Trend.** Worsening in burden terms: subpopulation-restricted approvals have risen over the past decade to nearly match all-comer approvals and reach market demonstrably later [E-3028].

**Direct constraint evidence.** T-U positive on the screening resource, but the constraint is **bidirectional and partly self-chosen**: enrichment shrinks the pool while raising PoS. No evidence was found that relaxing biomarker selection raises system output, and the available evidence points the other way. Improvement must therefore be defined as *screening efficiency at constant enrichment*; defined as "less precision", the elasticity is plausibly negative.

**Modality variance.** Hardest on cell therapy, where HLA, antigen and fitness selection stack multiplicatively, and on gene therapy for ultra-rare monogenic disease where the global pool can be under 1,000 patients. Strong for ADC and targeted small molecules in oncology. Weak for antibodies in broad immunology, negligible for vaccines.

**Region variance.** CN offers the largest single-country pools for common oncology biomarkers and the fastest accrual; US pools are fragmented across many competing trials; EU fragmentation is regulatory and linguistic as much as biological; JP-KR pools are often too small for ultra-rare precision trials to run domestically at all.

**Elasticity: 0.5 – 1.2 – 2.5 %** [E-3084], on the screening-efficiency definition.

### B5 — Regulatory review capacity and evidence standards
**Axes: T (capacity), P (evidence standards).**

**Current state.** On-time completion of FDA approval actions fell to about 78 % in H2 2025 against an 85–90 % historical band [E-3030], while output held at 46 CDER novel drugs [E-3001] / 53 including biologics [E-3029].

**Trend.** Mixed. Capacity was cut sharply (≈3,500 FDA staff terminated on 1 April 2025 [E-3031]) with only a modest timeliness slip and no collapse in approval count.

**Direct constraint evidence — NEGATIVE.** This is the clearest spare-capacity finding in the set. T-N returns a strongly negative result: capacity was cut hard and output barely moved [E-3001, E-3029, E-3030, E-3031]. T-U is negative on arithmetic grounds too — review occupies roughly 10–12 months of a 9.1-year clinical span [E-3004], so even abolishing review entirely changes the schedule by about a tenth. Where B5 *does* bind is evidence standards rather than headcount: only 11 biomarkers have ever been qualified [E-3072] and zero organ chips have completed ISTAND qualification [E-3015]. That component is scored separately as B15 to avoid double-counting.

**Modality variance.** Hardest on cell and gene therapy and ADCs, where CMC review and facility inspection dominate the cycle and CBER/OTP capacity is thinner than CDER's. Least on small molecules and antibodies with conventional packages. Vaccines are politically rather than capacity constrained.

**Region variance.** US: not capacity-binding. EU: centralised procedure adds predictable months. CN: median ICI indication approval lagged FDA by 344 days versus 118.5 days for the EU [E-3032] — materially binding for patient access, though not for the global approval count; the rare-disease lag has compressed to about 1.4 years [E-3033]. JP-KR: local-data expectations add a development leg rather than review time.

**Elasticity: 0.1 – 0.4 – 1.0 %** [E-3085]. Rank 14 of 16.

### B6 — CMC / manufacturing
**Axes: T, C, P** — all three, and the widest modality spread in the set.

**Current state.** In one myeloma cohort only 24 of 40 candidates (60 %) secured a commercial BCMA CAR-T production slot, with reported waits of 1–10 months and substantial progression or death before infusion [E-3038]. Autologous CAR-T manufacturing fails outright in about 25 % of NHL cases and 7 % of B-ALL [E-3034]. Vein-to-vein averages five to eight weeks [E-3041]. Autologous COGS is reported at ~$95,780 per dose against ~$4,460 allogeneic [E-3035].

**Trend.** Mixed, and the direction differs by sub-resource. Viral vector *suite* capacity is now modelled to exceed demand through 2031, with clinical demand growing at only ~4 % CAGR against 31 % commercial [E-3036]. Simultaneously, consolidation removed six of ten National Resilience sites in 2025 and WuXi divested its US/UK advanced therapies unit [E-3037], so the number of financially viable partners fell even as nominal capacity rose. ADC conjugation and ADC-specific fill-finish remain tight, with more than 200 candidates and 41 in Phase III competing for the same lines [E-3039].

**Direct constraint evidence.** T-Q **strongly positive for autologous cell therapy** — explicit rationing with measured patient loss [E-3038] is the textbook definition of a binding constraint. T-U **negative for AAV suite capacity** [E-3036]: supply outpaces demand, so the AAV constraint is yield and cost per dose (systemic doses reach 1×10¹⁴ vg per patient, and a 2,000 L run may treat only a handful of patients [E-3040]), not suite count. No queueing evidence at all for small molecule or mAb manufacture.

**Modality variance — the headline finding.** Autologous cell therapy **15–40 %** (point 25 %) — B6 is the *rank-1* constraint for this modality. ADC 3–8 %. Gene therapy / AAV 2–6 %, expressed as cost per dose rather than capacity. RNA / LNP 1–3 %. Antibody 0.5–2 %. Small molecule ≈0–0.5 %, effectively unconstrained. Vaccine 0.5–2 % outside pandemic surge. [INFER] Reporting a single system-level rank for B6 misrepresents it; the decomposition *is* the result.

**Region variance.** US and EU hold most GMP cell-therapy capacity and the tightest qualified-personnel constraint. CN has the largest and cheapest vector and ADC capacity but is subject to geopolitical de-risking [E-3037], which raises the effective cost for Western sponsors. JP-KR are net importers of CGT manufacturing with growing domestic ADC capacity.

**Elasticity (system-level): 0.8 – 1.8 – 3.5 %** [E-3086]; **cell therapy alone: 15 – 25 – 40 %**.

### B7 — Delivery and biodistribution
**Axes: P** (feasibility gate).

**Current state.** An engineered peptide-conjugated LNP achieved ~2.23 % of injected dose in brain [E-3042] — a best case, not a routine figure. Extensive hepatic accumulation is described as the central obstacle for extrahepatic nucleic acid therapeutics [E-3044].

**Trend.** Improving. From effectively liver-only systemic RNA delivery in the mid-2010s to demonstrated single-digit-percent CNS delivery, with physical adjuncts giving 10-fold (healthy brain) and 6.7-fold (glioblastoma) enhancement [E-3043].

**Direct constraint evidence.** T-M partially positive and mechanistically clear — the ultrasound result shows delivery, not payload design, is the limiting variable in those models [E-3043]. But no system-scale natural experiment has occurred, so the link to marginal approvals is inferential. [INFER] B7 does not slow existing programs; it deletes whole indication classes from the addressable set before a program is ever started, which does not show up in attrition statistics at all. That makes conventional constraint tests systematically under-detect it, and is why the band is wide.

**Modality variance.** Hardest on RNA and gene therapy, where tissue tropism determines which diseases are addressable. Hard on ADC and antibody in solid tumours (penetration gradients) and on any CNS indication. Least on small molecules — which are the incumbent *solution* to delivery — and on vaccines, where the delivery target is the immune system itself. Cell therapy faces a distinct variant: trafficking into solid tumours rather than crossing a barrier.

**Region variance.** None material; this is physics and biology. Regional variation appears only in trial tolerance for invasive administration routes.

**Elasticity: 1 – 3 – 6 %** [E-3087], band explicitly wide.

### B8 — Toxicity and immunogenicity prediction failure
**Axes: P (primary), C.**

**Current state.** Uncontrollable toxicity carries about 30 % of clinical failures, the second largest class after efficacy [E-3045]. Toxicity accounts for roughly one-fifth of clinical failures and about two-thirds of post-launch withdrawals [E-3047].

**Trend.** Flat. Safety and toxicology were the largest attrition source across four major companies for 2000–2010 [E-3046] and toxicity still carries ~30 % in 2024 reviews [E-3045] — two decades of in silico toxicology investment with no measurable shift in the attribution share. The failure mode persists in the newest modalities: haematologic malignancies were diagnosed in 10 of 67 Skysona trial participants (15 %), leading FDA to narrow the indication [E-3048].

**Direct constraint evidence.** T-M positive. Unlike efficacy failure, toxicity failure is predictable in principle, and the marginal return is doubled: preventing a late toxicity failure returns both the trial cost and, for the two-thirds of withdrawals that are toxicity-driven [E-3047], the launched-asset value. Not parallelizable — a toxicity signal terminates a program regardless of available capacity.

**Modality variance.** Hardest on small molecules (off-target, DILI, hERG) and ADCs, where payload-driven ocular, haematologic and interstitial lung toxicity is the dominant failure mode. Hard on gene therapy (insertional mutagenesis [E-3048], complement activation) and cell therapy (CRS/ICANS, secondary malignancy). Moderate on antibodies (immunogenicity, cytokine effects) and RNA (innate immune activation, hepatotoxicity at dose). Vaccines carry rare but reputationally decisive risk.

**Region variance.** Low in the biology. Regulatory risk tolerance differs at the margin: FDA has been more willing than EMA to accept managed oncology risk, and CN accepts higher CAR-T toxicity thresholds in relapsed settings.

**Elasticity: 3 – 6 – 9 %** [E-3088]. `f = 0.30`, θ = 0.15–0.40, plus a late-stage avoided-spend term.

### B9 — Wet-lab throughput (Design-Build-Test-Learn)
**Axes: T, C.**

**Current state.** Automated platforms report throughputs such as 6,048 samples per day against roughly ten reactions per operator per day conventionally [E-3049]. Against that, US National Primate Research Centers have been unable to fill up to two-thirds of requests for research monkeys since 2021 [E-3050], and most research primates are consumed by IND-enabling toxicology [E-3051].

**Trend.** Mixed. Automation capacity has risen by orders of magnitude over the decade [E-3049], while the NHP sub-step tightened sharply after 2021 and only began easing in 2025–2026 as Cambodian imports resumed and Charles River moved to secure breeding assets [E-3052].

**Direct constraint evidence — split verdict.** Screening and synthesis: all four tests negative. Automation has raised capacity faster than demand, so the step is *fast, not scarce*, and buying more of it purchases little [E-3049]. IND-enabling toxicology: T-Q and T-U positive — two-thirds of primate requests unfillable [E-3050] against a resource that gates entry to the clinic [E-3051]. [INFER] The correct reading of B9 is that the catalog treats as one candidate two sub-steps with opposite verdicts; only the NHP-dependent one binds.

**Modality variance.** NHP dependence — the binding part — is highest for antibodies and ADCs (species cross-reactivity forces NHP-only tox) and for gene therapy (NHP biodistribution). Small molecules use rodent plus one non-rodent and are less exposed. Cell therapy often cannot be modelled in animals at all, so B9 barely binds. Screening throughput matters most for small molecules and least for cell and gene therapy.

**Region variance.** Acute in the US, where Chinese cynomolgus export restrictions bit hardest [E-3050]. CN retains domestic supply and is the cheapest NHP tox venue. EU primate-use rules push work offshore. JP-KR are import-dependent and exposed to the same shock as the US.

**Elasticity: 0.3 – 0.9 – 2.0 %** overall [E-3089]; **NHP-dependent IND-enabling sub-step alone: 1 – 4 %**.

### B10 — Scarcity of high-quality experimental training data
**Axes: P** (via model quality).

**Current state.** ChEMBL release 36 (October 2025) holds about 2.8 million distinct compounds against 17,803 targets [E-3053], while the subset carrying both a 3D structure and a measured affinity — PDBbind v2024 general set — is about 6,999 complexes, three orders of magnitude smaller [E-3054].

**Trend.** Improving in volume, static in the binding dimension. Bulk bioactivity data grows steadily; the structure-plus-affinity subset does not.

**Direct constraint evidence.** T-M positive but indirect. The mechanism is documented: absence of large, unbiased negative examples is a first-order limitation on supervised generalization [E-3055], and heterogeneous IC50/Ki/Kd endpoints measured under differing assay conditions cap achievable precision even where volume is large [E-3056]. No natural experiment linking a data increment to an approval increment was found. [INFER] B10 is best understood as the constraint on *AI's own rate of improvement*, not on the pipeline directly — which is exactly why it matters disproportionately in the discovery-compressed scenario (§4).

**Modality variance.** Hardest where the design space is large and the assay cheap: small molecules, and increasingly de novo protein and antibody design. Hard on antibody developability prediction, where proprietary data dominates and public sets are thin. Least on cell therapy and vaccines, where design variables are not primarily molecular-structural. Gene therapy capsid engineering is data-poor but has strong directed-evolution alternatives that bypass labelled data entirely.

**Region variance.** Public datasets are global. Effective access differs: [INFER] CN firms benefit from larger in-house screening volumes and looser data-sharing constraints; EU GDPR constrains clinical and omics linkage more than US or CN regimes; JP-KR have strong national biobanks but limited industrial-scale assay corpora.

**Elasticity: 0.3 – 1.0 – 2.5 %** [E-3090], two-stage pass-through through B1 and B8.

### B11 — Capital / reimbursement / pricing
**Axes: C (primary), P (via program selection).**

**Current state.** Early-stage biotech capital contracted on both count and value: seed and Series A rounds fell from 228 in 2024 to 191 in 2025, dollars from $10.6 bn to $8.7 bn [E-3057]; Q1 2025 biopharma venture financing was $6.5 bn, down 20.2 % year on year [E-3058]. Commentary reports more than half of listed biotechs ended 2024 with under two years of runway [E-3061].

**Trend.** Worsening on the underlying measure. Deloitte's tracking of the top 20 shows projected R&D IRR rising to 7.0 % in 2025 from 5.9 % [E-3006], but excluding GLP-1/GIP assets the underlying return is about 2.9 %, *down* from 3.8 % [E-3007]. [INFER] A headline improvement produced entirely by one mechanism class in one indication is not a productivity trend; the ex-incretin series is the honest read, and it is deteriorating. This is consistent with, not a reversal of, Eroom's Law [E-3005].

**Direct constraint evidence.** T-M and T-N both positive. The mechanism is near-linear: `Y = N × PoS` and capital sets `N`. Three independent signals show it currently binding: early-stage capital contracting in both count and dollars [E-3057, E-3058]; ex-GLP-1 returns at 2.9 % [E-3007], at or below plausible cost of capital, which is the condition under which rational investors withdraw; and — most telling — **approved, technically successful products withdrawn for commercial reasons**: BioMarin pulled Roctavian after 2025 sales of ~$36 m, and bluebird pulled Skysona from the US after recording no commercial sales in Q1 2025 [E-3060]. That is the terminal-value constraint propagating backwards into what gets developed at all.

An industry-commissioned study reports a 68 % fall in small-molecule investment by sub-$2 bn companies since the IRA and a 35 % reduction in early-stage programs at small and mid-size biotechs from 2021 to 2023 [E-3059]. ⚠ LOW-EVIDENCE CLAIM — this figure is sponsored by parties with a direct financial interest in the policy conclusion (S4), and no independent replication was located. It is cited as *directionally consistent* with [E-3057] and [E-3058], not as load-bearing.

**Modality variance.** Hardest on gene and cell therapy, where the withdrawals actually happened [E-3060] and one-time-payment reimbursement remains unsolved — for these modalities B11 is arguably the terminal constraint regardless of technical success. Hard on US small molecules because of the nine-versus-thirteen-year IRA negotiation asymmetry [E-3059]. Least binding on antibodies and obesity/metabolic assets, which are absorbing most available capital [E-3006, E-3007]. Vaccines face a distinct political-demand risk.

**Region variance.** US: pricing policy is the dominant variable and the clock differs by modality. EU: HTA and joint clinical assessment compress achievable price and delay launch. CN: NRDL negotiation imposes steep price cuts but grants volume, favouring fast-follower economics. JP-KR: repeated price-cut cycles and reference pricing make them low-value launch markets, concentrating global return on the US.

**Elasticity: 4 – 6 – 8 %** [E-3091]. Near-linear, discounted by marginal-program quality δ = 0.4–0.8. **Caveat:** capital is an input, not a process step. A strict Theory-of-Constraints reading asks what limits the *productive absorption* of capital — and that returns to B1 and B8. B11 and B1/B8 are therefore complements, not substitutes.

### B12 — IP / FTO congestion
**Axes: C** (indirect).

**Current state.** USPTO unexamined inventory peaked at 837,928 in January 2025 and fell to 776,995 by April 2026, while average first-action pendency lengthened from 19.9 to 22.6 months [E-3065]. Inventorship rules for AI-assisted inventions were set in February 2024 [E-3062] and revised in November 2025 [E-3063], both requiring a natural-person inventor who made a significant contribution.

**Trend.** Mixed — backlog falling, pendency rising [E-3065].

**Direct constraint evidence — NEGATIVE on the direct channel.** Patent examination runs **in parallel** with clinical development, not in series, so 22.6 months of pendency adds no schedule delay to an approval. No evidence was found of programs halted for FTO congestion at a rate that moves annual approvals. The real channel is expected-exclusivity value feeding B11: Amgen v. Sanofi (18 May 2023) invalidated broad antibody genus claims for lack of enablement [E-3064], narrowing the protectable perimeter around a discovery — which matters more as AI makes generating adjacent sequences cheap. [INFER] That is a real effect on asset value, but it is a B11 input, not an independent throughput constraint.

**Modality variance.** Hardest on antibodies and de novo designed proteins — exactly where Amgen v. Sanofi narrowed genus scope and where AI generates near-neighbours at scale. Moderate on RNA (crowded sequence and chemistry space) and ADC (linker and payload thickets held by few players). Least on cell therapy, where process and know-how protection dominate, and on small molecules, where composition-of-matter claiming remains robust.

**Region variance.** US: AI-inventorship rules explicit [E-3062, E-3063]; enablement bar raised [E-3064]. EU/UPC: enablement doctrine differs and genus claims have fared better, so US and EU scope now diverge for the same asset. CN: fast grant, less predictable litigation. JP-KR: follow EPO practice; no AI-inventorship allowance.

**Elasticity: 0.05 – 0.3 – 1.0 %** [E-3092].

### B13 — Talent and organizational absorptive capacity
**Axes: T, C.**

**Current state.** AI/ML specialist roles take four to six months to fill [E-3066], with AI-related life-science postings up about 77 % year on year and 19,000+ openings reported [E-3067].

**Trend.** Mixed and internally contradictory. The same period saw roughly 22,500 roles eliminated at two employers alone — Novo Nordisk ~9,000 and Bayer ~13,500 since 2024 [E-3068].

**Direct constraint evidence — NEGATIVE at aggregate level.** The labour market is barbell-shaped, not short: mass reductions coexist with narrow AI-specialist scarcity [E-3067, E-3068]. [INFER] A shortage confined to an upstream specialism cannot bind system output when the downstream capacity it feeds is itself under-utilised — the same B3 evidence that shows 48 % of sites under-enrolling [E-3020] shows there is no shortage of hands at the expensive end of the pipeline. No evidence of trials or filings delayed for want of staff was located.

**Modality variance.** The narrow scarcity concentrates where AI is the method: small molecule and protein design. A distinct and more binding scarcity exists in cell and gene therapy — qualified GMP operators, apheresis staff, treatment-centre personnel — but that is properly a B6/B3 constraint expressed as labour. Antibody, RNA and vaccine programs show no distinctive talent constraint.

**Region variance.** US and EU compete with large technology firms for the same AI talent and lose on compensation [E-3066]. [INFER] CN has a deeper and cheaper computational-biology graduate pipeline. JP-KR face the sharpest shortage relative to ambition, since domestic AI-bio programs are newer.

**Elasticity: 0.2 – 0.6 – 1.5 %** [E-3093]. Note that the available evidence is dominated by recruiter and vendor sources, which are structurally biased toward reporting shortage.

### B14 — Biosecurity and model regulation
**Axes: T** (potential, not actual).

**Current state.** Of 375 surveyed biological AI tools, only 3 % carried any documented safeguard; 23 % of the highest-performing tools were assessed as high misuse potential and 61.5 % of those were fully open source [E-3070]. Access regimes range from restricted (AlphaProteo) to fully open weights [E-3071].

**Trend.** Flat in practice. A May 2025 US Executive Order set 90- and 120-day deadlines to revise nucleic acid synthesis screening and DURC frameworks; a July 2026 review could not confirm either had issued [E-3069].

**Direct constraint evidence — NEGATIVE, unambiguous.** No enforced access regime currently gates therapeutic developers [E-3069, E-3070, E-3071]. **A constraint that is not enforced cannot be relaxed for gain.** This is a downside risk term, not a lever.

**Modality variance.** Any future controls would fall hardest on de novo protein and peptide design and on gene therapy and vaccine work involving viral sequences. Small molecule, ADC conjugation, cell therapy and RNA chemistry work sit largely outside current proposals.

**Region variance.** US: EO-driven, deadlines unmet, direction uncertain [E-3069]. EU: the AI Act's systemic-risk provisions could capture large biological sequence models, potentially making the EU the strictest jurisdiction. CN: state-administered synthesis screening under a different rationale. JP-KR: minimal specific regulation.

**Elasticity: 0.0 – 0.1 – 0.5 %** [E-3094]. Rank 16 of 16, with explicitly asymmetric downside.

### B15 — [NEW] Clinical endpoint and biomarker qualification / measurement science
**Axes: T, P.** Added because it is not reducible to B5 (this is evidence infrastructure, not review headcount) nor to B1 (target validity is about biology; this is about measurability).

**Current state.** FDA's Biomarker Qualification Program had accepted 61 projects by 1 July 2025 but had qualified only 11 biomarkers since inception [E-3072]. Qualification-plan development took a median of 32 months overall and 47 months for surrogate endpoints, and only five of the accepted projects were surrogate endpoints [E-3073].

**Trend.** Mixed. No biomarker was qualified between 2018 and late 2025 — a seven-year gap — then three arrived in November–December 2025, including the first osteoporosis surrogate endpoint [E-3074].

**Direct constraint evidence.** T-Q and T-U positive, with an unusually clean mechanism: absent a qualified surrogate, a confirmatory trial must run to hard clinical outcomes, which sets both duration and sample size. This factor is therefore **in series with** the longest and most expensive step, not parallel to it. The queue is visible in the program's own statistics — 61 accepted, 11 ever qualified, 47-month median just to agree a plan [E-3072, E-3073].

**Modality variance.** Hardest in slowly progressive chronic disease regardless of modality — neurodegeneration, fibrosis, cardiovascular and metabolic outcomes — mapping onto small molecules, antibodies and RNA in those indications. Least binding in oncology, where response and PFS surrogates are established, and least of all in vaccines, where immunogenicity bridging is accepted. Gene therapy in monogenic disease sits in between: biomarker acceptance has been decisive where granted.

**Region variance.** The US BQP is the reference process and the slowest formal one [E-3073]; EMA qualification of novel methodologies runs in parallel under different criteria, so a surrogate accepted in one region may not transfer. CN and JP-KR generally follow whichever of FDA or EMA has accepted the endpoint, adding lag rather than an independent barrier.

**Elasticity: 1.5 – 3 – 5 %** [E-3095].

### B16 — [NEW] Protocol design complexity and operational data burden
**Axes: T, C.** Added because it is distinct from B3: B3 concerns patient and site availability, B16 concerns the load each protocol places on them, and it is sponsor-controllable.

**Current state.** Procedures per Phase III pivotal protocol rose from 187 to 301 between 2015 and 2025, more than 60 % [E-3075]. Phase III protocols now average 5.96 million data points [E-3076]. Trials average about 3.5 amendments, over 50 % more than five years earlier, and around 296 protocol deviations, roughly triple the level of ten years ago [E-3078].

**Trend.** Worsening consistently. Between 2010 and 2020, protocol-approval-to-first-patient lengthened 27.2 % and the enrollment interval 36.9 % [E-3077].

**Direct constraint evidence.** T-M positive, and this is the only candidate in the set where **the removable slack is directly measured**: a joint TransCelerate and Tufts CSDD study finds nearly a third of procedures and their associated data do not support primary or key secondary endpoints [E-3076]. Documented waste inside the most expensive step means the marginal return on removing it is immediate and depends on no new technology. It also compounds B3 — heavier protocols narrow eligibility and raise site burden while enrollment duration lengthens [E-3077].

**Modality variance.** Binds across all modalities because it is a behaviour, not a technology. Heaviest in oncology and in cell and gene therapy, where long-term follow-up requirements (up to 15 years for integrating vectors) add durable operational load. Lightest in vaccines, where endpoints are few and standardised.

**Region variance.** Multi-regional trials inherit the union of all regional expectations, so global programs carry the highest complexity. EU trials carry extra procedural load from the CTR/CTIS transition; CN-only trials are typically leaner; US trials carry the heaviest data-capture expectations, imposed by sponsors themselves rather than by FDA.

**Elasticity: 1.0 – 2.0 – 3.5 %** [E-3096]. Mid-pack on raw elasticity, **highest in the set on risk-adjusted tractability** because the improvement requires only a sponsor decision.

---

## 3. Consolidated ranking

| Rank | ID | Candidate | Axes | ε low | ε point | ε high | Evidence sufficiency |
|---|---|---|---|---|---|---|---|
| 1 | B1 | Target validation | P;C | 5 | **10.0** | 15 | moderate |
| 2 | B8 | Toxicity / immunogenicity prediction | P;C | 3 | **6.0** | 9 | strong |
| 3 | B11 | Capital / reimbursement / pricing | C;P | 4 | **6.0** | 8 | moderate |
| 4 | B2 | Preclinical→clinical translation | P;T | 2 | 4.0 | 7 | moderate |
| 5= | B7 | Delivery and biodistribution | P | 1 | 3.0 | 6 | weak |
| 5= | B15 | Endpoint / biomarker qualification | T;P | 1.5 | 3.0 | 5 | moderate |
| 7 | B3 | Recruitment / site capacity | T;C | 1.5 | 2.5 | 4.0 | strong |
| 8 | B16 | Protocol complexity / data burden | T;C | 1.0 | 2.0 | 3.5 | strong |
| 9 | B6 | CMC / manufacturing (system-level) | T;C;P | 0.8 | 1.8 | 3.5 | strong |
| 10 | B4 | Precision-medicine fragmentation | T;C | 0.5 | 1.2 | 2.5 | moderate |
| 11 | B10 | Training-data scarcity | P | 0.3 | 1.0 | 2.5 | moderate |
| 12 | B9 | Wet-lab throughput (DBTL) | T;C | 0.3 | 0.9 | 2.0 | moderate |
| 13 | B13 | Talent / absorptive capacity | T;C | 0.2 | 0.6 | 1.5 | weak |
| 14 | B5 | Regulatory review capacity | T;P | 0.1 | 0.4 | 1.0 | strong |
| 15 | B12 | IP / FTO congestion | C | 0.05 | 0.3 | 1.0 | weak |
| 16 | B14 | Biosecurity / model regulation | T | 0.0 | 0.1 | 0.5 | moderate |

**Ties.** B7 and B15 are tied at rank 5: their point elasticities coincide at 3.0 and their evidence bases are of comparable overall strength for opposite reasons — B15 has better process data and worse mechanistic grounding, B7 the reverse. B8 and B11 have identical point elasticities of 6.0; B8 is placed above B11 because it acts on probability of success, the axis with the weakest existing tooling, whereas the capital channel already has functioning markets and price signals.

### Reasoning for the top five

**1. B1 — target validation.** It sits on the largest attrition mass in the system (40–50 % of failures [E-3012]) and it is the one factor that cannot be relieved by adding capacity: running more programs on invalid targets multiplies failures. Measured input quality is poor and not improving (11 % and ~33 % replication [E-3010, E-3011]). It ranks first on elasticity while being the least purchasable improvement in the set — a 10 % gain in target validity cannot be bought, only produced.

**2. B8 — toxicity prediction.** Second-largest attrition class at ~30 % [E-3045], flat for two decades despite sustained investment [E-3046], and uniquely double-paying: it also drives about two-thirds of post-launch withdrawals [E-3047]. Unlike efficacy, it is predictable in principle, so θ is plausibly higher here than for B1 — which is why the band overlaps B1's despite the smaller failure share.

**3. B11 — capital and reimbursement.** The most nearly linear channel to output, and currently contracting on three independent measures [E-3057, E-3058, E-3007]. The decisive evidence is that technically successful, approved products are being withdrawn for purely commercial reasons [E-3060]: the terminal-value constraint has begun propagating backwards into what gets developed. Ranked third rather than first only because it is an input rather than a process step — under a strict ToC reading, more capital without better target and toxicity selection buys more failures.

**4. B2 — preclinical→clinical translation.** Ranks high because the ALS natural experiment [E-3017] is the cleanest demonstration in the set that a specific input's non-predictivity consumed real clinical capacity. It ranks below B1 and B8 because the replacement supply is genuinely immature — zero completed ISTAND qualifications against 16 projects [E-3015] caps θ.

**5=. B7 and B15.** B7 earns rank 5 on option value: it does not slow programs, it deletes indication classes before they start, so conventional constraint tests systematically under-detect it. B15 earns rank 5 on a clean serial dependency: without a qualified surrogate the confirmatory trial must run to hard outcomes, and the qualification pipeline produces about one qualified biomarker every two years [E-3072, E-3073, E-3074].

### Where the widely-assumed bottleneck has spare capacity — negative findings
These are reported as prominently as the positive findings, per assignment.

- **B5 regulatory review capacity has slack.** 3,500 staff cut, output essentially held [E-3001, E-3029, E-3030, E-3031]. Review is also only ~10 % of the clinical span [E-3004].
- **AAV viral vector suite capacity has slack.** Independent modelling projects supply outpacing demand through 2031, clinical demand growing at only ~4 % CAGR [E-3036]. The AAV constraint is cost and yield per dose [E-3040], not suites.
- **The raw clinical patient pool has slack.** ~7 % of cancer patients participate in any study [E-3023] and 56 % of non-enrollment is trial-unavailability at the site, not patient scarcity [E-3024]. The scarce resource is matched, activated site capacity.
- **Aggregate biopharma labour has slack.** ~22,500 roles cut at two employers while AI postings grew 77 % [E-3067, E-3068] — a barbell, not a shortage.
- **Screening and synthesis throughput has slack.** Automation capacity outruns demand [E-3049]; only the NHP-dependent sub-step queues [E-3050].
- **B14 imposes no enforced constraint at all.** 3 % of tools have safeguards; mandated framework revisions unissued more than a year past deadline [E-3069, E-3070].

---

## 4. Constraints now vs constraints that appear only if discovery is compressed (feeds Q3)

The Amdahl arithmetic bounds the whole question [E-3098]: with clinical development at 9.1 years [E-3004] and discovery at 3–6 years, setting discovery time to zero removes at most **23–37 %** of elapsed time and **zero** cumulative attrition, because PoS from Phase I (14.3 % [E-3002]) is set entirely downstream. The AI Phase I signal — 21 of 24 molecules succeeding [E-3008] — does not extend into Phase II, where the same source reports a fall to industry-normal rates. [INFER] That pattern is exactly what one would expect if AI is currently improving properties that Phase I measures (PK, tolerability, drug-likeness) without improving the target and efficacy judgements that Phase II measures. On the evidence recovered here, sub-test **H0-a is not supported and H0-b requires separating the two axes**: discovery duration has demonstrably compressed for some programs, while probability of success has not.

**Binding now (independent of AI progress):** B1, B8, B11, B15, B16, B3, and B6 for autologous cell therapy specifically.

**Latent — becomes binding only after discovery is compressed:**

| Candidate | Why it is not binding now | What makes it bind |
|---|---|---|
| **B9** (wet-lab, esp. NHP tox) | Screening capacity exceeds demand [E-3049] | More candidates per year → IND-enabling tox slots, already at two-thirds unmet demand [E-3050], become the gate |
| **B10** (training data) | Acts only through B1/B8 today | If AI is the mechanism for improving B1 and B8, data becomes the constraint on the constraint-reliever |
| **B6** (all modalities, not just cell) | Small molecule and mAb capacity idle | More candidates → GMP campaign slots and ADC conjugation lines [E-3039] saturate |
| **B3 / B4** (patient supply) | Patient pool has 90 %+ headroom [E-3023] | More candidates chasing the same biomarker-defined pools converts headroom into genuine scarcity; the ratio already doubled [E-3025] |
| **B5** (review) | Demonstrated slack [E-3029, E-3031] | A step-change in submission volume against a workforce already cut 3,500 [E-3031] would consume the remaining margin quickly |
| **B12** (IP/FTO) | Runs in parallel; no output effect | Mass AI-generated sequences create genuine prior-art and FTO congestion in exactly the antibody/de novo space narrowed by Amgen v. Sanofi [E-3064] |
| **B14** (biosecurity) | No enforced regime [E-3069] | If capability growth triggers enforced access controls, this converts from a null term to a negative one |

[INFER] The Theory-of-Constraints conclusion follows directly: compressing discovery does **not** move the constraint to "preclinical/clinical" as a block. It moves it to a specific, identifiable sequence — first to **IND-enabling toxicology capacity (B9-NHP) and GMP slots (B6)**, then to **matched patient and site capacity (B3/B4)**, and only then to review (B5). Meanwhile the factors that set PoS — B1, B8, B15 — are **not** relieved by discovery compression at all and remain binding throughout. That is the substantive answer to H0-d: "preclinical/clinical" decomposes into a capacity tier that shifts and a probability tier that does not.

---

## 5. UNRESOLVED

Four items could not be closed to a sourced number within this agent's scope. Each is recorded in `RLSX/work/C/unresolved.csv` with every query attempted, the failure reason, at least three alternative sources tried, and a current best estimate with its basis. Summary:

- **U-1** Per-phase capitalised cost shares with disclosed methodology (affects capital-channel `c` terms; best estimate and bounds given).
- **U-2** Published elasticity of annual approvals to any single pipeline factor (none exists; this is why M2 requires construction).
- **U-3** Modality-resolved share of the clinical pipeline needed to weight B6 exactly (best estimate 10–15 % for cell/gene).
- **U-4** Origin verification for the Tufts CSDD site-productivity figures behind [E-3020] and [E-3021] (secondary aggregators reached; primary Impact Report is paywalled).

No item was deferred, narrowed, or sampled. All sixteen candidates were assessed on all four required fields.

---

# STEP 6 revision

Every change below is recorded with its reason and its source. Evidence continues at **E-3099 … E-3125** (26 new records; ledger now E-3001–E-3125, 122 records). The matrix gains three columns — `original_rank`, `shift_rank`, `shift_elasticity_point` — so that every rank move is auditable against the pre-revision state. Parent rows B1–B14 are all retained; ten sub-rows and one new parent are added alongside them, never in place of them. Ten further WebSearch/WebFetch calls were run in this pass, for B17 evidence and to verify independently the two figures the red team contested.

**Standing warning, now quantified by an independent model: the elasticity column is not summable.** Agent D implemented my overlap logic and returned a naive sum of 20.76 % against a modelled joint of 14.42 % for B1+B2+B8+B10 — **30.5 % of the naive gain is not real** [E-3115]. Adding parent rows and their sub-rows together compounds the error further. This warning is repeated in the `notes` field of every affected row.

---

## 6.1 Adjudication of the B3 dispute with Agent F — F is right, my inference was inverted

**I withdraw the inference.** I read ~7–8 % cancer trial participation and the 56 % "no trial available locally" share as evidence of usable slack in the patient pool, and part of B3's rank 7 rested on it. Agent F argues that figure *is* the measurement of matched-capacity scarcity. Agent X attacked F's position as X-15 and rejected its own attack. F stands, and on re-examination F is correct [E-3099].

**What decided it.** The test that matters is whether relieving the candidate resource converts the pool, and F ran it:

- A deployed AI prescreening system read **98,348 charts across 29 trials, flagged 825 eligible, and produced 117 enrolments** — a 0.12 % yield **after cutting screening cost tenfold** [E-5047, E-5067]. Screening effort is held constant and removed as an explanation. If raw-pool slack were the operative variable, cheap exhaustive screening would have converted it. It did not.
- NCI-MATCH isolates the same variable inside one well-funded protocol with central sequencing and 1,117 sites: **26.4 % of screened patients were matchable but 17.8 % were assigned**, so 8.6 percentage points of *already-matched* patients were lost purely because their arm was not open [E-5028]. Zero contribution from pool size, biology or willingness.
- Agent X adds non-overlapping supply-side corroboration: global investigators −9 % and coordinators −28 % over six years [E-9524].

F's formulation is the correct one and I adopt it: reading the 56 % figure as slack is reading the size of the unserved queue as evidence that the server is idle. **What survives from my original entry is narrower and still correct**: the scarce resource is the matched, activated site slot rather than the patient, so remedies that add eligible patients without adding open slots do not raise output. The data I reported [E-3023, E-3024] stand; my reading of them does not.

**Rank consequence.** B3 falls 7 → 11 on *current-state* elasticity — but not because of this adjudication. It falls because of Agent D's model (§6.5). F itself endorses rank ~7 at today's candidate flow. F's second argument, that B3 belongs in the top three under the constraint-shift scenario, is adopted and is now carried explicitly: **B3's `shift_rank` is 1** [E-3121].

## 6.2 Constraint-shift rank is now a separate column

F's point generalises and Agent D's model confirms it: several candidates' elasticity is a function of candidate flow, not a constant. D's scenarios give the ordering directly — at current flow capital binds with GMP plasmid the first physical resource at u = 0.90; at 5× inflow with capital freed the binding constraint becomes **NHP toxicology** at u = 1.00 (S6b); with capacities at measured historical growth over ten years it becomes **Phase III patient slots** (S7), and S7 delivers *fewer* approvals than S6b because measured clinical capacity shrinks at −0.92 %/yr [E-3121].

Top of the shift ordering: **1 B3, 2 B9 (NHP fragment), 3 B6a (shared inputs), 4 B9b, 5 B8, 6 B17.** The probability candidates B1, B8 and B17 barely move, because compressing discovery does not relieve them.

## 6.3 Three composite candidates split

Parents kept with aggregate values; sub-row `provisional_rank` is *the position that fragment would occupy if substituted for its parent*, not an extra entry in the parent ordering.

**B6 → B6a/b/c/d** on Agent G [E-3117]. G measures a **9.4× modality spread** and finds **GMP plasmid DNA binds first at ~1.06× current IND volume**, because it feeds AAV, lentiviral and mRNA simultaneously and so saturates while each modality still shows suite headroom; aseptic fill-finish is third at ~1.12× with a three-year response lag capital cannot shorten. D's tornado orders the same way independently (fill-finish 7.8 % downside swing; autologous suite capacity and mAb drug substance exactly zero in both directions). G confirms my order-of-magnitude autologous claim (1.19× against a slack-modality range of 4.8–10×). The fragment that had **no visibility inside the parent** is B6a: shared inputs bind before any modality-specific step. Parent 9 → 14; B6a's shift rank is 3.

**B9 → B9a/B9b** on Agent H [E-3118]. H endorses my rank 12 for nominal throughput and supplies a market test I lacked: the largest public foundry is cutting footprint up to 60 % against a 48 % revenue decline, and a flagship cloud lab was absorbed after a headcount collapse. Suppliers do not fail for lack of demand at a binding constraint. But B9 was two bottlenecks under one label: **predictive-assay throughput (B9b) belongs at rank 6**, alongside B1 and B2, because it acts on decision-tool predictive validity. The IND-enabling NHP toxicology capacity sits in B9a and carries that row's entire shift exposure — D ranks it 4th of 26 parameters with a 43 % downside swing and zero upside.

**B10 → B10a/B10b** on Agent H [E-3119]. The quantity test was actually run: MELLODDY pooled **123× the public corpus** and returned ~4 % AUC-PR improvement. B10a drops to 19. **B10b (label noise, standardisation, negative-data reporting) rises to 7** — the mechanism is computable, a 10 % cut in σₑ lifts the achievable ceiling ~9 % relative, worth roughly 12× a 10 % throughput gain. X-18's caveat travels with the row: the ceiling bounds *measured benchmark scores and the resolving power of the adjudicating experiment*, not model capability.

**B5 → B5a/B5b** on Agent E [E-3120]. E independently reconfirms near-zero elasticity for review capacity from primary agency sources (queue in contract, 44–55 day reviews for selected products in the worst staffing year, CBER CGT capacity that submissions did not fill) and places it 15th–16th; **evidence standards (B5b) belong at 8**, because they act on P rather than T. The split is **region-conditional** and that must travel downstream: for an EU-centric portfolio B5 ranks materially higher because of the JCA gate. Japan is the cleanest counter-case in the run — the world's fastest review coexists with 86 US/EU-approved drugs nobody filed.

## 6.4 B17 added — clinical development design (dose, schedule, endpoint, population)

**Recorded plainly: B17 was absent from the B1–B16 catalogue and was surfaced by the red team (X-19), not by me.** The orchestrator admitted it and adjudication X-30 set its parameters, which I adopt: **axes P primary, C secondary, explicitly not T; elasticity 2 / 4 / 7; rank 4 of 17** [E-3122]. My own independent construction returned 1.8 / 3.3 / 5.0 [E-3111], so the two agree inside their bands and X's wider band is used. It does not rest on one agent's collection: **seven of its fifteen evidence records were collected independently by me** (E-3104–E-3110) alongside X's six (E-9539–E-9544).

Current state and constraint evidence, all of it decisions rather than capacities:
- **Dose** — MTD-set oncology doses are reduced post-approval in **36 %** of cases against 23 % for below-MTD regimens, and the MTD or maximum studied dose was proposed as the label dose in ~70 % of approvals reviewed [E-3106]. Sotorasib carried a **fourfold dose overshoot at identical plasma exposure** (960 mg vs 240 mg) [E-3107], and the 209-patient randomised comparison mandated as a postmarketing requirement found no advantage for the higher dose [E-9543].
- **Endpoint** — of 362 industry Phase III oncology trials 2008–2017, **58.4 % of reported-positive results were false-positive on overall survival** and 87 % were false-positive or true-negative [E-3108]. Among accelerated approvals, confirmatory trials reusing the same endpoint type had *no* associated withdrawals while endpoint-type mismatch predicted withdrawal [E-3109].
- **Population** — applying broadened ASCO–Friends eligibility to a 10,500-patient advanced NSCLC cohort would have avoided excluding close to half of it [E-3110]; across 17,368 development trajectories, biomarker-guided selection reached **10.7 % success against 1.6 %** without [E-9541].
- **Trend: improving**, and regulator-forced. FDA's dose-optimisation final guidance issued 8 August 2024; Bayesian designs in early-phase oncology rose from 48 % (2021) to 75 % (2024) with 93 % of surveyed developers reporting changed strategy [E-3104, E-3105]; backfill-cohort specification rose 60 % → 77 % [E-9540]; MRD draft guidance issued 20 January 2026 [E-9542], though MRD is still not a qualified endpoint [E-9548].

**Modality variance** (as directed): hardest for oncology small molecules and ADCs, where the MTD paradigm originated and the payload therapeutic window makes dose and schedule decisive. Hard for cell and gene therapy, where dose is not titratable — one patient is one batch, vector dose is fixed by manufacture — and the population is genotype-fixed, so a design error cannot be corrected by dose adjustment and surfaces only as a failed pivotal. Moderate for antibodies, where dose–response is often flat and the characteristic error is dosing too high. RNA intermediate. Least for vaccines.

**Not additive with B1, B4 or B8**: the population limb overlaps B4's enrichment channel, the dose limb overlaps B8's toxicity channel, and the whole candidate is a proper subset of the efficacy attrition mass carried by B1.

**A signature worth naming.** Designs compliant with the dose-optimisation guidance are *longer* — randomised dose comparison and backfill cohorts add early-phase time. B17 therefore **raises output while worsening cycle time**, which is exactly what D's model produced for late-stage PoS in S5 (+31.8 % approvals, cycle time 13.50 → 15.03 years, because more survivors load the Phase III patient resource). Generalised: **on this system the levers that raise approvals make it slower, and the levers that make it faster do not raise approvals.** Anyone optimising for cycle time is optimising against output.

## 6.5 Reconciliation with Agent D's flow model

**Where D confirmed me.** D reproduced four of my point elasticities to within **0.35 percentage points** without the budget constraint and without using my formula — B1 +10.19 vs 10.0, B2 +3.77 vs 4.0, B8 +5.66 vs 6.0, B10 +1.13 vs 1.0 — and its modelled joint effect landed inside my stated 11–26 % band [E-3113, E-3115].

**Where D corrected me, and I revise.**

1. **Budget-binding recalibration.** With the industry R&D budget binding — D's default, and the realistic case since capital sits at u = 1.00 in every D scenario — each probability-channel elasticity falls by about a third: B1 7.05, B2 2.65, B8 3.96, B10 0.80. I adopt D's budget-binding values as point estimates because the brief's output metric is approvals in the real system, and retain my unconstrained originals as each band's upper bound [E-3113].
2. **Duration levers go to roughly zero.** D's S2/S3/S4 all return 54.45 approvals: a 40 % cut in enrollment duration and a 50 % cut in CMC lead time each add **exactly none**, because they shorten the carrying period without reducing out-of-pocket spend per programme [E-3114]. B3 2.5 → 0.6, B6 1.8 → 0.45, B4 1.2 → 0.55, B9 0.9 → 0.5. **B16 is cut least** (2.0 → 1.4) and consequently rises 8 → 7, because it removes out-of-pocket *procedures* rather than only calendar time, and D's own budget identity converts a reduction in risk-adjusted cost into approvals where a pure schedule gain does not.
3. **Discovery duration has an elasticity of exactly zero** on annual approvals across a 0.9–6.0 year range (D tornado rank 24 of 26), and S1 (−80 % discovery time) returns 50.00 approvals against a 50.00 baseline. This does not change any of my rows — no row of mine is discovery *duration* — but it is the sharpest available confirmation of my Amdahl record [E-3098] and of the T/P separation the brief demands.
4. **B11 is the largest revision in the set: rank 3 → 8, elasticity 6.0 → 0.8** [E-3116]. Two independent lines force it. D's tornado: **+50 % R&D budget yields zero additional approvals** (50.0 → 50.0) because physical capacities take over the moment capital stops binding, while −20 % costs 46 % of approvals. Red-team X-10 reaches the same place from the capital side: ~USD 1.3 trillion deployable at the top 25 pharma while novel-target entry fell to ~30/yr in 2024 and venture investment tripled — the marginal dollar was available and declined the novel bet. My original near-linear assumption was wrong on the improvement side. **The row is now asymmetric and is labelled so**: improvement side 0.0/0.8/3.0, downside approximately **−23 % of approvals per 10 % budget reduction**. B11 is relabelled *expected terminal value* — an endogenous multiplier on every other candidate's elasticity, not an independent capacity constraint — and its elasticity is explicitly not additive with B1 and B8 because it acts through them. It is placed above B10 despite an identical point estimate because it is a live systemic risk and a dead lever, and those are not the same as a small symmetric effect. The better-identified policy estimate (interrupted time-series: −11.4 industry-sponsored trials immediately post-IRA plus −1.2/month) supersedes the industry-commissioned 68 % figure I originally carried.

**Where I do not revise, and why.** I keep non-zero values on the duration and capacity rows rather than zeroing them to match D exactly. D lists *capital is exogenous, with no feedback from returns onto budget* as an explicit model assumption; in a real market a durable reduction in cost per approval attracts capital. The residual values I retain (0.45–1.4) are that channel and nothing more, and the gap between them and D's zero is stated here rather than smoothed away.

## 6.6 Adopted red-team findings

**X-11 — B1's trend was wrong; the rank is not** [E-3101, E-3124]. My trend cell rested on the Amgen 6-of-53 and Bayer two-thirds statistics, which are **level measurements from 2011–2012 with undisclosed paper-selection criteria** and cannot establish a 2016–2026 trend. The cell is corrected to two channels: **improving on decision quality, flat on literature reproducibility.** Human genetic support is a measured **2.6× relative-success multiplier** (verified independently against the Nature primary source [E-3100]) and already underpins **63 % of the 428 FDA approvals of 2013–2022**, with remaining headroom equal to the 37 % that lack it; novel oncology target validation rose from ~2/yr (2000–04) to ~10/yr (2020–24).

X-26 adds a second correction that I adopt for my own language: **no statement of mine may imply that nothing technological is being brought to bear on B1.** Cis-pQTL Mendelian randomisation is a causal human instrument that does not require a trial, and its resource base has industrialised to ~2,940 plasma proteins in 34,557 UK Biobank participants [E-9549]. The countervailing result travels with it: across 11,482 target–indication pairs, MR significance alone did *not* enrich for Phase II success while GWAS support did. **The objection to the instrument is empirical, not conceptual.** B1 stays at rank 1 — a factor can be improving, and tractable, and still be the binding constraint.

**X-14 / X-29 — B15: my figure was right, my use of it was wrong, and the error is mine** [E-3103, E-3123]. X traced both contested figures to primary agency sources and found Agent E and I were counting two different objects while neither of us named the object:

| Object | Count | Route |
|---|---|---|
| Biomarkers formally **qualified** through FDA's Biomarker Qualification Program | **8** as of 1 Jul 2025 (7 pre-2016 legacy, most recent 2018); **11** including 3 qualified Nov–Dec 2025; **zero surrogate endpoints ever qualified** | Formal qualification |
| Disease-or-use × patient-population × surrogate-endpoint **pairings** in FDA's Table of Surrogate Endpoints | **over 200** | Reached **without** qualification |

My arithmetic checks out — 11 = 8 + 3. **The substantive error is mine and it is a denominator error of exactly the kind M3 exists to catch: I reported a numerator without naming its denominator, then treated the throughput of a nearly-unused channel as the system constraint.** Seven of the eight qualifications predate the 2016 Cures Act. A channel almost nobody uses cannot be the binding constraint on a process that is evidently happening by another route — and the 200+ pairings, which I verified independently against FDA's own page (Cures-Act-mandated, updated six-monthly, content dated 29 April 2026, no reference to BQP qualification [E-3102]), demonstrate that other route. Agent E's error was descriptive only (calling pairings "markers"); mine was substantive.

**B15: rank 5-equal → 7 → 10; elasticity 3.0 → 1.1 → 0.7. Current-state metric restated to name both objects explicitly.** What survives, and it remains real and striking: **zero surrogate endpoints have ever been formally qualified**, and MRD is still not qualified as of August 2026 (the April 2024 advisory vote was non-binding; the January 2026 document is draft) [E-9545, E-9548]. That supports a claim about the **portability and reusability of endpoint evidence between sponsors** — not the claim I attached it to. The residual constraint under B15 is scientific: surrogates that genuinely predict clinical benefit in slowly progressive disease.

**X-16** raised B2's θ lower bound (the premise of zero qualified NAM tools is no longer true — one qualified 8 Dec 2025); rank unchanged at 5. **X-17** attacked B7 and rejected its own attack; B7's split verdict stands intact. **X-13** requires every capacity ceiling to be labelled with its jurisdictional scope; the shared-manufacturing rows (B6a) survive it because shared inputs are global markets and do not relocate when a trial moves.

## 6.7 Revised ranking

Ranks 2, 4 and 5 sit **within the resolution of this analysis** — D's reproduction error is ±0.35 pp and my θ bands span a factor of two to three, so point estimates of 2.65, 3.96 and 4.00 are not separable on the evidence; ordering inside that block rests on band width and evidence maturity as much as on the point value.

**Rank 3 is intentionally vacant.** The computed ordering places B17 third on point elasticity (4.0 vs B8's 3.96); the orchestrator directed rank 4. Rather than renumber the tail and hide the discrepancy, the directed rank is recorded and the gap left visible, so seventeen parents occupy ranks 1–18 [E-3125].

| Rank | Was | ID | Candidate | ε point | Shift rank |
|---|---|---|---|---|---|
| 1 | 1 | B1 | Target validation | 7.0 | 4 |
| 2 | 2 | B8 | Toxicity / immunogenicity prediction | 3.96 | 5 |
| *3* | — | *(vacant — see above)* | | | |
| 4 | new | **B17** | **Clinical development design** | **4.0** | 6 |
| 5 | 4 | B2 | Preclinical→clinical translation | 2.65 | 11 |
| 6 | 5 | B7 | Delivery and biodistribution | 1.9 | 13 |
| 7 | 8 | B16 | Protocol complexity / data burden | 1.4 | 8 |
| 8 | **3** | B11 | Expected terminal value (capital) | **0.8** | 17 |
| 9 | 11 | B10 | Training-data scarcity | 0.8 | 14 |
| 10 | **5=** | B15 | Endpoint / biomarker qualification | **0.7** | 12 |
| 11 | 7 | B3 | Recruitment / site capacity | 0.6 | **1** |
| 12 | 10 | B4 | Precision-medicine fragmentation | 0.55 | 7 |
| 13 | 12 | B9 | Wet-lab throughput | 0.5 | **2** |
| 14 | 9 | B6 | CMC / manufacturing | 0.45 | **3** |
| 15 | 13 | B13 | Talent / absorptive capacity | 0.4 | 16 |
| 16 | 14 | B5 | Regulatory review + evidence standards | 0.35 | 12 |
| 17 | 15 | B12 | IP / FTO congestion | 0.2 | 15 |
| 18 | 16 | B14 | Biosecurity / model regulation | 0.1 | 18 |

Sub-rows, ranked as *position if substituted for their parent*: **B9b 6** (predictive-assay throughput), **B10b 7** (data quality / label noise), **B5b 8** (evidence standards), B6a 17, B6b 17, B5a 18, B6c 18, B6d 19, B9a 19, B10a 19. Three fragments — B9b, B10b, B5b — rank far above their parents; three others (B6d, B9a, B10a) rank below every parent. That spread is the case for the splits in one line: **a single rank averaged a binding constraint and a non-constraint into a number true of neither.**

## 6.8 What the revision did not change

B1 remains rank 1 on elasticity. The six negative "spare capacity" findings all survived independent attack and are strengthened, not weakened, by the revision — D's model adds a seventh by showing that discovery *duration* has an elasticity of exactly zero. The Amdahl ceiling [E-3098] is confirmed by D's S1. The constraint-shift ordering I predicted (B9-NHP and B6 first) is reproduced by D's S6b from an independent model.
