# REPLACE
**Category:** 文字列操作
**Source:** マニュアル/関数/REPLACE

## Signature
```
REPLACE( src , before , after [ , count ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 変換対象の文字列 |
| before | 検索する部分文字列 |
| after | 置換後の部分文字列 |
| count | （省略可）置換を行う回数。0未満または省略した場合はすべての該当箇所を置換する |

## Returns
- 成功: 置換後の文字列
- 失敗: 元の src 文字列（変更なし）

## Description
文字列の置換を行います。該当するすべての変換前文字列が置換されます。`count` を指定することで置換回数を制限できます。

## Example
```
_tehai = '4m4m5m5m6m6m2p3p3p4p1s1s1s'
_tsumo = '4p'
_dahai = '1s'
_tehai = REPLACE(_tehai, _dahai, _tsumo, 1)
_tehai // '4m4m5m5m6m6m2p3p3p4p4p1s1s'
```

## Compatibility
- YAYA: 初期リリースから使用可能（countパラメータはTc548-1で追加）
- AYA: バージョン5.8から使用可能
