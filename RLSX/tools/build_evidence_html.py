#!/usr/bin/env python3
"""Render RLSX_evidence.html: the clickable evidence-chip UI (spec section 8).

Single file, no CDN/font/library dependency. The ledger is embedded as an
inline application/json block and rendered by vanilla JS. Standard library only.
"""
import csv
import json
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
OUT = os.path.join(ROOT, "RLSX_evidence.html")

GRADE_COLOR = {"상": "#1a7f37", "중": "#9a6700", "하": "#cf222e"}
REASON_LABEL = {
    "S1": "S1 단일출처", "S2": "S2 방법론비공개", "S3": "S3 순환참조",
    "S4": "S4 이해상충", "S5": "S5 표본편향", "S6": "S6 구버전",
    "S7": "S7 원출처확인불가",
}


def load_jsonl(path):
    out = []
    if not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def load_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def main():
    recs = load_jsonl(os.path.join(ROOT, "evidence", "evidence.jsonl"))
    unresolved = load_csv(os.path.join(ROOT, "audit", "unresolved.csv"))
    circ = {r["evidence_id"]: r for r in load_csv(os.path.join(ROOT, "audit", "circular_audit.csv"))}

    # attach the provenance audit verdict so a card can show it
    for r in recs:
        a = circ.get(r["id"])
        if a:
            r["audit_verdict"] = a.get("circular_verdict", "")
            r["audit_origin_reached"] = a.get("origin_reached", "")

    report_path = os.path.join(ROOT, "RLSX_report.md")
    cited = set()
    if os.path.exists(report_path):
        with open(report_path, encoding="utf-8") as fh:
            cited = set(re.findall(r"\[(E-\d{4})", fh.read()))
    for r in recs:
        r["cited_in_report"] = r["id"] in cited

    payload = {
        "generated_for": "RLSX — Rate-Limiting Step eXplorer",
        "record_count": len(recs),
        "unresolved_count": len(unresolved),
        "evidence": recs,
        "unresolved": unresolved,
    }
    data = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    # guard against closing the inline script early
    data = data.replace("</", "<\\/")

    html = HTML_TEMPLATE.replace("__DATA__", data)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html)

    size = os.path.getsize(OUT)
    dist = {}
    for r in recs:
        dist[r.get("confidence")] = dist.get(r.get("confidence"), 0) + 1
    print("wrote RLSX_evidence.html (%d records, %d unresolved, %.1f KB)"
          % (len(recs), len(unresolved), size / 1024.0))
    print("grade distribution: %s" % dist)
    print("cited in report   : %d" % len(cited))
    return 0


