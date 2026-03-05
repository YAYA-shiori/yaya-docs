# FREADENCODE

**Category:** ファイル操作
**Source:** マニュアル/関数/FREADENCODE

## Signature

```
FREADENCODE(path, size [, type])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | FOPENで指定したファイル名 |
| size | 読み取るバイト数。0 を指定するとファイル全体を読み取る |
| type | エンコード種別。"base64"、"url"、"form" のいずれか。省略時は "base64"（詳細は STRENCODE 参照） |

## Returns

- 成功時: エンコードされた文字列
- ファイル終端に達した場合: -1
- 失敗時: 空文字列

ファイルをBase64またはURLエンコードしながら読み取る。バイナリモードで開いていない場合は行コード変換が適用される。事前に FOPEN でファイルを開いておく必要がある。

## Compatibility

- YAYA: Tc535-1 以降

## See Also

- FREAD
- FREADBIN
- FOPEN
- STRENCODE
