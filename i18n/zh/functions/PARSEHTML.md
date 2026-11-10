# PARSEHTML
**Category:** 型取得/変換

## Signature
```
PARSEHTML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | HTML 字符串 |

## Returns
- 成功时：表示 `<html>` 元素的哈希
- 失败时：空（VOID）

## Description
解析 HTML 字符串，并将 `<html>` 元素作为哈希返回。元素的结构和解析规则与 [FREADHTML](FREADHTML.md#要素の形) 相同。

由于字符串已经是 YAYA 字符串，因此会忽略 `<meta charset>`。从文件读取时，请使用 [FREADHTML](FREADHTML.md)。

即使传入的不是完整 HTML，而是其中一部分（例如 `<p>a</p>`），也会补全 `<html>`、`<head>`、`<body>`，构成一棵树。可以从 `<body>` 的 `children` 中取出该部分内容。

### 错误
| 状况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| str 不是字符串 | W0009 | 9 |
| 嵌套过深（超过 128 层） | W0026（也会输出原因） | 26 |

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
- YAYA：Tc605-1 及更高版本

## See Also
- [FREADHTML](FREADHTML.md)
- [PARSEXML](PARSEXML.md)
- [PARSEJSON](PARSEJSON.md)
