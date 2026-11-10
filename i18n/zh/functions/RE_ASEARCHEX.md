# RE_ASEARCHEX
**Category:** 正規表現

## Signature
```
RE_ASEARCHEX( key , array )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key | 要搜索的正则表达式模式 |
| array | 要搜索的通用数组（不支持简易数组） |

## Returns
列出匹配元素序号的通用数组（从 0 开始）。没有匹配元素时返回空数组。

**注意：**不能使用 `RE_GETSTR`、`RE_GETPOS`、`RE_GETLEN`。

## Description
在通用数组中搜索与指定正则表达式有“部分”匹配的值，并搜索**所有**匹配项。

## Example
```
_tea = ("鉄観音", "烏龍", "やぶきた", "烏龍", "ジャスミン")
ipod = RE_ASEARCHEX("^烏", _tea)
// ipod は (1,3) になる（"烏"で始まる要素のインデックス）
```

## Compatibility
- YAYA：从初始版本起即可使用
- AYA：从 5.8 版起可使用
- Tc606-6：正则表达式引擎改为 uka_regexp（语法接近 PCRE2）。可以通过变量或函数解析模式中的子程序调用（[正则表达式](../grammar/14-regular-expressions.md)）

## See Also
- ASEARCHEX
- RE_ASEARCH
- [正则表达式](../grammar/14-regular-expressions.md)
