# SPLITPATH
**Category:** 文字列操作

## Signature
```
SPLITPATH(string)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | Path string to decompose |

## Returns
- On success: a generic array `(ドライブ名, パス, ファイル名本体, 拡張子)`
- On failure: 0

## Description
Decomposes the specified path string into elements and returns them as a generic array. The returned array contains four elements: drive name, path, file name without extension, and extension.

## Example
```
// 例1: Windowsの絶対パス
_i = SPLITPATH("C:\umeici\sample\readme.txt")
// 結果: "C:", "\umeici\sample\", "readme", ".txt"

// 例2: 相対パス
_j = SPLITPATH("../../../aa/bb/cc.ddd")
// 結果: "", "../../../aa/bb/", "cc", ".ddd"
```

## Compatibility
- YAYA: Available since the initial version
- AYA: 5.8 and later
