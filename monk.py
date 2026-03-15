#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

print("Content-Type: text/html; charset=utf-8")
print()

MAIN_ATTACKS = ["雷鳴拳", "長手拳"]

SKILLS = [
    "七星死戯", "双身", "天鐘", "拘禁拳", "波状撃",
    "爆裂掌", "瞬撃", "禅定障壁", "竜巻天翔", "聖域",
    "飛翔脚", "飛龍拳", "天の息吹"
]

ESSENCES = {
    "頭": [
        {"skill": "爆裂掌", "name": "萎縮の洞察", "desc": "〈爆裂掌〉のチャージ上限が1増加。爆裂掌のクールダウン時間が短縮:3.6%"},
        {"skill": "聖域", "name": "エンパシーの祝福", "desc": "〈聖域〉が〈祝福の聖域〉になり、内部にいる自分と味方の予ダメージが増加する。聖域のクールダウン時間が短縮:7.2%"},
        {"skill": "聖域", "name": "山々の癒やし", "desc": "〈聖域〉が冷却の輪となり、その中にいる敵に連続ダメージと冷却効果を与える。ただし、自分と味方へのシールドはなくなる。聖域のダメージが増加:18.0%"},
        {"skill": "聖域", "name": "静寂の眼差し", "desc": "〈聖域〉発動時、円陣に出入りする敵にダメージを与え、スタン状態にさせるようになる。ただし自分と味方へのシールドはなくなる。聖域のダメージが増加:18.0%"},
        {"skill": "双身", "name": "開かれし心", "desc": "〈双身〉のダメージが19%増加。"},
        {"skill": "禅定障壁", "name": "清浄なる思考", "desc": "〈禅定障壁〉発動時、状態異常を受けなくなる。禅定障壁のクールダウン時間が短縮:3.6%"},
        {"skill": "聖域", "name": "裁きの監視", "desc": "〈聖域〉発動時、範囲内の敵すべてに連続ダメージを与えるようになる。ただし、自分と味方へのシールドはなくなる。聖域のダメージが増加:18.0%"},
        {"skill": "禅定障壁", "name": "深慮の冠", "desc": "〈禅定障壁〉の持続時間が39%増加。"},
        {"skill": "爆裂掌", "name": "麻痺の具現化", "desc": "〈爆裂掌〉の出血効果が、追加の攻撃によって30%の確率で爆発するようになる。爆裂掌のクールダウン時間が短縮:3.6%"},
        {"skill": "双身", "name": "融合の王冠", "desc": "〈双身〉が詠唱者を守るようになり、自身が受けるダメージの29%を肩代わりする。"},
        {"skill": "聖域", "name": "不体裁", "desc": "〈聖域〉が、エリア内の敵が石化されるまで、敵の移動速度低下を蓄積させる。聖域のダメージが増加:18.0%"},
        {"skill": "聖域", "name": "鼓舞せし巨人", "desc": "〈聖域〉が範囲内で敵の移動速度と攻撃速度を低下させ、自信と味方の移動速度と攻撃速度を上昇させる。聖域のクールダウン時間が短縮:7.2%"},
        {"skill": "双身", "name": "復活の気運", "desc": "敵を倒すと、〈双身〉の効果時間が0.4秒増加するようになる。最大6.4秒。"},
        {"skill": "爆裂掌", "name": "ラストレヴェラー", "desc": "〈爆裂掌〉の効果を受けた敵にダメージを与えると、持続時間が0.8秒延長する。最大で6.4秒間まで。"},
        {"skill": "聖域", "name": "悲哀の鐘兜", "desc": "〈聖域〉を発動すると霊性を帯びた領域を作り出すようになる。その中にいる敵は移動速度が大幅に低下し、ダッシュスキルを使用できなくなる。聖域のダメージが増加：18.0%"},
        {"skill": "双身", "name": "陰気な入り江", "desc": "〈双身〉が能力の劣る分身を追加で1体召喚するようになる。"}
    ],
    "肩": [
        {"skill": "飛翔脚", "name": "鶴の肩鎧", "desc": "〈飛翔脚〉の範囲が20%増加。"},
        {"skill": "天鐘", "name": "天の絆", "desc": "〈天鐘〉発動時、天から黄金の鐘が飛来し、範囲内のすべての敵に移動障害効果を与えるようになる。"},
        {"skill": "拘禁拳", "name": "血流沸騰", "desc": "〈拘禁拳〉発動時、電気を帯びて空中に飛び上がり、着地地点付近の敵にダメージと移動障害効果を与えるようになる。"},
        {"skill": "七星死戯", "name": "規律の重圧", "desc": "〈七星死戯〉のダメージが10%増加。"},
        {"skill": "七星死戯", "name": "ファースト・ウィンド", "desc": "〈七星死戯〉が一撃当たるごとに、受ける全ダメージを一時的に3.5%減少させる。減少は最大7回まで蓄積する。"},
        {"skill": "天鐘", "name": "輝ける太陽", "desc": "〈天鐘〉発動時、〈残響鐘〉を呼び出すようになり、付近の敵すべてに継続的にダメージを与えるが、チャージは1回限りとなる。"},
        {"skill": "拘禁拳", "name": "自由の疾風", "desc": "〈拘禁拳〉発動時、周囲の敵を空中に打ち上げてスタン状態にするようになるが、移動障害効果は発生しなくなる。"},
        {"skill": "拘禁拳", "name": "忍耐の権威", "desc": "〈拘禁拳〉発動時、一定の方向に突撃する。チャージすると範囲とダメージが増加する。"},
        {"skill": "拘禁拳", "name": "終わりなき試練", "desc": "〈拘禁拳〉が連続でパンチを繰り出し、さらに使用中に方向を変えられるようになる。使用中は徐々にエネルギーが消費されるが、使用をやめると回復する。"},
        {"skill": "天鐘", "name": "シマーリン", "desc": "〈天鐘〉がエネルギー波を放ち、軌道上のすべての敵にダメージを与え、炎上させるようになるが、チャージは1回限りとなる。"},
        {"skill": "瞬撃", "name": "昇雲", "desc": "〈瞬撃〉使用時、3秒間、回避率が20％上昇する。"},
        {"skill": "天鐘", "name": "猛火の沐浴", "desc": "〈天鐘〉発動時、複数の金色の鐘を呼び出すようになる。自身か味方のメイン攻撃で鐘を叩けば、共鳴により付近のすべての敵にダメージを与えられる。"},
        {"skill": "瞬撃", "name": "舞い降りし宿命", "desc": "〈瞬撃〉により、4秒以内に使用した次のスキルのダメージが30％増加する。"},
        {"skill": "瞬撃", "name": "猫族の反抗", "desc": "〈瞬撃〉にメイン攻撃の速度を6.4秒間、30%上昇させる効果が加わる。"},
        {"skill": "天鐘", "name": "ヴィルナスの肩当て", "desc": "〈天鐘〉が詠唱系スキルに変化し、前方に落とした黄金の鐘を攻撃し続けて近くにいるすべての敵にダメージを与えるようになる。天鐘のダメージが増加：18.0%"},
        {"skill": "飛翔脚", "name": "放たれた川", "desc": "シールドを持つ敵に〈飛翔脚〉が与えるダメージが350%増加する。"}
    ],
    "胴": [
        {"skill": "竜巻天翔", "name": "テンペストハート", "desc": "〈竜巻天翔〉を使うと竜巻と化し、敵を引き寄せてから爆発して付近の敵すべてにダメージを与え、ノックバックするようになる。"},
        {"skill": "竜巻天翔", "name": "ストームスピリット", "desc": "〈竜巻天翔〉発動時、強力な竜巻を生み出し、付近の敵すべてに連続で攻撃を加えるようになる。"},
        {"skill": "波状撃", "name": "響き渡る魂", "desc": "〈波状撃〉のダメージが10%増加。"},
        {"skill": "七星死戯", "name": "香の息吹", "desc": "〈七星死戯〉で流血状態の敵を倒すと〈爆裂掌〉を発動できるようになる。"},
        {"skill": "聖域", "name": "眼前の平穏", "desc": "〈聖域〉が自分と付近の味方すべてにシールド効果を与え、シールドがxxxxのダメージを吸収する。"},
        {"skill": "天鐘", "name": "調和の歌", "desc": "〈天鐘〉の範囲が20%増加。"},
        {"skill": "聖域", "name": "規律ある休見", "desc": "〈聖域〉のクールダウン時間が15%短縮。"},
        {"skill": "禅定障壁", "name": "啓発の祝福", "desc": "〈禅定障壁〉発動中、移動速度が25%上昇し、敵をすり抜けて移動できるようになる。"},
        {"skill": "竜巻天翔", "name": "テュフロット・ローブ", "desc": "〈竜巻天翔〉が敵に視界を遮り、ダメージを与える砂嵐を発生させるようになる。"},
        {"skill": "禅定障壁", "name": "平和の誓約", "desc": "〈禅定障壁〉の発動中にダメージを受けると、一定の確率でカウンター攻撃が発動し、付近のすべての敵にxxxxのダメージを与える。"},
        {"skill": "飛龍拳", "name": "痛切なる装具", "desc": "〈飛龍拳〉で前方へダッシュするようになり、進路上のすべての敵をノックバックさせ、スタンさせる。"},
        {"skill": "七星死戯", "name": "再びの萌芽", "desc": "〈七星死戯〉に、xxxxダメージを吸収するシールド効果が加わる。"},
        {"skill": "波状撃", "name": "整列の黒曜石", "desc": "操作障害効果を受けている敵への〈波状撃〉のダメージが20％増加する。"},
        {"skill": "聖域", "name": "真夜中の鐘", "desc": "〈聖域〉がさらに、範囲内の味方にノックバック耐性を与えるようになる。聖域のクールダウン時間が短縮:3.6%"},
        {"skill": "飛龍拳", "name": "高貴なる道", "desc": "〈飛龍拳〉を発動すると標的エリアに巨大な上昇気流を発生させ、エリア内のすべての敵を宙に浮かせるようになる。敵に命中したあとで〈飛龍拳〉を再度発動すると、敵の位置にテレポートして連続キックを繰り出し、ダメージを与えつつスタンさせる。飛龍拳のダメージが増加：18.0%"},
        {"skill": "竜巻天翔", "name": "冬の抱擁", "desc": "〈竜巻天翔〉が冷気の風で強化され、ダメージを与えると同時に付近の敵を引き寄せて凍結させるようになるが、チャージできなくなる。"}
    ],
    "脚": [
        {"skill": "飛翔脚", "name": "猛虎の飛翔", "desc": "〈飛翔脚〉発動時、炎の竜巻を生み、軌道上の敵にダメージを与えるようになる。"},
        {"skill": "竜巻天翔", "name": "嵐の道", "desc": "〈竜巻天翔〉がすべての被ダメージを一時的に20%減少させる。"},
        {"skill": "飛翔脚", "name": "気品の恵み", "desc": "〈飛翔脚〉が〈旋回脚〉に変化し、付近の敵すべてにダメージを与える。"},
        {"skill": "飛翔脚", "name": "無窮の足運び", "desc": "〈飛翔脚〉発動時、軌道上の敵に蹴りを連発する。最後の1撃は敵をノックバックさせる。"},
        {"skill": "爆裂掌", "name": "内なるリズム", "desc": "〈爆裂掌〉の爆発ダメージが30%増加するが、初撃のダメージはなくなる。"},
        {"skill": "天鐘", "name": "光輝の折檻", "desc": "〈天鐘〉のダメージが10%増加。"},
        {"skill": "拘禁拳", "name": "孤立の道", "desc": "〈拘禁拳〉のチャージ上限が1増加。"},
        {"skill": "双身", "name": "使い魔の旋律", "desc": "〈双身〉の持続時間が30%増加。"},
        {"skill": "飛龍拳", "name": "スタービング・モスキート", "desc": "〈飛龍杖〉のダメージが命中した敵1体ごとに2%、最大20%まで増加。"},
        {"skill": "飛翔脚", "name": "不安定な塔", "desc": "〈飛翔脚〉発動時、敵をスタンさせる、より強力でチャージ可能な一撃を繰り出すようになる。"},
        {"skill": "瞬撃", "name": "旅叱り", "desc": "〈瞬撃〉発動時、指定地点に突進し、付近の敵すべてを突き上げてダメージを与えるようになる。"},
        {"skill": "瞬撃", "name": "燃える腰帯", "desc": "〈瞬撃〉発動時、一方方向に素早く動き、進路上の敵すべてにダメージを与えるようになる。"},
        {"skill": "瞬撃", "name": "ガーゲルの親密", "desc": "〈瞬撃〉が亡霊の味方を召喚するようになる。亡霊は前方に突進して、進路上の敵にダメージを与えて移動速度を低下させる。"},
        {"skill": "飛翔脚", "name": "救済の針", "desc": "〈飛翔脚〉が1体の敵に向けて強力な蹴りを放ち、大きくノックバックさせるようになる。蹴られた敵はぶつかった敵にもダメージを与え、小さくノックバックさせる。飛翔脚のダメージが増加:18.0%"},
        {"skill": "天鐘", "name": "砂漠の闊歩靴", "desc": "〈天鐘〉で2秒以内に敵1体へのダメージを与える毎に、その敵に与えるダメージが5.7%増加する。増加量は最大57%"},
        {"skill": "双身", "name": "苦難の贈り物", "desc": "〈双身〉が最大ライフの10%を消費して分身を強化するようになり、攻撃速度と移動速度が20%上昇する。"}
    ],
    "メインハンド": [
        {"skill": "波状撃", "name": "不動の重荷", "desc": "〈波状撃〉の半径が20%増加。"},
        {"skill": "七星死戯", "name": "花弁の氷片", "desc": "〈七星死戯〉が氷ダメージに変わり、冷気効果を与える。"},
        {"skill": "七星死戯", "name": "精霊の手", "desc": "〈七星死戯〉発動時、ルーンの円陣を描き、その中にいるすべての敵を亡霊の仲間が攻撃するようになる。"},
        {"skill": "七星死戯", "name": "竜の義憤", "desc": "〈七星死戯〉に敵を継続的に炎上させる効果が加わる。"},
        {"skill": "拘禁拳", "name": "ウィズダム・グラスプ", "desc": "〈拘禁拳〉のダメージが10%上昇。"},
        {"skill": "双身", "name": "反響の杖", "desc": "〈双身〉のクールダウンが15%短縮される。"},
        {"skill": "禅定障壁", "name": "法の介入", "desc": "〈禅定障壁〉が指定地点でチャージされるようになり、自分と付近の味方にダメージを吸収する障壁を付与する。"},
        {"skill": "禅定障壁", "name": "平和の炎", "desc": "〈禅定障壁〉の障壁効果がなくなるが、付近の敵に定期的にダメージを与えるようになる。"},
        {"skill": "七星死戯", "name": "拳闘家の存在", "desc": "〈七星死戯〉が攻撃を同一方向に何度も繰り出し、各パンチが敵をノックバックさせるようになる。"},
        {"skill": "双身", "name": "はかなき魂", "desc": "〈双身〉発動時、分身が一方向に突進するようになり、貫通した敵にダメージを与え、近くの敵に分身を攻撃させる。"},
        {"skill": "長手拳", "name": "比類なき導き", "desc": "〈長手拳〉の３ヒット目が敵を宙に打ち上げてxxxxのダメージを与えるようになる。"},
        {"skill": "雷鳴拳", "name": "不屈の経典", "desc": "〈雷鳴拳〉でダメージを与えるたびに10％の確率で電気を帯び、1秒間、メイン攻撃の速度が50％増加する。"},
        {"skill": "長手拳", "name": "アセンダントの円弧", "desc": "〈長手拳〉が25％の確率で敵を脆弱状態にし、2秒間、敵が受けるダメージを10％増加させる。"},
        {"skill": "七星死戯", "name": "薄闇の掌握", "desc": "〈七星死戯〉を使用すると、メイン攻撃で精霊が呼び出されるようになる。精霊は標的に強力な攻撃を放ち、その途中にいる敵にもダメージを与える。七星死戯のダメージが増加:18.0%"},
        {"skill": "雷鳴拳", "name": "罪なき秩序", "desc": "〈雷鳴拳〉のフルコンボの最後の一撃が電撃の球を発生させるようになる。この電撃球は4,706の継続ダメージを与える。ダメージ増加90.0%"},
        {"skill": "双身", "name": "サープテブのランプライター", "desc": "〈双身〉が2体の炎の分身を召喚するようになる。炎の分身は付近の敵を炎上させる。"}
    ],
    "オフハンド": [
        {"skill": "波状撃", "name": "衝撃波の籠手", "desc": "〈波状撃〉が継続的に複数のエネルギー波を前方に放つようになる。"},
        {"skill": "飛翔脚", "name": "ホイールスポーク", "desc": "〈飛翔脚〉により、与える全ダメージが一時的に10%増加する。"},
        {"skill": "竜巻天翔", "name": "台風の目", "desc": "〈竜巻天翔〉の範囲が20%拡大する。"},
        {"skill": "波状撃", "name": "海原の咆哮", "desc": "〈波状撃〉が速やかにエネルギーを集めて〈爆発波〉を発生させるようになる。最大チャージが2回になる。"},
        {"skill": "爆裂掌", "name": "追い迫る叱責", "desc": "〈爆裂掌〉発動時、指定地点に跳躍し、着地時に巨大な掌を叩きつけて付近の敵すべてにダメージを与えるようになる。その一方でクールダウン時間は増加する。"},
        {"skill": "爆裂掌", "name": "現在の道", "desc": "〈爆裂掌〉発動時、巨大な掌を放ち、軌道上の敵すべてにダメージを与える。"},
        {"skill": "聖域", "name": "休息の溜息", "desc": "〈聖域〉の持続時間が30%増加する。"},
        {"skill": "爆裂掌", "name": "スコルディング・ストーム", "desc": "〈爆裂掌〉が氷結属性になり、氷結効果を与えるようになる。"},
        {"skill": "波状撃", "name": "ラトリング・アーム", "desc": "〈波状撃〉が気の球となり、敵を引き寄せて連続的にダメージを与える。"},
        {"skill": "爆裂掌", "name": "邪悪なる集結", "desc": "〈爆裂掌〉が近くの敵を真正面に集めるようになる。チャージは最大で1回まで。"},
        {"skill": "波状撃", "name": "意趣の潮衝", "desc": "〈波状撃〉が周囲の敵を宙に打ち上げてダメージを与え、スタンさせる衝撃波を地面に放つようになる。"},
        {"skill": "雷鳴拳", "name": "収縮掌", "desc": "〈雷鳴拳〉の最初一撃が稲妻で強化され、それぞれがxxxxのダメージを与える雷撃を放つ。"},
        {"skill": "波状撃", "name": "うねり柳", "desc": "〈波状撃〉が、エリア内の敵にダメージを与える大きなエネルギーを即時に放つようになる。"},
        {"skill": "波状撃", "name": "幾多なる震えの柱", "desc": "〈波状撃〉を使用すると、メイン攻撃が爆発を起こして付近の敵にダメージを与えるようになる。波攻撃のダメージが増加:18.0%"},
        {"skill": "飛龍拳", "name": "ヴェデニンの刺突", "desc": "〈飛龍拳〉発動時、敵に向かって突進し、ダメージを与えながら貫き通す。"},
        {"skill": "瞬撃", "name": "無口な風", "desc": "〈瞬撃〉発動時、3秒間姿が見えなくなる。"}
    ]
}

