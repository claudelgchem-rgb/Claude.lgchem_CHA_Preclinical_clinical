CHARTER_ACK: R1,R2,R3,R4

# Agent G — CMC, Manufacturing, Supply Chain and Delivery (B6, B7)

Evidence block E-6001…E-6076 (72 records) in `./RLSX/evidence/parts/G.jsonl`.
Structured data (63 rows) in `./RLSX/data/cmc_capacity.csv`. UNRESOLVED register (14 items) in `./RLSX/work/G/unresolved.csv`.
All confidence grading is left to Agent R; every record carries `confidence:null, graded_by:null`.

---

## 0. Methodology

**Collection.** 28 WebSearch calls and 13 WebFetch calls. No fact in this report is written from memory; every factual sentence carries an `[E-6xxx]` identifier, and every interpretive sentence is marked `[INFER]`.

**Source hierarchy applied.** Company filings and results releases (Samsung Biologics, Lonza, WuXi Biologics, Moderna 10-Q, Denali 8-K) and regulator primary documents (FDA press announcements, openFDA CRL archive, FDA guidance, FDA safety actions) were preferred over consultancy and market-research output. Where a number exists only in a paid market report or an AI-generated aggregator page, it is typed `market_report` or `secondary`, `circular_risk` is set true, and `provenance_hops` records the attempted trace to origin. Eleven records carry `circular_risk:true`.

**The adjective filter.** The assignment forbids accepting "capacity crunch" without a utilization number or a booking lead time, and equally forbids accepting "overbuild" without one. I applied this symmetrically and it eliminated a great deal of material. Two consequences that must be visible to the reader:

- The **ADC and aseptic fill-finish "tightness"** narratives survive only as adjectives. No CDMO publishes conjugation-suite utilization or slot lead time; L.E.K.'s fill-finish analysis, fetched in full, discloses no capacity, no utilization, no CAGR, no gap and no lead time. Both are recorded as UNRESOLVED for the measurement, and the constraint verdicts I assign rest on structural facts (suite counts, build lags, format non-fungibility) rather than on the narrative.
- The **AAV "overbuild"** narrative fails the same test at the level of its headline number. The "<50% suite utilization" figure traces only to Mordor Intelligence and IntuitionLabs with no disclosed sample or denominator [E-6005]. I did not adopt it on its own authority. I adopted the *direction* on the strength of two market-clearing events that no analyst controls: National Resilience closing six of ten sites during 2025 [E-6006], and an FDA-approved 125,000 sq ft commercial viral vector plant transacting at USD 4.5 million [E-6007].

**The utilization proxy rule.** Most sub-areas publish a lead time but not a utilization rate. To make the Part 4 arithmetic auditable and mutually comparable, one rule is applied uniformly across every modality: booking lead time L in months maps to utilization u as L≤3 → 0.60; 4–8 → 0.80; 9–14 → 0.90; ≥15 → 0.95; and the static saturation multiple is M = 0.95/u, the demand multiple that drives the sub-area to 95% utilization with capacity held fixed. Where I depart from the rule (autologous CAR-T, oligonucleotide, mRNA, small molecule) the departure and its numeric assumption are stated inside the derivation record itself. `[INFER]` The rule is crude; its virtue is that it is the *same* crudeness everywhere, so the ordering it produces is more trustworthy than any individual multiple.

**What "constraint" means here.** Per the common brief, a slow step that is parallelizable or holds spare capacity is not a constraint. I therefore report an explicit elasticity test (M2) in §2.5 rather than relying on the intuition that manufacturing "feels" hard.

---

## 1. Part 1 — Capacity, lead time, batch failure and COGS by modality

### 1.1 Small molecule

Verdict: **slack**, saturation multiple ~10x [E-6069].

The small-molecule CDMO market was about USD 71.3 billion in 2024, growing at roughly 6.7% CAGR, with solid orals about 40% of CDMO market share in 2025 [E-6021]. No utilization figure, shortage metric or booking lead time for innovator small-molecule API or oral solid dose was located despite targeted search [E-6021]. `[INFER]` The absence of a lead-time signal in a market of that size, with continuing capital additions, is itself the evidence: scarce capacity produces queues, and queues get reported. This is the loosest estimate in the deliverable and is labelled as such.

The one tightening variable for small molecule is not physical capacity but **compliance capacity**. FDA issued 303 drug and biologics warning letters in FY2025, of which 112 cited 21 CFR 211 GMP deficiencies — the highest GMP count published in over twenty years; 59% went to US facilities and data integrity appeared in 15% of all letters [E-6026].

### 1.2 Monoclonal antibody / recombinant protein

Verdict: **binding at the commercial tier (~1.0x), slack at the IND-enabling clinical tier (~4.8x)** [E-6060].

This split is the single most important correction to any one-line reading of biologics capacity.

- Commercial tier: Samsung Biologics reports 785,000 L installed across Bio Campus I and II, with Plants 1–3 at full utilization throughout 2025 and Plant 4 reaching full utilization in Q3 2025, cumulative contract value above USD 21 billion and FY2025 revenue of KRW 4,557 billion [E-6003]. Lonza reports ~330,000 L at Vacaville and Integrated Biologics sales up 32.2% CER with contracting volumes described as high [E-6001]. Samsung's plain-language "full utilization" is the only legally-attested utilization anchor in the entire dataset.
- Clinical/IND tier: WuXi Biologics states regulatory submission capacity sized for about 200 INDs and 20 BLAs/MAAs per year at a single CDMO, against a total backlog of USD 23.7 billion, 945 cumulative integrated projects and 209 new projects in 2025 [E-6004]. `[INFER]` One supplier declaring 200 IND-programmes per year of throughput, against a CDER commercial IND flow of 1,139 across all modalities [E-6031], is not a picture of scarcity at IND stage.

