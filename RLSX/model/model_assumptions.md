# Model assumptions — RLSX Agent D constraint model

Every assumption the model makes is listed here. Each carries either an evidence ID or the
literal marker `[ASSUMPTION-UNSUPPORTED]`. Nothing that affects a reported number is omitted.

Model file: `RLSX/model/constraint_model.py`. Seed `20260818`. Standard library only.
Outputs: `RLSX/data/scenario_results.csv`, `RLSX/data/tornado_sensitivity.csv`.

---

## 1. Stage structure

| Assumption | Value | Basis |
|---|---|---|
| Eight stages S1–S8 | target-to-hit, hit-to-lead, lead optimisation, preclinical, Phase I, Phase II, Phase III, submission-to-launch | [E-9001] |
| Stage p(TS) | 0.80 / 0.75 / 0.85 / 0.69 / 0.54 / 0.34 / 0.70 / 0.91 | [E-9001], independently recorded by Agent A as [E-1018] |
| Stage cycle times (years) | 1.0 / 1.5 / 2.0 / 1.0 / 1.5 / 2.5 / 2.5 / 1.5 | [E-9001], first four independently [E-1017] |
| Cost per WIP unit (USD m) | 1 / 2.5 / 10 / 5 / 15 / 40 / 150 / 40 | [E-9001] — this column exists in no other recovered source |
| Stages are strictly serial | no stage overlap modelled | `[ASSUMPTION-UNSUPPORTED]`. Tufts CSDD measured 18 % of programmes overlapping Phase II and Phase III [E-1036]; the model cannot represent that, so it slightly overstates cycle time for expedited programmes |
| WIP per launch = 1 / cumulative PoS | exact arithmetic identity | [E-9001], reproduced to 0.02 % [E-9025] |

**Why one source rather than a blend of the seven Agent A collected.** Blending DiMasi's costs
with BIO's probabilities and Sertkaya's durations would produce a stage model whose parts were
never reconciled with each other, and whose totals could not be checked against anything. Using
one internally consistent published model means the engine can be validated against that model's
own published totals before any scenario is run. The cost of that choice is that the absolute
level is 2010-era; the tornado sweeps the largest cost term (Phase III cost per WIP) across the
full published range 89.3–245.8 USD m [E-1012][E-1004].

---

## 2. Discount rate and cost bases

| Assumption | Value | Basis |
|---|---|---|
| **Base discount rate** | **11.0 % / year** | [E-9001], the rate of the source stage model |
| Capitalization rule | each stage's risk-adjusted spend compounded forward from that stage's own midpoint to launch | Derived: this rule reproduces the source model's published per-stage capitalized column to within 1.3 % and its total to 0.02 % [E-9025] |
| Out-of-pocket basis | cash for one successful programme, failures excluded | M1 |
| Risk-adjusted basis | failures loaded, no cost of capital | M1 |
| Capitalized basis | risk-adjusted plus cost of capital | M1 |
| Alternative rates run | 10.5 % [E-1001], 8.49 % [E-9002], 7.85 % [E-9002], 7.0 % [E-1009] | reported in full; the spread alone moves the headline 32 % [E-9041] |

The current market cost of capital for the sector is roughly two percentage points below the
rate embedded in the canonical cost-per-approval literature [E-9002]. The model reports both
rather than choosing.

---

## 3. Modality decomposition (M5)

| Assumption | Value | Basis |
|---|---|---|
| Ten modalities | small molecule, mAb, protein, peptide, vaccine, ADC, antisense, siRNA, gene therapy, autologous CAR-T | [E-1024] |
| Mix weights | BIO 2011–2020 Phase I programme counts (6803/2136/800/619/316/184/162/70/96/67) | [E-1024] |
| Per-modality clinical PoS | S5–S8 scaled by a fixed factor so cumulative Phase-I-to-approval matches that source's modality LoA | [E-1024] |
| Scale factor computed once, from base probabilities | not recomputed per scenario | Mandatory. Recomputing it would renormalise every PoS intervention back to baseline and make the model report that PoS improvements do nothing. This was an actual bug in the first build and is documented here so no one reintroduces it |
| Mix understates 2026 cell/gene share | 1.45 % modelled vs roughly 14 % implied by current IND stocks | [E-9021], [E-6031], [E-6032]. Both values are run in the tornado; swing 5.2 approvals/yr |
| Discovery and preclinical p(TS) do not vary by modality | shared | `[ASSUMPTION-UNSUPPORTED]` — no modality-resolved preclinical transition data was recovered by Agent A or by this agent |