SLOT_LIMITS = {"頭": 1, "肩": 1, "胴": 1, "脚": 1, "メインハンド": 2, "オフハンド": 2}
SLOT_ICONS = {"頭": "🪖", "肩": "🦺", "胴": "🛡️", "脚": "👟", "メインハンド": "👊", "オフハンド": "🪬"}

essences_json = json.dumps(ESSENCES, ensure_ascii=False)
limits_json = json.dumps(SLOT_LIMITS, ensure_ascii=False)
main_attacks_json = json.dumps(MAIN_ATTACKS, ensure_ascii=False)
skills_json = json.dumps(SKILLS, ensure_ascii=False)

HTML = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>モンク もぐらリサーチ精髄チェッカー</title>
<style>
  :root {{
    --bg-primary: #f0f4f8;
    --bg-secondary: #ffffff;
    --bg-card: #ffffff;
    --bg-card-hover: #fffbeb;
    --accent: #d97706;
    --accent-glow: rgba(217,119,6,0.18);
    --accent2: #b45309;
    --gold: #d97706;
    --gold-dark: #92400e;
    --text-primary: #1a202c;
    --text-secondary: #4a5568;
    --text-muted: #a0aec0;
    --border: #e2e8f0;
    --border-accent: rgba(217,119,6,0.3);
    --selected-bg: rgba(217,119,6,0.07);
    --selected-border: #d97706;
    --slot-head: #dc2626;
    --slot-shoulder: #9333ea;
    --slot-chest: #2563eb;
    --slot-legs: #0d9488;
    --slot-main: #d97706;
    --slot-off: #db2777;
    --shadow: 0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.05);
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Segoe UI', 'Noto Sans JP', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    min-height: 100vh;
    line-height: 1.6;
  }}
  header {{
    background: linear-gradient(135deg, #713f12 0%, #422006 100%);
    border-bottom: 2px solid rgba(255,255,255,0.08);
    padding: 0.85rem 1.5rem;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 12px rgba(0,0,0,0.3);
  }}
  .header-inner {{
    max-width: 1600px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    gap: 1rem;
  }}
  .back-btn {{
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    color: rgba(255,255,255,0.65);
    text-decoration: none;
    font-size: 0.78rem;
    padding: 0.3rem 0.75rem;
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 20px;
    transition: all 0.2s;
    white-space: nowrap;
  }}
  .back-btn:hover {{ color: white; border-color: rgba(255,255,255,0.5); background: rgba(255,255,255,0.08); }}
  .header-title {{
    flex: 1;
    text-align: center;
  }}
  .header-title h1 {{
    font-size: clamp(0.95rem, 2.5vw, 1.3rem);
    font-weight: 700;
    background: linear-gradient(90deg, #fde68a, #fed7aa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 0.05em;
  }}
  .header-title p {{ color: rgba(255,255,255,0.5); font-size: 0.75rem; margin-top: 0.1rem; }}
  .header-spacer {{ width: 80px; }}

  #selected-panel {{
    background: linear-gradient(135deg, #fffbeb, #fef3c7);
    border-bottom: 2px solid var(--border);
    padding: 0.75rem 1.5rem;
    display: none;
    box-shadow: var(--shadow);
  }}
  #selected-panel h2 {{
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--gold-dark);
    margin-bottom: 0.6rem;
  }}
  #selected-list {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
  }}
  .selected-tag {{
    display: flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(146,64,14,0.08);
    border: 1px solid rgba(146,64,14,0.3);
    border-radius: 20px;
    padding: 0.25rem 0.75rem;
    font-size: 0.75rem;
    cursor: pointer;
    transition: all 0.2s;
    color: var(--text-primary);
  }}
  .selected-tag:hover {{ background: rgba(146,64,14,0.15); }}
  .selected-tag .slot-badge {{ font-size: 0.65rem; opacity: 0.7; }}
  .selected-tag .remove-btn {{ opacity: 0.45; font-size: 0.8rem; margin-left: 0.2rem; }}
  .selected-tag:hover .remove-btn {{ opacity: 1; }}

  main {{
    max-width: 1600px;
    margin: 0 auto;
    padding: 1.5rem;
  }}
  .skill-section, .bookmark-section {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    box-shadow: var(--shadow);
  }}
  .section-title {{
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }}
  .section-title.amber {{ color: var(--accent); }}
  .section-title.gold {{ color: var(--gold-dark); }}
  .section-title::before {{
    content: '';
    display: block;
    width: 3px;
    height: 1em;
    border-radius: 2px;
    background: currentColor;
  }}
  .skill-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 0.8rem;
  }}
  .skill-slot {{ display: flex; flex-direction: column; gap: 0.35rem; }}
  .skill-slot label {{
    font-size: 0.72rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
  }}
  .skill-slot select {{
    background: var(--bg-secondary);
    color: var(--text-primary);
    border: 1.5px solid var(--border);
    border-radius: 8px;
    padding: 0.5rem 2rem 0.5rem 0.75rem;
    font-size: 0.85rem;
    cursor: pointer;
    transition: border-color 0.2s, box-shadow 0.2s;
    width: 100%;
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='%23d97706'%3E%3Cpath d='M7 10l5 5 5-5z'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    box-shadow: var(--shadow);
  }}
  .skill-slot select:focus {{
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 3px var(--accent-glow);
  }}
  .skill-slot select.has-value {{ border-color: var(--accent); color: var(--accent); font-weight: 600; }}

  .bookmark-section {{ padding: 1.25rem 1.5rem; }}
  .bookmark-actions {{
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 0.75rem;
    flex-wrap: wrap;
  }}
  #bookmark-name-input {{
    flex: 1;
    min-width: 180px;
    border: 1.5px solid var(--border);
    border-radius: 8px;
    padding: 0.45rem 0.75rem;
    font-size: 0.85rem;
    color: var(--text-primary);
    background: var(--bg-secondary);
    box-shadow: var(--shadow);
    transition: border-color 0.2s, box-shadow 0.2s;
  }}
  #bookmark-name-input:focus {{
    outline: none;
    border-color: var(--gold);
    box-shadow: 0 0 0 3px rgba(217,119,6,0.15);
  }}
  #save-bookmark-btn {{
    background: linear-gradient(135deg, var(--gold-dark), #f59e0b);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.48rem 1.2rem;
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    box-shadow: var(--shadow);
    white-space: nowrap;
  }}
  #save-bookmark-btn:hover {{ transform: translateY(-1px); box-shadow: var(--shadow-md); }}
  #bookmark-list {{ display: flex; flex-wrap: wrap; gap: 0.5rem; min-height: 1.5rem; }}
  .bookmark-tag {{
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background: #fef3c7;
    border: 1px solid #fcd34d;
    border-radius: 20px;
    padding: 0.3rem 0.5rem 0.3rem 0.9rem;
    font-size: 0.78rem;
    cursor: pointer;
    transition: all 0.2s;
    color: #78350f;
  }}
  .bookmark-tag:hover {{ background: #fde68a; border-color: #f59e0b; }}
  .bookmark-tag .bm-name {{ font-weight: 600; }}
  .bookmark-tag .bm-date {{ font-size: 0.68rem; opacity: 0.65; }}
  .bookmark-tag .bm-delete {{ opacity: 0.45; font-size: 0.72rem; padding: 0.1rem 0.3rem; border-radius: 50%; transition: all 0.15s; }}
  .bookmark-tag .bm-delete:hover {{ opacity: 1; background: rgba(0,0,0,0.1); }}
  .bookmark-empty {{ font-size: 0.8rem; color: var(--text-muted); }}

  .search-wrap {{ text-align: center; margin: 1.25rem 0; }}
  #search-btn {{
    background: linear-gradient(135deg, #92400e, var(--accent));
    color: white;
    border: none;
    border-radius: 30px;
    padding: 0.85rem 3rem;
    font-size: 1rem;
    font-weight: 700;
    cursor: pointer;
    letter-spacing: 0.05em;
    transition: all 0.3s;
    box-shadow: 0 4px 20px rgba(217,119,6,0.3);
    position: relative;
    overflow: hidden;
  }}
  #search-btn::before {{
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s;
  }}
  #search-btn:hover::before {{ left: 100%; }}
  #search-btn:hover {{ transform: translateY(-2px); box-shadow: 0 6px 30px rgba(217,119,6,0.45); }}
  #search-btn:active {{ transform: translateY(0); }}

  #results {{ display: none; }}
  .tooltip-hint {{ font-size: 0.72rem; color: var(--text-muted); text-align: center; margin-bottom: 0.75rem; }}

  .slots-grid {{
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 0.75rem;
  }}
  @media (max-width: 1400px) {{ .slots-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
  @media (max-width: 900px) {{ .slots-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
  @media (max-width: 560px) {{ .slots-grid {{ grid-template-columns: 1fr; }} }}

  .slot-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    transition: border-color 0.2s, box-shadow 0.2s;
    box-shadow: var(--shadow);
    animation: fadeIn 0.25s ease both;
  }}
  .slot-card:hover {{ border-color: var(--border-accent); box-shadow: var(--shadow-md); }}
  .slot-card:nth-child(1) {{ animation-delay: 0.03s; }}
  .slot-card:nth-child(2) {{ animation-delay: 0.06s; }}
  .slot-card:nth-child(3) {{ animation-delay: 0.09s; }}
  .slot-card:nth-child(4) {{ animation-delay: 0.12s; }}
  .slot-card:nth-child(5) {{ animation-delay: 0.15s; }}
  .slot-card:nth-child(6) {{ animation-delay: 0.18s; }}
  .slot-header {{
    padding: 0.65rem 0.9rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid var(--border);
    background: #f8fafc;
  }}
  .slot-title {{ display: flex; align-items: center; gap: 0.4rem; font-weight: 700; font-size: 0.9rem; }}
  .slot-limit {{
    font-size: 0.68rem;
    background: rgba(0,0,0,0.05);
    border-radius: 10px;
    padding: 0.12rem 0.45rem;
    color: var(--text-secondary);
    white-space: nowrap;
  }}
  .slot-limit.at-limit {{ background: rgba(217,119,6,0.1); color: var(--accent); font-weight: 700; }}
  .slot-essences {{ padding: 0.4rem; }}
  .essence-count {{ font-size: 0.68rem; color: var(--text-muted); padding: 0.25rem 0.4rem; text-align: right; }}
  .no-essences {{ padding: 1.25rem; text-align: center; color: var(--text-muted); font-size: 0.82rem; }}

  .essence-card {{
    border: 1.5px solid transparent;
    border-radius: 8px;
    padding: 0.6rem 0.65rem;
    cursor: pointer;
    transition: all 0.15s;
    margin-bottom: 0.3rem;
    user-select: none;
  }}
  .essence-card:last-child {{ margin-bottom: 0; }}
  .essence-card:hover {{ background: #fffbeb; border-color: rgba(217,119,6,0.2); }}
  .essence-card.selected {{
    background: var(--selected-bg);
    border-color: var(--selected-border);
    box-shadow: 0 0 0 1px var(--selected-border) inset;
  }}
  .essence-card.disabled {{ opacity: 0.3; cursor: not-allowed; pointer-events: none; }}
  .essence-name {{
    font-weight: 600;
    font-size: 0.84rem;
    color: var(--text-primary);
    margin-bottom: 0.2rem;
    display: flex;
    align-items: center;
    gap: 0.35rem;
    line-height: 1.3;
  }}
  .essence-name .check-icon {{ color: var(--accent); font-size: 0.72rem; display: none; flex-shrink: 0; }}
  .essence-card.selected .check-icon {{ display: inline; }}
  .essence-skill {{ font-size: 0.68rem; color: var(--text-muted); margin-bottom: 0.25rem; }}
  .essence-skill span {{
    color: var(--accent);
    background: rgba(217,119,6,0.07);
    padding: 0.08rem 0.35rem;
    border-radius: 4px;
    font-weight: 600;
  }}
  .essence-desc {{ font-size: 0.72rem; color: var(--text-secondary); line-height: 1.5; }}

  .slot-card[data-slot="頭"] .slot-header {{ border-left: 3px solid var(--slot-head); }}
  .slot-card[data-slot="肩"] .slot-header {{ border-left: 3px solid var(--slot-shoulder); }}
  .slot-card[data-slot="胴"] .slot-header {{ border-left: 3px solid var(--slot-chest); }}
  .slot-card[data-slot="脚"] .slot-header {{ border-left: 3px solid var(--slot-legs); }}
  .slot-card[data-slot="メインハンド"] .slot-header {{ border-left: 3px solid var(--slot-main); }}
  .slot-card[data-slot="オフハンド"] .slot-header {{ border-left: 3px solid var(--slot-off); }}

  @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: translateY(0); }} }}
  @media (max-width: 600px) {{
    main {{ padding: 0.75rem; }}
    .skill-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .header-inner {{ gap: 0.5rem; }}
  }}

  /* ===== 効果検索 ===== */
  .effect-search-section {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
    box-shadow: var(--shadow);
  }}
  .effect-search-actions {{
    display: flex;
    align-items: center;
    gap: 0.6rem;
    flex-wrap: wrap;
  }}
  #effect-search-input {{
    flex: 1;
    min-width: 220px;
    border: 1.5px solid var(--border);
    border-radius: 8px;
    padding: 0.45rem 0.75rem;
    font-size: 0.85rem;
    color: var(--text-primary);
    background: var(--bg-secondary);
    box-shadow: var(--shadow);
    transition: border-color 0.2s, box-shadow 0.2s;
  }}
  #effect-search-input:focus {{
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 3px var(--accent-glow);
  }}
  #effect-search-btn {{
    background: linear-gradient(135deg, var(--accent2), var(--accent));
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.48rem 1.2rem;
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    box-shadow: var(--shadow);
    white-space: nowrap;
  }}
  #effect-search-btn:hover {{ transform: translateY(-1px); box-shadow: var(--shadow-md); }}
  #effect-search-clear-btn {{
    background: #f1f5f9;
    color: var(--text-secondary);
    border: 1.5px solid var(--border);
    border-radius: 8px;
    padding: 0.48rem 0.9rem;
    font-size: 0.85rem;
    cursor: pointer;
    transition: all 0.2s;
    white-space: nowrap;
  }}
  #effect-search-clear-btn:hover {{ background: #e2e8f0; }}
  #effect-search-results {{ margin-top: 1rem; }}
  .effect-result-summary {{ font-size: 0.8rem; color: var(--text-secondary); margin-bottom: 0.75rem; }}
  .effect-result-summary strong {{ color: var(--accent); }}
  .effect-no-results {{ font-size: 0.82rem; color: var(--text-muted); padding: 0.5rem 0; }}
  .effect-slot-group {{ margin-bottom: 0.85rem; }}
  .effect-slot-label {{
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-secondary);
    margin-bottom: 0.35rem;
    display: flex;
    align-items: center;
    gap: 0.3rem;
    padding: 0.25rem 0;
    border-bottom: 1px solid var(--border);
  }}
  .effect-essence-card {{
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.55rem 0.65rem;
    margin-bottom: 0.3rem;
    background: var(--bg-card);
    transition: border-color 0.15s;
  }}
  .effect-essence-card:hover {{ border-color: var(--border-accent); }}
  .effect-essence-card:last-child {{ margin-bottom: 0; }}
  mark.highlight {{
    background: #fef08a;
    color: #713f12;
    border-radius: 2px;
    padding: 0 1px;
  }}
