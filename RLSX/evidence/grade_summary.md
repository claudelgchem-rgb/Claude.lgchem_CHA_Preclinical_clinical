CHARTER_ACK: R1,R2,R3,R4

# Independent Reliability Grading — Agent R

Every record in the merged ledger has been graded: **750 of 750**, no gaps, no deferrals.
Grades were assigned solely by Agent R. No collector graded its own evidence.

---

## 1. Grade distribution

### Overall

| 상 (High) | 중 (Medium) | 하 (Low) | Total |
|---|---|---|---|
| 5 (0.7%) | 430 (57.3%) | 315 (42.0%) | 750 |

Only five records in the entire ledger meet the R3 test for 상 — a primary source, **plus**
two or more genuinely independent cross-confirmations, **plus** methodology disclosed well
enough to reproduce. That is the expected shape. Genuine triple-qualification is rare.

### Per collecting agent

| Agent | 상 | 중 | 하 | n | share 하 |
|---|---|---|---|---|---|
| A (economics of development) | 1 | 49 | 14 | 64 | 22% |
| B (AI track record) | 0 | 27 | 47 | 74 | 64% |
| C (bottleneck matrix) | 0 | 55 | 67 | 122 | 55% |
| D (flow model) | 0 | 9 | 20 | 29 | 69% |
| E (regulatory landscape) | 1 | 70 | 14 | 85 | 16% |
| F (trial operations) | 1 | 52 | 16 | 69 | 23% |
| G (CMC and delivery) | 1 | 31 | 40 | 72 | 56% |
| H (data and DBTL) | 1 | 45 | 28 | 74 | 38% |
| I (breakthrough catalogue) | 0 | 61 | 45 | 106 | 42% |
| X (red team) | 0 | 31 | 24 | 55 | 44% |
| **All** | **5** | **430** | **315** | **750** | **42%** |

The spread is not noise. E and A worked domains with public primary records (statutes,
Federal Register notices, FDA tables, peer-reviewed cost studies) and their evidence holds up.
B, C, G and D worked domains where the available evidence is company self-report, paid market
research, or the agent's own model — and the grades reflect that, not the agents' effort.
D scores lowest because its own assumptions file marks fifteen load-bearing choices
`[ASSUMPTION-UNSUPPORTED]`; that transparency is a credit to D and a constraint on its outputs.

### By record type

| Type | 상 | 중 | 하 |
|---|---|---|---|
| primary_literature | 3 | 208 | 14 |
| regulatory | 2 | 88 | 12 |
| registry | 0 | 7 | 9 |
| filing | 0 | 6 | 7 |
| derived | 0 | 66 | 68 |
| secondary | 0 | 50 | 183 |
| market_report | 0 | 5 | 22 |

Every market report but five is Low. That is the S2 rule applied without exception:
a paid figure with undisclosed methodology does not become reliable by being repeated.

### The five 상 records

| ID | Claim | Why it clears the bar |
|---|---|---|
| E-1006 | Wouters 2020: median $985.3M capitalized R&D per approved agent, 63 agents / 47 companies | Public SEC filings, nameable sample, reproduced exactly on re-access, magnitude independently corroborated by Prasad 2017 and Sertkaya 2024 |
| E-4004 | FDA qualified its first AI drug development tool (AIM-NASH) on 8 Dec 2025 | Regulatory act of record, confirmed by four independent outlets and the sponsor; also settles a cross-agent conflict |
| E-5032 | Unger 2019 meta-analysis: 55.6% no trial available / 21.5% ineligible / 14.8% eligible non-enrollers / 8.1% enrolled | Pools 13 independent studies (the cross-confirmation is internal to the design), published method, every pooled estimate and interval reproduced exactly |
| E-6041 | AVLAYAH (tividenofusp alfa) accelerated approval 25 Mar 2026, first receptor-mediated brain-delivery biologic | Regulatory act of record, four independent confirmations, label and confirmatory condition public |
| E-7018 | Reproducibility Project: Cancer Biology — median replication effect 85% smaller, 92% of effects smaller | Preregistered multi-laboratory programme, public protocols and data, reproduced exactly, corroborated in direction by two independent industry programmes |

---

## 2. Downgrade reason code histogram

