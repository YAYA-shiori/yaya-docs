# 從文字檔案建立通用陣列

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

例如

```
だいふく
おさしみ
とうふ
ラーメン
```

假設在 `\master\words` 中有一個名為 food.txt 的檔案，內容是以換行分隔的單字（文字編碼為 Shift-JIS）。

若要建立一個名為 food 的通用陣列來儲存這些元素

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

這樣一來，`food[0]` 會是「だいふく」，`food[1]` 會是「おさしみ」……。
