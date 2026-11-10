# 简易数组→通用数组的转换

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### 最新版中的做法

最新版新增了一个名为 SPLIT 的函数。<br>
如果是无需使用正则表达式的简单拆分，可以使用这个函数。

```
i = SPLIT("Sakura,Seriko,Mayura,Naru", ",")
```

这个函数也可以用于简易数组转换为通用数组以外的场景。<br>
详情请参阅[手册](../INDEX.md)。

### 以前的备忘

```
簡易配列→汎用配列の変換はRE_SPLITで可能です。
（…ってわたしが回答してしまうのは皆さんの楽しみを奪ってしまうようで些か心苦しいですけど。）

i = RE_SPLIT("Sakura,Seriko,Mayura,Naru", ",")
(:::looseleafより）
```

具体用法示例（制作中）
