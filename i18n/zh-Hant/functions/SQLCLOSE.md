# SQLCLOSE
**Category:** データベース

## Signature
```
SQLCLOSE( path )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 透過 [SQLOPEN](SQLOPEN.md) 開啟的資料庫路徑 |

## Returns
沒有傳回值（VOID）。

## Description
關閉透過 SQLOPEN 開啟的資料庫。尚未完成的交易會復原。

忘記關閉的資料庫會在 unload 時自動關閉。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| path 不是字串 | W0009 | 9 |
| 資料庫未開啟 | W0015 | 15 |

## Example
```
SQLOPEN("ghost.db")
SQLEXEC("ghost.db", "INSERT INTO talk(text) VALUES(?)", "こんにちは")
SQLCLOSE("ghost.db")
```

## Compatibility
- YAYA：Tc602-11 以後

## See Also
- [SQLOPEN](SQLOPEN.md)
- [SQLEXEC](SQLEXEC.md)
- [SQLQUERY](SQLQUERY.md)
