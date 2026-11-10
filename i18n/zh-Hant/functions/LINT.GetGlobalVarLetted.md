# LINT.GetGlobalVarLetted
**Category:** デバッグ

## Signature
```
LINT.GetGlobalVarLetted(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 要分析的函式名稱 |

## Returns
- 成功：指定函式內被指派的全域變數名稱之通用陣列
- 沒有候選項目：空的通用陣列
- 錯誤：-1

## Description
列出指定函式內有對全域變數進行指派（let）的位置，並以通用陣列傳回。只讀取變數的位置不會列出。若要同時列出讀取的位置，請使用 `LINT.GetGlobalVarUsedBy`。

傳回的變數名稱會移除重複項目，並依名稱排序。

以下情況也會列為指派。
- 複合指派（例如 `+=`、`-=`）以及 `++`、`--`
- 對陣列元素的指派（`G_a[0] = 1` 會列出 `G_a`）（Tc574-1 以上）
- `foreach _list ; G_v` 的迴圈變數 `G_v`（Tc574-1 以上）
- `foreach _list ; G_k, G_v` 的兩個迴圈變數 `G_k`、`G_v`（Tc600-3 以上）

關於限制的詳細資訊，請參閱 [LINT 系列函式的規格與限制](../other/lint-functions.md)。

## Compatibility
- YAYA: Tc568-1 以上即可使用
- Tc574-1: 修改為列出對陣列元素的指派以及 foreach 的迴圈變數
- Tc600-3: 修改為列出雙變數 foreach 的兩個迴圈變數

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
