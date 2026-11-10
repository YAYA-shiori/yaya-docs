# CVAUTO

**Category:** 型取得/変換

## Signature

```
CVAUTO(var [, strict_convert])
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| var | 要转换的变量 |
| strict_convert | （可省略，默认值：0）传入非 0 值时，仅当转换结果再转换为字符串后与原字符串一致，才进行转换（行为与 [CVAUTOEX](CVAUTOEX.md) 相同。Tc571-2 及以上版本） |

## Returns

无返回值（直接转换变量）

如果指定的变量中存储的是符合字符串格式的字符串，则将其转换为整数或实数（以可解析的类型为准）并重新存储。如果两者都无法解析，则保持为字符串，不进行转换。传入通用数组变量时的行为未定义。

## Example

```
_val = '3.14159'
CVAUTO(_val)
GETTYPE(_val) // 2 を返す（実数型であることを示す）
```

## Compatibility

- YAYA: TC516-901 及以上版本
- Tc571-2：新增 `strict_convert`

## See Also

- CVREAL
- CVINT
- CVSTR
- CVAUTOEX
- TOAUTO
