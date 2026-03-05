# FREAD

**Category:** ファイル操作
**Source:** マニュアル/関数/FREAD

## Signature

```
FREAD(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | FOPENで指定したファイルの相対パス（yaya.dll からの相対パス） |

## Returns

- 成功時: 読み取った1行の文字列（CR・LF等の行末文字は除去される）。FCHARSETで指定した文字コードからYAYAの内部エンコーディングに変換される
- ファイル終端に達した場合: -1
- 失敗時: 空文字列

事前に FOPEN でファイルを開いておく必要がある。

## Compatibility

- YAYA: 初回リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- FWRITE
- FREADBIN
- FOPEN
- FREADENCODE
- FWRITE2
- FCHARSET
