# 第6回
## ブロックを崩せ（ex06/block.py）
### ゲーム概要
- ex06/blockn.pyを実行すると，650x1000の黒い背景のスクリーンが描画され,棒とボールを使いブロックを崩すゲーム
- 80個のブロックが表示(澤井)
- 残機が3で、ボールが三回床と接触するとゲームオーバーで終了する
- ボールと棒を当てることで反射する
### 操作方法
- 矢印キーで棒を左右に移動する
### 追加機能
- ブロックにボールが当たるとscoreが一回目は10、２回目は20増加する(澤井,下田)
- 残機が減少後ボールを消してキー(s)を押すとボールが出る(近藤)
- キー(s)を押すことでスタート(近藤,村田)
- キー(r)を押すことでリスタート(近藤,村田)
- キー(q)を押すことでゲーム終了(近藤,村田)
- 床にボールが当たるとボールが消え残機が1減る(近藤,山口)
- ブロックにボールが二回当たったら消える(澤井,小嶋)
### TODO(今回できなかった)
### 参考サイト
- Pythonスクリプト【Pygameでスプライトを使おう https://mulberrytassel.com/python-practice-pygame-6/
- Pygameのドキュメント（日本語訳） http://westplain.sakuraweb.com/translate/pygame/
- 【Pygame】ブロック崩しの作り方（効果音付き) https://algorithm.joho.info/programming/python/pygame-blockout/
- 【Python】1時間で作る「ブロックくずし」／初心者プログラミング学習。 https://kusakarism.info/2021/05/breakout/