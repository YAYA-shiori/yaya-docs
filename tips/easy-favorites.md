# お気に入りを書きやすくする

## 概要

お気に入りメニューのエントリを記述する際、`CHR(1)` や `CHR(2)` などの制御文字を直接書く必要があり冗長になる。ヘルパー関数を使ってより読みやすい記法で書けるようにするTips。

## コア関数

```
LinkMenuConvert
{
    _text = ''
    _data = IARRAY
    for _i = 0 ; _i < _argc ; _i++ {
        _data = (RE_SPLIT(_argv[_i],'\[ \t\]*\|\[ \t\]*'),'','')
        _text += "%(_data[0])%(CHR(1))%(_data[1])%(CHR(1))%(_data[2])%(CHR(1))%(CHR(2))"
    }
    _text;
}
```

## 使い方

制御文字を直接書く代わりに、パイプ文字 `|` で区切った読みやすい形式で定義する：

```
On_sakura.recommendsites_EX : array
{
   'Site Name  | http://url.com/ | '
   'Another    | http://other/   | '
}
```

その後、`LinkMenuConvert(On_sakura.recommendsites_EX)` として呼び出す。

パイプ文字（`|`）がフィールドの区切りとなり、前後の空白は無視される。

## 注意

このソリューションを実装するには `???_string.dic` ファイルへの修正が必要。

## 関連項目

- [IARRAY](../functions/IARRAY.md)
- [RE_SPLIT](../functions/RE_SPLIT.md)
- [CHR](../functions/CHR.md)
