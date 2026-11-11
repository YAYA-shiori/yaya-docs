# STRFORM
**Category:** 文字列操作

## Signature
```
STRFORM(format [, arg ...])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| format | 格式字符串 |
| arg | 要嵌入格式字符串的参数（可指定多个） |

## Returns
- 成功时：格式化后的字符串
- 失败时：行为未定义

## Description
返回相当于 C 语言 sprintf 的格式化字符串。

格式说明符使用 `$` 而不是 `%` 作为前缀（例如：`$04d`、`$s`）。每个格式说明符展开的字符串最长为 1024 个字符。

除了通过返回值获取结果，以及格式说明符的前缀字符为 `$` 以外，使用方法与 sprintf 完全相同。

## Example
与 sprintf 的比较。

```
// C言語
int year = 1941;
char *warname = "太平洋";
sprintf(str, "%04d年　%s戦争勃発。", year, warname);

// 文
year = 1941
warname = "太平洋"
str = STRFORM("$04d年　$s戦争勃発。", year, warname)
// 結果: "1941年　太平洋戦争勃発。"
```

## Compatibility
- YAYA：从初始版本起可用
- AYA：5.8 及以上版本