</style>
</head>
<body>
<header>
  <div class="header-inner">
    <a class="back-btn" href="index.py">← クラス選択</a>
    <div class="header-title">
      <h1>👊 モンク 精髄チェッカー</h1>
      <p>スキルを選択して使用可能な精髄を検索</p>
    </div>
    <div class="header-spacer"></div>
  </div>
</header>

<div id="selected-panel">
  <h2>✨ 選択中の精髄</h2>
  <div id="selected-list"></div>
</div>

<main>
  <section class="skill-section">
    <h2 class="section-title amber">スキル選択</h2>
    <div class="skill-grid" id="skill-grid"></div>
  </section>

  <section class="bookmark-section">
    <h2 class="section-title gold">🔖 ブックマーク</h2>
    <div class="bookmark-actions">
      <input type="text" id="bookmark-name-input" placeholder="ブックマーク名を入力..." maxlength="30">
      <button id="save-bookmark-btn" onclick="saveBookmark()">💾 保存</button>
    </div>
    <div id="bookmark-list"></div>
  </section>

  <section class="effect-search-section">
    <h2 class="section-title amber">🔎 効果検索</h2>
    <div class="effect-search-actions">
      <input type="text" id="effect-search-input" placeholder="効果に含まれるキーワード（例：スタン、冷気、ノックバック）" maxlength="50">
      <button id="effect-search-btn" onclick="searchByEffect()">🔍 検索</button>
      <button id="effect-search-clear-btn" onclick="clearEffectSearch()">✕ クリア</button>
    </div>
    <div id="effect-search-results"></div>
  </section>

  <div class="search-wrap">
    <button id="search-btn" onclick="doSearch()">🔍 精髄を検索</button>
  </div>

  <div id="results">
    <p class="tooltip-hint">精髄をクリックして選択（頭・肩・胴・脚：各1つ、メインハンド・オフハンド：各2つまで）</p>
    <div class="slots-grid" id="slots-grid"></div>
  </div>
