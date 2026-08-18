CHARTER_ACK: R1,R2,R3,R4

# Agent X — 반증 레드팀 / Falsification Red Team, Pass 1

Target: the emerging consensus of Agents A, B, C, E, F, G, H as written in their reports on disk.
Evidence block: **E-9500 … E-9538** (39 records) in `RLSX/evidence/parts/X.jsonl`. All records carry `confidence: null`, `graded_by: null` for Agent R.
Search record: 38 WebSearch/WebFetch calls. Four fetches were blocked (BCG 403, Science 403, OECD 403, Nature IdP redirect) and were replaced by independently reachable carriers; one PDF (L.E.K.) was parsed locally with Python `zlib`/`re` and then confirmed against the publisher's HTML page.

**Method.** For each attack I first constructed the strongest version of the case *against* the consensus, using evidence I collected myself rather than evidence inherited from the agents I am attacking. I then asked whether that case survives its own best counter-test. A verdict of 기각 means the attack was built in good faith and failed; those sections state why, because a failed attack is a load-bearing result.

**Verdict tally: 채택 3 / 부분채택 12 / 기각 5.**

---

## X-01 — H0-a: per-programme economics are structurally blind to programmes that were never started

**The attack.** Every upstream agent tests H0-a with per-programme statistics: stage durations [A], stage costs [A], phase transition probabilities [A][C], attrition attribution [C]. Every one of those statistics is conditioned on a programme having started. If discovery-stage constraints suppressed the *number of programmes ever attempted*, that suppression is invisible in all of them by construction, and the consensus rejection of H0-a would be an artefact of the estimator rather than a finding about the world.

**The evidence.** The suppressed population is large and measurable at its boundary. About 4,500 genes are classified as the druggable genome and fewer than 700 are targeted by an approved drug [E-9501]; Santos and colleagues independently count 667 human protein targets across all 1,578 FDA-approved drugs [E-9500]. About 85 percent of the druggable genome has therefore never yielded an approved drug [E-9536]. Thirty-eight percent of the proteome is classified dark, and 10 percent of human proteins absorb 75 percent of research attention [E-9501]. Roughly a quarter of the ~13,600 drug-target pairs in the current pipeline sit on 37 targets [E-9509].

The mechanism is demonstrable on a single target. RAS was confirmed as the first human oncogene in 1982; target validity was never in doubt; the first direct inhibitor was approved on 28 May 2021, 39 years later, and the intervening obstacle was the absence of a bindable pocket until the switch-II site was found in 2013 [E-9502]. For 31 of those 39 years, no KRAS programme existed to appear in anyone's attrition statistics.

**[INFER]** This is a genuine hole in the consensus methodology and it is not repaired by any evidence currently in the ledger. The Amdahl calculations in A §4 and C §1.3 both compute *what fraction of an existing programme's time and cost discovery consumes*. Neither computes *how many additional programmes would exist if discovery capability were higher*, and the second quantity is the one H0-a is actually about.

**What survives the counter-test.** The attack establishes that the channel exists and is quantitatively large at its boundary. It does not establish that the channel was *binding on annual approvals*, because approvals are also limited by clinical throughput and capital, and X-04 shows that the historical episode in which target supply expanded fastest did not raise first-in-class output. The honest reading is that the suppressed-programme channel sets the *option set*, and clinical attrition sets the *conversion rate* on that option set.

**Verdict: 부분채택.**

**Required change to the report.** Wherever the report states that H0-a is rejected, it must add the following qualification in the same paragraph, not in a footnote: *"This rejection is established on per-programme time, cost and attrition statistics, all of which are conditioned on a programme having started. It does not cover the channel in which discovery-stage capability limits the number of programmes ever attempted; on that channel about 85 percent of the druggable genome has never yielded an approved drug [E-9536] and no programme-level dataset records the counterfactual, so H0-a is rejected for per-programme economics and undetermined for programme count."* The word "rejected" must never appear unqualified.

---

## X-02 — H0-a: a Phase II efficacy failure is a discovery-stage decision error observed late

**The attack.** The consensus books efficacy failures as clinical attrition. But a molecule that engages its target, achieves exposure and still fails on efficacy has not failed clinically in any causal sense — it has failed at target selection, which is a discovery-stage act. If a large share of clinical attrition is displaced discovery error, then attributing it to "clinical" is an accounting convention, and H0-a is closer to correct than the consensus allows.

**The evidence.** The consensus's own agents already document the mechanism: Agent B's failure census finds seven of nine terminated AI assets failed on target validity, exposure or unpredicted toxicity, and none failed because a molecule could not be found; Agent C attributes 40-50 percent of failures to lack of clinical efficacy and ranks B1 first. My own collection sharpens the causal attribution rather than the share. Human genetic support raises the probability of success 2.6-fold, up to fourfold in haematology and metabolic disease [E-9507]. That is the size of the *decision-quality* effect available at target-selection time, and it is larger than any effect any clinical-operations intervention in Agent F's catalogue produces.

**Why the attack does not go the whole way.** The displacement argument proves that the *cause* of clinical failure is upstream. It does not prove that the *constraint* was upstream, because the common brief defines a constraint as a step whose improvement raises system output, and the improvement in question — better target choice — was not available to be made. Kola and Landis document what it looks like when a discovery-stage capability genuinely becomes available: pharmacokinetic attrition fell from about 40 percent of failures in 1991 to about 10 percent by 2000 [E-9506]. No comparable capability existed for target validity in that period. So the correct statement is that target selection is the *causal locus* of most attrition and has been throughout, while the *binding resource* was the absence of a method for judging target validity ex ante.

**Verdict: 부분채택.**

**Required change to the report.** The sentence pattern "clinical attrition has dominated throughout" must be replaced wherever it appears by: *"Attrition is overwhelmingly observed in clinical stages, but its dominant cause is a decision taken at the discovery stage — target selection — so the stage where failure is measured and the stage where it is caused are different [E-9507][E-9506]. Reporting attrition by the stage of observation, as every published dataset does, systematically flatters discovery and penalises the clinic."* The report must not claim that this distinction is merely semantic; it changes which intervention has elasticity.

---

## X-03 — H0-a: discovery genuinely was the rate-limiting step in identifiable domains, and the consensus states H0-a as if it were domain-uniform

**The attack.** H0-a is asked as a single global question. It has different answers by therapeutic domain, and in at least two domains the pro-H0-a answer is decisively correct.

**The evidence.** Antibacterials: no major new class was introduced between 1962 and 2000, and the field's own diagnosis of the void is failure of screening to yield leads, not clinical failure and not absent demand [E-9503]. The decisive single measurement is GSK's: more than 300 targets evaluated, 70 high-throughput screening campaigns against a library of over 500,000 compounds between 1995 and 2001, five leads, no approved drug [E-9504] — a yield of 0.07 leads per campaign. In that domain, in that period, output was limited by the inability to find chemical matter, which is exactly the claim H0-a makes. Oncogenic RAS is the second case [E-9502].

**Counter-test.** Both cases are domains where the *chemical-matter* problem, not the *target-identification* problem, was binding. H0 as posed says "research to find hit protein structures/sequences", which covers chemical matter. So the cases support H0-a on its literal wording. They do not generalise: antibacterials and KRAS are selected precisely because they are the field's canonical hard cases, and a claim built on the two hardest cases in the literature is a claim about the tail.

**Verdict: 부분채택.**

**Required change to the report.** The H0-a verdict must be stated with an explicit domain qualifier: *"H0-a is rejected as a statement about the aggregate pipeline and is supported in specific domains where chemical matter, not target biology, was the binding scarcity — antibacterials 1962-2000 [E-9503][E-9504] and oncogenic RAS 1982-2021 [E-9502] are the two documented cases. Any conclusion of the form 'discovery was never the bottleneck' is too strong and must not be written."*

---

## X-04 — the strongest pro-H0-a case fails its own natural experiment

**The attack, and why I built it.** If discovery capability constrained output, then the largest expansion of discovery capability in the field's history — genome sequencing plus target-based high-throughput screening, roughly 1995-2010 — should have produced a measurable rise in first-in-class output. This is the best available natural experiment on H0-a and no upstream agent ran it.

**The evidence.** It did not. Of 50 first-in-class small molecules approved 1999-2008, 28 (56 percent) came from phenotypic screening and only 17 (34 percent) from target-based approaches [E-9505]. The paradigm that the genomics expansion was supposed to supercharge produced fewer first-in-class medicines than the paradigm it replaced. The pattern persists in the current period in a different form: despite a doubling of the overall pipeline and a threefold rise in early- and mid-stage venture investment, the number of novel biological targets entering the pipeline each year fell from around 100 a decade ago to 30 in 2024 [E-9509]. Target supply is not what is scarce; target *appetite* is.

