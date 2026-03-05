# SPLITPATH
**Category:** 文字列操作
**Source:** マニュアル/関数/SPLITPATH

## Signature
```
SPLITPATH(string)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 分解対象のパス文字列 |

## Returns
- 成功時: `(ドライブ名, パス, ファイル名本体, 拡張子)` の汎用配列
- 失敗時: 0

## Description
指定したパス文字列を要素に分解して汎用配列として返します。返す配列の内容はドライブ名・パス・ファイル名本体・拡張子の4要素です。

## Example
```
// 例1: Windowsの絶対パス
_i = SPLITPATH("C:\\umeici\\sample\\readme.txt")
// 結果: "C:", "\\umeici\\sample\\", "readme", ".txt"

// 例2: 相対パス
_j = SPLITPATH("../../../aa/bb/cc.ddd")
// 結果: "", "../../../aa/bb/", "cc", ".ddd"
```

## Compatibility
- YAYA: 初期バージョンより利用可能
- AYA: 5.8以降
