CHARTER_ACK: R1,R2,R3,R4

# Agent D — Constraint modelling and counterfactual simulation

Deliverables: `RLSX/model/constraint_model.py` (runs end to end, standard library only, seed
20260818), `RLSX/data/scenario_results.csv` (10 rows), `RLSX/data/tornado_sensitivity.csv`
(26 rows), `RLSX/model/model_assumptions.md`, `RLSX/evidence/parts/D.jsonl` (29 records,
E-9001–E-9042), this report, `RLSX/work/D/unresolved.csv` (7 records).

Evidence grading is not performed here. Every record carries `confidence: null`,
`graded_by: null`, `grade_reason: []` for Agent R (R3).

---

## 1. Model structure, stated up front

A steady-state, capacity-constrained flow model of the pipeline, run per modality, with sixteen
finite shared resources and queueing.

**Eight stages** S1–S8, each with a transition probability, a cycle time and an out-of-pocket
cost per work-in-process unit, all taken from a single internally consistent published stage
model recovered in full during this work [E-9001]. Agent A independently recorded that source's
probabilities and first four cycle times [E-1017][E-1018] and its two totals [E-1019]; the
cost-per-WIP column is new here and exists in no other source Agent A or I recovered.

**Attrition is the spine.** No cost in this model is a multiplier on duration. Every stage cost
is `(1 / cumulative PoS from that stage) × cost per WIP`, so a change in any downstream
probability re-prices every upstream stage [E-9001]. A scenario that shortens timelines without
touching attrition therefore cannot show large gains — by the arithmetic, not by assumption. The
assignment stipulated that a model failing this test is wrong; §5 shows the model passes it, and
S1 returns exactly zero.

**Ten modalities** weighted by BIO 2011–2020 Phase I programme counts, each with its own
clinical probability of success from the same source [E-1024][E-9021].

**Sixteen resources with queues**: ten GMP sub-capacities, IND-enabling non-human-primate
toxicology, Phase I/II clinical capacity, Phase III patient slots, the 30-day IND gate, NDA/BLA
review, and the industry R&D budget. Baseline utilisations come from Agent G's measured or
proxied figures; the Phase III patient capacity is Agent F's measured 289,129 industry
participants per year [E-5064]. Demand above capacity is not served — throughput is capped and
the excess is lost. Each resource throttles exactly one stage, so rationing is never compounded.
Queue delay uses a coefficient of 0.11 years derived from three published pairs of utilisation
and observed lead time, not chosen [E-9020].

**Three cost bases, never mixed** (M1): out-of-pocket for one successful programme; risk-adjusted
with failures loaded; capitalized with each stage's spend compounded forward from its own midpoint
to launch. **Base discount rate 11.0 %/yr** [E-9001]. Cross-checked against the January 2026
sector cost of capital of 7.85 % pharmaceutical and 8.49 % biotechnology [E-9002], and against
DiMasi's 10.5 % [E-1001], Sertkaya's 11 % [E-1011] and Prasad's 7 % [E-1009]. All five are run
and reported: the choice of rate alone moves the headline by 32 % [E-9041].

### Limitations, stated before the results

Full list in `RLSX/model/model_assumptions.md` §10. The four that bound the results hardest:

1. **It is a steady state.** It cannot represent the 3–5 year transient in which a capacity
   shortfall is real and is then absorbed — which is precisely Agent G's central caveat. S6b and
   S7 are two static answers to what is really a dynamic question.
2. **Delivery (B7) is structurally invisible to it.** Agent C's finding that delivery failure
   deletes whole indication classes before a programme is ever started [E-3042][E-3044] cannot
   appear in a model whose only failure channel is attrition among programmes that exist. This
   biases every result toward understating the constraint.
3. **Capital is exogenous.** There is no feedback from returns onto budget, even though ex-incretin
   R&D returns of 2.9 % and falling [E-3007] and commercial withdrawal of technically successful
   products [E-3060] both point to the budget contracting. Every scenario is therefore more
   optimistic than it should be.
4. **Utilisations are largely proxies.** Agent G was explicit that most manufacturing sub-areas
   publish a lead time and not a utilisation. That crudeness propagates directly here, which is
   why the tornado sweeps every capacity parameter.

---