Tech transfer runs 9–15 months from kickoff to first released GMP batch, with commercial transfers 12–18 months or longer [E-6033]; Lonza markets a 5-month fast-track best case [E-6034]. Batch failure in established biologics manufacturing is low and improvable: GSK reduced batch rejections from 5.2% to 0.8% in eight months under a right-first-time programme [E-6050]. CDMOs are projected to hold 54% of global biologics capacity by 2028, up from 43% in 2024 [E-6054].

### 1.3 ADC

Verdict: **near_binding**, saturation multiple ~1.19x on current assets, ~1.67x after announced expansions [E-6065].

The bioconjugation CDMO market is estimated at USD 2.18 billion in 2025 growing at ~15% CAGR to USD 4.37 billion by 2030, and Lonza is adding two conjugation suites at Visp to its existing five [E-6020]. Lonza projects above-20% CAGR for the ADC CDMO market and has added a Swissmedic-approved aseptic line at Stein covering mAbs, bispecifics and ADCs [E-6002]. WuXi Biologics reports 252 ADC programmes, up ~30% year on year, with ADCs and bispecifics together two-thirds of new project additions [E-6004].

**The tightness is not verified by a utilization number or a booking lead time, and I will not pretend otherwise.** No CDMO discloses either; the C&EN trade analysis returned HTTP 406 on fetch. What is verifiable is structural: capacity growing ~40% at a flagship site against demand growing 20–30% per year means the expansion is consumed in roughly two years, and the genuinely scarce asset is not conjugation volume but *integrated* conjugation plus ADC-qualified containment filling [E-6002; E-6023 row G-023]. `[INFER]` Tight, not binding — an ADC sponsor waits, it does not fail.

### 1.4 Autologous cell therapy

Verdict: **binding**, saturation multiple ~1.19x, and the lowest-headroom modality in the set [E-6063].

- Slot and time: patients wait up to 3 weeks for an allocated manufacturing slot, with 2–4 weeks for manufacture plus release and a vein-to-vein time of 3–6 weeks [E-6014].
- Failure: 4–7% of patients cannot receive their product because of manufacturing failure, with clinical-trial rates spanning 1–13% [E-6011]. The strongest single figure is registry-grade: the UK National CAR T Panel reported 38 manufacturing failures in 981 approved LBCL patients, 3.87% [E-6012]. Out-of-specification rates for CD19-directed products run 1–6%, including about 5% for liso-cel [E-6013].
- COGS: about USD 115,000 per dose on recent estimates, against USD 95,780 in 2019, with a working range of USD 100,000–300,000 [E-6015].

`[INFER]` The decisive structural fact is arithmetic, not economic. One batch equals one dose. A clean suite on a 21-day cycle at 94% success yields 365/21 × 0.94 ≈ 16.3 patient-doses per year; a ten-suite facility yields ~163 [E-6063]. There is no batch-size lever available anywhere in this modality, which is true of no other modality in this report. Capacity scales strictly linearly with suites and, more bindingly, with trained operators.

### 1.5 Allogeneic cell therapy

Verdict: **slack** relative to autologous, and the escape route from the one-batch-one-dose trap.

COGS is estimated at about USD 40,000 per dose recently, against USD 4,460 in 2019, with one platform claim of USD 10–20k at 20,000–60,000 doses per year [E-6015]. The autologous-to-allogeneic COGS ratio has *narrowed*, from ~21x on the 2019 estimates to ~2.9x on recent ones [E-6015 / CSV G-041]. `[INFER]` That narrowing is not good news for allogeneic: it says allogeneic COGS has risen an order of magnitude as real products faced real release testing, while autologous COGS barely moved. The structural argument for allogeneic — batch amortisation across many doses — survives; the empirical cost gap is much smaller than the platform pitch.

### 1.6 AAV gene therapy

Verdict: **slack in aggregate suite-hours (~1.9x static, ~1.5x net of contraction), near_binding at the commercial quality tier** [E-6061].

Secondary aggregators report capacity outrunning clinical demand, many suites below 50% utilization because they were built for early-phase work, ~8 months from first contact to signed MSA, and slot lead times often exceeding 18 months [E-6005]. National Resilience closed six of ten sites in 2025 and WuXi divested its Advanced Therapies unit [E-6006]. OXB acquired Resilience's Research Triangle Park site — 125,000 sq ft, FDA-approved for commercial-scale viral vector, two GMP drug substance suites plus fill-finish — for USD 4.5 million in October 2025 [E-6007].

`[INFER]` The apparent contradiction between idle suites and 18-month slot lead times is not a contradiction. It is a tier mismatch: commercial-grade, high-titre, low-empty-capsid suites are booked, while early-phase suites built during the 2020–2022 capital wave sit idle. An asset price of USD 4.5 million for an FDA-approved commercial plant is a market-clearing observation, and it is the most legible single piece of evidence for excess supply anywhere in this dataset.

Productivity, not capacity, is where AAV manufacturing actually loses: empty capsids are 70–90% of total capsid yield in standard processes, against an industry target below 30% and an aspiration below 10%, with a projected 30–60% cost reduction from the dose reduction that follows [E-6016].

The binding constraint for systemic AAV is not manufacturing at all — it is dose. Elevidys is dosed at 1.33 × 10^14 vg/kg; three acute liver failure deaths occurred in 2025 across Elevidys and SRP-9004, and FDA imposed a boxed warning and narrowed the indication [E-6045].

### 1.7 Lentiviral gene therapy

Verdict: **binding**, saturation multiple ~1.06x [E-6062].

GMP lentiviral lead times run 8–14 months [E-6009]. Oxford Biomedica batches to Novartis are reported at about USD 1.5 million each, giving roughly USD 5,000 of vector per Kymriah dose and under 300 patient doses per batch, with vector about 40% of total cell therapy manufacturing cost [E-6009]. Process economics show 2,000 L yielding ~672 doses at ~USD 1,459 per dose versus 50 L yielding ~17 doses at ~USD 19,127 — a ~13x unit-cost penalty for small-scale operation [E-6010]. `[INFER]` That penalty is why lentiviral demand cannot be absorbed by simply running more small campaigns: the modality is scale-inflexible in the wrong direction.

