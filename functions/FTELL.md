# FTELL

**Category:** ファイル操作
**Source:** マニュアル/関数/FTELL

## Signature

```
FTELL(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | FOPENで指定したファイル名 |

## Returns

- 成功時: ファイル先頭からのバイトオフセット（現在のファイル位置）
- 失敗時: -1

非バイナリモードでは改行コードの自動変換により FSEEK/FTELL が期待通りに動作しない場合がある。これらの関数を使用する場合は FOPEN でバイナリモードを指定することを推奨する。

## See Also

- FSEEK
- FOPEN
