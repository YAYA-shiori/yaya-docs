# ランダムトークをさとりっぽく

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

## ランダムトークをさとりっぽく簡単に書いてみよう＠AYA5

これ書いたの＠ちに。

辞書：[satori_for_aya.dic](http://mistnar.hp.infoseek.co.jp/ukagaka/ayav_text/satori_for_aya.dic)

<span style="color:Red">※ここでは、OnChoiceSelectの選択肢をいきなり独立した関数で書いています。[選択肢をいきなり独立した関数で書く](independent-choice-function.md)を参照してください。</span>

### 分かりにくい説明

AYA辞書内で里々風スクリプトものを使うことが出来ます。<br>
しかしながら、基本的には当然AYAなので、その辺は勘違いしないようにー。

### 使い方

aya_aitalk.dic内の

```
OnAiTalk
```

部分の

```
RandomTalk
```

を

```
OnAiTalk.Satori
```

と書き換えるなり、書き足すなりで動きます。<br>
トーク類は、この辞書の

```
RandomTalk.Satori
```

内に書いてってください。<br>
里々風スクリプトはこの関数内のみ有効です。

### 対応タグ

```
（サーフィス番号）
：
＠
＞
＿
```

です。ちなみに＠と＞は全く同じ処理をしていますので、どっちでもいいです。<br>
（＿あそぶ）のように書くと、`\_q[あそぶ,＿あそぶ]`と同等になります。

そのほかの例は、下の"RandomTalk.Satori"見てー。

### 玉で試したいっ

```
GET SHIORI/3.0
ID: OnAiTalk.Satori
Sender: CallAIMist
SecurityLevel: local
Charset: Shift_JIS
```

以上、コピペしる。

### 注意

バグ潰しなんてやってません。<br>
動かなかったら、ごめん。（特に＿タグ試してない(ﾟ∀ﾟ)
