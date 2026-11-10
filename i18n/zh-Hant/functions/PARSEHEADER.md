# PARSEHEADER
**Category:** 型取得/変換

## Signature
```
PARSEHEADER( str [, conv ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | HTTP 或 SHIORI 等標頭格式的字串 |
| conv | 可省略。若非 0，則依照與 [TOAUTOEX](TOAUTOEX.md) 相同的規則，將值轉換為整數或實數。省略時為 0（不轉換） |

## Returns
- 成功時：包含下列索引鍵的雜湊
- 失敗時：空（VOID）

| 索引鍵 | 內容 |
|------|------|
| `start` | 起始行（例如 `GET SHIORI/3.0` 或 `HTTP/1.1 200 OK`）。若沒有起始行則為空字串 |
| `header` | 標頭的索引鍵→值雜湊。若有多個相同索引鍵，則保留較後出現的值 |
| `key` | 標頭索引鍵的陣列（依出現順序，包含重複項目） |
| `value` | 標頭值的陣列（依出現順序）。若 `conv` 非 0，則為轉換後的值 |
| `rawvalue` | 轉換前的值（字串）陣列（依出現順序） |
| `body` | 空行之後的字串。若沒有空行則為空字串 |

## Description
解析 HTTP 或 SHIORI、SAORI、SSTP 的請求／回應等「起始行 + `索引鍵: 值` 行 + 空行 + 本文」形式的字串，並整理成雜湊和陣列後傳回。比逐行使用 [STRSTR](STRSTR.md) 或 [SUBSTR](SUBSTR.md) 擷取更快。

- 換行可以是 CRLF 或 LF
- 標頭在第一個空行結束，其後的所有內容都會成為 `body`
- 每行以第一個 `:` 分隔索引鍵和值。值會略過 `:` 後的一個空白字元（空格或定位字元），其餘空白則原樣保留（`Key:  a` 的值為 ` a`）
- 第一個 `:` 之前為空，或包含空白字元的行，不會視為標頭行。若這種情況出現在第 1 行，則會作為起始行放入 `start`；若出現在第 2 行以後則會忽略。因此也可以解析沒有起始行、只有標頭的字串
- 索引鍵會區分大小寫
- 將 `conv` 設為非 0 時，會依照與 [TOAUTOEX](TOAUTOEX.md) 相同的規則轉換；只有在轉回字串後與原字串相同時才會轉換。`12` 會成為整數，但 `007` 和 `1.5` 會維持字串

`header` 雜湊會依索引鍵排序；若需要取得出現順序，請使用 `key` / `value` / `rawvalue`。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| str 不是字串 | W0009 | 9 |

## Example
```
request
{
	_r = PARSEHEADER(_argv[0], 1)
	// _argv[0] が
	//   GET SHIORI/3.0
	//   Charset: UTF-8
	//   ID: OnBoot
	//   Reference0: 12
	//   Reference1: 007
	// のとき

	_r["start"]                 // GET SHIORI/3.0
	_r["header"]["ID"]          // OnBoot
	_r["header"]["Reference0"]  // 12（整数）
	_r["header"]["Reference1"]  // 007（文字列）
	_r["key"]                   // Charset,ID,Reference0,Reference1
	_r["rawvalue"][2]           // 12（文字列）
}
```

```
_nl = CHR(13) + CHR(10)
_r = PARSEHEADER('HTTP/1.1 200 OK' + _nl + 'Content-Type: text/plain' + _nl + _nl + 'hello')
_r["start"]                     // HTTP/1.1 200 OK
_r["header"]["Content-Type"]    // text/plain
_r["body"]                      // hello
```

在與 500 系共用的辭典中，可以使用 `#ifdef __AYA_SYSTEM_SYSFUNC_PARSEHEADER__` 判斷是否可用，並據此撰寫不同內容（[前處理](../grammar/08-preprocessor.md#500-系と-600-系で共用する辞書)）。

## Compatibility
- YAYA: Tc602-3 以後

## See Also
- [TOAUTOEX](TOAUTOEX.md)
- [HASH_SPLIT](HASH_SPLIT.md)
- [PARSEJSON](PARSEJSON.md)
- [SPLIT](SPLIT.md)
