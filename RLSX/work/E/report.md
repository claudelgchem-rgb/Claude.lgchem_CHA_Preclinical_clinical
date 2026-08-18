CHARTER_ACK: R1,R2,R3,R4

# Agent E — Regulatory, Policy and Evidence Standards (B5 and adjacent)

Basal-state analysis. H0 is treated as a hypothesis under test, not a premise. No conclusion here is tilted toward any company, modality or region. All confidence grading is left to Agent R; every record in `RLSX/evidence/parts/E.jsonl` carries `confidence: null`, `graded_by: null`.

---

## 0. Methodology

**Scope.** Five agencies (FDA, EMA, PMDA, NMPA, MFDS) across five mandatory topics (NAM acceptance, AI-derived evidence, review capacity, accelerated pathways, cell/gene-therapy routes). Every assigned item was processed; unresolvable items are recorded in `unresolved.csv` with full query logs.

**Sources.** 58 WebSearch/WebFetch calls, of which 8 were blocked by HTTP 401/403 or an unfollowable redirect and were replaced by independently corroborated substitutes. Priority order: statute text (congress.gov, uscode.house.gov), Federal Register, agency primary pages (fda.gov, ema.europa.eu, pmda.go.jp, english.nmpa.gov.cn, mfds.go.kr), then peer-reviewed analyses, then specialist regulatory press (RAPS, Citeline, Arnold & Porter, Wilson Sonsini, Spencer Fane). `www.fda.gov` and `federalregister.gov` returned HTTP 401/302-block to the fetch tool in this environment; those facts were recovered through indexed agency-page search summaries plus at least one independent non-agency corroborant per record, and the agency URL is retained in `provenance_hops` so the chain is auditable.

**The distinction that governs this whole domain.** Five status tiers are kept strictly separate throughout, because conflating them is the dominant error in regulatory commentary:

| Tier | Binding on FDA? | Sponsor can rely on it? | Example in this dataset |
|---|---|---|---|
| statute | yes | yes, but only as written | FDAMA 2.0; FDORA §2503; PDUFA |
| binding_guidance / final guidance | no (guidance is non-binding) but represents settled agency position | largely yes in practice | ICH S1B(R1); ICH M15; surrogate endpoint table |
| draft_guidance | no | no — current thinking only | AI credibility framework (Jan 2025); mAb nonclinical (Dec 2025); plausible mechanism (Feb 2026) |
| pilot | no | only if selected, and slots are tiny | ISTAND; START; CNPV; Ex-IND |
| aspirational | no | no | Animal-testing roadmap; RDEP; EMA AI reflection paper |

**Constraint test.** Per the common brief §2, a step is a rate-limiting step only if improving it raises system output (annual approvals; approvals per $). Elasticity (M2), not slowness, is the criterion. Every topic below carries an explicit `constraint` / `reliever` / `mixed` / `neutral` verdict, and the same verdict is machine-readable in the `direction` column of `RLSX/data/regulatory_landscape.csv` (49 rows).

---

## 1. NAM acceptance pathways

### 1.1 What FDAMA 2.0 actually changed versus what is claimed

The FDA Modernization Act 2.0 was enacted 29 Dec 2022 inside the Consolidated Appropriations Act 2023. It amended FD&C Act §505(i) and PHS Act §351(k) so the required package reads "nonclinical tests" instead of tests that must include animal testing, and it explicitly names cell-based assays and computer models among permissible alternatives [E-4001].

What it did **not** do, contrary to very widespread reporting: it did not require FDA to accept any specific non-animal method, did not create a qualification right, and did not amend FDA's own regulations. The decisive proof is FDAMA 3.0 itself — the bill's entire operative content is an order to HHS/FDA to publish an interim final rule within one year of enactment replacing "animal" with "nonclinical" throughout the 21 CFR IND regulations [E-4002]. If the 2022 statute had changed the regulations, the 2026 bill would be unnecessary. FDAMA 3.0 passed the House 20 Jul 2026 and the Senate passed the same language in Dec 2025, but it was **not enacted law as of 18 Aug 2026** [E-4002]. So for three and a half years the statute said "nonclinical" while the binding regulation still said "animal". [INFER] That gap is the single cleanest example in this whole report of announced change outrunning binding change.

### 1.2 Counting qualified tools, not announced programmes

ISTAND accepted **eight** submissions across roughly five years of pilot operation — three AI-based tools, two animal-free preclinical safety tools, two tissue-based methods, one novel statistical approach — and was converted to a permanent DDT qualification programme on 31 Jul 2025 [E-4003]. Exactly **one** tool has completed full qualification: the AI-Based Histologic Measurement of NASH, qualified 8 Dec 2025 for MASH trials [E-4004]. Zero organ-on-chip and zero in-silico toxicology tools are formally qualified. Derived throughput: ~1.6 accepted submissions/year and ~0.2 qualifications/year [E-4055].

### 1.3 The April 2025 roadmap and its actual milestones

The roadmap (Apr 2025) is a policy statement sequencing monoclonal antibodies first, then other biologics, then new chemical entities and countermeasures [E-4005]. Its Year-1 deliverables, with correct legal tiers:

- 31 Jul 2025 — ISTAND made permanent (programme status change) [E-4003]
- Aug 2025 — FDA–NIH MOU on alternative-method standardisation (agreement, not rule) [E-4004]
- Oct 2025 — NAMs Acceptability Database live (transparency inventory) [E-4008]
- 2 Dec 2025 — **draft** guidance removing routine six-month NHP studies for mAbs in favour of weight-of-evidence [E-4006]
- 8 Dec 2025 — first AI DDT qualified [E-4004]
- 18 Mar 2026 — **draft** NAM general-considerations guidance, four validation principles, plus LAL alternatives [E-4007]
- 29 May 2026 — oncology nonclinical guidance centred on three-month tox studies [E-4009]

So the substantive animal-reduction content sits in draft guidance, and the only fully binding, cross-region NAM instruments in the dataset are the ICH ones.

### 1.4 ICH and the EU

ICH S1B(R1) (2022) permits a six-factor weight-of-evidence assessment in lieu of the two-year rat carcinogenicity bioassay, implemented in the US, EU and Japan and underpinned by a prospective ICH S1 study — the strongest evidence base of any NAM item here [E-4010]. ICH M15 on model-informed drug development reached Step 4 on 29 Jan 2026 and FDA adopted it via Federal Register notice on 3 Jun 2026, converting MIDD/in-silico modelling from best practice to harmonised regulatory expectation [E-4011].

The European Commission adopted its Roadmap towards phasing out animal testing for chemical safety assessments on 1 Jun 2026: 15 domains including pharmaceuticals, over 30 recommendations, a regulatory-needs report due 2027, an indicator dashboard by end-2026 [E-4012]. Critically, **biologicals, vaccines, gene therapies and ATMPs are excluded from its framework** [E-4012] — i.e. the EU roadmap omits exactly the modalities where animal models are least predictive.

