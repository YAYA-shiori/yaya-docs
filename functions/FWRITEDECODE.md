# FWRITEDECODE
**Category:** ファイル操作

## Signature
```
FWRITEDECODE( path, string [, type] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | FOPENで指定したファイル名 |
| string | 書き込むエンコードされた文字列 |
| type | デコード方式: `"base64"`, `"url"`, `"form"` のいずれか（省略時はbase64。詳細は [STRDECODE](STRDECODE.md) を参照）。Tc554-1 は実装ミスで省略できなかった |

## Returns
なし

## Description
base64またはURLエンコードからデコードしながらデータを書き込む関数。FREADENCODEの逆操作を行う。

事前にFOPENでファイルを開いておく必要がある。FOPENをバイナリアクセスで開かない場合は、改行コード変換が行われる。デコード結果にバイト値0（0x00）が含まれていても、正常に書き込める。

## Compatibility
- YAYA: Tc554-1 以降
- Tc554-1 では実装ミスで `type` を省略できなかった

## See Also
- FWRITE
- FREADENCODE
- STRDECODE
