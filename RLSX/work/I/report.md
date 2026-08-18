CHARTER_ACK: R1,R2,R3,R4

# Agent I - Breakthrough Technology Scouting

**Scope executed.** 81 candidate technologies across all sixteen bottlenecks (B1-B16), against a mandated floor of 70. Every technology carries all seven mandatory fields plus attacked axis, dependency and modality scope in `RLSX/data/breakthrough_candidates.csv`. 106 evidence records, E-8001 to E-8106, in `RLSX/evidence/parts/I.jsonl`, all with `graded_by:null` and `confidence:null` for Agent R.

## 1. Methodology

**Search.** 36 WebSearch calls executed between the bottleneck matrix read and the first CSV write, covering: NAM regulatory status; virtual cell models and perturbation atlases; human genetics target validation; in vivo CAR-T; BBB shuttles; ML capsid engineering; enzymatic DNA; AAV producer cell lines; rapid CAR-T manufacture; immunogenicity prediction; liver MPS/DILI; AI trial prescreening; MRD and ctDNA endpoints; CMS gene therapy payment; digital twins; self-driving labs; n-of-1 ASO; AI inventorship; DNA synthesis screening; FDA Elsa and CNPV; federated learning; SORT LNP; continuous fill-finish; organoid predictivity; in vivo CRISPR screens; focused ultrasound; decentralised trials; protocol digitisation; digital endpoints; master protocols; biotech financing instruments; droplet microfluidics; AI toxicity models; workforce consortia; patent thickets; continuous bioprocessing; FDA AI/ICH E6(R3)/RWE guidance; solid-tumour penetration; site capacity and registry trials; ADC conjugation; newborn genomic screening; AI biosecurity; EU HTA; Human Cell Atlas. No technology in the catalogue rests on recalled facts; every TRL rating is anchored to a retrieved, dated source.

**How TRL was anchored.** Each rating is pinned to an observable milestone, not to a developer's own readiness claim. The scale applied here:

| TRL | Anchor used in this catalogue |
|---|---|
| 1-2 | Mechanism proposed in literature; no working instance |
| 3 | Proof of concept in one publication or one case study; result not reproduced by a third party |
| 4 | Component validation in the laboratory; works on the developer's own problem set |
| 5 | Validated in a relevant environment - real biological samples, real clinical data, real GMP constraints |
| 6 | Demonstrated in a relevant environment at scale: first-in-human, pilot-scale GMP, or accepted into a regulatory pathway |
| 7 | Operating in the real environment: pivotal trials, commercial GMP supply, routine third-party service - **but not regulatorily accepted as substitutive evidence** |
| 8 | In real-world regulatory or commercial use with a formal decision behind it (a qualification, an approval, an in-force rule) |
| 9 | Proven in routine operations, used by third parties as the default, with no remaining acceptance question |

For therapeutic-adjacent technologies the line between 7 and 9 is regulatory acceptance plus routine third-party use, as instructed. This is why humanised-immune-system mice sit at 7 despite twenty years of commercial availability [E-8085]: agencies do not accept the data in place of the required study. It is also why stride velocity 95th centile sits at 7 rather than 8 in the US sense - EMA qualified it in July 2023, FDA has qualified zero sensor-derived endpoints across 1,021 wearable-using trials [E-8078][E-8080].

**Company self-claims are demoted, not adopted.** Where a company states its own platform's readiness, the record is `type:"secondary"` with the company in `authors_or_org` so Agent R can apply S4 (conflict of interest). Examples: Touchlight's GMP licence claim [E-8020], Voyager's transduction percentages [E-8018], Dyno's 1.9x claim [E-8019], EpiVax's ADA correlation improvement [E-8029], Lonza's 72-hour workflow [E-8025], Benchling's 89 percent copilot statistic [E-8069]. None of these set the TRL; in each case the TRL is set by an independently observable event (a clinical trial registration, a peer-reviewed paper, a regulatory action).

**Axis assignment rule.** A technology attacks P when it changes whether a programme succeeds, C when it changes what a fixed programme costs, T when it changes how long a fixed programme takes. A technology that shortens a step already running with spare capacity is flagged LOW-VALUE in the `notes` column regardless of TRL, per the core definition in the common brief.

## 2. Technology entries by bottleneck

Full seven-field detail for every entry is in `RLSX/data/breakthrough_candidates.csv`. The tables below give the decision-relevant summary; the prose under each table states the finding that the table cannot carry.

### B1 - Target validation / translational validity of target biology

*Agent C matrix: provisional rank 1, elasticity point estimate 10. Technologies scouted: 6.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-001 | Virtual cell foundation models (perturbation-response transformers) | 3 | P | 2031-2038 | B10;B9 | E-8005, E-8006, E-8008 |
| T-002 | Human-genetics-anchored target selection (GWAS + colocalisation + Mendelian randomisation + ML integration) | 8 | P | 2015-2026 | - | E-8009, E-8010 |
| T-003 | In vivo spatially resolved pooled CRISPR screening (Perturb-DBiT, Perturb-Multimodal) | 4 | P | 2029-2035 | B7 | E-8011, E-8012, E-8087 |
| T-004 | Genome-scale Perturb-seq in primary human cells | 5 | P | 2027-2032 | B9;B10 | E-8087, E-8012 |
| T-005 | Chemical-genetic perturbation atlases as an industrial data factory (Tahoe Mosaic-class) | 6 | C;P | 2026-2030 | - | E-8006, E-8007 |
| T-006 | Cross-tissue 3D spatial human reference atlases (Human Cell Atlas, HuBMAP) | 6 | P | 2028-2034 | - | E-8013 |

