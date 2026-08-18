# RLSX Executive Brief — where the drug-development bottleneck actually is in 2026

**For a reader making a resource-allocation decision.** Full analysis: `RLSX_report.md`. Clickable evidence: `RLSX_evidence.html`. Every claim carries a chip of the form `[E-1006 상]` — record identifier plus the reliability grade assigned by an agent that collected none of the evidence [E-9551 중].

⚠ **Read this first.** Of 774 evidence records, 7 grade 상 (High), 449 grade 중 (Medium) and 318 grade 하 (Low, 41%) [E-9551 중]. Of 572 records carrying a figure, 340 are provenance-clean, 157 are unverifiable and 75 are circular [E-9551 중]. The quantitative flow model and the bottleneck ranking both grade 하 and are arguments about mechanism, not measurements. Nothing below should be read as more certain than its chip says it is.

---

## The five answers

### Q1 — Has AI actually compressed structure prediction, sequence design and molecular generation? Quantitatively.

**Four sub-claims, four different answers.** *Computation:* substantiated and measured — ESMFold reaches a median TM-score of 0.95 against AlphaFold2's 0.96 [E-2019 중] across more than 200 million predicted structures [E-2018 하], and prospective docking against unrefined AF2 models matches experimental structures on hit rate, 54% versus 51% and 26% versus 23% [E-2012 중]. *Discovery-stage duration:* partially substantiated at **30–50% on preclinical activities**, from two peer-reviewed reviews plus a third independent one [E-2009 중] [E-2010 중]; the per-programme saving in years is never stated here in this report's own voice because that framing exists only in company-issued material [E-9534 하]. *Time to a dosed patient:* not substantiated — median founding-to-first-Phase-1 across 63 AI-native companies is 6.5 years [E-2054 하], and clinical development timelines are reported as essentially unchanged [E-2009 중]. *Probability of success:* **indeterminate, not null** — no adequately powered, denominator-matched comparison exists in either direction, and the apparent effect is set by the comparator: about +3 points against a historical 37% benchmark and +12 against the contemporaneous 28% rate [E-9537 하] [E-9513 하] [E-2003 중]. Detecting a 37-versus-40 difference at 80% power needs ~4,126 per arm against 8 completed Phase 2 assets field-wide [E-2065 하] [E-2055 하]. **Zero AI-discovered drugs have been approved by FDA as of 2026** [E-2053 중]. Independent pooled de novo binder success is 11.6% across 3,766 designs and 15 targets, against developer self-reports up to 68% [E-2020 중] [E-2023 하].

⚠ The evidence on AI is asymmetric by direction: Medium-grade where deflationary because those findings came from peer-reviewed literature and registries, Low-grade where inflationary because those came from companies and aggregators [E-2053 중] [E-2054 하]. That is a property of the source landscape, not of the grading, and a reader must apply it symmetrically.

### Q2 — Where is the true rate-limiting step in 2026, separately for T, C and P?

**P (probability): this is where the constraint is.** Phase II is the lowest-transition stage in every source examined [E-1023 중] [E-1027 중] [E-1015 중]; lack of efficacy accounts for 40–50% of all failures [E-3012 중] and toxicity for a further ~30% [E-3045 중]. The named candidates are target validation, toxicity prediction and clinical development design — dose, schedule, endpoint and population [E-9541 하] [E-3106 중].

**T (time): the long poles are clinical, and the biggest single removable block is recruitment.** Pre-IND is 21–41% of elapsed development time depending on where the clock starts [E-1093 중]; 18 of a median 29.6-month Phase III is spent recruiting [E-5060 중]; median Phase 2 elapsed length exceeds Phase 3 in every year 2015–2023 [E-5011 하]; regulatory review is 11.0–12.5% of elapsed time [E-1095 중].

**C (cost): always tag the basis, because the tag moves the number more than the biology does.** One model returns 172.7 out-of-pocket, 515.8 risk-adjusted and 879.3 capitalized USD million for the same drug [E-1011 중]. About 32% of any headline capitalized figure is the analyst's discount-rate choice [E-9041 중]. Measured industry cash goes 15.9% pre-human against 28.8% to Phase III alone [E-1042 중], and the only directly observed preclinical share from company filings is 12.4% median [E-1007 중].

**Where the constraint is not.** Regulatory review capacity: 96% of 2025 CDER approvals met their PDUFA goal date through a 17.8% workforce cut [E-4020 중] [E-4019 하], the pending pile is inside goal dates [E-4021 중], and Japan has the world's fastest review at a 290-day median alongside 86 US/EU-approved drugs nobody filed there [E-4075 중] [E-4077 중]. Screening throughput: the largest public foundry is cutting footprint by up to 60% against a 48% revenue decline [E-7036 중]. Data volume: pooling a corpus ~123× the public one returned about 4% relative improvement [E-7010 중] [E-7101 중]. The raw patient pool: 55.6% of cancer patients have no trial available locally [E-5032 상] — but that figure measures the constraint rather than slack, because cheap exhaustive screening of 98,348 charts produced 117 enrolments [E-5047 중].

