#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

# Windows CGI環境でのUTF-8出力
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-Type: text/html; charset=utf-8")
print()

# === データ定義 ===
MAIN_ATTACKS = ["波刃", "風刃"]

SKILLS = [
    "うねる白波", "スコール", "剣舞", "小滝", "嵐の憤怒",
    "横風", "流麗な一撃", "渦潮", "激流", "激浪",
    "砕波", "西風の猛追", "風の歩み", "霧包み"
]

ESSENCES = {
    "頭": [
        {"skill": "西風の猛追", "name": "林道の道", "desc": "消費した西風の数に応じて3秒間〈西風の猛追〉のダメージが11.4%増加する（最大34.2%）。"},
        {"skill": "スコール", "name": "風下を見よ", "desc": "〈スコール〉発動時、敵を3秒間マークした後に切り裂き、マーク中に標的に与えたダメージの28.5％分のダメージを与える。"},
        {"skill": "うねる白波", "name": "不屈の幻視", "desc": "〈うねる白波〉のクリティカルヒット時、水が爆発して付近の敵に17,928ダメージを与える。"},
        {"skill": "風の歩み", "name": "夜明けの笑み", "desc": "〈風の歩み〉のクールダウン時間が18.6％短縮される。"},
        {"skill": "小滝", "name": "壮麗な膨脹", "desc": "〈小滝〉発動時、定期的にプレイヤーと西風から水の爆発が放たれ、付近の敵にダメージを与える。"},
        {"skill": "小滝", "name": "迫りくる失明", "desc": "〈小滝〉発動時、西風が1体召喚されて指定地点の地面を叩き付け、波を発生させて付近の敵にダメージを与えて引き寄せる。"},
        {"skill": "小滝", "name": "聖なる喘ぎ", "desc": "〈小滝〉発動時、プレイヤーの周りに収束する気流を呼び起し、付近の敵にダメージを与えて空中に打ち上げる。気流のダメージと範囲は操っている西風の数に応じて増加する。"},
        {"skill": "小滝", "name": "夢の溺没", "desc": "〈小滝〉発動時、プレイヤーと西風が強化され、敵を攻撃した際に波が発生し、標的や付近の敵にダメージを与える。"},
        {"skill": "小滝", "name": "執拗なるバイデント", "desc": "〈小滝〉発動時、プレイヤーと西風が壊滅的な波を発生させ、敵にダメージを与えてスタンさせる。敵は次の攻撃で追加ダメージを受ける。スタンした敵にダメージを与えると効果が解除される。"},
        {"skill": "剣舞", "name": "解放者の目", "desc": "〈剣舞〉発動時、刃を投げて最初に当たった敵を串刺しにし、ダメージを与えてスタンさせる。刃は短時間、標的に刺さったままとなってダッシュスキルの使用を妨げ、再びスキルを発動すると敵に狙われなくなり、標的の背後までダッシュして進路上の敵すべてにダメージを与える。"},
        {"skill": "小滝", "name": "ヴァストウォッシュ", "desc": "〈小滝〉が床を冠水させ、敵にダメージを与えながらプレイヤーと範囲内の味方を強化し、スキル発動時に敵に打ち付けてダメージを与える波を発生させる。"},
        {"skill": "剣舞", "name": "愉悦の障害", "desc": "〈剣舞〉発動時、円形の風の刃を放ち、敵にダメージを与えて流血させる。"},
        {"skill": "剣舞", "name": "辛辣な歌", "desc": "〈剣舞〉発動時、刃を投げて最初に当たった敵を串刺しにし、力を吸収してプレイヤーの攻撃速度と移動速度を上昇させる。刃は短時間標的に刺さり続けた後、敵をスタンさせる。"},
        {"skill": "小滝", "name": "押し流す水流", "desc": "〈小滝〉発動時、高波が発生して潮だまりが形成される。潮だまりにいる敵は電撃ダメージを受けると感電状態になり、潮だまりにいる敵すべてに追加ダメージを与える。"},
        {"skill": "風の歩み", "name": "欺瞞の囁き", "desc": "クリティカルヒットを繰り出すたびに〈風の歩み〉のクールダウン時間が0.24秒短縮されるが、この効果は9秒に10回しか発動しない。"},
        {"skill": "激流", "name": "海山の兜", "desc": "〈激流〉が敵に操作障害もしくはノックバック効果を付与した場合、敵の受けるダメージが3秒間19%増加する。"},
        {"skill": "剣舞", "name": "ストームロストの相貌", "desc": "〈剣舞〉発動時、付近の敵すべてを引き寄せ、敵はダッシュスキルを使用できなくなる。"},
        {"skill": "小滝", "name": "悩みの多き波止場", "desc": "〈小滝〉発動時、刃を地面に叩きつけて付近の敵にダメージを与え、間欠泉が敵の足元から吹き出して打ち上げる。"},
        {"skill": "うねる白波", "name": "一瞬のしかめ面", "desc": "〈うねる白波〉がさらに、次の5回のメイン攻撃（発動後3秒以内）を強化してダメージを48%増加させる。"},
        {"skill": "激浪", "name": "職業病", "desc": "〈激浪〉発動時、自身と西風のメイン攻撃のダメージが2秒間28.5%上昇する。"},
        {"skill": "うねる白波", "name": "分別と殺戮", "desc": "〈うねる白波〉が敵を流血させるようになり、3秒間にわたり毎秒9,028ダメージを与える。ダメージ増加90.0%"}
    ],
    "肩": [
        {"skill": "流麗な一撃", "name": "外套の輝き", "desc": "3秒間〈流麗な一撃〉のダメージが22.8%増加する。"},
        {"skill": "渦潮", "name": "ザ・ショール", "desc": "〈渦潮〉が敵のアーマーを破壊するようになり、敵の受けるダメージが3秒間増加する（最大28.5%）。"},
        {"skill": "嵐の憤怒", "name": "数値なき嵐", "desc": "〈嵐の憤怒〉発動時、プレイヤーだけが強化され、メイン攻撃を3回繰り出すごとに標的の周りに猛烈な嵐を巻き起こし、付近の敵にダメージを与えて引き寄せる。"},
        {"skill": "風の歩み", "name": "重みなき存在", "desc": "〈風の歩み〉発動時、回避率が上昇し、全スキルのクールダウン時間が短縮される。"},
        {"skill": "砕波", "name": "豊作の兆し", "desc": "〈砕波〉のクールダウン時間が18.6%減少する。"},
        {"skill": "霧包み", "name": "高位な金貨", "desc": "西風の持続時間が短くなるが、消滅時に敵に突進して爆発し、付近の敵すべてにダメージを与える。霧包みのダメージが増加:18.0%"},
        {"skill": "流麗な一撃", "name": "反抗の団結", "desc": "〈流麗な一撃〉発動時、西風が追加で1体召喚される。流麗な一撃のクールダウン時間が短縮:3.6%"},
        {"skill": "砕波", "name": "フジツボの飾り盾", "desc": "〈砕波〉のチャージ上限が1増加する。砕波のクールダウン時間が短縮:3.6%"},
        {"skill": "砕波", "name": "デプスドローン", "desc": "〈砕波〉発動時、4秒間、与えるダメージが19%増加する。"},
        {"skill": "流麗な一撃", "name": "安全な境界", "desc": "操作障害状態やノックバック状態でも〈流麗な一撃〉が発動可能になり、完全な操作障害効果とノックバックを0.5秒間無効化する。流麗な一撃のクールダウン時間が短縮:3.6%"},
        {"skill": "風の歩み", "name": "疾風の恵み", "desc": "〈風の歩み〉がプレイヤー自身を強化するようになる。強化中、メイン攻撃時にダメージを吸収するシールドが付与され、ノックバック効果が無効化される。風の歩みのクールダウン時間が短縮:7.2%"},
        {"skill": "風の歩み", "name": "ブレステイカー", "desc": "〈風の歩み〉発動時、移動するごとにプレイヤーの周りにつむじ風が発生し、ランダムな敵にダメージを与えて速度を低下させる。風の歩みのダメージが増加:18.0%"},
        {"skill": "嵐の憤怒", "name": "聖化された旅", "desc": "〈嵐の憤怒〉発動時、敵を風で包み込み、ダメージを与えて空中に打ち上げる。標的が攻撃を3回受けると爆発し、付近の敵に追加ダメージを与える。嵐の憤怒のダメージが増加:18.0%"},
        {"skill": "嵐の憤怒", "name": "唸るポールド", "desc": "〈嵐の憤怒〉発動時、プレイヤーを追従する雷嵐が出現し、付近のランダムな敵に連続で電撃ダメージを与える。嵐の憤怒のダメージが増加:18.0%"},
        {"skill": "風の歩み", "name": "垂涎の軟骨", "desc": "〈風の歩み〉発動時、〈切り裂く風〉が付与されて不可視状態になり、移動速度とクリティカルヒット率が上昇する。ボーナスクリティカルヒット率は不可視状態が解除されたあともしばらく持続する。風の歩みのクールダウン時間が短縮:7.2%"},
        {"skill": "嵐の憤怒", "name": "甲殻の留金", "desc": "〈嵐の憤怒〉発動時、プレイヤーが強化されて切り裂く旋風に包まれ、移動速度が上昇し、付近の敵を引き寄せながらダメージを与える。嵐の憤怒のダメージが増加:18.0%"},
        {"skill": "砕波", "name": "贖罪者の帳", "desc": "〈砕波〉のクールダウン時間がダメージを与えた敵1体につき0.16秒短縮される（最大1.6秒）。"},
        {"skill": "砕波", "name": "クサスラの使命", "desc": "〈砕波〉発動時、44,636ダメージを吸収するシールドが2秒間付与され、操作障害効果を1回無効化する。盾の効果が増加:54.0%"},
        {"skill": "流麗な一撃", "name": "衝撃への沈淪", "desc": "〈流麗な一撃〉がさらに、クリティカルヒット率を3秒間15.2%上昇させる。"},
        {"skill": "嵐の憤怒", "name": "ハウルフューリー", "desc": "〈嵐の憤怒〉が自身と西風を強化し、メイン攻撃がダメージを与えると〈風の印〉を蓄積させる。印を付けられた敵はその蓄積によって追加ダメージを受ける。嵐の憤怒のダメージが増加:18.0%"},
        {"skill": "流麗な一撃", "name": "漂流する記憶", "desc": "〈流麗な一撃〉がさらに、メイン攻撃速度を3秒間38%上昇させる。"}
    ],
    "胴": [
        {"skill": "流麗な一撃", "name": "冒流の戦利品", "desc": "〈流麗な一撃〉発動時、前方にダッシュしてダッシュし終えると西風を数体召喚する。流麗な一撃のクールダウン時間が短縮:7.2%"},
        {"skill": "渦潮", "name": "驀進する水流", "desc": "〈渦潮〉発動時、指定地点に水の柱が発生し、敵に継続ダメージを与えながら中心に引き寄せる。中心まで引き寄せられた敵は空中に打ち上げられる。渦潮のクールダウン時間が短縮:7.2%"},
        {"skill": "うねる白波", "name": "商人の天秤", "desc": "〈うねる白波〉発動時、西風を1体召喚する。うねる白波のクールダウン時間が短縮:3.6%"},
        {"skill": "激流", "name": "潮目の力", "desc": "〈激流〉発動時、プレイヤーに向かって波が打ち付けられ、敵を引き寄せてダメージを与え、スタンさせる。激流のクールダウン時間が短縮:7.2%"},
        {"skill": "渦潮", "name": "オーバーフロー", "desc": "〈渦潮〉発動時、ランダムな敵の足元で間欠泉が毎秒爆発し、ダメージを与えて空中に打ち上げる。渦潮のダメージが増加:18.0%"},
        {"skill": "小滝", "name": "脱走兵の誇り", "desc": "〈小滝〉発動時、メイン攻撃速度も5.7秒間30%上昇する。"},
        {"skill": "流麗な一撃", "name": "西風の護り", "desc": "〈流麗な一撃〉発動時、西風が召喚され、指定地点の敵を切り裂いてスタンさせた後、プレイヤーは前方にダッシュしながら連続で切りつける。流麗な一撃のクールダウン時間が短縮:7.2%"},
        {"skill": "小滝", "name": "祝福のアシェト", "desc": "〈小滝〉が敵に命中すると移動速度が3.8秒間40%上昇する。"},
        {"skill": "小滝", "name": "フェード・トゥ・ブロンズ", "desc": "〈小滝〉が命中した敵は弱体化し、4秒間、受けるクリティカルヒットダメージが47.5%増加する。"},
        {"skill": "剣舞", "name": "はためく逃亡", "desc": "〈剣舞〉発動時、メイン攻撃のダメージが3秒間16%上昇する（最大32%）。"},
        {"skill": "小滝", "name": "敬虔なる賢者", "desc": "〈小滝〉のクールダウン時間が18.6%短縮される。"},
        {"skill": "スコール", "name": "滑らかな殻", "desc": "〈スコール〉発動時、ダメージが5.7秒間8%上昇する。この効果は最大3回まで蓄積する。"},
        {"skill": "流麗な一撃", "name": "流体の式服", "desc": "〈流麗な一撃〉発動時、水中に溶け込んで一時的に敵から狙われなくなり、元の姿に戻ると西風を2体召喚して、ダメージを吸収するシールドを得る。流麗な一撃のクールダウン時間が短縮:7.2%"},
        {"skill": "流麗な一撃", "name": "対のダブレット", "desc": "〈流麗な一撃〉発動時、標的に雷を落として印を付与する。再度発動すると2体の西風が出現する。西風は印を付与された標的に向かってプレイヤーと一緒に突進し、強力な雷攻撃を繰り出す。印と斬撃の両方が感電効果を付与する。流麗な一撃のダメージが増加:18.0%"},
        {"skill": "流麗な一撃", "name": "メメント・オヌス", "desc": "〈流麗な一撃〉発動時、前方にダッシュして進路上の敵にダメージを与えてスタンさせ、付近の敵を攻撃する西風を召喚する。〈流麗な一撃〉がクリティカルヒットした場合、追加の西風を召喚する。流麗な一撃のダメージが増加:18.0%"},
        {"skill": "激流", "name": "アシカの毛皮", "desc": "〈激流〉発動時、移動中にエネルギーが生成される。エネルギーが最大になってから発動すると波に乗って前方にダッシュし、進路上の敵すべてにダメージを与えてノックバックする。激流のダメージが増加:18.0%"},
        {"skill": "激流", "name": "ハナラグの艦隊", "desc": "〈激流〉発動時、プレイヤーと西風が渦潮に包まれ、付近の敵すべてに継続ダメージを与える。激流のダメージが増加:18.0%"},
        {"skill": "小滝", "name": "光り輝く逆流", "desc": "ライフが50%未満の敵に対する〈小滝〉のクリティカルヒット率が38%上昇する。"},
        {"skill": "流麗な一撃", "name": "盗まれた誓い", "desc": "〈流麗な一撃〉発動時、前方にダッシュして進路上にいる敵にダメージを与える。敵プレイヤーに命中すると強制的にこちらに背を向けさせて移動不能状態にする。流麗な一撃のクールダウン時間が短縮:7.2%"},
        {"skill": "激浪", "name": "流れと狂乱", "desc": "〈激浪〉がさらに、メイン攻撃速度を2秒間24%上昇させる。"},
        {"skill": "流麗な一撃", "name": "新たなる暁", "desc": "〈流麗な一撃〉で５秒間強化され、ダッシュスキルを使用するたびに波（0.5秒に１回発動可能）を放ち、敵に36,864ダメージを与えてノックバックさせる。同じ敵をノックバックできるのは６秒に１回まで。流麗な一撃のダメージが増加：18.0%"}
    ],
    "脚": [
        {"skill": "激浪", "name": "フォグカッター", "desc": "〈激浪〉によって西風の間をダッシュし、進路上の敵にダメージを与え複数個の水の刃を放つ。ダッシュ中は操作障害とノックバックが無効。激浪のダメージが増加:18.0%"},
        {"skill": "流麗な一撃", "name": "船乗りの精霊", "desc": "〈流麗な一撃〉で、3秒間ダメージが19%増加する。"},
        {"skill": "霧包み", "name": "吹きさらしの約束", "desc": "操っている西風1体につき、プレイヤーの攻撃速度が13.3%上昇する。"},
        {"skill": "霧包み", "name": "真実の財宝", "desc": "〈霧包み〉のクールダウン時間がスキルを発動するごとに0.95秒短縮される。"},
        {"skill": "砕波", "name": "燃えさかる灯台", "desc": "〈砕波〉発動時、前方にダッシュして敵にダメージを与え、通過地点に西風を召喚する。また、吸収シールドも得る。砕波のクールダウン時間が短縮:7.2%"},
        {"skill": "砕波", "name": "深淵の足跡", "desc": "〈砕波〉発動時、西風を2体召喚して波に乗り、進路上の敵にダメージを与える。砕波のクールダウン時間が短縮:7.2%"},
        {"skill": "西風の猛追", "name": "贖罪の烙印", "desc": "〈西風の猛追〉発動時、同じ敵に命中するたびにダメージが15.2%ずつ増加していく（最大76%）。"},
        {"skill": "砕波", "name": "冗長な双子", "desc": "〈砕波〉発動時、2体の西風を召喚する。西風は波のように互いに衝突し、進路上の敵にダメージを与えてノックバックさせる。砕波のクールダウン時間が短縮:7.2%"},
        {"skill": "砕波", "name": "ウェーブライダー", "desc": "〈砕波〉発動時、前方にダッシュして進路上の敵すべてにダメージを与えてノックバックさせ、移動先で西風を召喚する。砕波のクールダウン時間が短縮:7.2%"},
        {"skill": "激浪", "name": "純たる意志", "desc": "〈激浪〉発動時、西風が指定地点に突撃し、進路上の敵にダメージを与えてスタンさせる。激浪のダメージが増加:18.0%"},
        {"skill": "激浪", "name": "孤立の優美", "desc": "〈激浪〉発動時、操っている西風を犠牲にして、ダメージを吸収して投擲物を防ぐシールドを味方に与える。盾の効果が増加:10.8%"},
        {"skill": "横風", "name": "遠吠えの錨", "desc": "〈横風〉発動時に敵が5秒間流血するようになり、毎秒7,093ダメージを与える。横風のダメージが増加:9.0%"},
        {"skill": "嵐の憤怒", "name": "スパイントゥースのすね当て", "desc": "〈嵐の憤怒〉が敵に命中するとメイン攻撃速度も5%上昇する。この効果は6回まで蓄積する。嵐の憤怒のクールダウン時間が短縮:3.6%"},
        {"skill": "霧包み", "name": "ヴェイポライザー", "desc": "西風が消えると霧包みのオーブが出現しなくなり、代わりに潮だまりが形成される。潮だまりにいる敵は電撃ダメージを受けると感電状態になり、潮だまりにいる敵すべてに40,529の追加ダメージを与える。霧包みのクールダウン時間が短縮:3.6%"},
        {"skill": "流麗な一撃", "name": "無慈悲な勢い", "desc": "〈流麗な一撃〉発動時、3秒間〈水の道〉が付与され、次にスキルを発動するまでダメージが48%増加する。"},
        {"skill": "横風", "name": "北風の導き", "desc": "〈横風〉発動後、次のスキルによるダメージが4秒間48%増加する。"},
        {"skill": "砕波", "name": "ミストウォーカー", "desc": "〈砕波〉発動時、敵に狙われなくなり、波に乗ってダッシュして進路上の敵にダメージを与え、西風を召喚する。砕波のダメージが増加:18.0%"},
        {"skill": "砕波", "name": "戸惑いの海岸", "desc": "〈砕波〉発動時、プレイヤーの位置に西風を召喚した後、プレイヤーが標的の方向に突進し、与えるダメージが増加する。〈砕波〉を再使用する、範囲から離れる、もしくは効果が切れると元の位置に戻る。砕波のクールダウン時間が短縮:7.2%"},
        {"skill": "横風", "name": "ハリットの脚甲", "desc": "〈横風〉がさらに、メイン攻撃速度を3秒間38%上昇させる。"},
        {"skill": "激浪", "name": "殺しの幻影", "desc": "〈激浪〉が自身の周囲に複数の西風を召喚する。激浪のクールダウン時間が短縮:7.2%"},
        {"skill": "横風", "name": "血の芳香", "desc": "〈横風〉は流血状態の敵にさらに27,085ダメージを与える。同じ敵に対しては1秒に1回しか追加ダメージを与えられない。ダメージ増加90.0%"}
    ],
    "メインハンド": [
        {"skill": "激浪", "name": "嵐の瞳", "desc": "〈激浪〉が付近の西風ごとに3秒間スキルのダメージが11.4%増加する（最大34.2%）。"},
        {"skill": "スコール", "name": "螺旋の導き", "desc": "〈スコール〉が連続発動スキルに変化し、プレイヤーと西風が定期的に風の刃を放ち、進路上の敵にダメージを与える。スコールのダメージが増加:18.0%"},
        {"skill": "うねる白波", "name": "サード・デュース", "desc": "〈うねる白波〉発動時、プレイヤーの刃が強化され、一時的に完全な操作障害効果とノックバック効果が無効になる。強化中は、プレイヤーと西風のメイン攻撃が、命中するごとにダメージの増加する剣によるなぎ払い攻撃になる。うねる白波のダメージが増加:18.0%"},
        {"skill": "スコール", "name": "協調のキャスティール", "desc": "〈スコール〉発動時、敵から狙われなくなると同時に、プレイヤーと西風が前方にダッシュして進路上の敵にダメージを与える。さらに、プレイヤーと一緒にダッシュした西風数に従ってメイン攻撃速度が上昇する。スコールのダメージが増加:18.0%"},
        {"skill": "うねる白波", "name": "冠水せし小川", "desc": "〈うねる白波〉発動時、刃が強化され、移動中のプレイヤーと西風のメイン攻撃が渦巻く鞭攻撃になる。うねる白波のダメージが増加:18.0%"},
        {"skill": "波刃", "name": "水溜の讃美歌", "desc": "〈波刃〉発動時、同じ敵を4回攻撃した後、西風を1.5秒間召喚する。波刃のダメージが増加:9.0%"},
        {"skill": "風の歩み", "name": "グラスブレード・エッジ", "desc": "〈風の歩み〉の持続時間が28.5%増加する。"},
        {"skill": "横風", "name": "シュリークワース", "desc": "〈横風〉発動時、クリティカルヒットで4つの風の刃が発生して標的のもとで砕け散り、命中した敵に20,086ダメージを与える。この効果は0.5秒に1回しか発動しない。ダメージ増加90.0%"},
        {"skill": "風刃", "name": "悪魔断ち", "desc": "〈風刃〉が6秒ごとに強化され、次の攻撃が敵を貫通して切り裂く風を放つ。風は敵に19,386ダメージを与えてアーマーを粉砕し、3秒間、ダメージが19%増加する。"},
        {"skill": "スコール", "name": "千の終焉", "desc": "〈スコール〉がプレイヤーと西風を強化し、ダッシュスキルの発動時に敵に追加ダメージを与えてアーマーを粉砕し、受けるダメージを増加させる。スコールのダメージが増加:18.0%"},
        {"skill": "風の歩み", "name": "マールウェンの恭謙", "desc": "〈風の歩み〉発動時、操作障害以外の全デバフ効果が取り除かれる。風の歩みのクールダウン時間が短縮:3.6%"},
        {"skill": "スコール", "name": "深淵の回帰", "desc": "〈スコール〉発動時、プレイヤーと西風が前方にダッシュし、進路上の敵にダメージを与える。流血状態の敵に命中すると即座に残りの流血ダメージを与えて、〈スコール〉のクールダウン時間がリセットされる。スコールのダメージが増加:18.0%"},
        {"skill": "うねる白波", "name": "不揃いの結盟", "desc": "〈うねる白波〉発動時、刃が強化され、プレイヤーと西風のメイン攻撃が自分のもとに戻ってくる水の短剣を投げるようになる。発動中、スキルまたはメイン攻撃を繰り出すごとに短剣が1つ追加される。うねる白波のダメージが増加:18.0%"},
        {"skill": "波刃", "name": "嵐の紋章", "desc": "〈波刃〉の最後の一撃が命中した敵に連続で雷が落ち、29,378の電撃ダメージを与える。ダメージ増加90.0%"},
        {"skill": "風刃", "name": "ファングダウズ", "desc": "〈風刃〉のクリティカルヒットが敵のアーマーを破壊するようになり、敵の受けるクリティカルヒットダメージが2秒間34.5%増加する。"},
        {"skill": "嵐の憤怒", "name": "ノックブロッドの角", "desc": "〈嵐の憤怒〉でダメージを与えると、クリティカルヒット率が3秒間7.6%上昇する（最大22.8%）。"},
        {"skill": "激流", "name": "タイドブレーカー", "desc": "〈激流〉発動時、命中した敵1体につき与えるダメージが3秒間、7.6%増加する（最大22.8%）。"},
        {"skill": "スコール", "name": "叫ぶ突風", "desc": "〈スコール〉発動時、刃と共に回転し、付近の敵を引き寄せてダメージを与え、刻印を付与する。数秒後に刻印が爆発し、爆発までに与えたダメージの一定割合に等しい追加ダメージを与える。スコールのダメージが増加:18.0%"},
        {"skill": "うねる白波", "name": "最後の裏切り", "desc": "〈うねる白波〉発動時、次の数回のメイン攻撃が強化され、ボルトを放つようになる。ボルトが同じ敵の背中に連続で命中するとダメージが増加する。うねる白波のダメージが増加:18.0%"},
        {"skill": "波刃", "name": "数多のうちの最初", "desc": "〈波刃〉が4回命中するたびに敵を空中に吹き飛ばす。効果は同じ敵プレイヤーに対して4秒に1回しか発動しない。波刃のダメージが増加:9.0%"},
        {"skill": "うねる白波", "name": "ハルスラッシャー", "desc": "〈うねる白波〉が自身を5秒間強化し、メイン攻撃をダッシュに変化させ、進路上の敵に40,543ダメージを与えてアーマーを粉砕し、2秒間受けるダメージを5%増加させる。この効果は最大6回まで蓄積する。このスキルを使用すると2秒間操作障害とノックバック効果が無効になる。"}
    ],
    "オフハンド": [
        {"skill": "西風の猛追", "name": "無窮の囁き", "desc": "〈西風の猛追〉が全ての西風を消費してプレイヤーを標的の位置にテレポートさせる。テレポートした先で消費した西風に応じた回数斬撃を行う。この攻撃中は敵に狙われなくなる。消費した西風は攻撃が終わると復活する。西風の猛追のダメージが増加:18.0%"},
        {"skill": "剣舞", "name": "サミリアン・ウィンドブラシ", "desc": "〈剣舞〉のチャージ上限が1増加する。剣舞のクールダウン時間が短縮:3.6%"},
        {"skill": "横風", "name": "竜巻の妨害", "desc": "〈横風〉発動時、風で刃を強化し、プレイヤーと西風のメイン攻撃が風の刃となって敵にダメージを与える。横風のダメージが増加:18.0%"},
        {"skill": "横風", "name": "こだまする空", "desc": "〈横風〉発動時、プレイヤーと西風が風の刃を放ち、敵にダメージを与えて速度を低下させる。横風のダメージが増加:18.0%"},
        {"skill": "渦潮", "name": "クサスラの栄光", "desc": "〈渦潮〉が敵に命中するとメイン攻撃速度が3秒間28.5%上昇する。"},
        {"skill": "霧包み", "name": "マーロジの背骨", "desc": "〈西風〉のダメージが28.5%増加する。"},
        {"skill": "西風の猛追", "name": "ミストウィスパー", "desc": "〈西風の猛追〉発動時、敵に狙われなくなり、敵に向かってダッシュして素早く連続攻撃する。西風の消費数に応じて攻撃回数が増える。西風の猛追のダメージが増加:18.0%"},
        {"skill": "横風", "name": "旋風の呼び声", "desc": "〈横風〉が連続発動スキルに変化して移動中に使用できるようになる。プレイヤーと西風が回転し、風の刃を放ち、付近の敵にダメージを与える。横風のダメージが増加:18.0%"},
        {"skill": "西風の猛追", "name": "ダイン・オン・フィッシュテール", "desc": "〈西風の猛追〉発動時、チャージするとダメージが増加して強烈な空気の刃を放てるようになる。西風を消費するごとにこの攻撃のクリティカルヒット率が上昇する。西風の猛追のダメージが増加:18.0%"},
        {"skill": "風刃", "name": "一度きりのチャンス", "desc": "スキルを発動させると〈風刃〉が強化され、次の2回のメイン攻撃が付近の敵に27,075の追加ダメージを与える。ダメージ増加90.0%"},
        {"skill": "霧包み", "name": "一口の吐息", "desc": "霧包みのオーブによって4秒間攻撃速度と移動速度が28.5%上昇する。"},
        {"skill": "風刃", "name": "リッパージョーズ", "desc": "スキルを3回発動させると〈風刃〉が強化され、次のメイン攻撃発動時に突風を放ち、敵に19,007ダメージを与えて流血させる。4秒間、毎秒7,093の継続ダメージを与える。ダメージ増加90.0%"},
        {"skill": "剣舞", "name": "迅速と無垢", "desc": "〈剣舞〉が敵に命中するとクリティカルヒット率が3秒間19%上昇する。"},
        {"skill": "西風の猛追", "name": "スパークスカル", "desc": "〈西風の猛追〉発動時、敵から狙われなくなり、前方にダッシュして進路上の敵に電撃でダメージを与える。感電状態の敵には追加のダメージを与える。ダッシュ時に消費した西風ごとに追加チャージを獲得する。西風の猛追のダメージが増加:18.0%"},
        {"skill": "西風の猛追", "name": "沈みし深淵", "desc": "〈西風の猛追〉発動時、標的と距離を取りながら複数の刃を標的や付近の敵に放つ。刃がクリティカルヒットすると2つに分裂し、再び標的を攻撃する。西風の猛追のダメージが増加:18.0%"},
        {"skill": "横風", "name": "珊瑚の軸", "desc": "〈横風〉発動時、前方にダッシュし、付近の敵に向かって複数の風刃を放つ。ダッシュ距離と風刃の数は移動速度に比例して増加する。横風のダメージが増加:18.0%"},
        {"skill": "剣舞", "name": "鋸状の巻貝", "desc": "〈剣舞〉が敵に命中すると〈風枷〉を3秒間付与し、敵を5回攻撃するたびに13,390の追加ダメージを与える。この効果は同じ敵に対しては0.3秒に1回しか発動しない。ダメージ増加90.0%"},
        {"skill": "風刃", "name": "囁くそよ風", "desc": "ライフが50%未満の敵に〈風刃〉でダメージを与えると、突進のクールダウン時間が1.5秒短縮される。風刃のダメージが増加:9.0%"},
        {"skill": "横風", "name": "留め具割り", "desc": "〈横風〉発動時、プレイヤーが強化され、次のメイン攻撃時に貫通性の風の刃を放てるようになる。刃は敵の防具を破壊し、その敵に対する自身のダメージを増加させる。横風のダメージが増加:18.0%"},
        {"skill": "波刃", "name": "満たされぬ飢え", "desc": "〈波刃〉によりダメージを与えるたびにメイン攻撃速度が3秒間9.5%上昇する（最大28.5%）。"},
        {"skill": "横風", "name": "霞刃", "desc": "〈横風〉で自身を5秒間強化し、ダッシュスキルを使用するたびに風の刃を1個発生させ保持する。この効果は最大3回まで蓄積する。風の刃は0.5秒に1回まで発生する。次のメイン攻撃で保持している風の刃を全て消費して回転する刃で攻撃し、風の刃1個あたり40,543ダメージを与える。刃が流血している敵にヒットすると、自身のライフが与えたダメージの20%回復する。横風のダメージが増加：18.0%"}
    ]
}