B1 carries the highest elasticity in Agent C's matrix (point estimate 10) and has exactly one mature technology attacking it: human-genetics-anchored target selection at TRL 8 [E-8009][E-8010]. Everything else here is TRL 3-6. [INFER] That asymmetry - the highest-value bottleneck served by one technology that predates the AI wave and five that are a decade from a clinical readout - is the single most consequential structural fact in this catalogue. Note also the negative result inside the strongest evidence: Mendelian randomisation significance on its own did **not** enrich for Phase II success across 11,482 target-indication pairs; GWAS support did [E-8009]. That is a direct caution against treating 'has genetic evidence' as one undifferentiated signal.

### B2 - Preclinical-to-clinical translation (animal model predictivity, NAM validation)

*Agent C matrix: provisional rank 4, elasticity point estimate 4. Technologies scouted: 6.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-007 | Liver microphysiological systems for drug-induced liver injury inside the FDA ISTAND pathway | 6 | C;P | 2027-2032 | B5 | E-8003, E-8030, E-8001 |
| T-008 | Multi-organ body-on-chip with linked pharmacokinetic scaling | 4 | C;P | 2030-2038 | B5;B2 | E-8001, E-8095 |
| T-009 | Patient-derived organoid co-clinical response prediction | 5 | P | 2027-2033 | - | E-8083 |
| T-010 | Immune-competent organoids and lymphoid organoid systems | 3 | P | 2031-2039 | - | E-8084 |
| T-011 | Humanised-immune-system mice (HIS mice, HLA-transgenic models) | 7 | P | 2016-2026 | - | E-8085 |
| T-012 | NAM regulatory acceptance framework as an institutional technology (FDA NAM guidance, animal-testing roadmap, FDA Modernization Act 3.0) | 6 | T;P | 2026-2032 | B5 | E-8001, E-8002, E-8004 |

Two things moved in 2025-2026 that were not true before: FDA published a roadmap for reducing animal testing [E-8002] and issued draft guidance defining four validation principles for NAMs [E-8001], and FDA Modernization Act 3.0 passed both chambers [E-8004]. [INFER] The binding constraint in B2 has therefore shifted from 'do human-relevant assays exist' to 'will a regulator accept one in place of the animal study, and will a sponsor go first'. The liver MPS is three years past its ISTAND letter of intent [E-8003] and is still at step one of three. The technology entries here are ordered by how much of their remaining risk is scientific versus institutional; for T-007 and T-012 it is mostly institutional.

### B3 - Clinical trial patient recruitment / site capacity

*Agent C matrix: provisional rank 7, elasticity point estimate 2.5. Technologies scouted: 5.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-013 | LLM-based EHR prescreening and trial matching (TRIAGE-class systems) | 7 | T | 2024-2027 | - | E-8034, E-8035, E-8091 |
| T-014 | Registry-based and embedded pragmatic randomised trials | 8 | T;C | 2014-2026 | B15 | E-8038, E-8092 |
| T-015 | Decentralised and hybrid trial operations (home nursing, direct-to-patient supply, televisits) | 7 | T;C | 2021-2028 | B5;B13 | E-8036, E-8037, E-8048 |
| T-016 | Federated real-world data networks for feasibility and site selection | 8 | T;C | 2018-2026 | B10 | E-8036, E-8049 |
| T-017 | Community and rural site network expansion with protocol-burden reduction | 8 | T;C | 2026-2035 | B13;B16 | E-8039, E-8091 |

The strongest single result in this section is a negative one: a randomised evaluation in 355 charts found human-plus-AI prescreening matched or improved accuracy and did **not** improve efficiency [E-8035]. Separately, 59 percent of sites report losing patients before the screening step at all [E-8091] and over 80 percent report staffing shortages [E-8039]. [INFER] Taken together these locate the recruitment constraint upstream of eligibility determination, in referral flow and staffed site capacity - which is exactly where the AI tools do not operate. The two entries with genuine leverage here are registry-based randomisation [E-8038] and community site capacity, and the second is a labour problem (B13), not a technology.

### B4 - Patient-pool fragmentation from precision medicine

*Agent C matrix: provisional rank 10, elasticity point estimate 1.2. Technologies scouted: 4.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-018 | Master protocols: basket, umbrella and platform trials with shared controls | 8 | T;C | 2014-2026 | - | E-8041 |
| T-019 | Bayesian information borrowing and external control arms | 6 | T;C | 2027-2032 | B10;B5 | E-8041, E-8049 |
| T-020 | Population genomic newborn screening to build trial-ready rare disease cohorts | 6 | T;P | 2028-2036 | B11 | E-8043, E-8044 |
| T-021 | Individualised n-of-1 antisense oligonucleotide pathway with a regulatory platform template | 7 | T;P | 2023-2030 | B11;B15 | E-8042 |

Only one of these four technologies increases the number of identified patients rather than reallocating a fixed pool: genomic newborn screening, which found that 92 percent of true positives in the first 4,000 GUARDIAN newborns were in genes outside standard screening [E-8043]. [INFER] Master protocols and Bayesian borrowing make a fragmented pool go further; they do not make it larger. Since B4's elasticity is 1.2, the arithmetic ceiling on this bottleneck is low regardless of which technology wins.

### B5 - Regulatory review capacity and evidence standards

*Agent C matrix: provisional rank 14, elasticity point estimate 0.4. Technologies scouted: 4.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-022 | Agency-internal generative AI for review workflow (FDA Elsa and successors) | 6 | T | 2025-2029 | - | E-8045 |
| T-023 | AI model credibility qualification framework (FDA seven-step, context-of-use based) | 5 | T;P | 2027-2032 | - | E-8047, E-8049 |
| T-024 | Expedited-review instruments: Commissioner's National Priority Voucher, platform technology designation, priority review vouchers | 7 | T | 2012-2027 | B13 | E-8046, E-8062 |
| T-025 | Machine-readable regulatory submissions built on structured study definitions | 5 | T;C | 2028-2034 | B16 | E-8081, E-8082 |

