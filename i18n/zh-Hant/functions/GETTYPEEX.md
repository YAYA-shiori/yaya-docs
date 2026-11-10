# GETTYPEEX
**Category:** 型取得/変換

## Signature
```
GETTYPEEX( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 要檢查型別的變數名稱（以字串傳入） |

## Returns
- 0：內部錯誤（失敗）
- 1：整數
- 2：實數
- 3：字串
- 4：通用陣列
- 5：雜湊（Tc600-3 以後）

## Description
取得指定變數的資料型別。與 `GETTYPE` 的主要差異在於，引數不是變數本身，而是以**字串形式傳入變數名稱**。

此函式也會正確傳回元素數為 1 的通用陣列型別，因此在 `GETTYPE` 因向後相容行為而無法正確判定時，可使用此函式。

## Compatibility
- YAYA：Tc537-3 以後
- Tc600-3：雜湊型別改為傳回 5

## See Also
- GETTYPE
- GETVARLIST
