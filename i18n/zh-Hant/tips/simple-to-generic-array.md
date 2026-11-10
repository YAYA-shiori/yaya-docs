# 簡易陣列→通用陣列的轉換

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### 最新版本的做法

最新版新增了 SPLIT 函式。<br>
若是無須使用正規表示式的簡單分割，可以使用此函式。

```
i = SPLIT("Sakura,Seriko,Mayura,Naru", ",")
```

除了將簡易陣列轉換為通用陣列之外，也可以用於其他用途。<br>
詳情請參閱[手冊](../INDEX.md)。

### 之前的筆記

```
簡易配列→汎用配列の変換はRE_SPLITで可能です。
（…ってわたしが回答してしまうのは皆さんの楽しみを奪ってしまうようで些か心苦しいですけど。）

i = RE_SPLIT("Sakura,Seriko,Mayura,Naru", ",")
(:::looseleafより）
```

使用方式的具體範例（製作中）
