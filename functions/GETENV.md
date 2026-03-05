# GETENV
**Category:** システム情報
**Source:** マニュアル/関数/GETENV

## Signature
```
GETENV( [name] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 取得したい環境変数名（文字列） |

## Returns
- 成功: 環境変数の内容（文字列）
- 失敗: 空文字列

## Description
OSの環境変数を名前で取得する関数。指定した環境変数が存在しない場合は空文字列を返す。

なお、環境変数の設定関数は不用意に触ると危険なため、現状実装予定はない。

## Compatibility
Tc552-1以降
