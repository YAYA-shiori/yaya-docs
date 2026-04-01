# FSTATUS

**Category:** ファイル操作
**Source:** マニュアル/関数/FSTATUS

## Signature

```
FSTATUS(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | FOPENで指定したファイル名 |

## Returns

直前のファイルI/O操作（FOPEN・FREAD・FWRITE・FSEEK・FTELLなど）の結果ステータスを返す。

| 戻り値 | 意味 |
|--------|------|
| 0 | 正常終了（エラーなし） |
| -1 | エラー発生 |
| 1 | ファイル末尾（EOF）に達した |

## Availability

Tc573-3 以降

## See Also

- FOPEN
- FSEEK
- FTELL
