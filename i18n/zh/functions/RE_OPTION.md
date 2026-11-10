# RE_OPTION
**Category:** 正規表現

## Signature
```
RE_OPTION( オプション文字列 )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| オプション文字列 | 要设置的 Perl 兼容正则表达式选项字符串（i、s、m、x）。省略时返回当前设置 |

## Returns
表示当前有效选项的字符串（i、s、m、x 的组合）

## Description
设置 Perl 兼容的正则表达式选项。

支持的选项:
- **i**: 匹配时不区分大小写
- **m**: 将输入视为多行
- **s**: 使通配符（.）也能匹配换行符
- **x**: 忽略正则表达式模式中的注释（#）和空白

默认不启用任何选项（`RE_OPTION("")` 也会恢复到相同状态）。不带参数调用时，会以字符串形式返回当前选项。

也可以在模式中指定选项（例如 `(?i)abc`）。详情请参阅[正则表达式](../grammar/14-regular-expressions.md#オプション)。

## Compatibility
- YAYA: Tc534-1 及以上版本支持

## See Also
- RE_MATCH
- RE_SEARCH
- RE_REPLACE
- [正则表达式](../grammar/14-regular-expressions.md)