SLOT_LIMITS = {"頭": 1, "肩": 1, "胴": 1, "脚": 1, "メインハンド": 2, "オフハンド": 2}
SLOT_ICONS = {"頭": "🪖", "肩": "🦺", "胴": "🛡️", "脚": "👟", "メインハンド": "⚔️", "オフハンド": "🗡️"}

essences_json = json.dumps(ESSENCES, ensure_ascii=False)
limits_json = json.dumps(SLOT_LIMITS, ensure_ascii=False)
main_attacks_json = json.dumps(MAIN_ATTACKS, ensure_ascii=False)
skills_json = json.dumps(SKILLS, ensure_ascii=False)

HTML = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>テンペスト スキル・精髄チェッカー | Diablo Immortal</title>
<style>
  :root {{
    --bg-primary: #0a0d14;
    --bg-secondary: #10151f;
    --bg-card: #161c2a;
    --bg-card-hover: #1e2738;
    --accent: #4fc3f7;
    --accent-glow: rgba(79,195,247,0.3);
    --accent2: #7c4dff;
    --gold: #ffd54f;
    --gold-dark: #f9a825;
    --text-primary: #e8eaf6;
    --text-secondary: #90a4ae;
    --text-muted: #546e7a;
    --border: #1e2d3d;
    --border-accent: #4fc3f730;
    --selected-bg: rgba(79,195,247,0.12);
    --selected-border: #4fc3f7;
    --success: #66bb6a;
    --slot-head: #ef5350;
    --slot-shoulder: #ab47bc;
    --slot-chest: #42a5f5;
    --slot-legs: #26a69a;
    --slot-main: #ffa726;
    --slot-off: #ec407a;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Segoe UI', 'Noto Sans JP', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    min-height: 100vh;
    line-height: 1.6;
  }}
  /* Header */
  header {{
    background: linear-gradient(135deg, #0d1b2e 0%, #1a0a2e 100%);
    border-bottom: 1px solid var(--border);
    padding: 1rem 1.5rem;
    text-align: center;
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(10px);
  }}
  header h1 {{
    font-size: clamp(1rem, 3vw, 1.4rem);
    font-weight: 700;
    background: linear-gradient(90deg, var(--accent), var(--gold));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 0.05em;
  }}
  header p {{ color: var(--text-secondary); font-size: 0.8rem; margin-top: 0.2rem; }}

  /* Selected panel */
  #selected-panel {{
    background: linear-gradient(135deg, #0f1923, #1a1030);
    border-bottom: 1px solid var(--border-accent);
    padding: 0.75rem 1.5rem;
    display: none;
  }}
  #selected-panel h2 {{
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--gold);
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
    background: rgba(255,213,79,0.1);
    border: 1px solid rgba(255,213,79,0.4);
    border-radius: 20px;
    padding: 0.25rem 0.75rem;
    font-size: 0.75rem;
    cursor: pointer;
    transition: all 0.2s;
  }}
  .selected-tag:hover {{ background: rgba(255,213,79,0.2); }}
  .selected-tag .slot-badge {{
    font-size: 0.65rem;
    opacity: 0.7;
  }}
  .selected-tag .remove-btn {{
    opacity: 0.5;
    font-size: 0.8rem;
    margin-left: 0.2rem;
  }}
  .selected-tag:hover .remove-btn {{ opacity: 1; }}

  /* Main container */
  main {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 1.5rem;
  }}

  /* Skill selection */
  .skill-section {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
  }}
  .skill-section h2 {{
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--accent);
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }}
  .skill-section h2::before {{
    content: '';
    display: block;
    width: 3px;
    height: 1em;
    background: var(--accent);
    border-radius: 2px;
  }}
  .skill-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 0.8rem;
  }}
  .skill-slot {{
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
  }}
  .skill-slot label {{
    font-size: 0.72rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }}
  .skill-slot select {{
    background: var(--bg-secondary);
    color: var(--text-primary);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.5rem 0.75rem;
    font-size: 0.85rem;
    cursor: pointer;
    transition: border-color 0.2s;
    width: 100%;
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='%234fc3f7'%3E%3Cpath d='M7 10l5 5 5-5z'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    padding-right: 2rem;
  }}
  .skill-slot select:focus {{
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 2px var(--accent-glow);
  }}
  .skill-slot select.has-value {{
    border-color: var(--accent);
    color: var(--accent);
  }}

  /* Search button */
  .search-wrap {{
    text-align: center;
    margin: 1.5rem 0;
  }}
  #search-btn {{
    background: linear-gradient(135deg, #0077b6, var(--accent2));
    color: white;
    border: none;
    border-radius: 30px;
    padding: 0.85rem 3rem;
    font-size: 1rem;
    font-weight: 700;
    cursor: pointer;
    letter-spacing: 0.05em;
    transition: all 0.3s;
    box-shadow: 0 4px 20px rgba(79,195,247,0.3);
    position: relative;
    overflow: hidden;
  }}
  #search-btn::before {{
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
    transition: left 0.5s;
  }}
  #search-btn:hover::before {{ left: 100%; }}
  #search-btn:hover {{ transform: translateY(-2px); box-shadow: 0 6px 30px rgba(79,195,247,0.5); }}
  #search-btn:active {{ transform: translateY(0); }}

  /* Results */
  #results {{ display: none; }}
  #results h2 {{
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-secondary);
    margin-bottom: 1rem;
    text-align: center;
  }}
  .slots-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1rem;
  }}
  .slot-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    transition: border-color 0.2s;
  }}
  .slot-card:hover {{ border-color: var(--border-accent); }}
  .slot-header {{
    padding: 0.75rem 1rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid var(--border);
  }}
  .slot-title {{
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 700;
    font-size: 0.95rem;
  }}
  .slot-limit {{
    font-size: 0.7rem;
    background: rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 0.15rem 0.5rem;
    color: var(--text-secondary);
  }}
  .slot-limit.at-limit {{ background: rgba(79,195,247,0.15); color: var(--accent); }}
  .slot-essences {{ padding: 0.5rem; }}
  .essence-count {{
    font-size: 0.7rem;
    color: var(--text-muted);
    padding: 0.3rem 0.5rem;
    text-align: right;
  }}
  .no-essences {{
    padding: 1.5rem;
    text-align: center;
    color: var(--text-muted);
    font-size: 0.85rem;
  }}

  /* Essence card */
  .essence-card {{
    border: 1px solid transparent;
    border-radius: 8px;
    padding: 0.65rem 0.75rem;
    cursor: pointer;
    transition: all 0.2s;
    margin-bottom: 0.35rem;
    position: relative;
  }}
  .essence-card:hover {{
    background: var(--bg-card-hover);
    border-color: var(--border-accent);
  }}
  .essence-card.selected {{
    background: var(--selected-bg);
    border-color: var(--selected-border);
    box-shadow: 0 0 0 1px var(--selected-border) inset;
  }}
  .essence-card.disabled {{
    opacity: 0.4;
    cursor: not-allowed;
  }}
  .essence-card.disabled:hover {{
    background: transparent;
    border-color: transparent;
  }}
  .essence-name {{
    font-weight: 600;
    font-size: 0.88rem;
    color: var(--text-primary);
    margin-bottom: 0.25rem;
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }}
  .essence-name .check-icon {{
    color: var(--accent);
    font-size: 0.75rem;
    display: none;
  }}
  .essence-card.selected .check-icon {{ display: inline; }}
  .essence-skill {{
    font-size: 0.7rem;
    color: var(--text-muted);
    margin-bottom: 0.3rem;
  }}
  .essence-skill span {{
    color: var(--accent);
    background: rgba(79,195,247,0.1);
    padding: 0.1rem 0.4rem;
    border-radius: 4px;
  }}
  .essence-desc {{
    font-size: 0.75rem;
    color: var(--text-secondary);
    line-height: 1.5;
  }}

  /* Slot color accents */
  .slot-card[data-slot="頭"] .slot-header {{ border-left: 3px solid var(--slot-head); }}
  .slot-card[data-slot="肩"] .slot-header {{ border-left: 3px solid var(--slot-shoulder); }}
  .slot-card[data-slot="胴"] .slot-header {{ border-left: 3px solid var(--slot-chest); }}
  .slot-card[data-slot="脚"] .slot-header {{ border-left: 3px solid var(--slot-legs); }}
  .slot-card[data-slot="メインハンド"] .slot-header {{ border-left: 3px solid var(--slot-main); }}
  .slot-card[data-slot="オフハンド"] .slot-header {{ border-left: 3px solid var(--slot-off); }}

  /* Responsive */
  @media (max-width: 600px) {{
    main {{ padding: 1rem; }}
    .skill-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .slots-grid {{ grid-template-columns: 1fr; }}
    header {{ padding: 0.75rem 1rem; }}
    #selected-panel {{ padding: 0.75rem 1rem; }}
  }}

  /* Animation */
  @keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(10px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}
  .slot-card {{ animation: fadeIn 0.3s ease both; }}
  .slot-card:nth-child(1) {{ animation-delay: 0.05s; }}
  .slot-card:nth-child(2) {{ animation-delay: 0.1s; }}
  .slot-card:nth-child(3) {{ animation-delay: 0.15s; }}
  .slot-card:nth-child(4) {{ animation-delay: 0.2s; }}
  .slot-card:nth-child(5) {{ animation-delay: 0.25s; }}
  .slot-card:nth-child(6) {{ animation-delay: 0.3s; }}

  /* Tooltip on mobile */
  .tooltip-hint {{
    font-size: 0.7rem;
    color: var(--text-muted);
    text-align: center;
    margin-bottom: 0.75rem;
  }}
