# SQLOPEN
**Category:** データベース

## Signature
```
SQLOPEN( path [, mode] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 資料庫檔案的路徑（相對於 yaya.dll 的路徑或絕對路徑）。若為 `":memory:"`，則使用記憶體中的資料庫 |
| mode | 開啟方式（可省略，詳見下方）。省略時為 `"rwc"` |

### mode
| mode | 動作 |
|------|------|
| `"rwc"` | 讀寫。檔案不存在時建立（省略時的預設值） |
| `"rw"` | 讀寫。檔案不存在時失敗 |
| `"r"` | 唯讀。檔案不存在時失敗 |

## Returns
- 1：成功
- 0：失敗
- 2：已開啟

## Description
開啟 [SQLite](https://www.sqlite.org/) 資料庫。開啟後的資料庫可使用 [SQLEXEC](SQLEXEC.md) 和 [SQLQUERY](SQLQUERY.md) 執行 SQL。

與 [FOPEN](FOPEN.md) 相同，資料庫是以開啟時使用的路徑識別。之後使用 SQLEXEC、SQLQUERY、[SQLCLOSE](SQLCLOSE.md) 時，請傳入與 SQLOPEN 相同寫法的路徑。若寫法不同，例如 `"data.db"` 和 `"./data.db"`，即使是同一個檔案，也會被視為不同資料庫並開啟第二個連線（SQLite 鎖定機制會保護資料，因此內容不會損毀，但關閉時必須分別關閉）。

- 可以同時開啟多個資料庫
- 只能開啟一個 `":memory:"` 資料庫。關閉後內容會消失
- 開啟的資料庫會以 SQLCLOSE 關閉，或在 unload 時自動關閉。尚未完成的交易會回復
- 其他程序（例如其他人格）正在寫入而導致鎖定時，最多會等待 1 秒。若仍未解除鎖定，該 SQL 就會發生錯誤（database is locked）

資料庫內容（例如資料表的建立方式、日誌模式）由 SQL 指定。例如，若用途會頻繁寫入，建議在開啟後立即執行 `SQLEXEC(path, "PRAGMA journal_mode=WAL")`。

無法載入 SQLite 擴充功能（`load_extension`）。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| path 或 mode 不是字串 | W0009 | 9 |
| path 是空字串 | W0010 | 10 |
| mode 無效 | W0012 | 12 |
| 無法開啟資料庫 | W0029 | 29 |

W0029 警告會附帶 SQLite 的錯誤訊息。

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
