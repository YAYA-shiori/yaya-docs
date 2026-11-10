# FREADHTML
**Category:** ファイル操作

## Signature
```
FREADHTML( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要讀取的 HTML 檔案路徑（相對於 yaya.dll 的路徑，或絕對路徑） |
| charset | 檔案的字元編碼（可省略）。以字串（`"UTF-8"` `"Shift_JIS"` 等。[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）或數值指定。省略時會依下方說明自動決定 |

## Returns
- 成功時：代表 `<html>` 元素的雜湊（如下方的 [元素格式](#要素の形)）
- 失敗時：空值（VOID）

## Description
讀取並解析整份 HTML 檔案，將 `<html>` 元素轉換為雜湊後傳回。不需要先使用 [FOPEN](FOPEN.md) 開啟。

HTML 解析使用 [Gumbo](https://github.com/ponapalt/gumbo-parser-mirror)（遵循 HTML5 語法解析規則的剖析器）。即使缺少結束標籤或巢狀結構錯誤，也會依照與瀏覽器相同的規則補齊並建立樹狀結構，因此解析本身不會失敗。若缺少 `<html>`、`<head>`、`<body>`，也會自動補上。

省略 charset 時，會依下列順序決定字元編碼。

1. 若開頭有 UTF-8 BOM，則使用 UTF-8
2. 開頭 1024 位元組內的 `<meta charset="Shift_JIS">`，或 `<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">` 所指定的字元編碼。不會讀取註解中的內容。`Windows-31J`、`CP932` 也會視為 Shift_JIS
3. 若兩者皆無，或 YAYA 不認識該字元編碼（包括 `UTF-16`），則使用 UTF-8

指定 charset 時會忽略 `<meta>`。

### 元素格式

與 [FREADXML](FREADXML.md#要素の形) 相同，元素會成為具有以下 4 個鍵的雜湊。即使內容為空，這些鍵也一定存在。

| 鍵 | 值 |
|------|----|
| `name` | 標籤名稱（HTML 元素為小寫，例如 `div`、`custom-tag`） |
| `attr` | 屬性名稱 → 屬性值的雜湊。值全部都是字串。屬性名稱會轉為小寫 |
| `children` | 子元素雜湊的通用陣列（依出現順序排列） |
| `text` | 依序串接直接位於該元素中的文字所形成的字串 |

- 字元參照（例如 `&amp;`、`&#x3042;`、`&nbsp;`）會先展開
- `<br>`、`<img>` 等沒有內容的元素，也會成為 `children` 和 `text` 均為空的元素
- 子元素和文字混合時，文字與子元素的前後關係會遺失（`<p>a<b>x</b>c</p>` 的 `text` 為 `ac`）
- 含有子元素的元素中，只有空白的文字（元素之間的換行或縮排）不會放入 `text`。沒有子元素的元素即使只有空白也會保留（`<pre> </pre>` 的 `text` 為半形空格）
- `<script>`、`<style>`、`<textarea>` 的內容也會放入 `text`
- 註解、DOCTYPE、處理指令會忽略
- SVG、MathML 中的 `xlink:href`、`xml:lang` 等屬性會使用含前綴的名稱
- 巢狀層數超過 128 層的 HTML 會失敗（以 `<html>` 為第 1 層）
- 不會保留屬性的排列順序，而會依照雜湊鍵的順序排列

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| path 不是字串 | W0009 | 9 |
| charset 無效 | W0012 / W0009 | 12 / 9 |
| 無法開啟檔案 | W0025 | 25 |
| 巢狀層數過深 | W0026（也會輸出原因） | 26 |

## Example
page.html:
```html
<!DOCTYPE html>
<html>
<head><meta charset="Shift_JIS"><title>お知らせ</title></head>
<body>
<h1>お知らせ</h1>
<ul>
  <li><a href="a.html">その1</a></li>
  <li><a href="b.html">その2</a></li>
</ul>
</body>
</html>
```

```
_h = FREADHTML("page.html")
_h["children"][0]["children"][1]["text"]     // お知らせ（<title>。[0] は <meta>）
_body = _h["children"][1]
_body["children"][0]["text"]                 // お知らせ（<h1>）
_ul = _body["children"][1]
foreach _ul["children"]; _li {
    _a = _li["children"][0]
    // _a["attr"]["href"] と _a["text"] を順に扱える
}
```

## Compatibility
- YAYA：Tc605-1以後

## See Also
- [PARSEHTML](PARSEHTML.md)
- [FREADXML](FREADXML.md)
- [FREADJSON](FREADJSON.md)
- [巢狀值與多維指派](../grammar/13-nesting.md)