B5 has the second-lowest elasticity in the matrix (0.4) and its technologies are correspondingly low-value in isolation. [INFER] The important thing about B5 is not its own elasticity but that it gates other bottlenecks: the NAM framework [E-8001], the AI credibility framework [E-8047] and the qualification pathways determine whether high-TRL technologies in B2, B8, B15 and B16 can ever be used as substitutive evidence. Expedited-review instruments are explicitly zero-sum against a fixed reviewer pool [E-8046] - they reallocate capacity rather than create it.

### B6 - CMC / manufacturing

*Agent C matrix: provisional rank 9, elasticity point estimate 1.8. Technologies scouted: 9.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-026 | Cell-free enzymatic DNA (doggybone DNA) replacing plasmid DNA - SHARED INPUTS | 8 | T;C | 2026-2031 | - | E-8020, E-8021 |
| T-027 | Robotic gloveless isolator aseptic fill-finish with small-batch and on-demand filling - SHARED INPUTS | 7 | T;C | 2026-2031 | - | E-8027 |
| T-028 | Stable AAV producer cell lines with high-cell-density perfusion - VIRAL VECTOR | 7 | T;C;P | 2027-2033 | - | E-8022, E-8023 |
| T-029 | AAV process intensification: perfusion bioreaction with integrated continuous clarification - VIRAL VECTOR | 6 | T;C | 2027-2032 | - | E-8022 |
| T-030 | In vivo CAR-T: eliminating per-patient cell manufacturing entirely - AUTOLOGOUS CELL THERAPY | 6 | T;C;P | 2029-2034 | B7 | E-8014, E-8015, E-8089 |
| T-031 | Sub-24-hour and next-day automated closed-system CAR-T manufacture - AUTOLOGOUS CELL THERAPY | 6 | T;C;P | 2027-2031 | - | E-8024, E-8025 |
| T-032 | Integrated continuous bioprocessing with N-1 perfusion intensification - BULK API / mAb | 7 | T;C | 2026-2032 | B5 | E-8026, E-8093 |
| T-033 | Digital twins, AI soft sensors and PAT for real-time release - BULK API / mAb | 5 | T;C | 2029-2035 | B5;B10 | E-8026, E-8093 |
| T-034 | Site-specific enzymatic and bioorthogonal ADC conjugation - ADC | 7 | C;P | 2026-2031 | - | E-8028, E-8100 |

Distributed across the four sub-areas Agent G identified, because the modality spread is real and the levers do not read across. Shared inputs: cell-free enzymatic DNA at TRL 8 with a GMP licence [E-8020][E-8021] and robotic isolator fill-finish at TRL 7 [E-8027]. Viral vector: stable producer lines with 3-6 fold titre gains [E-8022][E-8023] and perfusion process intensification. Autologous cell therapy: in vivo CAR-T [E-8014][E-8015] and sub-24-hour manufacture with 23 of 25 patients reaching MRD-negative CR [E-8024]. Bulk API/mAb: intensified continuous processing [E-8026][E-8093] and digital twins for real-time release. Plus site-specific ADC conjugation, where manufacturing is described as the bottleneck rather than science across 200+ candidates [E-8028]. [INFER] The bulk mAb sub-area is where capacity is least constrained, so its two technologies are the weakest system levers in this section even though they are the highest-TRL.

### B7 - Delivery and biodistribution

*Agent C matrix: provisional rank 5, elasticity point estimate 3. Technologies scouted: 6.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-035 | Transferrin-receptor blood-brain-barrier shuttle biologics (Brainshuttle, transport vehicle) | 8 | P | 2027-2031 | - | E-8016, E-8017 |
| T-036 | Machine-learning-designed AAV capsids for CNS, muscle and liver detargeting | 5 | P | 2030-2036 | B10;B6 | E-8018, E-8019 |
| T-037 | Selective organ targeting lipid nanoparticles (SORT and successors) | 4 | P | 2031-2038 | - | E-8050 |
| T-038 | Antibody-targeted lipid nanoparticles for in vivo cell-type-specific delivery | 6 | P | 2029-2034 | - | E-8014, E-8089 |
| T-039 | MR-guided focused ultrasound blood-brain-barrier opening | 6 | P | 2028-2034 | - | E-8051, E-8052, E-8094 |
| T-040 | Tumour-penetrating peptides and stromal modulation for solid-tumour access | 4 | P | 2031-2039 | - | E-8053 |

B7 binds on P alone in Agent C's matrix, which makes it structurally more valuable than its rank-5 position suggests. It also contains the highest-TRL pure-P technology in the whole catalogue: TfR blood-brain-barrier shuttles, in Phase 3 after 91 percent amyloid PET negativity at 28 weeks in Phase Ib/IIa [E-8016]. [INFER] The four lower-TRL entries share one failure mode: every one of them has been validated in a species whose relevant biology differs from the human in exactly the dimension being exploited - mouse protein corona for SORT [E-8050], primate capsid tropism for ML capsids [E-8018][E-8019], mouse tumour vasculature for penetrating peptides [E-8053]. That is not four independent risks; it is one risk appearing four times.

### B8 - Toxicity and immunogenicity prediction failure

