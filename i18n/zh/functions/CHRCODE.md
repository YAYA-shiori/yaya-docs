# CHRCODE

**Category:** 文字列操作

## Signature

```
CHRCODE( string [ , pos ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | 包含要获取字符编码的字符的文本 |
| pos | （可省略）要获取字符编码的字符位置（从0开始）。省略时为0 |

## Returns

成功时：表示字符编码的数值
失败时：0

返回 UCS-2 字符编码。ASCII 字符（半角英数字）与 ASCII 编码兼容。

## Example

```
CHRCODE('A')      // 65 を返す
CHRCODE('ABC', 2) // 67（文字'C'）を返す
CHRCODE('伺')     // 20282 を返す
```

## Compatibility

- YAYA: 从初版起可用
- AYA: 5.8版及之后

## See Also

- CHR
