# 簡易配列→汎用配列の変換

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

### 最新版でのやり方

最新版では、SPLITという関数が追加されました。<br>
正規表現を利用する必要のない簡単な分割であればこの関数で行えます。

```
i = SPLIT("Sakura,Seriko,Mayura,Naru", ",")
```

これは、簡易配列から汎用配列の変換以外でも利用できます。<br>
詳しくは[マニュアル](../INDEX.md)を見てください。

### 以前のメモ

```
簡易配列→汎用配列の変換はRE_SPLITで可能です。
（…ってわたしが回答してしまうのは皆さんの楽しみを奪ってしまうようで些か心苦しいですけど。）

i = RE_SPLIT("Sakura,Seriko,Mayura,Naru", ",")
(:::looseleafより）
```

使い方の具体例（作成中）