*Agent C matrix: provisional rank 2, elasticity point estimate 6. Technologies scouted: 6.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-041 | Machine-learning immunogenicity prediction and computational deimmunisation | 6 | C;P | 2020-2027 | - | E-8029 |
| T-042 | Integrated in vitro plus in silico DILI battery (liver MPS, spheroids, toxicogenomics reference) | 5 | C;P | 2028-2033 | B2;B5 | E-8030, E-8086, E-8003 |
| T-043 | Human iPSC cardiomyocyte assays coupled to in silico proarrhythmia modelling | 7 | C;P | 2024-2029 | B5 | E-8090, E-8031 |
| T-044 | Broad in vitro secondary pharmacology panels with target-adverse-reaction association maps | 8 | C;P | 2010-2026 | - | E-8096, E-8033 |
| T-045 | Generative de-risking: model-guided redesign to remove a specific safety liability | 3 | P | 2029-2035 | B10 | E-8032, E-8031 |
| T-046 | Large public human toxicogenomics reference resources | 5 | P | 2026-2030 | B10 | E-8086 |

B8 is rank 2 with elasticity 6 and binds on P and C. The technologies split cleanly: three are high-TRL and address failure modes that are already largely managed (secondary pharmacology panels at TRL 8 [E-8096], hERG-successor cardiac assays at TRL 7 [E-8090]), and three address the failure modes that actually dominate late attrition and are TRL 3-6 (immunogenicity [E-8029], idiosyncratic DILI [E-8030], generative de-risking [E-8032]). [INFER] The gap is specific and diagnosable: idiosyncratic DILI and immunogenicity are immune-mediated, and none of the deployed platforms contains a functioning human adaptive immune compartment. The immune-competent organoid entry under B2 (T-010, TRL 3) is the technology that would close this, and it is the lowest-TRL entry in the catalogue.

### B9 - Wet-lab throughput (Design-Build-Test-Learn cycle)

*Agent C matrix: provisional rank 12, elasticity point estimate 0.9. Technologies scouted: 5.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-047 | Droplet microfluidic ultrahigh-throughput screening with cell-free expression | 6 | T;C | 2026-2031 | - | E-8054 |
| T-048 | Self-driving laboratories with closed-loop design-build-test-learn | 4 | T;C | 2028-2036 | B10 | E-8055, E-8056 |
| T-049 | LLM agent orchestration of laboratory workflows (Coscientist, Virtual Lab class) | 3 | T | 2029-2036 | B13 | E-8055, E-8056 |
| T-050 | Cloud laboratories and remote-execution experimental APIs | 7 | T;C | 2020-2027 | - | E-8055 |
| T-051 | Image-based optical pooled screening in primary cells and tissues (PerturbView class) | 5 | T;C | 2027-2032 | B10 | E-8097, E-8012 |

Every technology in this section is flagged or flaggable as low-value. B9's elasticity point estimate is 0.9, and library screening throughput - where droplet microfluidics delivers 10 million variants per hour [E-8054] - is already among the fastest steps in the pipeline. Self-driving labs remain at autonomy Level 2 with a handful at Level 3, and the flagship demonstrations are in robotically simple chemistry [E-8055]. [INFER] The honest reading is that B9 technologies are impressive and system-irrelevant on their own; their only route to value is as data generators feeding B10 and B1, which is a dependency, not a direct effect.

### B10 - Scarcity of high-quality experimental training data

*Agent C matrix: provisional rank 11, elasticity point estimate 1.0. Technologies scouted: 5.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-052 | Cross-pharma federated learning consortia (MELLODDY lineage, K-MELLODDY, Apheris) | 6 | P | 2027-2032 | - | E-8057, E-8060, E-8088, E-8098 |
| T-053 | Precompetitive open data generation programmes (LIGAND-AI) | 4 | P | 2028-2033 | - | E-8058 |
| T-054 | Standardised immutable benchmarks with enforced evaluation protocols (Polaris, Virtual Cell Challenge) | 6 | P | 2025-2029 | - | E-8059, E-8008 |
| T-055 | Industrial perturbation data factories as a purpose-built training corpus | 7 | P | 2025-2029 | - | E-8006, E-8007 |
| T-056 | Self-driving laboratories as designed data generators, including negatives | 4 | P | 2029-2036 | B9 | E-8055, E-8056 |

The interesting entry here is the one aimed at negative data specifically: LIGAND-AI, an open-science programme with reported funding around EUR 60 million to generate and publish protein-small-molecule interaction data [E-8058]. Federated learning has a completed industrial demonstration at 2.6 billion data points across ten companies [E-8057] and a documented technical failure mode in cross-site batch effects [E-8098]. [INFER] The data-scarcity problem has two halves - volume and design - and industry has solved volume (Tahoe-100M and its 225,000-interaction successor [E-8006][E-8007]) while leaving design untouched, because no commercial actor is paid to generate the uninformative-looking experiments that would fix the training distribution.

### B11 - Capital / reimbursement / pricing

*Agent C matrix: provisional rank 3, elasticity point estimate 6. Technologies scouted: 6.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-057 | Government-brokered multi-state outcomes-based agreements (CMS Cell and Gene Therapy Access Model) | 7 | C;P | 2025-2029 | B15 | E-8061 |
| T-058 | Transferable priority review vouchers as a pull incentive | 8 | C | 2012-2026 | B5 | E-8062 |
| T-059 | Synthetic royalty monetisation and non-dilutive structured finance | 8 | C | 2010-2026 | - | E-8063 |
| T-060 | Focused Research Organizations as mission-scoped non-dilutive vehicles | 5 | C;P | 2027-2034 | - | E-8064 |
| T-061 | Harmonised EU joint clinical assessment as a single-evidence-package mechanism | 7 | C | 2025-2030 | B15 | E-8065 |
| T-062 | Advance market commitments and pull funding for uncommercial indications | 7 | C;P | 2027-2034 | - | E-8099 |