## 2. S0 calibration check, and its discrepancies reported honestly

**S0 approvals are pinned at 50 by construction** — candidate inflow is calibrated so the
unconstrained steady state hits the observed 50 US novel approvals of CY2024 [E-1038]. "The
model reproduces 50 approvals" is therefore *not* a test and is not offered as one. Three things
that are tests:

**(a) Engine reproduction — passes.** On the un-decomposed single path, the model returns
out-of-pocket 263.5 (published 263.5, error 0.00 %), risk-adjusted 873.0 (published 873, error
0.00 %), capitalized 1,778.4 (published 1,778, error +0.02 %), cycle time 13.50 years (published
13.5) [E-9025]. Any divergence in a scenario is attributable to the scenario, not to the engine.

**(b) Independent cross-validation — passes, with a caveat.** With the modality decomposition on,
the model returns 1,318.9 risk-adjusted and 2,790.7 capitalized USD million per approval. Against
DiMasi's independently produced figures that is −5.5 % and +9.1 % respectively, and −2.8 %
against his 2,870 including post-approval R&D [E-1001][E-1002][E-9026]. **Nothing was tuned to
achieve this.** The model takes per-stage *costs* from one source [E-9001] and per-modality
*success rates* from another [E-1024] and lands on a third party's total. The entire gap between
873 and 1,319 is the modality decomposition, because E[1/PoS] > 1/E[PoS] and small molecules carry
60 % of the pipeline at a 5.7 % Phase I likelihood of approval [E-1024]. The caveat: costs are
2010-era dollars and probabilities are 2011–2020, so the absolute level is not a 2026 figure.
Wouters' 985 median / 1,336 mean [E-1006] and Sertkaya's 879.3 [E-1011] sit well below the model;
the model does not reproduce those and should not be read as arbitrating between them.

**(c) Constrained solution stays at 50 — passes, and that is itself the finding.** Once all
sixteen capacities are imposed, output is unchanged at 50.00, because no physical resource
exceeds 0.90 utilisation at baseline [E-9030]. **The system today is not physically capacity-bound.**

### Discrepancies I am reporting rather than fixing

| Discrepancy | Size | Comment |
|---|---|---|
| Model Phase I entries 654/yr vs observed 1,139 CDER commercial INDs [E-6031] | model is 57 % of observed | The novel-NME backbone is not the whole IND flow. Carried as fixed exogenous background load [E-9023], not ignored. That parameter ranks 5th of 26 in the tornado, so it is a material uncertainty |
| Model Phase III patient demand 141,000/yr vs 289,129 measured [E-5064] | model is 49 % of observed | Same cause, same treatment |
| Model S0 approvals 50.00 vs CY2025 actual 46 [E-3001] | +8.7 % | Model is calibrated to CY2024, not CY2025. Not corrected |
| Model capitalized 2,791 vs Sertkaya 879.3 [E-1011] | +217 % | Not reconcilable. Sertkaya's is a bottom-up per-trial cost model; this model's cost column is a firm-reported WIP cost. Reported, not averaged |
| Model risk-adjusted 1,319 vs Wouters observed 985 median capitalized [E-1006] | model higher on a stricter basis | Wouters measured from filings; the model is a synthetic portfolio. Reported |

---

## 3. Scenario results

All figures from `RLSX/data/scenario_results.csv`. Costs in USD millions per approval.
"Binding" is the highest-utilisation resource; "1st physical" excludes the R&D budget, which sits
at 1.00 by identity rather than by measurement (see §4).

