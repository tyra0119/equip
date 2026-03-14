#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print("Content-Type: text/html; charset=utf-8")
print()

HTML = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>精髄チェッカー | Diablo Immortal</title>
<style>
  :root {
    --bg: #f0f4f8;
    --card: #ffffff;
    --border: #e2e8f0;
    --text: #1a202c;
    --text-sub: #4a5568;
    --text-muted: #a0aec0;
    --shadow: 0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.05);
    --shadow-lg: 0 10px 25px rgba(0,0,0,0.1), 0 4px 10px rgba(0,0,0,0.06);
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Segoe UI', 'Noto Sans JP', sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
  }
  header {
    background: linear-gradient(135deg, #1e3a5f 0%, #312e81 100%);
    padding: 2rem 1.5rem;
    text-align: center;
    box-shadow: 0 2px 12px rgba(0,0,0,0.25);
  }
  header h1 {
    font-size: clamp(1.3rem, 4vw, 2rem);
    font-weight: 700;
    background: linear-gradient(90deg, #90cdf4, #fbd38d);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 0.05em;
    margin-bottom: 0.4rem;
  }
  header p {
    color: rgba(255,255,255,0.55);
    font-size: 0.9rem;
  }
  main {
    max-width: 1100px;
    margin: 0 auto;
    padding: 2.5rem 1.5rem;
  }
  .section-label {
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--text-muted);
    margin-bottom: 1.25rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }
  .section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
  }
  .class-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 1.25rem;
    margin-bottom: 2.5rem;
  }
  .class-card {
    background: var(--card);
    border: 1.5px solid var(--border);
    border-radius: 16px;
    padding: 1.75rem 1.25rem;
    text-align: center;
    text-decoration: none;
    color: var(--text);
    cursor: pointer;
    transition: all 0.22s ease;
    box-shadow: var(--shadow);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.75rem;
    position: relative;
    overflow: hidden;
  }
  .class-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: var(--class-color, #a0aec0);
    opacity: 0.7;
    transition: opacity 0.2s;
  }
  .class-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
    border-color: var(--class-color, #a0aec0);
  }
  .class-card:hover::before { opacity: 1; }
  .class-card.coming-soon {
    cursor: not-allowed;
    opacity: 0.55;
  }
  .class-card.coming-soon:hover { transform: none; box-shadow: var(--shadow); }
  .class-icon {
    font-size: 2.8rem;
    line-height: 1;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
  }
  .class-name {
    font-size: 1.05rem;
    font-weight: 700;
    letter-spacing: 0.03em;
  }
  .class-name-en {
    font-size: 0.72rem;
    color: var(--text-muted);
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }
  .class-desc {
    font-size: 0.78rem;
    color: var(--text-sub);
    line-height: 1.5;
  }
  .badge {
    display: inline-block;
    font-size: 0.65rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    padding: 0.2rem 0.6rem;
    border-radius: 20px;
    margin-top: 0.25rem;
  }
  .badge-available { background: #d1fae5; color: #065f46; }
  .badge-soon { background: #f3f4f6; color: #9ca3af; }

  footer {
    text-align: center;
    padding: 2rem;
    color: var(--text-muted);
    font-size: 0.78rem;
    border-top: 1px solid var(--border);
    margin-top: 1rem;
  }

  @media (max-width: 480px) {
    .class-grid { grid-template-columns: repeat(2, 1fr); gap: 0.75rem; }
    main { padding: 1.5rem 1rem; }
    header { padding: 1.5rem 1rem; }
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to { opacity: 1; transform: translateY(0); }
  }
  .class-card { animation: fadeUp 0.3s ease both; }
  .class-card:nth-child(1) { animation-delay: 0.05s; }
  .class-card:nth-child(2) { animation-delay: 0.10s; }
  .class-card:nth-child(3) { animation-delay: 0.15s; }
  .class-card:nth-child(4) { animation-delay: 0.20s; }
  .class-card:nth-child(5) { animation-delay: 0.25s; }
  .class-card:nth-child(6) { animation-delay: 0.30s; }
  .class-card:nth-child(7) { animation-delay: 0.35s; }
  .class-card:nth-child(8) { animation-delay: 0.40s; }
</style>
</head>
<body>
<header>
  <h1>⚔️ 精髄チェッカー</h1>
  <p>Diablo Immortal — クラスを選択してスキルと精髄を検索</p>
</header>

<main>
  <p class="section-label">利用可能なクラス</p>
  <div class="class-grid">

    <div class="class-card coming-soon" style="--class-color:#9ca3af;">
      <div class="class-icon"><img src="/images/ウィザード.png" style="width: 50px;"/></div>
      <div>
        <div class="class-name">ウィザード</div>
        <div class="class-name-en">Wizard</div>
      </div>
      <div class="class-desc">強力な呪文で敵を殲滅する<br>遠距離魔法クラス</div>
      <span class="badge badge-soon">近日追加</span>
    </div>

    <div class="class-card coming-soon" style="--class-color:#9ca3af;">
      <div class="class-icon"><img src="/images/バーバリアン.png" style="width: 50px;"/></div>
      <div>
        <div class="class-name">バーバリアン</div>
        <div class="class-name-en">Barbarian</div>
      </div>
      <div class="class-desc">圧倒的な力で敵を粉砕する<br>最強の近接戦士</div>
      <span class="badge badge-soon">近日追加</span>
    </div>

    <a class="class-card" href="monk.py" style="--class-color:#f59e0b;">
      <div class="class-icon"><img src="/images/モンク.png" style="width: 50px;"/></div>
      <div>
        <div class="class-name">モンク</div>
        <div class="class-name-en">Monk</div>
      </div>
      <div class="class-desc">武道と精神力で戦う<br>近接戦闘の達人</div>
      <span class="badge badge-available">利用可能</span>
    </a>

    <a class="class-card" href="demonhunter.py" style="--class-color:#dc2626;">
      <div class="class-icon"><img src="/images/デーモン・ハンター.png" style="width: 50px;"/></div>
      <div>
        <div class="class-name">デーモンハンター</div>
        <div class="class-name-en">Demon Hunter</div>
      </div>
      <div class="class-desc">弓と罠で敵を仕留める<br>遠距離戦闘のスペシャリスト</div>
      <span class="badge badge-available">利用可能</span>
    </a>

    <div class="class-card coming-soon" style="--class-color:#9ca3af;">
      <div class="class-icon"><img src="/images/クルセイダー.png" style="width: 50px;"/></div>
      <div>
        <div class="class-name">クルセイダー</div>
        <div class="class-name-en">Crusader</div>
      </div>
      <div class="class-desc">信仰の力で敵を薙ぎ払う<br>重装備の聖戦士</div>
      <span class="badge badge-soon">近日追加</span>
    </div>

    <div class="class-card coming-soon" style="--class-color:#9ca3af;">
      <div class="class-icon"><img src="/images/ネクロマンサー.png" style="width: 50px;"/></div>
      <div>
        <div class="class-name">ネクロマンサー</div>
        <div class="class-name-en">Necromancer</div>
      </div>
      <div class="class-desc">アンデッドの軍団を率いる<br>死霊術師</div>
      <span class="badge badge-soon">近日追加</span>
    </div>

    <div class="class-card coming-soon" style="--class-color:#9ca3af;">
      <div class="class-icon"><img src="/images/ブラッド・ナイト.png" style="width: 50px;"/></div>
      <div>
        <div class="class-name">ブラッド・ナイト</div>
        <div class="class-name-en">Tempest</div>
      </div>
      <div class="class-desc">人間離れした守護者。その体には呪われた吸血鬼の力が宿っており、敵の血を取って騎士の槍で切り刻む</div>
      <span class="badge badge-soon">近日追加</span>
    </div>

    <a class="class-card" href="tempest.py" style="--class-color:#0077b6;">
      <div class="class-icon"><img src="/images/テンペスト.png" style="width: 50px;"/></div>
      <div>
        <div class="class-name">テンペスト</div>
        <div class="class-name-en">Tempest</div>
      </div>
      <div class="class-desc">風と水を操る<br>新クラス・近接支援型</div>
      <span class="badge badge-available">利用可能</span>
    </a>

    <div class="class-card coming-soon" style="--class-color:#9ca3af;">
      <div class="class-icon"><img src="/images/ドルイド.png" style="width: 50px;"/></div>
      <div>
        <div class="class-name">ドルイド</div>
        <div class="class-name-en">Druid</div>
      </div>
      <div class="class-desc">自然の力と変身能力を持つ<br>形態変化の達人</div>
      <span class="badge badge-soon">近日追加</span>
    </div>
  </div>
</main>

<footer>
  Diablo Immortal 精髄チェッカー — 非公式ファンツール
</footer>
</body>
</html>"""

print(HTML)