B11 is rank 3 with elasticity 6 and binds on C and P. Every candidate here is a financial or institutional instrument rather than a laboratory tool, and each was rated on the same TRL-analogue scale with the anchor stated. The strongest is CMS's multi-state outcomes-based agreement model, live across 33 states covering 84 percent of Medicaid sickle cell beneficiaries [E-8061]. [INFER] Two entries have ambiguous sign. EU joint clinical assessment could raise evidence-generation cost through PICO multiplication rather than lowering it [E-8065]. Royalty financing concentrates on de-risked late assets [E-8063], which is the part of the capital chain that is least constrained. Neither of these should be counted as relief without a measured outcome.

### B12 - IP / FTO congestion

*Agent C matrix: provisional rank 15, elasticity point estimate 0.3. Technologies scouted: 3.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-063 | USPTO AI-assisted invention inventorship framework (2025 revised guidance) | 8 | C | 2024-2026 | - | E-8066, E-8067 |
| T-064 | Mass AI-generated defensive publication to establish prior art | 4 | C | 2027-2033 | - | E-8068, E-8067 |
| T-065 | AI-assisted freedom-to-operate and patent landscape analysis over sequence space | 6 | C | 2025-2029 | - | E-8100, E-8067 |

Three technologies, which is the floor, and that is a finding rather than an omission - see the scarcity note in section 6. B12's elasticity is 0.3, second lowest in the matrix. The USPTO's November 2025 revised guidance is in force and reaffirms that inventorship attaches to natural persons [E-8066], and Amgen v. Sanofi continues to constrain functional genus claims for computationally generated sequences [E-8067]. [INFER] The unresolved question is not technological at all: it is how much human contribution suffices when a model generates ten thousand sequences and a human picks one, and that will be settled by a court, not by a tool.

### B13 - Talent and organizational absorptive capacity

*Agent C matrix: provisional rank 13, elasticity point estimate 0.6. Technologies scouted: 3.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-066 | AI copilots embedded in electronic laboratory notebooks and scientific workflows | 7 | T;C | 2024-2027 | - | E-8069 |
| T-067 | Public-private apprenticeship and biomanufacturing training consortia (NIIMBL, gene therapy training networks) | 7 | T;C | 2026-2033 | - | E-8070, E-8071 |
| T-068 | Robotic and automation substitution for scarce technician labour | 6 | T;C | 2026-2032 | B6 | E-8027, E-8025, E-8039 |

Three technologies, again the floor and again a finding. NIIMBL's eight funded projects total USD 9.7 million and train cohorts in the dozens [E-8070] against searches for senior cell-and-gene-therapy CMC roles that run six to nine months [E-8071]. [INFER] The AI copilot entry deserves explicit caution: 89 percent of scientists reportedly use copilots as their first step [E-8069], and the plausible failure mode is that copilots accelerate the production of analyses while eroding the judgement needed to check them, which would move B13 in the wrong direction. A technology whose most likely failure is to worsen the bottleneck it targets should not be counted as relief.

### B14 - Biosecurity and model regulation

*Agent C matrix: provisional rank 16, elasticity point estimate 0.1. Technologies scouted: 3.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-069 | Universal nucleic acid synthesis order screening (SecureDNA, IBBIS Common Mechanism) | 7 | T | 2024-2027 | - | E-8072, E-8073, E-8074 |
| T-070 | AI-resilient screening against generative protein redesign (Paraphrase Project patches) | 6 | T | 2025-2029 | - | E-8075 |
| T-071 | Tiered structured access and frontier model biological capability evaluations | 5 | T | 2026-2031 | - | E-8076 |

Three technologies, the floor, and B14 has the lowest elasticity in the entire matrix at 0.1. Screening is deployed with a federal framework tightening to a 50-nucleotide window by October 2026 [E-8072], and the Paraphrase Project showed that AI-redesigned toxin sequences evaded existing screens before patches were deployed [E-8075]. [INFER] These technologies have high societal value and close to zero effect on annual approvals. That distinction should be stated plainly rather than blurred: B14 is a real problem and not a rate-limiting step for drug output.

### B15 - Clinical endpoint and biomarker qualification / measurement science

*Agent C matrix: provisional rank 5, elasticity point estimate 3. Technologies scouted: 5.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-072 | Minimal residual disease as a qualified intermediate endpoint for accelerated approval | 8 | T;P | 2026-2030 | - | E-8077, E-8102 |
| T-073 | Circulating tumour DNA as an intermediate endpoint in solid tumours | 5 | T;P | 2029-2035 | B10 | E-8079, E-8077 |
| T-074 | Wearable-derived digital primary endpoints (stride velocity 95th centile) | 7 | T;P | 2023-2029 | B5 | E-8078, E-8080 |
| T-075 | Cross-indication digital mobility biomarkers (real-world walking speed) | 4 | T;P | 2029-2036 | B5 | E-8101, E-8080 |
| T-076 | Drug development tool qualification pathways as institutional infrastructure (DDT, COA, ISTAND) | 7 | T;P | 2026-2033 | B5;B11 | E-8003, E-8078, E-8080 |

The most informative number in this catalogue sits here: 1,021 drug trials have used wearables and FDA has formally qualified zero sensor-derived endpoints [E-8080], while EMA qualified exactly one in July 2023 [E-8078]. Against that, MRD in myeloma cleared an advisory committee 12-0 in April 2024 and reached draft guidance in January 2026 [E-8077]. [INFER] The contrast identifies the actual mechanism: MRD succeeded because a consortium spent a decade building trial-level surrogacy evidence as a public good, and digital endpoints have not, because nobody will fund evidence generation for a tool competitors then use for free. B15's bottleneck is therefore partly a B11 funding problem, and the qualification-pathway entry (T-076) says so explicitly.

