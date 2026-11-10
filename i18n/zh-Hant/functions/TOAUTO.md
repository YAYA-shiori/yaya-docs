# TOAUTO
**Category:** 型取得/変換

## Signature
```
TOAUTO( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要轉換的字串 |

## Returns
- 可解讀為整數時：整數值
- 可解讀為實數時（整數轉換失敗時）：實數值
- 無法解讀為上述任一數值時：原樣傳回字串

## Description
嘗試自動轉換字串型別的函式。會優先嘗試轉換為整數，若失敗則嘗試轉換為實數。兩種轉換都失敗時，會原樣傳回字串。

以通用陣列作為引數時，行為未定義。

## Compatibility
- YAYA：TC516-901 以後

## See Also
- TOINT
- TOREAL
- TOSTR
- TOAUTOEX
- CVAUTO
