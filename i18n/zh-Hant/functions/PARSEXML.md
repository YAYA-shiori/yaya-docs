# PARSEXML
**Category:** 型取得/変換

## Signature
```
PARSEXML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | XML 字串 |

## Returns
- 成功時：代表根元素的雜湊
- 失敗時：空（VOID）

## Description
解析 XML 字串，並以雜湊形式傳回根元素。元素的結構與 [FREADXML](FREADXML.md#要素の形) 相同。

由於字串已經是 YAYA 字串，因此會忽略 XML 宣告中的 encoding。從檔案讀取時請使用 [FREADXML](FREADXML.md)。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| str 不是字串 | W0009 | 9 |
| 無法解析為 XML | W0026（也會輸出錯誤內容和行號） | 26 |

## Example
```
_x = PARSEXML('<res code="0"><msg>OK</msg></res>')
_x["attr"]["code"]              // 0（文字列）
_x["children"][0]["text"]       // OK

PARSEXML('<a><b></a>')          // 空（警告 W0026）
```

## Compatibility
- YAYA: Tc601-1 以後

## See Also
- [FREADXML](FREADXML.md)
- [DUMPXML](DUMPXML.md)
- [PARSEHTML](PARSEHTML.md)
- [PARSEJSON](PARSEJSON.md)
