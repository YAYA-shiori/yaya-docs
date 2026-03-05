# TOLOWER
**Category:** 文字列操作
**Source:** マニュアル/関数/TOLOWER

## Signature
```
TOLOWER( string [ , locale ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 変換したい文字列 |
| locale | （省略可）setlocale互換のロケール文字列。省略時はCモード（A-Zのみa-zに変換） |

## Returns
- 成功: 変換後の小文字文字列
- 失敗: VOID

## Description
文字列中の大文字をすべて小文字に変換して返す。localeを省略した場合はCモード（A-Zのみa-zに変換）となる。

## Example
```
_str = 'sAkuRa'
_str = TOLOWER( _str )
_str // 'sakura'
```

## Compatibility
- YAYA: 初期バージョンより（localeパラメータはTc569-5以降）
- AYA: 5.8以降

## See Also
- TOUPPER