| Code | Meaning | Count |
|---|---|---|
| S1 | single source | 466 |
| S2 | methodology undisclosed | 225 |
| S7 | origin unverifiable | 176 |
| S4 | conflict of interest | 122 |
| S3 | circular reference | 121 |
| S5 | sample bias | 43 |
| S6 | outdated | 16 |

`S7` at 176 is the single most damning number in this table. It means that for nearly a
quarter of the ledger neither the collector, nor Agent X's three-hop audit, nor my own
re-access could reach the place a figure came from.

`S4` at 122 reflects how much of the AI-in-drug-discovery and manufacturing evidence base
consists of companies reporting on their own platforms.

---

## 3. Re-access rate

| Method | Count | Share |
|---|---|---|
| `refetched` — source re-opened and claim checked against it | 76 | 10% |
| `refetch_failed` — access attempted, blocked (paywall, 401/403/404, auth redirect) | 51 | 7% |
| `metadata_only` — graded conservatively on publisher class, source type, disclosed methodology and corroboration inside the ledger | 623 | 83% |

I attempted re-access on **127 records (17%)** across roughly sixty WebFetch and WebSearch
calls, and prioritised exactly as instructed: every anchor figure, every headline quantitative
result, every `circular_risk:true` record I could reach, and every `market_report`.
Where a PDF defeated the fetch tool I decompressed its content streams and read the text
directly — that is how the CIRS regulatory-timing tables, the BIO 2011-2020 success-rate
tables, the Ringel Eroom's-Law analysis and FDA's 2025 IND activity table were verified.

I never recorded a record as re-accessed that I did not open.

---

## 4. Reconciliation with the provenance audit (Agent X)

Agent X marked **232 records FORCE_LOW**. Of the 232:

- **207 graded 하**, with S3 where circularity is demonstrated and S7 where no origin was reached.
- **25 overridden with a traced provenance chain**, recorded in `corrected_provenance_hops`.
  In each case I reached an origin the audit did not.

The 25 overrides, and what I reached:

| Records | Origin I reached that the audit did not |
|---|---|
| E-1032, E-1033, E-1034, E-4061, E-4062, E-4076 | Decompressed the CIRS R&D Briefing 101 PDF content streams and read the 2024 approval-time and expedited-pathway tables verbatim |
| E-1038, E-1039 | OWID parent page confirms the series is FDA's own CDER NME compilation plus the CBER Purple Book |
| E-1041, E-1042 | PhRMA survey located at its live URL; the ~16% pre-human share corroborated independently |
| E-1010 | Light & Warburton $59.4M (incl. ~$16M capital; $43.4M without) confirmed at the BioSocieties article and in two independent restatements |
| E-1049 | Traced to the NRDD data article restating NMPA registry counts, with a second independent restatement |
| E-1051, E-4080 | MFDS 420→295-day target traced to the agency announcement via three independent trade sources |
| E-1052 | Chain traced: ASPE 2014 → Sertkaya et al. 2016 (Clinical Trials) → Medidata proprietary cost database |
| E-1053 | Corrected the dead URL and confirmed the 2024 CGT approval count independently |
| E-2003, E-2004 | Traced to the Jayatunga (Drug Discovery Today, June 2024) paper and BCG's 73-molecule tracking base |
| E-2022 | Adaptyv Bio **is** the origin — it performed the replication; report re-opened and figures reproduced |
| E-2053 | Zero AI-discovered FDA approvals confirmed independently across multiple 2026 sources |
| E-3008 | Confirmed the Jayatunga Phase I denominator is disclosed: 21 of 24 |
| E-3020, E-3021 | Traced to Getz 2012 (Applied Clinical Trials, 151 trials, 2008-2010) and the Tufts CSDD 2024 "Day of Delay" white paper (447 protocols) |
| E-3036 | Corrected the dead BioProcess International URL; article title confirms the capacity-outpaces-demand finding |
| E-8072 | The OSTP nucleic-acid screening framework is a primary US government document on an official domain |

I did **not** override E-1001/E-1002 (DiMasi). My re-access reached the same place the audit
did — the published abstract — and no further. The 106-compound sample is a confidential
survey of unnamed firms about unnamed compounds and cannot be re-derived by anyone. The audit
is right and the anchor is Low.

Circular-risk flags after grading: **128 stand** (against 114 set by collectors). I cleared
25 and set additional flags where my own re-access found untraced circulation the collectors
had not flagged.

---

