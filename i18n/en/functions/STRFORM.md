# STRFORM
**Category:** 文字列操作

## Signature
```
STRFORM(format [, arg ...])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| format | Format string |
| arg | Arguments to insert into the format string (multiple arguments can be specified) |

## Returns
- On success: Formatted string
- On failure: Behavior is undefined

## Description
Returns a formatted string equivalent to one produced by C's sprintf.

Format specifiers use `$` as a prefix instead of `%` (for example, `$04d`, `$s`). The string expanded by each format specifier is at most 1024 characters long.

Except for returning the result as the return value and using `$` as the format specifier prefix, it works just like sprintf.

## Example
Comparison with sprintf.

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
- YAYA: Available since the initial version
- AYA: 5.8 and later