</style>
</head>
<body>

<header>
  <h1>⚔️ テンペスト 精髄チェッカー</h1>
  <p>Diablo Immortal — スキルを選択して使用可能な精髄を検索</p>
</header>

<div id="selected-panel">
  <h2>✨ 選択中の精髄</h2>
  <div id="selected-list"></div>
</div>

<main>
  <section class="skill-section">
    <h2>スキル選択</h2>
    <div class="skill-grid" id="skill-grid">
      <!-- populated by JS -->
    </div>
  </section>

  <div class="search-wrap">
    <button id="search-btn" onclick="doSearch()">🔍 精髄を検索</button>
  </div>

  <div id="results">
    <h2>使用可能な精髄一覧</h2>
    <p class="tooltip-hint">精髄をタップ／クリックして選択（頭・肩・胴・脚：各1つ、メインハンド・オフハンド：各2つまで）</p>
    <div class="slots-grid" id="slots-grid"></div>
  </div>
</main>

<script>
const ESSENCES = {essences_json};
const LIMITS = {limits_json};
const MAIN_ATTACKS = {main_attacks_json};
const SKILLS = {skills_json};
const SLOT_ICONS = {{"頭":"🪖","肩":"🦺","胴":"🛡️","脚":"👟","メインハンド":"⚔️","オフハンド":"🗡️"}};
const SLOT_ORDER = ["頭","肩","胴","脚","メインハンド","オフハンド"];