**[INFER]** This is the cleanest disconfirmation of H0-a in the whole run and it is stronger than anything the upstream agents assembled, because it is a natural experiment on the exact variable H0-a names rather than an accounting decomposition. A step whose capacity was multiplied by orders of magnitude, and whose output share of first-in-class medicines then *fell*, was not the constraint.

**Verdict: 기각 — the consensus survives, and this attack strengthens it.**

**Required change to the report.** None to the conclusion. The report should *add* this natural experiment as the primary evidence for the H0-a rejection, in place of or alongside the FDA-review-time argument the agents currently lean on, because it tests the discovery step directly rather than by analogy: *"Target-based discovery, the paradigm the genomics expansion enabled, produced 17 of 50 first-in-class small molecules approved 1999-2008 against 28 from phenotypic screening [E-9505]; and in the current decade novel targets entering the pipeline fell from about 100 a year to 30 in 2024 while the pipeline doubled and venture funding tripled [E-9509]."*

---

## X-05 — "clinical will become the rate-limiting step" is a restatement of the status quo, not a prediction

**The attack.** If clinical stages have dominated time, cost and attrition for the entire period for which stage-resolved data exist — which is what Agents A, B and C jointly establish — then H0's forward-looking half asserts that a thing which has been true for forty years will continue to be true. That is not falsifiable as posed, and a report that adopts it is reporting a tautology as a finding.

**The evidence that the claim has *some* content.** The forward claim is not entirely empty, because the relevant quantities are moving. Cumulative likelihood of approval from Phase I fell across successive Citeline/BIO analyses from 10.4 percent (2014) to 9.6 (2016), 7.9 (2021) and 6.7 percent (2024) [E-9512], and Phase I success fell from over 75 percent in 2006-2008 to below 40 percent [E-9513]. Trial terminations fell over the same period, from 10.6 percent in 2010 to 4.7 percent in 2021 [E-9514], so the decline in approval probability is not an artefact of more operational failures. The clinical constraint is therefore *tightening*, and it is tightening on the probability axis rather than the operational axis.

**[INFER]** So H0's forward half can be given content, but only by restating it as a rate claim rather than a rank claim. "Clinical becomes the rate-limiting step" is unfalsifiable; "clinical probability of success continues to fall at roughly 4 percent relative per year, so the clinical constraint tightens faster than discovery relieves" is falsifiable and is currently supported.

**Verdict: 부분채택.**

**Required change to the report.** The report must not answer H0's forward half in rank terms. Wherever it says clinical becomes or remains the rate-limiting step, it must state the falsifiable version and its test: *"Restated as a rate claim: cumulative likelihood of approval fell from 10.4 percent to 6.7 percent across successive analyses of the same dataset, 2014 to 2024, while trial termination rates fell [E-9512][E-9514]. The prediction that fails this test is any scenario in which clinical probability of success stabilises or rises through 2030."* The report must also state explicitly that the rank formulation of H0's second half is not falsifiable and is not adopted as a finding.

---

## X-06 — is there any credible path on which clinical stops being the constraint by 2040?

**The attack.** I looked for the strongest bull case that the clinical constraint dissolves, rather than assuming it persists.

**The candidates and what each is worth.** (i) *In-silico trials and virtual control arms.* EMA published a draft qualification opinion on virtual control groups on 31 March 2026, and it is a consultation document covering matched historical controls under defined conditions [E-9529]. FDA CDER and EMA published ten joint Guiding Principles of Good AI Practice in January 2026, and in-silico evidence remains exploratory or supplemental, with the demonstrated use being sample-size reduction rather than trial replacement [E-9530]. (ii) *Surrogate endpoints.* FDA's public table lists over 200 surrogate markers that have been the basis of an approval [E-9528] — the accepted set is already two orders of magnitude larger than the formally qualified set, so the near-term headroom from this lever is smaller than the qualification-queue statistics suggest. (iii) *Jurisdictional relocation.* Covered in X-13; it moves where trials run, not whether they are needed. (iv) *Genetic pre-validation.* A 2.6-fold relative success multiplier [E-9507] applied to a 6.7 percent base gives about 17 percent — a large improvement that still leaves five of six programmes failing in the clinic.

**[INFER]** The strongest combination — universal genetic pre-validation, surrogate endpoints everywhere they are scientifically admissible, and virtual controls at their qualified scope — raises cumulative probability of success by roughly a factor of two to three and cuts sample sizes by tens of percent. That is a large gain and it does not move the constraint, because at 17 percent cumulative probability of success the clinic still destroys more than four fifths of everything entering it, and no located instrument removes the requirement to expose humans to the molecule.

**Verdict: 기각 — no credible path was found on which clinical ceases to be the binding constraint by 2040.**

**Required change to the report.** None to the conclusion. The report should record that the bull case was constructed and failed, and should name the specific instrument that would falsify the conclusion if it matured: *"The conclusion that clinical remains binding through 2040 fails if virtual control groups move from EMA draft qualification [E-9529] to routine acceptance for pivotal efficacy evidence in non-rare indications. As of August 2026 the qualified scope is matched historical controls under defined conditions, and in-silico evidence is supplemental [E-9530]."*

---

## X-07 — is the AI discovery-compression finding real at all?

**The attack.** Compression could be an artefact of four things at once: the comparator baseline is chosen by the party making the claim; the targets chosen are precedented; the clock starts where the claimant chooses; and only successes are reported.

**The evidence.** The comparator is the weakest link. Insilico's 18-month target-to-candidate claim is stated against "a typical 4-5 years", company-reported, with no matched control cohort [E-9534]. Agent B independently found the flagship Exscientia asset targeted 5-HT1A, a class with decades of medicinal chemistry behind it. Against that, the 30-50 percent preclinical-time reduction figure appears in two peer-reviewed reviews collected by Agent B and in a third independent review I retrieved, which reports the same 30-50 percent from a systematic review of 20 AI-driven programmes 2018-2023 while stating that Phase I/II attrition remained at industry benchmarks.

**Why the attack fails.** The comparator baseline is independently corroborated rather than self-serving: Paul and colleagues' widely used stage model puts target-to-hit at 12 months, hit-to-lead at 18 and lead optimisation at 24, i.e. 54 months, which is the 4-5 years the companies cite. The 30-50 percent figure survives in reviews that are not authored by the companies claiming it. And the compression claim is separable from the impact claim: Agent B's finding that compression does not propagate to time-to-dosed-patient is a stronger and better-evidenced attack than the one I built here, and it is already in the consensus.

**Verdict: 기각 — the 30-50 percent preclinical compression finding survives.**

**Required change to the report.** One wording constraint only. The report must never state the per-programme saving in years ("2.5-4.5 years saved") in its own voice; that framing exists only in company-issued material [E-9534]. The defensible statement is a percentage on preclinical activities.

---

## X-08 — the low-base-rate ceiling is a statement about 2026 and it fails for 2035 and 2040

**The attack.** The consensus caps AI's system-level effect at low single-digit percent because AI-derived candidates are 1.0-3.4 percent of INDs. That is a snapshot. The mission asks for ranked bottlenecks with probabilities at 2030, 2035 and 2040. If the share is growing exponentially, a snapshot ceiling is invalid for every one of those horizons.

**The evidence.** The cumulative count of AI-derived clinical-stage molecules ran about 15 in early 2022 across 20 AI-intensive companies [E-9516], 67 by April 2024 and more than 75 by end-2024, and 117 by December 2025 across 63 companies. Pairwise doubling times are 1.28, 1.21, 2.05 and 1.56 years, giving a range of **1.2 to 2.1 years, central about 1.5** [E-9517]. Setting base IND growth at 5 percent per year, the AI share doubles every 1.66 to 2.35 years. Starting from 1.0 percent on a global IND denominator or 3.7 percent on the US commercial IND denominator, the share **crosses 10 percent between about 2029 and 2033 and 50 percent between about 2032 and 2039** [E-9518].

**The counter-test, and why the attack still stands.** Three objections apply and none of them rescues the snapshot ceiling. The anchors use different inclusion rules, so the ratio bounds rather than measures growth [E-9517] — but every plausible tightening of the definition lowers both endpoints and leaves the doubling time roughly intact. Exponentials off small bases have been over-extrapolated in this exact field before, and the 2022 BCG projection [E-9516] is the cautionary case. And share is not effect: at an unchanged probability of success, a 50 percent share produces zero additional approvals. That last point is decisive for the *magnitude* of the effect and irrelevant to the *validity of the ceiling argument*, which is what is under attack.

