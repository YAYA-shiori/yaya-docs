# TOUPPER
**Category:** 文字列操作
**Source:** マニュアル/関数/TOUPPER

## Signature
```
TOUPPER( string [ , locale ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 変換したい文字列 |
| locale | （省略可）setlocale互換のロケール文字列。省略時はCモード（a-zのみA-Zに変換） |

## Returns
- 成功: 変換後の大文字文字列
- 失敗: VOID

## Description
文字列中の小文字をすべて大文字に変換して返す。localeを省略した場合はCモード（a-zのみA-Zに変換）となる。

## Example
```
_str = 'sAkuRa'
_str = TOUPPER( _str )
_str // 'SAKURA'
```

## Compatibility
- YAYA: 初期バージョンより（localeパラメータはTc569-5以降）
- AYA: 5.8以降

## See Also
- TOLOWER
- TRANSLATE