### 1.8 Plasmid DNA (shared upstream input)

Verdict: **binding**, saturation multiple ~1.06x, and the earliest-binding shared input in the system [E-6064].

The industry average plasmid wait is reported at ten months for production, analytics and release [E-6008], with 2025 commentary putting access to GMP plasmid capacity at more than twelve months and actual GMP production at 3–5 months, placing plasmid on the critical path for most AAV programmes [E-6008]. Downstream purification is the specific bottleneck: agarose resin capacity is reported still tight after Purolite's USD 150 million plant came online, and a single mRNA manufacturer's new UK, Australian and Canadian plants absorb hundreds of GMP plasmid batches annually [E-6051].

`[INFER]` Plasmid is the sleeper. It is an input to AAV, lentiviral *and* mRNA simultaneously, so its multiple caps all three regardless of their own suite headroom. An AAV programme with an idle suite waiting on plasmid is still waiting. Caveat carried honestly: the ten-month figure originates in a 2022 company press release with no cited source [E-6008].

### 1.9 mRNA-LNP

Verdict: **slack on physical capacity (~6x); binding on ionizable-lipid intellectual property** [E-6068].

Post-pandemic mRNA lines run at a fraction of nameplate, with Moderna actively scaling back its network to reduce underutilized-capacity costs [E-6017]. `[INFER]` A manufacturer closing capacity is a costly and therefore credible signal; the direction is not in doubt even though no percentage is published.

The binding constraint is legal and financial. Moderna settled the Arbutus/Genevant LNP patent litigation in March 2026 with an immediate USD 950 million payment plus provision for a further USD 1.3 billion [E-6052]. Alnylam's cationic-lipid suits went the other way: the Federal Circuit ruled for Moderna on 4 June 2025 and the parties settled on 15 September 2025 with no payment, and final judgment of non-infringement was entered against Alnylam in the Pfizer case on 30 July 2025 [E-6053]. `[INFER]` The net FTO picture is narrower than the Arbutus headline suggests — the Alnylam claim construction of "cationic lipid" was outcome-determinative and cut in favour of the defendants — but a USD 2.25 billion aggregate exposure on one lipid family is a real per-programme cost that reactor time is not.

Lung delivery is a separate and unresolved failure: Vertex terminated VX-522, the inhaled CFTR mRNA-LNP, after a tolerability issue that first paused the Phase 1/2 in 2025 became persistent; the issue was lung inflammation attributed to the LNP, and efficacy was never assessed [E-6048].

### 1.10 siRNA / ASO

Verdict: **slack at the IND-enabling tier (~8x); the constrained tier is commercial multi-hundred-kilogram supply** [E-6067].

Nitto Avecia expanded its Milford site to 3.0 mol of cGMP synthesis capacity, described at the time as the largest oligonucleotide site in the world [E-6018], and Agilent is investing USD 725 million in nucleic-acid therapeutic manufacturing with customer shipments from 2026 [E-6018]. `[INFER]` IND-enabling oligonucleotide campaigns need grams to low kilograms; 3.0 mol at a representative 7 kDa siRNA is of order 21 tonnes of theoretical annual output. The clinical tier is not utilization-limited by several orders of magnitude. The scarce thing is commercial-scale supply for cardiometabolic siRNA, which is a different question from IND throughput.

### 1.11 Vaccine

Verdict: **unknown for bulk antigen; near_binding for the shared fill-finish step**.

The vaccine contract manufacturing market is estimated at USD 3.90 billion in 2025 rising to USD 4.33 billion in 2026, with CDMO consolidation reported to be tightening sterile fill-finish availability and USD 24.86 billion of disclosed CDMO investment in 2025, about three-quarters into US facilities [E-6055]. WHO and CGD both document that global vaccine manufacturing capacity is poorly defined, inconsistently measured and insufficiently understood (UNRESOLVED item 7). I record bulk antigen capacity as genuinely unknown rather than guessing a number.

### 1.12 Aseptic fill-finish (shared across every injectable)

Verdict: **near_binding**, saturation multiple ~1.12x, and the least elastic sub-area in the system [E-6066].

Building and qualifying a new aseptic line takes 2–3 years and can exceed 5 for complex formats, and lines are not interchangeable across vials, prefilled syringes, cartridges and lyophilised presentations [E-6019]. `[INFER]` The multiple is not the interesting number here; the *lag* is. Capital is abundant — USD 24.86 billion of disclosed CDMO investment in 2025 [E-6055] — and cannot buy a line inside three years. A step change in IND volume cannot be absorbed by fill-finish on any timescale shorter than a development cycle, and a change in the *product mix* (say, toward prefilled syringes or lyophilised biologics) can strand nameplate capacity that exists but cannot be used.

---

## 2. Part 2 — The regulatory-manufacturing interface

### 2.1 What the published CRLs actually show

FDA published 202 Complete Response Letters issued between 2020 and 2024 through the openFDA archive on 10 July 2025 [E-6022; E-6056]. A Pharma Manufacturing analysis of that set found 150 of 202 — 74% — involved quality or manufacturing issues [E-6022]. An independent Parexel analysis of the same set found facility plus quality/CMC deficiencies at 29.1% of all cited deficiencies, exceeding clinical safety (13.4%) and efficacy (10.9%) combined [E-6023].

### 2.2 The selection caveat that changes the answer

**Every application in that 202-letter cohort was subsequently approved** [E-6022]. The cohort was defined as CRLs for applications that ultimately gained approval. It therefore cannot estimate the rate at which manufacturing kills an application; by construction, in that cohort the conditional probability of eventual approval after a manufacturing-implicated CRL is 100% [E-6074].