---

## 4. Resources, capacities, and utilisations

Capacity is set as `capacity = baseline_total_demand / u0`, so every resource sits at its
published baseline utilisation in S0 by construction. This makes u0 the load-bearing parameter,
not the absolute capacity, which is why u0 is stated explicitly for each resource.

| Resource | u0 | Growth (S7) | Basis for u0 | Basis for growth |
|---|---|---|---|---|
| gmp_plasmid | 0.90 | +6.5 %/yr | 10-month lead time [E-6008], saturation multiple 1.06x [E-6064] | [E-9005] |
| gmp_lentiviral | 0.90 | +6.5 %/yr | 11-month lead time [E-6009], 1.06x [E-6062] | [E-9005] |
| gmp_fill_finish | 0.85 | +4.0 %/yr | 1.12x [E-6066] | `[ASSUMPTION-UNSUPPORTED]`, set below the mammalian rate because of the 2.5–3 y build-and-qualify lag and format non-fungibility [E-6019] |
| gmp_cell_suite | 0.80 | +6.5 %/yr | 1.19x [E-6063], 3-week slot wait [E-6014] | [E-9005] |
| gmp_adc_conj | 0.80 | +15.0 %/yr | 1.19x [E-6065] | bioconjugation market ~15 % CAGR, Lonza 5→7 suites [E-6020] |
| gmp_aav | 0.50 | +6.5 %/yr | 50 % suite utilisation [E-6061] | [E-9005] |
| gmp_mab_ds | 0.80 | +6.5 %/yr | 4.8x on declared IND support [E-6060] | [E-9005] |
| gmp_sm_api | 0.095 | +6.7 %/yr | 10x [E-6069] — G's own loosest estimate | small-molecule CDMO market CAGR [E-6021] |
| gmp_oligo | 0.12 | +10.0 %/yr | 8x [E-6067] | `[ASSUMPTION-UNSUPPORTED]`, directionally from the Agilent expansion [E-6018] |
| gmp_vaccine_ff | 0.85 | +4.0 %/yr | 1.12x [E-6066] | as fill-finish |
| nhp_tox | 0.90 | +2.0 %/yr | two-thirds of NHP requests unfillable since 2021 [E-3050] | 4–5 y breeding lag [E-9009] |
| clinical_ph12 | 0.80 | −0.92 %/yr | `[ASSUMPTION-UNSUPPORTED]` — scaled down from the Phase III value; 48 % of sites fail their enrolment plan [E-5020] is consistent with a high but sub-unity figure | measured phase III participant throughput [E-5063] |
| ph3_patients | 0.83 | −0.92 %/yr | derived: 78.5 modelled Phase III starts/yr × 1,800 patients ≈ 141,000 against 289,129 measured [E-5064] plus background [E-9023] | [E-5063] |
| reviewer_ind | 0.85 | +4.65 %/yr | 1,855 INDs against 5,044 staff [E-4024][E-4019] | [E-9006] |
| reviewer_nda | 0.85 | +4.65 %/yr | derived from the April 2025 RIF as a natural experiment [E-9022] | [E-9006] |
| capital | 1.00 | +6.36 %/yr | budget identity, not a queue — see §5 | nominal PhRMA R&D CAGR 2000–2022 [E-1041] |

**Conflicting capacity growth rates, both modelled and both reported.** Agent G's saturation
multiples imply manufacturing sub-capacities near 1.06–1.19x of current demand and therefore
essentially no headroom, while G's own commentary holds that biological manufacturing has
historically absorbed sustained demand within 3–5 years. Independently, [E-9005] measures
installed mammalian supply growing at 6.5 %/yr against demand at 11.5 %/yr — a widening gap.
S6b uses G's frozen-capacity reading; S7 uses the growth reading. They give 63.4 and 56.9
approvals per year respectively, and both are reported.

### Resource demand coefficients

