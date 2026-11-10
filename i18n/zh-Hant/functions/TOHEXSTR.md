# TOHEXSTR
**Category:** 文字列操作

## Signature
```
TOHEXSTR( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 要轉換的整數值 |

## Returns
- 成功：十六進位數值字串
- 失敗：VOID

## Description
將整數轉換為十六進位數值字串。

## Example
```
_i = 30
_hex = TOHEXSTR( _i )
_hex // "1E" (10進数30 = 16進数1E)
```

## Compatibility
- YAYA：自初期版本起
- AYA：5.8 以後
- Tc574-4 / Tc602-5：修正整數最小值（-9223372036854775808）只會顯示為 `-` 的問題

## See Also
- TOBINSTR
- HEXSTRTOI
