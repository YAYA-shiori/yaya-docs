# FSIZE

**Category:** ファイル操作

## Signature

```
FSIZE(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | サイズを取得するファイルのパス。フルパス指定可。相対パスはDLLのロード位置を基準とする |

## Returns

- 成功時: ファイルサイズ（バイト数）を表す非負の整数
- 失敗時: -1

## Description

ファイルサイズを取得する。パスはフルパスで指定できる。相対パスの場合は DLL load で渡された位置（多くの場合、DLL のある位置）が基準になる。

## Compatibility

- YAYA: 初回リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- FATTRIB
- FSEEK
- FTELL
