# SQLCLOSE
**Category:** データベース

## Signature
```
SQLCLOSE( path )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | [SQLOPEN](SQLOPEN.md) で開いたデータベースのパス |

## Returns
返り値はない（VOID）。

## Description
SQLOPEN で開いたデータベースを閉じる。終わっていないトランザクションはロールバックされる。

閉じ忘れたデータベースは unload のときに自動で閉じる。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| path が文字列でない | W0009 | 9 |
| 開いていない | W0015 | 15 |

## Example
```
SQLOPEN("ghost.db")
SQLEXEC("ghost.db", "INSERT INTO talk(text) VALUES(?)", "こんにちは")
SQLCLOSE("ghost.db")
```

## Compatibility
- YAYA: Tc602-11以降

## See Also
- [SQLOPEN](SQLOPEN.md)
- [SQLEXEC](SQLEXEC.md)
- [SQLQUERY](SQLQUERY.md)