The correct denominator for the "does manufacturing stop approvals" question is the second batch: 89 CRLs released in September 2025 for pending or withdrawn applications that were never approved [E-6024]. **No source located has decomposed those 89 by deficiency type.** This is UNRESOLVED item 6, and it is the single most consequential gap in Part 2.

### 2.3 Quantified answer to the assigned question

How often is manufacturing, rather than clinical data, what stops an approval? `[INFER]` The defensible answer, stated with its uncertainty:

- Manufacturing is implicated in roughly **three quarters of first-cycle rejections** [E-6022] and is roughly **29% of all deficiency citations** [E-6023].
- Manufacturing is the terminal cause of roughly **20% of permanent non-approval decisions**, the best independent estimate available [E-6027].
- Therefore the dominant effect of manufacturing on approvals is a **review-cycle delay of typically 6–12 months, not a programme kill** [E-6074].

This distinction matters for the mission question. A step that delays is not automatically a constraint on annual approvals; in steady state, uniform delay shifts timing without reducing throughput.

### 2.4 Inspection, comparability and platform designation

- **Inspection.** FDA issued 303 drug and biologics warning letters in FY2025 including 112 citing 21 CFR 211 — the highest GMP count in over twenty years [E-6026]. `[INFER]` This is a rising enforcement intensity against a manufacturing base that has not correspondingly improved, and it raises the probability that a facility issue delays a specific approval.
- **Comparability.** FDA's July 2023 draft guidance sets a lifecycle, risk-based framework requiring a risk assessment for every CGT manufacturing change with the comparability study scaled to assessed risk [E-6030]. `[INFER]` For CGT the process defines the product, which makes comparability materially harder than for mAbs and is the principal reason process improvements are *not* adopted mid-development even when available — a hidden tax on CGT cost curves that has no analogue in small molecules.
- **Flexibility, January 2026.** FDA announced it will not require overly stringent comparability data for minor development-stage changes, will consider flexibility on BLA release specifications revisable from post-approval experience, and clarified there is **no requirement to manufacture three PPQ lots** [E-6029]. Covington notes this does not change underlying legal requirements [E-6029]. `[INFER]` The PPQ-lot clarification is the item with real economic content: three PPQ lots of an autologous product is three patients' worth of suite time and three release-testing campaigns.
- **Platform technology designation.** Exactly two designations have been granted: the first to Sarepta in June 2025 for the AAVrh74 platform, revoked about a month later after three patient deaths, and the second to Krystal Biotech in October 2025 for a non-replicating HSV-1 platform [E-6028]. `[INFER]` The practical throughput effect of the programme to date is approximately zero, and the Sarepta revocation demonstrates the structural weakness of platform designation: a platform claim is only as good as the worst product built on it, so the designation transmits risk across a portfolio in exactly the way it was meant to transmit efficiency.

### 2.5 Elasticity test (M2) for B6

`[INFER]` If manufacturing improves 10%, by what percent does annual approvals rise? Three channels, computed in [E-6075]:

1. **Review-cycle delay.** Manufacturing-implicated CRLs are 74% of first-cycle rejections [E-6022]; a 10% reduction advances approvals by roughly 0.5% of the annual figure — a timing shift, not a permanent throughput gain.
2. **Outright kills.** Manufacturing is terminal in ~20% of non-approvals [E-6027]; a 10% reduction recovers 2% of non-approvals, which at typical first-cycle approval rates is roughly 0.7–0.9% more approvals.
3. **Throughput.** Binds only where the saturation multiple is near 1.0 — plasmid, lentiviral, fill-finish, autologous slots [E-6070] — which together are a minority of annual approvals.

**Summed elasticity ≈ 0.05** [E-6075]. That is an order of magnitude below what a genuine system constraint would show. The sharp exception: within autologous CAR-T, manufacturing failure at 3.9–7% [E-6011; E-6012] is a 1:1 loss of treated patients, so elasticity *on patients treated* approaches 1.0 within that modality.

---

## 3. Part 3 — Delivery and biodistribution (B7)

The framing question: is delivery an engineering/design problem that scales with effort and iteration, or a biological/physical limit that does not? I treat each sub-problem separately and give an explicit verdict line.

### 3.1 Hepatic versus extrahepatic (LNP and GalNAc)

**Mechanism.** LNP liver tropism arises from ApoE adsorption onto the particle surface followed by LDL-receptor-mediated hepatocyte uptake, and helper-lipid composition redirects distribution — DOPE enhances ApoE-mediated liver uptake, DSPC directs particles to spleen, cationic cholesterol increases lung and heart delivery [E-6035]. The picture is more subtle than a single receptor: a 2026 Advanced Materials study found hepatic expression strongly ApoE-dependent but largely LDLR-*independent*, with equivalent expression in wild-type and LDLR-knockout mice [E-6036].

**State of the art off-liver.** Ribo reports up to 80% target knockdown in kidney proximal tubular cells from rodent through NHP, 96% knockdown in NHP adipose, and sustained cardiac knockdown with minimal liver and kidney activity in mouse [E-6046]. ⚠ LOW-EVIDENCE CLAIM — [E-6046] is a company press release with no disclosed assay and no clinical confirmation, and no conclusion below rests on it alone. Against that, reviews state flatly that **no extrahepatic receptor-ligand system matches the efficiency and receptor recyclability of the GalNAc-ASGPR axis**, with critically low endosomal escape and tissue-specific barriers remaining limiting [E-6047].

**Quantitative ratio.** Against a deliberately conservative 40 %ID-to-liver anchor, human solid-tumour uptake of 0.01 %ID/g gives a tumour-to-liver delivery ratio of ~2.5 × 10^-4, roughly 4,000-fold [E-6072].

