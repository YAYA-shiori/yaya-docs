# FSTATUS

**Category:** ファイル操作

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

## Description

ファイル読み書き関数（FOPEN・FREAD 系・FWRITE 系・FSEEK・FTELL）の直前の操作の状態を取得する。

## Compatibility

- YAYA: Tc573-3 以降

## See Also

- FOPEN
- FSEEK
- FTELL
