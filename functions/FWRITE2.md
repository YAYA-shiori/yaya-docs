# FWRITE2
**Category:** ファイル操作
**Source:** マニュアル/関数/FWRITE2

## Signature
```
FWRITE2( path, string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | FOPENで開いたファイルのパス（yaya.dllからの相対パス） |
| string | 書き込む文字列 |

## Returns
なし（VOID）

## Description
ファイルに1行書き込む関数。事前にFOPENでファイルを開いておく必要がある。

文字コードはYAYA内部形式からFCHARSETで指定した形式に変換して書き込む。FWRITEと異なり、**行末に改行文字は付加されない**。

改行文字を自動付加したい場合はFWRITEを使用すること。

## Compatibility
- YAYA: 初期バージョンから使用可能
- AYA: バージョン5.8以降

## See Also
- FWRITE
- FREAD
- FWRITEBIN
- FOPEN
