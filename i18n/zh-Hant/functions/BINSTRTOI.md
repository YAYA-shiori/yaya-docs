# BINSTRTOI

**Category:** 文字列操作

## Signature

```
BINSTRTOI(string)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | 要轉換的二進位字串 |

## Returns

成功時：轉換後的數值
失敗時：0

## Description

將表示二進位數的字串轉換為整數。

## Example

```
_bin = '11110'
_i = BINSTRTOI(_bin)
_i // 30 を出力（2進数 11110 = 10進数 30）
```

## Compatibility

- YAYA：從初始版本起即可使用
- AYA：版本 5.8 以後

## See Also

- HEXSTRTOI
- TOBINSTR
