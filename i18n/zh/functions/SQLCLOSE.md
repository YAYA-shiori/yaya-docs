# SQLCLOSE
**Category:** データベース

## Signature
```
SQLCLOSE( path )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 通过 [SQLOPEN](SQLOPEN.md) 打开的数据库路径 |

## Returns
无返回值（VOID）。

## Description
关闭通过 SQLOPEN 打开的数据库。尚未完成的事务会回滚。

忘记关闭的数据库会在 unload 时自动关闭。

### 错误
| 状况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| path 不是字符串 | W0009 | 9 |
| 数据库未打开 | W0015 | 15 |

## Example
```
SQLOPEN("ghost.db")
SQLEXEC("ghost.db", "INSERT INTO talk(text) VALUES(?)", "こんにちは")
SQLCLOSE("ghost.db")
```

## Compatibility
- YAYA：Tc602-11 及之后

## See Also
- [SQLOPEN](SQLOPEN.md)
- [SQLEXEC](SQLEXEC.md)
- [SQLQUERY](SQLQUERY.md)