**VERDICT — Hepatic vs extrahepatic: MIXED, leaning engineering, with a hard anatomical floor.** `[INFER]` The liver's advantage decomposes into four factors, and they are not the same kind of thing. Two are *chemistry* — ApoE opsonization and receptor density — and chemistry is engineerable, which is exactly what the kidney and adipose conjugate results demonstrate. Two are *anatomy*: the hepatic sinusoid's fenestrated endothelium admits ~100 nm particles without transcytosis, and the liver receives a large fraction of cardiac output on first pass. No formulation creates a fenestration in a continuous endothelium. So the correct statement is conditional: **extrahepatic delivery is an engineering problem wherever the target sits behind a discontinuous or fenestrated barrier or presents a high-density recycling receptor on an accessible surface (kidney proximal tubule via scavenging receptors, adipose, spleen, liver-adjacent), and it is a physical limit wherever the target sits behind continuous endothelium with no such receptor.** The decade's progress fits this rule precisely: every extrahepatic win reported is in a tissue that satisfies the condition.

### 3.2 Blood-brain barrier

**Receptor-mediated transcytosis, quantitative trajectory.** A bivalent-binding-monovalently TfR shuttle achieved 2–3 %ID/g brain at two hours in mouse, ~80-fold over the unmodified parent antibody, implying an unshuttled baseline near 0.03 %ID/g [E-6039]. In primates the modelled gain is 4–18 fold for trontinemab [E-6040] — i.e. the mouse figure attenuates roughly 5–20x on crossing species [E-6073].

**Clinical confirmation, twice.** Trontinemab at 3.6 mg/kg reduced amyloid below the 24-centiloid threshold in 91% of participants (49/54) at 28 weeks, with 72% (39/54) below 11 centiloids and ARIA-E in fewer than 5% (4/149 across the 1.8 and 3.6 mg/kg cohorts) [E-6040]. Denali's TfR1 enzyme transport vehicle product tividenofusp alfa received FDA accelerated approval on 25 March 2026 for neurologic manifestations of Hunter syndrome — the first approval of an RMT brain-delivery platform product [E-6041].

**Device route.** Focused-ultrasound BBB opening plus aducanumab produced an additional 32% SUVR reduction in FUS-treated regions versus antibody alone over 26 weeks [E-6042], with a preclinical 5–6 fold antibody concentration increase [E-6042].

**AAV capsids — the opposite story.** AAV-PHP.B/PHP.eB CNS tropism depends on the murine-restricted receptor LY6A, giving high CNS transduction in C57BL/6J mice and near-complete failure in BALB/c mice, NHPs and humans; MyoAAV shows diminished NHP transduction and AAV-LK03 shows the mirror-image failure, transducing human hepatocytes well and murine liver poorly [E-6043]. No paper publishes a numeric failure rate; from the named case set I estimate the murine magnitude of gain transfers at essentially **0% for capsids selected on non-conserved receptors** [E-6071]. The corrective is already in hand: primate-conserved carbonic anhydrase IV and the highly conserved brain vascular receptor ALPL both mediate BBB crossing by engineered vectors across species [E-6044].

**VERDICT — Blood-brain barrier: ENGINEERING PROBLEM. High confidence.** `[INFER]` This is the strongest evidence in the entire delivery domain that a barrier long described as fundamental yielded to protein engineering. From the first bivalent shuttle publication in 2017 to the first approval of an RMT-platform product in 2026 is nine years, with a delivered primate gain one order of magnitude below the mouse figure but still clinically decisive [E-6073]. The AAV-capsid sub-branch does not contradict this: **the capsid failure was a failure of the selection model, not of the barrier.** Selecting in C57BL/6J mice on a receptor that primates do not have is a methodology error, and the fix — select on conserved receptors — is itself engineering [E-6044; E-6071]. FUS is real but adjunctive: a 32% incremental effect [E-6042] delivered by a device, which does not scale to chronic dosing and does not generalise to non-antibody payloads.

### 3.3 Solid-tumour penetration (cell therapies and ADCs)

**The numbers.** Antibody uptake is around 30 %ID/g in mouse tumours versus roughly 0.01 %ID/g in human tumours estimated from molecular imaging and biopsy — a ~3,000-fold difference driven principally by body-mass scaling [E-6037]. The perivascular binding-site barrier is established in both animals and the clinic [E-6037]. Mechanistically, the concentration required to *saturate perivascular cells*, not total exposure or AUC, determines maximum penetration distance, because binding is fast relative to diffusive transport in an interstitium where elevated pressure suppresses convection [E-6038].

**Rate of improvement over the decade: zero on the transport metric.** The human ~0.01 %ID/g figure is unchanged from the antibody imaging literature of the preceding two decades, and the governing mechanism is *worsened*, not improved, by higher affinity [E-6076].

**VERDICT — Solid-tumour penetration: BIOPHYSICAL LIMIT for the transport problem; ENGINEERING-TRACTABLE only by routing around transport.** `[INFER]` This is the one sub-problem where I will state a genuine limit, and the reason is that the barrier is a *ratio of rate constants*, not a missing component. Binding rate exceeds diffusion rate; that is what produces the perivascular shell. Every intuitive fix makes it worse: higher affinity binds faster and penetrates less; higher dose helps only until perivascular saturation, which is the saturating-concentration result [E-6038]. Elevated interstitial fluid pressure abolishes convection, so there is no bulk-flow term to engineer. Antigen heterogeneity means that even perfect delivery leaves antigen-negative cells alive.

The successful engineering escapes all change the problem rather than solving it: **bystander payloads** (deliver to the perivascular shell, kill the neighbours the drug never reached), smaller binding formats, co-administered unconjugated antibody to consume the perivascular sink, and dose fractionation. `[INFER]` That the field's working solutions are all workarounds is itself the diagnostic. Effort and iteration have not moved %ID/g and there is no mechanism by which they would.

