# テキストファイルから汎用配列を作成

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

たとえば

```
だいふく
おさしみ
とうふ
ラーメン
```

と単語が改行で区切られたfood.txtというファイル(文字コードはShift-JIS)が`\master\words`にあるとする。

これらの要素を格納したfoodという汎用配列を作りたい場合

```
 //テキストファイルから汎用配列を作る処理
 FCHARSET("Shift-JIS")//単語ファイルの文字コードを指定。UTF-8ならここを変える
 _flag = FOPEN("words\food.txt", "r")
 food = IARRAY//空の配列の作成
 while 1 {
   _word = FREAD("words\food.txt")
   if (_word == -1){
     break
   }
   food = (food,_word)
 }
 FCLOSE("words\food.txt")
```

これで`food[0]`がだいふく、`food[1]`がおさしみ...となる。