## 5. Records most load-bearing for the run's conclusions, and their grades

This is the section to read before trusting any headline number.

### Q1 — has AI compressed discovery, empirically?

| Record | Claim | Grade |
|---|---|---|
| E-3008 | Jayatunga: 21 of 24 AI molecules cleared Phase I (denominator IS disclosed) | 중 (S4, S5) |
| E-2002 | Same paper: Phase I 80-90% vs stated 50-65% historical | 중 (S4, S5) |
| E-2003 | Same paper: Phase II ~40%, matching historical | 중 (S4, S5) |
| E-2066 | Wilson 95% CI at n=24 is [0.661, 0.943] — overlaps conventional rates | 중 (S4, S5) |
| E-2065 | Detecting the 3-point Phase II difference needs ~4,126 per arm | 하 (S1, S3) |
| E-2054 / E-2055 | 117 AI assets, 63 companies, median 6.5 years founding-to-Phase-1 | **하** (S1, S3, S7) |
| E-2053 | Zero AI-discovered drugs FDA-approved as of 2026 | 중 (S1) |
| E-7100 | Label-noise ceiling: max achievable R² on public pIC50 is 0.54-0.88 | 중 (S1) |
| E-7018 | Preclinical replication: median effect 85% smaller | **상** |

The verdict-bearing facts here are solid; the **census** figures are not.

### Q2 / H0-c — Amdahl ceiling on discovery compression

| Record | Claim | Grade |
|---|---|---|
| E-1093 | Pre-IND is 21.2-40.7% of elapsed development time | 중 (S2, S6) |
| E-1094 | Ceiling: ≤21-41% of time, ≤40-43% capitalized cost, only 7-31% of cash cost | 중 (S2, S6) |
| E-3098 | Independent computation: 23-37% of elapsed time | 하 (S2, S3) |
| E-9039 | Third independent computation: 33.3% of time, 41.0% of capitalized cost | 하 (S2) |
| E-5071 | Clinical-side ceiling: perfect recruitment removes 25-61% of clinical elapsed time | 중 (S1) |

**Three agents computed the discovery time ceiling independently, on different datasets, and
got 21-41%, 23-37% and 33.3%.** That agreement is real triangulation and I verified all three
arithmetically. It is the best-supported quantitative conclusion in the run, even though two
of the three individual records are Low because of their inputs.

### Q2 — cost and probability anchors

| Record | Claim | Grade |
|---|---|---|
| E-1001 / E-1002 | DiMasi 2016: $2,558M capitalized / $1,395M out-of-pocket | **하** (S2, S7) |
| E-1006 | Wouters 2020: $985.3M median, from public filings | **상** |
| E-1011 | Sertkaya 2024: $879.3M expected capitalized at 11% CoC | 중 (S2) |
| E-9041 | ~32% of the headline cost figure is the discount-rate choice alone | 중 (S2) |
| E-1023 | BIO 2011-2020: 7.9% Phase I LOA, n=12,728 transitions | 중 (S2) |
| E-1020 | Wong 2019: 13.8% Phase I to approval, 406,038 trial entries | 중 (S2) |
| E-1027 | Zhou 2025 Nature Comms: ~5-6.5% for 2015-2023, public databases | 중 (S2) |
| E-1026 | Citeline 6.7% (2014-2023) | **하** (S1, S2, S3) |
| E-1096 | Cumulative PoS recomputed from BIO transitions, reproduces 7.9% exactly | 중 (S2) |

### Q2 — patient throughput and trial operations

| Record | Claim | Grade |
|---|---|---|
| E-5032 | Unger: 55.6% of cancer patients have no trial locally; only 14.8% are eligible non-enrollers | **상** |
| E-5006 | Industry Phase III participants fell 1,245,175 → 1,156,515 across 2008-2019 | 중 (S1) |
| E-5003 | Participants per site per month 0.6 → 0.8 → 0.4 | 중 (S1) |
| E-5001 | Median recruitment 13 → 18 months | 중 (S1) |
| E-5069 | 2× IND flow needs ~289,000 more Phase III participants, ~60,000 site-slots | 중 (S1, S2) |
| E-5026 | Tufts 2023 cycle: enrolments **exceeded** plan, timelines shorter | 중 (S2) |

### Q3 — where the constraint moves