**Verdict: 채택 — the consensus is wrong as written and must change.**

**Required change to the report.** Every statement of the form "AI-derived candidates are a low-single-digit share of INDs, which caps any system-level effect at low single digits" must be time-indexed. Replace with: *"AI-derived candidates are 1.0-3.4 percent of current annual IND flow, which caps the system-level effect at +0.6 to +2.7 percent relative on annual approvals **in 2026**. The cumulative count of AI-derived clinical-stage molecules has a doubling time of 1.2-2.1 years [E-9517]; at that rate the share crosses 10 percent between 2029 and 2033 and 50 percent between 2032 and 2039 [E-9518]. The base-rate ceiling is therefore valid for the 2030 horizon and invalid for the 2035 and 2040 horizons, and any bottleneck ranking for 2035 or 2040 that assumes a low AI share is unsupported."* The 2035 and 2040 rankings must carry this as an explicit stated assumption.

---

## X-09 — the "no evidence AI raised probability of success" verdict rests on a comparator that is not contemporaneous

**The attack.** Agent B compares the AI cohort's Phase II rate of about 40 percent against a conventional benchmark of about 37 percent and concludes there is no evidence of an effect. The 37 percent benchmark is historical. The contemporaneous Citeline programme-level Phase II transition rate is 28 percent [E-9513], on a dataset whose cumulative likelihood of approval fell from 10.4 to 6.7 percent over the same period [E-9512].

**The arithmetic.** Against 37 percent the difference is +3 points; against 28 percent it is +12 points [E-9537]. The comparator choice changes the apparent effect size fourfold and it changes the direction of the presumption. Agent B's power calculation, which requires about 4,126 per arm, is computed for a 3-point difference; for a 12-point difference the required n falls by roughly an order of magnitude and the observed n of 8 is far less absurdly underpowered, though still underpowered.

**Why this is not an argument that AI works.** Neither comparison is denominator-matched. The Citeline figure is a programme-level Phase II to Phase III transition; the AI figure's denominator was never disclosed, which Agent B correctly logs as unresolved. A comparison between two undefined denominators is not evidence in either direction. The correct conclusion is a statement about the absence of a matched comparison, not a statement about the absence of an effect.

**Verdict: 부분채택.**

**Required change to the report.** The heading "증거 없음 / NO EVIDENCE" must not stand unqualified over a claim about the effect. Replace the verdict sentence with: *"No adequately powered, denominator-matched comparison of AI-derived and conventional clinical probability of success exists in either direction. The published AI Phase II figure of about 40 percent is +3 points against the historical 37 percent benchmark and +12 points against the contemporaneous Citeline programme-level rate of 28 percent [E-9537][E-9513]; the choice of comparator, not the data, determines the apparent effect size. The evidentiary state is indeterminate, not null."* The report must state which comparator it uses wherever it quotes a benchmark success rate.

---

## X-10 — capital (B11) is a symptom of expected returns, not an independent constraint

**The attack.** B11 is ranked third. Capital is not a process step: it is an input whose supply responds to expected returns. If the marginal programme is not value-creating, then capital withdrawing from it is the market working, not a constraint binding. Agent C half-concedes this in a caveat and then leaves B11 at rank 3 anyway.

**The evidence.** Capital is not scarce in aggregate. The top 25 pharmaceutical companies held about USD 1.3 trillion of deployable capital entering 2026, one of the highest figures on record, and the 2025 dealmaking rebound did not materially deplete it [E-9526]. Chinese developers signed about 157 out-licensing deals with roughly USD 136 billion of disclosed value in 2025 against 94 deals and USD 51.9 billion in 2024 [E-9522] — capital moving fast toward assets it judges attractive. Meanwhile the number of novel targets entering the pipeline fell to 30 in 2024 from around 100 a decade earlier *despite* a doubling of the pipeline and a tripling of early- and mid-stage venture investment [E-9509]. More capital arrived and fewer novel bets were placed. That is close to a decisive disproof of capital-as-quantity-constraint: the marginal dollar was available and chose crowded targets.

**What survives.** Two of Agent C's three signals do survive as evidence of something real, but it is not capital scarcity. Approved products withdrawn for commercial reasons are evidence about *terminal value*, and the Inflation Reduction Act analysis showing an immediate reduction of 11.4 industry-sponsored trials plus a further 1.2 per month [E-9525] is evidence about *policy-set expected returns*. Both are the price signal, not the supply.

**Verdict: 부분채택.**

**Required change to the report.** B11 must be relabelled and its ranking annotated. Required text: *"B11 is not an independent capacity constraint. Aggregate capital is abundant — about USD 1.3 trillion of deployable capital at the top 25 pharmaceutical companies [E-9526] — and novel-target entry fell to 30 per year in 2024 while venture investment tripled [E-9509], so the marginal dollar was available and declined the novel bet. B11 should be carried as **expected terminal value**, an endogenous multiplier on every other bottleneck's elasticity, not as a rank-3 constraint in the same list. Its measurable channel is policy-set return, for which the cleanest estimate is the post-IRA step change of 11.4 fewer industry-sponsored trials [E-9525]."* If the report keeps a single ranked list, B11 must carry a footnote saying its elasticity is not additive with B1 and B8 because it acts through them.

---

## X-11 — B1's trend is not flat; target validation has been partly industrialised and the consensus misses it

**The attack.** Agent C scores B1's trend as "mixed to flat" and grounds it on replication-failure statistics — Amgen 6 of 53, Bayer roughly two thirds inconsistent. Those two anchors are from 2011 and 2012, neither discloses paper-selection criteria or protocols [E-9538], and both are among the most heavily re-cited and least re-derivable numbers in the field. Using them to establish a *trend* through 2026 is a category error: they are a level measurement from fifteen years ago.

**The evidence that the trend moved.** Human genetic support raises the relative probability of success 2.6-fold, and up to fourfold in haematology and metabolic disease [E-9507]. Crucially it is now the majority practice, not a research finding: genetic evidence supported 63 percent of the 428 new drugs approved by FDA in 2013-2022, with an annual range of 41-72 percent [E-9508]. Novel oncology target validation rose from about two per year in 2000-2004 to about ten per year in 2020-2024 [E-9511], and 1,578 potential first-in-class oncology drugs entered clinical development over 2009-2024 with a statistically significant rising trend [E-9510].

**[INFER]** B1's *rank* survives — it still sits on the largest attrition mass and it is still the least purchasable improvement. What does not survive is the claim that no improvement channel exists or that the trend is flat. There is a demonstrated 2.6-fold lever, it is being used in a majority of successful programmes, and its remaining headroom is the 37 percent of approvals that still lack genetic support [E-9508].

**Verdict: 부분채택.**

**Required change to the report.** The B1 trend cell must be changed from "mixed to flat" to "improving on the decision-quality channel, flat on the literature-reproducibility channel", and the report must add: *"Human genetic support is a measured 2.6-fold relative-success multiplier [E-9507] and already underpins 63 percent of 2013-2022 FDA approvals [E-9508]. The Amgen and Bayer replication statistics are level measurements from 2011-2012 with undisclosed selection criteria [E-9538] and must not be cited as evidence about the 2016-2026 trend."*

---

## X-12 — a discovery-stage improvement has moved the system before, and the consensus's strongest rhetorical line forbids that

**The attack.** The consensus repeatedly uses the formulation that discovery improved and system output did not move, therefore discovery is not a constraint. That inference is only valid if discovery-stage improvements *never* move system output. They have.

**The evidence.** Attrition attributed to poor pharmacokinetics and bioavailability fell from about 40 percent of clinical failures in 1991 to about 10 percent by 2000, following industry-wide adoption of in-vitro ADME and physicochemical property screening — a discovery-stage capability [E-9506]. An entire attrition class was removed by a discovery-stage tool. The uncomfortable corollary is that removing it did not raise approvals either, because efficacy and safety expanded to fill the space, which is precisely the Theory-of-Constraints prediction.

**Verdict: 부분채택.**

**Required change to the report.** The report must not use the formulation "discovery improved and output did not move, therefore discovery was never a constraint" without the Kola-Landis qualifier. Required text: *"A discovery-stage capability has removed an entire attrition class once before: pharmacokinetic failures fell from about 40 percent of clinical failures in 1991 to about 10 percent by 2000 [E-9506]. System output did not rise, because the constraint moved to efficacy and safety rather than disappearing. This is the correct precedent for what AI-driven discovery compression should be expected to do — relocate the constraint, not relieve it — and it means the observation that output has not risen is consistent with discovery having been a real, and now retired, constraint."*

