# PARSEXML
**Category:** 型取得/変換

## Signature
```
PARSEXML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | XML の文字列 |

## Returns
- 成功時: ルート要素を表すハッシュ
- 失敗時: 空（VOID）

## Description
XML の文字列を解析し、ルート要素をハッシュにして返す。要素の形は [FREADXML](FREADXML.md#要素の形) と同じ。

文字列はすでに YAYA の文字列になっているので、XML 宣言の encoding は無視する。ファイルから読むときは [FREADXML](FREADXML.md) を使う。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| str が文字列でない | W0009 | 9 |
| XML として解析できない | W0026（エラーの内容と行番号も出力する） | 26 |

## Example
```
_x = PARSEXML('<res code="0"><msg>OK</msg></res>')
_x["attr"]["code"]              // 0（文字列）
_x["children"][0]["text"]       // OK

PARSEXML('<a><b></a>')          // 空（警告 W0026）
```

## Compatibility
- YAYA: Tc601-1以降

## See Also
- [FREADXML](FREADXML.md)
- [DUMPXML](DUMPXML.md)
- [PARSEHTML](PARSEHTML.md)
- [PARSEJSON](PARSEJSON.md)