| ID | Scenario | Approvals/yr | Δ% | OOP | Risk-adj | Capitalized | Cycle (y) | Binding (u) | 1st physical (u) |
|---|---|---|---|---|---|---|---|---|---|
| S0 | Current state | 50.00 | — | 263.5 | 1318.9 | 2790.7 | 13.50 | capital 1.00 | gmp_plasmid 0.90 |
| S1 | Discovery time −80 %, PoS unchanged | **50.00** | **+0.00** | 263.5 | 1318.9 | 2631.4 | 9.90 | capital 1.00 | gmp_plasmid 0.90 |
| S2 | S1 + preclinical PoS +30 % | 54.45 | +8.90 | 263.5 | 1209.0 | 2386.1 | 9.88 | capital 1.00 | gmp_plasmid 0.93 |
| S3 | S2 + enrollment duration −40 % | 54.45 | +8.90 | 263.5 | 1209.0 | 2106.9 | 8.19 | capital 1.00 | reviewer_nda 0.88 |
| S4 | S3 + CMC lead time −50 % | 54.45 | +8.90 | 263.5 | 1209.0 | 2105.6 | 8.17 | capital 1.00 | reviewer_nda 0.88 |
| S5 | Phase II PoS +50 % | **65.88** | **+31.77** | 263.5 | 996.9 | 2383.7 | 15.03 | capital 1.00 | ph3_patients 0.96 |
| S6 | Inflow ×5, ALL capacities frozen | **50.00** | **+0.00** | 263.5 | 1318.9 | 2790.7 | 13.50 | capital 1.00 | nhp_tox 0.90 |
| S6b | Inflow ×5, capital ×5, physical frozen | 63.40 | +26.80 | 263.5 | 1318.9 | 4106.4 | 18.45 | nhp_tox 1.00 | nhp_tox 1.00 |
| S7 | Inflow ×5, capacities at historical growth, 10 y | 56.90 | +13.79 | 263.5 | 1318.9 | 3751.8 | 17.47 | ph3_patients 1.00 | ph3_patients 1.00 |
| S8 | Most favourable jointly plausible | 60.17 | +20.34 | 263.5 | 897.5 | 1908.5 | 12.35 | ph3_patients 1.00 | ph3_patients 1.00 |

Monte Carlo cycle-time bands (4,000 seeded successful paths) are in the `notes` column of the CSV:
S0 mean 13.5 y, p10 11.1, p90 16.5; S6b mean 18.7 y, p10 15.8, p90 21.6.

### The results that matter, including the null ones

**S1 produces exactly zero additional approvals.** Cutting discovery duration by 80 % moves mean
cycle time from 13.50 to 9.90 years and capitalized cost down 5.7 %, and leaves annual approvals,
risk-adjusted cost and out-of-pocket cost unchanged to the decimal [E-9031]. This is structural,
not parametric: with probability of success held constant, the only channel through which duration
can raise steady-state output is by freeing a scarce resource, and discovery duration occupies
none of the sixteen modelled resources. **This is a null result and it is the single most
important output of the model.**

**S6 also produces exactly zero.** A fivefold candidate inflow with every capacity — including the
R&D budget — held at current levels changes nothing, because the budget rations the extra
candidates out at the point of entry [E-9033]. This is not an artefact to be smoothed away: it is
the arithmetic statement that a fivefold pipeline needs a fivefold budget, at a moment when
early-stage capital is contracting on both count and dollars [E-3057][E-3058].

**S5 is the largest single-lever gain in the whole set: +31.8 %.** Raising Phase II probability
of success by 50 %, with no timeline change anywhere, raises approvals from 50.0 to 65.9 and cuts
risk-adjusted cost per approval 24.4 % [E-9032]. Under a fixed budget the mechanism is exact:
approvals = budget ÷ risk-adjusted cost per approval. Note what else happens — **mean cycle time
gets worse**, 13.50 → 15.03 years, because more survivors load the Phase III patient resource from
0.83 to 0.96 utilisation and lengthen its queue. Improving success rates makes the system slower.

**S3 and S4 add nothing to S2.** Cutting enrollment duration 40 % and CMC lead time 50 % move
approvals not at all (54.45 in all three) and cut capitalized cost by 13.3 % and a further 0.06 %
respectively. Duration levers buy schedule and cost of capital. They do not buy drugs.

**S8, the upper bound, reaches +20.3 %.** It assumes *simultaneously*: discovery duration −80 %,
preclinical PoS +30 %, clinical enrollment −40 %, CMC lead time −50 %, Phase II PoS +50 %, a joint
B2/B8/B10 attrition package with overlap, candidate inflow ×2, and ten years of historical capacity
growth [E-9036]. Every one of those holding at once buys 20 % more approvals, a 32 % cut in
risk-adjusted cost, and a cycle time of 12.35 years — still longer than a decade, and still bound
by Phase III patient slots.