| Coefficient | Value | Basis |
|---|---|---|
| Patients per Phase I programme | 60 | [E-9008], published range 20–100 |
| Patients per Phase II programme | 250 | [E-9008], published range 100–300 |
| Patients per Phase III programme | 1,800 | [E-9008], published range 300–3,000; swept 1,000–3,000 in the tornado |
| Patients per programme does not vary by modality | uniform | `[ASSUMPTION-UNSUPPORTED]`. This is wrong in a known direction: rare-disease and biomarker-selected programmes need fewer patients but harder-to-find ones [E-3027][E-5028]. The model therefore understates the constraint for precision-medicine modalities |
| NHP intensity weights | SM 0.6, mAb 1.4, protein 1.2, peptide 0.6, vaccine 0.8, ADC 1.4, RNA 0.9, GT 1.3, CAR-T 0.2 | `[ASSUMPTION-UNSUPPORTED]` as numbers; the ordering is from [E-3050][E-3051] (species cross-reactivity forces NHP-only work for antibodies and ADCs; cell therapy is often not modellable in animals). Relative weights, not animal counts |
| GMP occupancy = clinical duration × modality line map | see `GMP_MAP` in the code | line assignments from [E-6064] (plasmid feeds AAV, lentiviral and mRNA at once); intensities `[ASSUMPTION-UNSUPPORTED]` |
| Capital demand = risk-adjusted spend across all live stages | identity | [E-9001] |

---

## 5. Capital as a resource

Capital is modelled with `u0 = 1.00`, i.e. the industry R&D budget is fully spent [E-1041]. This
is a **budget identity, not a measured queue**, and it is flagged as such everywhere it appears.
Its consequences are large and must be read with that caveat:

- In S0–S5 capital is nominally the highest-utilisation resource. That is definitional.
- In S6 it rations a fivefold candidate inflow back to baseline, producing a null result.
- S6b exists solely to remove it and expose the physical ordering underneath.
- The report gives a separate physical-only constraint migration table for this reason.

What the model does **not** contain: any feedback from output or returns back onto capital supply.
Agent C's evidence that ex-incretin R&D returns are 2.9 % and falling [E-3007], and that approved
products are being withdrawn commercially [E-3060], both point to the budget shrinking in response
to poor returns. The model holds the budget exogenous, which makes every scenario more optimistic
than it should be.

---

## 6. Queueing

| Assumption | Value | Basis |
|---|---|---|
| Queue function | `W(u) = QK · u / (1 − u)` | standard heavy-traffic form; `[ASSUMPTION-UNSUPPORTED]` as a functional choice |
| QK | 0.11 years | derived from three published (utilisation, lead-time) pairs [E-9020] |
| Utilisation capped at 0.95 for delay purposes | yes | a rationed loss system cannot express an infinite queue; excess demand is lost, not queued forever |
| Queue enters cycle time as a **delta** from the S0 solution | yes | published stage durations already contain today's queueing, so adding W(u) in full would double-count it. Consequence: S0 mean cycle time is exactly 13.50 y |
| Reviewer IND delay weight 0.10 | yes | the 30-day IND clock is statutory and non-negotiable [E-4029], so this resource blocks rather than delays |
| Reviewer NDA delay weight 0.35 | yes | `[ASSUMPTION-UNSUPPORTED]`; PDUFA goal dates cap the delay a queue can express [E-4020] |
| Rationing is multiplicative in intensity: `t_modality = throttle ^ (intensity / mean intensity)` | yes | `[ASSUMPTION-UNSUPPORTED]` as a functional choice. A linear rule was tried first and eliminated whole modalities outright, which is not how rationing of a shared input behaves |

---

## 7. Attrition structure

- Attrition is the spine of the model. Every stage cost is `(1 / cumulative PoS from that stage)
  × cost per WIP` [E-9001], so any change in a downstream p(TS) re-prices every upstream stage.
- Attrition is modelled as a per-stage Bernoulli transition; there is no correlation between a
  molecule's Phase II and Phase III outcomes beyond what the stage probabilities encode.
  `[ASSUMPTION-UNSUPPORTED]` — in reality a mechanism that fails in one indication predicts
  failure in adjacent ones, which would make attrition more clustered and less diversifiable.
- Failure causes are not represented individually. B1, B2, B8 and B10 act on a single pooled
  clinical failure mass. This is the same simplification Agent C made and is what makes the
  overlap structure in §8 necessary.
- Terminations for business rather than technical reasons are inside the published transition
  probabilities and cannot be separated out. Agent A flagged this as a denominator problem across
  the six studies she collected [E-1020][E-1023][E-1027].

---

## 8. Overlap / non-additivity structure