</main>

<script>
const ESSENCES = {essences_json};
const LIMITS = {limits_json};
const MAIN_ATTACKS = {main_attacks_json};
const SKILLS = {skills_json};
const SLOT_ICONS = {{"頭":"🪖","肩":"🦺","胴":"🛡️","脚":"👟","メインハンド":"👊","オフハンド":"🪬"}};
const SLOT_ORDER = ["頭","肩","胴","脚","メインハンド","オフハンド"];
const BM_KEY = 'monk_bookmarks';

let currentEssences = {{}};
SLOT_ORDER.forEach(s => currentEssences[s] = []);
const selected = {{}};
SLOT_ORDER.forEach(s => selected[s] = []);

function buildSkillGrid() {{
  const grid = document.getElementById('skill-grid');
  const slots = [
    {{id: 'main', label: 'メイン攻撃', options: MAIN_ATTACKS}},
    ...Array.from({{length:5}}, (_,i) => ({{id: `skill${{i+1}}`, label: `スキル${{i+1}}`, options: SKILLS}}))
  ];
  slots.forEach(s => {{
    const div = document.createElement('div');
    div.className = 'skill-slot';
    div.innerHTML = `<label for="${{s.id}}">${{s.label}}</label>
      <select id="${{s.id}}">
        <option value="">-- 未設定 --</option>
        ${{s.options.map(o => `<option value="${{o}}">${{o}}</option>`).join('')}}
      </select>`;
    grid.appendChild(div);
  }});
  grid.querySelectorAll('select').forEach(sel => sel.addEventListener('change', onSkillChange));
}}

