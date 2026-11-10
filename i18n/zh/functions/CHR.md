# CHR

**Category:** 文字列操作

## Signature

```
CHR( val [, val ... ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | UCS-2 字符代码值（数值）。可以指定多个 |

## Returns

成功时：转换后的字符或字符串（长度等于参数数量的字符串）
失败时：VOID

## Description

以数值指定 UCS-2 代码时，返回对应的 1 个字符组成的字符串。可以指定多个数值，此时返回长度等于参数数量的字符串（传入通用数组时会返回字符串）。UCS-2 代码在 ASCII 范围内与 ASCII 代码兼容。

## Example

```
CHR(65)      // "A" を返す
CHR(20282)   // "伺" を返す
```

## Compatibility

- YAYA：从初版起可用
- AYA：5.8 版及更高版本可用

## See Also

- CHRCODE
