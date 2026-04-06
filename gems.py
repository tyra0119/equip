#!/usr/bin/env python3
"""
Diablo Immortal - レジェンダリー宝石一覧 (Rank 10)
全ての ★1 / ★2 / ★5 宝石の Rank 10 時の性能を
HTML ファイルとして出力する Python スクリプト。

出典: MisterMenPlays.com / GINX / Game8
※ diablo.tv はSPAのためスクレイピング不可。最新値は diablo.tv で要確認。
"""

import html as h
import os

# ─────────────────────────────────────────────
# データ定義  (name_en, name_jp, color, rank10_effect)
# ─────────────────────────────────────────────

GEMS_1STAR = [
    ("Berserker's Eye", "バーサーカーの瞳", "#e74c3c",
     "与ダメージ+16%、クリティカルヒット率+2%。ただし被ダメージ+5%"),
    ("The Black Rose", "ブラックローズ", "#2c3e50",
     "被攻撃時24%の確率でツタ召喚→攻撃者を3.3秒間固定。同敵20秒CD"),
    ("Ca'arsen's Invigoration", "カーセンの活力", "#f39c12",
     "通常攻撃速度+16%、通常攻撃ダメージ+2%"),
    ("Chained Death", "チェインドデス", "#8e44ad",
     "ヒットしたターゲット1体につき与ダメージ+2.5%（最大7体で+17.5%）"),
    ("Defiant Soul", "反抗の魂", "#3498db",
     "ブロック時に周囲へ基礎ダメージ192%+777。その後3秒間被ダメージ-6%。20秒CD"),
    ("Everlasting Torment", "永遠の苦悶", "#c0392b",
     "クリティカルで苦悶付与:毎秒基礎ダメージ30%+122を6秒間。苦悶中の周囲敵1体につき攻撃速度+6%。20秒CD"),
    ("Freedom and Devotion", "自由と献身", "#27ae60",
     "召喚物の持続時間+24%、召喚物ダメージ+3%"),
    ("Mocking Laughter", "嘲笑", "#e67e22",
     "通常攻撃で敵の与ダメージ-8%を付与し、非エリートに6秒間自分を攻撃させる"),
    ("Nightmare Wreath", "ナイトメアリース", "#9b59b6",
     "敵撃破時10%の確率で周囲の敵を2.4秒間恐怖。逃走中の敵への与ダメージ+8%。20秒CD"),
    ("Pain of Subjugation", "制圧の苦痛", "#1abc9c",
     "行動制御中の敵への与ダメージ+16%。自身の行動制御中は被ダメージ-4%"),
    ("Respite Stone", "休息の石", "#34495e",
     "HP10%減少ごとに被ダメージ-1.6%（最大-16%）。HP50%以下でブロック率+6%"),
    ("Seled's Weakening", "セレドの弱体", "#d35400",
     "エリート撃破後60秒間、与ダメージ+18%。エリートへの与ダメージ+4%"),
    ("Trickshot Gem", "トリックショットジェム", "#2980b9",
     "チャネリングのエネルギー消費-24%。チャネリング中の被ダメージ-2%"),
    ("Zod Stone", "ゾドストーン", "#7f8c8d",
     "アルティメットスキル持続時間+48%。アルティメットダメージ+6%"),
    ("Blessed Pebble", "祝福の小石", "#f1c40f",
     "有益な効果の持続時間+12%。有益な効果取得後3秒間、移動速度+8%"),
    ("Hearthstone", "ハースストーン", "#e74c3c",
     "吸収シールド持続時間+36%。シールド中、行動制御の持続時間-24%"),
    ("Lo's Focused Gaze", "ロの集中した凝視", "#3498db",
     "全装備の基本属性+0.75%。チャージスキルのチャージ速度+15%"),
    ("Eye of the Unyielding", "不屈の瞳", "#e67e22",
     "継続ダメージの与ダメージ+16%。継続ダメージの被ダメージ-4%"),
    ("Unrefined Passage", "未精錬の通路", "#9b59b6",
     "移動中の被ダメージ-15%。スロウ効果を4%の確率で無効化"),
    ("Lucent Watcher", "ルーセントウォッチャー", "#1abc9c",
     "行動制御効果の持続時間-8%"),
    ("Misery Elixir", "ミザリーエリクサー", "#c0392b",
     "自身が付与する有害効果の持続時間+8%"),
]

