# FWRITEBIN
**Category:** ファイル操作
**Source:** マニュアル/関数/FWRITEBIN

## Signature
```
FWRITEBIN( path, string [, char] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | FOPENで指定したファイル名 |
| string | 書き込む文字列 |
| char | バイト値0x00の代替文字（省略時は半角スペース） |

## Returns
なし

## Description
文字コード変換を行わずにデータを書き込む関数。事前にFOPENでファイルを開いておく必要がある。

バイナリモードで開いていない場合は改行コード変換が発生する。

`char`に指定した文字は、YAYAが文字列中にnullバイトを持てないという制限により、バイト値0に変換される。

## Compatibility
Tc516-901以降

## See Also
- FWRITE
- FREADBIN
- FOPEN
