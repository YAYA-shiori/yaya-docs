# 予約語

## 概要

YAYAシステムで予約されている名前。ユーザー定義の変数名や関数名に使用できない。

## システム関数

[システム関数一覧](../system/system-functions-index.md) に掲載されているすべての関数名は予約済み。

> 大文字＋アンダースコアのみで構成される名前は将来の互換性のためにも使わないほうが良い。

## 制御構造キーワード

以下の制御フロー用語は予約済み：

```
if  elseif  else  case  when  others  switch
while  for  break  continue  return  foreach
void  parallel
```

`void` と `parallel` は関数の出力を制御するキーワード（[配列](05-arrays.md#並列出力)）。

## 演算子

変数名・関数名に使用できない予約済み演算子記号：

```
( ) [ ] ! ++ -- * / % + - & == != <= >= < > _in_ !_in_ && ||
= := += -= *= /= %= +:= -:= *:= /:= %:= ,=
```