### 1.5 Verdict — NAM

**Direction: reliever, but a weak one, with one narrow constraint pocket.** Reliever because nothing in the current framework blocks a sponsor from filing NAM data in an individual IND; the statute is permissive [E-4001], the mAb and oncology guidances actively remove animal study requirements [E-4006][E-4009], and ICH S1B(R1)/M15 give cross-region cover [E-4010][E-4011]. The constraint pocket is narrow and specific: if a sponsor wants a *portable, pre-agreed* NAM — one qualified once and reusable across programmes — the qualification channel processes ~0.2 tools/year [E-4055]. [INFER] That is a real limit on NAM *industrialisation*, but not on NAM *use*, and it does not currently gate any approval, because no product is waiting on a NAM qualification to be approved.

---

## 2. Regulatory acceptance of AI-derived evidence

FDA's draft guidance "Considerations for the Use of Artificial Intelligence to Support Regulatory Decision-Making for Drug and Biological Products" appeared 6–7 Jan 2025 with a risk-based seven-step credibility-assessment framework anchored on a defined context of use; comments closed 7 Apr 2025 and the document was **still in draft** as of Aug 2026 — nineteen months without finalisation [E-4013].

CDER reports over 500 submissions containing AI components from 2016 to 2023, CBER over 560, concentrated in oncology, neurology and gastroenterology [E-4014]. **FDA has never published the denominator**, so the AI share of all submissions cannot be computed from agency data; the widely quoted "500+" is a numerator in search of a base [E-4014]. Against CDER's FY2024 scale of 1,979 completed PDUFA actions in a single year [E-4021], 500 AI-touching submissions spread over eight years is plainly a minority phenomenon. [INFER]

Neither FDA nor EMA has created any distinct pathway, designation or evidence standard for AI-*designed* molecules; such candidates use the ordinary IND/CTA and NDA/BLA/MAA route, and the credibility framework attaches only where an AI model itself generates evidence used in a decision [E-4017]. This matters for H0: **there is no regulatory gate specific to AI-derived candidates to be a bottleneck at.**

FDA's internal Elsa assistant was deployed agency-wide in Jun 2025 for summarisation, protocol-review support, label comparison and inspection targeting; reviewers publicly reported fabricated study and citation output and inability to link external literature, and reporting indicates it is not embedded in product-review decision systems [E-4015]. Elsa therefore adds no measurable review capacity today.

EMA/HMA published the first AI reflection paper in Sep 2024 as one deliverable of the 2023–2028 AI workplan, designed to interlock with the EU AI Act [E-4016]. A reflection paper is not a scientific guideline and carries no binding acceptance criteria [E-4016].

### Verdict — AI evidence

**Direction: mixed, leaning neutral.** Neutral because AI-discovered molecules face no special gate [E-4017] — the frequently asserted "regulators won't accept AI drugs" framing is not supported by any instrument found. Mixed because where an AI model *substitutes* for evidence (a surrogate model replacing a study), the sponsor faces a non-final draft framework in the US [E-4013] and a non-binding reflection paper in the EU [E-4016], which is uncertainty, not prohibition. [INFER] Uncertainty raises sponsor cost and conservatism; it does not currently reduce approvals per year.

---

## 3. Review capacity and staffing — the direct B5 test

### 3.1 The inputs collapsed

HHS executed a reduction in force on 1 Apr 2025 covering roughly 3,500 FDA positions within a ~10,000-position departmental cut; the CBER director and the CDER Office of New Drugs director were among the departures [E-4018]. FDA's own FY2025 figures: **CDER ended at 5,044 staff, a net loss of 1,093 (−17.8%), against a net gain of 259 in FY2024; CBER ended at 1,339, a net loss of 224 (−14.3%), against a net gain of 105 in FY2024; combined 6,383, down 1,317 in one year** [E-4019]. Leadership churn continued: the CDER director resigned Nov 2025, the CBER director departed Mar 2026, and the Office of Therapeutic Products saw staff disruption [E-4051].

### 3.2 The outputs did not

- 96% of CDER approvals met their PDUFA goal date in 2025; 47 of 50 novel approvals (94%) met it in 2024; FDA met all 10 of 10 FY2024 PDUFA review performance goals [E-4020].
- FY2024: 1,979 review actions completed, with 1,690 further submissions pending **inside** their goal dates — a pending pile that is in-contract, not overdue [E-4021].
- Novel CDER approvals: 50 in 2024, 46 in 2025 [E-4022].
- Derived: output fell ~8% while the review workforce fell ~17.8% [E-4056]. Approvals in year *t* reflect filings one to three years earlier, so this is a lagged, not contemporaneous, test — the 2026 and 2027 cohorts are where a staffing effect would surface, and H1 2026 NDA/BLA approvals were reported down, with CDER novel approvals recovering and CBER's count dropping [E-4028].

### 3.3 The queueing question: who is waiting for whom?

This is the decisive evidence and it points one way.

- **The agency's IND workload is growing at 1.7%/year, not surging.** CDER had 14,870 active INDs in 2024 with 1,855 newly received, rising to 15,124 active in 2025 [E-4024][E-4025]. Active INDs rose 15% across 2020–2024 with growth *decelerating* from +6.8% in 2021 to +1.7% in 2024 [E-4024].
- **The pending review pile is inside goal dates** [E-4021], which is the formal definition of a queue that is not backed up.
- **US CGT output is running below FDA's own stated capacity expectation.** FDA projected 10–20 CGT approvals/year by 2025 in 2019; actual was 7 in 2023 and 8 novel in 2024 [E-4050]. The centre built extra capacity (OTP created 2023 with a plan for 125 new staff [E-4052]) and the submissions did not arrive at that rate. [INFER] That is the signature of an agency waiting on applications, not applications waiting on an agency.
- **The CNPV pilot proves review time was compressible.** 21 vouchers awarded Oct 2025–May 2026; 10 approvals by Jul 2026 with filing-to-action times of 1, 24, 31, 44, 54, 55, 79, 113, 157 and 166 days — median 54.5 days against a 300–365 day standard clock [E-4033][E-4053]. [INFER] A programme that can cut a review to 44 days for selected products, executed during the *worst* staffing year in the agency's modern history, is direct evidence that the 10-month clock contained slack rather than reflecting a binding resource limit.

### 3.4 Where FDA capacity genuinely *is* fragile

Two findings run the other way and should not be discounted:

- **Money, not headcount.** Entering FY2025, FDA disclosed that carryover user-fee balances would fund **fewer than ten weeks (9.82 weeks)** of drug review work, with FY2024 collections below target [E-4023]. The review programme has under three months of financial buffer.
- **Appropriations risk is a real throughput chokepoint.** During the shutdown beginning 1 Oct 2025, FDA lost authority to accept *any* new fee-requiring submission — NDAs, BLAs, ANDAs, biosimilars — while continuing in-flight reviews on carryover with ~86% of staff retained [E-4026]. PDUFA VII expires Sep 2027, with FDA's recommendations due to Congress by 15 Jan 2027.

[INFER] The correct statement is therefore not "FDA has spare capacity" and not "FDA is the bottleneck", but: *FDA's throughput is currently adequate to demand and structurally underwritten by a funding mechanism with under three months of slack and a hard reauthorisation cliff in Sep 2027.* The vulnerability is financial and legislative, not a reviewer shortage.

### 3.5 Other regions

EMA runs on roughly 897 in-house staff and a ~€478m budget while drawing on over 4,500 external national-agency experts, and recommended 104 human medicines in 2025 of which 38 had a new active substance [E-4027][E-4022]. PMDA has about 873 employees including ~560 technical reviewers [E-4027]. Derived staffing-per-output: 138.8 CDER+CBER staff per novel CDER approval versus 23.6 EMA staff per new active substance [E-4058] — a ratio that is *not* evidence of FDA inefficiency, because FDA's staff also carry generics, OTC, supplements, inspections and post-market work while EMA externalises assessment to the national network [E-4058].

### Verdict — review capacity

**Direction: neutral in the US today, with a constraint tail risk.** Neutral because on-time performance held at 94–96% through an 18% workforce contraction [E-4020][E-4056], the pending pile is inside goal dates [E-4021], IND growth is 1.7%/year [E-4025], and CGT output is below the agency's own capacity plan [E-4050]. Constraint tail risk from the <10-week funding buffer [E-4023], the demonstrated ability of an appropriations lapse to halt new-submission intake entirely [E-4026], and lagged 2026–2027 effects of the RIF [E-4028].

---

## 4. Accelerated pathways and surrogate endpoints

### 4.1 United States

FDORA (Dec 2022) made four statutory accelerated-approval changes: authority to require confirmatory trials be underway at approval, an expedited withdrawal procedure, mandatory public confirmatory-trial status reporting, and an internal Accelerated Approval Council [E-4030]. The expedited withdrawal power was first used in Feb 2024 on Pepaxto, and by 2026 withdrawals had spread beyond oncology to Makena, Ocaliva, Andexxa and Elevidys [E-4031]. Uptake held up: 14 new accelerated approvals in CY2025 against 46 novel CDER approvals [E-4032][E-4022].

Designations: breakthrough therapy — ~540 granted of ~1,300 requests through 2024, a ~40% grant rate [E-4035]; RMAT — operating since 13 Dec 2016 with grant rates well under half and FDA publishing granted, withdrawn/rescinded and approved lists [E-4036].

Vouchers: the rare pediatric disease PRV lapsed Dec 2024 and was reauthorised 3 Feb 2026 by the Consolidated Appropriations Act 2026 with a 30 Sep 2029 sunset; 63 RPD PRVs have issued since 2012 across 47 diseases, four in 2025 [E-4034]. The Commissioner's National Priority Voucher pilot is the standout: 21 vouchers, 10 approvals, median 54.5 days filing-to-action [E-4033][E-4053].

Surrogate endpoints: FDA's public table, first published 2018 under the 21st Century Cures Act and refreshed roughly six-monthly with separate adult and paediatric sections, lists **over 200** surrogate markers accepted or acceptable as a basis for approval [E-4037]. This is materially larger than the handful of formally *qualified* biomarkers, and it bears directly on any B15 "surrogate endpoint scarcity" candidate: **the accepted set is two orders of magnitude larger than the qualified set**, so scarcity of surrogates is not primarily a regulatory-listing problem. [INFER]

### 4.2 Europe, Japan, China, Korea

- **EMA PRIME**: 98 acceptances Mar 2016–Jun 2021 with 18 authorised; 6 new acceptances and 8 conditional marketing authorisations in 2025 [E-4038]. Best measured effect anywhere in this dataset: in 26 EMA-approved ATMPs through Nov 2024, PRIME-supported products reached authorisation in a median 376 days versus 669 without (−42.7%), orphan status gave a statistically significant −32.8%, and CMA at 405 days versus 462 standard and 644 exceptional circumstances was **not statistically significant** [E-4039]. [INFER] The PRIME effect is uncontrolled for selection — PRIME admits the best-prepared programmes — so 42.7% is an upper bound on the causal effect, not the causal effect.
- **PMDA Sakigake**: 22 drugs plus 11 regenerative products by 31 May 2019, still in use (bemdaneprocel, Dec 2025) [E-4040].
- **NMPA**: 289 NDAs approved in 2025 including ~120 new drugs, 61 first-in-the-world approvals and 48 first-in-class [E-4042]; Announcement [2025] No.86, effective 9 Sep 2025, commits CDE to a **30-working-day** review of clinical trial applications for eligible Class I innovative drugs, with 20-working-day notification and a 60-day maximum extension — converting a 2024 pilot into standing policy [E-4043].
- **MFDS GIFT**: launched Sep 2022 under Pharmaceutical Affairs Act Art.35-4 and Advanced Regenerative Medicine Act Art.36; cuts assessment from 120 to 90 working days, adds rolling review and post-approval submission of certain non-safety data; 56 designated and 34 approved as of 8 Feb 2024 (15 COVID-19 vaccines, 8 biologics, 7 chemical drugs; anticancer 51.6% of approvals) [E-4041].

### 4.3 Evidence-quality controversy

The FDORA reforms are a deliberate tightening: confirmatory trials must be underway, status must be published, and withdrawal is faster [E-4030][E-4031]. Simultaneously FDA is signalling a loosening for rare disease via the plausible-mechanism framework and a single-trial-plus-confirmatory-evidence default [E-4047]. [INFER] These move in opposite directions and the net effect on the *evidence bar* is currently indeterminate; what is not indeterminate is that neither is currently reducing the number of approvals.

### Verdict — accelerated pathways

**Direction: strong reliever on T, mixed on P.** Reliever: CNPV compresses review by ~8–10 months for selected products [E-4053], PRVs convert a 10-month clock to 6 months [E-4034], PRIME/CMA/Sakigake/GIFT/NMPA-30-day all cut elapsed regulatory time [E-4039][E-4040][E-4041][E-4043], and 14 of 46 US novel approvals in 2025 used accelerated approval [E-4032]. Mixed on probability of success: FDORA's withdrawal machinery raises the post-approval bar [E-4031] while RDEP and plausible-mechanism lower the pre-approval bar for ultra-rare disease [E-4046][E-4047].

