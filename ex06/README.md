# 第6回
## ブロックを崩せ（ex06/block.py）
### ゲーム概要
- ex06/blockn.pyを実行すると，650x1000の黒い背景のスクリーンが描画され，90個のブロックが表示され棒とボールを使いブロックを崩すゲーム
- ボールが三回床と接触するとゲームオーバーで終了する
- ボールと棒を当てることで反射する
### 操作方法
- 矢印キーで棒を左右に移動する
### 追加機能
- ブロックにボールが当たるとscoreが10増加する
- キー(r)を押すことでリスタートできる
- 床にボールが当たるとボールが消え残機が1減る
### TODO(今回できなかった)
- ブロックにボールが二回当たったら消えるようにする
- 残機が減少後ボールを消してキー(s)を押すとボールが出るようにする
- ブロックにボールが当たっても反応せずにscoreが増加しない
### 参考サイト
- Pythonスクリプト【Pygameでスプライトを使おう https://mulberrytassel.com/python-practice-pygame-6/
- Pygameのドキュメント（日本語訳） http://westplain.sakuraweb.com/translate/pygame/
- 【Pygame】ブロック崩しの作り方（効果音付き) https://algorithm.joho.info/programming/python/pygame-blockout/