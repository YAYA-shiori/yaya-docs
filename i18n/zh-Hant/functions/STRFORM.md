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

格式指定符會以 `$` 而非 `%` 作為前綴（例如：`$04d`、`$s`）。每個格式指定符展開的字串最多為 1024 個字元。

## Example
```
year = 1941
warname = "太平洋"
str = STRFORM("$04d年　$s戦争勃発。", year, warname)
// 結果: "1941年　太平洋戦争勃発。"
```

## Compatibility
- YAYA：自初期版本起即可使用
- AYA：5.8 之後
