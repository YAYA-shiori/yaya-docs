# HEXSTRTOI
**Category:** 文字列操作

## Signature
```
HEXSTRTOI( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要轉換的十六進位數值字串 |

## Returns
- 成功時：轉換後的數值（整數）
- 失敗時：0

## Description
將十六進位數值字串轉換為整數。開頭有 `0x` 前綴時會予以忽略。

## Example
```
_hex = '1E'
_i = HEXSTRTOI( _hex )
// _i は 30（16進数 1E = 10進数 30）
```

## Compatibility
- YAYA：從初期版本起即可使用
  - Tc547-1 以後：可處理開頭的 `0x` 前綴
- AYA：5.8 以後

## See Also
- BINSTRTOI
- TOHEXSTR
