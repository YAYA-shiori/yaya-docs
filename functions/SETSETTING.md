# SETSETTING
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/SETSETTING

## Signature
```
SETSETTING( name , string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 設定情報のエントリ名（文字列）。基本設定ファイルのエントリ名を指定 |
| string | 設定する値（文字列） |

## Returns
- **1**: 成功
- **0**: 失敗

## Description
動作中の文の設定情報を変更します。GETSETTING と対になる関数です。

以下の設定エントリは初回ロード時にのみ意味を持つため、実行時に変更しても効果がありません:
- dic
- msglang
- charset.dic
- checkparser

## Compatibility
- YAYA: 初期バージョンより対応

## See Also
- GETSETTING
- マニュアル/文法/1.基本設定
