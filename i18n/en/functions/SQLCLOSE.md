# SQLCLOSE
**Category:** データベース

## Signature
```
SQLCLOSE( path )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path of the database opened with [SQLOPEN](SQLOPEN.md) |

## Returns
No return value (VOID).

## Description
Closes the database opened with SQLOPEN. Any unfinished transactions are rolled back.

Databases left open are closed automatically during unload.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| path is not a string | W0009 | 9 |
| Not open | W0015 | 15 |

## Example
```
SQLOPEN("ghost.db")
SQLEXEC("ghost.db", "INSERT INTO talk(text) VALUES(?)", "こんにちは")
SQLCLOSE("ghost.db")
```

## Compatibility
- YAYA: Tc602-11 and later

## See Also
- [SQLOPEN](SQLOPEN.md)
- [SQLEXEC](SQLEXEC.md)
- [SQLQUERY](SQLQUERY.md)
