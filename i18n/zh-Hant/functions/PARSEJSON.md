# PARSEJSON
**Category:** 型取得/変換

## Signature
```
PARSEJSON( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | JSON 字串 |

## Returns
- 成功時：轉換 JSON 後的值
- 失敗時：空（VOID）

## Description
解析 JSON 字串，並轉換成雜湊、陣列等值後傳回。支援的值及註解處理方式與 [FREADJSON](FREADJSON.md#値の対応) 相同。

用於處理從 SAORI 或外部接收的 JSON 字串。從檔案讀取時請使用 [FREADJSON](FREADJSON.md)。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| str 不是字串 | W0009 | 9 |
| 無法解析為 JSON | W0026 | 26 |

## Example
```
_j = PARSEJSON('{"result": [{"id": 1, "text": "こんにちは"}]}')
_j["result"][0]["text"]     // こんにちは
_j["result"][0]["id"]       // 1

PARSEJSON('[1, 2.5, "a"]')  // 整数 1、実数 2.5、文字列 a の汎用配列
PARSEJSON('{')              // 空（警告 W0026）
```

## Compatibility
- YAYA: Tc601-1 以後
- Tc602-1：修正了在小數點符號為 `,` 的語系（例如德語）環境中，解析包含小數的 JSON 會失敗的問題

## See Also
- [FREADJSON](FREADJSON.md)
- [DUMPJSON](DUMPJSON.md)
- [PARSEXML](PARSEXML.md)
