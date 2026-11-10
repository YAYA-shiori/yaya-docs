# RE_ASEARCHEX
**Category:** 正規表現

## Signature
```
RE_ASEARCHEX( key , array )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key | 要搜尋的正規表示式模式 |
| array | 搜尋目標通用陣列（不支援簡易陣列） |

## Returns
列出符合項目索引的通用陣列（從 0 開始）。沒有符合項目時，會傳回空陣列。

**注意：**無法使用 `RE_GETSTR`・`RE_GETPOS`・`RE_GETLEN`。

## Description
從通用陣列中搜尋「部分符合」指定正規表示式的**所有**值。

## Example
```
_tea = ("鉄観音", "烏龍", "やぶきた", "烏龍", "ジャスミン")
ipod = RE_ASEARCHEX("^烏", _tea)
// ipod は (1,3) になる（"烏"で始まる要素のインデックス）
```

## Compatibility
- YAYA：從初始版本起即可使用
- AYA：5.8 版及之後的版本即可使用
- Tc606-6：正規表示式引擎改為 uka_regexp（語法近似 PCRE2）。可以透過變數或函式解析模式中的子程序呼叫（[正規表示式](../grammar/14-regular-expressions.md)）

## See Also
- ASEARCHEX
- RE_ASEARCH
- [正規表示式](../grammar/14-regular-expressions.md)
