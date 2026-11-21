# PARSEJSON
**Category:** 型取得/変換

## Signature
```
PARSEJSON( str [, key ...] )
```

## Parameters
| 參數 | 說明 |
|-----------|-------------|
| str | JSON 字串 |
| key | 要取出的鍵（可省略，可指定任意數量，Tc608-6 以後）。最上層為物件時，只傳回這些鍵的值（[指定鍵進行解析](#キーを指定して解析する)）。僅限字串 |

## Returns
- 成功時：轉換 JSON 所得的值
- 失敗時：空值（VOID）

## Description
解析 JSON 字串，並將其轉換為雜湊、陣列等值後傳回。值的對應方式及註解的處理方式與 [FREADJSON](FREADJSON.md#値の対応) 相同。

處理從 SAORI 或外部接收的 JSON 字串時使用。從檔案讀取時請使用 [FREADJSON](FREADJSON.md)。

### 指定鍵進行解析
指定 `key` 時，若最上層為物件，則只將這些鍵的值轉換成雜湊後傳回（Tc608-6 以後）。雖然仍會解析整個 JSON，但結果轉換（字串轉換與雜湊建立）只需處理指定的鍵，因此只使用包含長字串或大型巢狀結構的 JSON 中一部分資料時，速度較快，結果也較小。

- 只能指定最上層的鍵，無法使用 `.` 指向下層（`"a.b"` 指的是名稱包含 `.` 的鍵）
- JSON 中不存在的鍵也不會在結果雜湊中建立。值為 `null` 的鍵與轉換整體時相同，會以 VOID 值保留
- 若最上層不是物件，則不使用 `key`，而是轉換整體
- 鍵也可以用陣列傳入（作為函式引數時，外層陣列會被展開）
- 若要讀取每行包含一個 JSON 的檔案，使用 [FREADJSONL](FREADJSONL.md) 會更快

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| str 不是字串。key 不是字串 | W0009 | 9 |
| 無法解析為 JSON | W0026 | 26 |

## Example
```
_j = PARSEJSON('{"result": [{"id": 1, "text": "こんにちは"}]}')
_j["result"][0]["text"]     // こんにちは
_j["result"][0]["id"]       // 1

PARSEJSON('[1, 2.5, "a"]')  // 整数 1、実数 2.5、文字列 a の汎用配列
PARSEJSON('{')              // 空（警告 W0026）

_j = PARSEJSON('{"a": 1, "b": [1, 2], "c": {"d": 4}}', "a", "c")   // Tc608-6 以降。このキーだけのハッシュ
_j["c"]["d"]                // 4
HASH_EXIST("b", _j)         // 0（取り出していない）
```

## Compatibility
- YAYA：Tc601-1 以後
- Tc602-1：修正了在小數點為 `,` 的地區設定（如德語）環境中，解析含小數的 JSON 時失敗的問題
- Tc608-6：可在 `str` 之後指定要取出的鍵

## See Also
- [FREADJSON](FREADJSON.md)
- [FREADJSONL](FREADJSONL.md)
- [DUMPJSON](DUMPJSON.md)
- [PARSEXML](PARSEXML.md)
