# LOADLIB
**Category:** 外部ライブラリ
**Source:** マニュアル/関数/LOADLIB

## Signature
```
LOADLIB(path)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 読み込むDLLのパス。YAYAのディレクトリからの相対パス、または絶対パスで指定する |

## Returns
- 1: 読み込み成功
- 2: すでに読み込み済み
- 0: 読み込み失敗

## Description
外部ライブラリ（DLL）ファイルを読み込みます。初回呼び出し時のみLoadLibraryを実行し、ロード関数を呼び出します。読み込む外部DLLはYAYAと同じインターフェース（load/unload/request関数のエクスポート）を持つ必要があります。

## Compatibility
- YAYA: 初期バージョンより使用可能
- AYA: バージョン5.8以降で使用可能

## See Also
- REQUESTLIB
- UNLOADLIB
