# BINSTRTOI

**Category:** 文字列操作
**Source:** マニュアル/関数/BINSTRTOI

## Signature

```
BINSTRTOI(string)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | 変換する2進数の文字列 |

## Returns

成功時：変換後の数値
失敗時：0

## Example

```
_bin = '11110'
_i = BINSTRTOI(_bin)
_i // 30 を出力（2進数 11110 = 10進数 30）
```

## Compatibility

- YAYA: 初期リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- HEXSTRTOI
- TOBINSTR
