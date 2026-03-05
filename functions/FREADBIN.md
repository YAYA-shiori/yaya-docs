# FREADBIN

**Category:** ファイル操作
**Source:** マニュアル/関数/FREADBIN

## Signature

```
FREADBIN( path , size [ , char ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | FOPENで開いたファイルのファイル名 |
| size | 読み取るバイト数。0 を指定するとファイル全体を読み取る |
| char | ヌルバイト（0x00）を置換する文字（省略時はスペース） |

## Returns

- 成功時: 読み取ったデータの文字列
- ファイル終端に達した場合: -1
- 失敗時: 空文字列

文字コード変換を行わずにバイナリデータをそのまま読み取る。行末変換を避けるため、事前に FOPEN でバイナリモードを指定することが推奨される。ヌルバイト（0x00）は指定した文字に置換される。

## Compatibility

- YAYA: Tc516-901 以降
- 注意: Tc540-3 まで、0x80 以上のバイトがキャストエラーにより 0xFF80 番台に誤変換されるバグが存在した

## See Also

- FREAD
- FWRITEBIN
