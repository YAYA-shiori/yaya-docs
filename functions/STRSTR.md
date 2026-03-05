# STRSTR
**Category:** 文字列操作
**Source:** マニュアル/関数/STRSTR

## Signature
```
STRSTR(src, search, pos)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 検索対象の文字列 |
| search | 検索する部分文字列 |
| pos | 検索開始位置（0始まり） |

## Returns
- 見つかった場合: 部分文字列が始まる文字位置（0始まり）
- 見つからない場合: -1

## Description
文字列内の部分文字列を検索し、見つかった文字位置を返します。

## Compatibility
- YAYA: 初期バージョンより利用可能
- AYA: 5.8以降

## See Also
- STRLEN（文字列長取得）
- SUBSTR（部分文字列取得）