### 3.4 Muscle, lung, kidney and immune-cell in vivo targeting

- **Muscle.** Systemic muscle-directed AAV is dosed at 1.33 × 10^14 vg/kg; three acute liver failure deaths occurred in 2025 across Elevidys and SRP-9004, and FDA imposed a boxed warning and narrowed the indication [E-6045]. `[INFER]` **VERDICT — Muscle: HARD LIMIT under the current vector class; engineering-tractable only by raising potency per genome, never by dose escalation.** Muscle is ~40% of body mass, so a systemic dose sufficient to transduce it puts the liver over its toxicity threshold. The metric that must move is the muscle-to-liver uptake ratio, by roughly an order of magnitude — and that is a capsid-engineering problem, which places it in the same category as the BBB capsid problem: tractable, but the mouse-selection trap applies here too, since MyoAAV already shows diminished NHP transduction [E-6043].
- **Lung.** Vertex terminated VX-522, the inhaled CFTR mRNA-LNP, after a persistent tolerability issue — lung inflammation attributed to the LNP; efficacy was never assessed [E-6048]. `[INFER]` **VERDICT — Lung: ENGINEERING PROBLEM (materials chemistry), but with a poor track record and a tolerability rather than an efficiency ceiling.** The failure was not that too little reached the lung; it was that what reached the lung inflamed it. That is a lipid-design problem, which is exactly the kind of problem iteration solves — but it has now consumed a flagship programme, so confidence is moderate at best.
- **Kidney.** Up to 80% proximal tubule knockdown reported from rodent through NHP [E-6046]. `[INFER]` **VERDICT — Kidney: ENGINEERING PROBLEM, tractable.** The proximal tubule expresses high-capacity scavenging receptors and sees the entire filtrate; it satisfies the accessible-receptor condition from §3.1. ⚠ LOW-EVIDENCE CLAIM — evidence is a single company press release with no assay disclosure and no clinical confirmation.
- **Immune cells in vivo.** Capstan dosed the first participants in a Phase 1 of CPTX2309, anti-CD19 CAR mRNA in CD8-targeted LNPs, in 2025; in NHPs a two-dose cycle produced deep B-cell depletion in blood and tissues with repopulation by naive B cells [E-6049]. `[INFER]` **VERDICT — Immune-cell in vivo targeting: ENGINEERING PROBLEM, already demonstrated in NHP and now dosing in humans.** Circulating leukocytes are the easiest possible target — no endothelium to cross — and antibody-conjugated LNPs solve the specificity problem directly. If this holds, it does not relieve the autologous cell therapy manufacturing constraint of §1.4; it **deletes** it.

### 3.5 Summary verdict — Design problem or biological limit

`[INFER]` **Split, and the split is predictable from a single rule rather than case by case.**

> **Delivery is an engineering problem wherever the target is reachable by a high-density, recycling, species-conserved receptor on an accessible luminal surface. It is a physical limit wherever the barrier is bulk transport through a pressurised, convection-free interstitium.**

Applying the rule: BBB (TfR1, CD98hc — conserved, recycling, luminal) → engineering, and now clinically proven twice [E-6040; E-6041]. Immune cells (surface antigen, no barrier) → engineering, in humans [E-6049]. Kidney proximal tubule and adipose (scavenging receptors, accessible) → engineering, preclinical [E-6046]. Liver (ApoE/LDLR plus fenestration) → solved. Muscle → dose-limited by an off-target sink, tractable by capsid potency, not by effort [E-6045]. Lung → materials chemistry, repeatedly failing on tolerability [E-6048]. Solid tumour interstitium → physical limit, zero measured improvement in a decade, and the mechanism forecloses the obvious fixes [E-6037; E-6038; E-6076].

Two second-order findings that a per-case reading would miss:

1. **The most common delivery failure of the last decade was not a barrier failure but a model failure.** The AAV capsid case is the clearest instance: an enormous published literature of murine CNS gains that transferred at essentially 0% because the selection ran on a murine-restricted receptor [E-6043; E-6071]. `[INFER]` This is a B10/B2-shaped problem (training data and model predictivity) masquerading as a B7 problem, and it means that a portion of the "delivery is hard" consensus is really "our preclinical selection systems were wrong."
2. **The rate of improvement is not uniform and should not be modelled as one curve.** Over roughly a decade: BBB moved ~80-fold in mouse and 4–18 fold in primate and produced an approval; extrahepatic conjugates moved from nothing to order-90% knockdown in NHP with zero approvals; human solid-tumour %ID/g moved by 0-fold [E-6076].

---

## 4. Part 4 — The scale-up question

**Question.** If AI multiplies the number of candidates reaching IND, which manufacturing sub-capacity binds first, and at what multiple?

**Demand baseline.** CDER received 1,139 commercial IND submissions in CY2024, plus 716 research INDs, totalling 1,855 receipts [E-6031]. CBER OTP holds more than 2,500 active cell and gene therapy INDs of which about 1,300 are gene therapy [E-6032]; dividing the stock by an assumed ~7-year active IND life implies roughly 350 new CGT INDs per year `[INFER]`, giving a total commercial IND flow of order 1,500 per year across all modalities.

**Method.** Saturation multiple M = 0.95/u under the uniform proxy rule of §0, computed per sub-area in [E-6060]…[E-6069] and sorted in [E-6070]. The arithmetic for each is written out in full inside its own derivation record; the load-bearing cases are reproduced here.

### 4.1 The arithmetic, worked

**Plasmid DNA** [E-6064]. Lead time 10 months average, >12 months to access GMP capacity [E-6008] → falls in the 9–14 band → u = 0.90 → **M = 0.95/0.90 = 1.06x**. Caps AAV, lentiviral and mRNA simultaneously as a shared input.

