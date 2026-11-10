# SPLITPATH
**Category:** 文字列操作

## Signature
```
SPLITPATH(string)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要拆解的路徑字串 |

## Returns
- 成功時：`(磁碟機名稱, 路徑, 檔名主體, 副檔名)` 的通用陣列
- 失敗時：0

## Description
將指定的路徑字串拆解為各個元素，並以通用陣列傳回。傳回的陣列包含磁碟機名稱、路徑、檔名主體、副檔名等 4 個元素。

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
- YAYA：從初始版本起即可使用
- AYA：5.8 以後