### B16 - Protocol design complexity and operational data burden

*Agent C matrix: provisional rank 8, elasticity point estimate 2.0. Technologies scouted: 5.*

| ID | Technology | TRL | Axis | Window | Depends on | Key evidence |
|---|---|---|---|---|---|---|
| T-077 | Machine-readable study definitions (CDISC USDM, Digital Data Flow, 360i) | 5 | T;C | 2027-2033 | B5 | E-8081, E-8082, E-8103 |
| T-078 | LLM protocol authoring and automated schedule-of-activities generation | 4 | T;C | 2027-2031 | B5;B13 | E-8103, E-8081 |
| T-079 | AI-generated digital twins for prognostic covariate adjustment (PROCOVA) | 7 | T;C | 2023-2029 | B10 | E-8040, E-8104 |
| T-080 | eSource and direct EHR-to-EDC data capture | 6 | T;C | 2027-2033 | B5;B3 | E-8048, E-8081 |
| T-081 | Risk-based quality management under ICH E6(R3) | 7 | T;C | 2025-2030 | B13 | E-8048 |

The one qualified technology here is PROCOVA, which holds a positive EMA qualification opinion from September 2022 [E-8040], with claimed enrollment reductions of 10-30 percent that have not been independently confirmed prospectively [E-8104]. Protocol digitisation is real but early: about 90 percent of protocols remain unstructured documents and CDISC 360i specifications complete in 2026 [E-8081]. [INFER] Every technology in B16 depends on either regulatory acceptance of structured or model-based evidence (B5) or on people to operate new workflows (B13), and none of them changes what a protocol asks of a patient - which is the part that drives the operational burden.

## 3. Bottlenecks with no credible technological solution

This section is deliberately blunt. "No credible technological solution" here means: on no horizon examined does any candidate in this catalogue - or any candidate the searches surfaced and I rejected - remove the constraint. It does not mean nothing helps at the margin.

### B1 - target validation: no technology closes the loop, on any horizon

[INFER] Every candidate in B1 improves a *prior*. None of them supplies the thing that would actually validate a human disease target, which is a causal readout in humans. Human genetics comes closest and is a natural experiment rather than a technology, is available for only a minority of targets, and its own strongest recent evidence shows that one of its two main statistical instruments does not enrich for Phase II success on its own [E-8009]. Virtual cell models are trained overwhelmingly on immortalised cancer lines under acute perturbation [E-8005][E-8006] and have no causal identifiability. In vivo screens re-import the animal-model problem they were meant to bypass [E-8011]. Atlases describe rather than test [E-8013]. The decisive point is structural: the only instrument that validates a target in humans is a clinical trial, and a technology that requires a clinical trial to prove that it can replace clinical trials has not solved the bottleneck. B1 has the highest elasticity in the matrix (10) and the thinnest technological answer in this catalogue. If that combination is right, the largest available gain in the system is not purchasable with any technology now in existence.

### B11 - capital and reimbursement: not a technology problem, and the instruments are near their limits

[INFER] Every B11 candidate is an institutional design. The best of them, CMS's multi-state outcomes-based agreement model, addresses the payment problem for one-time therapies in one disease and is not yet evaluated [E-8061]. Priority review vouchers reallocate reviewer capacity rather than create it [E-8046][E-8062]. Royalty financing serves de-risked late assets, not the early-stage gap [E-8063]. EU joint clinical assessment may raise evidence cost through PICO multiplication [E-8065]. B11 is rank 3 with elasticity 6, and there is no laboratory technology on any horizon that changes a payer's willingness to pay or an investor's cost of capital. Anyone proposing to relieve B11 with a tool is proposing the wrong instrument class.

### B13 - talent and absorptive capacity: no solution, and the leading candidate may invert

[INFER] Training consortia operate at dozens per cohort against thousands of vacancies [E-8070][E-8071]. Automation converts a technician shortage into an automation-engineer shortage, and automation engineers are scarcer. AI copilots are the only candidate operating at scale [E-8069], and their most plausible failure mode is that they degrade the judgement that constitutes absorptive capacity. There is no technology that produces experienced people faster than time does.

### Partial - B4, patient-pool arithmetic

[INFER] Three of four B4 technologies reallocate a fixed pool rather than enlarging it. Genomic newborn screening genuinely enlarges the identified pool [E-8043][E-8044] but finds patients faster than therapies exist for them. For a stratum defined by a mutation present in two hundred people worldwide, no design technology creates a two-hundred-and-first patient.

## 4. Dependency chains

A technology that presupposes the solution to its own prerequisite is not a solution. The `depends_on` column encodes these; the chains that matter are:

1. **B9 -> B10 -> B1.** Virtual cell models (T-001) depend on perturbation data (B10). The most promising route to *designed* rather than scavenged data is self-driving labs run as information-maximising generators (T-056), which depends on B9 reaching reliable Level 3 autonomy in biology - currently Level 2 with a handful at Level 3, in chemistry [E-8055]. So the highest-profile technology aimed at the highest-elasticity bottleneck sits at the end of a three-link chain whose first link is unsolved.
2. **B7 -> B6 (inverted).** In vivo CAR-T (T-030) is catalogued under B6 because it eliminates per-patient manufacturing entirely. But it does so by converting a manufacturing problem into a targeted-delivery problem [E-8014][E-8015]. It relieves B6 only to the extent B7 is solved. This is the clearest instance in the catalogue of a technology whose value is contingent on another bottleneck.
3. **B5 gates B2, B8, B15, B16.** Liver MPS (T-007), multi-organ chips (T-008), humanised mice (T-011), the integrated DILI battery (T-042), digital endpoints (T-074, T-075) and structured submissions (T-025) all sit at TRL 5-7 for scientific reasons and stay there for regulatory ones. The March 2026 NAM guidance [E-8001] and the AI credibility framework [E-8047] are the gates. B5's own elasticity is 0.4, but its *gating value* is much larger than its direct value, and the matrix's elasticity metric does not capture that. [INFER] This is a case where the ranking understates importance.
4. **B10 -> B7.** ML-designed capsids (T-036) need large capsid fitness datasets, and their manufacturability at CNS-effective systemic doses returns to B6 [E-8018][E-8019].
5. **B15 -> B11 and B11 -> B15.** Outcomes-based agreements (T-057) need measurable durable outcomes, which is B15. Qualification pathways (T-076) fail on a public goods funding problem, which is B11 [E-8080]. This is a genuine loop, not a chain, and neither side can be solved unilaterally.
6. **B13 -> B3, B16.** Decentralised trial operations (T-015), community site expansion (T-017), eSource (T-080) and risk-based quality management (T-081) all require staff who do not currently exist [E-8039].
7. **B10 -> B8.** Generative de-risking (T-045) optimises against a safety predictor, so its ceiling is the predictor's quality, which is a B10 data problem [E-8032].

## 5. High-TRL but low-value

These technologies work. They attack steps that are not binding, and their impressiveness is unrelated to their system value. Listed with TRL and the elasticity of the bottleneck they attack.

| ID | Technology | TRL | Bottleneck (elasticity) | Why the value is low |
|---|---|---|---|---|
| T-013 | LLM EHR prescreening | 7 | B3 (2.5) | Randomised evaluation shows accuracy gain with no efficiency gain [E-8035]; 59 percent of sites lose patients before screening even begins [E-8091]. Speeds a step that was not the constraint. |
| T-047 | Droplet microfluidic ultrahigh-throughput screening | 6 | B9 (0.9) | 10 million variants per hour [E-8054] against a step already among the fastest in the pipeline. |
| T-050 | Cloud laboratories | 7 | B9 (0.9) | Efficient execution of standardised assays; every programme keeps a local laboratory for the non-standard work that is the actual constraint. |
| T-059 | Synthetic royalty monetisation | 8 | B11 (6) | High TRL, large market [E-8063], but serves de-risked late assets - the least capital-constrained point in the chain. |
| T-069 | Universal nucleic acid synthesis screening | 7 | B14 (0.1) | Lowest elasticity in the matrix [E-8072]. High societal value, negligible effect on approvals per year. |
| T-063 | USPTO AI inventorship framework | 8 | B12 (0.3) | In force and clear [E-8066], attacking the second-lowest-elasticity bottleneck. |
| T-044 | Broad secondary pharmacology panels | 8 | B8 (6) | High TRL but addresses off-target liabilities that are already routinely managed; the P-relevant failures are immune-mediated and unmodelled [E-8096]. |
| T-011 | Humanised-immune-system mice | 7 | B2 (4) | Routine commercial availability for two decades [E-8085]; the constraint is regulatory acceptance, so more capability does not help. |
| T-032 | Integrated continuous bioprocessing for mAb | 7 | B6 (1.8) | Real cost benefit [E-8026][E-8093] in the manufacturing sub-area with the most spare capacity. |

[INFER] The pattern across this table is consistent: technologies attacking T on a step with spare capacity are common and mature, and technologies attacking P on a binding step are rare and immature. That asymmetry exists because T-attacking technologies have a legible business case and P-attacking technologies require a clinical readout to prove their value.

## 6. Where credible candidates are genuinely scarce

Three bottlenecks - B12, B13, B14 - reached exactly the mandated floor of three, and this reflects the field rather than the search. Each is recorded as an UNRESOLVED item in `unresolved.csv` with the full query record.

[INFER] The common cause is that all three are governance problems in which the object being governed is not a scientific unknown. In B12 the unresolved question is how much human contribution suffices for inventorship, which a court decides [E-8066][E-8067]. In B13 the scarce input is experienced judgement, which accumulates at the rate of careers [E-8071]. In B14 the object is an adversary's choices [E-8075]. None of these has the shape a technology can address, so the sparse candidate set is the correct answer, not an artefact.

B4 and B5 reached four each. In B4 the shortfall is arithmetic: three of the four candidates redistribute a fixed pool. In B5 it is that regulatory capacity is set by appropriated headcount, and the instruments that exist reallocate rather than expand it [E-8046].

## 7. Highest-expected-value technologies

Ranked by elasticity of the attacked bottleneck, weighted down for T-only attack, weighted down for dependency on an unsolved prerequisite, and weighted down where the TRL is so low that no readout arrives inside the 2030 horizon. Derivation recorded as [E-8106].

