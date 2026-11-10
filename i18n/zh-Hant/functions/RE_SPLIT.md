# RE_SPLIT
**Category:** 正規表現

## Signature
```
RE_SPLIT( string , regexp [, max] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要分割的字串 |
| regexp | 用於分割的正規表示式模式 |
| max | 最大分割數（省略或指定 0 時會全部分割） |

## Returns
- 成功: 儲存分割後字串的通用陣列
- 失敗: 空的通用陣列

## Description
使用正規表示式模式分割要處理的字串，並以通用陣列傳回結果。

指定 `max` 時，會在分割到該數量後停止，並將剩餘部分合併到最後一個元素中（`RE_SPLIT('a,b,c,d', ',', 2)` 會得到 `a` 和 `b,c,d`）。

可使用 RE_GETSTR、RE_GETPOS、RE_GETLEN 取得分割結果的詳細資訊。

## Compatibility
- YAYA: 自初始版本起支援（max 參數自 Tc536-1 起支援）
- Tc606-6: 將正規表示式引擎變更為 uka_regexp（語法接近 PCRE2）。可透過變數或函式解析模式中的子程式呼叫（[正規表示式](../grammar/14-regular-expressions.md)）

## See Also
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [正規表示式](../grammar/14-regular-expressions.md)