---

## X-13 — candidate flow is routing to a jurisdiction whose capacity is growing, so the US-derived saturation ceilings understate the global ceiling

**The attack, which the orchestrator required.** Agents F and G derive saturation multiples from US capacity: US phase III participant throughput at −0.92 percent per year, the US investigator workforce at −3.97 percent per year, US-anchored manufacturing multiples of 1.06x to 10x. Agent E separately found China receives more INDs than the US with a 30-working-day clock. If candidate flow simply routes east, the ceilings are jurisdictional artefacts rather than physical limits.

**The evidence for the attack.** China's CDE recorded 4,900 registered trials in 2024, up 13.9 percent on 4,300 in 2023, which was up 26.1 percent on 3,410 in 2022, with a five-year average of about 16 percent per year; 2,539 were innovative-drug trials and 1,735 were new-to-world Category 1 products [E-9519]. China took 39 percent of global oncology trial starts in 2024 against the US at 32 percent, up from 5 percent in 2014; its share of global innovative-drug trials rose from 5 percent in 2016 to 30 percent in 2025 while the US fell from 45 to 33 percent; Chinese Phase I trials are reported 50 percent shorter and 43 percent cheaper, and the human-trial approval clock fell from 501 to 87 days [E-9520]. China's share of global innovative-drug approvals went from 3 percent in 2015 to 38 percent in 2024 [E-9521]. Capital has already priced this: 157 out-licensing deals worth about USD 136 billion in 2025 against 94 and USD 51.9 billion in 2024 [E-9522].

**The evidence against the attack.** Three counters, and together they are decisive on the strong form. First, the global aggregate is not expanding. Global clinical trial investigators fell from about 128,303 in 2017-18 to 116,948 in 2023-24 and coordinators from about 56,036 to 40,472 [E-9524]; annual new registrations on ClinicalTrials.gov are flat to declining — about 31,400 per year 2015-2020, 37,000 in 2021, 38,000 in 2022, about 31,200 per year 2023-2024 [E-9533]. China is growing inside a global total that is not. That is reallocation, not expansion. Second, the pivotal-evidence gate does not relocate. FDA's advisory committee voted 14 to 1 in February 2022 that a China-only pivotal trial required an additional US-applicable study, on population-generalisability grounds, and a complete response letter followed [E-9523]. Registrational evidence for a US approval still consumes US and multiregional site capacity, and only 337 of China's 2,539 innovative-drug trials in 2024 were multiregional [E-9519]. Third, the manufacturing ceilings Agent G derives are on shared physical inputs — GMP plasmid, aseptic fill-finish — which are global markets, not US ones, and do not move when a trial relocates.

**Verdict: 부분채택 — the ceiling on *early* clinical capacity is materially higher than the US-derived figure, and the ceiling on *pivotal* capacity and on shared manufacturing inputs is not.**

**Required change to the report.** Every saturation multiple and clinical-capacity ceiling must be labelled with its jurisdictional scope, and the following must be added wherever the clinical-operations ceiling is stated: *"These ceilings are derived from US capacity. First-in-human and early clinical capacity is not US-bound: China took 39 percent of global oncology trial starts in 2024 against the US 32 percent, with Phase I trials about 50 percent shorter and 43 percent cheaper and an 87-day trial-approval clock [E-9520], and Chinese registrations grew about 16 percent per year to 4,900 in 2024 [E-9519]. The early-phase ceiling is therefore materially higher than the US-derived figure. Two things do not relocate: pivotal evidence acceptable to FDA, since a China-only pivotal trial was rejected 14-1 by ODAC on generalisability grounds [E-9523] and only 337 of 2,539 Chinese innovative-drug trials in 2024 were multiregional [E-9519]; and shared manufacturing inputs, which are global markets. The binding clinical constraint is pivotal, multiregional trial capacity, not clinical capacity as such."* The report must also record that the global aggregate is not expanding — investigators −9 percent and coordinators −28 percent over six years [E-9524], flat registry inflow [E-9533] — so the eastward shift is substitution.

---

## X-14 — B15 is over-ranked, and the consensus contains an unresolved internal contradiction about it

**The attack.** Agent C ranks B15 (endpoint and biomarker qualification) equal fifth of sixteen, and grounds it on the FDA Biomarker Qualification Program's throughput: 61 projects accepted, 11 biomarkers ever qualified, a 32-month median to agree a plan. Agent E, working the same domain from primary regulatory sources, reports that FDA's public table of surrogate endpoints that have actually been the basis of an approval lists over 200 markers, and states in terms that the accepted set is two orders of magnitude larger than the qualified set. Both cannot support the same rank.

**The evidence.** I verified E's side independently: FDA has maintained the Table of Surrogate Endpoints That Were the Basis of Drug Approval or Licensure since 2018 and it lists over 200 surrogate markers [E-9528]. The qualification queue measures the throughput of the *portable, reusable* channel. It does not measure whether a sponsor can get a surrogate endpoint accepted for its own programme, and the 200-entry table is direct evidence that they routinely can.

**[INFER]** C measured the wrong resource. The scarce good is not "a qualified biomarker"; it is "a surrogate that predicts clinical benefit in this indication", and where such a surrogate exists FDA has accepted it roughly 200 times without requiring formal qualification. B15's elasticity is therefore closer to the low end of C's own 1.5-5 percent band, and its rank should fall.

**Verdict: 채택 — the consensus is internally inconsistent and must be resolved.**

**Required change to the report.** B15 must be moved from rank 5-equal to approximately rank 9-11, and the ranking table must carry: *"B15's constraint statistic is the qualification queue (11 biomarkers qualified against 61 accepted projects), which measures the portable, reusable channel only. The programme-specific channel is not congested: FDA's public table lists over 200 surrogate markers that have been the basis of an approval [E-9528]. Scarcity of surrogates is a scientific problem in slowly progressive disease, not a regulatory-listing problem."* The final report must not carry both C's rank-5 justification and E's 200-endpoint finding without reconciling them.

---

## X-15 — the raw-patient-pool slack argument against B3

**The attack.** Agent C observes about 7-8 percent trial participation among cancer patients and 56 percent of non-enrolment attributed to no trial being available locally, and infers pool slack. If that inference held, B3 would be a matching problem solvable with software rather than a capacity constraint.

**Why it fails.** Agent F already ran the decisive test and I could not break it. A deployed AI prescreening system read 98,348 charts across 29 trials, flagged 825 eligible patients and produced 117 enrolments — 0.12 percent yield — after cutting screening cost tenfold. Cheap exhaustive screening did not convert the pool. Independently, NCI-MATCH lost 8.6 percentage points of *already-matched* patients purely because the right arm was not open at that moment. Both hold screening effort constant and isolate slot availability. My own collection adds the supply-side corroboration from a different source than F used: global investigators fell about 9 percent and coordinators about 28 percent over six years [E-9524], and US trial starts fell about 15 percent in 2023 and more than 20 percent below the 2021 peak [E-9525].

**Verdict: 기각 — the consensus survives. Raw pool slack is real and is not the operative variable.**

**Required change to the report.** None. The report should retain F's formulation that the 56 percent figure measures the constraint rather than slack, and may cite the independent workforce series [E-9524] as corroboration from a non-overlapping source.

---

## X-16 — B2's pass-through cap is set on a statistic that has since moved

**The attack.** Agent C caps B2's pass-through parameter θ at 0.10-0.35 explicitly because zero new-approach methodologies had completed qualification against 16 projects in the pipeline. That premise is stale by the time Agent E's evidence is added.

**The evidence.** One tool has now completed full qualification — the AI-based histologic measurement of MASH, qualified 8 December 2025 — and CHMP issued its qualification opinion on the same tool in March 2025, nine months earlier. FDA's December 2025 draft guidance removes routine six-month non-human-primate studies for monoclonal antibodies in favour of weight of evidence, and the March 2026 draft sets four NAM validation principles. On the trial side, EMA opened a draft qualification opinion on virtual control groups on 31 March 2026 [E-9529], and FDA and EMA jointly issued ten Guiding Principles of Good AI Practice in January 2026 [E-9530]. Against that, in-silico evidence remains supplemental rather than substitutive [E-9530], and the EU's own animal-testing phase-out roadmap excludes biologicals, vaccines, gene therapies and ATMPs — exactly the modalities where animal models are least predictive.

**Verdict: 부분채택 — the rank survives, the justification does not.**

