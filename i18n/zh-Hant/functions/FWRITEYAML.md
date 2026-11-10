# FWRITEYAML
**Category:** ファイル操作

## Signature
```
FWRITEYAML( path, value [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要寫入檔案的路徑（相對於 yaya.dll 的路徑，或絕對路徑） |
| value | 要轉換成 YAML 的值。雜湊或陣列（包含巢狀結構）也可以作為一個引數傳入 |
| charset | 檔案的字元編碼（可省略）。以字串（例如 `"UTF-8"`、`"Shift_JIS"`。[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）或數值指定。省略時或為空字串時，使用 UTF-8（不含 BOM） |
| pretty | 若為 1，則使用區塊格式；若為 0，則使用流程格式，寫成一行。省略時為 1 |

## Returns
- 成功時：1
- 失敗時：0

## Description
將值轉換成 YAML 並寫入檔案。若檔案已存在，則會覆寫。不需要先使用 [FOPEN](FOPEN.md) 開啟檔案。

支援的值與格式化方式和 [DUMPYAML](DUMPYAML.md#値の対応) 相同。使用區塊格式時，會在檔案末尾加上換行（LF）。

寫入的檔案可以使用 [FREADYAML](FREADYAML.md) 讀回（若使用 UTF-8 以外的編碼寫入，請指定相同的 charset）。

字串中若含有無法以 charset 表示的字元（例如 Shift_JIS 中的表情符號），不會以不加引號的形式或區塊純量（`|`）表示，而會以 `"..."` 括住，並將該字元寫成 `\uXXXX`（BMP 以外的字元則寫成 `\U0001F600` 之類的 8 位數形式）。鍵也一樣。讀回時會還原成原本的字元。

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
_conf["memo"] = "1行目" + CHR(10) + "2行目"

FWRITEYAML("config.yaml", _conf)
// config.yaml:
// friends:
//   - うにゅう
//   - まゆら
// memo: |-
//   1行目
//   2行目
// volume: 80

FWRITEYAML("config.flow.yaml", _conf, "", 0)
// {friends: [うにゅう, まゆら], memo: "1行目\n2行目", volume: 80}
```

## Compatibility
- YAYA：Tc602-5 以後
- Tc603-1：改為將無法以 charset 表示的字元以格式規定的跳脫方式寫入，而不再默默轉成 `?`。傳入不明的字元編碼名稱時，會顯示警告 W0012 並失敗（在此之前不會顯示警告，而是將其視為 OS 預設值）

## See Also
- [DUMPYAML](DUMPYAML.md)
- [FREADYAML](FREADYAML.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FWRITETOML](FWRITETOML.md)
