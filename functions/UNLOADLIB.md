# UNLOADLIB
**Category:** 外部ライブラリ

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

別のスレッド（[THREADSTART](THREADSTART.md)）が [REQUESTLIB](REQUESTLIB.md) でそのライブラリを呼び出している最中は、アンロードせずに警告 W0013 を出す。呼び出しが終わってから、もう一度 UNLOADLIB すればよい。

## Compatibility
- YAYA: 初期バージョンより
- AYA: 5.8以降
- Tc608-1: ほかのスレッドが呼び出し中のライブラリは、アンロードしないようにした

## See Also
- LOADLIB
- REQUESTLIB
