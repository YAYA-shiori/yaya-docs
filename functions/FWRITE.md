# FWRITE
**Category:** ファイル操作
**Source:** マニュアル/関数/FWRITE

## Signature
```
FWRITE( path, string )
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

文字コードはYAYA内部形式からFCHARSETで指定した形式に変換して書き込む。行末には自動的に改行文字が付加される。

改行文字を付加せずに書き込む場合はFWRITE2を使用すること。

## Compatibility
- YAYA: 初期バージョンから使用可能
- AYA: バージョン5.8以降

## See Also
- FWRITE2
- FREAD
- FOPEN
- FCHARSET
