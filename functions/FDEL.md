# FDEL

**Category:** ファイル操作

## Signature

```
FDEL( path )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 削除するファイルのパス。フルパスまたは相対パス（DLLロード位置基準）。 |

## Returns

- `1`: 成功
- `0`: 失敗

## Description

ファイルを削除する。パスはフルパスで指定できる。相対パスの場合は DLL load で渡された位置（多くの場合、DLL のある位置）が基準になる。

## Compatibility

- YAYA: 初版より対応
- AYA: 5.8以降

## See Also

- FCOPY
- FMOVE
- FRENAME