// selected: {{slotName: [{{name, skill, desc}}, ...]}}
const selected = {{}};
SLOT_ORDER.forEach(s => selected[s] = []);

// Build skill selects
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
      <select id="${{s.id}}" onchange="onSkillChange()">
        <option value="">-- 未設定 --</option>
        ${{s.options.map(o => `<option value="${{o}}">${{o}}</option>`).join('')}}
      </select>`;
    grid.appendChild(div);
  }});
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
  // Prevent duplicate skill selections (not main attack)
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

  const mainSel = document.getElementById('main');
  mainSel.classList.toggle('has-value', !!mainSel.value);
}}

function doSearch() {{
  const skills = getSelectedSkills();
  const slotsGrid = document.getElementById('slots-grid');
  slotsGrid.innerHTML = '';

  SLOT_ORDER.forEach((slot, idx) => {{
    const essences = ESSENCES[slot].filter(e => skills.includes(e.skill));
    const card = document.createElement('div');
    card.className = 'slot-card';
    card.dataset.slot = slot;
    card.style.animationDelay = `${{idx * 0.05}}s`;

    const limit = LIMITS[slot];
    const selCount = selected[slot].length;

    card.innerHTML = `
      <div class="slot-header">
        <div class="slot-title">${{SLOT_ICONS[slot]}} ${{slot}}</div>
        <div class="slot-limit" id="limit-${{slot}}">選択: ${{selCount}}/${{limit}}</div>
      </div>
      <div class="slot-essences" id="essences-${{slot}}">
        ${{essences.length === 0
          ? '<div class="no-essences">該当する精髄なし</div>'
          : `<div class="essence-count">${{essences.length}}件</div>` + essences.map(e => renderEssence(slot, e)).join('')
        }}
      </div>`;
    slotsGrid.appendChild(card);
  }});

  document.getElementById('results').style.display = 'block';
  document.getElementById('results').scrollIntoView({{behavior:'smooth', block:'start'}});
  refreshSelectedPanel();
}}

function renderEssence(slot, e) {{
  const isSelected = selected[slot].some(s => s.name === e.name);
  const atLimit = selected[slot].length >= LIMITS[slot];
  const isDisabled = !isSelected && atLimit;
  return `<div class="essence-card${{isSelected?' selected':''}}${{isDisabled?' disabled':''}}"
    onclick="toggleEssence('${{slot}}', ${{JSON.stringify(JSON.stringify(e))}})">
    <div class="essence-name">
      <span class="check-icon">✓</span>
      ${{e.name}}
    </div>
    <div class="essence-skill">スキル: <span>${{e.skill}}</span></div>
    <div class="essence-desc">${{e.desc}}</div>
  </div>`;
}}

function toggleEssence(slot, eJson) {{
  const e = JSON.parse(eJson);
  const idx = selected[slot].findIndex(s => s.name === e.name);
  if (idx >= 0) {{
    selected[slot].splice(idx, 1);
  }} else {{
    if (selected[slot].length >= LIMITS[slot]) return;
    selected[slot].push(e);
  }}
  // Re-render just this slot's essences
  const skills = getSelectedSkills();
  const essences = ESSENCES[slot].filter(ev => skills.includes(ev.skill));
  const container = document.getElementById(`essences-${{slot}}`);
  const selCount = selected[slot].length;
  const limitEl = document.getElementById(`limit-${{slot}}`);
  limitEl.textContent = `選択: ${{selCount}}/${{LIMITS[slot]}}`;
  limitEl.className = `slot-limit${{selCount >= LIMITS[slot] ? ' at-limit' : ''}}`;
  container.innerHTML = essences.length === 0
    ? '<div class="no-essences">該当する精髄なし</div>'
    : `<div class="essence-count">${{essences.length}}件</div>` + essences.map(e2 => renderEssence(slot, e2)).join('');
  refreshSelectedPanel();
}}

function refreshSelectedPanel() {{
  const panel = document.getElementById('selected-panel');
  const list = document.getElementById('selected-list');
  const allSelected = SLOT_ORDER.flatMap(slot => selected[slot].map(e => ({{...e, slot}})));
  if (allSelected.length === 0) {{
    panel.style.display = 'none';
    return;
  }}
  panel.style.display = 'block';
  list.innerHTML = allSelected.map(e => `
    <div class="selected-tag" onclick="toggleEssence('${{e.slot}}', ${{JSON.stringify(JSON.stringify(e))}})">
      <span class="slot-badge">${{SLOT_ICONS[e.slot]}} ${{e.slot}}</span>
      <strong>${{e.name}}</strong>
      <span class="remove-btn">✕</span>
    </div>`).join('');
  // Scroll to top
  window.scrollTo({{top: 0, behavior: 'smooth'}});
}}

buildSkillGrid();
</script>
</body>
</html>"""

print(HTML)