| Record | Claim | Grade |
|---|---|---|
| E-9031 | Discovery duration −80% → **zero** change in annual approvals | **하** (S2) |
| E-9033 | 5× candidate inflow at fixed budget → **zero** change | **하** (S2) |
| E-9032 | Phase II PoS +50% → +31.8% approvals (largest single lever) | **하** (S2) |
| E-9034 | 5× inflow with capital freed → +26.8%, NHP toxicology binds | **하** (S2) |
| E-9042 | Constraint migration: budget → NHP tox → vectors → Phase III slots; review never binds | **하** (S2) |
| E-6070 | Manufacturing saturation ordering: plasmid/lentiviral first at ~1.06× | **하** (S2, S7) |
| E-3125 | Final parent bottleneck ranking, 18 rows | **하** (S2) |

### Q5 / regulatory

| Record | Claim | Grade |
|---|---|---|
| E-4004 | First AI drug development tool qualified, 8 Dec 2025 | **상** |
| E-4025 | CDER 15,124 active INDs at 31 Dec 2025 (9,932 commercial) | 중 (S1) |
| E-4056 | Approvals fell 8% while CDER headcount fell 17.8% | 중 (S1) |
| E-9545 | FDA has formally qualified **eight** biomarkers, seven of them pre-2016 | 중 (S1) |
| E-6041 | First receptor-mediated brain-delivery biologic approved | **상** |
| E-6074 | Manufacturing CRLs delay approval but do not prevent it (survivorship-selected cohort) | 중 (S1) |

---

## 6. Conflicts between agents, and how each side graded

Peer agents contradicted one another in eleven places. I graded both sides on their merits.
Five conflicts are now **resolved by evidence**; six remain **open** and the report must say so.

### Resolved

**(a) AI Phase I denominator.** B (E-2002) recorded that "the accessible sources do not
disclose the Phase I denominator". C (E-3008) recorded that the denominator is 21 of 24.
I re-accessed and **C is right**. I withdrew the S2 code I had provisionally placed on
E-2002 and regraded it 중. *B 중 / C 중 — conflict closed in C's favour.*

**(b) ISTAND and NAM qualification.** C (E-3015, via an AI-content aggregator) recorded
16 ISTAND projects and **zero** qualified drug development tools as of 1 Jan 2026.
E (E-4003/E-4004) recorded 8 accepted submissions and **one** qualified AI tool from
8 Dec 2025. I confirmed the AIM-NASH qualification through four independent outlets.
*C 하 / E 중 and 상 — conflict closed in E's favour. C's zero-qualified claim is wrong.*

**(c) Biomarker qualification count.** C (E-3072) recorded 11 qualified biomarkers and
E-3103 explicitly reaffirmed it as "not contradicted". X (E-9545) recorded eight.
I re-accessed the paper both cite: it says **eight**, seven of them pre-2016.
*C 하 / X 중 — closed in X's favour. C's later E-3123 accepts the correction.*

**(d) Patient-pool slack.** C's original B3 elasticity (E-3083, 2.5%) treated low
participation as evidence of usable slack. F's records (E-5003, E-5006, E-5069) treat the
same figures as evidence of matched-capacity scarcity. C conceded in E-3099 after applying
the right test: F's deployed AI prescreening natural experiment collapsed screening *cost*
tenfold and converted 117 patients from 98,348 charts. *C's original 하 / F 중 / C's
concession 중 — closed in F's favour.*

**(e) Genetic-support multiplier.** I (E-8010) carried the recycled "≈2×". C (E-3100) and
X (E-9507) carry Minikel 2024's 2.6× with therapy-area detail. *I 하 / C and X 중 —
use 2.6×, not 2×.*

### Open — the report must address these, not pick a side

**(f) Manufacturing capacity: slack or scarcity?** C's E-3036 (viral vector supply outpaces
demand through 2031, 중) and D's E-9030 (no physical resource above 0.90 utilisation at
baseline, 하) say slack. G's E-6005/E-6006/E-6008/E-6019 (하 throughout) and C's E-3037 (하)
say contraction and lead-time scarcity, and G's ordering E-6070 (하) puts plasmid DNA at
1.06× from binding. **The slack side is better evidenced than the scarcity side**, which is
uncomfortable for the run's constraint-migration story. The single best-evidenced record in
the area, E-6074 (중), points a third way: manufacturing problems delay approvals rather than
prevent them.

