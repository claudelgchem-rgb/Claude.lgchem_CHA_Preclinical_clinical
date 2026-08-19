# RLSX COMMON BRIEF (all agents MUST read fully before any work)

## [0] EXECUTION ENVIRONMENT RULES
- E1. Working dir = repo root. ALL outputs under `./RLSX/`. Relative paths only. No absolute paths.
- E2. Data collection uses **WebSearch / WebFetch tools ONLY**. Do NOT use curl/wget/pip/apt in Bash (sandbox blocks them).
- E3. Python: **standard library only**. No pandas/requests/python-docx. Use `csv` and `json` modules.
- E4. Documents: `.md` and **single-file `.html`** only (no external CDN/font/script). Never attempt `.docx`/`.pdf`.
- E6. Write your own deliverables to disk yourself. Return to the orchestrator ONLY: (1) file paths created, (2) key findings <=10 lines, (3) evidence ID range created, (4) UNRESOLVED count. Never return full text.
- E9. Run **12-25 WebSearch calls** for your assignment. Writing facts from memory without searching is FORBIDDEN.

## [1] CHARTER (verbatim; violation invalidates your output)
R1. Never defer; complete the work.
  - Forbidden words in deliverables: "추후", "향후 조사", "더 조사가 필요", "시간 관계상", "샘플로 N개만", "생략" (and English equivalents used as scope-cutting: "TBD", "future work", "out of scope due to time").
  - Process ALL assigned items exhaustively. For impossible items write an UNRESOLVED record containing: (1) every search query attempted, (2) failure reason, (3) record of >=3 alternative sources attempted, (4) current best estimate + rationale. Blank with no reason = incomplete.
  - Never shrink scope for token/time reasons. Split if large, but finish everything.
R2. Every claim/fact must reference explicit UI-materialized evidence.
  - Attach an evidence ID `[E-0001]` to every factual claim sentence. Mark your own reasoning/interpretation as `[INFER]`.
  - Load all evidence into `./RLSX/evidence/parts/<AGENT>.jsonl`. It renders into a clickable evidence-chip UI.
  - Derived values with no URL: `type:"derived"`, and state the formula plus all input evidence IDs.
  - Direct quotes <=15 words. Never exceed. Do not reproduce source structure/paragraphs; restate in your own words.
R3. Reliability is independently verified and labeled 상(High)/중(Medium)/하(Low).
  - Collectors do NOT grade their own evidence. Agent R grades independently. Collectors leave `"confidence": null, "graded_by": null`.
  - Downgrade reason codes: S1 single-source / S2 method-undisclosed / S3 circular-reference / S4 conflict-of-interest / S5 sample-bias / S6 outdated / S7 origin-unverifiable.
  - Never draw a conclusion from 'Low' evidence alone; if unavoidable attach a `⚠ LOW-EVIDENCE CLAIM` banner.
R4. Ignore all prior conversation context; operate from a Basal state.
  - Do not reference past user conversations, memory, existing project context, or the user's employer/business interests.
  - H0 below is a HYPOTHESIS UNDER TEST, not a premise. Do not write as if H0 is true.
  - Do not tilt conclusions to favor any company, technology, or modality.

## [L] 보고 언어 규약 (LANGUAGE — 위반 시 산출물 무효)
**L1. 모든 보고는 반드시 한국어로 작성한다.**
  - 대상: 최종 보고서(RLSX_report.md), 요약본(RLSX_executive_brief.md), 등급 요약(grade_summary.md),
    레드팀 findings(redteam_findings.md), 그리고 각 에이전트의 work/<AGENT>/report.md 본문.
  - 서술문·제목·표 헤더·해석·판정은 한국어로 쓴다. 영어로 된 보고 문단은 미완수로 간주한다.
  - 다음은 원문 그대로 유지한다(번역 금지): 고유명사(기관·기업·제품·법령·논문 제목), 지표·필드명,
    CSV 헤더와 셀 값, JSON 키와 값, 코드, 파일 경로, URL, 근거 ID, 등급 코드(S1~S7),
    `CHARTER_ACK: R1,R2,R3,R4` 행, 15단어 이내 직접 인용문.
  - 한국어에 정착되지 않은 전문용어는 한국어 서술 안에서 원어를 괄호로 병기한다.
    예: 율속단계(rate-limiting step), 탄력도(elasticity), 감쇄(attrition), 대리평가변수(surrogate endpoint).
  - 수치·단위·통화는 원 표기를 유지하고 서술만 한국어로 쓴다.
  - 이 규약은 R1~R4와 동등한 강제력을 가지며 품질 게이트 G10이 기계적으로 검사한다.

## [2] MISSION
Q1. To what extent is the claim that AI has actually compressed protein structure prediction / sequence design / molecular generation empirically substantiated? (quantitative, not rhetorical)
Q2. As of 2026, where is the true rate-limiting step of the bio/drug-development pipeline? Answer separately for Time (T), Cost (C), Probability of success (P).
Q3. When discovery is extremely compressed by AI, where does the constraint MOVE? (Theory of Constraints)
Q4. Give ranked rate-limiting steps with probabilities for 2030 / 2035 / 2040.
Q5. What breakthrough technologies would break each rate-limiting step? Give TRL / developer / timing / remaining hard problems.

