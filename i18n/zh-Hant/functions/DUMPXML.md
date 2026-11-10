# DUMPXML
**Category:** 型取得/変換

## Signature
```
DUMPXML( element [, pretty] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| element | 表示根元素的雜湊（形狀與 [FREADXML](FREADXML.md#要素の形) 傳回的相同） |
| pretty | 為 1 時加入換行與縮排進行排版。省略時為 0（輸出為單行） |

## Returns
- 成功時：帶有 XML 宣告（`<?xml version="1.0" encoding="UTF-8"?>`）的 XML 字串
- 失敗時：空字串

## Description
將元素的雜湊轉換為 XML 字串並傳回。這是 [PARSEXML](PARSEXML.md) 的反向轉換。

元素雜湊的索引鍵如下。除了 `name` 以外，都可以省略（也可以是空值）。

| 索引鍵 | 值 |
|------|----|
| `name` | 標籤名稱（必要）。字串 |
| `attr` | 屬性名稱 → 屬性值的雜湊。值可為整數、實數或字串（會轉換為字串後寫入） |
| `children` | 子元素雜湊的通用陣列 |
| `text` | 元素的文字。整數、實數或字串 |

- 文字會寫在子元素之前。[FREADXML](FREADXML.md) 讀取的元素若同時包含文字與子元素（`<p>a<b>x</b>c</p>`），就無法還原成原本的順序（會變成 `<p>ac<b>x</b></p>`）
- `&`、`<`、`>` 以及屬性值中的 `"` 會進行跳脫
- 標籤名稱與屬性名稱只會針對 ASCII 範圍，依 XML 名稱規則檢查（開頭為英文字母、`_`、`:`，第二個字元起也可使用數字、`-`、`.`）。日文等非 ASCII 字元也可以使用

進行排版時會使用 4 個空白字元縮排，並以 LF 換行。即使在包含文字的元素中，第二個子元素起的前方也會加入換行與縮排。[FREADXML](FREADXML.md) / [PARSEXML](PARSEXML.md) 會忽略元素之間只包含空白的文字，因此不會影響讀回時的 `text`。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| 元素不是雜湊、沒有 `name` 或其值不正確、`attr` 不是雜湊、屬性名稱不正確、屬性值或 `text` 是陣列或雜湊、`children` 不是陣列、子元素不是雜湊 | W0027（也會輸出錯誤所在之處） | 27 |

## Example
```
_item = IHASH("name", "item", "text", "りんご")
_item["attr"] = IHASH("id", 1)
_shop = IHASH("name", "shop")
_shop["children"] = IARRAY()
_shop["children"] ,= _item

DUMPXML(_shop)
// <?xml version="1.0" encoding="UTF-8"?><shop><item id="1">りんご</item></shop>

DUMPXML(_shop, 1)
// <?xml version="1.0" encoding="UTF-8"?>
// <shop>
//     <item id="1">りんご</item>
// </shop>

DUMPXML(PARSEXML('<a x="1"><b/></a>'))
// <?xml version="1.0" encoding="UTF-8"?><a x="1"><b/></a>
```

## Compatibility
- YAYA：Tc602-1 以後

## See Also
- [FWRITEXML](FWRITEXML.md)
- [PARSEXML](PARSEXML.md)
- [DUMPJSON](DUMPJSON.md)