**(g) CAR-T manufacturing failure rate.** E-3034 gives 25% in NHL (중, and the source
discloses no denominator). E-6012 gives 3.87% from a UK national cohort of 981 patients (중).
E-6011 gives a 4-7% pooled range (중). A sixfold spread, all Medium. The national-registry
figure is the only one with a stated numerator and denominator.

**(h) AI clinical-molecule counts.** 29 (E-9007, 중), 75 (E-2072, 하), 117 (E-2054, 하),
~175 (unrecorded search hit). No record reconciles the inclusion rules. Any statement of
"how many AI drugs are in the clinic" must name its counting rule.

**(i) Novel target entry rate.** X's own block contains both E-9509 (falling from ~100/yr to
~30/yr, 하, consultancy) and E-9510 (rising significantly, p<0.001, 중, peer-reviewed).
Prefer E-9510.

**(j) Enrolment performance direction.** F's own E-5001/E-5003 (중, recruitment lengthening,
site productivity halving, 2008-2019) versus F's own E-5026 (중, Tufts 2023 cycle: actual
enrolments exceeded plan, timelines shorter than expected). Unresolved inside F's block.

**(k) Cost per approval, model versus measurement.** D's model returns 2,791 capitalized;
Sertkaya (E-1011, 중) returns 879.3. D reports the +217% gap as **not reconcilable** and
declines to average. That is the right call and the report should repeat it rather than
splitting the difference.

---

## 7. ⚠ Claims that cannot bear the weight placed on them

Each of the following is a conclusion the run is positioned to draw that rests on **하**-grade
evidence. Every one requires the `⚠ LOW-EVIDENCE CLAIM` banner, or restatement as a
directional judgment rather than a quantity.

**1. ⚠ "Compressing discovery to zero changes annual approvals by exactly zero."**
E-9031, E-9033 — 하. The zero is a direct consequence of D's budget identity (capital
utilisation fixed at 1.00 by construction), which D's own assumptions file does not support
with evidence. *The directional claim survives* — it is independently corroborated by the
three Amdahl computations in §5 — *the exact zero does not.*

**2. ⚠ The manufacturing saturation ordering (plasmid DNA and lentiviral vector bind first
at ~1.06× current IND volume).** E-6070, E-6064, E-6062, E-6066, E-6069, E-3117 — all 하.
Nine of the ten component multiples are Low, and all ten are generated by a single invented
lead-time-to-utilisation mapping with no cited empirical basis. The rank order may be roughly
right; the multiples must never be quoted as measurements.

**3. ⚠ Capital as the top-ranked bottleneck (B11 elasticity 6.0, later revised to 0.8).**
E-3091 — 하, and **all six** of its evidence inputs are Low with circular flags standing.
The revision E-3116 is also 하. The near-linear capital argument may well be correct; as
evidenced it is an assertion.

**4. ⚠ The final eighteen-row bottleneck ranking.** E-3125 — 하. Of its component
elasticities, only B8 (E-3088, 중) and the B10 quality split (E-3119, 중) rest on Medium
evidence. B13 (E-3093), B14 (E-3094), B16 (E-3096), B3 (E-3083), B5 (E-3120), B6 (E-3117),
B9 (E-3118), B12-adjacent and B17 (E-3111/E-3122) are all 하. Report the ordering as a
reasoned ranking, never as measured elasticities.

**5. ⚠ "117 AI-enabled assets across 63 companies, median 6.5 years from founding to Phase 1."**
E-2054, E-2055 — 하. The named origin (an ASCO 2026 / JCO abstract) could not be located, and
the only corroborating hits are other AI-generated aggregator pages — the signature of
circulation, not confirmation. Derived quantities E-2057 and E-2058 inherit this.

**6. ⚠ "Preclinical/animal-model non-predictivity: 90-95% of drugs passing animal tests fail
in humans."** E-3019 — 하, and X's E-9554 (중, which I verified at source) shows the
denominator is misapplied: the 90% is 90% of the ~60% that clear preclinical. This claim
should be **removed**, not banner-tagged.

**7. ⚠ Protocol-complexity and operational-burden figures** (procedures per Phase III protocol
187→301; 5.96 million data points; 3.5 amendments; enrolment interval +36.9%). E-3075, E-3076,
E-3077, E-3078 — all 하 with circular flags standing, several from vendors selling the remedy.
The B16 elasticity built on them (E-3096) is 하.