**S7 delivers fewer approvals than S6b** (56.90 against 63.40) despite a decade of capacity growth,
because on the measured series clinical capacity *shrinks* at −0.92 %/yr [E-5063] while candidate
inflow does not [E-9035].

### Modality decomposition of the constraint shift (M5)

Under S6b the gain is distributed very unevenly [E-9040]:

| Modality | S0 | S6b | Realised multiple on a 5.0× input multiple |
|---|---|---|---|
| small molecule | 22.54 | 42.10 | 1.87 |
| peptide | 2.88 | 5.38 | 1.87 |
| vaccine | 1.78 | 2.40 | 1.35 |
| autologous CAR-T | 0.65 | 0.83 | 1.28 |
| siRNA / antisense | 1.04 | 1.19 | 1.14 |
| protein | 4.37 | 3.05 | 0.70 |
| gene therapy | 0.56 | 0.33 | 0.59 |
| antibody | 15.02 | 7.55 | **0.50** |
| ADC | 1.16 | 0.58 | **0.50** |

Antibodies and ADCs lose absolute output. Rationing a scarce shared input reallocates it toward
the modalities that consume least of it, and antibodies and ADCs are the heaviest users of
non-human-primate toxicology (species cross-reactivity forces NHP-only studies [E-3050][E-3051])
and of aseptic fill-finish [E-6019]. [INFER] The magnitudes here rest on relative intensity
weights that are judgements rather than measured animal counts, so this table should be read as
an ordering, not a forecast. The ordering is nonetheless the model's clearest statement that "the
constraint moves" is not a single-valued claim: it moves to different places for different
modalities, and for two of them it moves output backwards.

---

## 4. Constraint migration path

This is the headline output. Two tables, because the R&D budget sits at utilisation 1.00 by
definition — it is a budget identity, not a measured queue — and mixing it into the physical
ordering would hide the physical story [E-9042].

### 4a. Including capital

| Scenario | Binding | u | Second | u |
|---|---|---|---|---|
| S0 baseline | capital | 1.00 | gmp_plasmid | 0.90 |
| S1 discovery −80 % | capital | 1.00 | gmp_plasmid | 0.90 |
| S2 + preclinical PoS | capital | 1.00 | gmp_plasmid | 0.93 |
| S3 + enrollment −40 % | capital | 1.00 | reviewer_nda | 0.88 |
| S4 + CMC −50 % | capital | 1.00 | reviewer_nda | 0.88 |
| S5 Phase II PoS +50 % | capital | 1.00 | ph3_patients | 0.96 |
| S6 inflow ×5, all frozen | capital | 1.00 | nhp_tox | 0.90 |
| S6b inflow ×5, capital freed | **nhp_tox** | 1.00 | gmp_lentiviral | 1.00 |
| S7 inflow ×5, capacity growth | **ph3_patients** | 1.00 | nhp_tox | 1.00 |
| S8 upper bound | **ph3_patients** | 1.00 | nhp_tox | 1.00 |

### 4b. Physical resources only — the migration proper

```
S0/S1   GMP plasmid DNA + lentiviral vector + NHP toxicology, all at 0.90
        -- none of them BINDING; the system has ~10% headroom everywhere
   |
   |  add preclinical PoS (S2): more survivors, GMP rises 0.90 -> 0.93
   v
S2      GMP plasmid 0.93   (still not binding)
   |
   |  add enrollment and CMC duration cuts (S3, S4): GMP occupancy falls,
   |  the highest physical utilisation shifts to NDA review at 0.88
   v
S3/S4   reviewer_nda 0.88  (still not binding; output unchanged at 54.45)
   |
   |  raise Phase II PoS 50% (S5): survivors load the clinic
   v
S5      ph3_patients 0.96  (approaching binding)
   |
   |  multiply candidate inflow x5, free the budget (S6b)
   v
S6b     nhp_tox 1.00  ==  gmp_lentiviral 1.00  ==  gmp_plasmid  <-- FIRST TRUE BIND
   |
   |  let capacities grow ten years at historical rates (S7, S8)
   v
S7/S8   ph3_patients 1.00, nhp_tox 1.00        <-- TERMINAL BIND
```

**Reading of the path.**

1. **Today nothing physical binds.** Every physical resource is at or below 0.90 utilisation in
   S0 [E-9030]. What binds today is the R&D budget, and it binds by identity rather than by queue.