| Assumption | Value | Basis |
|---|---|---|
| A "10 % improvement" in factor *i* reduces cumulative clinical attrition by `q_i = f_i · θ_i / 10` | — | Agent C's own definition, [E-3080] lineage |
| `f, θ` for B1 / B2 / B8 / B10 | 0.45/0.30, 0.25/0.20, 0.30/0.25, 0.10/0.15 | [E-3081][E-3082][E-3088][E-3090] |
| Combination rule | `q_joint = q_max + (1 − ρ) · Σ(other q)` | `[ASSUMPTION-UNSUPPORTED]` as a functional form |
| ρ | 0.60 | calibrated so the joint effect lands inside C's stated 11–26 % band against a 21 % naive sum [E-3097][E-9024] |
| Gain allocated across S5–S8 in proportion to each stage's failure mass, solved by bisection | yes | keeps the intervention on C's scale (cumulative clinical attrition), not on one stage's sub-mass |

ρ is **calibrated to a published band, not measured**. No study of overlap between these four
failure classes was located. This is the single least-supported quantitative choice in the model
and it is the reason the non-additivity section reports the naive and joint numbers side by side
rather than only the joint one.

---

## 9. Calibration

| Assumption | Value | Basis |
|---|---|---|
| Baseline output target | 50 novel approvals/yr | [E-1038] CY2024; CY2025 was 46 [E-3001] |
| Candidate inflow calibrated to hit that target unconstrained | 1,859 target-to-hit starts/yr | derived |
| Implied Phase I entries | 654/yr | derived |
| Background (non-NME) load | held constant in every scenario | [E-9023]; the NME backbone is 57 % of observed IND flow and 49 % of measured Phase III patient volume |
| Background load does not respond to any scenario | yes | `[ASSUMPTION-UNSUPPORTED]`. If AI compresses discovery for non-NME work too, background load rises and every capacity binds sooner; the model is optimistic here. Swept 0.7–1.3× in the tornado, rank 5 of 26 |

S0 approvals are pinned at 50 by the calibration, so "S0 reproduces 50 approvals" is **not** a
test. The real tests, all reported in the run output and in the report, are: (a) does the engine
reproduce the source model's published totals — yes, to 0.02 %; (b) does the modality-weighted
cost land on independently published estimates without tuning — yes, within 5.5 % and 9.1 % of
DiMasi [E-9026]; (c) does the constrained solution stay at 50 once capacities are imposed — yes,
because no physical resource exceeds 0.90 at baseline.

---

## 10. What this model cannot represent

Stated plainly, because these bound every result above.

1. **It is a steady state.** It cannot represent the 3–5 year transient in which a capacity
   shortfall is real and then absorbed. Agent G's central caveat — that an inflow surge saturates
   several sub-capacities immediately, produces a genuine queueing period, and is then absorbed —
   is exactly the dynamic this model flattens into two static answers (S6b and S7).
2. **No geography.** M6 is out of reach. Every capacity is global and every approval is
   undifferentiated. The regional divergence Agent E identifies at the IND/CTA gate (China's
   30-working-day commitment [E-4043] against a US RFI stage [E-4029]) has no representation.
3. **No indication structure.** Oncology's 3.4 % Phase I LoA against non-oncology's 20.9 %
   [E-1021] is folded into the modality mix, which is not the same thing.
4. **No option value on indications never attempted.** Agent C's point that delivery failure
   (B7) deletes whole indication classes before a programme starts, and therefore never appears
   in attrition statistics [E-3042][E-3044], cannot be modelled here at all. B7's effect on
   output is structurally invisible to this model, and its absence biases the results toward
   understating the constraint.
5. **No candidate quality selection.** In S6 the model discards four fifths of a fivefold inflow
   at random rather than keeping the best fifth. Real sponsors select. This makes S6 pessimistic
   about the quality channel and optimistic about nothing.
6. **No capital feedback.** See §5.
7. **No learning curve.** Costs per WIP and probabilities are constant; there is no mechanism by
   which running more programmes makes each one cheaper or more likely to succeed.
8. **No representation of B12, B13, B14** — IP congestion, talent, biosecurity. Agent C scored
   all three as non-binding [E-3092][E-3093][E-3094] and none has a capacity representation here.
   If any of them becomes binding, this model will not see it.
9. **The cost basis is dated.** Costs are 2010-era USD [E-9001], probabilities 2011–2020
   [E-1024], capacities 2024–2026 [E-6xxx][E-5xxx]. The mixture is stated rather than deflated,
   because deflating one series and not the others would be worse.
10. **Utilisation figures are largely proxies, not measurements.** Agent G was explicit that most
    sub-areas publish a lead time and not a utilisation, and applied a uniform lead-time-to-
    utilisation rule to make them comparable. That crudeness propagates directly into this
    model's capacity levels, and it is why the tornado sweeps every capacity parameter.
