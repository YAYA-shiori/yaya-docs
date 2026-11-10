# Create a Generic Array from a Text File

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

For example,

```
だいふく
おさしみ
とうふ
ラーメン
```

Suppose there is a file named food.txt in `\master\words` whose words are separated by line breaks (the character encoding is Shift-JIS).

If you want to create a generic array named food containing these elements,

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

This makes `food[0]` contain the first item, `food[1]` the second item, and so on.