GEMS_2STAR = [
    ("Battleguard", "バトルガード", "#2c3e50",
     "3ヤード以内の敵からの近接ダメージ-24%。HP60%以下で敵をすり抜けて移動可能"),
    ("Bloody Reach", "ブラッディリーチ", "#c0392b",
     "敵との距離2ヤードごとに与ダメージ+6%（最大8ヤードで+24%）。攻撃の1.2%で敵の攻撃・移動速度-35%を2秒間"),
    ("Cutthroat's Grin", "カットスロートの笑み", "#8e44ad",
     "背後攻撃時クリティカルヒット率+24%。背後攻撃時の与ダメージ+4%"),
    ("Fervent Fang", "ファーヴェントファング", "#e74c3c",
     "同一敵へのダメージごとに与ダメージ+2.4%（最大10スタック+24%）。エリートへの全ダメージ+6%"),
    ("Lightning Core", "ライトニングコア", "#3498db",
     "通常攻撃と移動で電気チャージ。フルチャージで通常攻撃からチェインライトニング発動（基礎ダメージ280%+1134）。全ダメージ+12%を3秒間。20秒CD"),
    ("Power & Command", "パワー＆コマンド", "#f39c12",
     "9秒ごとに交互切替。パワー:通常攻撃ダメージ+24%。コマンド:他スキルダメージ+24%。切替時30%で有害効果1つ解除"),
    ("Follower's Burden", "フォロワーの重荷", "#27ae60",
     "召喚物1体につき全ダメージ+3%（最大+18%）。召喚物の被ダメージ-6%"),
    ("The Hunger", "ザ・ハンガー", "#d35400",
     "敵撃破時に基礎ダメージ140%+567のHP回復。撃破後3秒間移動速度+16%。20秒CD"),
    ("Unity Crystal", "ユニティクリスタル", "#1abc9c",
     "6ヤード以内のパーティメンバー1人につき被ダメージ-1.5%、与ダメージ+1.2%"),
    ("The Abiding Curse", "アバイディングカース", "#2c3e50",
     "攻撃の15%で呪い付与:攻撃・移動速度-35%を8秒間。呪い中の敵への与ダメージ+10%。同対象20秒CD"),
    ("Igneous Scorn", "イグネウススコーン", "#e67e22",
     "クリティカルで爆発（基礎ダメージ120%+486）。6秒CD。爆発後2秒間与ダメージ+10%"),
    ("Viper's Bite", "ヴァイパーズバイト", "#27ae60",
     "ダメージで敵に毒付与:毎秒基礎ダメージ16%+120を6秒間。同対象20秒CD"),
    ("Pain Clasp", "ペインクラスプ", "#9b59b6",
     "継続ダメージを受けている敵への与ダメージ+8%（Rank2で+10.5%）"),
    ("Kir Sling", "キアスリング", "#f1c40f",
     "被攻撃時15%で閃光→周囲の敵を4秒間ブラインド（完全行動制御）。20秒CD。ブラインド中の敵への与ダメージ+14%"),
    ("Volatility Shard", "ヴォラティリティシャード", "#e74c3c",
     "敵撃破時に爆発（基礎ダメージ90%+365）。2秒間与ダメージ+8%。6秒CD"),
    ("Mossthorn", "モスソーン", "#27ae60",
     "被ダメージ時6秒間有効化。被攻撃ごとにトゲ反撃（基礎ダメージ17%+201）。0.5秒CD。発動は20秒CD"),
    ("Tear of the Comet", "彗星の涙", "#3498db",
     "チャネリング中、毎秒アーケインミサイル2発（基礎ダメージ10%+120）"),
]

