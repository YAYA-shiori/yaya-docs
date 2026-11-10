# TOINT
**Category:** 型取得/変換

## Signature
```
TOINT( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要轉換的字串或實數 |

## Returns
- 成功：轉換後的整數值
- 失敗：0

## Description
將字串或實數轉換為整數。小數點以下的部分會直接捨去。

在 Tc542-4 以前的版本中，行為相當於 FLOOR()（這是錯誤行為）；Tc542-4 以後的版本則與其他語言相同，會直接捨去小數點以下的部分。

## Example
```
_i = '100'       // 文字列を代入
_j = _i + 1
// "1001" (文字列の連結になってしまう)

_i = '100'
_j = TOINT( _i ) + 1
// 101 (整数に変換してから加算)

_i = 1.1
_j = TOINT( _i )
// 1

_i = -1.1
_j = TOINT( _i )
// -1 (Tc542-4以降の動作)
```

## Compatibility
- YAYA：自初期版本起
- AYA：5.8 以後
- Tc542-4 以後：變更負數小數的捨去行為
- Tc574-4 / Tc602-6：修正數字後接著 `a`（`A`）的字串會將 `a` 當作 10 這個位數讀取，導致 `TOINT('1a')` 得到 20 的問題（現在會得到 1）

## See Also
- TOSTR
- TOREAL
