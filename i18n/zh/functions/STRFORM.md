# STRFORM
**Category:** 文字列操作

## Signature
```
STRFORM(format [, arg ...])
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| format | 格式字符串 |
| arg | 要插入格式字符串中的参数（可指定多个） |

## Returns
- 成功时：格式化后的字符串
- 失败时：行为未定义

## Description
返回相当于 C 语言 sprintf 的格式化字符串。

格式说明符使用 `$` 作为前缀，而不是 `%`（例如 `$04d`、`$s`）。每个格式说明符展开后的字符串最长为 1024 个字符。

## Example
```
year = 1941
warname = "太平洋"
str = STRFORM("$04d年　$s戦争勃発。", year, warname)
// 結果: "1941年　太平洋戦争勃発。"
```

## Compatibility
- YAYA：从初始版本起可用
- AYA：5.8 及之后