**Lentiviral vector** [E-6062]. Lead time 8–14 months, midpoint 11 [E-6009] → 9–14 band → u = 0.90 → **M = 0.95/0.90 = 1.06x**. No small-scale escape: unit cost rises ~13x from 2,000 L to 50 L [E-6010].

**Aseptic fill-finish** [E-6066]. No published utilization; the 5–10 year demand-exceeds-supply framing implies a persistently high-utilization regime → u = 0.85 assumed → **M = 0.95/0.85 = 1.12x**. The binding parameter is the 2–3 year (up to 5) build lag plus format non-fungibility [E-6019], not the multiple.

**Autologous CAR-T slots** [E-6063]. Slots are rationed, not queued, so utilization is taken at the observed commercial ceiling u = 0.80 → **M = 0.95/0.80 = 1.19x**. Throughput arithmetic: one suite × (365/21-day cycle) × 0.94 manufacturing success [E-6011; E-6012] = **16.3 patient-doses/suite/year**; ten suites = ~163/year. One batch = one dose, so a 10x IND increase requires 10x the suites and 10x the trained operators, with no batch-size lever.

**ADC bioconjugation** [E-6065]. Assumed L = 6 months → u = 0.80 → M = 1.19x on current assets. Lonza going 5 → 7 suites at Visp is +40% at one flagship site [E-6020] → **M = 1.19 × 1.40 = 1.67x** after expansion. Demand growth of 20–30%/yr [E-6002; E-6004] consumes that in ~2 years.

**AAV suites** [E-6061]. Reported below 50% utilization [E-6005] → u = 0.50 → M = 0.95/0.50 = **1.90x** static. Netting a −20% capacity adjustment for 2025 contraction [E-6006; E-6007] → **M = 1.90 × 0.80 = 1.52x**.

**mAb clinical tier** [E-6060]. Supply side: seven largest mammalian CDMOs at a conservative 100 IND-programmes/yr each ≈ 700/yr, against WuXi alone declaring 200 [E-6004]. Demand side: biologics at ~30% of 1,139 CDER commercial INDs ≈ 342, call it ~400/yr [E-6031]. 700/400 = 1.75x supply/demand ratio, multiplied by 2.75 for the ratio of all-tier to commercial-tier suite hours available to clinical work → **M ≈ 4.8x**. Commercial tier separately: u = 0.95 [E-6003] → **M = 1.0x**.

**mRNA-LNP** [E-6068]. "A fraction of nameplate" taken conservatively as u = 0.16 → **M = 0.95/0.16 = 6x** on physical capacity.

**Oligonucleotide** [E-6067]. Clinical-tier demand is orders of magnitude below the 3.0 mol single-site scale [E-6018]; u set at 0.12 → **M = 0.95/0.12 ≈ 8x**.

**Small molecule** [E-6069]. u set at 0.10 against the installed base available to innovator IND work → **M = 0.95/0.10 ≈ 10x**.

### 4.2 Saturation ordering — the answer

| Rank | Sub-capacity | Saturation multiple | Verdict |
|---|---|---|---|
| 1= | GMP plasmid DNA | **1.06x** | binding |
| 1= | Lentiviral vector | **1.06x** | binding |
| 3 | Aseptic fill-finish | **1.12x** | near_binding |
| 4= | Autologous CAR-T slots | **1.19x** | binding |
| 4= | ADC bioconjugation | **1.19x** (1.67x post-expansion) | near_binding |
| 6 | AAV vector suites | **1.5–1.9x** | slack in aggregate |
| 7 | mAb clinical-scale drug substance | **4.8x** | slack |
| 8 | mRNA-LNP drug substance | **6x** | slack |
| 9 | Oligonucleotide clinical API | **8x** | slack |
| 10 | Small-molecule IND-enabling API | **10x** | slack |

(mAb *commercial*-scale sits at 1.0x — already binding — but that is a launch-supply constraint, not an IND-throughput constraint.)

**Answer to the assigned question.** `[INFER]` **GMP plasmid DNA binds first, at roughly 1.06x current IND volume — i.e. essentially immediately.** It binds first for a structural reason rather than an accidental one: it is an *input to three modalities at once* (AAV, lentiviral, mRNA), so it saturates while each of those modalities still shows suite headroom of its own. Aseptic fill-finish binds third at ~1.12x and is the worst case in practice, because it is shared across *every* injectable and has a three-year minimum response lag that no amount of capital shortens [E-6019; E-6055].

The spread between the tightest and loosest sub-capacity is **9.4x** [E-6070]. That spread is the quantitative basis for §5 below.

**A caveat I will not bury.** `[INFER]` Every one of these multiples is small — between 1.06x and 10x — and biological manufacturing capacity has historically responded to sustained demand within 3–5 years. So the honest reading of Part 4 is: an AI-driven IND surge saturates several sub-capacities almost immediately, produces a 3–5 year period of genuine queueing, and then is absorbed — *except* for autologous cell therapy, where the one-batch-one-dose structure means capacity scales linearly with trained operators forever and no learning curve breaks the linearity [E-6063], and *except* for aseptic fill-finish, where format non-fungibility can strand nameplate capacity against a changed product mix [E-6019].

---

## 5. B6/B7 ranking test — independent verdict on Agent C's placements

I verified Agent C's two flagged items independently. I did not read Agent C's evidence and did not inherit any of it.

### 5.1 On B6 ranked 9th of 16 at whole-system level

**Verdict: the rank is defensible as a weighted average, and Agent C is right that it misrepresents the item. I go further: as a scalar it is a category error and should not be carried.**

Supporting the rank itself: my independent elasticity test gives a system-wide elasticity of ~0.05 for a 10% manufacturing improvement [E-6075]. Mid-table is where an elasticity of 0.05 belongs. The CRL evidence independently supports mid-table rather than top: manufacturing is implicated in 74% of first-cycle rejections but terminal in only ~20% of permanent non-approvals, so its dominant effect is a review-cycle delay rather than a programme kill [E-6074].

