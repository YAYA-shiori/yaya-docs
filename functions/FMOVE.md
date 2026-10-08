# FMOVE

**Category:** ファイル操作

## Signature

```
FMOVE( path , dir )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 移動元のファイル名。フルパス指定可。相対パスはDLLのロード位置を基準とする |
| dir | 移動先のディレクトリ名 |

## Returns

- 成功時: 1
- 失敗時: 0

## Description

ファイルを移動する。パスはフルパスで指定できる。相対パスの場合は DLL load で渡された位置（多くの場合、DLL のある位置）が基準になる。

## Compatibility

- YAYA: 初回リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- FCOPY
- FRENAME
- FDEL