2. **Compressing discovery duration does not move the constraint at all** (S0 → S1 identical).
   Duration is not a resource.
3. **Improving probability of success moves the constraint into the clinic** (S5: ph3_patients
   0.83 → 0.96). More survivors need more patients. This is a real and under-appreciated
   mechanism: the reward for fixing target validation is paid partly in clinical congestion.
4. **Multiplying candidates moves the constraint to IND-enabling toxicology first, then to GMP
   vector and plasmid** (S6b). This independently reproduces both Agent C's prediction (B9-NHP and
   B6 first) and Agent G's (plasmid saturates at 1.06× because it feeds AAV, lentiviral and mRNA
   simultaneously [E-6064]). Three agents, three methods, same answer.
5. **The terminal constraint is Phase III patient slots** (S7, S8). It is terminal because it is
   the one resource whose measured historical growth rate is *negative* [E-5063]. Ten years of
   capacity growth everywhere else moves the bind onto the one thing that does not grow.
6. **Regulatory review capacity never binds in any of the ten scenarios.** Its highest utilisation
   anywhere is 0.88, and that only in S3/S4 where the GMP queue has been relieved around it
   [E-9042]. This agrees with the natural-experiment evidence Agents C and E produced independently
   — 3,500 FDA staff cut with output essentially held [E-3031][E-3001][E-4020] and review
   compressed to a 54.5-day median under CNPV during the worst staffing year [E-4033][E-4053].

---

## 5. Tornado sensitivity

Full data in `RLSX/data/tornado_sensitivity.csv` (26 parameters). Swing = difference in annual
approvals between the low and high end of each parameter's uncertainty range [E-9037].

| Rank | Parameter | Low → High | Approvals low → high | Swing | Swing % |
|---|---|---|---|---|---|
| 1 | Candidate inflow multiplier | 0.5 → 5.0 | 25.00 → 50.00 | 25.00 | 50.0 |
| 2 | Industry R&D budget | 0.8 → 1.5× | 26.91 → 50.00 | 23.09 | 46.2 |
| 3 | Phase II p(TS) | 0.28 → 0.486 | 41.18 → 63.88 | 22.70 | 45.4 |
| 4 | IND-enabling NHP toxicology capacity | 0.7 → 1.5× | 28.44 → 50.00 | 21.56 | 43.1 |
| 5 | Exogenous non-NME load | 0.7 → 1.3× | 50.00 → 30.36 | 19.64 | 39.3 |
| 6 | Discovery p(TS) product S1×S2×S3 | 0.40 → 0.62 | 39.22 → 51.26 | 12.04 | 24.1 |
| 7 | Phase I p(TS) | 0.47 → 0.664 | 43.52 → 55.33 | 11.81 | 23.6 |
| 8 | Phase III p(TS) | 0.578 → 0.72 | 41.29 → 51.37 | 10.08 | 20.2 |
| 9 | IND-gate reviewer capacity | 0.8 → 1.5× | 42.18 → 50.00 | 7.82 | 15.6 |
| 10 | Patients per Phase III programme | 1000 → 3000 | 50.00 → 42.57 | 7.43 | 14.9 |
| 11 | NDA/BLA review capacity | 0.8 → 1.5× | 42.65 → 50.00 | 7.35 | 14.7 |
| 12 | Phase III cost per WIP | 89.3 → 245.8 | 50.00 → 43.43 | 6.57 | 13.1 |
| 13 | Cell + gene share of pipeline | 1.45 % → 14 % | 50.00 → 44.79 | 5.22 | 10.4 |
| 14 | Preclinical p(TS) | 0.68 → 0.897 | 49.28 → 54.45 | 5.17 | 10.3 |
| 15 | Aseptic fill-finish capacity | 0.8 → 2.0× | 46.11 → 50.00 | 3.89 | 7.8 |
| 16 | Phase III patient-slot capacity | 0.8 → 1.5× | 46.30 → 50.00 | 3.70 | 7.4 |
| 17 | Filing-to-approval p(TS) | 0.883 → 0.92 | 48.54 → 50.54 | 2.01 | 4.0 |
| 18 | CMC lead time multiplier | 0.5 → 1.5× | 50.00 → 48.88 | 1.12 | 2.2 |
| 19 | GMP plasmid capacity | 0.8 → 2.0× | 49.58 → 50.00 | 0.42 | 0.8 |
| 20 | Clinical duration multiplier S5–S7 | 0.7 → 1.35× | 50.00 → 49.99 | 0.01 | 0.0 |
| 21 | Phase I/II clinical capacity | 0.8 → 1.5× | 50.00 → 50.00 | 0.00 | 0.0 |
| 22 | Autologous cell-therapy suite capacity | 0.8 → 2.0× | 50.00 → 50.00 | 0.00 | 0.0 |
| 23 | mAb drug-substance capacity | 0.8 → 2.0× | 50.00 → 50.00 | 0.00 | 0.0 |
| 24 | **Discovery duration (years)** | **0.9 → 6.0** | **50.00 → 50.00** | **0.00** | **0.0** |
| 25 | Queue-time coefficient | 0.05 → 0.20 | 50.00 → 50.00 | 0.00 | 0.0 |
| 26 | Discount rate | 7.85 % → 11.5 % | 50.00 → 50.00 | 0.00 | 0.0 |

