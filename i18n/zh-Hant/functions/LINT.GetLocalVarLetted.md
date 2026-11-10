# LINT.GetLocalVarLetted
**Category:** デバッグ

## Signature
```
LINT.GetLocalVarLetted(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 要分析的函式名稱 |

## Returns
- 成功：指定函式內被指派的區域變數名稱之通用陣列。以 `{` / `}` 表示進出巢狀範圍
- 沒有候選項目（包括只有 `{` `}` 的情況）：空的通用陣列
- 錯誤：-1

## Description
列出指定函式內有對區域變數進行指派（let）的位置，並以通用陣列傳回。只讀取變數的位置不會列出。若要同時列出指派與讀取的位置，請使用 `LINT.GetLocalVarUsedBy`。

變數名稱會依指派發生的順序傳回，並以 `{` 和 `}` 表示進出巢狀範圍（大括號區塊）。

以下情況也會列為指派。
- 複合指派（例如 `+=`、`-=`）以及 `++`、`--`
- 對陣列元素的指派（`_a[0] = 1` 會列出 `_a`）（Tc574-1 以上）
- `foreach _list ; _v` 的迴圈變數 `_v`（Tc574-1 以上）
- `foreach _list ; _k, _v` 的兩個迴圈變數 `_k`、`_v`（Tc600-3 以上）

不會列出 `case` 語法在內部產生的區域變數（以 `_CaSe_ExPr_PrEfIx_` 開頭的名稱）（Tc574-1 以上）。

關於限制的詳細資訊，請參閱 [LINT 系列函式的規格與限制](../other/lint-functions.md)。

## Compatibility
- YAYA: Tc568-1 以上即可使用
- Tc574-1: 修改為列出對陣列元素的指派以及 foreach 的迴圈變數，並排除 case 的內部變數
- Tc600-3: 修改為列出雙變數 foreach 的兩個迴圈變數

## See Also
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetGlobalVarUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetFuncUsedBy
- LINT.GetVarRefs
