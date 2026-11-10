# FREADXML
**Category:** ファイル操作

## Signature
```
FREADXML( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要讀取的 XML 檔案路徑（相對於 yaya.dll 的路徑，或絕對路徑） |
| charset | 檔案的字元編碼（可省略）。以字串（例如 `"UTF-8"`、`"Shift_JIS"`。[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）或數值指定。省略時依照下方說明自動決定 |

## Returns
- 成功時：代表根元素的雜湊（見下方的[元素結構](#要素の形)）
- 失敗時：空（VOID）

## Description
讀取並解析整個 XML 檔案，將根元素轉換成雜湊後傳回。不必先用 [FOPEN](FOPEN.md) 開啟檔案。

XML 解析使用 [TinyXML-2](https://github.com/ponapalt/tinyxml2)。

省略 charset 時，依照以下順序決定字元編碼。

1. 如果開頭有 UTF-8 BOM，則使用 UTF-8
2. XML 宣告（`<?xml version="1.0" encoding="Shift_JIS"?>`）中的 encoding。`Windows-31J` 和 `CP932` 也會視為 Shift_JIS
3. 以上皆無，或 encoding 是 YAYA 不認識的字元編碼時，使用 UTF-8

指定 charset 時，會忽略 XML 宣告中的 encoding。

### 元素結構

元素會成為包含以下 4 個鍵的雜湊。即使內容為空，這些鍵也一律存在。

| 鍵 | 值 |
|------|----|
| `name` | 標籤名稱（若有命名空間前綴，則維持 `ns:tag`） |
| `attr` | 屬性名稱 → 屬性值的雜湊。所有值都是字串 |
| `children` | 子元素的雜湊通用陣列（依出現順序排列） |
| `text` | 依序串接直接位於元素內的文字（包含 CDATA） |

- 實體參照（例如 `&amp;`、`&#x3042;`）會先展開
- 文字前後的空白與換行會原樣保留。元素之間只有空白的部分不會放入 `text`
- 子元素與文字混合時，文字和子元素的先後順序會遺失（`<p>a<b>x</b>c</p>` 的 `text` 為 `ac`）
- 註解、處理指令、DOCTYPE、XML 宣告都會忽略。根元素以外的內容也不會傳回
- 不保留屬性的順序，而是依照雜湊鍵的順序排列

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| path 不是字串 | W0009 | 9 |
| charset 無效 | W0012 / W0009 | 12 / 9 |
| 無法開啟檔案 | W0025 | 25 |
| 無法以 XML 格式解析 | W0026（也會輸出錯誤內容與行號） | 26 |

## Example
shop.xml:
```xml
<?xml version="1.0" encoding="Shift_JIS"?>
<shop name="A">
  <item id="1">りんご</item>
  <item id="2">バナナ</item>
</shop>
```

```
_x = FREADXML("shop.xml")
_x["name"]                          // shop
_x["attr"]["name"]                  // A
_x["children"][1]["name"]           // item
_x["children"][1]["attr"]["id"]     // 2
_x["children"][1]["text"]           // バナナ

foreach _x["children"]; _item {
    // _item["attr"]["id"] と _item["text"] を順に扱える
}
```

## Compatibility
- YAYA：Tc601-1 以後
- Tc603-1：傳入未知的字元編碼名稱時，改為顯示警告 W0012 並以失敗告終（此前不會顯示警告，而是以 OS 預設值處理）

## See Also
- [PARSEXML](PARSEXML.md)
- [FWRITEXML](FWRITEXML.md)
- [FREADHTML](FREADHTML.md)
- [FREADJSON](FREADJSON.md)
- [巢狀值與多維指派](../grammar/13-nesting.md)