HTML_TEMPLATE = r"""<title>RLSX 근거 원장</title>
<style>
:root{
  --bg:#ffffff; --panel:#f6f8fa; --panel2:#eef1f4; --ink:#1f2328; --muted:#59636e;
  --line:#d1d9e0; --accent:#0969da;
  --hi:#1a7f37; --hi-bg:#eaf6ec; --mid:#9a6700; --mid-bg:#fdf5e2; --lo:#cf222e; --lo-bg:#fdeceb;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#0d1117; --panel:#151b23; --panel2:#1c232b; --ink:#e6edf3; --muted:#9198a1;
    --line:#3d444d; --accent:#4493f8;
    --hi:#3fb950; --hi-bg:#12261a; --mid:#d29922; --mid-bg:#2b2011; --lo:#f85149; --lo-bg:#2d1416;
  }
}
:root[data-theme="dark"]{
  --bg:#0d1117; --panel:#151b23; --panel2:#1c232b; --ink:#e6edf3; --muted:#9198a1;
  --line:#3d444d; --accent:#4493f8;
  --hi:#3fb950; --hi-bg:#12261a; --mid:#d29922; --mid-bg:#2b2011; --lo:#f85149; --lo-bg:#2d1416;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans KR",Helvetica,Arial,sans-serif;}
.wrap{max-width:1180px;margin:0 auto;padding:28px 20px 80px}
h1{font-size:26px;margin:0 0 4px;letter-spacing:-0.01em}
h2{font-size:18px;margin:34px 0 12px;padding-bottom:6px;border-bottom:1px solid var(--line)}
.sub{color:var(--muted);margin:0 0 22px;font-size:14px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:14px 16px}
.stat .n{font-size:26px;font-weight:640;letter-spacing:-0.02em}
.stat .k{color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.05em;margin-top:2px}
.bar{height:26px;display:flex;border-radius:6px;overflow:hidden;border:1px solid var(--line);margin:6px 0 4px}
.bar span{display:block;height:100%}
.legend{display:flex;gap:16px;flex-wrap:wrap;color:var(--muted);font-size:13px;margin-bottom:8px}
.dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:5px;vertical-align:middle}
table{border-collapse:collapse;width:100%;font-size:13.5px}
.scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--muted);font-weight:600;font-size:12px;text-transform:uppercase;letter-spacing:.04em}
.hbar{background:var(--accent);height:9px;border-radius:2px;display:inline-block;min-width:2px}
.filters{position:sticky;top:0;background:var(--bg);padding:12px 0;border-bottom:1px solid var(--line);
  z-index:5;display:flex;gap:8px;flex-wrap:wrap;align-items:center}
select,input[type=search]{background:var(--panel);color:var(--ink);border:1px solid var(--line);
  border-radius:6px;padding:6px 9px;font-size:13px;font-family:inherit}
input[type=search]{min-width:210px;flex:1}
label.chk{display:inline-flex;align-items:center;gap:5px;font-size:13px;color:var(--muted);
  background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:6px 9px;cursor:pointer}
.chip{display:inline-flex;align-items:center;gap:5px;font:600 12px/1 ui-monospace,SFMono-Regular,Menlo,monospace;
  padding:4px 8px;border-radius:999px;border:1px solid;cursor:pointer;user-select:none;white-space:nowrap}
.chip.hi{color:var(--hi);background:var(--hi-bg);border-color:var(--hi)}
.chip.mid{color:var(--mid);background:var(--mid-bg);border-color:var(--mid)}
.chip.lo{color:var(--lo);background:var(--lo-bg);border-color:var(--lo)}
.card{border:1px solid var(--line);border-left-width:4px;border-radius:8px;background:var(--panel);
  margin:0 0 10px;padding:0;overflow:hidden}
.card.hi{border-left-color:var(--hi)} .card.mid{border-left-color:var(--mid)} .card.lo{border-left-color:var(--lo)}
.card > summary{padding:11px 14px;cursor:pointer;list-style:none;display:flex;gap:10px;align-items:flex-start}
.card > summary::-webkit-details-marker{display:none}
.card[open] > summary{border-bottom:1px solid var(--line);background:var(--panel2)}
.claim{flex:1;min-width:0}
.meta{color:var(--muted);font-size:12.5px;margin-top:3px}
.body{padding:12px 14px;font-size:13.5px}
.kv{display:grid;grid-template-columns:170px 1fr;gap:5px 14px;margin:0}
.kv dt{color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.03em;padding-top:2px}
.kv dd{margin:0;word-break:break-word}
a{color:var(--accent)}
code{font:12.5px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--panel2);
  padding:1px 5px;border-radius:4px}
.tag{display:inline-block;font-size:11px;padding:2px 7px;border-radius:999px;background:var(--panel2);
  border:1px solid var(--line);color:var(--muted);margin:0 4px 4px 0}
.tag.warn{color:var(--lo);border-color:var(--lo)}
.count{color:var(--muted);font-size:13px;margin:14px 0 10px}
.empty{color:var(--muted);padding:36px;text-align:center;border:1px dashed var(--line);border-radius:8px}
#more{display:block;width:100%;margin-top:10px;padding:10px;background:var(--panel);color:var(--ink);
  border:1px solid var(--line);border-radius:8px;cursor:pointer;font:inherit;font-size:13px}
.note{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--mid);
  border-radius:8px;padding:12px 14px;font-size:13.5px;margin:12px 0}
</style>

<script type="application/json" id="rlsx-ledger">__DATA__</script>

<div class="wrap">
<h1>RLSX 근거 원장</h1>
<p class="sub">Rate-Limiting Step eXplorer — 보고서의 모든 사실 주장은 이곳의 레코드로 연결된다.
신뢰도 등급은 독립 채점 에이전트가 부여했으며, 어떤 에이전트도 자신이 수집한 근거를 채점하지 않았다.</p>

<div class="grid" id="stats"></div>

<h2>신뢰도 등급 분포</h2>
<div class="legend">
  <span><i class="dot" style="background:var(--hi)"></i>상 — 1차 출처 + 독립 교차확인 2건 이상 + 재현 가능한 방법론</span>
  <span><i class="dot" style="background:var(--mid)"></i>중 — 1차 출처 1건이거나 교차검증 부분적</span>
  <span><i class="dot" style="background:var(--lo)"></i>하 — 단일 2·3차 출처, 방법론 비공개, 원출처 역추적 실패</span>
</div>
<div class="bar" id="dist"></div>
<div class="meta" id="distlabel"></div>

<h2>하향 사유 코드 분포</h2>
<div class="scroll"><table id="reasons"></table></div>

<h2>병목별 근거 수</h2>
<div class="scroll"><table id="bottlenecks"></table></div>

<h2>근거 레코드</h2>
<div class="filters">
  <input type="search" id="q" placeholder="주장·출처·발행처·ID 검색…" autocomplete="off">
  <select id="fg"><option value="">전체 등급</option><option>상</option><option>중</option><option>하</option></select>
  <select id="fa"><option value="">전체 에이전트</option></select>
  <select id="fb"><option value="">전체 병목</option></select>
  <select id="ft"><option value="">전체 유형</option></select>
  <label class="chk"><input type="checkbox" id="fc"> 순환참조 위험만</label>
  <label class="chk"><input type="checkbox" id="fr"> 보고서 인용만</label>
</div>
<p class="count" id="count"></p>
<div id="list"></div>
<button id="more" hidden>더 보기</button>

<h2>UNRESOLVED 전량 목록</h2>
<p class="sub">이번 런에서 종결하지 못한 항목. 헌장 R1에 따라 각 항목은 시도한 검색 쿼리, 실패 사유,
대체 출처 시도 기록, 현시점 최선 추정치를 모두 갖는다. 사유 없는 공란은 미완수로 간주된다.</p>
<div class="scroll"><table id="unres"></table></div>
</div>

<script>
(function(){
"use strict";
var D = JSON.parse(document.getElementById('rlsx-ledger').textContent);
var E = D.evidence || [], U = D.unresolved || [];
var CLS = {'상':'hi','중':'mid','하':'lo'};
var REASONS = __REASONS__;

function esc(s){ return String(s==null?'':s).replace(/[&<>"']/g, function(c){
  return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]; }); }
function uniq(a){ return Array.from(new Set(a.filter(Boolean))).sort(); }

/* ---------- dashboard ---------- */
var dist = {'상':0,'중':0,'하':0}, byAgent={}, byBn={}, byReason={}, circ=0, cited=0, withFig=0;
E.forEach(function(r){
  if(dist[r.confidence]!==undefined) dist[r.confidence]++;
  byAgent[r.collected_by]=(byAgent[r.collected_by]||0)+1;
  String(r.bottleneck||'').split(/[;,\s]+/).forEach(function(b){ if(b) byBn[b]=(byBn[b]||0)+1; });
  (r.grade_reason||[]).forEach(function(x){ byReason[x]=(byReason[x]||0)+1; });
  if(r.circular_risk) circ++;
  if(r.cited_in_report) cited++;
  if(r.figures && r.figures.value !== null && r.figures.value !== undefined) withFig++;
});

document.getElementById('stats').innerHTML = [
  ['근거 레코드', E.length],
  ['정량 수치 보유', withFig],
  ['보고서 인용', cited],
  ['순환참조 위험', circ],
  ['UNRESOLVED', U.length]
].map(function(s){ return '<div class="stat"><div class="n">'+s[1]+'</div><div class="k">'+s[0]+'</div></div>'; }).join('');

var tot = E.length || 1;
document.getElementById('dist').innerHTML = ['상','중','하'].map(function(g){
  var pct = dist[g]/tot*100;
  return '<span style="width:'+pct+'%;background:var(--'+CLS[g]+')" title="'+g+' '+dist[g]+'"></span>';
}).join('');
document.getElementById('distlabel').textContent =
  '상 '+dist['상']+' ('+(dist['상']/tot*100).toFixed(1)+'%) · 중 '+dist['중']+' ('+(dist['중']/tot*100).toFixed(1)+
  '%) · 하 '+dist['하']+' ('+(dist['하']/tot*100).toFixed(1)+'%)';

function hbar(tbl, obj, head, labels){
  var keys = Object.keys(obj).sort(function(a,b){ return obj[b]-obj[a]; });
  var max = Math.max.apply(null, keys.map(function(k){ return obj[k]; }).concat([1]));
  document.getElementById(tbl).innerHTML =
    '<tr><th>'+head+'</th><th>건수</th><th style="width:55%"></th></tr>' +
    keys.map(function(k){
      return '<tr><td>'+esc(labels&&labels[k]?labels[k]:k)+'</td><td>'+obj[k]+
             '</td><td><i class="hbar" style="width:'+(obj[k]/max*100)+'%"></i></td></tr>'; }).join('');
}
hbar('reasons', byReason, '하향 사유', REASONS);
hbar('bottlenecks', byBn, '병목', null);

/* ---------- filters ---------- */
function fill(id, vals){
  var s=document.getElementById(id);
  vals.forEach(function(v){ var o=document.createElement('option'); o.textContent=v; s.appendChild(o); });
}
fill('fa', uniq(E.map(function(r){return r.collected_by;})));
fill('fb', uniq(Object.keys(byBn)));
fill('ft', uniq(E.map(function(r){return r.type;})));

var LIMIT=60, shown=LIMIT;
var els={q:'q',g:'fg',a:'fa',b:'fb',t:'ft'};

function match(r){
  var g=document.getElementById('fg').value, a=document.getElementById('fa').value,
      b=document.getElementById('fb').value, t=document.getElementById('ft').value,
      q=document.getElementById('q').value.trim().toLowerCase();
  if(g && r.confidence!==g) return false;
  if(a && r.collected_by!==a) return false;
  if(b && String(r.bottleneck||'').split(/[;,\s]+/).indexOf(b)<0) return false;
  if(t && r.type!==t) return false;
  if(document.getElementById('fc').checked && !r.circular_risk) return false;
  if(document.getElementById('fr').checked && !r.cited_in_report) return false;
  if(q){
    var hay=[r.id,r.claim,r.source_title,r.publisher,r.authors_or_org,r.bottleneck,
             (r.figures&&r.figures.metric)].join(' ').toLowerCase();
    if(hay.indexOf(q)<0) return false;
  }
  return true;
}

function card(r){
  var c=CLS[r.confidence]||'mid', f=r.figures||{};
  var tags=[];
  if(r.type) tags.push('<span class="tag">'+esc(r.type)+'</span>');
  if(r.bottleneck) tags.push('<span class="tag">'+esc(r.bottleneck)+'</span>');
  if(r.circular_risk) tags.push('<span class="tag warn">순환참조 위험</span>');
  if(r.audit_verdict) tags.push('<span class="tag">원출처 감사: '+esc(r.audit_verdict)+'</span>');
  (r.grade_reason||[]).forEach(function(x){
    tags.push('<span class="tag warn">'+esc(REASONS[x]||x)+'</span>'); });

  var rows=[];
  function add(k,v){ if(v!==''&&v!==null&&v!==undefined) rows.push('<dt>'+k+'</dt><dd>'+v+'</dd>'); }
  add('출처', esc(r.source_title));
  add('발행처', esc(r.publisher||r.authors_or_org));
  if(r.url) add('URL','<a href="'+esc(r.url)+'" target="_blank" rel="noopener noreferrer">'+esc(r.url)+'</a>');
  add('발행일', esc(r.published_date)); add('접근일', esc(r.accessed_date));
  if(r.quote) add('직접 인용','&ldquo;'+esc(r.quote)+'&rdquo;');
  if(f.metric) add('지표', esc(f.metric));
  if(f.value!==null&&f.value!==undefined) add('값', esc(f.value)+' '+esc(f.unit||''));
  if(f.value_note) add('값(비수치)', esc(f.value_note));
  add('분모 정의', esc(f.denominator_def)); add('표본', esc(f.sample));
  if(f.coc_included!==null&&f.coc_included!==undefined) add('자본비용 포함 여부', esc(f.coc_included));
  add('수집 에이전트', esc(r.collected_by)); add('채점 에이전트', esc(r.graded_by));
  add('등급 판정 사유', esc(r.grade_rationale));
  add('검증 방식', esc(r.verification_method)+(r.verification_note?' — '+esc(r.verification_note):''));
  if((r.provenance_hops||[]).length) add('원출처 역추적',
    r.provenance_hops.map(function(h){ return /^https?:/.test(h)
      ? '<a href="'+esc(h)+'" target="_blank" rel="noopener noreferrer">'+esc(h)+'</a>' : esc(h); }).join('<br>'));
  if((r.cross_refs||[]).length) add('교차참조',
    r.cross_refs.map(function(x){ return '<a href="#'+esc(x)+'">'+esc(x)+'</a>'; }).join(', '));
  if(r.derivation) add('산출식','<code>'+esc(r.derivation)+'</code>');

  return '<details class="card '+c+'" id="'+esc(r.id)+'">'+
    '<summary><span class="chip '+c+'">'+esc(r.id)+' '+esc(r.confidence||'—')+'</span>'+
    '<span class="claim">'+esc(r.claim)+'<div class="meta">'+esc(r.publisher||r.authors_or_org||'')+
    (r.published_date?' · '+esc(r.published_date):'')+'</div></span></summary>'+
    '<div class="body">'+(tags.length?'<div>'+tags.join('')+'</div>':'')+'<dl class="kv">'+rows.join('')+'</dl></div>'+
    '</details>';
}

function render(){
  var sel = E.filter(match);
  document.getElementById('count').textContent =
    '전체 '+E.length+'건 중 '+sel.length+'건'+(sel.length>shown?' — 상위 '+shown+'건 표시':'');
  document.getElementById('list').innerHTML = sel.length
    ? sel.slice(0,shown).map(card).join('')
    : '<div class="empty">해당 조건에 맞는 근거가 없습니다.</div>';
  document.getElementById('more').hidden = sel.length<=shown;
}
Object.keys(els).forEach(function(k){
  var el=document.getElementById(els[k]);
  el.addEventListener(k==='q'?'input':'change', function(){ shown=LIMIT; render(); });
});
['fc','fr'].forEach(function(id){
  document.getElementById(id).addEventListener('change', function(){ shown=LIMIT; render(); }); });
document.getElementById('more').addEventListener('click', function(){ shown+=LIMIT; render(); });

/* deep link: open and scroll to a card named in the URL hash */
function openHash(){
  var h=location.hash.slice(1);
  if(!/^E-\d{4}$/.test(h)) return;
  var rec=E.filter(function(r){return r.id===h;});
  if(!rec.length) return;
  document.getElementById('q').value=h; shown=LIMIT; render();
  var el=document.getElementById(h);
  if(el){ el.open=true; el.scrollIntoView({block:'center'}); }
}
window.addEventListener('hashchange', openHash);

/* ---------- unresolved ---------- */
document.getElementById('unres').innerHTML =
  '<tr><th>에이전트</th><th>항목</th><th>미종결 사유</th><th>최선 추정치</th></tr>' +
  U.map(function(u){
    return '<tr><td>'+esc(u.agent)+'</td><td>'+esc(u.item)+'</td><td>'+esc(u.failure_reason)+
           '</td><td>'+esc(u.best_estimate)+'</td></tr>'; }).join('');

render();
openHash();
})();
</script>
"""

HTML_TEMPLATE = HTML_TEMPLATE.replace("__REASONS__", json.dumps(REASON_LABEL, ensure_ascii=False))

if __name__ == "__main__":
    sys.exit(main())
