# Converting a Simple Array to a Generic Array

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### How to do it in the latest version

The SPLIT function was added in the latest version.<br>
You can use this function to split strings simply when you do not need regular expressions.

```
i = SPLIT("Sakura,Seriko,Mayura,Naru", ",")
```

This function can also be used for purposes other than converting a simple array to a generic array.<br>
See the [manual](../INDEX.md) for details.

### Earlier notes

```
簡易配列→汎用配列の変換はRE_SPLITで可能です。
（…ってわたしが回答してしまうのは皆さんの楽しみを奪ってしまうようで些か心苦しいですけど。）

i = RE_SPLIT("Sakura,Seriko,Mayura,Naru", ",")
(:::looseleafより）
```

Specific usage examples (in progress)
