# MKDIR
**Category:** ファイル操作

## Signature
```
MKDIR(path)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要建立的目錄路徑 |

## Returns
- 成功：1
- 失敗：0

## Description
建立目錄。支援指定完整路徑。若指定相對路徑，基準位置為 DLL 所在位置。

**限制事項：** 一次只能建立一層目錄。若一次指定不存在的多層巢狀目錄，會發生錯誤。

## Compatibility
- YAYA: 從初始版本起即可使用
- AYA: 從版本 5.8 起即可使用

## See Also
- RMDIR