function getSelectedSkills() {{
  const vals = [];
  const mainVal = document.getElementById('main').value;
  if (mainVal) vals.push(mainVal);
  for (let i = 1; i <= 5; i++) {{
    const v = document.getElementById(`skill${{i}}`).value;
    if (v) vals.push(v);
  }}
  return vals;
}}

function onSkillChange() {{
  const allSkillSelects = Array.from({{length:5}}, (_,i) => document.getElementById(`skill${{i+1}}`));
  const chosen = allSkillSelects.map(s => s.value).filter(Boolean);
  allSkillSelects.forEach(sel => {{
    const current = sel.value;
    Array.from(sel.options).forEach(opt => {{
      if (!opt.value) {{ opt.disabled = false; return; }}
      opt.disabled = chosen.includes(opt.value) && opt.value !== current;
    }});
    sel.classList.toggle('has-value', !!current);
  }});
  document.getElementById('main').classList.toggle('has-value', !!document.getElementById('main').value);
}}

function doSearch() {{
  const skills = getSelectedSkills();
  const slotsGrid = document.getElementById('slots-grid');
  slotsGrid.innerHTML = '';
  SLOT_ORDER.forEach(slot => {{
    currentEssences[slot] = ESSENCES[slot].filter(e => skills.includes(e.skill));
  }});
  SLOT_ORDER.forEach((slot, idx) => {{
    const essences = currentEssences[slot];
    const card = document.createElement('div');
    card.className = 'slot-card';
    card.dataset.slot = slot;
    card.style.animationDelay = `${{idx * 0.03}}s`;
    const limit = LIMITS[slot];
    const selCount = selected[slot].length;
    card.innerHTML = `
      <div class="slot-header">
        <div class="slot-title">${{SLOT_ICONS[slot]}} ${{slot}}</div>
        <div class="slot-limit${{selCount >= limit ? ' at-limit' : ''}}" id="limit-${{slot}}">選択: ${{selCount}}/${{limit}}</div>
      </div>
      <div class="slot-essences" id="essences-${{slot}}">
        ${{renderEssenceList(slot, essences)}}
      </div>`;
    slotsGrid.appendChild(card);
  }});
  document.getElementById('results').style.display = 'block';
  document.getElementById('results').scrollIntoView({{behavior:'smooth', block:'start'}});
  refreshSelectedPanel();
}}

