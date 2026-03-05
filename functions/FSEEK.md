# FSEEK

**Category:** ファイル操作
**Source:** マニュアル/関数/FSEEK

## Signature

```
FSEEK(path, offset, origin)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | FOPENで指定したファイル名 |
| offset | 移動するバイト数 |
| origin | 移動の起点を示す文字列。`SEEK_CUR` または `current`（現在位置）、`SEEK_END` または `end`（ファイル終端）、`SEEK_SET` または `start`（ファイル先頭） |

## Returns

- 成功時: 1
- 失敗時: 0

非バイナリモードでは改行コードの自動変換により FSEEK/FTELL が期待通りに動作しない場合がある。これらの関数を使用する場合は FOPEN でバイナリモードを指定することを推奨する。

## See Also

- FTELL
- FOPEN
