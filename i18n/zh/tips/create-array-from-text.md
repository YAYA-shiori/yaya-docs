# 从文本文件创建通用数组

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) 转载

例如

```
だいふく
おさしみ
とうふ
ラーメン
```

假设在`\master\words`中有一个名为food.txt的文件，其中单词以换行符分隔（字符编码为Shift-JIS）。

如果想创建一个存储这些元素的名为food的通用数组

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

这样，`food[0]`就是だいふく，`food[1]`就是おさしみ……。