### Q3 — Where does the constraint move if discovery is heavily compressed?

**It does not move to "preclinical/clinical" as a block. It splits.** A probability tier — target validation, toxicity, development design, translation — is not relieved at all by making discovery faster [E-9031 하]. A capacity tier shifts in a specific order: IND-enabling non-human-primate toxicology first, where up to two-thirds of primate requests have been unfillable since 2021 [E-3050 하]; then shared manufacturing inputs [E-6064 하]; then matched clinical site capacity, which is the terminal bind because it is the one resource whose measured growth rate is negative at −0.92% a year [E-5063 중].

⚠ **LOW-EVIDENCE CLAIM.** The model that produces this ordering returns exactly zero additional approvals from an 80% cut in discovery duration [E-9031 하] and exactly zero from a fivefold candidate inflow at fixed budget [E-9033 하]. Both grade 하 because both follow from a budget identity the model's own assumptions do not support [E-9042 하]. The *directional* claim survives independently; the exact zero does not, and it must not borrow credibility from the Amdahl bound below.

**The bound that does hold, and it is the best-triangulated result in the run.** Three agents, three datasets, three methods: setting discovery time to zero removes at most **21–41%** [E-1094 중], **23–37%** [E-3098 하] and **33.3%** [E-9039 하] of total elapsed development time, and at most 40–43% of capitalized cost [E-1094 중] but only 7–31% of actual cash [E-1094 중]. This is a bound on **elapsed time**. It is not a statement about output.

**One open conflict cuts against this run's own story and is not hidden.** ⚠ On manufacturing, the slack side is better evidenced than the scarcity side: supply projected to outpace demand through 2031 grades 중 [E-3036 중] while the contraction and lead-time evidence grades 하 throughout [E-6005 하] [E-6006 하] [E-6008 하]. The best-evidenced record in the area says manufacturing **delays** approvals rather than preventing them [E-6074 중]. The saturation ordering that puts plasmid DNA first at 1.06× is not adopted here: it rests on an invented lead-time-to-utilisation rule with no cited empirical basis [E-6070 하].

### Q4 — Ranked rate-limiting steps with probabilities for 2030 / 2035 / 2040

[INFER] The probabilities below are this report's judgement, not measurements: no published elasticity of annual approvals to any pipeline factor exists [E-3080 중]. They are conditioned on an explicitly stated AI-share trajectory, because the low-share ceiling is a 2026 snapshot and not a bound — at an observed doubling time of 1.2–2.1 years the AI share of new clinical molecules crosses 10% between about 2029 and 2033 and 50% between about 2032 and 2039 [E-9517 하] [E-9518 하].

| Horizon | AI share assumed | Top three, with P(top constraint) |
|---|---|---|
| 2030 | 4–12%, central 7% | B1 target validation 0.30 · B17 development design 0.15 · B8 toxicity 0.14 |
| 2035 | 15–50%, central 28% | B3 matched site capacity 0.24 · B1 target validation 0.20 · B8 toxicity 0.12 |
| 2040 | 35–90%, central 60% | B3 pivotal multiregional trial capacity 0.26 · B1 target validation 0.17 · B7 delivery 0.12 |

The full nine-deep rankings with per-item bases and grades are in §5 of the main report. [INFER] The single most consequential judgement embedded in them is that share growth changes *which* bottleneck binds without changing output, because at unchanged probability of success a 50% AI share produces zero additional approvals [E-2058 하].

### Q5 — What breaks each bottleneck? TRL, developer, timing, remaining hard problems

From a 93-technology catalogue [E-8130 하]. Only 30 of 93 milestones resolve by 2029 and 64 by 2030, so two thirds of the roadmap cannot be scored before the first horizon the question asks about [E-8130 하].

