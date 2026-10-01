# お気に入りを書きやすくする

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

いちいちCHR(1)CHR(2)などと書いてられんわボケ！という方向けTips。<br>
**???`_string.dic`の改修が必要です。**

### 方法

ということで、まずは関数追加。

```
LinkMenuConvert
{
    _text = ''
    _data = IARRAY
    for _i = 0 ; _i < _argc ; _i++ {
        _data = (RE_SPLIT(_argv[_i],'[ \t]*\|[ \t]*'),'','') //ダミー
        _text += "%(_data[0])%(CHR(1))%(_data[1])%(CHR(1))%(_data[2])%(CHR(1))%(CHR(2))"
    }
    _text;
}
```

どこでもいいので、まずはこれを追加します。

次に、お気に入りメニューの書き方自体を変更します。<br>
On_sakura.recommendsitesの例を挙げていますが、どれでも構いません。

```
On_sakura.recommendsites
{
    "/
    ごにょごにょ%(CHR(1))http://go.nyo/%(CHR(1))%(CHR(2))/
    "
}
```

元はこうなっています……が、編集が非常に面倒で目がちかちかします。<br>
ということで書き直ししますと、

```
On_sakura.recommendsites
{
   LinkMenuConvert(On_sakura.recommendsites_EX)
}
 
On_sakura.recommendsites_EX : array
{
   'ごにょごにょ  | http://go.nyo/ | '
   'ほげほげ      | http://ho.ge/  | '
   "ふがふが      | http://fu.ga/  | "
}
```

 | が区切りです。<br>
半角スペースやタブをその左右に適当に入れて、適当に見やすくして構いません。

なんたら`_EX`は適当な名前で構いませんが : array とつけるのを忘れないでください。

サンプルは ' ' で囲んでいますが、別に " " でも全く問題ありません。<br>
変数等を利用したい場合や、サイト名に ' が含まれて回避したい場合は " " を使ってください。

Emily/Phase4などで利用しています。<br>
わからない場合はそちらも参考にしてください。

―― ぽな@ばぐとら
