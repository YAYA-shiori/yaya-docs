# STRFORM
**Category:** 文字列操作

## Signature
```
STRFORM(format [, arg ...])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| format | 格式字串 |
| arg | 要嵌入格式字串的引數（可指定多個） |

## Returns
- 成功時：格式化後的字串
- 失敗時：行為未定義

## Description
傳回相當於 C 語言 sprintf 的格式化字串。

格式指定子使用 `$` 作為前綴，而非 `%`（例如：`$04d`、`$s`）。每個格式指定子展開的字串最多為 1024 個字元。

除了透過傳回值取得結果，以及格式指定子的前綴字元為 `$` 之外，使用方式與 sprintf 完全相同。

## Example
與 sprintf 的比較。

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
- YAYA：從初期版本起即可使用
- AYA：5.8 以後
