# TOBINSTR
**Category:** 文字列操作

## Signature
```
TOBINSTR( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 要轉換的整數值 |

## Returns
- 成功：二進位數值字串
- 失敗：VOID

## Description
將整數轉換為二進位數值字串。

## Example
```
_i = 30
_bin = TOBINSTR( _i )
_bin // "11110" (10進数30 = 2進数11110)
```

## Compatibility
- YAYA：自初期版本起
- AYA：5.8 以後
- Tc574-4 / Tc602-5：修正整數最小值（-9223372036854775808）只會顯示為 `-` 的問題

## See Also
- TOHEXSTR
- BINSTRTOI