GEMS_5STAR = [
    ("Blood-Soaked Jade", "血塗られたヒスイ", "#e74c3c",
     "全ダメージ+最大24%（HP低下で最低12%まで減少）。移動速度+24%。HP50%以下で被ダメージ-8%"),
    ("Seeping Bile", "滲む胆汁", "#27ae60",
     "攻撃の4%で毒付与:毎秒基礎ダメージ65%+263を6秒間。移動速度-24%。死亡時に拡散。同対象20秒CD"),
    ("Blessing of the Worthy", "価値ある者の祝福", "#f39c12",
     "被ダメージ時20%で報復:最大HP28%のダメージを周囲に。発動後6秒間被ダメージ-16%。15秒CD"),
    ("Bottled Hope", "瓶詰めの希望", "#3498db",
     "バフスキル使用時、対象の与ダメージ+24%、移動速度+24%を6秒間。スキルCD-6%。20秒CD"),
    ("Chip of Stoned Flesh", "石化の欠片", "#8e44ad",
     "行動制御で爆発の呪い付与。呪い中ダメージの45%で爆発（最大基礎ダメージ450%）。呪い中の被ダメージ+24%。20秒CD"),
    ("Echoing Shade", "反響する影", "#2c3e50",
     "攻撃の15%でシャドウクローン召喚（20秒間、一部能力使用）。最大3体。クローンHP+100%"),
    ("Howler's Call", "ハウラーの呼び声", "#d35400",
     "通常攻撃の10%でスピリットウルフ召喚。経路上全敵に基礎ダメージ360%+1458。48%で3秒スタン。10秒CD"),
    ("Phoenix Ashes", "フェニックスの灰", "#e67e22",
     "致命ダメージ防止→基礎ダメージ1050%のシールドを6秒間。終了時残量の80%を回復。180秒CD"),
    ("Zwenson's Haunting", "ツヴェンソンの憑依", "#9b59b6",
     "敵撃破時にダークビースト召喚。周囲に基礎ダメージ120%+486。28%で追加召喚。6秒CD"),
    ("Frozen Heart", "フローズンハート", "#1abc9c",
     "被ダメージ時、基礎ダメージ360%+1458のシールドを6秒間。敵を冷却。攻撃に60%で冷却付与。20秒CD"),
    ("Maw of the Deep", "深淵の顎", "#2980b9",
     "ダメージ時に渦潮→2秒後に海獣噴出（基礎ダメージ450%+1701）。ノックアップ。6秒間被ダメージ+24%。20秒CD"),
    ("Gloom Cask", "グルームキャスク", "#34495e",
     "通常攻撃でグルームブレード:基礎ダメージ30%+275を6秒間。20秒CD。Rank2で36%"),
    ("Concentrated Will", "集中する意志", "#f1c40f",
     "ダッシュで守護天使が聖光（基礎ダメージ135%+547）。帰還時、与ダメージと移動速度+16%を2秒間。6秒CD"),
    ("Hellfire Fragment", "ヘルファイアの欠片", "#c0392b",
     "スキル使用で地獄の炎3つ召喚。6ヤード内に基礎ダメージ108%+510。複数ヒットで+50%。20秒CD"),
    ("Void Spark", "ヴォイドスパーク", "#8e44ad",
     "虚空エネルギーで敵にダメージ（詳細はゲーム内参照）"),
    ("Hilt of Many Realms", "多界の柄", "#7f8c8d",
     "ダメージ時に飛剣5本召喚（10秒間）。スキルで飛剣消費→ソードレイン。Rank3で大剣落下（+50%、ノックバック）。20秒CD"),
    ("Roiling Consequence", "ロイリングコンシクエンス", "#e67e22",
     "ダメージ時6秒間クリ率上昇。クリティカルで炎の爆発→基礎ダメージ36%燃焼3秒（1秒CD）。20秒CD"),
    ("Stormvault", "ストームヴォルト", "#3498db",
     "ダメージ時に嵐を6秒間召喚。0.5秒ごとに基礎ダメージ22.5%+203。20秒CD"),
]

# ─────────────────────────────────────────────
# 星カテゴリごとの共通ステータス (Rank 10)
# ─────────────────────────────────────────────
STAR_META = {
    "1star": {
        "label": "★1",
        "gems": GEMS_1STAR,
        "cr": "44",
        "resonance": "150",
        "magic_find": "+5%",
        "accent": "#a0a0a0",
    },
    "2star": {
        "label": "★2",
        "gems": GEMS_2STAR,
        "cr": "66",
        "resonance": "300",
        "magic_find": "+10%",
        "accent": "#4ade80",
    },
    "5star": {
        "label": "★5",
        "gems": GEMS_5STAR,
        "cr": "240 (5/5★)",
        "resonance": "1000 (5/5★)",
        "magic_find": "+15%",
        "accent": "#fbbf24",
    },
}