function renderEssenceList(slot, essences) {{
  if (essences.length === 0) return '<div class="no-essences">該当する精髄なし</div>';
  return `<div class="essence-count">${{essences.length}}件</div>` +
    essences.map((e, idx) => renderEssence(slot, e, idx)).join('');
}}

function renderEssence(slot, e, idx) {{
  const isSelected = selected[slot].some(s => s.name === e.name);
  const atLimit = selected[slot].length >= LIMITS[slot];
  const isDisabled = !isSelected && atLimit;
  return `<div class="essence-card${{isSelected ? ' selected' : ''}}${{isDisabled ? ' disabled' : ''}}" data-slot="${{slot}}" data-index="${{idx}}">
    <div class="essence-name"><span class="check-icon">✓</span>${{e.name}}</div>
    <div class="essence-skill">スキル: <span>${{e.skill}}</span></div>
    <div class="essence-desc">${{e.desc}}</div>
  </div>`;
}}

document.getElementById('slots-grid').addEventListener('click', function(ev) {{
  const card = ev.target.closest('.essence-card');
  if (!card || card.classList.contains('disabled')) return;
  const slot = card.dataset.slot;
  const idx = parseInt(card.dataset.index);
  const essence = currentEssences[slot] && currentEssences[slot][idx];
  if (!essence) return;
  toggleEssence(slot, essence);
}});