**Required change to the report.** The B2 entry must not state that zero tools have been qualified. Required text: *"One drug development tool has completed FDA qualification (AI-based histologic measurement of MASH, 8 December 2025), with the EMA opinion nine months earlier, and the replacement channel is now moving from zero. The pass-through cap on B2 should be raised at its lower bound accordingly, while remaining bounded by the fact that in-silico evidence is supplemental rather than substitutive [E-9530] and that the EU roadmap excludes ATMPs and biologicals."*

---

## X-17 — the spare-capacity and arbitrage attack on B7 (delivery)

**The attack.** If delivery were a binding constraint with high returns, capital would have arbitraged it away; billions have gone into delivery and the returns should show.

**Why it fails.** Agent G's decomposition holds against the arbitrage argument on the one sub-problem that matters most. Human solid-tumour antibody uptake of about 0.01 percent of injected dose per gram has not moved in a decade, and the governing mechanism — binding rate exceeding diffusion rate in a pressurised, convection-free interstitium — is worsened by the obvious fixes, since higher affinity binds faster and penetrates less. An arbitrage argument requires that money can buy the improvement; here the mechanism forecloses it. G's counter-case is equally strong in the other direction: the blood-brain barrier did yield to engineering, going from first bivalent shuttle publication to first approval of a receptor-mediated-transcytosis platform product in nine years. That is capital working, and G already books it as such.

**Verdict: 기각 — the consensus survives, including its split verdict.**

**Required change to the report.** None. The report should carry G's split verdict intact and must not collapse B7 into a single rank, because the two halves have opposite arbitrage properties.

---

## X-18 — the label-noise ceiling caps measured benchmark scores, not model capability

**The attack.** The consensus states that a label-noise ceiling caps achievable model accuracy, with R²max = 1 − σe²/σy² and an RMSE floor of 0.68 log units. The derivation assumes additive noise independent of the true value, and it computes a ceiling on *agreement with a noisy label*. Real discovery is a ranking and selection problem, and a model can rank correctly while scoring poorly against noisy labels. Agent H's own evidence says so: apparent error against noisy labels rises 2.9 to 55 times faster than true error.

**What survives.** The ceiling binds fully in one place, and H says so: when the assay that adjudicates the model is the noisy assay, the experimenter cannot distinguish a correct prediction from a lucky one. And Scannell's decision-theoretic result is unaffected by the objection, because it is stated in terms of correlation with *clinical* utility rather than with an assay label — a high-validity tool yields about 20 percent positive predictive value from 200 candidates while a low-validity tool yields about 5 percent from 30,000, and a 0.1 absolute change in that correlation offsets a 10-fold to 100-fold change in throughput [E-9527].

**Verdict: 부분채택.**

**Required change to the report.** The claim must be split. Required text: *"The label-noise ceiling (R²max = 1 − σe²/σy², RMSE floor 0.68 log units) is a hard bound on measured benchmark scores and on the resolving power of the experiment that adjudicates a model. It is not a bound on model capability, because apparent error against noisy labels rises 2.9 to 55 times faster than true error. The bound that does constrain system output is the decision-tool predictive-validity result: about 20 percent positive predictive value from 200 candidates at high validity against about 5 percent from 30,000 at low validity [E-9527]."*

---

## X-19 — a bottleneck ranked nowhere that belongs in the list: clinical development design (dose, endpoint, population)

**The attack.** The catalogue B1-B16 contains no entry for the sponsor's choice of dose, schedule, endpoint and population — the design decisions taken between a validated target and a pivotal trial. These are neither target validity (B1), nor toxicity prediction (B8), nor protocol operational burden (B16). They are a distinct, sponsor-controllable failure mode with measured incidence.

**The evidence.** FDA's Oncology Center of Excellence created Project Optimus in 2021 specifically because maximum-tolerated-dose selection was producing doses patients could not sustain; 48 percent of patients in Phase III of molecularly targeted agents required dose modification at the dose and schedule recommended by Phase I, and post-marketing dose changes were required for ceritinib, dasatinib, niraparib, ponatinib, cabazitaxel and gemtuzumab ozogamicin [E-9531]. Independently, of 640 novel therapeutics entering pivotal development, 344 failed and 74 of the failures were for commercial rather than scientific reasons [E-9515] — a further design-and-strategy failure class that no B-number captures.

**[INFER]** This factor has the profile the brief prizes: it acts on probability of success rather than only on time, it is measurable, it requires no new technology, and it is entirely within sponsor control. On those grounds it belongs in the same tractability tier as B16, and above it on elasticity because it acts on P rather than on T and C.

**Verdict: 채택 — a bottleneck candidate is missing from the catalogue and must be added.**

**Required change to the report.** Add **B17 — clinical development design: dose, schedule, endpoint and population selection**, distinct from B1, B8 and B16, with axes P and C, evidence anchored on [E-9531] and [E-9515], and a stated rank. The report must state explicitly that B17 was surfaced by the red team and was absent from the B1-B16 catalogue, so that the omission is visible rather than silently repaired.

---

## X-20 — "regulation is a net reliever outside the EU" is true only for marketing-authorisation regulation

**The attack.** Agent E's direction count across 80 mechanisms gives 44 relievers against 11 constraints and concludes net reliever, driven by China, Korea and the US. The scope of that count is marketing-authorisation and trial-authorisation regulation. Pricing and reimbursement regulation is a regulatory instrument too, and on the evidence it is the one with a measured negative effect on output in the United States.

**The evidence.** An interrupted time-series analysis of industry-sponsored trial activity found an immediate reduction of 11.4 trials plus a further 1.2 trials per month after passage of the Inflation Reduction Act [E-9525], and new trial starts fell about 15 percent in 2023 against 2022 and more than 20 percent below the 2021 peak [E-9525]. That is a US regulatory instrument with a measured, signed, negative effect on the count of programmes entering the clinic — the exact quantity the brief defines as system output. Agent C reports the industry-commissioned 68 percent small-molecule investment claim and correctly flags it as conflicted; the interrupted time-series result is a different and better-identified estimate pointing the same way.

**Verdict: 부분채택.**

**Required change to the report.** The net-reliever finding must be scoped. Required text: *"Regulation is a net reliever outside the EU **when 'regulation' is scoped to marketing- and trial-authorisation instruments**. Scoped to include pricing and reimbursement regulation, the US carries a measured negative: an interrupted time-series analysis finds an immediate reduction of 11.4 industry-sponsored trials plus 1.2 per month after IRA passage [E-9525]. The two findings are not in conflict; they concern different instruments, and the report must state which scope it is using at every point where the net-reliever conclusion appears."*

---

## Summary table

| ID | Attack | Target agents | Verdict |
|---|---|---|---|
| X-01 | Per-programme economics cannot see programmes never started; ~85% of the druggable genome untargeted | A, C | 부분채택 |
| X-02 | Phase II efficacy failure is a discovery-stage decision error observed late | A, B, C | 부분채택 |
| X-03 | Discovery genuinely was the constraint in antibacterials and for KRAS; H0-a is domain-conditional | A, B, C | 부분채택 |
| X-04 | Target-based discovery expanded and first-in-class output did not follow | A, C | 기각 |
| X-05 | "Clinical becomes the constraint" is a restatement, not a falsifiable prediction | all | 부분채택 |
| X-06 | Is there a path where clinical stops binding by 2040? | C, E, F | 기각 |
| X-07 | Is the 30-50% AI compression finding an artefact of comparator choice? | B | 기각 |
| X-08 | The low-share ceiling is a 2026 snapshot; doubling time is 1.2-2.1 years | B, C | **채택** |
| X-09 | The "no evidence on PoS" verdict uses a non-contemporaneous comparator | B | 부분채택 |
| X-10 | Capital is endogenous to expected returns, not an independent rank-3 constraint | C | 부분채택 |
| X-11 | B1's trend is not flat; genetic support is a used 2.6x lever | C | 부분채택 |
| X-12 | A discovery-stage tool removed an entire attrition class in 1991-2000 | A, B, C | 부분채택 |
| X-13 | Candidate flow routes to China; US-derived ceilings understate early-phase capacity | C, E, F, G | 부분채택 |
| X-14 | B15 over-ranked; C's 11-qualified statistic contradicts E's 200-accepted table | C, E | **채택** |
| X-15 | Raw patient-pool slack means B3 is not binding | C, F | 기각 |
| X-16 | B2's θ cap rests on a zero-qualifications premise that has since moved | C, E | 부분채택 |
| X-17 | Delivery would have been arbitraged away if it were binding | G | 기각 |
| X-18 | The label-noise ceiling caps measurement, not capability | H | 부분채택 |
| X-19 | Missing bottleneck: clinical development design (dose/endpoint/population) | C | **채택** |
| X-20 | "Regulation is a net reliever" holds only for authorisation instruments | E | 부분채택 |

