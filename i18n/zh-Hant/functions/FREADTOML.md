# FREADTOML
**Category:** ファイル操作

## Signature
```
FREADTOML( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要讀取的 TOML 檔案路徑（相對於 yaya.dll 的路徑，或絕對路徑） |
| charset | 檔案的字元編碼（可省略）。以字串（例如 `"UTF-8"`、`"Shift_JIS"`。[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）或數值指定。省略時使用 UTF-8（TOML 規格規定使用 UTF-8） |

## Returns
- 成功時：轉換 TOML 後的雜湊（見下方的[值的對應](#値の対応)）
- 失敗時：空（VOID）

## Description
讀取並解析整個 TOML 檔案，轉換成雜湊後傳回。不必先用 [FOPEN](FOPEN.md) 開啟檔案。

TOML 由 YAYA 自行解析。支援 [TOML v1.0.0](https://toml.io/ja/v1.0.0)。也接受 v1.1 新增的行內表換行與結尾逗號，以及 `\e`、`\xHH` 跳脫序列。

- 忽略開頭的 UTF-8 BOM。換行可以是 CRLF 或 LF
- 最上層一律為雜湊。空檔案或只有註解的檔案會成為空雜湊
- 同一個鍵或表格定義兩次、以點分隔的鍵建立的表格又用 `[表]` 重新定義、在行內表之後再新增內容等規格禁止的情況，都會視為錯誤

### 值的對應

| TOML | YAYA |
|------|------|
| 表格（`[table]`、行內表 `{ }`、點分隔的鍵 `a.b = 1`） | 雜湊 |
| 表格陣列（`[[array]]`） | 雜湊的通用陣列 |
| 陣列 | 通用陣列（可包含陣列或雜湊，形成巢狀結構） |
| 字串（`"..."`、`'...'`、`"""..."""`、`'''...'''`） | 字串 |
| 整數（`42`、`1_000`、`0xDEAD`、`0o755`、`0b1101`） | 整數 |
| 實數（`3.14`、`5e+22`、`inf`、`nan`） | 實數 |
| `true` / `false` | 整數 1 / 0 |
| 日期時間（例如 `1979-05-27T07:32:00Z`、`1979-05-27`、`07:32:00`） | 原樣寫入的字串 |

- 超出整數範圍（大於等於 -2^63 且小於 2^63）的整數會視為錯誤
- 不保留鍵的順序，而是依照雜湊鍵的順序（參閱 [HASH_KEYS](HASH_KEYS.md)）

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| path 不是字串 | W0009 | 9 |
| charset 無效 | W0012 / W0009 | 12 / 9 |
| 無法開啟檔案 | W0025 | 25 |
| 無法以 TOML 格式解析 | W0026（也會輸出行號與原因） | 26 |

## Example
config.toml:
```toml
# ゴーストの設定
title = "設定"
updated = 2026-09-27T12:00:00+09:00

[ghost]
name = "さくら"
age = 17
visible = true
tags = ["ghost", "shell"]
path = 'C:\ssp\ghost'

[[friends]]
name = "うにゅう"

[[friends]]
name = "まゆら"
```

```
_t = FREADTOML("config.toml")
_t["title"]                 // 設定
_t["updated"]               // 文字列の 2026-09-27T12:00:00+09:00
_t["ghost"]["name"]         // さくら
_t["ghost"]["visible"]      // 1
_t["ghost"]["tags"][1]      // shell
_t["ghost"]["path"]         // C:\ssp\ghost
_t["friends"][1]["name"]    // まゆら

foreach _t["friends"]; _f {
    // _f に {name: うにゅう}、{name: まゆら} のハッシュが順に入る
}
```

## Compatibility
- YAYA：Tc602-5 以後
- Tc603-1：傳入未知的字元編碼名稱時，改為顯示警告 W0012 並以失敗告終（此前不會顯示警告，而是以 OS 預設值處理）

## See Also
- [PARSETOML](PARSETOML.md)
- [FWRITETOML](FWRITETOML.md)
- [FREADJSON](FREADJSON.md)
- [FREADYAML](FREADYAML.md)
- [巢狀值與多維指派](../grammar/13-nesting.md)