**Three things to read carefully.**

The top-ranked parameter, candidate inflow, has its **entire swing on the downside**: halving
inflow halves output (25.0 approvals), quintupling it changes nothing (50.0). Rank 1 by swing is
not rank 1 by lever. The same asymmetry applies to the R&D budget and to NHP capacity — all three
are resources you can lose and cannot usefully gain.

**Discovery duration ranks 24th of 26 with a swing of exactly zero** across a range from 0.9 to
6.0 years. That is a 6.7-fold variation in the length of discovery producing no change whatever in
annual approvals.

The discount rate and the queue coefficient also swing zero, because neither acts on the approvals
axis at all. They are included rather than dropped, so the reader can see which parameters the
output is *not* sensitive to.

---

## 6. Non-additivity

Agent C logged that B1, B2, B8 and B10 act on overlapping attrition mass and must never be summed
[E-3097]. The model implements `q_joint = q_max + (1 − rho)·Sum(other q)` with rho = 0.60, calibrated so
the joint effect lands inside C's stated 11–26 % band against a 21 % naive sum [E-9024]. rho is
calibrated to a published band, not measured; it is the least-supported quantitative choice in the
model and is flagged as such in `model_assumptions.md` §8.

**Without the budget constraint** (directly comparable to C's elasticity definition) [E-9038]:

| Lever | Model, alone | Agent C's point elasticity |
|---|---|---|
| B1 target validation | **+10.19 %** | 10.0 % [E-3081] |
| B2 preclinical translation | **+3.77 %** | 4.0 % [E-3082] |
| B8 toxicity prediction | **+5.66 %** | 6.0 % [E-3088] |
| B10 training data | **+1.13 %** | 1.0 % [E-3090] |
| Arithmetic sum of the four | **+20.76 %** | 21 % naive sum [E-3097] |
| **Modelled joint with overlap** | **+14.42 %** | 11–26 % band [E-3097] |

The model, built from a different source's stage probabilities, reproduces C's four elasticities to
within 0.35 percentage points each. That is an independent confirmation of C's arithmetic, arrived
at without using C's formula.

**The comparison the assignment asked for:** naive sum +20.76 %, modelled joint +14.42 %.
**30.5 % of the naive gain is not real.** Anyone adding these four elasticities together
overstates the achievable gain by about three tenths.

**With the industry R&D budget binding** (this model's default), every one of those numbers falls
by roughly a third: singles +7.05 / +2.65 / +3.96 / +0.80, naive +14.03, joint **+9.88 %**. [INFER]
The budget acts as a second, multiplicative discount on top of the biological overlap: improving
success rates raises the number of programmes reaching expensive stages, which consumes budget,
which rations entry. Both discounts are real and they compound.

---

## 7. Amdahl envelope for H0-c, with the arithmetic shown

**Time.** Discovery (S1+S2+S3) is 1.0 + 1.5 + 2.0 = **4.5 years of a 13.5-year programme**
[E-9001].

```
4.5 / 13.5 = 0.3333  ->  maximum reduction in total elapsed development time = 33.3 %
model returns: 13.50 y -> 9.00 y                                              = 33.3 %  [E-9039]
```

**Capitalized cost, discovery instantaneous but still paid for.** Only the compounding horizon
shortens; the discovery spend is still incurred.

```
capitalized per approval 2,790.7 -> 2,595.7 USD m
(2790.7 - 2595.7) / 2790.7 = 0.0699                                           = 7.0 %   [E-9039]
```

**Capitalized cost, discovery instantaneous AND free.**

```
2,790.7 -> 1,647.6 USD m
(2790.7 - 1647.6) / 2790.7 = 0.4096                                           = 41.0 %  [E-9039]
```

**Risk-adjusted cost, discovery instantaneous and free.**

```
1,318.9 -> 948.2 USD m
(1318.9 - 948.2) / 1318.9 = 0.2811                                            = 28.1 %  [E-9039]
```

**True out-of-pocket cost of one successful molecule, discovery instantaneous and free.**

```
per-WIP costs: 1 + 2.5 + 10 = 13.5 of 263.5 USD m
263.5 -> 250.0;  13.5 / 263.5 = 0.0512                                        = 5.1 %   [E-9039]
```

**Annual approvals.**

```
50.00 -> 50.00                                                                = 0.0 %   [E-9039]
```

**The envelope.** Setting discovery time to zero removes **at most 33.3 % of elapsed development
time**, **7.0 % of capitalized cost per approval** if the work is still paid for, **41.0 % of
capitalized cost** if it is also free, **28.1 % of risk-adjusted cost**, **5.1 % of the cash spent
on a molecule that works**, and **0.0 % of the constraint on annual output**.

Three agents converged on the time figure by three routes: Agent A got 21–41 % [E-1094], Agent C
got 23–37 % [E-3098], this model gets 33.3 % [E-9039]. On the cost axis A got 40–43 % of
capitalized [E-1094] against this model's 41.0 % on the same "free discovery" definition — also
convergent. The number nobody had before is the last one: **zero**.

[INFER] The reason the capitalized figure looks large while the cash figure looks small is that a
capitalized cost is mostly compound interest on early spending and on downstream attrition. Making
discovery instantaneous removes the pre-clinical duration from the compounding horizon. It does
nothing to the attrition the compounding is applied to. That is the H0-b distinction in its
sharpest form: **discovery duration and probability of success are different levers, and only the
second one touches the dominant term.**

---

## 8. What this model would need to be wrong about for H0 to hold

H0 states that discovery was historically the rate-limiting step and that AI progress will make
preclinical/clinical rate-limiting instead. The model's results are unfavourable to the first half
and only partially supportive of the second. Here is what would have to be false for H0 to hold as
stated. This section is written to be usable against me.

**1. The eight-stage cost and probability structure would have to be materially wrong in the
direction of discovery.** The whole result rests on discovery being 4.5 of 13.5 years, 13.5 of
263.5 USD million of true cash per successful molecule, and 49 % of the *count* of attrition but
almost none of the *value* of it [E-9001]. If discovery's real cost share is much larger than the
source's cost-per-WIP column implies, the Amdahl ceiling rises. Agent A found the one direct
measurement of the preclinical cash share from company filings to be 12.4 % [E-1007] against
DiMasi's assumed 42.9 % [E-1090] — the observed value is closer to this model's than to the
assumed one, so this failure route is not the likely one, but it is the biggest single lever on
the conclusion.

**2. AI would have to raise probability of success, not just compress duration.** The model is
agnostic about this and shows exactly what each does: duration buys 0.0 % of output, Phase II
probability of success buys +31.8 %. If AI in fact raises Phase II probability of success by
something like 50 %, H0's *conclusion* is partly vindicated by a route H0 does not name — the
constraint does move into the clinic (ph3_patients 0.83 -> 0.96 in S5), but because more molecules
survive, not because discovery got faster. Agent B's collected evidence is that the AI Phase I
signal does not extend into Phase II [E-3008]. If that changes, S5 is the relevant scenario and
the model says the constraint does move.

**3. Candidate inflow would have to actually multiply.** The model shows a fivefold inflow buys
nothing with a fixed budget (S6) and 1.27x output with the budget freed (S6b). But the premise
itself is unverified: 29 AI-derived programmes have reached human studies cumulatively [E-9007]
against a commercial IND flow of 1,139 per year [E-6031], and CDER IND growth is 1.7 %/yr and
*decelerating* [E-4024][E-4025]. The observed inflow multiple is currently far below 1.1x, let
alone 5x. If inflow does multiply, the model's answer to Q3 is the migration path in §4b; if it
does not, the whole constraint-shift question is counterfactual.

**4. The R&D budget would have to be elastic.** The model treats it as fixed, which makes capital
the nominal binding constraint everywhere. If capital in fact expands to meet a genuinely better
pipeline, S6b rather than S6 is the right reading and the physical constraints bind. If capital
contracts — which is the observed direction [E-3057][E-3058][E-3007] — then even the modest gains
in S2–S5 do not arrive.

**5. Phase III patient capacity would have to be able to grow.** The terminal constraint in S7 and
S8 is patient slots, and it is terminal only because the measured series is −0.92 %/yr [E-5063]
with the investigator workforce at −3.97 %/yr [E-5072]. If those series reverse — through
decentralised trials, external controls, or a genuine expansion of matched site capacity — the
terminal bind moves elsewhere and the ceiling rises. Agent F's judgement is that the available
mitigations are real but bounded and none is a 2x multiplier [E-5034][E-5042][E-5037].

**6. The overlap coefficient would have to be much lower than 0.60.** If the four probability
levers are in fact nearly independent, the joint gain is +20.8 % rather than +14.4 % and the
probability route is correspondingly more attractive. rho is calibrated to Agent C's stated band,
not measured [E-9024], and no study of overlap between these failure classes was found.

**7. The model would have to be wrong to treat delivery (B7) as invisible.** It cannot represent
indication classes that are never attempted [E-3042][E-3044]. If a large share of the addressable
disease space is currently excluded by delivery physics, then solving delivery adds programmes the
model cannot count, and the true ceiling is higher than 60 approvals a year. This is the
limitation most likely to make the model's conclusions too pessimistic about the value of
non-clinical work.

**What would falsify the model's own conclusion most cleanly.** A natural experiment in which
discovery duration was sharply compressed for a large, identifiable cohort of programmes and
annual approvals from that cohort rose more than the model's 0.0 %. No such experiment exists in
the data any agent collected. The nearest available natural experiment runs the other way and
concerns a different step: FDA review time fell from over three years to under one between 1983
and 2017 and total time from clinical-testing authorisation to approval did not move [E-1029].
A very large improvement was delivered at one step and system throughput did not respond. The
model reproduces that logic and applies it to discovery.

---

## 9. UNRESOLVED

7 records in `RLSX/work/D/unresolved.csv`, each with the full query list, the failure reason, at
least three alternative sources attempted, and a current best estimate with its basis. Summary:

1. **Per-stage cost data newer than 2010 with the same eight-stage resolution.** No source
   published since resolves discovery into three stages with costs. Best estimate: the 2010 column
   [E-9001], with the Phase III term swept 89.3–245.8 in the tornado.
2. **Measured utilisation for aseptic fill-finish and ADC conjugation.** No CDMO discloses either;
   Agent G reached the same wall independently. Best estimate: G's lead-time proxy rule.
3. **Absolute non-human-primate toxicology study capacity per year.** Not published by any source
   reached. Best estimate: utilisation 0.90 from the two-thirds-unfillable figure [E-3050].
4. **A published overlap coefficient for B1/B2/B8/B10.** Does not exist. Best estimate: rho = 0.60
   calibrated to Agent C's band [E-9024].
5. **CDER FTE series 2015–2025 in machine-readable form.** FDA pages return HTTP 401. Best
   estimate: FY2007 and FY2014 anchors giving 4.65 %/yr [E-9006], flagged `circular_risk: true`.
6. **Per-modality patients-per-programme.** Not published. Best estimate: uniform, with the known
   direction of error stated.
7. **Non-NME share of shared-resource demand, measured rather than inferred.** Best estimate:
   57 % IND-side and 49 % clinical-side [E-9023], swept 0.7–1.3x in the tornado.

No item was deferred, narrowed, or sampled. All nine mandated scenarios plus two additions were
run, all 26 tornado parameters were swept, and every model assumption is enumerated in
`RLSX/model/model_assumptions.md`.
