#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

print("Content-Type: text/html; charset=utf-8")
print()

# ── アクティビティ定義 ──
TYPES = {
    "馬車": {
        "icon": "🐴", "color": "#b48cff", "label": "恐怖の馬車",
        "duration": 60,
        "desc": "アッシュウォルドの墓地を訪れて馬車を捕まえましょう。",
        "reward": "ロードライト、ノーマル宝石、レジェンダリーアイテム、鉱石等",
        "req": "参加レベル: 60+",
        "period": "3/19 3:00～3/26 2:59\n4/2 3:00～4/9 2:59",
    },
    "戦場": {
        "icon": "⚔️", "color": "#ff4d4d", "label": "戦場 (Battleground)",
        "duration": 60,
        "desc": "8v8 PvP。チーム戦で勝利を目指せ。",
        "reward": "栄誉, 伝説の紋章 x1, ゴールド x10,000",
        "req": "参加レベル: 60+\n推奨共鳴: 1000+",
    },
    "闘技場": {
        "icon": "🏟️", "color": "#ffb020", "label": "古代の闘技場",
        "duration": 60,
        "desc": "制限時間内にウェーブを生き残れ。",
        "reward": "装備, ゴールド, 経験値",
        "req": "参加レベル: 60+",
    },
    "悪夢": {
        "icon": "💀", "color": "#a78bfa", "label": "恐怖の古の悪夢",
        "duration": 60,
        "desc": "イベント。マップ上に出現するボスを倒せ。",
        "reward": "ロードライト、ノーマル宝石、レジェンダリーアイテム、鉱石等",
        "req": "参加レベル: 60+",
        "period": "3/26 3:00～4/2 2:59\n4/9 3:00～4/16 2:59",
    },
    "門": {
        "icon": "🌀", "color": "#34d399", "label": "悪魔の門",
        "duration": 60,
        "desc": "悪魔の門を閉じよ。パーティ推奨。",
        "reward": "装備, 魔法アイテム",
        "req": "参加レベル: 60+",
    },
    "集会": {
        "icon": "👥", "color": "#38bdf8", "label": "シャドウの集い",
        "duration": 60,
        "desc": "シャドウ勢力の集会。",
        "reward": "勢力ポイント, アイテム",
        "req": "シャドウ所属",
    },
    "襲撃": {
        "icon": "🔥", "color": "#fb923c", "label": "襲撃",
        "duration": 60,
        "desc": "勢力間の大規模戦闘。",
        "reward": "勢力ポイント, 装備",
        "req": "参加レベル: 60+",
    },
    "組合戦": {
        "icon": "🏰", "color": "#f472b6", "label": "暗黒組合戦争",
        "duration": 60,
        "desc": "組合同士の攻城戦。",
        "reward": "組合ポイント, 装備",
        "req": "組合所属",
    },
    "ボス": {
        "icon": "👹", "color": "#ef4444", "label": "ワールドボス",
        "duration": 60,
        "desc": "巨大ワールドボスに挑め。",
        "reward": "伝説装備, 希少素材",
        "req": "参加レベル: 60+",
    },
}

