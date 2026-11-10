# CVAUTOEX

**Category:** 型取得/変換

## Signature

```
CVAUTOEX(var)
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| var | 要转换的变量 |

## Returns

无返回值（直接转换变量）

如果字符串格式的文本可以解析为整数或实数，则进行转换；否则保持为字符串。与 CVAUTO 的区别在于，只有「转换为字符串后的结果与原字符串一致」时才会进行转换。先尝试转换为整数，再尝试转换为实数。传入通用数组变量时的行为未定义。

## Example

```
// 文字列のまま残る例
_val = '3.14'
CVAUTOEX(_val)
GETTYPE(_val)  // "3" を出力（文字列型）

// 実数に変換される例
_val = '3.140000'
CVAUTOEX(_val)
GETTYPE(_val)  // "2" を出力（実数型）
```

## Compatibility

- YAYA: TC571-3 及以上版本

## See Also

- CVAUTO
- CVINT
- CVREAL
- CVSTR
- TOAUTO
