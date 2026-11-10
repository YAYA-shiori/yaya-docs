# LINT.GetLocalVarUsedBy
**Category:** デバッグ

## Signature
```
LINT.GetLocalVarUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 分析對象的函式名稱 |

## Returns
- 成功：指定函式內使用的區域變數名稱之通用陣列。巢狀範圍的進出以 `{` / `}` 表示
- 沒有候選項（也包含只有 `{` `}` 的情況）：空的通用陣列
- 錯誤：-1

## Description
列出指定函式內使用的區域變數名稱，並以通用陣列傳回。指派與讀取兩種使用情況皆為目標。

變數名稱會依使用順序傳回，巢狀範圍（大括號區塊）的進出以 `{` 及 `}` 表示。

Tc574-1 以後，同一個陳述式內作為指派目標的變數（包含 `foreach` 的迴圈變數）會列在該陳述式的最後。這是因為指派會在右側運算式求值後進行。

```
_z = _z + 1      // → _z（読み）, _z（代入）
_a[0] = _b       // → _b, _a
```

不會列出 `case` 語法在內部產生的區域變數（以 `_CaSe_ExPr_PrEfIx_` 開頭的名稱）（Tc574-1 以後）。

傳回值不會區分讀取與指派。限制的詳細資訊請參閱 [LINT 系函式的規格與限制](../other/lint-functions.md)。

## Compatibility
- YAYA：Tc568-1 以後可使用
- Tc574-1：變更為將同一個陳述式內的指派目標列在最後。排除 case 的內部變數

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