SCHEDULE = {
    "月": [
        ("0:00","週替わり"),("2:00","週替わり"),("4:00","週替わり"),("6:00","週替わり"),
        ("8:00","戦場"),("8:00","週替わり"),("10:00","週替わり"),
        ("12:00","戦場"),("12:00","週替わり"),
        ("14:00","週替わり"),("15:00","戦場"),("16:00","週替わり"),
        ("18:00","戦場"),("18:00","週替わり"),("19:00","門"),
        ("20:00","週替わり"),("21:00","戦場"),("21:00","闘技場"),
        ("22:00","週替わり"),
    ],
    "火": [
        ("0:00","週替わり"),("2:00","週替わり"),("4:00","週替わり"),("6:00","週替わり"),
        ("8:00","戦場"),("8:00","週替わり"),("10:00","週替わり"),
        ("12:00","戦場"),("12:00","週替わり"),
        ("14:00","週替わり"),("15:00","戦場"),("16:00","週替わり"),
        ("18:00","戦場"),("18:00","週替わり"),("19:00","門"),
        ("20:00","週替わり"),("21:00","戦場"),("21:00","闘技場"),
        ("22:00","週替わり"),
    ],
    "水": [
        ("0:00","週替わり"),("2:00","週替わり"),("4:00","週替わり"),("6:00","週替わり"),
        ("8:00","戦場"),("8:00","週替わり"),("10:00","週替わり"),
        ("12:00","戦場"),("12:00","週替わり"),
        ("14:00","週替わり"),("15:00","戦場"),("16:00","週替わり"),
        ("18:00","戦場"),("18:00","週替わり"),("19:00","門"),
        ("20:00","週替わり"),("20:00","集会"),("21:00","戦場"),("21:00","闘技場"),
        ("22:00","週替わり"),
    ],
    "木": [
        ("0:00","週替わり"),("2:00","週替わり"),("4:00","週替わり"),("6:00","週替わり"),
        ("8:00","戦場"),("8:00","週替わり"),("10:00","週替わり"),
        ("12:00","戦場"),("12:00","週替わり"),
        ("14:00","週替わり"),("15:00","戦場"),("16:00","週替わり"),
        ("18:00","戦場"),("18:00","週替わり"),("19:00","門"),
        ("20:00","週替わり"),("21:00","戦場"),("21:00","闘技場"),
        ("22:00","週替わり"),
    ],
    "金": [
        ("0:00","週替わり"),("2:00","週替わり"),("4:00","週替わり"),("6:00","週替わり"),
        ("8:00","戦場"),("8:00","週替わり"),("10:00","週替わり"),
        ("12:00","戦場"),("12:00","週替わり"),
        ("14:00","週替わり"),("15:00","戦場"),("16:00","週替わり"),
        ("18:00","戦場"),("18:00","週替わり"),("19:00","門"),
        ("20:00","週替わり"),("21:00","戦場"),("21:00","闘技場"),
        ("22:00","週替わり"),
    ],
    "土": [
        ("0:00","週替わり"),("2:00","週替わり"),("4:00","週替わり"),("6:00","週替わり"),
        ("8:00","戦場"),("8:00","週替わり"),("10:00","週替わり"),
        ("12:00","戦場"),("12:00","週替わり"),
        ("14:00","週替わり"),("15:00","戦場"),("16:00","週替わり"),
        ("18:00","戦場"),("18:00","週替わり"),("19:00","門"),
        ("20:00","週替わり"),("20:00","襲撃"),
        ("21:00","戦場"),("21:00","闘技場"),("21:00","組合戦"),
        ("22:00","週替わり"),
    ],
    "日": [
        ("0:00","週替わり"),("2:00","週替わり"),("4:00","週替わり"),("6:00","週替わり"),
        ("8:00","戦場"),("8:00","週替わり"),("10:00","週替わり"),
        ("12:00","戦場"),("12:00","週替わり"),
        ("14:00","週替わり"),("15:00","戦場"),("16:00","週替わり"),
        ("18:00","戦場"),("18:00","週替わり"),("19:00","門"),
        ("20:00","週替わり"),("20:00","襲撃"),
        ("21:00","戦場"),("21:00","闘技場"),("21:00","組合戦"),
        ("22:00","週替わり"),
    ],
}

sj = json.dumps(SCHEDULE, ensure_ascii=False)
tj = json.dumps(TYPES, ensure_ascii=False)

HTML = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<title>アクティビティ・カレンダー</title>
<style>
/* ======== RESET & BASE ======== */
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{
  font-family:-apple-system,'Segoe UI','Noto Sans JP','Hiragino Sans',sans-serif;
  font-size:17px;
  background:#0c0e17;color:#d4d4e0;min-height:100vh;
  display:flex;flex-direction:column;
  background-image:
    radial-gradient(ellipse at 20% 0%,rgba(60,40,90,0.25) 0%,transparent 60%),
    radial-gradient(ellipse at 80% 100%,rgba(40,20,60,0.2) 0%,transparent 60%);
}}

