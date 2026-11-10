# SPLITPATH
**Category:** 文字列操作

## Signature
```
SPLITPATH(string)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要拆分的路径字符串 |

## Returns
- 成功时：`(驱动器名, 路径, 文件名主体, 扩展名)` 组成的通用数组
- 失败时：0

## Description
将指定的路径字符串拆分为各个元素，并以通用数组的形式返回。返回数组包含驱动器名、路径、文件名主体和扩展名这 4 个元素。

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
- YAYA：从初始版本起可用
- AYA：5.8 及之后