| Rank | ID | Technology | Bottleneck (elas.) | TRL | Axis | Reasoning |
|---|---|---|---|---|---|---|
| 1 | T-002 | Human-genetics-anchored target selection | B1 (10) | 8 | P | The only mature technology attacking the highest-elasticity bottleneck, and it attacks P. Its ceiling is the fraction of targets with tractable genetic signal, and the recent negative MR result [E-8009] shows the signal must be disaggregated rather than used wholesale. Highest expected value in the catalogue despite being the least novel entry in it. |
| 2 | T-057 | CMS multi-state outcomes-based agreements | B11 (6) | 7 | C;P | Rank-3 bottleneck, live at national scale across 84 percent of the relevant Medicaid population [E-8061], with an evaluation arriving inside the horizon. The only candidate that directly attacks payment for durable one-time therapies. |
| 3 | T-041 | ML immunogenicity prediction and deimmunisation | B8 (6) | 6 | P;C | Rank-2 bottleneck, attacks P, deployed now [E-8029]. Discounted because the performance evidence is vendor-controlled and because formulation and aggregation drive much of the variance the method does not model. |
| 4 | T-026 | Cell-free enzymatic DNA replacing plasmid | B6 (1.8) | 8 | T;C | Lower elasticity, but it is the shared input to every viral vector, mRNA and cell therapy product simultaneously, has a GMP licence and a DMF [E-8020][E-8021], and its effect compounds across sub-areas rather than staying in one. |
| 5 | T-035 | TfR blood-brain-barrier shuttles | B7 (3) | 8 | P | The highest-TRL pure-P technology in the catalogue, in Phase 3 with a readout inside the horizon [E-8016]. Its risk is that the Phase 3 indicts the target rather than the shuttle. |
| 6 | T-072 | MRD as a qualified intermediate endpoint | B15 (3) | 8 | T;P | Advisory committee cleared 12-0 and draft guidance issued [E-8077]. Shortens trials without weakening the causal chain, conditional on surrogacy holding in confirmation. |
| 7 | T-030 | In vivo CAR-T | B6 (1.8) | 6 | T;C;P | Would eliminate an entire manufacturing category [E-8014][E-8015]. Heavily discounted for the B7 dependency: it converts a manufacturing bottleneck into a delivery bottleneck rather than removing one. |
| 8 | T-012 | NAM regulatory acceptance framework | B2 (4) | 6 | P;T | Low direct value, very high gating value: it determines whether roughly a dozen other entries in this catalogue can ever be substitutive evidence [E-8001][E-8002][E-8004]. |
| 9 | T-019 | Bayesian borrowing and external controls | B4 (1.2) | 6 | T;C | Modest elasticity but broad applicability across rare disease and oncology, with draft guidance now in place [E-8041]. |
| 10 | T-053 | Precompetitive open data generation (LIGAND-AI) | B10 (1.0) | 4 | P | Low TRL and low direct elasticity, included because it is the only funded candidate attacking the *design* of the training distribution rather than its volume [E-8058], and every B1 and B8 model entry ultimately depends on that. |

[INFER] Two observations about this table. First, four of the top ten are institutional or regulatory rather than laboratory technologies, which follows directly from where the high-elasticity bottlenecks sit. Second, the highest-ranked genuinely novel laboratory technology is at rank 3, and everything above it is either two decades old or a payment mechanism. If attrition dominates - as Agent C's elasticity estimates indicate, with B1 at 10 and B8 at 6 against B9 at 0.9 - then a portfolio weighted toward discovery-acceleration tooling is weighted toward the wrong axis.

## 8. UNRESOLVED

Ten items, recorded in full in `RLSX/work/I/unresolved.csv` with every query attempted, the failure reason, at least three alternative sources tried, and a current best estimate with its basis. Summary:

| # | Item | Best estimate |
|---|---|---|
| 1 | B12 has only three credible candidate technologies | Correct as found; the residual questions are judicial, not technological |
| 2 | B13 has only three credible candidate technologies | Correct as found; the scarce input is experience, which no technology produces |
| 3 | B14 has only three credible candidate technologies | Correct as found; the object of the bottleneck is adversary behaviour |
| 4 | Quantitative performance of the specific liver MPS in ISTAND | Best available proxy is 69 percent sensitivity at 100 percent specificity for PHH spheroids [E-8030] |
| 5 | FDA qualification decision date for any liver MPS | 2028-2031, from ISTAND three-step structure and the 2024 LOI acceptance date |
| 6 | TRONTIER Phase 3 primary completion date | 2027-2028, inferred from Phase 3 initiation timing and anti-amyloid trial durations |
| 7 | Measured CNPV review times against a matched comparator | No published data; FDA states a 1-2 month target against 10-12 month standard [E-8046] |
| 8 | Independent validation of EpiVax ADA prediction performance | None found; vendor-reported 3x correlation improvement is the only figure [E-8029] |
| 9 | AAV cost of goods per dose before and after stable producer lines | No published figure; titre uplift of 3-6x is the only quantified input [E-8022] |
| 10 | Independent confirmation that FDA has qualified zero sensor-derived endpoints | Single secondary source [E-8080]; FDA DDT list is consistent with it |

## 9. Charter compliance notes

- **R1**: all sixteen bottlenecks processed; 81 of 70 required entries; every shortfall recorded as an UNRESOLVED item with queries, failure reason, alternative sources and a best estimate. No deferral or scope-cutting language appears in any deliverable.
- **R2**: every factual sentence carries an [E-8xxx] identifier; every inference is marked [INFER]; two derived records (E-8105, E-8106) state their formulas and inputs; no quotation exceeds fifteen words and none is reproduced structurally.
- **R3**: no confidence grade is assigned anywhere in this output. All 106 records carry `graded_by:null`, `confidence:null`, `grade_reason:[]`. Records likely to attract S4 (company self-report) are marked by placing the company in `authors_or_org`; records where a figure could not be traced to origin carry `circular_risk:true` (E-8010, E-8032, E-8033, E-8036, E-8063).
- **R4**: no prior conversation, memory or user-affiliation context was used. H0 is not assumed anywhere; where the evidence bears on it, section 5 and section 7 report that mature high-TRL technology clusters on discovery-adjacent throughput while the high-elasticity bottlenecks are thinly served - which bears against the framing that discovery acceleration is where the leverage sits, and this is stated as a finding rather than smoothed over. No company, modality or technology was favoured; in vivo CAR-T, virtual cell models and AI prescreening - the three most fashionable entries in this catalogue - each carry an explicit dependency or negative-evidence flag.
