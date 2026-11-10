# LINT.GetFuncUsedBy
**Category:** デバッグ

## Signature
```
LINT.GetFuncUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 要分析的函式名稱 |

## Returns
- 成功：指定函式中使用的函式名稱（使用者自訂函式與系統函式）的通用陣列
- 沒有候選項目：空的通用陣列
- 錯誤：-1

## Description
列出指定函式中使用的所有函式名稱（包括使用者自訂函式與系統函式），並以通用陣列傳回。這是用於分析程式碼相依關係或開發時檢查的 Lint 類型工具函式。

傳回的函式名稱會移除重複項目，並依名稱排序。若字串中包含內嵌運算式 `%(式)`，也會包含展開時在內部使用的 `TOSTR`。關於限制的詳細資訊，請參閱 [LINT 系列函式的規格與限制](../other/lint-functions.md)。

## Compatibility
- YAYA: Tc568-1 以上即可使用

## See Also
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
