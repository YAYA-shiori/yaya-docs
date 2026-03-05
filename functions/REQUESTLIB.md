# REQUESTLIB
**Category:** 外部ライブラリ
**Source:** マニュアル/関数/REQUESTLIB

## Signature
```
REQUESTLIB( path , string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | DLLの位置。YAYAのある位置からの相対パス、または絶対パス。 |
| string | request関数に渡す文字列 |

## Returns
- 成功: request関数が生成した文字列
- 失敗: VOID（何も返さない）

## Description
事前にロードされた外部ライブラリのrequest関数を呼び出し、その結果を取得します。外部ライブラリのDLLは、YAYAと同じインターフェース（load/unload/request関数のエクスポート）を持つ必要があります。

## Compatibility
- YAYA: 初期リリースから使用可能
- AYA: バージョン5.8以降で使用可能

## See Also
- LOADLIB
- UNLOADLIB
