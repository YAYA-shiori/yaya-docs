# RE_ASEARCH
**Category:** 正規表現

## Signature
```
RE_ASEARCH(key, array)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key | 要搜索的正则表达式模式 |
| array | 要搜索的通用数组（不支持简易数组） |

## Returns
- 第一个匹配元素的索引（从 0 开始）
- 没有匹配元素时：-1

## Description
在通用数组中搜索与指定正则表达式有“部分”匹配的值，只返回第一个找到的值。

**注意：**不能使用 `RE_GETSTR`、`RE_GETPOS`、`RE_GETLEN`。要获取所有匹配项，请使用 `RE_ASEARCHEX`。

## Example
```
_array = ('さくら','まゆら','ねここ')
RE_ASEARCH('^ま', _array) // Returns: 1
```
搜索以“ま”开头的元素，找到索引 1（第 2 个元素）。

## Compatibility
- YAYA：从 Tc539-1 版起可使用
- Tc606-6：正则表达式引擎改为 uka_regexp（语法接近 PCRE2）。可以通过变量或函数解析模式中的子程序调用（[正则表达式](../grammar/14-regular-expressions.md)）

## See Also
- ASEARCH
- RE_ASEARCHEX
- [正则表达式](../grammar/14-regular-expressions.md)
