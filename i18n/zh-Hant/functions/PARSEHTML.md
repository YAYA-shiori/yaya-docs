# PARSEHTML
**Category:** 型取得/変換

## Signature
```
PARSEHTML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | HTML 字串 |

## Returns
- 成功時：代表 `<html>` 元素的雜湊
- 失敗時：空（VOID）

## Description
解析 HTML 字串，並以雜湊形式傳回 `<html>` 元素。元素的結構和解析規則與 [FREADHTML](FREADHTML.md#要素の形) 相同。

由於字串已經是 YAYA 字串，因此會忽略 `<meta charset>`。從檔案讀取時請使用 [FREADHTML](FREADHTML.md)。

即使傳入的不是完整 HTML，而是其中一部分（例如 `<p>a</p>`），也會補上 `<html>`、`<head>`、`<body>`，形成樹狀結構。部分內容可從 `<body>` 的 `children` 取出。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| str 不是字串 | W0009 | 9 |
| 巢狀層數過深（超過 128 層） | W0026（也會輸出原因） | 26 |

## Example
```
_h = PARSEHTML('<p class=a>x<b>y</b>z<br><img src="a.png" alt="&amp;"></p>')
_h["name"]                                   // html
_body = _h["children"][1]
_p = _body["children"][0]
_p["attr"]["class"]                          // a
_p["text"]                                   // xz
_p["children"][0]["text"]                    // y
_p["children"][2]["attr"]["alt"]             // &
```

## Compatibility
- YAYA: Tc605-1 以後

## See Also
- [FREADHTML](FREADHTML.md)
- [PARSEXML](PARSEXML.md)
- [PARSEJSON](PARSEJSON.md)