# ─────────────────────────────────────────────
# SVG アイコン生成
# ─────────────────────────────────────────────
def gem_svg(color: str) -> str:
    c = color.lstrip("#")
    return (
        f'<svg width="36" height="36" viewBox="0 0 36 36">'
        f'<defs><radialGradient id="rg{c}" cx="35%" cy="35%">'
        f'<stop offset="0%" stop-color="{color}" stop-opacity=".9"/>'
        f'<stop offset="100%" stop-color="{color}" stop-opacity=".25"/>'
        f'</radialGradient></defs>'
        f'<circle cx="18" cy="18" r="16" fill="url(#rg{c})" '
        f'stroke="{color}" stroke-width="1.5"/>'
        f'<rect x="10" y="10" width="12" height="12" rx="2" '
        f'transform="rotate(45 18 18)" fill="{color}" opacity=".55"/>'
        f'<circle cx="13" cy="12" r="2.5" fill="#fff" opacity=".45"/>'
        f'</svg>'
    )


# ─────────────────────────────────────────────
# HTML テーブルセクション生成
# ─────────────────────────────────────────────
def build_section(key: str, meta: dict) -> str:
    accent = meta["accent"]
    rows = []
    for i, (en, jp, color, effect) in enumerate(meta["gems"]):
        bg = "rgba(255,255,255,.018)" if i % 2 == 0 else "transparent"
        rows.append(
            f'<tr style="background:{bg}">'
            f'<td class="c-icon">{gem_svg(color)}</td>'
            f'<td class="c-name">'
            f'<span class="jp">{h.escape(jp)}</span>'
            f'<span class="en">{h.escape(en)}</span></td>'
            f'<td class="c-star">'
            f'<span class="badge" style="color:{accent};'
            f'background:{accent}18;border:1px solid {accent}44">'
            f'{meta["label"]}</span></td>'
            f'<td class="c-fx">{h.escape(effect)}</td></tr>'
        )

    return (
        f'<section id="{key}">'
        f'<div class="sec-head" style="border-left:4px solid {accent}">'
        f'<h2 style="color:{accent}">{meta["label"]} レジェンダリー宝石'
        f' <small>({len(meta["gems"])}個)</small></h2>'
        f'<div class="badges">'
        f'<span class="sb">戦闘レーティング: '
        f'<b style="color:{accent}">{meta["cr"]}</b></span>'
        f'<span class="sb">レゾナンス: '
        f'<b style="color:{accent}">{meta["resonance"]}</b></span>'
        f'<span class="sb">Magic Find: '
        f'<b style="color:{accent}">{meta["magic_find"]}</b></span>'
        f'</div></div>'
        f'<table><thead><tr>'
        f'<th style="width:48px">Icon</th>'
        f'<th style="width:210px">宝石名</th>'
        f'<th style="width:72px">星</th>'
        f'<th>Rank 10 性能</th>'
        f'</tr></thead><tbody>{"".join(rows)}</tbody></table></section>'
    )


