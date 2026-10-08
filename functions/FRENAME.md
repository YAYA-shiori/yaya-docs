# FRENAME

**Category:** ファイル操作

## Signature

```
FRENAME( from , to )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| from | 変更前のファイル名。フルパス指定可。相対パスはDLLのロード位置を基準とする |
| to | 変更後のファイル名 |

## Returns

- 成功時: 1
- 失敗時: 0

## Description

ファイルの名前を変更する。パスはフルパスで指定できる。相対パスの場合は DLL load で渡された位置（多くの場合、DLL のある位置）が基準になる。

## Compatibility

- YAYA: 初回リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- FCOPY
- FMOVE
- FDEL