/* ======== HEADER ======== */
.hdr{{
  background:linear-gradient(180deg,rgba(30,20,45,0.95),rgba(12,14,23,0.95));
  border-bottom:1px solid rgba(180,140,255,0.15);
  padding:1rem 1.25rem;
  position:sticky;top:0;z-index:100;
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
}}
.hdr-inner{{max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between}}
.hdr-title{{display:flex;align-items:center;gap:0.6rem;font-size:1rem;font-weight:700;color:#e8e0f4}}
.hdr-title .icon{{font-size:1.3rem}}
.hdr-home{{
  color:#8b8ba0;text-decoration:none;font-size:0.8rem;
  border:1px solid rgba(255,255,255,0.1);border-radius:8px;
  padding:0.35rem 0.75rem;transition:all 0.2s;
}}
.hdr-home:hover{{background:rgba(255,255,255,0.06);color:#c4c4d8}}

/* ======== DATE BAR ======== */
.datebar{{
  max-width:1100px;margin:0 auto;padding:0.8rem 1.25rem;
  display:flex;align-items:center;gap:0.75rem;flex-wrap:wrap;
}}
.datebar-text{{font-size:0.78rem;color:#7a7a94;text-transform:uppercase;letter-spacing:0.08em;font-weight:600}}
.datebar-date{{font-size:0.95rem;font-weight:700;color:#e0d8f0}}

/* ======== DAY TABS ======== */
.dtabs{{
  max-width:1100px;margin:0 auto;padding:0 1.25rem;
  display:flex;gap:2px;overflow-x:auto;scrollbar-width:none;
}}
.dtabs::-webkit-scrollbar{{display:none}}
.dtab{{
  flex:1;min-width:48px;padding:0.55rem 0.3rem;text-align:center;
  font-size:0.82rem;font-weight:600;color:#5a5a72;
  background:none;border:none;cursor:pointer;
  border-bottom:2px solid transparent;transition:all 0.2s;
  position:relative;
}}
.dtab:hover{{color:#9090a8}}
.dtab.active{{color:#b48cff;border-bottom-color:#b48cff}}
.dtab.today .dow{{position:relative}}
.dtab.today .dow::after{{
  content:'TODAY';position:absolute;top:-14px;left:50%;transform:translateX(-50%);
  font-size:0.5rem;color:#ff6b6b;letter-spacing:0.08em;white-space:nowrap;
}}

/* ======== LAYOUT ======== */
.wrap{{
  max-width:1100px;margin:0 auto;padding:1rem 1.25rem 3rem;
  display:flex;gap:1.5rem;flex:1;
}}
.tl-col{{flex:1;min-width:0}}
.detail-col{{
  width:340px;flex-shrink:0;position:sticky;top:80px;align-self:flex-start;
  display:none;
}}
.detail-col.has-content{{display:block}}

/* ======== TIMELINE ======== */
.tl{{position:relative;padding-left:28px}}
/* vertical line */
.tl::before{{
  content:'';position:absolute;left:11px;top:0;bottom:0;
  width:2px;background:rgba(180,140,255,0.12);
}}

/* current-time red line */
.tl-now{{
  position:absolute;left:0;right:0;height:0;z-index:10;
  border-top:2px solid #ff4d4d;
  transition:top 0.3s;
}}
.tl-now::before{{
  content:'';position:absolute;left:6px;top:-6px;
  width:10px;height:10px;border-radius:50%;
  background:#ff4d4d;border:2px solid #0c0e17;
}}
.tl-now-label{{
  position:absolute;left:28px;top:-10px;
  font-size:0.65rem;font-weight:700;color:#ff4d4d;
  background:rgba(12,14,23,0.9);padding:1px 6px;border-radius:4px;
  white-space:nowrap;letter-spacing:0.04em;
}}

/* collapsed "..." */
.tl-dots{{
  padding:0.3rem 0 0.3rem 12px;
  color:#4a4a60;font-size:1.2rem;letter-spacing:0.15em;line-height:1;
  cursor:pointer;user-select:none;transition:color 0.2s;
}}
.tl-dots:hover{{color:#7a7a94}}

/* time slot */
.tl-slot{{
  position:relative;
  padding:0.6rem 0 0.6rem 12px;
  transition:opacity 0.3s;
}}
.tl-slot.past{{opacity:0.35}}
.tl-slot.past:hover{{opacity:0.7}}

/* diamond marker */
.tl-slot::before{{
  content:'';position:absolute;
  left:-22px;top:14px;
  width:10px;height:10px;
  background:#1a1a28;border:2px solid rgba(180,140,255,0.3);
  transform:rotate(45deg);
  transition:all 0.2s;z-index:2;
}}
.tl-slot.live::before{{
  background:#ff4d4d;border-color:#ff4d4d;
  box-shadow:0 0 8px rgba(255,77,77,0.5);
}}
.tl-slot.next::before{{
  background:#b48cff;border-color:#b48cff;
  box-shadow:0 0 8px rgba(180,140,255,0.4);
}}

.tl-time{{
  font-size:0.75rem;font-weight:600;color:#5a5a72;
  margin-bottom:0.35rem;font-variant-numeric:tabular-nums;
  display:flex;align-items:center;gap:0.5rem;
}}
.tl-slot.live .tl-time{{color:#ff8080}}
.tl-slot.next .tl-time{{color:#b48cff}}

/* ======== EVENT ROW ======== */
.ev{{
  display:flex;align-items:center;gap:0.65rem;
  padding:0.5rem 0.7rem;margin:0.25rem 0;
  background:rgba(26,26,40,0.6);
  border:1px solid rgba(255,255,255,0.04);
  border-radius:10px;
  cursor:pointer;transition:all 0.18s;
  position:relative;overflow:hidden;
}}
.ev::before{{
  content:'';position:absolute;left:0;top:0;bottom:0;
  width:3px;background:var(--ec);border-radius:3px 0 0 3px;
}}
.ev:hover{{
  background:rgba(40,36,60,0.7);
  border-color:rgba(180,140,255,0.15);
  transform:translateX(3px);
}}
.ev.selected{{
  background:rgba(60,50,90,0.5);
  border-color:rgba(180,140,255,0.3);
}}

.ev-icon{{
  width:36px;height:36px;
  display:flex;align-items:center;justify-content:center;
  background:rgba(0,0,0,0.3);border-radius:8px;
  font-size:1.2rem;flex-shrink:0;
}}
.ev-body{{flex:1;min-width:0}}
.ev-name{{font-size:0.85rem;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.ev-sub{{font-size:0.7rem;color:#7a7a94;margin-top:1px}}

/* badges */
.badge{{
  display:inline-flex;align-items:center;gap:3px;
  font-size:0.6rem;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;
  padding:2px 7px;border-radius:4px;flex-shrink:0;
}}
.badge-live{{background:#ff4d4d;color:#fff;animation:pulse 1.5s infinite}}
.badge-ended{{background:rgba(255,255,255,0.08);color:#6a6a80}}
.badge-soon{{background:rgba(180,140,255,0.15);color:#b48cff}}

.badge-live::before{{
  content:'';width:6px;height:6px;border-radius:50%;
  background:#fff;
}}
@keyframes pulse{{
  0%,100%{{opacity:1}}
  50%{{opacity:0.6}}
}}

/* ======== DETAIL PANEL ======== */
.dp{{
  background:linear-gradient(170deg,rgba(30,25,50,0.95),rgba(18,16,30,0.95));
  border:1px solid rgba(180,140,255,0.12);
  border-radius:14px;overflow:hidden;
}}
.dp-head{{
  padding:1.25rem;
  background:linear-gradient(135deg,rgba(80,50,120,0.3),rgba(40,20,60,0.3));
  border-bottom:1px solid rgba(180,140,255,0.08);
  text-align:center;
}}
.dp-icon{{font-size:2.5rem;margin-bottom:0.4rem}}
.dp-title{{font-size:1.05rem;font-weight:700;color:#e8e0f4}}
.dp-schedule{{font-size:0.78rem;color:#8b8ba0;margin-top:0.3rem}}
.dp-body{{padding:1.25rem}}
.dp-desc{{font-size:0.82rem;color:#a0a0b8;line-height:1.6;margin-bottom:1rem}}
.dp-section{{margin-bottom:0.8rem}}
.dp-label{{font-size:0.68rem;text-transform:uppercase;letter-spacing:0.1em;color:#6a6a80;margin-bottom:0.3rem;font-weight:600}}
.dp-val{{font-size:0.82rem;color:#c8c8d8;line-height:1.5;white-space:pre-line}}

/* ======== MOBILE MODAL ======== */
.modal-overlay{{
  display:none;position:fixed;inset:0;z-index:200;
  background:rgba(0,0,0,0.6);
  backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);
}}
.modal-overlay.open{{display:flex;align-items:flex-end;justify-content:center}}
.modal-sheet{{
  background:linear-gradient(170deg,#1e1932,#121020);
  border:1px solid rgba(180,140,255,0.12);
  border-radius:18px 18px 0 0;
  width:100%;max-width:500px;max-height:70vh;
  overflow-y:auto;padding-bottom:env(safe-area-inset-bottom,0);
  animation:slideUp 0.25s ease;
}}
.modal-handle{{
  width:36px;height:4px;background:rgba(255,255,255,0.15);
  border-radius:2px;margin:10px auto 0;
}}
@keyframes slideUp{{
  from{{transform:translateY(100%)}}
  to{{transform:translateY(0)}}
}}

/* ======== BOTTOM TABS ======== */
.btabs{{
  max-width:1100px;margin:0 auto;padding:0.5rem 1.25rem;
  display:flex;gap:0.5rem;
}}
.btab{{
  flex:1;padding:0.6rem;text-align:center;
  font-size:0.8rem;font-weight:600;color:#5a5a72;
  background:rgba(26,26,40,0.6);border:1px solid rgba(255,255,255,0.04);
  border-radius:10px;cursor:pointer;transition:all 0.2s;
  display:flex;align-items:center;justify-content:center;gap:0.4rem;
}}
.btab:hover{{background:rgba(40,36,60,0.5);color:#9090a8}}
.btab.active{{background:rgba(80,50,120,0.3);color:#b48cff;border-color:rgba(180,140,255,0.2)}}

/* ======== RESPONSIVE ======== */
@media(max-width:768px){{
  .detail-col{{display:none!important}}
  .wrap{{padding:0.75rem 1rem 3rem}}
  .ev-icon{{width:30px;height:30px;font-size:1rem}}
  .ev-name{{font-size:0.8rem}}
  .datebar{{padding:0.6rem 1rem}}
  .dtabs{{padding:0 1rem}}
}}
@media(min-width:769px){{
  .modal-overlay{{display:none!important}}
}}

/* ======== SCROLLBAR ======== */
::-webkit-scrollbar{{width:6px}}
::-webkit-scrollbar-track{{background:transparent}}
::-webkit-scrollbar-thumb{{background:rgba(180,140,255,0.15);border-radius:3px}}
</style>
</head>
<body>

<!-- HEADER -->
<div class="hdr">
  <div class="hdr-inner">
    <div class="hdr-title"><span class="icon">📅</span> アクティビティ・カレンダー</div>
    <a class="hdr-home" href="index.py">← ホーム</a>
  </div>
</div>

<!-- DATE -->
<div class="datebar">
  <span class="datebar-text">TODAY'S DATE &amp; TIME</span>
  <span class="datebar-date" id="dateLabel"></span>
</div>

<!-- DAY TABS -->
<div class="dtabs" id="dtabs"></div>

<!-- BOTTOM TABS (filter) -->
<div class="btabs">
  <button class="btab active" data-mode="today" onclick="setMode('today')">✅ 今日のアクティビティ</button>
  <button class="btab" data-mode="star" onclick="setMode('star')">☆ 目玉アクティビティ</button>
</div>

<!-- MAIN -->
<div class="wrap">
  <div class="tl-col">
    <div class="tl" id="timeline"></div>
  </div>
  <div class="detail-col" id="detailCol">
    <div class="dp" id="detailPanel"></div>
  </div>
</div>

<!-- MOBILE DETAIL MODAL -->
<div class="modal-overlay" id="modal" onclick="closeModal(event)">
  <div class="modal-sheet" id="modalSheet">
    <div class="modal-handle"></div>
    <div class="dp" id="modalPanel"></div>
  </div>
</div>

<script>
const SCHEDULE={sj};
const TYPES={tj};
const DAYS=["月","火","水","木","金","土","日"];
const DAYF=["月曜日","火曜日","水曜日","木曜日","金曜日","土曜日","日曜日"];
const STAR_KEYS=new Set(["戦場","闘技場","悪夢","門","集会","襲撃","組合戦","ボス"]);

// ── 週替わりイベント期間判定 ──
const ROT_PERIODS=[
  {{key:"馬車",  ranges:[[new Date(2026,2,19,3),new Date(2026,2,26,3)],[new Date(2026,3,2,3),new Date(2026,3,9,3)]]}},
  {{key:"悪夢",  ranges:[[new Date(2026,2,26,3),new Date(2026,3,2,3)],[new Date(2026,3,9,3),new Date(2026,3,16,3)]]}},
];
function resolveRotKey(){{
  const now=new Date();
  for(const p of ROT_PERIODS){{
    for(const [s,e] of p.ranges){{
      if(now>=s&&now<e) return p.key;
    }}
  }}
  return "馬車";
}}
const ROT_KEY=resolveRotKey();

function todayIdx(){{const d=new Date().getDay();return d===0?6:d-1}}
function parseH(t){{return parseInt(t)}}
function pad2(n){{return String(n).padStart(2,'0')}}

let curDay=todayIdx();
let mode='today';
let selectedKey=null;
let selectedTime=null;

// ── Date label ──
function updateDate(){{
  const n=new Date();
  const mm=n.getMonth()+1,dd=n.getDate();
  const hh=pad2(n.getHours()),mi=pad2(n.getMinutes());
  document.getElementById('dateLabel').textContent=
    `${{mm}}月${{dd}}日 ${{DAYF[todayIdx()]}}, ${{hh}}:${{mi}}`;
}}
updateDate();setInterval(updateDate,30000);

// ── Tabs ──
function renderTabs(){{
  const el=document.getElementById('dtabs');
  el.innerHTML=DAYS.map((d,i)=>{{
    const a=i===curDay?' active':'';
    const t=i===todayIdx()?' today':'';
    return `<button class="dtab${{a}}${{t}}" onclick="pickDay(${{i}})"><span class="dow">${{DAYF[i]}}</span></button>`;
  }}).join('');
}}

// ── Timeline ──
function renderTL(){{
  const el=document.getElementById('timeline');
  const dk=DAYS[curDay];
  let raw=SCHEDULE[dk]||[];

  // 週替わりを実際のイベントキーに解決
  raw=raw.map(([t,k])=>[t, k==='週替わり' ? ROT_KEY : k]);

  // filter by mode
  if(mode==='star') raw=raw.filter(([,k])=>STAR_KEYS.has(k));

  // group by time
  const groups=new Map();
  raw.forEach(([t,k])=>{{
    if(!groups.has(t)) groups.set(t,[]);
    groups.get(t).push(k);
  }});

  const now=new Date();
  const curH=now.getHours();
  const curM=now.getMinutes();
  const isToday=curDay===todayIdx();

  // find "next scheduled"
  let nextTime=null;
  if(isToday){{
    for(const t of groups.keys()){{
      const h=parseH(t);
      if(h>curH){{nextTime=t;break}}
    }}
  }}

  // Determine which past slots to collapse (consecutive same-only "馬車")
  const timeKeys=[...groups.keys()];
  const collapsed=new Set();
  // Collapse only deep-night 馬車 runs (0-6am when all are just 馬車)
  let streak=[];
  for(const t of timeKeys){{
    const evs=groups.get(t);
    const h=parseH(t);
    if(evs.length===1&&evs[0]==='馬車'&&isToday&&h<curH){{
      streak.push(t);
    }}else{{
      if(streak.length>2){{
        // collapse middle ones
        for(let i=1;i<streak.length-1;i++) collapsed.add(streak[i]);
      }}
      streak=[];
    }}
  }}
  if(streak.length>2){{
    for(let i=1;i<streak.length-1;i++) collapsed.add(streak[i]);
  }}

  let html='';
  let prevWasCollapsed=false;

  for(const t of timeKeys){{
    const evs=groups.get(t);
    const h=parseH(t);

    // insert "..." for collapsed
    if(collapsed.has(t)){{
      if(!prevWasCollapsed){{
        html+=`<div class="tl-dots" title="省略されたスロットを表示">···</div>`;
      }}
      prevWasCollapsed=true;
      continue;
    }}
    prevWasCollapsed=false;

    // status
    let cls='tl-slot';
    let statusHtml='';
    if(isToday){{
      if(h<curH){{
        cls+=' past';
        statusHtml='<span class="badge badge-ended">終了</span>';
      }}else if(h===curH){{
        cls+=' live';
        statusHtml='<span class="badge badge-live">LIVE</span>';
      }}else if(t===nextTime){{
        cls+=' next';
        const mins=(h-curH)*60-curM;
        statusHtml=`<span class="badge badge-soon">あと ${{mins}}分</span>`;
      }}
    }}

    // label
    let timeLabel=t;
    let extra='';
    if(isToday&&t===nextTime) extra='<span style="font-size:0.65rem;color:#b48cff;margin-left:4px">Next Scheduled</span>';
    if(isToday&&h===curH) extra='<span style="font-size:0.65rem;color:#ff8080;margin-left:4px">[ Current Time ]</span>';

    html+=`<div class="${{cls}}" data-hour="${{h}}">`;
    html+=`<div class="tl-time">${{timeLabel}}${{extra}}</div>`;

    for(const k of evs){{
      const tp=TYPES[k];
      const sel=(k===selectedKey&&t===selectedTime)?' selected':'';
      html+=`<div class="ev${{sel}}" style="--ec:${{tp.color}}" onclick="showDetail('${{k}}','${{t}}')">
        <div class="ev-icon">${{tp.icon}}</div>
        <div class="ev-body">
          <div class="ev-name">${{tp.label}}</div>
          <div class="ev-sub">${{DAYF[curDay]}} ${{t}}</div>
        </div>
        ${{statusHtml}}
      </div>`;
    }}
    html+=`</div>`;
  }}

  // current-time indicator
  if(isToday){{
    const totalMin=curH*60+curM;
    // calculate position: find the slot elements and interpolate
    // We'll use a JS-based approach after render
  }}

  el.innerHTML=html;

  // position the current-time line
  if(isToday) positionNowLine(el,curH,curM);

  // auto-scroll to live/next
  setTimeout(()=>{{
    const target=el.querySelector('.tl-slot.live')||el.querySelector('.tl-slot.next');
    if(target) target.scrollIntoView({{behavior:'smooth',block:'center'}});
  }},150);

  // dots expand
  el.querySelectorAll('.tl-dots').forEach(d=>{{
    d.addEventListener('click',()=>{{
      // remove collapse and re-render
      mode='today';// force show all
      // quick hack: just re-render without collapse by switching mode
      renderTL();
    }});
  }});
}}

function positionNowLine(el,h,m){{
  // find slots before and at current hour
  const slots=[...el.querySelectorAll('.tl-slot')];
  if(!slots.length) return;

  let beforeSlot=null,afterSlot=null;
  for(const s of slots){{
    const sh=parseInt(s.dataset.hour);
    if(sh<=h) beforeSlot=s;
    if(sh>h&&!afterSlot) afterSlot=s;
  }}

  if(!beforeSlot) return;

  // create now line
  const line=document.createElement('div');
  line.className='tl-now';
  line.innerHTML=`<span class="tl-now-label">${{pad2(h)}}:${{pad2(m)}}</span>`;

  // position after the "live" slot
  if(afterSlot){{
    el.insertBefore(line,afterSlot);
  }}else{{
    el.appendChild(line);
  }}
}}

// ── Detail panel ──
function showDetail(key,time){{
  selectedKey=key;selectedTime=time;
  const tp=TYPES[key];
  const dayLabel=DAYF[curDay];

  const panelHtml=`
    <div class="dp-head">
      <div class="dp-icon">${{tp.icon}}</div>
      <div class="dp-title">${{tp.label}}</div>
      <div class="dp-schedule">${{dayLabel}} ${{time}} - ${{parseH(time)+1}}:00</div>
    </div>
    <div class="dp-body">
      <div class="dp-desc">${{tp.desc}}</div>
      ${{tp.period ? `<div class="dp-section">
        <div class="dp-label">📅 イベント期間</div>
        <div class="dp-val" style="color:#f9d262;white-space:pre-line">${{tp.period}}</div>
      </div>` : ''}}
      <div class="dp-section">
        <div class="dp-label">参加条件</div>
        <div class="dp-val">${{tp.req}}</div>
      </div>
      <div class="dp-section">
        <div class="dp-label">報酬</div>
        <div class="dp-val">${{tp.reward}}</div>
      </div>
    </div>`;

  // Desktop: side panel
  const col=document.getElementById('detailCol');
  col.classList.add('has-content');
  document.getElementById('detailPanel').innerHTML=panelHtml;

  // Mobile: bottom sheet
  if(window.innerWidth<769){{
    document.getElementById('modalPanel').innerHTML=panelHtml;
    document.getElementById('modal').classList.add('open');
  }}

  // highlight selected
  renderTL();
}}

function closeModal(e){{
  if(e.target===document.getElementById('modal')){{
    document.getElementById('modal').classList.remove('open');
  }}
}}

// ── Controls ──
function pickDay(i){{curDay=i;selectedKey=null;selectedTime=null;renderTabs();renderTL();updateDetailVisibility()}}
function setMode(m){{
  mode=m;
  document.querySelectorAll('.btab').forEach(b=>b.classList.toggle('active',b.dataset.mode===m));
  renderTL();
}}
function updateDetailVisibility(){{
  if(!selectedKey) document.getElementById('detailCol').classList.remove('has-content');
}}

// ── Init ──
renderTabs();
renderTL();
</script>
</body>
</html>"""

print(HTML)
