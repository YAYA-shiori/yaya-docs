# FCOPY

**Category:** ファイル操作
**Source:** マニュアル/関数/FCOPY

## Signature

```
FCOPY( path, dir )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | コピー元のファイル名。フルパスまたは相対パス（DLLロード位置基準）。 |
| dir | コピー先のディレクトリ名 |

## Returns

- `1`: 成功
- `0`: 失敗

## Compatibility

- YAYA: 初版より対応
- AYA: 5.8以降

## See Also

- FMOVE
- FRENAME
- FDEL
