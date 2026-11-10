# RE_ASEARCH
**Category:** 正規表現

## Signature
```
RE_ASEARCH(key, array)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key | 要搜尋的正規表示式模式 |
| array | 搜尋目標通用陣列（不支援簡易陣列） |

## Returns
- 第一個符合項目的索引（從 0 開始）
- 沒有符合項目時：-1

## Description
從通用陣列中搜尋「部分符合」指定正規表示式的值，並只傳回第一個找到的項目。

**注意：**無法使用 `RE_GETSTR`・`RE_GETPOS`・`RE_GETLEN`。若要取得所有符合項目，請使用 `RE_ASEARCHEX`。

## Example
```
_array = ('さくら','まゆら','ねここ')
RE_ASEARCH('^ま', _array) // Returns: 1
```
搜尋以「ま」開頭的項目，並找到索引 1（第 2 個項目）。

## Compatibility
- YAYA：Tc539-1 版起即可使用
- Tc606-6：正規表示式引擎改為 uka_regexp（語法近似 PCRE2）。可以透過變數或函式解析模式中的子程序呼叫（[正規表示式](../grammar/14-regular-expressions.md)）

## See Also
- ASEARCH
- RE_ASEARCHEX
- [正規表示式](../grammar/14-regular-expressions.md)