function toggleEssence(slot, e) {{
  const idx = selected[slot].findIndex(s => s.name === e.name);
  if (idx >= 0) {{
    selected[slot].splice(idx, 1);
  }} else {{
    if (selected[slot].length >= LIMITS[slot]) return;
    selected[slot].push(e);
  }}
  const essences = currentEssences[slot];
  const container = document.getElementById(`essences-${{slot}}`);
  if (!container) return;
  const selCount = selected[slot].length;
  const limitEl = document.getElementById(`limit-${{slot}}`);
  if (limitEl) {{
    limitEl.textContent = `選択: ${{selCount}}/${{LIMITS[slot]}}`;
    limitEl.className = `slot-limit${{selCount >= LIMITS[slot] ? ' at-limit' : ''}}`;
  }}
  container.innerHTML = renderEssenceList(slot, essences);
  refreshSelectedPanel();
}}

function refreshSelectedPanel() {{
  const panel = document.getElementById('selected-panel');
  const list = document.getElementById('selected-list');
  const allSelected = SLOT_ORDER.flatMap(slot => selected[slot].map(e => ({{...e, slot}})));
  if (allSelected.length === 0) {{ panel.style.display = 'none'; return; }}
  panel.style.display = 'block';
  list.innerHTML = allSelected.map(e => `
    <div class="selected-tag" data-slot="${{e.slot}}" data-name="${{encodeURIComponent(e.name)}}">
      <span class="slot-badge">${{SLOT_ICONS[e.slot]}} ${{e.slot}}</span>
      <strong>${{e.name}}</strong>
      <span class="remove-btn">✕</span>
    </div>`).join('');
}}

