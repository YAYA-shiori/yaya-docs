# SUBSTR
**Category:** 文字列操作

## Signature
```
SUBSTR(src, pos, len)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 源字符串 |
| pos | 起始位置（从 0 开始。负值表示从末尾开始的偏移量） |
| len | 要获取的字符数 |

## Returns
- 成功时：获取的子字符串
- pos 超出字符串长度时：空字符串 `""`
- pos + len 超出字符串末尾时：获取至末尾
- 出错时：VOID

## Description
从字符串中提取子字符串。将负值指定给 `pos` 时，会将其视为从字符串末尾开始的偏移量（例如：-2 表示从末尾开始第 2 个字符）。

## Example
```
SUBSTR("HOGE", -2, 1)  // 結果: "G"（末尾から2番目の文字）
```

## Compatibility
- YAYA：从早期版本起可用
- AYA：5.8 及更高版本（但不支持负数 pos 值）

## See Also
- STRSTR（子字符串搜索）
- STRLEN（获取字符串长度）
