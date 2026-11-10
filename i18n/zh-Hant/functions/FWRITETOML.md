# FWRITETOML
**Category:** ファイル操作

## Signature
```
FWRITETOML( path, value [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要寫入的檔案路徑（相對於 yaya.dll 的相對路徑，或絕對路徑） |
| value | 要轉換為 TOML 的雜湊（包含巢狀結構） |
| charset | 檔案的字元編碼（可省略）。以字串（例如 `"UTF-8"` `"Shift_JIS"`。[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）或數值指定。省略時或為空字串時，使用 UTF-8（無 BOM）。TOML 規格規定使用 UTF-8，因此通常省略即可 |
| pretty | 設為 1 時使用 `[表]` 標頭排版；設為 0 時，每個最上層鍵各占一行。省略時為 1 |

## Returns
- 成功時：1
- 失敗時：0

## Description
將雜湊轉換為 TOML 並寫入檔案。若檔案已存在，則會覆寫。不需要先使用 [FOPEN](FOPEN.md) 開啟檔案。

值的對應方式與排版格式和 [DUMPTOML](DUMPTOML.md#値の対応) 相同。

寫入的檔案可以使用 [FREADTOML](FREADTOML.md) 讀回。

字串包含 charset 無法表示的字元（例如 Shift_JIS 中的表情符號）時，不會以 `'...'` 括住，而會改用 `"..."`（包含換行時使用 `"""..."""`），並以 `\uXXXX` 表示該字元（BMP 以外的字元會以 `\U0001F600` 這類 8 位數序列表示）。鍵也相同。讀回時會還原為原始字元。

不會建立目錄。無法寫入不存在的目錄。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引數不足 | W0008 | 8 |
| path 不是字串 | W0009 | 9 |
| charset 無效 | W0012 / W0009 | 12 / 9 |
| value 不是雜湊，或陣列元素包含空值（VOID） | W0027（也會輸出原因） | 27 |
| 無法開啟檔案 | W0025 | 25 |
| 字元編碼轉換本身失敗 | W0027 | 27 |
| 寫入失敗 | W0013 | 13 |

## Example
```
_conf = IHASH()
_conf["volume"] = 80
_conf["friends"] = ("うにゅう", "まゆら")
_conf["memo"] = "1行目" + CHR(10) + "2行目"

FWRITETOML("config.toml", _conf)
// config.toml:
// friends = ["うにゅう", "まゆら"]
// memo = """
// 1行目
// 2行目"""
// volume = 80
```

## Compatibility
- YAYA：Tc602-5 以後
- Tc603-1：改為以格式的跳脫序列寫入 charset 無法表示的字元，不再默默轉換成 `?`。傳入不明的字元編碼名稱時，會發出警告 W0012 並失敗（在此之前不會發出警告，而是會視為 OS 預設值）

## See Also
- [DUMPTOML](DUMPTOML.md)
- [FREADTOML](FREADTOML.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FWRITEYAML](FWRITEYAML.md)