**Totals: 채택 3, 부분채택 12, 기각 5.**

---
---

# PASS 2 — provenance audit, Agent I attack, X-14 adjudication, B17 evidence base

Evidence added: **E-9539 … E-9554** (16 records; block now E-9500 … E-9554, 55 records).
New deliverable: `RLSX/audit/circular_audit.csv` (572 rows, header as specified).
Search record for this pass: 18 further WebSearch/WebFetch calls, of which three were blocked (ASCO Publications 403, AACR Journals 403, NCBI 301 redirect handled by re-fetch) and each was replaced by an independently reachable carrier.

**Pass-2 verdict tally: 채택 4 / 부분채택 5 / 기각 1. Cumulative across both passes: 채택 7 / 부분채택 17 / 기각 6, over 30 findings.**

---

## X-21 — anchor faithfulness: three of the four named anchors are not faithful to their origins as commonly repeated

**The audit.** The common brief names four anchors for individual treatment. Each was traced hop by hop and the result is recorded in `circular_audit.csv` under a manual override, so the chain is auditable row by row.

**Anchor 1 — capitalized cost per approved drug (~USD 2.2-2.9 bn).** Origin reached **partially**. The hop chain resolves to DiMasi, Grabowski and Hansen, *Journal of Health Economics* 47:20-33 (2016), but not to its inputs: the 106-compound sample is a confidential survey of 10 firms that no third party can re-derive. **The number is faithful in value and unfaithful in framing**: it is quoted without the capitalized basis and the 10.5 percent discount rate that generate it, and the same authors' out-of-pocket figure is 1,395. Independent reanalyses of overlapping inputs give 985 million (Wouters, from SEC filings — the only member of this family whose origin is reproducible) and 59.4 million (Light and Warburton, net of tax relief). Verdict on the family: **unverifiable at origin**; FORCE_LOW on the per-stage split.

**Anchor 2 — clinical success 7-14 percent.** Origin reached **yes**, four times over: BIO/Informa/QLS, Hay 2014, Wong-Siah-Lo 2019 and Paul 2010, each with a disclosed denominator. **The range is faithful; any point estimate drawn from it is not**, because the four origins use incompatible denominators (drug-indication-sponsor paths, registration-enabling programmes, lead indications, merged programmes). The contemporaneous Citeline series used in X-09 is a separate object and is **unverifiable**: it is a proprietary database whose cohort definition is undisclosed in every accessible carrier.

**Anchor 3 — total development 10-15 years, discovery 3-6 years.** Origin reached **yes**, three times: DiMasi's 128-month synthesis-to-approval clock, Sertkaya's 147-month model, and Brown's 9.1-year clinical span. **The commonly repeated 10-15 year band is unfaithful to all three.** No source in the ledger measures 10-15 years; the band is a rounded trade convention assembled from clocks that start in different places. This is the clearest case in the audit of a number that everyone repeats and no one sourced.

**Anchor 4 — AI Phase I 80-90 percent.** Origin reached **partially**: Jayatunga et al., *Drug Discovery Today* 29(6):104009, June 2024, located and dated, paywalled, no open-access deposit. The Phase I denominator, the Phase II denominator, the company list and the operational definition of "AI-discovered" are undisclosed **at origin**, not merely in relay. All five authors are Boston Consulting Group and the work was BCG-funded, so S4 attaches at the origin itself. Agents B and C independently imported the same unresolvable origin, which is textbook cross-agent recurrence. **Faithful in value, unfaithful in use**: it is quoted as a success rate without its denominator. FORCE_LOW.

**Verdict: 채택.**

**Required change to the report.** Anchor 3 must be corrected, not merely qualified. Every use of "10-15 years" must be replaced by the measured figure with its clock stated: *"Measured development duration is 128 months synthesis-to-approval (DiMasi), 147 months (Sertkaya) and 9.1 years of clinical development (Brown). The frequently quoted 10-15 year range corresponds to no measurement in the ledger and must not be used."* Anchors 1, 2 and 4 must each carry a one-clause faithfulness statement at first use, in the form given above, and Anchor 4 must never appear without its denominator being described as undisclosed at origin.

---

## X-22 — two fifths of the quantitative ledger cannot be traced to a reproducible origin in three hops

**The audit.** All 572 records carrying a figure were enumerated and adjudicated; coverage is 572 of 572. Tier composition: tier 1 (collector-flagged `circular_risk`) 92 rule-adjudicated plus the flagged records absorbed into manual traces; tier 2 (`market_report` and `secondary`) 117; tier 3 (cross-agent recurrence on the same source title) 12; tier 4 (remainder) 318; plus **33 rows carrying a manual, hop-by-hop origin trace performed in this pass**.

**Method disclosure, because it bears on how much the result is worth.** The 33 manual rows were traced by retrieving the origin. The remaining 539 were adjudicated by a stated rule applied uniformly and written into the `notes` column of every row: the deepest provenance hop is classified into peer-reviewed, preprint, agency, registry, filing, consultancy, company, trade press, aggregator or none, and the verdict follows from that class plus the collector's own `circular_risk` flag. This classifies the **provenance chain**; it does not re-verify each figure at its origin. That distinction is stated here rather than left for a reader to infer.

**Result** [E-9551]: **340 clean, 157 unverifiable, 75 circular. 232 of 572 records (40.6 percent) carry a FORCE_LOW marker** in the `notes` column, meaning no origin was reachable within three hops and Agent R must grade them Low. Thirty-eight shared-origin groups were identified; the four largest contain 17, 17, 16 and 11 records respectively.

**[INFER]** A 59 percent clean rate is not a scandal for a ledger of this size and it is materially better than the field's published norm. But 232 records is a large enough set that conclusions must be checked against it rather than assumed to survive it.

**Verdict: 채택.**

**Required change to the report.** The report must carry a provenance statement and must honour it mechanically: *"Of 572 quantitative records, 340 are provenance-clean, 157 unverifiable and 75 circular; 232 are marked FORCE_LOW in `RLSX/audit/circular_audit.csv` and are graded Low [E-9551]."* No sentence in the report may rest solely on a FORCE_LOW record, and any that does must carry the ⚠ LOW-EVIDENCE CLAIM banner. Agent R must take the FORCE_LOW column as binding so that the audit and the grading do not disagree.

---

## X-23 — sixteen ledger records present as quantitative and carry no auditable quantity

**The attack.** The ledger schema states that `figures.value` must be a JSON number or null. Sixteen records violate it by carrying a string: twelve from Agent G, mostly empty strings, and four from Agent F, categorical strings such as a regulatory acceptance status [E-9552]. These records pass a naive "has a figure" filter and fail any arithmetic use.

**Consequence.** The corrected count of records carrying a genuine numeric figure is **556, not 572**. Every denominator computed over "records with a figure" is off by 16.

**Verdict: 부분채택.** The defect is real and mechanical, and it does not change any substantive conclusion.

**Required change to the report.** Where the report states ledger statistics it must use 556 as the count of numeric records and note the 16 non-conforming records. The 16 rows are flagged with a leading `SCHEMA DEFECT` string in `circular_audit.csv` so the correction is checkable by grep.

---

## X-24 — Agent I's TRL ratings are mostly disciplined, with one two-level inflation and one category error

**The attack.** I rated 81 technologies with 22 at TRL 7 and 12 at TRL 8. I tested all twelve TRL 8 ratings against I's own published scale, in which TRL 8 requires "a formal decision behind it (a qualification, an approval, an in-force rule)" and TRL 7 is pivotal-stage use without regulatory acceptance.

**T-072, minimal residual disease, rated TRL 8 — inflated by two levels, and internally inconsistent.** The stated basis is an advisory committee vote and a draft guidance. The advisory vote is non-binding; the January 2026 document is *draft*, with comments closing 23 March 2026; and no drug has been approved with MRD as the primary endpoint [E-9548]. Under I's own scale that is TRL 6, "accepted into a regulatory pathway". The inconsistency is decisive: I rates stride velocity at 7 rather than 8 *because* FDA has qualified zero sensor-derived endpoints, then rates MRD at 8 on a record that also contains zero qualifications and zero approvals. The entry is also mistitled — it calls MRD "a qualified intermediate endpoint" and MRD is not qualified. T-072 is ranked sixth in I's highest-expected-value table, so the error is load-bearing.

**T-017, community and rural site network expansion, rated TRL 8 — category error.** The stated basis argues that over 80 percent of US research sites report staffing shortages and that "capacity is demonstrably below need" — an argument that the thing does *not* operate at the required scale — and then assigns the rating reserved for real-world operation with a formal decision behind it. The commercialisation window of 2026-2035 is also inconsistent with a TRL 8 rating. I's own B3 prose concedes the point, calling community site capacity "a labour problem (B13), not a technology". A labour shortage does not have a technology readiness level.

