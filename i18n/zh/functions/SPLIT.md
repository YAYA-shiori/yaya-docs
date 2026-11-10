# SPLIT
**Category:** 文字列操作

## Signature
```
SPLIT(src, delim [, max])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 要分割的字符串（建议将数值变量通过 TOSTR 转换后再传入） |
| delim | 分隔字符串 |
| max | 最大分割数（省略或设为 0 时完全分割） |

## Returns
- 成功时：包含分割后字符串元素的通用数组
- 失败时：空数组

## Description
分割字符串并以通用数组的形式返回。由于不进行正则表达式处理，因此比 RE_SPLIT 更快。

指定 `max` 时，会在达到该数量后停止分割，并将剩余部分合并到最后一个元素中。

## Example
```
_array = SPLIT("A//B//C//D//E", "//", 3)
// 結果: ("A", "B", "C//D//E")
```

## Compatibility
- YAYA：从初始版本起可用
- AYA：5.8 及之后

## See Also
- RE_SPLIT（使用正则表达式进行分割）
