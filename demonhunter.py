#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

print("Content-Type: text/html; charset=utf-8")
print()

MAIN_ATTACKS = ["エクスプローシブ・アロー", "クロスボウ・ショット"]

SKILLS = [
    "インペール", "ストレイフ", "スピニング・チャクラム", "セントリー",
    "ナイフの罠", "ノックバック・ショット", "マルチショット", "報復",
    "大振り", "影の視界", "復讐の雨", "煙幕", "脱出"
]

ESSENCES = {
    "頭": [
        {"skill": "マルチショット", "name": "厳罰の頭巾", "desc": "＜マルチショット＞のダメージが19%上昇。"},
        {"skill": "ノックバック・ショット", "name": "デイの恐るべき人格", "desc": "＜ノックバック・ショット＞のダメージが19%増加する。"},
        {"skill": "セントリー", "name": "凍てついた守護者の先見", "desc": "＜セントリー＞が氷結で強化され、敵にダメージと冷却効果を与える。"},
        {"skill": "セントリー", "name": "砲兵長の兜", "desc": "＜セントリー＞発動時、巨大な砲弾を発射し、敵にダメージを与えてノックバックするようになる。ただし、同時に展開できる＜セントリー＞の数が減少する。"},
        {"skill": "セントリー", "name": "自制されしイシルの破壊", "desc": "＜セントリー＞発動時、榴弾を放って爆発させ、範囲内の敵すべてにダメージを与えるようになる。"},
        {"skill": "報復", "name": "亡者の視覚", "desc": "＜報復＞発動中、敵を倒すごとに同スキルの持続時間が0.2秒延長する。この効果は最長で2.4秒まで蓄積する。"},
        {"skill": "マルチショット", "name": "怨恨の頭巾", "desc": "＜マルチショット＞が追加で4の矢を放つ。"},
        {"skill": "大振り", "name": "無限の創意", "desc": "＜大振り＞のチャージ上限が1増加する。"},
        {"skill": "報復", "name": "マーダーモースト", "desc": "＜報復＞発動時、クリティカル・ヒット率が12％増加するが、1秒毎にライフの3％が失われるようになる。"},
        {"skill": "報復", "name": "スキャッターの仮面", "desc": "＜報復＞の発動時、ただちに周囲のすべての敵に3,185ダメージを与え、3秒間恐怖で逃走させる効果が加わる。"},
        {"skill": "脱出", "name": "囮の手引き", "desc": "＜脱出＞のチャージ上限が1増加する。"},
        {"skill": "脱出", "name": "莫大なる無形", "desc": "＜脱出＞を発動してから2.4秒間、姿が見えない状態になる。"},
        {"skill": "大振り", "name": "ハウラのしゃくり上げ", "desc": "＜大振り＞により移動速度が4.8秒間30%上昇する。"},
        {"skill": "ノックバック・ショット", "name": "破れられし宣言", "desc": "＜ノックバック・ショット＞使用後、6.4秒間、メイン攻撃の速度が30%増加する。"},
        {"skill": "脱出", "name": "ヴァトロの決別", "desc": "＜脱出＞に、発動時に爆発する罠を残す効果が加わる。罠は少し遅れて付近の敵すべてに7,500ダメージを与える。"},
        {"skill": "脱出", "name": "最高の裁量", "desc": "ダメージを受ける度に＜脱出＞のクールダウン時間が1.6秒間短縮される。最大で4.8秒間短縮される。"},
        {"skill": "脱出", "name": "狩りの角", "desc": "＜脱出＞発動時、まきびしを地面に撒いて、範囲内の敵の移動速度を低下させて12,269ダメージを与え、ダッシュスキルの使用を妨げる。"},
        {"skill": "セントリー", "name": "門前の猪", "desc": "＜セントリー＞発動時、敵に狙われない影のタレットを標的の位置に召喚し、付近の敵を攻撃する。"},
        {"skill": "マルチショット", "name": "虚ろな凝視", "desc": "＜マルチショット＞のダメージが、敵がライフを1％失うごとに0.8%上昇する（最大48%）"},
        {"skill": "マルチショット", "name": "燃え立つ瞳", "desc": "＜マルチショット＞発動時、炎上中の敵に命中すると爆発を起こし、付近の敵に追加で14,766ダメージを与える。"},
        {"skill": "マルチショット", "name": "捕食者のくちばし", "desc": "＜マルチショット＞発動時、3秒間、与えるダメージが19％増加する。"},
        {"skill": "セントリー", "name": "不利な駆け引き", "desc": "＜セントリー＞発動時、プレイヤーを追従して付近の敵を自動攻撃する＜集束せし憎悪＞が出現する。"},
        {"skill": "報復", "name": "狩人の嗅覚", "desc": "＜報復＞の発動中、付近の流血状態の敵ごとにメイン攻撃速度が11.4%上昇する（最大34.2%）"},
        {"skill": "影の視界", "name": "隠匿のセレナーデ", "desc": "＜影の視界＞発動時、指定したエリアにいる敵に印を付与して移動不能状態にする。移動不能中はダッシュスキルが使用できず、印が付与されている間に何度か攻撃を受けると爆発して付近の敵にダメージを与える。"},
        {"skill": "脱出", "name": "罪深き虚構", "desc": "メイン攻撃で敵を攻撃するたびに＜脱出＞のクールダウンが0.16秒短縮される。"},
        {"skill": "報復", "name": "顔盗み", "desc": "＜報復＞発動中に毒状態の敵を攻撃すると、猛毒が爆発して9,088ダメージを与える。この効果は敵毎に１秒に１回しか発動しない。"},
        {"skill": "セントリー", "name": "盲目の見張り", "desc": "＜セントリー＞発動時、ロープタレットを召喚する。タレットは周囲の敵を攻撃し、ロープを取り付けて引き寄せる。影響を受けた敵はタレットの射程外に出るとスタンする。"},
        {"skill": "ノックバック・ショット", "name": "熾烈なる代償", "desc": "＜ノックバック・ショット＞で敵をノックバックした時、与えるダメージが3秒間9.5％増加する（最大28.5%）"},
        {"skill": "大振り", "name": "いじけさせておけ", "desc": "＜大振り＞のクールダウン時間が、命中した敵1体につき0.3秒短縮される。最大0.9秒。"},
        {"skill": "報復", "name": "君主の血", "desc": "敵が遠くに居るほど＜報復＞のダメージが増加する（最大16%のダメージ増加）"},
        {"skill": "セントリー", "name": "導星のヴェール", "desc": "＜セントリー＞はプレイヤーが近づくと起動し、メイン攻撃を模倣して敵にダメージを与えるタブレットを2つ召喚する。"},
        {"skill": "セントリー", "name": "無慈悲なる狩り", "desc": "＜セントリー＞で付近の敵を自動的に射撃するタレットを呼び出す。タレットの近くでスキルを使う度、爆発する投射体を放つ。"}
    ],
    "肩": [
        {"skill": "マルチショット", "name": "ヘイルファイア", "desc": "＜マルチショット＞発動時、2発の誘導ロケット弾を発射し、各ロケット弾が4,018のダメージを与える。"},
        {"skill": "復讐の雨", "name": "ヴァアシュのタイフォニック・スタンピード", "desc": "＜復讐の雨＞発動時、前方に突進するシャドウ・ビーストの群れを召喚する。"},
        {"skill": "復讐の雨", "name": "スカイストライカーの肩甲", "desc": "＜復讐の雨＞の代わりに、空を飛ぶシャドウ・ビーストを召喚し、範囲内の敵すべてにダメージを与える爆弾を連続で投下させる。"},
        {"skill": "ナイフの罠", "name": "ブレードウィング", "desc": "＜ナイフ罠＞の最大起動可能数が1増加し、チャージ上限が1増加する。"},
        {"skill": "復讐の雨", "name": "雹の肩当て", "desc": "＜復讐の雨＞が冷気によって強化され、40％の冷気効果を与えるとともに、4秒間で80,228のダメージを与える。（リキャ13秒）"},
        {"skill": "復讐の雨", "name": "爆撃の犠牲", "desc": "＜復讐の雨＞発動時、空を飛び爆弾を投下するシャドウ・ビーストを召喚し、敵にダメージを与えてスタンさせるようになる。"},
        {"skill": "スピニング・チャクラム", "name": "闇を歩きし者のスパルダー", "desc": "＜スピニング・チャクラム＞のチャージ上限が1増加。"},
        {"skill": "大振り", "name": "チルラスの肩鎧", "desc": "＜大振り＞発動時、地面に氷の矢を放ち、連続ダメージと冷気効果を与える氷の軌跡を作り出すようになる。"},
        {"skill": "脱出", "name": "ハンター・ギャザラー", "desc": "＜脱出＞発動時、付近の敵に対して3発の誘導ロケット弾を発射し、各ロケット弾がダメージ4,121を与える。"},
        {"skill": "マルチショット", "name": "決然たる廻報", "desc": "＜マルチショット＞が敵をノックバックさせるようになる。この効果はプレイヤーに対して6秒に1回しか発動しない。"},
        {"skill": "脱出", "name": "生き餌", "desc": "＜脱出＞発動時、前方宙返りするようになる。短時間の間に再度発動すると元の位置に戻れる。"},
        {"skill": "マルチショット", "name": "百撃の影", "desc": "＜マルチショット＞が障壁に対して350%のダメージを与えるようになる。"},
        {"skill": "ナイフの罠", "name": "シュレッドバンク", "desc": "操作障害効果を受けている敵への＜ナイフの罠＞ダメージが38%増加する。"},
        {"skill": "復讐の雨", "name": "性急なる処刑", "desc": "＜復讐の雨＞を発動すると燃える矢を放ち、4秒間にわたって標的エリア内のすべての敵を炎上させ、77,336ダメージを与えるようになる。（リキャ11秒）"},
        {"skill": "大振り", "name": "絞首刑執行人の策略", "desc": "＜大振り＞が命中した敵を移動不能状態にするようになる。"},
        {"skill": "ナイフの罠", "name": "密かな衝突", "desc": "＜ナイフの罠＞の爆発が敵のアーマーを破壊するようになり、ダメージが3秒間19％増加する。"},
        {"skill": "ナイフの罠", "name": "森の叫び", "desc": "＜ナイフの罠＞のクールダウン時間が18.6%短縮される。"},
        {"skill": "ナイフの罠", "name": "砕けたガラスのワルツ", "desc": "＜ナイフの罠＞をセントリーの近くで発動すると、そのセントリーの攻撃速度が4.8秒間30％上昇する。"},
        {"skill": "脱出", "name": "高まる暴力", "desc": "＜脱出＞発動時、前方に突進して進路上の敵にダメージを与えて移動速度を低下させる。"},
        {"skill": "大振り", "name": "コインの達人", "desc": "＜大振り＞発動時、火矢を放って進路を燃え上がらせ、敵を炎上させる。"},
        {"skill": "大振り", "name": "巨人の罠", "desc": "＜大振り＞発動時、メイン攻撃が強化され、複数の敵の間で跳ね返る拘束用のロープを放つ。拘束された敵は移動不能になる。"},
        {"skill": "ナイフの罠", "name": "自警団のスパルダー", "desc": "＜ナイフの罠＞発動時、3秒間印を付与する。印付きの敵に対する＜セントリー＞のダメージが57％増加する。"},
        {"skill": "スピニング・チャクラム", "name": "破滅の羅針盤", "desc": "＜スピニング・チャクラム＞は流血状態の敵に命中すると爆発し、18,643の追加ダメージを与える。"},
        {"skill": "復讐の雨", "name": "不協和の魅力", "desc": "＜復讐の雨＞発動時、指定した場所に矢の雨を降らせる。矢は急速に降り注いで複数の敵にダメージを与える。"},
        {"skill": "脱出", "name": "苦難の亡霊", "desc": "＜脱出＞発動時、短距離をローリング移動する。プレイヤーが強化され、メイン攻撃時に同時に２回撃つ。"},
        {"skill": "復讐の雨", "name": "満たされぬ欲望", "desc": "＜復讐の雨＞発動時、狙った範囲に毒矢が3秒間降り注ぎ、範囲内の敵を毒状態にして毎秒18,000ダメージを与える（最大42,336ダメージ）"},
        {"skill": "ナイフの罠", "name": "深手の残響", "desc": "＜ナイフの罠＞が2秒以内に同じ敵に命中すると、ダメージが15.2%上昇する（最大45.6%）"},
        {"skill": "脱出", "name": "厄災の脱出", "desc": "＜脱出＞発動時、標的の位置に突進し、進路上の敵にダメージを与えてスタンさせる。命中した敵はアーマーが破壊され、プレイヤーから受けるダメージが増加する。"},
        {"skill": "大振り", "name": "機敏な競争者", "desc": "＜大振り＞発動時、一方的にフックを投げて地面に突き刺したあと、フックに向かって自身を引き寄せながら、進路上に居る敵にダメージを与える。引き寄せられている間、ノックバックと操作障害効果が無効化される。"},
        {"skill": "マルチショット", "name": "自我の重荷", "desc": "＜マルチショット＞のダメージが敵との距離1ヤードごとに3％ずつ増加する（最大24%）"},
        {"skill": "マルチショット", "name": "折れ枝", "desc": "＜マルチショット＞が3秒以内に敵に3回命中すると、さらに30,009ダメージを与える。同じ敵に対しては0.2秒に1回しか追加ダメージを与えられない。"},
        {"skill": "復讐の雨", "name": "気まぐれな奇襲", "desc": "＜復讐の雨＞発動時、標的の位置に断続的に矢の雨を降らせて敵をスタンさせる。ほかのスキルで敵にダメージを与えると自動発動し、その敵を中心に矢の雨が降り注ぐ。"}
    ],
    "胴": [
        {"skill": "ノックバック・ショット", "name": "放埒なる憎悪", "desc": "＜ノックバック・ショット＞発動時、榴弾を発射し、範囲内の敵を爆撃するようになる。"},
        {"skill": "復讐の雨", "name": "闇の翼の胸当て", "desc": "＜復讐の雨＞の持続時間が30%増加する。"},
        {"skill": "ストレイフ", "name": "デスウォッチの胸当て", "desc": "＜ストレイフ＞のダメージが10%上昇。"},
        {"skill": "ナイフの罠", "name": "ヘルトラッパーの檻", "desc": "＜ナイフの罠＞のダメージが10%増加。"},
        {"skill": "ナイフの罠", "name": "殺意のプレート", "desc": "メイン攻撃で敵を攻撃すると、＜ナイフの罠＞のクールダウン時間が0.3秒短縮される。"},
        {"skill": "煙幕", "name": "闇の抱擁", "desc": "煙幕の煙がより濃く、長期持続するようになり、中にいる間姿を隠し続けることができる。ただし、攻撃の間だけは姿が見える。"},
        {"skill": "ノックバック・ショット", "name": "ペタームの秘密兵器", "desc": "凍てついた風：＜ノックバック・ショット＞が氷結で強化され、敵にダメージを与えて凍結させる氷の軌跡を残す。"},
        {"skill": "報復", "name": "復讐心", "desc": "＜報復＞のクールダウン時間が15%短縮。"},
        {"skill": "煙幕", "name": "辛辣なる衣服", "desc": "＜煙幕＞発動時、敵に連続的にダメージを与える酸性爆弾を投げつけるようになる。"},
        {"skill": "煙幕", "name": "広がる帳", "desc": "＜煙幕＞が目標位置に煙玉を投下するようになり、そのエリアに残る敵に継続ダメージを与え、視界を大幅に狭める。"},
        {"skill": "復讐の雨", "name": "辛辣", "desc": "＜復讐の雨＞が敵のアーマーを腐食させ、3秒間、与えるダメージが2%増加するようになる。この効果は5回まで蓄積する。"},
        {"skill": "ストレイフ", "name": "ラデラの組み紐", "desc": "＜ストレイフ＞で敵1体にダメージを与える毎に、その敵に与えるダメージが3%増加する。増加量は最大30%で、最大1秒間持続する。"},
        {"skill": "ノックバック・ショット", "name": "反響のダブレット", "desc": "＜ノックバック・ショット＞が敵を移動不能状態にする矢を放つ。"},
        {"skill": "ノックバック・ショット", "name": "ペテン師の予言", "desc": "＜ノックバック・ショット＞を発動すると、メイン攻撃とともに敵を打ちのめす突風を発射するようになる。"},
        {"skill": "報復", "name": "憎悪の鞘", "desc": "＜報復＞を使うと怒りで完全に我を忘れるようになり、メイン攻撃の速度が大幅に上昇するが、標的にする敵を選べなくなる。"},
        {"skill": "ノックバック・ショット", "name": "正反対の秩序", "desc": "＜ノックバック・ショット＞が敵を炎上させる火炎放射器を呼び出すようになる。"},
        {"skill": "ノックバック・ショット", "name": "憎悪の支点", "desc": "＜ノックバック・ショット＞がチャージできるようになり、凝縮された憎悪の爆風を発射し、進路上の敵にダメージを与える。チャージ時間が長いほど攻撃の範囲とダメージが増加する。チャージは最大3回まで。"},
        {"skill": "報復", "name": "新馬の炉", "desc": "＜報復＞発動時、ターゲットを継続的に攻撃する内なるデーモンを召喚するが、移動速度は上昇しない。"},
        {"skill": "ストレイフ", "name": "規律の散在", "desc": "＜ストレイフ＞のクリティカルヒット率がライフ50％未満の敵に対して38％上昇する。"},
        {"skill": "煙幕", "name": "不活性の炎", "desc": "＜煙幕＞発動時、指定した場所にファイアボムを投げ、敵の速度を低下させて炎上させる。"},
        {"skill": "ストレイフ", "name": "罪深き活力", "desc": "メイン攻撃時に＜ストレイフ＞のエネルギーが1.5％回復する。"},
        {"skill": "報復", "name": "溺没の抱擁", "desc": "＜報復＞発動中、＜セントリー＞と＜ナイフの罠＞発動時に2本の貫通光線を放ち、5,260ダメージを与える。"},
        {"skill": "報復", "name": "皮剥ぎの晩餐", "desc": "＜報復＞の発動中メイン攻撃全てが流血を与え、敵のアーマーを破壊する。また、継続ダメージを与え、敵が受けるダメージが増えるが、これらの2つのダメージは累積する。"},
        {"skill": "復讐の雨", "name": "雷の斉唱", "desc": "＜復讐の雨＞が同じ敵に命中すると、2秒間にわたりダメージが10％ずつ徐々に増加していく（最大30％）"},
        {"skill": "報復", "name": "残忍なる節制", "desc": "＜報復＞発動時、メイン攻撃が一時的に貫通弾を放つ。"},
        {"skill": "報復", "name": "尽きぬ恨み", "desc": "＜報復＞発動時、猛毒が爆発して付近の敵すべてに11,382ダメージを与え、3秒間毒状態にし、毎秒8,762ダメージを与える。さらに、付近の毒状態の敵に向かって1秒毎に最大4発の貫通矢を放ち、53,272ダメージを与える。"},
        {"skill": "煙幕", "name": "扇動の息吹", "desc": "＜煙幕＞発動時、標的の位置にグレネードを投げて粉塵を発生させ、炎上状態の敵を爆発させる。"},
        {"skill": "ノックバック・ショット", "name": "汚れなき皮革", "desc": "＜ノックバック・ショット＞発動時、標的の方向に複数の貫通する衝撃波を放ち、敵にダメージを与えてノックバックする。"},
        {"skill": "煙幕", "name": "煙霧の糸", "desc": "＜煙幕＞発動時、プレイヤーが強化され、移動しながら付近の敵にグレネードを投げられるようになる。同じ敵に短期間で別のグレネードをヒットさせると、ダメージが増加する。ダッシュスキルを使用すると、グレネードを投げるのに必要な移動距離が短縮される。"},
        {"skill": "報復", "name": "純粋なる怒り", "desc": "＜報復＞発動時、＜ピアシング・ショット＞を放ち、効果が切れるまで自身の体をその場に固定する。再び発動させることで新たに＜ピアシング・ショット＞を放ち、ダメージを与えると同時に敵をノックバックさせ、スロウ状態にすうことができる。"},
        {"skill": "ノックバック・ショット", "name": "道拓きの者", "desc": "＜ノックバック・ショット＞が広がりながらゆっくり移動する投射物を放つ。投射物は継続的に敵をノックバックしダメージを与える。"},
        {"skill": "報復", "name": "ナイフのクローク", "desc": "＜報復＞で復讐の化身に変身する。操作障害とノックバック効果が無効かされ、スキルダメージが増加して新たにアクティブ・スキルを獲得する。"}
    ],
    "脚": [
        {"skill": "ナイフの罠", "name": "逃れ得ぬ捕食者", "desc": "＜ナイフの罠＞が＜氷結の罠＞になり、爆発すると敵にダメージと冷却効果を与える。"},
        {"skill": "煙幕", "name": "高位錬金術師の脚当て", "desc": "＜煙幕＞の代わりに自身の位置にガス爆弾を設置し、付近の敵すべてに連続ダメージを与える。"},
        {"skill": "煙幕", "name": "暗殺者の遺産", "desc": "＜煙幕＞の代わりに指定地点にグレネードを放って爆発させる。最大チャージが3に増加する。"},
        {"skill": "ナイフの罠", "name": "定めの業火の脚当て", "desc": "＜ナイフの罠＞が＜生け贄の罠＞になり、爆発時に地面と付近の敵すべてを炎上させる。"},
        {"skill": "報復", "name": "破滅の道", "desc": "＜報復＞の発動中に与えるすべてのダメージが11.4%増加する。"},
        {"skill": "煙幕", "name": "ジェインの静かなる報い", "desc": "＜煙幕＞が消えた後の1秒間、クリティカルヒット率が50%上昇する。"},
        {"skill": "スピニング・チャクラム", "name": "スレイヤーの下衣", "desc": "＜スピニング・チャクラム＞を短時間に連続で敵に当てると、4%の追加ダメージを与える。最大5回まで蓄積する。"},
        {"skill": "報復", "name": "コフの無慈悲なる憤怒", "desc": "＜報復＞発動中、メイン攻撃2回につき1発のロケット弾を追加で発射し、各ロケット弾が付近の敵に5,030のダメージを与える。"},
        {"skill": "ナイフの罠", "name": "スクラップダックス", "desc": "＜ナイフ罠＞が、踏むと爆発する複数の地雷をまき散らすようになるが、チャージは1回限りとなる。"},
        {"skill": "ナイフの罠", "name": "掴む爪", "desc": "＜ナイフの罠＞発動時に周囲の敵を拘束し、自身が与える全ダメージが増加するようになる。"},
        {"skill": "脱出", "name": "秘密の安全策", "desc": "＜脱出＞に7,510のダメージを吸収するシールド効果が加わる。シールドは5秒間持続する。"},
        {"skill": "煙幕", "name": "濃厚なる冷気", "desc": "＜煙幕＞発動時、指定地点に氷の爆弾を投げ、付近のすべての敵に冷気効果とダメージを与えるようになる。＜煙幕＞の最大チャージが2に増加する。"},
        {"skill": "ナイフの罠", "name": "ポットボイラー", "desc": "＜ナイフの罠＞が、ダメージを与えた際に発動する、より頑丈な罠を設置するようになる。"},
        {"skill": "ナイフの罠", "name": "定められし結末", "desc": "＜ナイフの罠＞が発動すると敵を引き寄せ、数秒後に爆発するようになる。"},
        {"skill": "大振り", "name": "嘲笑の嘴", "desc": "＜大振り＞にメイン攻撃の速度を6.4秒間、30%上昇させる効果が加わる。"},
        {"skill": "ナイフの罠", "name": "フェイント・キフ", "desc": "＜ナイフの罠＞がフックつきの鎖で満たされた罠を設置するようになる。起動すると鎖が周囲に放たれ、付近のすべての敵にダメージを与えて引き寄せ、移動障害効果を与える。"},
        {"skill": "ナイフの罠", "name": "揺るがぬ舞", "desc": "＜ナイフの罠＞が＜スネア・トラップ＞に変化する。起動すると付近の敵すべてにダメージを与えて移動不能状態にし、ダッシュスキルの使用を4秒間妨げる。"},
        {"skill": "報復", "name": "豊かな旅", "desc": "＜報復＞発動時、6秒間持続するフィールドが発生する。プレイヤーと味方の召喚した存在は0.5秒ごとに追加のボルトを1発発射し、3,071ダメージを与える。"},
        {"skill": "脱出", "name": "さえずりのグリーヴ", "desc": "＜脱出＞発動時、クリティカルヒット率が3秒間19％上昇する。"},
        {"skill": "スピニング・チャクラム", "name": "収束の月", "desc": "メイン攻撃が敵に命中するたびに＜スピニング・チャクラム＞のクールダウン時間が0.24秒短縮される。"},
        {"skill": "大振り", "name": "踏みにじられた希望", "desc": "＜大振り＞により攻撃速度が4秒間19％上昇する。"},
        {"skill": "ナイフの罠", "name": "船乗りの記章", "desc": "＜ナイフの罠＞発動時、プレイヤーを追従しながら付近の敵に刃を放つ＜集束せし戒め＞が出現する。"},
        {"skill": "スピニング・チャクラム", "name": "源泉の追跡者", "desc": "＜スピニング・チャクラム＞発動時、メイン攻撃速度が4.8秒間30%上昇する。"},
        {"skill": "影の視界", "name": "鳴り響く蹄鉄", "desc": "＜影の視界＞発動時、クリティカルヒット率も1.5秒間28.5％上昇する。"},
        {"skill": "報復", "name": "犠牲者の怨恨", "desc": "＜報復＞発動時、クリティカルヒット率が2秒間15.2％上昇する。"},
        {"skill": "煙幕", "name": "忍び寄る破滅", "desc": "＜煙幕＞発動時、武器に5秒間毒が込められ、メイン攻撃時に2秒間敵を毒状態にし、毎秒5,302ダメージを与える。毒を込めたメイン攻撃でクリティカルヒットが発生すると猛毒が爆発して42,572ダメージを与える。"},
        {"skill": "ナイフの罠", "name": "火ふき", "desc": "＜ナイフの罠＞発動時、移動式の罠を召喚する。移動式の罠は付近の敵を自動的に攻撃して炎上させる。"},
        {"skill": "脱出", "name": "曲芸のチャップス", "desc": "完全な制御不能状態やノックバック効果を受けているときにも脱出を使用できるようになる。これにより、0.5秒間、それらの効果を無効化できます。"},
        {"skill": "スピニング・チャクラム", "name": "メニーマーク", "desc": "＜スピニング・チャクラム＞がさらに、命中した敵にチャクラムの印を3秒間付与する。印を付与された敵が3回攻撃を受けると、20,148の追加ダメージを受ける（この効果は同じ敵に対して0.5秒に1回した発動しない）"},
        {"skill": "報復", "name": "捨てられた枷", "desc": "＜報復＞がダメージを与えると自身から5ヤード以上離れている敵は30,262の追加ダメージを受ける。この効果は同じ敵に対して0.7秒ごとに1回しか発生しない。"},
        {"skill": "大振り", "name": "糸渡りの徘徊者", "desc": "＜大振り＞のクールダウン時間が15％短縮される。"},
        {"skill": "報復", "name": "長引く憤怒", "desc": "スキルのクリティカルヒットが発生すると、＜報復＞の持続時間が0.2秒延長される。最大1.6秒。"}
    ],
    "メインハンド": [
        {"skill": "ストレイフ", "name": "騒乱", "desc": "＜ストレイフ＞発動時、誘導ロケットを発射し、各ロケットが付近の敵に5,044のダメージを与える。"},
        {"skill": "マルチショット", "name": "フレイムスパイト", "desc": "＜マルチショット＞発動時、炎の矢を放ち、敵にダメージを与え炎上させるようになる。"},
        {"skill": "復讐の雨", "name": "恐怖の地の報復", "desc": "＜復讐の雨＞のダメージが19%増加。"},
        {"skill": "マルチショット", "name": "冬の息吹", "desc": "＜マルチショット＞発動時、氷の矢を発射し、敵にダメージと冷却効果を与えるようになる。"},
        {"skill": "セントリー", "name": "監視者の救済", "desc": "＜セントリー＞の最大起動可能数が1増加し、チャージ上限が1増加する。"},
        {"skill": "煙幕", "name": "エンバーミスト", "desc": "＜煙幕＞のクールダウン時間が18.6%短縮。"},
        {"skill": "ストレイフ", "name": "無慈悲なる激憤", "desc": "＜ストレイフ＞の持続時間が39%増加。"},
        {"skill": "セントリー", "name": "ヴィジランス", "desc": "＜セントリー＞がロケット弾を発射し、攻撃2回ごとに3,335の追加ダメージを与える。"},
        {"skill": "マルチショット", "name": "ピンポイント・オーバーフロー", "desc": "＜マルチショット＞が標的の方向に対してすべての矢を発射するようになり、同じ敵に何度も当たる可能性がある。"},
        {"skill": "エクスプローシブ・アロー", "name": "寛大なる戦", "desc": "＜エクスプローシブ・ショット＞が4発毎に敵をノックバックさせる爆発矢を発生させる。プレイヤーに対しては3秒に1回しか影響しない。"},
        {"skill": "ストレイフ", "name": "ホブリングデッキ", "desc": "＜ストレイフ＞発動中、まきびしを地面に撒いて敵に2,336のダメージを与え、移動速度を30%低下させる。"},
        {"skill": "ストレイフ", "name": "空飛ぶハゲタカ", "desc": "＜ストレイフ＞発動中、移動速度が30%増加する。"},
        {"skill": "インペール", "name": "レイザーフライト", "desc": "＜インペール＞をチャージできるようになり、一度に複数のナイフを投擲できるようになる。"},
        {"skill": "マルチショット", "name": "執拗なる非難", "desc": "＜マルチショット＞を発動すると憎悪の矢と規律の矢どちらかをランダムに放ち、それぞれが命中したすべての敵を脆弱状態か移動速度低下状態にする。両方の効果を受けた敵に追加ダメージを与え、さらにスタンさせる。"},
        {"skill": "インペール", "name": "エクスカヴェイター", "desc": "＜インペール＞発動時、メイン攻撃がナイフも放つようになる。ナイフは敵を貫通して複数の相手にダメージを与える。"},
        {"skill": "インペール", "name": "二番目の欠点", "desc": "＜インペール＞がナイフを投げるようになる。ナイフは複数回敵の間を跳ね回り、地面に落ちる。落ちたナイフを拾うと＜インペール＞のクールダウン時間が減少する。"},
        {"skill": "セントリー", "name": "優雅な報復", "desc": "＜セントリー＞を他の＜セントリー＞の近くに設置すると最大3回までアップデート可能となり、与ダメージが最大380%増加し、被ダメージが最大82.5%減少する。"},
        {"skill": "煙幕", "name": "漆黒の雨", "desc": "＜煙幕＞発動時、霧が発生してプレイヤーの姿を隠し、現在の操作障害効果が即座に解除され、ノックバック効果を受けなくなる。"},
        {"skill": "インペール", "name": "憤怒の断片", "desc": "＜インペール＞が弧を描くように複数のナイフを放つようになる。"},
        {"skill": "クロスボウ・ショット", "name": "死の補完", "desc": "＜クロスボウ・ショット＞発動時、28.5％の確率で追加攻撃を行う。"},
        {"skill": "マルチショット", "name": "ファングスピッター", "desc": "＜マルチショット＞発動時、メイン攻撃が短時間強化され、＜マルチショット＞を放つ。"},
        {"skill": "インペール", "name": "ヴェイルピアサー", "desc": "＜インペール＞が1方向に複数の刃を放ち、命中した敵にダメージを与える。"},
        {"skill": "セントリー", "name": "針毛の呪詛", "desc": "＜セントリー＞の6ヤード以内の別の＜セントリー＞ごとに、ダメージが13.3％増加する（最大39.9％）"},
        {"skill": "クロスボウ・ショット", "name": "ピッチドリンカー", "desc": "＜クロスボウ・ショット＞は流血状態の敵に命中すると2つの投射物に分裂し、以降の敵に27,620ダメージを与える。"},
        {"skill": "インペール", "name": "沈黙の糸", "desc": "＜インペール＞が付近のランダムな敵を追尾する複数のナイフを放つ。"},
        {"skill": "マルチショット", "name": "ねじれた運命", "desc": "＜マルチショット＞発動時、メイン攻撃が一時的に爆発弾を放つ。"},
        {"skill": "煙幕", "name": "頭蓋の絶叫", "desc": "＜煙幕＞によりメイン攻撃速度が3秒間38％上昇する。"},
        {"skill": "煙幕", "name": "陰鬱な使者", "desc": "＜煙幕＞の最大チャージ数が1増加する。"},
        {"skill": "インペール", "name": "苦難の伝染", "desc": "＜インペール＞発動時、周囲にナイフを放ち、付近の敵の体にナイフを埋め込む。敵をノックバックすると埋め込まれたナイフが引きぬかれ、ランダムの方向に飛ぶ。"},
        {"skill": "煙幕", "name": "惑わす円弧", "desc": "＜煙幕＞がさらに、攻撃速度を3秒間10％上昇させる。"},
        {"skill": "マルチショット", "name": "天使などいない", "desc": "＜マルチショット＞が自身を強化し、スキルを使う度に追加で矢を一斉に放ち敵にダメージを与える。"},
        {"skill": "マルチショット", "name": "秘教の悪業者", "desc": "＜マルチショット＞発動時プレイヤーが強化され、メイン攻撃がランダムな敵に大量の追尾型の投射物を放つ。"},
        {"skill": "復讐の雨", "name": "クイックソーン", "desc": "＜復讐の雨＞により移動速度が2秒間40％上昇する。"}
    ],
    "オフハンド": [
        {"skill": "ストレイフ", "name": "ディスアレイ", "desc": "＜ストレイフ＞の代わりにグレネードを放って爆発させ、1発につき付近の敵すべてにダメージを与える。"},
        {"skill": "セントリー", "name": "チェインボルター", "desc": "＜ブラッディ・チェイン＞がセントリータレットと連動するようになる。チェイン1回につき、セントリーに30%のダメージ軽減効果が与えられる。軽減効果は最大60%。"},
        {"skill": "クロスボウ・ショット", "name": "飢えたる者", "desc": "＜クロスボウ・ショット＞発動時、矢が敵を貫き、背後にいる複数の敵にも攻撃する。"},
        {"skill": "ストレイフ", "name": "黒爪", "desc": "＜ストレイフ＞発動時、貫通力のある矢を連続で一方向に放つようになる。"},
        {"skill": "セントリー", "name": "夜襲の瞳", "desc": "＜セントリー＞のダメージが19%増加。"},
        {"skill": "エクスプローシブ・アロー", "name": "ヘルバインダー", "desc": "＜エクスプローシブ・アロー＞発動時、敵を2秒間炎上させ、5,560のダメージを与えるようになる。"},
        {"skill": "スピニング・チャクラム", "name": "ブレード・スロワー", "desc": "＜スピニング・チャクラム＞発動時、放ったチャクラムがその場にとどまり、付近の敵すべてに連続ダメージを与える。"},
        {"skill": "スピニング・チャクラム", "name": "シュレッダー・ヴェイン", "desc": "＜スピニング・チャクラム＞が発動すると数秒間自分の周囲を旋回する。"},
        {"skill": "インペール", "name": "プンクタ・オブスクラ", "desc": "＜インペール＞発動時、敵を3秒間出血させ、ダメージ6,180を与えるようになる。"},
        {"skill": "インペール", "name": "衝撃", "desc": "＜インペール＞のダメージが、有害な効果が発生している敵に対して28.5%増加する。"},
        {"skill": "セントリー", "name": "独力斉射", "desc": "＜セントリー＞の攻撃が敵に刻印を与え、4.8秒間、その標的に対して与えるダメージが8%増加する。"},
        {"skill": "ストレイフ", "name": "スジカー", "desc": "＜ストレイフ＞が付近の敵に貫通攻撃を放つようになる。"},
        {"skill": "ノックバック・ショット", "name": "手練れの術", "desc": "＜ノックバック・ショット＞使用後、4.8秒間、与えるダメージが10%増加する。"},
        {"skill": "クロスボウ・ショット", "name": "報復の学理", "desc": "＜クロスボウ・ショット＞が同じ敵に3回ダメージを与えるたびに11,172の追加ダメージを与えるようになる。"},
        {"skill": "セントリー", "name": "鋼の楽団", "desc": "セントリーの近くにいるとメイン攻撃の速度が19%上昇するようになる。"},
        {"skill": "ノックバック・ショット", "name": "グリスルグリン", "desc": "＜ノックバック・ショット＞が操作障害状態の敵に与えるダメージが38%増加する。"},
        {"skill": "セントリー", "name": "未亡人の歯牙", "desc": "＜セントリー＞が現在のライフの5%を消費し、＜セントリー＞の最大ライフの30%分のシールドを適用する。シールドが有効の間、＜セントリー＞のダメージが19%増加する。"},
        {"skill": "ストレイフ", "name": "休閑地", "desc": "＜ストレイフ＞発動時、回転する影を5秒間召喚して全方向を攻撃し、命中するたびに5,667ダメージを与える。チャージは最大2回まで。"},
        {"skill": "インペール", "name": "クィル・ラットのジレンマ", "desc": "敵がプレイヤーに近いほど、＜インペール＞のダメージが増加する（最大57％）"},
        {"skill": "スピニング・チャクラム", "name": "琥珀の月", "desc": "＜スピニング・チャクラム＞発動時、風車状の刃を放つ。刃は進路上の敵を引き寄せた後、その場で回転して爆発する。"},
        {"skill": "ストレイフ", "name": "ペインソウアー", "desc": "＜ストレイフ＞発動時、最も近い敵に向かってメイン攻撃で集中砲火を浴びせる。"},
        {"skill": "クロスボウ・ショット", "name": "悪意ある救済", "desc": "メイン攻撃が敵に命中すると＜セントリー＞のクールダウン時間が0.3秒短縮される。"},
        {"skill": "スピニング・チャクラム", "name": "獅子の顎", "desc": "＜スピニング・チャクラム＞は代わりにプレイヤーを数秒間強化し、その間メイン攻撃は敵の間を跳ね返ってダメージを与えるチャクラムを放つ。"},
        {"skill": "インペール", "name": "痛点", "desc": "＜インペール＞でライフが50％未満の敵に与えるダメージが38％増加する。"},
        {"skill": "クロスボウ・ショット", "name": "生存者の一撃", "desc": "スキルを使用してから3秒間、＜クロスボウ・ショット＞の次の4発のダメージが57％増加する。"},
        {"skill": "クロスボウ・ショット", "name": "優しい拒絶", "desc": "毒状態の敵に対する＜クロスボウ・ショット＞のダメージが28.5％増加する。"},
        {"skill": "セントリー", "name": "定めのスコーピオン", "desc": "＜セントリー＞が破壊されると小さな爆発が起こり、26,800ダメージを与えて敵を2秒間スタンさせる。"},
        {"skill": "インペール", "name": "滴る傷口", "desc": "＜インペール＞が同じ敵に命中するたび、ダメージが15.2%ずつ増加していく（最大45.6%）"},
        {"skill": "スピニング・チャクラム", "name": "無尽の補給", "desc": "＜スピニング・チャクラム＞発動時、プレイヤーが強化され、移動しながら付近の敵にチャクラムを投げられるようになる。チャクラムが行きだけでなく帰りに敵に当たると追加のダメージを与える。ダッシュスキルを使用すると、チャクラムを投げるのに必要な移動距離が短縮される。"},
        {"skill": "ノックバック・ショット", "name": "連続砲撃", "desc": "＜ノックバック・ショット＞のダメージが敵との距離1ヤードごとに3％ずつ増加する（最大24％）"},
        {"skill": "セントリー", "name": "干渉せし恩人", "desc": "＜セントリー＞のタレットは3秒間、メイン攻撃でダメージを与えた敵に対するダメージが15％増加する。"},
        {"skill": "セントリー", "name": "悪意の考案", "desc": "＜セントリー＞使用時、同スキルのクリティカルヒット率が3秒間5％上昇する。最大20％。"}
    ]
}

