# FWRITEXML
**Category:** ファイル操作

## Signature
```
FWRITEXML( path, element [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要寫入的檔案路徑（相對於 yaya.dll 的相對路徑，或絕對路徑） |
| element | 表示根元素的雜湊（與 [FREADXML](FREADXML.md#要素の形) 傳回的格式相同） |
| charset | 檔案的字元編碼（可省略）。以字串（例如 `"UTF-8"` `"Shift_JIS"`。[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）或數值指定。省略時或為空字串時，使用 UTF-8（無 BOM） |
| pretty | 設為 1 時加入換行與縮排來排版。省略時為 1（排版） |

## Returns
- 成功時：1
- 失敗時：0

## Description
將元素的雜湊轉換為 XML 並寫入檔案。若檔案已存在，則會覆寫。不需要先使用 [FOPEN](FOPEN.md) 開啟檔案。

元素雜湊的格式、跳脫方式與排版格式和 [DUMPXML](DUMPXML.md) 相同。檔案開頭會附加符合 charset 的 XML 宣告。

| charset | XML 宣告的 encoding |
|---------|------|
| UTF-8（省略時） | `UTF-8` |
| Shift_JIS | `Shift_JIS` |
| EUC-JP | `EUC-JP` |
| ISO-2022-JP | `ISO-2022-JP` |
| BIG5 | `Big5` |
| GB2312 | `GB2312` |
| EUC-KR | `EUC-KR` |
| default（OS 的字元編碼） | 根據 OS 的碼頁決定（若為 932，則為 `Shift_JIS`） |

讀取寫入的檔案時，[FREADXML](FREADXML.md) 會參照 XML 宣告中的 encoding，因此不必指定 charset。

包含 charset 無法表示的字元（例如 Shift_JIS 中的表情符號）時，文字與屬性值中的字元會以字元參照 `&#x1F600;` 寫入。讀回時會還原為原始字元。元素名稱或屬性名稱中的字元無法使用字元參照，因此會發生 W0027 錯誤。

不會建立目錄。無法寫入不存在的目錄。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引數不足 | W0008 | 8 |
| path 不是字串 | W0009 | 9 |
| charset 無效 | W0012 / W0009 | 12 / 9 |
| 元素雜湊無效（請參閱 [DUMPXML](DUMPXML.md#エラー)） | W0027 | 27 |
| 元素名稱或屬性名稱包含 charset 無法表示的字元 | W0027 | 27 |
| 無法開啟檔案 | W0025 | 25 |
| 寫入失敗 | W0013 | 13 |

## Example
```
_x = FREADXML("shop.xml")
_x["children"][0]["text"] = "みかん"

FWRITEXML("shop.xml", _x, "Shift_JIS")
// shop.xml:
// <?xml version="1.0" encoding="Shift_JIS"?>
// <shop name="A">
//     <item id="1">みかん</item>
//     <item id="2">バナナ</item>
// </shop>
```

## Compatibility
- YAYA：Tc602-1 以後
- Tc603-1：改為以格式的跳脫序列寫入 charset 無法表示的字元，不再默默轉換成 `?`。傳入不明的字元編碼名稱時，會發出警告 W0012 並失敗（在此之前不會發出警告，而是會視為 OS 預設值）

## See Also
- [DUMPXML](DUMPXML.md)
- [FREADXML](FREADXML.md)
- [FWRITEJSON](FWRITEJSON.md)
