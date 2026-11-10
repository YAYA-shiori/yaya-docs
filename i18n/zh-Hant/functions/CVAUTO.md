# CVAUTO

**Category:** 型取得/変換

## Signature

```
CVAUTO(var [, strict_convert])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 要轉換的變數 |
| strict_convert | （可省略，預設值：0）傳入非 0 值時，只有在轉換結果再轉成字串後與原字串一致的情況下才會轉換（行為與 [CVAUTOEX](CVAUTOEX.md) 相同。Tc571-2 以後） |

## Returns

沒有傳回值（直接轉換變數）

指定一個存有字串形式內容的變數作為引數時，若能解讀為整數，就轉換為整數；若能解讀為實數，就轉換為實數並重新存入。若兩者皆無法解讀，則維持字串，不進行轉換。傳入通用陣列變數時的行為未定義。

## Example

```
_val = '3.14159'
CVAUTO(_val)
GETTYPE(_val) // 2 を返す（実数型であることを示す）
```

## Compatibility

- YAYA：TC516-901 以後
- Tc571-2：新增 `strict_convert`

## See Also

- CVREAL
- CVINT
- CVSTR
- CVAUTOEX
- TOAUTO
