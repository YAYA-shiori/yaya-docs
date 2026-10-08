# FCOPY

**Category:** ファイル操作

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

## Description

ファイルをコピーする。パスはフルパスで指定できる。相対パスの場合は DLL load で渡された位置（多くの場合、DLL のある位置）が基準になる。

## Compatibility

- YAYA: 初版より対応
- AYA: 5.8以降

## See Also

- FMOVE
- FRENAME
- FDEL
