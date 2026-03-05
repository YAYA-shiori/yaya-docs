# SETLASTERROR
**Category:** デバッグ
**Source:** マニュアル/関数/SETLASTERROR

## Signature
```
SETLASTERROR( code )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| code | 設定するエラーコード（整数値） |

## Returns
なし

## Description
システム関数のエラーコードを設定します。YAYA スクリプト実行中にエラー状態を手動で設定することができます。

GETLASTERROR と組み合わせてシステムレベルのエラー状態を管理します。

## Compatibility
- YAYA: 初期バージョンより対応
- AYA: 5.8以降

## See Also
- GETLASTERROR