document.getElementById('selected-list').addEventListener('click', function(ev) {{
  const tag = ev.target.closest('.selected-tag');
  if (!tag) return;
  const slot = tag.dataset.slot;
  const name = decodeURIComponent(tag.dataset.name);
  const essence = selected[slot].find(s => s.name === name);
  if (essence) toggleEssence(slot, essence);
}});

function saveBookmark() {{
  const nameInput = document.getElementById('bookmark-name-input');
  const name = nameInput.value.trim();
  if (!name) {{
    nameInput.focus();
    nameInput.style.borderColor = '#ef4444';
    setTimeout(() => nameInput.style.borderColor = '', 1800);
    return;
  }}
  const skills = {{ main: document.getElementById('main').value }};
  for (let i = 1; i <= 5; i++) skills[`skill${{i}}`] = document.getElementById(`skill${{i}}`).value;
  const bookmarks = JSON.parse(localStorage.getItem(BM_KEY) || '[]');
  bookmarks.push({{ name, skills, date: new Date().toLocaleDateString('ja-JP') }});
  localStorage.setItem(BM_KEY, JSON.stringify(bookmarks));
  nameInput.value = '';
  renderBookmarks();
}}

function loadBookmark(idx) {{
  const bookmarks = JSON.parse(localStorage.getItem(BM_KEY) || '[]');
  const bm = bookmarks[idx];
  if (!bm) return;
  document.getElementById('main').value = bm.skills.main || '';
  for (let i = 1; i <= 5; i++) document.getElementById(`skill${{i}}`).value = bm.skills[`skill${{i}}`] || '';
  onSkillChange();
  doSearch();
}}

function deleteBookmark(idx) {{
  const bookmarks = JSON.parse(localStorage.getItem(BM_KEY) || '[]');
  bookmarks.splice(idx, 1);
  localStorage.setItem(BM_KEY, JSON.stringify(bookmarks));
  renderBookmarks();
}}

function renderBookmarks() {{
  const list = document.getElementById('bookmark-list');
  const bookmarks = JSON.parse(localStorage.getItem(BM_KEY) || '[]');
  if (bookmarks.length === 0) {{
    list.innerHTML = '<span class="bookmark-empty">ブックマークはまだありません</span>';
    return;
  }}
  list.innerHTML = bookmarks.map((bm, idx) => `
    <div class="bookmark-tag" data-idx="${{idx}}">
      <span class="bm-name">${{bm.name}}</span>
      <span class="bm-date">${{bm.date}}</span>
      <span class="bm-delete" data-idx="${{idx}}">✕</span>
    </div>`).join('');
}}

document.getElementById('bookmark-list').addEventListener('click', function(ev) {{
  const del = ev.target.closest('.bm-delete');
  if (del) {{ ev.stopPropagation(); deleteBookmark(parseInt(del.dataset.idx)); return; }}
  const tag = ev.target.closest('.bookmark-tag');
  if (tag) loadBookmark(parseInt(tag.dataset.idx));
}});

// ===== 効果検索 =====
function searchByEffect() {{
  const keyword = document.getElementById('effect-search-input').value.trim();
  const container = document.getElementById('effect-search-results');
  if (!keyword) {{
    container.innerHTML = '<p class="effect-no-results">キーワードを入力してください。</p>';
    return;
  }}
  const kw = keyword.toLowerCase();
  let totalCount = 0;
  let html = '';
  SLOT_ORDER.forEach(slot => {{
    const matches = ESSENCES[slot].filter(e =>
      e.name.toLowerCase().includes(kw) ||
      e.desc.toLowerCase().includes(kw) ||
      e.skill.toLowerCase().includes(kw)
    );
    if (matches.length === 0) return;
    totalCount += matches.length;
    html += `<div class="effect-slot-group">
      <div class="effect-slot-label">${{SLOT_ICONS[slot]}} ${{slot}}&nbsp;(${{matches.length}}件)</div>
      ${{matches.map(e => `<div class="effect-essence-card">
        <div class="essence-name">${{hlKw(e.name, keyword)}}</div>
        <div class="essence-skill">スキル: <span>${{hlKw(e.skill, keyword)}}</span></div>
        <div class="essence-desc">${{hlKw(e.desc, keyword)}}</div>
      </div>`).join('')}}
    </div>`;
  }});
  if (totalCount === 0) {{
    container.innerHTML = `<p class="effect-no-results">「${{keyword}}」に一致する精髄は見つかりませんでした。</p>`;
    return;
  }}
  container.innerHTML =
    `<p class="effect-result-summary">「<strong>${{keyword}}</strong>」を含む精髄: <strong>${{totalCount}}件</strong></p>` + html;
  container.scrollIntoView({{behavior: 'smooth', block: 'nearest'}});
}}

function hlKw(text, kw) {{
  if (!kw || !text) return text || '';
  const lower = text.toLowerCase();
  const kwLower = kw.toLowerCase();
  let result = '';
  let lastIdx = 0;
  let idx;
  while ((idx = lower.indexOf(kwLower, lastIdx)) !== -1) {{
    result += text.slice(lastIdx, idx) + '<mark class="highlight">' + text.slice(idx, idx + kw.length) + '</mark>';
    lastIdx = idx + kw.length;
  }}
  return result + text.slice(lastIdx);
}}

function clearEffectSearch() {{
  document.getElementById('effect-search-input').value = '';
  document.getElementById('effect-search-results').innerHTML = '';
}}

document.getElementById('effect-search-input').addEventListener('keydown', function(ev) {{
  if (ev.key === 'Enter') searchByEffect();
}});

buildSkillGrid();
renderBookmarks();
</script>
</body>
</html>"""

print(HTML)