---

## 5. Cell and gene therapy dedicated routes

**Platform technology designation** (FDORA §2503, codified 21 U.S.C. §356k, draft guidance May 2024) has been used almost not at all. The first designation went to Sarepta's AAVrh74 vector platform in Jun 2025 and was **revoked about a month later** after three patient deaths; the second went to Krystal Biotech's non-replicating HSV-1 vector platform in Oct 2025, extended to further Krystal programmes reported May 2026 [E-4044]. Effectively one live platform holder in nearly four years of statutory availability.

**START pilot** (FR announcement 2 Oct 2023, launched 31 May 2024) is a joint CDER–CBER programme offering rapid ad-hoc advice, capped at three sponsors per centre — **six slots** [E-4045]. Against rare-disease IND volume this is a rounding error.

**RDEP** was announced 3 Sep 2025 for ultra-rare genetic disease under 1,000 US patients with a known inborn genetic defect and significant unmet need; eligibility grants have issued (e.g. Repair Biotechnologies' REP-0003) [E-4046]. It is an announced framework, not a statute. The **plausible mechanism** draft guidance followed on 23 Feb 2026, allowing conditional consideration of individualised therapies on mechanistic grounds and signalling a single-trial-plus-confirmatory-evidence default across drugs [E-4047] — potentially the largest evidence-standard relaxation in this dataset, and entirely non-binding today.

**EU ATMP hospital exemption** (Reg. (EC) 1394/2007 Art.28): 110 HE-ATMPs authorised across the EU 2008–2025, of which only 62 remain available, covering 28 indications — 37 somatic cell, 21 tissue-engineered, 4 gene therapy [E-4048]. [INFER] A 44% attrition rate among hospital-exemption products, and the diversion of ATMP activity out of the centralised route, means the exemption relieves patient access while fragmenting the evidence base that would support EU-wide authorisation.

**Japan's conditional and time-limited approval** for regenerative medical products (2014 PMD Act) produced five approvals, and the first (HeartSheet) went through a second review for full approval [E-4049] — a genuine reassessment gate, not a permanent shortcut. Three of the five also held Sakigake status [E-4040].

**Measured effect on approvals per year.** US CGT approvals were 7 in 2023 (cumulative 35) and 8 novel plus ≥6 new indications in 2024, against FDA's 2019 projection of 10–20/year by 2025 [E-4050]. CBER approved two orphan products in H1 2026 [E-4051]. The EMA ATMP timeline study gives the only clean measured effect: gene therapies reached authorisation in a median 385 days versus 660 for cell therapies and 1,174 for tissue-engineered products [E-4039].

### Verdict — CGT routes

**Direction: reliever in design, neutral in measured effect.** Every route listed is intended to accelerate, and none is blocking. But platform designation has one live holder [E-4044], START has six slots [E-4045], RDEP and plausible-mechanism are announced/draft [E-4046][E-4047], and CGT output sits below FDA's own projection with capacity deliberately built for more [E-4050][E-4052]. [INFER] The binding constraint on CGT approvals per year is upstream of the regulator — manufacturing (B6), delivery (B7) and trial feasibility in tiny populations (B3/B4) — which is exactly why building 125 OTP review slots [E-4052] did not produce 10–20 approvals/year.

---

## 6. B5 ranking test — independent verdict on Agent C's 14th-of-16

**Agent C's position:** B5 ranked 14th of 16 on improvement elasticity, reasoning that review time is a small share of total elapsed time and that FDA has been meeting most PDUFA goal dates.

**My verdict: C's placement is broadly correct on the elasticity question, and C's *reasoning* is right for one of its two limbs and under-argued for the other. I would place B5 12th–14th of 16 — the same neighbourhood — but I reject the framing that B5 is low-elasticity *because FDA meets goal dates*, and I add a funding-cliff qualifier C omitted.**

### 6.1 Limb one — "review time is a small share of elapsed time." Confirmed, and quantified.

Derived Amdahl ceiling: a standard 10-month PDUFA action period (6 months priority) plus filing is ~10–12 months out of a total development span commonly cited at 10–15 years, i.e. **~5.6–10.0% of elapsed time, midpoint ~7.5%** [E-4057]. The CNPV pilot supplies the empirical upper bound directly: compressing review to a median 54.5 days saves roughly 8–10 months per product [E-4053]. Driving FDA review to zero removes at most ~5–8% of total elapsed development time [E-4057]. Note that the 10–15 year total-development figure is an anchor under test per the common brief and is not adopted here as verified; the derived share is therefore a bounded estimate.

A 10% improvement in B5 — reading "improvement" as 10% faster review — therefore buys ~0.5–1.0% of total elapsed time and, since review capacity is not rejecting applications [E-4021], approximately zero additional approvals per year. That is a very low elasticity. **Limb one holds.**

### 6.2 Limb two — "FDA has been meeting PDUFA goal dates." True but non-probative as stated; the right argument is a queueing argument.

Meeting goal dates is compatible with being a constraint: an agency could meet every goal date while sponsors ration submissions to fit agency bandwidth, or while goal dates are set to whatever the agency can absorb. On-time performance alone cannot distinguish "adequate capacity" from "demand suppressed to match capacity."

The load-bearing evidence is queueing evidence, which C did not present and which I collected:

1. The FY2024 pending pile of 1,690 submissions was **inside** goal dates, not overdue [E-4021].
2. CDER IND growth is +1.7%/year and decelerating [E-4024][E-4025] — no demand surge pressing the intake.
3. CGT approvals ran at 7–8/year against FDA's own projection of 10–20/year, after CBER built OTP with a plan for 125 additional staff [E-4050][E-4052] — the agency built capacity that submissions did not fill.
4. Review time proved compressible to a median of 54.5 days for selected products **during the worst staffing year in decades** [E-4033][E-4053][E-4019] — slack existed inside the standard clock.
5. Output fell ~8% while the review workforce fell ~17.8% [E-4056].

Points 1–4 together are the actual demonstration that the agency is waiting on applications rather than applications waiting on the agency. [INFER] **So C reaches the right conclusion on a weaker argument than the evidence supports.**

### 6.3 Where I depart from C: two corrections and one addition

**Correction 1 — B5 is not monolithic; one sub-element is materially higher-elasticity than the rest.** B5 as defined in the catalog bundles "review capacity" with "evidence standards (incl. acceptance of AI/NAM evidence)". These have different elasticities:
- *Review capacity* — near-zero elasticity on annual approvals, per §6.1–6.2.
- *Evidence standards* — meaningfully higher elasticity, because a change in what counts as adequate evidence changes the **probability of success**, not just duration, and P enters approvals-per-year multiplicatively. The plausible-mechanism framework and a single-trial-plus-confirmatory-evidence default [E-4047], RDEP [E-4046], and the >200-entry surrogate endpoint table [E-4037] are P-axis levers. [INFER] If the plausible-mechanism default is finalised as drafted, it plausibly changes rare-disease approval probability by more than any conceivable review-speed change changes approval counts.
- Under the common brief's own definition (a step whose improvement raises system output), the evidence-standards half of B5 outranks the review-capacity half by a wide margin. If B5 were split, review capacity would sit ~15th–16th and evidence standards ~8th–10th. [INFER]

**Correction 2 — "regulation as brake" and "regulation as spare capacity" are both wrong for 2025–26; regulation has been a net *reliever* on the T axis.** Counting `direction` in `regulatory_landscape.csv`: 30 of 49 mechanisms are relievers, 8 mixed, 6 constraints, 5 neutral. The measured time effects all point the same way — CNPV median 54.5 days versus a 300–365 day clock [E-4053], PRIME −42.7% on ATMP authorisation time [E-4039], NMPA 30-working-day INDs [E-4043], GIFT 120→90 working days [E-4041], PRVs 10→6 months [E-4034], mAb guidance removing six-month NHP studies [E-4006]. Over the last 24 months regulators have been actively removing elapsed time, not adding it. C's ranking is consistent with this; C's stated reasoning does not capture it.

**Addition — the tail risk C omits.** FDA's review programme entered FY2025 with under ten weeks of carryover funding [E-4023], and the Oct–Nov 2025 shutdown demonstrated that an appropriations lapse halts new fee-requiring submission intake entirely while in-flight reviews continue [E-4026]. PDUFA VII expires Sep 2027. [INFER] This is a low-probability, high-severity discontinuity, not a gradual elasticity. It belongs in a scenario column, not in the elasticity ranking — which means it does not move B5 up the *ranking*, but it does mean B5's variance is much higher than a 14th-place point estimate conveys.

### 6.4 Bottom line

C's 14th-of-16 placement for B5 survives independent testing on primary evidence. I would say **12th–14th**, the difference being entirely attributable to the evidence-standards sub-element rather than to review capacity. **Review capacity taken alone belongs at or near the bottom of the 16.** Any conclusion that regulatory review is *the* rate-limiting step of 2026 drug development is not supported by the primary-source record: the pending queue is in-contract [E-4021], intake is growing 1.7%/year [E-4025], the agency built CGT capacity that submissions did not fill [E-4050][E-4052], and the agency compressed review to 44–55 days for selected products in its worst staffing year [E-4033][E-4019].

---

## 7. Region comparison (US / EU / CN / JP-KR)

| Dimension | US (FDA) | EU (EMA) | CN (NMPA/CDE) | JP (PMDA) | KR (MFDS) |
|---|---|---|---|---|---|
| In-house review staff | 6,383 CDER+CBER, −1,317 in FY2025 [E-4019] | ~897 + >4,500 external experts [E-4027] | not published in sources located (UNRESOLVED U-04) | ~873, ~560 technical reviewers [E-4027] | not published in sources located (UNRESOLVED U-04) |
| Annual novel output 2025 | 46 novel CDER approvals [E-4022] | 38 new active substances of 104 recommended [E-4022] | 289 NDAs, ~120 new drugs, 61 first-global, 48 first-in-class [E-4042] | not separately located (UNRESOLVED U-05) | not separately located (UNRESOLVED U-05) |
| On-time performance | 96% of 2025 approvals met PDUFA goal [E-4020] | not published as a goal-date metric | 30 working days for eligible Class I INDs [E-4043] | Sakigake target reductions [E-4040] | GIFT 120→90 working days [E-4041] |
| Flagship time-compression | CNPV median 54.5 days [E-4053] | PRIME median 376 vs 669 days [E-4039] | Announcement [2025] No.86 [E-4043] | Sakigake + conditional approval [E-4040][E-4049] | GIFT rolling review [E-4041] |
| NAM posture | Statute permissive since 2022; regs not yet conformed; 1 AI tool qualified [E-4001][E-4002][E-4004] | EC roadmap Jun 2026, 15 domains, **ATMPs/biologics excluded** [E-4012] | not located as a distinct NAM programme (UNRESOLVED U-01) | ICH S1B(R1)/M15 implementer [E-4010][E-4011] | ICH member; GIFT covers regenerative products [E-4041] |
| AI evidence posture | Draft guidance since Jan 2025, unfinalised 19 months [E-4013] | Reflection paper Sep 2024 + 2023–28 workplan, non-binding [E-4016] | not located (UNRESOLVED U-02) | ICH M15 implementer [E-4011] | ICH M15 implementer [E-4011] |
| CGT dedicated route | Platform designation (1 live holder), START (6 slots), RDEP, plausible mechanism [E-4044][E-4045][E-4046][E-4047] | ATMP Reg. + hospital exemption (110 authorised, 62 live) [E-4048] | breakthrough designation in routine use [E-4042] | Conditional/time-limited approval, 5 products [E-4049] | Advanced Regenerative Medicine Act underpins GIFT [E-4041] |
| Direction verdict | mixed → net reliever on T, neutral on capacity | reliever on T, constraint on ATMP fragmentation | strong reliever, fastest-improving | reliever with a real reassessment gate | reliever |

[INFER] The most consequential regional divergence is at the IND/CTA gate, not the approval gate: China now commits to a 30-working-day affirmative approval for eligible innovative-drug clinical trial applications [E-4043] while the US is still at the RFI stage for an equivalent capacity mechanism [E-4029]. If discovery output multiplies, that is the gate that differentiates regions.

---

## 8. Where regulation *becomes* the constraint if discovery output multiplies

This is the conditional question, and it has a different answer from the current-state question.

**Current baseline.** CDER received 1,855 new INDs in 2024 and carried 15,124 active INDs into 2026, growing at 1.7%/year, against 5,044 CDER staff [E-4024][E-4025][E-4019]. Derived load: **0.37 new INDs per CDER employee per year and 3.0 active INDs per employee** [E-4054].

**10× scenario.** Ten times the IND filings means ~18,550 new INDs/year, or **3.68 new INDs per CDER employee per year** — a tenfold rise in marginal intake load with no staffing plan addressing it [E-4054]. Three specific walls appear, in this order:

1. **The 30-day IND clock, first and hardest.** The IND review is statutory, non-fee-funded in the same way, and non-deferrable: FDA must act within 30 days or the study proceeds. Unlike NDA review, there is no goal-date negotiation and no ability to queue. At 18,550 filings/year the agency has roughly 71 working days of aggregate reviewer capacity per working day of intake to absorb. [INFER] This is where a discovery-output multiplication hits first — which is exactly why FDA opened the Ex-IND RFI in Jun 2026 proposing to delegate initial-IND assessment to Qualified Research Institutions with rolling review [E-4029]. That FDA is designing a delegation mechanism for the IND gate, and not for the NDA gate, is itself evidence about which gate has the thinner margin. [INFER]

2. **Meeting capacity, second.** Type B/C meetings, pre-IND advice and the START-style intensive engagement are the scarcest reviewer-time good and scale linearly with programme count. START's six slots [E-4045] and ISTAND's ~1.6 accepted submissions/year [E-4055] are the visible evidence that FDA's *bespoke-advice* channel is already operating at pilot scale. A 10× programme count makes bespoke advice mathematically impossible and forces standardisation.

3. **NDA/BLA review, last and least.** A 10× rise in INDs does not produce a 10× rise in NDAs, because Phase II/III attrition intervenes; and 2025 demonstrated a 96% on-time rate through an 18% workforce cut [E-4020][E-4019] plus 44-day reviews under CNPV [E-4033]. [INFER] The approval gate has the most demonstrated headroom of the three.

**The non-obvious answer.** Even in the 10× scenario, the binding regulatory constraint is unlikely to be *reviewer hours*. It is:
- **funding authority** — a review system with a 9.82-week carryover buffer [E-4023] and a demonstrated shutdown failure mode [E-4026] cannot absorb a 10× fee-bearing workload without a new fee structure, and PDUFA VIII must be legislated by Sep 2027;
- **evidence standards, not throughput** — 10× more INDs from AI-derived candidates raises the question of whether ten times as many candidates can each generate an adequate clinical evidence package, which is a clinical-trial-capacity question (B3/B4) and a manufacturing question (B6), not a review-desk question. [INFER]

**Quantified conclusion.** A 10× increase in IND filings hits an agency capacity wall at the **IND gate**, at approximately 3.7 new INDs per CDER employee per year [E-4054], within roughly one to two years of the surge, and FDA's own countermeasure (delegation to Qualified Research Institutions) was at the request-for-information stage with zero participants selected as of Aug 2026 [E-4029]. It does **not** hit a wall at the approval gate on any evidence found.

---

## 9. UNRESOLVED

Six items could not be resolved to a primary source within this environment. Every one is recorded in `RLSX/work/E/unresolved.csv` with the full query list, the failure reason, at least three alternative sources attempted, and a best estimate with its basis. Summary:

- **U-01** NMPA formal NAM / non-animal-methods programme — no dedicated NMPA NAM instrument located; best estimate is that China operates through ICH implementation rather than a standalone programme.
- **U-02** NMPA position on AI-derived evidence — no CDE guidance located in English.
- **U-03** Exact cumulative CBER RMAT totals (requests / granted / denied / withdrawn) — the FDA table pages returned HTTP 401/403 to the fetch tool and search summaries returned internally inconsistent fiscal-year figures, so no figure is asserted; the qualitative facts (programme start date, publication of withdrawn/rescinded and approval lists, grant rate under half) are retained [E-4036].
- **U-04** NMPA/CDE and MFDS reviewer headcounts.
- **U-05** PMDA and MFDS novel-approval counts for 2025 on a basis comparable to FDA novel approvals and EMA new active substances.
- **U-06** Count of missed PDUFA goal dates specifically in CY2026.

None of these six changes any verdict in §1–§8. U-03 and U-06 would sharpen the B5 tail-risk assessment; U-04 and U-05 would sharpen the region table only.

---

## 10. Summary of directional verdicts

| Topic | Direction | One-line basis |
|---|---|---|
| 1. NAM acceptance | reliever (weak), narrow constraint on portable qualification | Statute permissive [E-4001]; ~0.2 qualifications/year [E-4055]; nothing blocked at product level |
| 2. AI-derived evidence | mixed → neutral | No AI-specific pathway to be blocked at [E-4017]; US framework unfinalised 19 months [E-4013] |
| 3. Review capacity | neutral now, constraint tail risk | 96% on-time through −17.8% staffing [E-4020][E-4019]; <10-week funding buffer [E-4023] |
| 4. Accelerated pathways | strong reliever on T, mixed on P | CNPV median 54.5 days [E-4053]; PRIME −42.7% [E-4039]; FDORA withdrawals tighten P [E-4031] |
| 5. CGT routes | reliever in design, neutral in measured effect | 1 live platform holder [E-4044], 6 START slots [E-4045], output below FDA's own projection [E-4050] |

**B5 overall: 12th–14th of 16 on improvement elasticity. Review capacity alone belongs 15th–16th; evidence standards alone would belong 8th–10th.**

---

# Regional top-up (EU / CN / JP-KR)

Added in a second pass to satisfy M6 region decomposition. Evidence IDs **E-4059 – E-4085**; landscape CSV extended from 49 to **80 rows** (US 33, EU 16, CN 10, JP 10, KR 8, ICH 2, US+EU 1). 18 further WebSearch/WebFetch calls. The CIRS R&D Briefing 101 PDF could not be parsed by the fetch tool, so its text was extracted locally with Python's `zlib`/`re` (standard library only) and the figures below are read from that extraction.

## R.1 EU / EMA

**Review clock.** The centralised procedure runs up to 210 *active* assessment days, interrupted by one or two clock-stops — typically three months then one month — so elapsed assessment usually runs about a year; accelerated assessment cuts the active clock to 150 days but does not touch clock-stops, which are the larger term [E-4060]. CIRS puts EMA's 2024 median approval time (submission to approval, including European Commission decision time) at **430 days** — second slowest of six agencies, against FDA 356, PMDA 290, Health Canada 363, TGA 369, Swissmedic 444 [E-4061].

**The finding that reverses the EU picture.** In 2024, EMA approved **zero** new active substances through accelerated assessment (0%), against FDA 59%, PMDA 34%, Health Canada 29%, Swissmedic 22%, TGA 9%. Four applicants requested it: one withdrew, two were refused as not of major public health interest, one reverted to the standard timetable [E-4062]. Europe's headline acceleration instrument was, in the most recent full year measured, not used at all.

**PRIME.** Over 800 eligibility requests since Mar 2016, roughly 200 granted (~25%); 2024 was 15 grants from 58 requests (27%). SMEs succeed at 22.4% (75/335) versus 34.9% (96/275) for other applicants [E-4063]. [INFER] A reliever that is materially harder for small sponsors to enter is a distributional constraint sitting inside a reliever — and small sponsors are precisely the population most likely to be running AI-derived programmes.

**Conditional marketing authorisation.** 80 CMAs granted from 107 applications 2006–Nov 2022 (~75%); use rose from ~30 in the first decade to 44 in the following six years; 11 of 30 first-decade CMAs converted to standard within four years; 4 of 71 non-vaccine CMAs were later withdrawn (Zalmoxis, Zynteglo, Lartruvo, Arzerra) [E-4064].

**The new gate with no US analogue.** The EU HTA Regulation (2021/2282) began applying 12 Jan 2025 and makes Joint Clinical Assessment **mandatory** for new oncology medicines and ATMPs. Year one supported 10 JCAs and 7 joint scientific consultations, with scope expanding in 2026; the reported burden is scoping PICO questions across divergent member-state standards of care [E-4059]. This is a genuine addition of regulatory work, not a removal.

**Pharma legislation revision.** Political agreement 11 Dec 2025, Coreper 6 Mar 2026, SANT committee 18 Mar 2026; plenary and Council adoption expected autumn 2026 and application around autumn 2028. Regulatory data protection stays at 8 years, +1 with an exclusivity voucher [E-4067].

**Binding 3Rs.** Directive 2010/63/EU Article 4 (implemented per Article 13) obliges member states to use a scientifically satisfactory non-animal method instead of a procedure "wherever possible" [E-4068]. It is the EU's only *binding* replacement instrument — stronger on paper than FDAMA 2.0, and equally non-self-executing because of the conditional wording.

**AI.** CHMP issued its first AI qualification opinion (AIM-NASH) in **March 2025** — roughly nine months before FDA qualified the equivalent tool in Dec 2025 [E-4065]. Governance moved to the Network Data Steering Group with 2025–2028 and 2026–2028 workplans and an AI Observatory reporting in 2025 and Jun 2026; guidance on AI in clinical development and pharmacovigilance is planned, and **zero binding EU AI guidelines for medicines existed as of Aug 2026** [E-4066].

**EU verdict: mixed, with the only two hard constraint additions in the dataset.** 5 reliever / 6 mixed / 4 constraint / 1 neutral across 16 rows.

## R.2 CN / NMPA-CDE

**Intake now exceeds the US.** CDE's 2024 Drug Review Report (released 18 Mar 2025) records 15,318 registration applications accepted for technical evaluation — 2,407 TCM, 10,464 chemical, 2,447 biological — including **3,073 INDs** and 549 NDAs [E-4069]. Derived: China's IND intake is **1.66×** CDER's 1,855 new INDs in the same year [E-4070]. Caveat stated in the derivation: the two counts are not identically defined, so this is an order-of-magnitude comparison.

**Speed.** Announcement [2025] No.86, effective 9 Sep 2025, gives eligible Class I innovative drugs a **30-working-day** affirmative IND approval with 20-working-day notification and a 60-day cap, converting a 2024 pilot into standing policy [E-4043]. Four statutory expedited pathways sit under the 2020 Drug Registration Regulation: breakthrough, conditional approval, priority review, special approval [E-4073].

**Output.** 289 NDAs approved in 2025, ~120 new drugs, 61 first-in-the-world approvals, 48 first-in-class [E-4042]. In CGT, 2025 produced two world-firsts: satri-cel, the first CAR-T approved anywhere for a **solid tumour**, and pCAR-19B, the first CAR-T approved specifically for paediatric/adolescent r/r B-ALL [E-4071].

**Institutional trajectory.** ICH regulatory member since 2017, Management Committee 2018 and re-elected 2021, following the 2015 State Council reform; NMPA publicly acknowledges reviewer capacity as a bottleneck and is recruiting [E-4072]. NAM policy runs through ICH transposition rather than a national qualification programme, and no dedicated AI-evidence instrument was located [E-4072].

**CN verdict: strong reliever.** 8 reliever / 1 mixed / 1 neutral across 10 rows, and the only region where both intake and output are growing fast.

## R.3 JP / PMDA

**Fastest of the six.** PMDA's 2024 median approval time was **290 days** (267 to end of scientific assessment), the shortest of the six major agencies, and it issued 148 approval decisions in FY2024-25, of which 66 were new active ingredients [E-4075]. 34% of 2024 NAS approvals used an expedited pathway, and PMDA had the **smallest expedited-versus-standard gap** of the six at 77 days, against 122 at FDA and 210 at Swissmedic [E-4076]. [INFER] Japan's standard route is already almost as fast as its expedited route, so designations buy less in Japan than anywhere else — the marginal value of an accelerated pathway is inversely related to baseline speed.

**Yet Japanese output is constrained — by sponsors, not the regulator.** As of Mar 2023, **86** drugs approved in the US or EU had no development programme in Japan at all, 60.1% of the unapproved set: 48 (56%) venture-developed, 40 (47%) orphan, 32 (37%) paediatric [E-4077]. [INFER] This is the cleanest natural experiment available on B5 anywhere in this report. Japan has the fastest review in the world and simultaneously the worst filing shortfall among major markets. If review speed were the rate-limiting step, that combination could not exist. It is direct evidence that the constraint on national output sits with sponsors' market and development decisions, and that a regulator cannot relieve it by reviewing faster.

**The accelerated-route outcome record.** Two of the five products approved under the conditional and time-limited scheme — HeartSheet and Collategene — were denied full approval and **withdrawn in 2024**; HeartSheet's confirmatory trial gave a hazard ratio of 1.9 for cardiac death over eight years, directionally worse than control, and AnGes withdrew Collategene's full-approval application on 24 Jun 2024 after failing to reproduce trial results in post-market surveillance. Stemirac has been in a publicly funded confirmatory trial since Dec 2018; Delytact has been conditional since Jun 2021 [E-4078]. [INFER] Measured against durable output, this scheme's net contribution is at or below zero: it added approvals and then removed them. That is a material correction to any assumption that accelerated routes mechanically raise system output — and it is the empirical case that FDA's plausible-mechanism framework [E-4047] will be tested against.

**JP verdict: reliever on time, constraint on evidence durability and on filing volume.** 6 reliever / 1 mixed / 2 constraint / 1 neutral across 10 rows.

## R.4 KR / MFDS

**Timelines.** GIFT (Sep 2022, PAA Art.35-4 and Advanced Regenerative Bio Act Art.36) cuts assessment from 120 to 90 working days with rolling review and post-approval submission of certain non-safety data; 34 of 56 designated products were approved as of 8 Feb 2024 — a **61% designation-to-approval conversion** [E-4041]. The 2025 reform package (dedicated review teams, expanded face-to-face consultation, rolling review, parallel GMP inspection) targets cutting the total approval timeline from ~420 to 295 days and biosimilar review from up to 420 to 240 days; this is an announced target, not a measured outcome [E-4080].

**Volume.** MFDS approved 50 IND clinical trial applications in August 2025 alone — 38 (76%) global, 12 (24%) local — implying several hundred annually in a market a fraction of the US size [E-4084].

**Regenerative medicine.** The amended Advanced Regenerative Bio Act took effect **21 Feb 2025**: it expands ARM clinical research to all indications, removes the previous restriction to severe/rare/incurable disease, and creates a new legal category — advanced regenerative medicine treatment (ARMT) — delivered outside clinical trials by designated providers, with added pricing transparency and adverse-reaction monitoring [E-4081]. ARMT shortens time to access relative to the marketing-approval track [E-4082].

**AI.** MFDS issued Guidelines for Approval and Review of Generative AI Medical Devices on 24 Jan 2025 and has announced that it will set standards for drugs and devices developed using AI; as of Aug 2026 the binding instrument covers **devices only** [E-4083].

**KR verdict: reliever, with the usual access-versus-evidence trade-off in the ARMT route.** 5 reliever / 3 mixed across 8 rows.

## R.5 The bypass-route convergence

Three of the four non-US regions now operate a route that delivers cell and gene therapies to patients *without* full centralised marketing authorisation, and each has a measurable evidence cost:

| Region | Bypass route | Uptake | Evidence cost |
|---|---|---|---|
| EU | ATMP hospital exemption, Reg. 1394/2007 Art.28 | 110 authorised 2008–2025, 62 surviving (44% attrition) [E-4048] | Diverts activity out of the centralised route; fragments the EU-wide evidence base |
| JP | Conditional and time-limited approval, 2014 PMD Act | 5 approved; **2 withdrawn after confirmatory failure** [E-4049][E-4078] | Directly negative — HeartSheet HR 1.9 for cardiac death |
| KR | ARMT under the amended Advanced Regenerative Bio Act | Route opened 21 Feb 2025 [E-4081] | Treatment delivered outside trials; central evidence generation weakened by design [E-4082] |
| US | none equivalent | — | — |

[INFER] The US is the outlier in *not* having a bypass, and the two regions with the longest operating experience of one (EU, JP) both show substantial attrition or outright reversal. That is directly relevant to the plausible-mechanism framework [E-4047]: the FDA is proposing to move toward a design whose two closest international precedents have measurable failure records.

## R.6 Does the net-reliever verdict survive regionalization?

**Short answer: it survives for the US, CN, JP and KR, and it does not survive for the EU. The original verdict was partly a US-weighted artifact — but the artifact worked in the opposite direction to what one might expect.** The US-heavy sample did not *overstate* relief by counting US relievers; it *understated* constraint by under-sampling the one region that added hard gates in 2025–26.

Direction counts by region across the 80-row landscape:

| Region | Rows | reliever | mixed | constraint | neutral | Verdict |
|---|---|---|---|---|---|---|
| US | 33 | 18 | 4 | 5 | 6 | Net reliever on T; capacity neutral; funding-cliff tail risk |
| EU | 16 | 5 | 6 | 4 | 1 | **Net mixed-to-constraining** |
| CN | 10 | 8 | 1 | 0 | 1 | Strong reliever |
| JP | 10 | 6 | 1 | 2 | 1 | Reliever on T, constraint on evidence durability and filings |
| KR | 8 | 5 | 3 | 0 | 0 | Reliever |
| ICH | 2 | 2 | 0 | 0 | 0 | Reliever |
| **All** | **80** | **44** | **15** | **11** | **10** | Net reliever, driven by CN/KR/US |

The EU divergence is not a counting artefact; it rests on four independent primary observations [E-4085]:
1. **A new mandatory gate.** JCA under Reg. 2021/2282 since 12 Jan 2025, compulsory for oncology and ATMPs, expanding in 2026 [E-4059]. Nothing comparable was added in any other region.
2. **The acceleration instrument went unused.** 0% of 2024 EMA new-active-substance approvals used accelerated assessment, versus 59% at FDA and 34% at PMDA [E-4062].
3. **The slowest-but-one clock.** 430-day median in 2024, **140 days behind PMDA** and 74 behind FDA [E-4061][E-4085], with clock-stops rather than active days being the dominant term [E-4060].
4. **Selectivity that bites hardest on small sponsors.** PRIME grant rate 22.4% for SMEs versus 34.9% for others [E-4063].

Against this, the EU is genuinely ahead on one axis — it qualified an AI tool nine months before FDA [E-4065] — and its binding 3Rs directive predates FDAMA 2.0 by twelve years [E-4068]. So the EU is not uniformly slower; it is *evidentially demanding and procedurally heavy*, which is a different thing.

**Consequence for candidate routing.** [INFER] If a sponsor's gate cost differs by 140 days of median approval time [E-4085], by a 30-working-day versus multi-month IND clock [E-4043], and by whether a mandatory joint HTA assessment attaches at launch [E-4059], the rational routing of early clinical work shifts toward China first, Japan and Korea second, the US third for pivotal work, and the EU last. The IND-intake ratio already shows this happening: China 3,073 versus the US 1,855 in 2024 [E-4070], with US intake growing 1.7%/yr [E-4025]. This is a live, measured reallocation, not a forecast.

**Consequence for the B5 ranking.** None for the US ranking — §6 stands unchanged at 12th–14th, with review capacity alone at 15th–16th. But the ranking is **region-conditional**, and this should be stated wherever the B5 rank is used downstream. For an EU-centric portfolio, B5 would rank materially higher because the JCA gate and the unused accelerated-assessment route are output-relevant in a way that US review capacity is not. Japan supplies the cleanest counter-case in the whole report: the world's fastest review coexists with 86 US/EU-approved drugs that nobody bothered to file [E-4075][E-4077] — conclusive evidence that review speed and national output are decoupled at the current margin.

## R.7 UNRESOLVED after the top-up

Still **6**, with two materially narrowed and none blocking a verdict:
- **U-01 / U-02** (NMPA NAM programme; NMPA AI-evidence instrument) — no dedicated instrument exists in any located source; both are now carried as explicit CN rows in the landscape CSV grounded in ICH transposition [E-4072] rather than left blank, and the comparative check shows no major agency has a binding AI-evidence guideline for medicines [E-4013][E-4066][E-4083].
- **U-03** (exact cumulative CBER RMAT totals) — unchanged; fda.gov returns 401/403 to the fetch tool.
- **U-04** (CDE and MFDS reviewer headcounts) — partially relieved: the workload the headcount was wanted for is now measured directly (15,318 applications, 3,073 INDs) [E-4069], so the CN capacity rows use intake volume rather than staffing.
- **U-05** — **Japan half resolved** (66 new active ingredients in FY2024-25, 290-day median [E-4075][E-4061]); Korea half still open.
- **U-06** (CY2026 missed PDUFA goal dates) — unchanged, but now benchmarked: FDA's 356-day 2024 median was second fastest of six [E-4061], so moderate slippage would leave FDA inside the peer band.