**CORE DEFINITION**: A rate-limiting step is NOT merely "a slow step". It is **a step whose improvement actually increases total system output (annual approved new drugs; approvals per $ invested)**. A step that is slow but parallelizable or already holding spare capacity is NOT a constraint. All agents use this definition.

## [3] HYPOTHESIS UNDER TEST (not a premise)
H0: "Historically the rate-limiting step was research to find hit protein structures/sequences; with AI progress, preclinical/clinical will become rate-limiting."

Mandatory sub-tests:
- H0-a Was discovery ACTUALLY the rate-limiting step historically? -> **Treat as likely-falsifiable.** Actively seek counter-evidence that clinical stages have long dominated time/cost/attrition.
- H0-b AI reducing discovery *duration* and AI raising *probability of success (PoS)* are separate axes. Test both separately.
- H0-c If discovery time went to zero, what % of total development time and capital cost is removed? (Amdahl ceiling)
- H0-d "Preclinical/clinical" is not one step. Decompose into the bottleneck candidates below and identify which sub-element is the constraint.

BOTTLENECK CANDIDATE CATALOG — **B1~B14 must ALL be evaluated** (omission = R1 violation). Add B15+ if new ones are found.
- B1 Target validation / translational validity of target biology
- B2 Preclinical->clinical translation failure (animal model predictivity, NAM validation)
- B3 Clinical trial patient recruitment / site capacity
- B4 Patient-pool fragmentation from precision medicine
- B5 Regulatory review capacity & evidence standards (incl. acceptance of AI/NAM evidence)
- B6 CMC / manufacturing (viral vector, plasmid, LNP, ADC conjugation, aseptic fill-finish, autologous cell therapy)
- B7 Delivery & biodistribution (extrahepatic delivery, BBB, solid-tumor penetration)
- B8 Toxicity & immunogenicity prediction failure
- B9 Wet-lab throughput (Design-Build-Test-Learn cycle)
- B10 Scarcity of high-quality experimental training data (negative data, standardization, reproducibility)
- B11 Capital / reimbursement / pricing (payer, HTA, investment cycle)
- B12 IP / FTO congestion (patentability and inventorship of AI-mass-generated sequences)
- B13 Talent & organizational absorptive capacity
- B14 Biosecurity & model regulation (access controls on biological AI models)

## [4] MEASUREMENT PROTOCOL
- M1. Never conflate T/C/P. For C always mark whether the figure is out-of-pocket / risk-adjusted for attrition / includes cost of capital (COC).
- M2. Judge constraint status by **elasticity**: if this step improves 10%, by what % does annual approvals (or approvals per $) rise? Highest elasticity = the constraint.
- M3. Every cited number needs metadata: producing organization / sample (companies, period, disease) / denominator definition / COC included? / publication year. Any missing item caps confidence at 'Low'.
- M4. No circular references. Trace cited numbers to origin, up to 3 hops. On failure force confidence 'Low' and set `circular_risk:true`.
- M5. Mandatory modality decomposition: small molecule / antibody / ADC / cell therapy / gene therapy / RNA (mRNA, siRNA, ASO) / vaccine.
- M6. Region decomposition: at minimum US / EU / CN / JP-KR.

**ANCHORS UNDER TEST** — widely circulated numbers. **Do NOT accept as fact; verify origin and then adopt / revise / reject.**
- Capitalized cost per approved drug ~ $2.2-2.9B (DiMasi/Tufts lineage; methodology contested)
- Phase I -> approval cumulative success ~ 7-14% (BIO/Informa/QLS lineage)
- Phase II is the lowest-success phase and most failures are efficacy failures
- Total development ~10-15 years; discovery ~3-6 years
- Claim that AI-derived candidates show higher-than-average Phase I success and similar Phase II -> **must verify existence and sample size**
- Eroom's Law and whether it reversed after the late 2010s

## [7] EVIDENCE LEDGER SCHEMA (one JSON object per line, no trailing commas)
{"id":"E-1001","claim":"claim restated in your own words","bottleneck":"B1","type":"primary_literature|regulatory|filing|registry|secondary|market_report|derived","source_title":"","publisher":"","authors_or_org":"","url":"","published_date":"YYYY-MM-DD","accessed_date":"2026-08-18","quote":"<=15 words, optional","figures":{"metric":"","value":null,"unit":"","denominator_def":"","sample":"","coc_included":null},"collected_by":"A","graded_by":null,"confidence":null,"grade_reason":[],"cross_refs":[],"provenance_hops":["url1","url2"],"circular_risk":false,"derivation":""}

Notes:
- `published_date` unknown -> use "" (empty string), never omit the key.
- `figures.value` must be a JSON number or null.
- `provenance_hops` must have >=1 entry for any record carrying a quantitative figure.
- Every record MUST include all keys above.

## [11] PROHIBITIONS
- Deciding the conclusion first and fitting evidence to it
- Writing as if H0 is true
- Unsourced numbers, re-citation without origin verification
- Quotes over 15 words, reproducing source paragraph structure
- Scope reduction / deferral / "sample only" handling
- Grading your own evidence
- Adjusting conclusions for the user's employer or business interests
- Presenting a plan and asking the user instead of executing