**8. ⚠ Talent scarcity and biosecurity as bottlenecks.** E-3066, E-3067, E-3068, E-3069,
E-3070, E-8069, E-8071 — all 하. Both conclusions (labour is in aggregate surplus; no binding
access regime exists) are plausible and I suspect correct, but they rest entirely on
untraceable recruiter and aggregator figures.

**9. ⚠ Venture-capital and capital-availability figures** (seed/Series A 228→191 rounds,
$10.6bn→$8.7bn; Q1 2025 $6.5bn −20.2%; >50% of public biotechs under two years' runway;
post-IRA −68% small-molecule investment; $1.3tn top-25 deployable capital). E-3057, E-3058,
E-3059, E-3061, E-9526 — all 하. The one Medium record in this area is E-9525 (peer-reviewed
econometric estimate of the IRA step change), which should displace the industry-commissioned
E-3059 wherever the two disagree.

**10. ⚠ Cell-therapy cost of goods ($95,780/dose).** E-1046, E-3035, E-6015 — one 2019 model
appearing three times from three publications. Two of the three are 하. Its appearance in
three independent-looking records is repetition, not corroboration.

**11. ⚠ China trial-share and out-licensing figures** (39% of global oncology trial starts;
38% of innovative-drug approvals; $136bn out-licensing). E-9520, E-9521, E-9522 — all 하,
from one think-tank compilation of unnamed commercial databases plus a deal tracker whose
totals are dominated by contingent milestones.

**12. ⚠ Insilico's 18-month / $2.6M discovery timeline.** E-2030, E-2031, E-7058, E-9534 —
four records, four URLs, one company, no matched control cohort. All 하 except E-2008 (중),
which is a review restating the same company figures.

### Figures I found to be wrong on re-access — correct before publication

| Record | Recorded | Source actually says |
|---|---|---|
| E-3072, E-3103 | 11 biomarkers qualified | **8** (7 of them pre-2016) |
| E-9501 | dark proteome 38% of proteins | **~31% Tdark** |
| E-1024 | siRNA/RNAi n=70 | **n=87** |
| E-7062 | 33-fold increase in screening burden | **~53-fold** (739/14) |
| E-1027 | Phase 3 58%, overall 5.5% (2015-2023) | **~52% and ~6.5%** on re-access |
| E-7102 | 16-27% annual gene-synthesis price decline | its own derivation computes **14.8-23.8%** |
| E-4039 | 26 ATMPs analysed | **27** |
| E-8061 | 33 states + DC + PR | **32 states** + DC + PR at the 84% figure |
| E-5065 | site productivity halved | halved from the 2012-2015 **peak**; −33% from 2008-2011 |
| E-2075 | 35% of 200 antiviral compounds active | did not reproduce; only the 22.5% (45/200) figure did |
| E-9554 | attributes the 90% claim to a 2006 HHS statement | attribution did not reproduce; the denominator correction did |
| E-6067 | 8× oligonucleotide saturation multiple | does not follow from the record's own stated formula |

---

## 8. Bottom line for a reader deciding how much to trust the report

- The **descriptive economics of drug development** (stage costs, durations, phase transition
  probabilities, approval counts, regulatory timelines) is Medium-grade and mutually
  consistent across four independent lineages. Trust it, with the caveat that the most-quoted
  anchor of all — DiMasi's $2.6bn — is Low because its sample is confidential and
  irreproducible, and that roughly a third of any capitalized cost figure is the analyst's
  discount-rate choice (E-9041).
- The **Amdahl ceiling on discovery compression** is the run's best-triangulated finding:
  three agents, three datasets, 21-41% / 23-37% / 33.3% of elapsed development time.
- The **empirical case on AI's clinical track record** is Medium where it is deflationary
  (no approvals, Phase II unchanged, n=24 confidence interval overlaps) and Low where it is
  inflationary (census counts, company timelines, platform performance claims). That asymmetry
  is a property of the evidence, not of my grading: deflationary findings came from
  peer-reviewed literature and registries, inflationary ones from companies and aggregators.
- The **quantitative constraint model and the bottleneck ranking are Low**. They are careful,
  internally consistent and honestly caveated, but they are analyst constructions resting on
  parameters that no cited source supplies. They should be presented as a structured argument
  about mechanism, never as measurements of elasticity.
