# CVINT

**Category:** 型取得/変換

## Signature

```
CVINT(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 要轉換為整數型的變數 |

## Returns

沒有傳回值（直接轉換變數）

將存有整數形式字串的變數轉換為實際的整數型。小數部分會捨去。

## Example

```
_val = '583'
CVINT(_val)
GETTYPE(_val) // 1 を返す（整数型）

_val = '583.12'
CVINT(_val)
GETTYPE(_val) // 1 を返す（整数型）
_val // 583 を返す（小数部分は除去される）
```

## Compatibility

- YAYA：從初版起即可使用
- AYA：5.8 版以後
- Tc574-4 / Tc602-6：修正了數字後接 `a`（`A`）的字串會將 `a` 視為 10 這個位數來讀取，導致 `'1a'` 變成 20 的問題（現在會變成 1）

## See Also

- CVREAL
- CVSTR
- CVAUTO