| Rank | Technology | Bottleneck | TRL | Developers | Window | Remaining hard problem |
|---|---|---|---|---|---|---|
| 1 | Human-genetics-anchored target selection | B1 | 8 | Open Targets; Regeneron Genetics Center; deCODE | 2015–2026 | Only a minority of targets carry a tractable signal; MR significance alone does not enrich for Phase II success |
| 2 | Regulatory dose-optimisation instrument | B17 | 8 | FDA Oncology Center of Excellence | 2024–2030 | Randomised dose comparison is powered for response rate, not survival |
| 3 | Model-informed drug development | B17 | 8 | FDA CDER/CBER pharmacometrics; ICH M15 | 2018–2029 | Extrapolating beyond studied doses relies on an unverifiable functional form |
| 4 | ML immunogenicity prediction | B8 | 6 | EpiVax; Lonza; Abzena | 2020–2027 | Clinical immunogenicity depends on formulation, route and HLA as much as sequence |
| 5 | Estimand framework, ICH E9(R1) | B17 | 8 | ICH working group; FDA and EMA | 2019–2027 | Boilerplate compliance is the likeliest outcome and is not externally visible |

[INFER] **Six of the top ten are regulatory or methodological rules rather than laboratory tools, and the top three are all rules** [E-8130 하]. Three of those TRL-8 ratings rest on instruments that recommend rather than require and should be described as "final instrument issued", never as "mandate" [E-8108 중] [E-8112 중] [E-8116 중].

**Three bottlenecks have no credible technological solution, in corrected narrowed form.** *B1 target validation*: cis-pQTL Mendelian randomisation is a causal human instrument that does not require a trial and has industrialised [E-8124 중], but MR significance alone did not enrich for Phase II success across 11,482 target–indication pairs, so the objection is empirical rather than conceptual [E-8009 중]. *B13 talent*: no candidate found; investigators fell ~9% and coordinators ~28% over six years through heavy trial-technology investment [E-9524 하]. *B11 capital and reimbursement*: the "no laboratory technology" narrowing does no work, because a payment model is not a lab technology by definition. The claim the ledger supports is that **non-laboratory payment instruments operate at national scale in at least two jurisdictions** — the NHS antimicrobial subscription at roughly GBP 100m/yr with contracts from 1 April 2026 [E-8126 상], and the CMS Cell and Gene Therapy Access Model covering 84% of Medicaid sickle-cell beneficiaries across 32 states plus DC and Puerto Rico [E-8061 중] — that **no evidence shows either changed system output**, and that the constraint is therefore an unsolved allocation problem with demonstrated mechanism prototypes [E-8126 상].

---

## H0 verdict

**Partially supported, for reasons that damage rather than vindicate it.** Its historical half is **rejected for the aggregate pipeline on per-programme economics** — about 65% of lifetime attrition occurs after entry into humans [E-1097 중], pre-human work is 15.9% of measured industry cash [E-1042 중], and the genomics and target-based screening expansion produced 17 of 50 first-in-class small molecules 1999–2008 against 28 from phenotypic screening [E-9505 중]. **Three qualifications are binding.** Per-programme statistics are structurally blind to programmes never started, and about 85% of the druggable genome has never yielded an approved drug [E-9536 중] — the strongest surviving case for H0-a, and one this report cannot dispose of. Stage of observation is not stage of cause: a Phase II efficacy failure is frequently caused at target selection [E-9507 중]. And the rejection is domain-conditional, with antibacterials 1962–2000 and RAS 1982–2021 as documented counter-domains [E-9503 중] [E-9502 중]. **Its forward half is a restatement of a forty-year status quo and is not falsifiable as posed**; restated as a rate claim it is currently supported, since cumulative likelihood of approval fell from 10.4% to 6.7% across successive analyses 2014–2024 while termination rates fell [E-9512 하] [E-9514 하].

## Three things this run found that a reader should not lose

**The most-quoted anchors are not faithful as commonly repeated.** The 10–15 year development-duration anchor corresponds to no measurement anywhere in 774 records; the measured clocks are 128 months, 147 months and 9.1 years of clinical development [E-1005 중] [E-1014 중] [E-3004 중]. The cost anchor's sample is a confidential survey of 106 compounds from 10 unnamed firms and cannot be reproduced [E-1001 하]. The success-rate anchor spans four incompatible denominators, so no point estimate is admissible [E-1020 중] [E-1023 중]. The AI Phase I anchor had an undisclosed denominator at origin and is BCG-authored and BCG-funded [E-2001 하].

**One widely repeated claim about animal-model non-predictivity is removed entirely rather than qualified**, and it does not appear in either deliverable in any form. Its denominator is misapplied at source: the headline percentage is a share of the compounds that clear preclinical, not of all compounds [E-9554 중].

**The levers that raise output make the system slower, and the levers that make it faster do not raise output.** Raising Phase II probability of success 50% is the largest single modelled lever at +31.8% approvals and lengthens mean cycle time from 13.50 to 15.03 years [E-9032 하]; cutting enrolment duration 40% and CMC lead time 50% add exactly nothing [E-9036 하]. ⚠ LOW-EVIDENCE CLAIM on both figures. [INFER] Anyone optimising a portfolio for cycle time is, on this evidence, optimising against output.