**T-035, TfR blood-brain-barrier shuttles, rated TRL 8 — correct rating, wrong basis.** The basis cited is trontinemab's Phase 3 status, which under I's scale supports 7, not 8. The fact that does support 8 is one I missed: Denali's TfR1 transport-vehicle product tividenofusp alfa received FDA accelerated approval on 25 March 2026, which is a formal decision, and it sits in Agent G's evidence rather than I's.

**T-026, cell-free enzymatic DNA, rated TRL 8 — confirmed.** I verified independently: FDA drug master file accepted 2022, first FDA IND clearance using dbDNA February 2023, first cell-free DNA GMP licence 2025, benchtop kit with New England Biolabs March 2026, first UK patient dosed July 2026 in a ten-participant Phase I [E-9547]. TRL 8 holds, and I correctly states why it is not 9. The defect is in the *ranking* justification, not the TRL: I places it fourth on expected value describing it as the shared input to every viral vector, mRNA and cell therapy product simultaneously, when its clinical footprint as of August 2026 is one ten-patient Phase I.

**The other eight TRL 8 ratings — T-002, T-014, T-016, T-018, T-044, T-058, T-059, T-063 — survived the test**, each with a stated basis and an explicit reason for not being 9.

**Verdict: 부분채택.** One inflation in twelve is a low rate; the catalogue is more disciplined than technology scouting normally is, and saying so is part of the finding.

**Required change to the report.** Three specific edits, each checkable against the CSV: (1) **T-072 TRL must be changed from 8 to 6** and the technology renamed from "MRD as a qualified intermediate endpoint" to "MRD as a proposed intermediate endpoint (draft guidance stage)", with the note that zero approvals have used it [E-9548]; its position in the highest-expected-value table must be re-derived after the change. (2) **T-017 must either be removed from the technology catalogue or carry `trl` = not-applicable** with a note that it is a labour-capacity constraint rather than a technology, consistent with I's own B3 text. (3) **T-035's `trl_basis` must be amended** to cite the March 2026 accelerated approval of a TfR1 transport-vehicle product as the formal decision supporting TRL 8, rather than trontinemab's Phase 3 status, which supports only TRL 7.

---

## X-25 — the milestones are dated but only a third are falsifiable within three years, and seven have no numeric threshold

**The attack.** The orchestrator's hypothesis is that some decisive milestones cannot be falsified in three years. I tested all 81.

**What I found, in I's favour.** Every one of the 81 milestones carries an explicit "checkable by <year>" clause. That is unusually good practice and the catalogue deserves the credit.

**What survives the attack.** The horizon distribution is 27 checkable by 2029, 26 by 2030, 23 by 2031, 4 by 2032 and 1 by 2033. **Only 27 of 81 (33 percent) are falsifiable inside three years**, so two thirds of the catalogue cannot be scored against reality before the 2030 horizon the mission asks about. Separately, seven milestones state an unquantified comparative threshold — "materially lower", "measurably", "materially better" — with no number attached: **T-016, T-017, T-024, T-034, T-059, T-070 and T-076**. A milestone that requires a judgement call about whether a change was "material" is adjudicable but not mechanically checkable, which is the standard the orchestrator set.

**Verdict: 부분채택.**

**Required change to the report.** Each of the seven named entries must have a numeric threshold attached to its `decisive_milestone` field — for example, T-076 must state the qualification count that constitutes "materially above its historical single-digit rate", and T-059 must state the share of royalty-financing volume in pre-approval assets that counts. The report must also state, wherever the technology roadmap is used, that only a third of the milestones resolve before 2030.

---

## X-26 — Agent I's "no credible technological solution for B1" is too strong: cis-pQTL Mendelian randomisation is a causal human instrument

**The attack.** I's negative claim rests on one sentence: the only instrument that validates a target in humans is a clinical trial, so a technology that needs a trial to prove it can replace trials has not solved B1. That sentence excludes a class of instrument that exists and is scaling.

**The evidence.** Cis-protein-quantitative-trait-locus Mendelian randomisation uses a genetic variant that alters the level of a specific protein as an instrumental variable, which is a randomised natural experiment *in humans* and does not require a trial. The resource base has industrialised: the UK Biobank Pharma Proteomics Project measured about 2,940 plasma proteins in 34,557 participants [E-9549], and proteome-wide MR screens against disease outcomes are now routine. This is precisely the "causal readout in humans" that I says does not exist.

**What survives, in I's favour, and it is substantial.** I's own strongest evidence runs directly against the instrument: across 11,482 target-indication pairs, Mendelian randomisation significance on its own did **not** enrich for Phase II success, while GWAS support did. So the one empirical test of whether this instrument predicts clinical outcome returned a negative result for MR specifically. The instrument is causal in principle and, on the only available test, not yet predictive in practice — which is a different objection from I's, and a better one.

**Verdict: 부분채택.**

**Required change to the report.** I's sentence "the only instrument that validates a target in humans is a clinical trial" must be replaced by: *"Cis-pQTL Mendelian randomisation is a causal human instrument that does not require a trial, and its resource base has industrialised to about 2,940 proteins in 34,557 participants [E-9549]. It is nonetheless not yet a solution to B1, because the one published test of predictive performance found that MR significance alone did not enrich for Phase II success while GWAS support did. The objection to the instrument is empirical, not conceptual."* Proteome-wide MR should be added to the B1 technology list as a distinct entry from T-002, at a TRL no higher than 6.

---

## X-27 — Agent I's "no credible technological solution for B11" misses an in-force, at-scale payment instrument

**The attack.** I concludes there is no instrument on any horizon that changes a payer's willingness to pay, and that its best candidate, the CMS outcomes-based model, addresses one disease and is unevaluated.

**The evidence.** The NHS antimicrobial products subscription model is the first delinked payment model for medicines anywhere: piloted from July 2022, scaled in the May 2024 UK antimicrobial resistance action plan, with contracts tendered in August 2024 at an estimated GBP 1.9 billion over 16 years and an annual budget of about GBP 100 million, paying a fixed fee independent of volume against supply, stewardship and surveillance performance [E-9550]. It is in force, it is procuring, and it directly changes a payer's willingness to pay in the one domain where the terminal-value constraint is most acute — the same domain where finding X-03 established that discovery was genuinely rate-limiting [E-9503][E-9504]. I's catalogue has an advance-market-commitment entry at TRL 7 with a 2027-2034 window, which is a less mature description of a mechanism that has already been contracted.

**Verdict: 부분채택.** I's structural point — that B11 is an institutional-design problem and not a laboratory-tool problem — survives and is correct. The blanket "no credible solution" does not.

**Required change to the report.** Add the NHS antimicrobial subscription model as a B11 technology entry at TRL 8, with the August 2024 tender as the formal decision anchoring the rating and a decisive milestone of the form "the number of antibacterial candidates entering Phase 1 from companies holding or eligible for subscription contracts rises above its 2019-2023 baseline; checkable by 2030" [E-9550]. The sentence "there is no laboratory technology on any horizon that changes a payer's willingness to pay" must be narrowed to "no laboratory technology", with the delinked-payment counterexample stated in the same paragraph.

---

## X-28 — Agent I's "no credible technological solution for B13" survives

**The attack.** I searched for a technology that produces experienced people faster than time does, on the theory that a false negative here would be consequential.

**Why it fails.** Nothing was found. The candidate classes are training consortia, which operate at cohort sizes in the dozens against vacancies in the thousands; automation, which converts a technician shortage into a scarcer automation-engineer shortage; and AI copilots, whose most plausible failure mode is to erode the judgement that constitutes absorptive capacity. Independent corroboration from my own pass-1 collection points the same way: global clinical trial investigators fell about 9 percent and site coordinators about 28 percent over six years [E-9524], during a period of heavy investment in trial technology. The tooling improved and the workforce shrank.

**Verdict: 기각 — I's negative claim on B13 is correct and should be retained verbatim.**

**Required change to the report.** None. The report should carry I's B13 negative finding and may cite [E-9524] as independent corroboration from a non-overlapping source.

---

## X-29 — adjudication of the X-14 contradiction: two agents counted two different objects under one word

**The question.** Agent C reports roughly eleven qualified biomarkers; Agent E reports a table of roughly two hundred accepted items. Which is right.

**The finding: both numbers are right for their own object, and neither agent stated which object it was counting.**