Against carrying it as one number: the modality spread I measure is **9.4x** between plasmid/lentiviral (1.06x) and small molecule (10x) [E-6070], with autologous cell therapy at 1.19x and structurally inelastic in a way no other modality is [E-6063]. Agent C's characterisation of autologous cell therapy as an order of magnitude more constrained than the system average is **confirmed** — 1.19x against a slack-modality range of 4.8–10x is between 4x and 8x on the multiple, and effectively an order of magnitude once the absence of a batch-size lever is accounted for. A single ordinal rank averages a binding constraint and a non-constraint into a number that is true of nothing.

**Recommendation: split B6 into four entries** rather than carrying one rank:

- **B6a — Shared upstream and downstream inputs (GMP plasmid DNA; aseptic fill-finish).** System-wide, binding/near-binding at 1.06–1.12x, with a 3-year response lag on fill-finish. This is the highest-ranking fragment and it currently has no visibility because it is buried inside a modality-agnostic B6.
- **B6b — Viral vector suites (AAV, lentiviral).** Bifurcated: AAV slack in aggregate (1.5–1.9x) with a booked commercial-quality tier; lentiviral binding (1.06x).
- **B6c — Autologous cell therapy manufacture.** Binding, 1.19x, structurally inelastic, elasticity on patients treated ≈ 1.0.
- **B6d — Bulk API and mAb drug substance.** Slack at IND stage (4.8–10x); binding only at commercial launch scale.

`[INFER]` If forced to keep one rank, B6 belongs mid-table, but the ranked artefact should carry B6a separately and higher, because shared inputs are the fragment that actually gates system throughput and the fragment most likely to be missed by a modality-organised analysis.

### 5.2 On "AAV vector manufacturing supply now outpaces clinical demand"

**Verdict: CONFIRMED on direction; the supporting number is provenance-weak and should not be quoted as measured.**

- The headline "<50% suite utilization" traces only to Mordor Intelligence and IntuitionLabs with no disclosed sample or denominator; I recorded it with `circular_risk:true` [E-6005].
- The direction is independently corroborated by two events that no analyst controls: National Resilience closing six of ten manufacturing sites in 2025 [E-6006], and an FDA-approved 125,000 sq ft commercial viral vector plant with two GMP drug substance suites plus fill-finish transacting at USD 4.5 million in October 2025 [E-6007]. `[INFER]` A distressed asset price is a market-clearing observation and is a stronger form of evidence for excess supply than any survey.
- **One correction to how the finding should be stated.** It coexists with 18-month slot lead times [E-6005], and that is not a contradiction: it is a tier mismatch, with commercial-grade high-titre low-empty-capsid suites booked while early-phase suites from the 2020–2022 capital wave sit idle [E-6005; E-6016]. Stating "AAV supply outpaces demand" without the tier qualifier would mislead a sponsor who needs commercial-quality material.

### 5.3 My independent placement of B7

`[INFER]` I do not have Agent C's B7 rank and will not assume one. My independent view: **B7 should rank materially above B6 on the 2030–2040 horizon, in the top third of the catalogue.** The reasoning follows the common brief's constraint definition:

- B6 gates the *throughput* of programmes that are already addressable, and it responds to capital within 3–5 years. Its measured elasticity is ~0.05 [E-6075].
- B7 gates *which targets are addressable at all*. A target in a tissue with no viable delivery route does not enter the pipeline, so B7 sets the numerator of approvable programmes rather than the rate at which the numerator is processed. It does not respond to capital on any timescale — the BBB took nine years from first shuttle publication to first platform approval [E-6073], and solid-tumour transport has not moved at all in a decade [E-6076].

The one thing that would demote B7 sharply is the §3.5 finding that a portion of the delivery problem is really a preclinical-model problem [E-6071]. `[INFER]` To the extent that "delivery is hard" is actually "our murine selection systems mispredict primates," the constraint belongs at least partly to B2 and B10, and fixing it is cheaper and faster than fixing a physical barrier would be. I would state B7's placement conditionally: **top third, with the caveat that the solid-tumour fragment is a genuine physical limit and the CNS/extrahepatic fragments are engineering problems currently being solved.**

---

## 6. UNRESOLVED

14 items are recorded in full in `./RLSX/work/G/unresolved.csv`, each with the complete set of search queries attempted, the failure reason, at least three alternative sources tried, a current best estimate and the basis for that estimate. They are:

1. Aseptic fill-finish global utilization rate
2. ADC bioconjugation suite utilization or booking lead time
3. Innovator small-molecule API / oral solid dose utilization rate
4. Aggregate global installed AAV and lentiviral suite count with a public methodology
5. Numeric utilization of installed mRNA drug substance lines
6. CMC share of the 89 CRLs issued for pending or withdrawn applications
7. Global vaccine installed dose capacity and utilization
8. Quantified rate of clinical trial delays attributable to manufacturing or CMC
9. Explicit utilization percentages in Lonza, Catalent/Novo, Thermo Fisher and Charles River filings
10. Annual flow of new CBER cell and gene therapy INDs
11. Published numeric cross-species transfer failure rate for engineered AAV capsids
12. Directly measured human %ID to liver for a clinical ionizable LNP
13. Human muscle %ID versus liver %ID for systemic AAV
14. GMP batch failure / out-of-specification rate for AAV and lentiviral vector production

Every one carries a best estimate; none is left blank. Items 1, 2, 3, 5 and 7 share a single root cause worth naming: **the industry does not publish capacity denominators.** Utilization is a ratio, and the denominator — installed capacity — is a competitive disclosure that CDMOs withhold. `[INFER]` This is why "capacity crunch" and "overbuild" narratives circulate unfalsified in the same markets at the same time, and it is the reason I anchored this analysis on asset transactions, site closures, lead times and legally-attested company statements rather than on utilization claims.
