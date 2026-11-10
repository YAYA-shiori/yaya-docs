# FWRITEJSON
**Category:** ファイル操作

## Signature
```
FWRITEJSON( path, value [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要寫入的檔案路徑（相對於 yaya.dll 的相對路徑，或絕對路徑） |
| value | 要轉換為 JSON 的值。雜湊或陣列（包含巢狀結構）也可以作為單一引數傳入 |
| charset | 檔案的字元編碼（可省略）。以字串（例如 `"UTF-8"` `"Shift_JIS"`。[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）或數值指定。省略時或為空字串時，使用 UTF-8（無 BOM） |
| pretty | 設為 1 時加入換行與縮排來排版。省略時為 1（排版） |

## Returns
- 成功時：1
- 失敗時：0

## Description
將值轉換為 JSON 並寫入檔案。若檔案已存在，則會覆寫。不需要先使用 [FOPEN](FOPEN.md) 開啟檔案。

值的對應方式與排版格式和 [DUMPJSON](DUMPJSON.md#値の対応) 相同。排版時會在檔案末尾加上換行（LF）。

寫入的檔案可以使用 [FREADJSON](FREADJSON.md) 讀回（使用 UTF-8 以外的編碼寫入時，請指定相同的 charset）。

包含 charset 無法表示的字元（例如 Shift_JIS 中的表情符號）時，會以 JSON 跳脫序列 `\uXXXX` 寫入（BMP 以外的字元會以 `\uD83D\uDE00` 這類代理對的兩個序列表示）。讀回時會還原為原始字元。

不會建立目錄。無法寫入不存在的目錄。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引數不足 | W0008 | 8 |
| path 不是字串 | W0009 | 9 |
| charset 無效 | W0012 / W0009 | 12 / 9 |
| 無法開啟檔案 | W0025 | 25 |
| 字元編碼轉換本身失敗 | W0027 | 27 |
| 寫入失敗 | W0013 | 13 |

## Example
```
_conf = IHASH()
_conf["volume"] = 80
_conf["friends"] = ("うにゅう", "まゆら")

FWRITEJSON("config.json", _conf)
// config.json:
// {
//     "friends": [
//         "うにゅう",
//         "まゆら"
//     ],
//     "volume": 80
// }

FWRITEJSON("config.min.json", _conf, "", 0)   // UTF-8 で1行に
```

## Compatibility
- YAYA：Tc602-1 以後
- Tc603-1：改為以格式的跳脫序列寫入 charset 無法表示的字元，不再默默轉換成 `?`。傳入不明的字元編碼名稱時，會發出警告 W0012 並失敗（在此之前不會發出警告，而是會視為 OS 預設值）

## See Also
- [DUMPJSON](DUMPJSON.md)
- [FREADJSON](FREADJSON.md)
- [FWRITEXML](FWRITEXML.md)
