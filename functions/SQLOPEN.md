# SQLOPEN
**Category:** データベース

## Signature
```
SQLOPEN( path [, mode] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | データベースファイルのパス（yaya.dll からの相対パス、または絶対パス）。`":memory:"` ならメモリ上のデータベース |
| mode | 開き方（省略可。下記参照）。省略時は `"rwc"` |

### mode
| mode | 動作 |
|------|------|
| `"rwc"` | 読み書き。ファイルが無ければ作る（省略時） |
| `"rw"` | 読み書き。ファイルが無ければ失敗する |
| `"r"` | 読み取り専用。ファイルが無ければ失敗する |

## Returns
- 1: 成功
- 0: 失敗
- 2: すでに開いている

## Description
[SQLite](https://www.sqlite.org/) のデータベースを開く。開いたデータベースには、[SQLEXEC](SQLEXEC.md) と [SQLQUERY](SQLQUERY.md) で SQL を実行する。

[FOPEN](FOPEN.md) と同じく、データベースは開いたときのパスで識別する。以降の SQLEXEC・SQLQUERY・[SQLCLOSE](SQLCLOSE.md) には、SQLOPEN と同じ書き方のパスを渡す。`"data.db"` と `"./data.db"` のように書き方が違うと、同じファイルでも別のものとして扱われ、2つ目の接続が開く（SQLite のロックで守られるので中身は壊れないが、閉じるときはそれぞれ閉じる必要がある）。

- 複数のデータベースを同時に開ける
- `":memory:"` のデータベースは1つだけ開ける。閉じると中身は消える
- 開いたデータベースは、SQLCLOSE で閉じるか、unload のときに自動で閉じる。終わっていないトランザクションはロールバックされる
- 別のプロセス（ほかのゴーストなど）が書き込み中でロックされているときは、最大1秒待つ。それでも解除されなければ、その SQL はエラー（database is locked）になる

データベースの中身（表の作り方、ジャーナルの方式など）は SQL で指定する。たとえば書き込みの多い用途では、開いた直後に `SQLEXEC(path, "PRAGMA journal_mode=WAL")` を実行しておくとよい。

SQLite の拡張機能の読み込み（`load_extension`）は使えない。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| path または mode が文字列でない | W0009 | 9 |
| path が空文字列 | W0010 | 10 |
| mode が不正 | W0012 | 12 |
| データベースを開けない | W0029 | 29 |

W0029 の警告には SQLite のエラーメッセージが付く。

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
