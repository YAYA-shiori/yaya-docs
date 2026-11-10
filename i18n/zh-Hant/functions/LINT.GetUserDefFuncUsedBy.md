# LINT.GetUserDefFuncUsedBy
**Category:** デバッグ

## Signature
```
LINT.GetUserDefFuncUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 要分析的函式名稱 |

## Returns
- 成功：指定函式中使用的使用者自訂函式名稱之通用陣列
- 沒有候選項目：空的通用陣列
- 錯誤：-1

## Description
列出指定函式中使用的使用者自訂函式名稱，並以通用陣列傳回。不包含系統函式（若要同時列出系統函式，請使用 `LINT.GetFuncUsedBy`）。

傳回的函式名稱會移除重複項目，並依名稱排序。不包含透過 `EVAL` 等方式從字串呼叫的函式。關於限制的詳細資訊，請參閱 [LINT 系列函式的規格與限制](../other/lint-functions.md)。

## Compatibility
- YAYA: Tc568-1 以上即可使用

## See Also
- LINT.GetFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