*Object 1 — biomarkers formally qualified through FDA's Biomarker Qualification Program.* The peer-reviewed analysis of the programme's own records gives **eight qualified as of 1 July 2025**, of which **seven were qualified before the 21st Century Cures Act of 2016** under the legacy process, with the most recent qualification granted in **2018**; 61 of 99 projects were accepted, 30 of those 61 (49 percent) never advanced past the letter of intent, median qualification-plan development ran 32 months and 47 months for surrogate endpoints, and **no project including a surrogate endpoint has ever achieved qualification** [E-9545]. Agent C's figure of eleven is 8 plus the three qualifications C separately records for November-December 2025, so **C's arithmetic is correct** and the three late-2025 qualifications represent a genuine break in a seven-year drought.

*Object 2 — entries in FDA's Table of Surrogate Endpoints That Were the Basis of Drug Approval or Licensure.* The peer-reviewed analysis of the table establishes that it is organised as **disease-or-use by patient-population by surrogate-endpoint pairings**, with a column stating whether each pairing supports accelerated or traditional approval, and that it covers surrogate endpoints in use across more than 100 such combinations at its sixth update, growing past 200 entries by 2025 [E-9546][E-9528]. **These are pairings, not distinct markers**, and the set includes both validated and reasonably-likely surrogates.

**Which usage was wrong.** Both, in different ways, and the errors are not symmetric.

- **Agent C's usage is the substantive error.** C used the qualification count as the constraint statistic for B15 and ranked B15 fifth of sixteen on that basis. The qualification channel is the *portable, programme-independent* channel, and the new evidence shows industry has routed around it almost entirely: eight qualifications in the programme's history, seven of them pre-2016, and zero surrogate endpoints ever qualified [E-9545], against more than 200 disease-population-endpoint pairings that have actually supported approvals without qualification [E-9546]. C measured the throughput of a channel that is nearly unused and treated it as the scarcity governing endpoint availability.
- **Agent E's usage carries a lesser, descriptive error.** E writes "over 200 surrogate markers". They are not 200 distinct markers; they are 200-plus disease-use-population pairings, and the count of distinct markers is materially smaller. E's substantive inference — that surrogate scarcity is not primarily a regulatory-listing problem — is correct and is strengthened by the new evidence.

**Verdict: 채택.** This supersedes and refines X-14; the direction of X-14 stands and the mechanism is now established rather than inferred.

**Required change to the report.** Three edits, all checkable. (1) The report must never use the bare word "qualified" for these objects. It must write **"formally qualified through the Biomarker Qualification Program (8 as of 1 July 2025, 11 including the three qualified in November-December 2025)"** and **"disease-use-population pairings in FDA's Table of Surrogate Endpoints (over 200)"**, and must state that the second set was reached without qualification. (2) The B15 constraint statistic must be changed from the qualification count to the pairing count, and **B15 moved from rank 5-equal to approximately rank 9-11**, per X-14. (3) The report must state the fact that most sharpens the picture: **no surrogate endpoint has ever completed formal qualification** [E-9545], so the qualification channel has never once delivered the object B15 is about, while the informal channel has delivered it more than 200 times.

---

## X-30 — B17 clinical development design: evidence base and matrix placement

**Current-state metric.** In a series of 286 early-phase oncology protocols activated over 2021-2023 at one large research institute — 268 unique, 215 first-in-human, 179 sponsors — backfill cohorts were specified in 73 percent of protocols [E-9539]. On the dose limb, 48 percent of Phase III patients on molecularly targeted agents required dose modification at the dose and schedule recommended by Phase I, and post-marketing dose changes were required for six named marketed oncology drugs [E-9531].

**Trend.** Improving, and attributable to a specific regulatory intervention. Backfill-cohort specification rose from 60 percent in 2021 to 77 percent across 2022-2024, and FDA's 2024 final dose-optimisation guidance recommends carrying two dose levels into Phase II with a randomised dose comparison before or within the registrational trial [E-9540]. This is the only bottleneck in the catalogue whose trend can be attributed to a dated policy act.

**Direct evidence that it binds — that improving it raises output, not merely that it is done badly.** Two independent limbs, and one disciplining counter-case.
- *Population definition.* Across 17,368 development trajectories spanning 2000-2015, programmes using biomarker-guided patient selection succeeded at 10.7 percent against 1.6 percent without [E-9541]. This is a design decision taken before the pivotal trial, not a property of the molecule. Two further datasets already in the ledger agree on the direction at a smaller magnitude — biomarker-selected 15.9 against 7.6 percent, and 10.3 against 5.5 percent — so the effect is replicated across three independent samples at roughly two-fold, with the 6.7-fold figure the outlier.
- *Endpoint choice.* FDA's January 2026 draft guidance would allow MRD negativity and complete response as primary endpoints supporting accelerated approval in myeloma, following a 12-0 advisory vote [E-9542]. Changing the endpoint changes what a trial must demonstrate and therefore whether it is feasible at all.
- *The counter-case, which bounds the elasticity.* Sotorasib's FDA-required randomised comparison of 960 mg against 240 mg in 209 patients found the higher dose numerically better on response (32.7 against 24.8 percent) and on duration of response; the requirement was deemed fulfilled in December 2023 and the original label was retained [E-9543]. A rigorous design exercise can return no gain, and the elasticity band must not be set as though every design review finds an error.

**Verdict: 채택 — B17 meets the same evidentiary standard as the existing sixteen and can enter the matrix.**

**Matrix fields.**
- **Axes:** **P primary, C secondary.** It changes whether a programme succeeds, and secondarily what it costs, by moving spend out of pivotal trials that were designed to fail. It is not a T-axis factor: Project Optimus-compliant designs are explicitly longer and more expensive per programme.
- **Elasticity:** **2 – 4 – 7** percent change in annual approvals per 10 percent improvement [E-9544], on Agent C's probability-channel formula with PoS = 0.12, f = 0.15-0.25 and θ = 0.20-0.40. θ is set above B1's because design choices are observable and controllable before the trial, unlike target validity; f is held below B1's to avoid double-counting target-driven efficacy failure.
- **Modality variance:** Hardest on **oncology small molecules and ADCs**, where the maximum-tolerated-dose paradigm was the default and payload therapeutic windows are narrow. Hard on **cell and gene therapy**, where dose is a cell or vector-genome count that cannot be titrated after administration and the population is defined by a genotype fixed at enrolment. Moderate on **antibodies**, where saturation pharmacology makes dose selection more forgiving. Least binding on **vaccines**, where dose and endpoint conventions are standardised and immunogenicity bridging is accepted. **RNA therapeutics** sit between antibodies and small molecules, with the population limb dominating in monogenic indications.
- **Rank:** **4th of seventeen**, between B8 (elasticity 6) and B2 (elasticity 4), and above B2 on tractability because it requires only a sponsor decision plus an existing regulatory framework rather than a new scientific method. Note the interaction that must be stated wherever the rank is used: B17's population limb overlaps B4, and its elasticity is not additive with B1, B4 or B8.

**Required change to the report.** Add B17 to the bottleneck catalogue and to the consolidated ranking with the four fields above, and state explicitly that it was surfaced by the red team and was absent from B1-B16. The ranking table must carry the non-additivity note.

---

## Pass-2 summary table

| ID | Attack | Target | Verdict |
|---|---|---|---|
| X-21 | Anchor faithfulness: 10-15 year duration anchor matches no measurement; three of four anchors unfaithful as repeated | A, B, C, all | **채택** |
| X-22 | 232 of 572 quantitative records unreachable to origin in three hops; 157 unverifiable, 75 circular | all | **채택** |
| X-23 | 16 records violate the ledger schema and carry no auditable quantity | F, G | 부분채택 |
| X-24 | TRL inflation: T-072 MRD rated 8, is 6 by I's own scale; T-017 is a labour problem with a TRL | I | 부분채택 |
| X-25 | Only 27 of 81 milestones checkable by 2029; 7 have no numeric threshold | I | 부분채택 |
| X-26 | B1 negative claim too strong: cis-pQTL MR is a causal human instrument | I | 부분채택 |
| X-27 | B11 negative claim misses the in-force NHS antimicrobial subscription model | I | 부분채택 |
| X-28 | B13 negative claim: searched for a counter and found none | I | 기각 |
| X-29 | X-14 adjudicated: 8 formally qualified vs 200+ disease-population pairings; C's usage is the error | C, E | **채택** |
| X-30 | B17 evidence base and matrix placement: axes P;C, elasticity 2-4-7, rank 4 of 17 | C | **채택** |

**Pass 2: 채택 4, 부분채택 5, 기각 1. Cumulative: 채택 7, 부분채택 17, 기각 6.**