# ─────────────────────────────────────────────
# 全体 HTML 構築
# ─────────────────────────────────────────────
def build_html() -> str:
    sections = "\n".join(build_section(k, v) for k, v in STAR_META.items())

    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Diablo Immortal – レジェンダリー宝石一覧 (Rank 10)</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{
  background:#08080d;color:#d8d8d8;
  font-family:"Segoe UI","Noto Sans JP","Hiragino Sans",sans-serif;
  padding:24px 16px;line-height:1.65;
}}
.wrap{{max-width:1020px;margin:0 auto}}
h1{{
  text-align:center;font-size:30px;font-weight:800;letter-spacing:3px;
  background:linear-gradient(90deg,#ff4444,#ff8844,#ffcc44);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}}
.sub{{text-align:center;color:#555;font-size:13px;margin:4px 0 20px}}
.nav{{display:flex;justify-content:center;gap:10px;margin-bottom:28px;flex-wrap:wrap}}
.nav a{{
  padding:9px 22px;border-radius:8px;text-decoration:none;
  font-weight:700;font-size:14px;border:2px solid #333;
  background:#0e0e14;color:#777;transition:.2s;
}}
.nav a:hover{{border-color:#666;color:#bbb}}
.nav .a1{{border-color:#a0a0a0;color:#a0a0a0;background:#a0a0a00d}}
.nav .a2{{border-color:#4ade80;color:#4ade80;background:#4ade800d}}
.nav .a5{{border-color:#fbbf24;color:#fbbf24;background:#fbbf240d}}
section{{margin-bottom:36px}}
.sec-head{{
  padding:14px 18px;background:rgba(255,255,255,.025);
  border-radius:8px;margin-bottom:12px;
}}
.sec-head h2{{font-size:19px;margin-bottom:6px}}
.sec-head small{{font-weight:400;font-size:14px;opacity:.7}}
.badges{{display:flex;gap:10px;flex-wrap:wrap}}
.sb{{
  padding:3px 10px;border-radius:5px;font-size:12px;
  background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);
}}
table{{width:100%;border-collapse:collapse;border-radius:8px;overflow:hidden}}
thead{{background:rgba(255,255,255,.04)}}
th{{
  padding:9px 10px;text-align:left;font-size:12px;
  color:#777;font-weight:600;border-bottom:1px solid #1c1c1c;
}}
td{{padding:9px 10px;border-bottom:1px solid #141418;vertical-align:middle}}
.c-icon{{width:48px;text-align:center}}
.c-name{{width:210px}}
.c-name .jp{{display:block;font-size:14px;font-weight:700;color:#fff}}
.c-name .en{{display:block;font-size:10.5px;color:#777;margin-top:1px}}
.c-star{{width:72px;text-align:center}}
.badge{{
  display:inline-block;padding:2px 8px;border-radius:4px;
  font-size:11px;font-weight:700;
}}
.c-fx{{font-size:13px;color:#bbb;line-height:1.55}}
.foot{{text-align:center;color:#444;font-size:11px;margin-top:20px;line-height:1.7}}
.foot a{{color:#fbbf24}}
@media(max-width:700px){{
  .c-name{{width:140px}}.c-name .en{{display:none}}.c-fx{{font-size:12px}}
}}
</style>
</head>
<body>
<div class="wrap">
<h1>DIABLO IMMORTAL</h1>
<p class="sub">レジェンダリー宝石一覧 — 全 Rank 10 性能</p>
<nav class="nav">
  <a class="a1" href="#1star">★1 宝石 ({len(GEMS_1STAR)})</a>
  <a class="a2" href="#2star">★2 宝石 ({len(GEMS_2STAR)})</a>
  <a class="a5" href="#5star">★5 宝石 ({len(GEMS_5STAR)})</a>
</nav>
{sections}
<p class="foot">
※ 数値は Rank 10（5星宝石は 5/5★）時点の情報です。<br>
※ ゲームのアップデートにより変更される場合があります。<br>
※ 最新の正確な値は <a href="https://diablo.tv/legendary-gems">diablo.tv</a> で確認してください。<br>
出典: MisterMenPlays.com / GINX / Game8
</p>
</div>
</body>
</html>'''


# ─────────────────────────────────────────────
# メイン実行
# ─────────────────────────────────────────────
def main():
    out_dir = "/mnt/user-data/outputs"
    os.makedirs(out_dir, exist_ok=True)

    # HTML 出力
    html_path = os.path.join(out_dir, "diablo_immortal_gems.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(build_html())

    # Python スクリプト自身もコピー
    script_src = os.path.abspath(__file__)
    script_dst = os.path.join(out_dir, "diablo_immortal_gems.py")
    if os.path.abspath(script_src) != os.path.abspath(script_dst):
        import shutil
        shutil.copy2(script_src, script_dst)

    total = len(GEMS_1STAR) + len(GEMS_2STAR) + len(GEMS_5STAR)
    print(f"✅ HTML 生成完了: {html_path}")
    print(f"   ★1: {len(GEMS_1STAR)}個 / ★2: {len(GEMS_2STAR)}個 / ★5: {len(GEMS_5STAR)}個")
    print(f"   合計: {total}個")


if __name__ == "__main__":
    main()