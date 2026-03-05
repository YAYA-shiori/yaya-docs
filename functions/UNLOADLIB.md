# UNLOADLIB
**Category:** 外部ライブラリ
**Source:** マニュアル/関数/UNLOADLIB

## Signature
```
UNLOADLIB( path )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | DLLのパス。YAYAのディレクトリからの相対パスまたは絶対パス |

## Returns
VOID（戻り値なし）

## Description
外部ライブラリ（DLL）をアンロードする。最初の呼び出し時にアンロード操作を実行し、その後FreeLibraryを行う。

外部ライブラリDLLは、YAYA自身と同じインターフェース（load/unload/request関数のエクスポート）を持っている必要がある。

## Compatibility
- YAYA: 初期バージョンより
- AYA: 5.8以降

## See Also
- LOADLIB
- REQUESTLIB
