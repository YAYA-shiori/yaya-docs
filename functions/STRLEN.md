# STRLEN
**Category:** 文字列操作
**Source:** マニュアル/関数/STRLEN

## Signature
```
STRLEN(string)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 文字数を取得する文字列 |

## Returns
- 成功時: 文字数（整数）
- 失敗時: 0

## Description
文字列の文字数を返します。バイト数ではなく文字数を返すため、漢字などのマルチバイト文字も1文字としてカウントされます。

## Compatibility
- YAYA: 初期バージョンより利用可能
- AYA: 5.8以降

## See Also
- STRSTR（部分文字列検索）
- SUBSTR（部分文字列取得）
- GETSTRBYTES（バイト数取得）