SLOT_LIMITS = {"頭": 1, "肩": 1, "胴": 1, "脚": 1, "メインハンド": 2, "オフハンド": 2}
SLOT_ICONS = {"頭": "🪖", "肩": "🦺", "胴": "🛡️", "脚": "👟", "メインハンド": "🏹", "オフハンド": "🗡️"}

essences_json = json.dumps(ESSENCES, ensure_ascii=False)
limits_json = json.dumps(SLOT_LIMITS, ensure_ascii=False)
main_attacks_json = json.dumps(MAIN_ATTACKS, ensure_ascii=False)
skills_json = json.dumps(SKILLS, ensure_ascii=False)

HTML = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>デーモンハンター もぐらリサーチ精髄チェッカー</title>
<style>
  :root {{
    --bg-primary: #f0f4f8;
    --bg-secondary: #ffffff;
    --bg-card: #ffffff;
    --bg-card-hover: #f7fafc;
    --accent: #dc2626;
    --accent-glow: rgba(220,38,38,0.18);
    --accent2: #7c3aed;
    --gold: #d97706;
    --gold-dark: #b45309;
    --text-primary: #1a202c;
    --text-secondary: #4a5568;
    --text-muted: #a0aec0;
    --border: #e2e8f0;
    --border-accent: rgba(220,38,38,0.3);
    --selected-bg: rgba(220,38,38,0.07);
    --selected-border: #dc2626;
    --slot-head: #dc2626;
    --slot-shoulder: #9333ea;
    --slot-chest: #2563eb;
    --slot-legs: #0d9488;
    --slot-main: #ea580c;
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
    background: linear-gradient(135deg, #7f1d1d 0%, #450a0a 100%);
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
    background: linear-gradient(90deg, #fca5a5, #fde68a);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 0.05em;
  }}
  .header-title p {{ color: rgba(255,255,255,0.5); font-size: 0.75rem; margin-top: 0.1rem; }}
  .header-spacer {{ width: 80px; }}

  #selected-panel {{
    background: linear-gradient(135deg, #fff1f2, #fdf4ff);
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
    background: rgba(180,83,9,0.08);
    border: 1px solid rgba(180,83,9,0.3);
    border-radius: 20px;
    padding: 0.25rem 0.75rem;
    font-size: 0.75rem;
    cursor: pointer;
    transition: all 0.2s;
    color: var(--text-primary);
  }}
  .selected-tag:hover {{ background: rgba(180,83,9,0.15); }}
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
  .section-title.red {{ color: var(--accent); }}
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
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='%23dc2626'%3E%3Cpath d='M7 10l5 5 5-5z'/%3E%3C/svg%3E");
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
    background: linear-gradient(135deg, #b91c1c, var(--accent2));
    color: white;
    border: none;
    border-radius: 30px;
    padding: 0.85rem 3rem;
    font-size: 1rem;
    font-weight: 700;
    cursor: pointer;
    letter-spacing: 0.05em;
    transition: all 0.3s;
    box-shadow: 0 4px 20px rgba(220,38,38,0.3);
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
  #search-btn:hover {{ transform: translateY(-2px); box-shadow: 0 6px 30px rgba(220,38,38,0.45); }}
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
  .slot-limit.at-limit {{ background: rgba(220,38,38,0.1); color: var(--accent); font-weight: 700; }}
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
  .essence-card:hover {{ background: #fff1f2; border-color: rgba(220,38,38,0.2); }}
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
    background: rgba(220,38,38,0.07);
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
      <h1>🏹 デーモンハンター 精髄チェッカー</h1>
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
    <h2 class="section-title red">スキル選択</h2>
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
    <h2 class="section-title red">🔎 効果検索</h2>
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
const SLOT_ICONS = {{"頭":"🪖","肩":"🦺","胴":"🛡️","脚":"👟","メインハンド":"🏹","オフハンド":"🗡️"}};
const SLOT_ORDER = ["頭","肩","胴","脚","メインハンド","オフハンド"];
const BM_KEY = 'demonhunter_bookmarks';

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
