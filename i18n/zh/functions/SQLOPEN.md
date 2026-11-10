# SQLOPEN
**Category:** データベース

## Signature
```
SQLOPEN( path [, mode] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 数据库文件的路径（相对于 yaya.dll 的路径，或绝对路径）。如果为 `":memory:"`，则使用内存中的数据库 |
| mode | 打开方式（可省略。参见下文）。省略时为 `"rwc"` |

### mode
| mode | 动作 |
|------|------|
| `"rwc"` | 读写。如果文件不存在则创建（省略时） |
| `"rw"` | 读写。如果文件不存在则失败 |
| `"r"` | 只读。如果文件不存在则失败 |

## Returns
- 1：成功
- 0：失败
- 2：已经打开

## Description
打开 [SQLite](https://www.sqlite.org/) 数据库。打开数据库后，可使用 [SQLEXEC](SQLEXEC.md) 和 [SQLQUERY](SQLQUERY.md) 执行 SQL。

与 [FOPEN](FOPEN.md) 相同，数据库以打开时使用的路径进行标识。之后调用 SQLEXEC、SQLQUERY 和 [SQLCLOSE](SQLCLOSE.md) 时，需传入与 SQLOPEN 相同写法的路径。如果路径写法不同，例如 `"data.db"` 和 `"./data.db"`，即使指向同一个文件，也会被视为不同的数据库，并打开第二个连接（SQLite 锁会保护数据库，因此内容不会损坏；但关闭时需要分别关闭这两个连接）。

- 可以同时打开多个数据库
- 只能打开一个 `":memory:"` 数据库。关闭后，其中的内容会消失
- 已打开的数据库会通过 SQLCLOSE 关闭，或在 unload 时自动关闭。尚未结束的事务会回滚
- 如果数据库因其他进程（例如其他人格）正在写入而被锁定，最多会等待 1 秒。如果仍未解除锁定，该 SQL 会报错（database is locked）

数据库内容（例如表的创建方式、日志模式等）由 SQL 指定。例如，对于写入频繁的用途，建议在打开后立即执行 `SQLEXEC(path, "PRAGMA journal_mode=WAL")`。

无法使用 SQLite 扩展的加载功能（`load_extension`）。

### 错误
| 状况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| path 或 mode 不是字符串 | W0009 | 9 |
| path 为空字符串 | W0010 | 10 |
| mode 无效 | W0012 | 12 |
| 无法打开数据库 | W0029 | 29 |

W0029 警告会附带 SQLite 的错误消息。

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
- YAYA：Tc602-11 及以后

## See Also
- [SQLCLOSE](SQLCLOSE.md)
- [SQLEXEC](SQLEXEC.md)
- [SQLQUERY](SQLQUERY.md)
