# SQLOPEN
**Category:** データベース

## Signature
```
SQLOPEN( path [, mode] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path to the database file (relative to yaya.dll, or an absolute path). If `":memory:"`, the database is stored in memory |
| mode | How to open the database (optional; see below). Defaults to `"rwc"` |

### mode
| mode | Behavior |
|------|------|
| `"rwc"` | Read and write. Create the file if it does not exist (default) |
| `"rw"` | Read and write. Fail if the file does not exist |
| `"r"` | Read-only. Fail if the file does not exist |

## Returns
- 1: Success
- 0: Failure
- 2: Already open

## Description
Open a [SQLite](https://www.sqlite.org/) database. Run SQL on the opened database with [SQLEXEC](SQLEXEC.md) and [SQLQUERY](SQLQUERY.md).

As with [FOPEN](FOPEN.md), a database is identified by the path used when it was opened. For subsequent calls to SQLEXEC, SQLQUERY, and [SQLCLOSE](SQLCLOSE.md), pass a path written in the same way as for SQLOPEN. If the paths are written differently, such as `"data.db"` and `"./data.db"`, they are treated as separate databases even if they refer to the same file, and a second connection is opened (SQLite locking prevents the contents from being corrupted, but each connection must be closed separately).

- Multiple databases can be open at the same time
- Only one `":memory:"` database can be open. Its contents are erased when it is closed
- An opened database is closed by SQLCLOSE or automatically when unloaded. Any unfinished transactions are rolled back
- If the database is locked because another process (such as another ghost) is writing to it, YAYA waits for up to 1 second. If the lock is still in place, that SQL operation fails with an error (database is locked)

Specify database details (such as how to create tables and the journaling mode) in SQL. For example, for workloads with frequent writes, it is a good idea to run `SQLEXEC(path, "PRAGMA journal_mode=WAL")` immediately after opening the database.

Loading SQLite extensions (`load_extension`) is not supported.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| path or mode is not a string | W0009 | 9 |
| path is an empty string | W0010 | 10 |
| Invalid mode | W0012 | 12 |
| Unable to open the database | W0029 | 29 |

The W0029 warning includes an SQLite error message.

## Example
```
if SQLOPEN("ghost.db") == 0 {
    // 開けなかった
}
SQLEXEC("ghost.db", "CREATE TABLE IF NOT EXISTS talk(id INTEGER PRIMARY KEY, text TEXT)")

SQLOPEN(":memory:")      // メモリ上の作業用データベース
SQLOPEN("ref.db", "r")   // 読み取り専用
```

## Compatibility
- YAYA: Tc602-11以降

## See Also
- [SQLCLOSE](SQLCLOSE.md)
- [SQLEXEC](SQLEXEC.md)
- [SQLQUERY](SQLQUERY.md)
