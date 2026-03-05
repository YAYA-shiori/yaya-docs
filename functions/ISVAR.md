# ISVAR
**Category:** 型取得/変換
**Source:** マニュアル/関数/ISVAR

## Signature
```
ISVAR(string)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 存在を確認する変数名の文字列 |

## Returns
- 0: 変数が存在しない
- 1: グローバル変数が存在する
- 2: ローカル変数が存在する

## Description
指定した名前の変数が存在するかどうかを確認します。

## Compatibility
- YAYA: 初期バージョンより使用可能
- AYA: バージョン5.8以降で使用可能

## See Also
- ISFUNC
