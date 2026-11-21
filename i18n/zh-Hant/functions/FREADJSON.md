# FREADJSON
**Category:** ファイル操作

## Signature
```
FREADJSON( path [, charset [, key ...]] )
```

## Parameters
| 參數 | 說明 |
|-----------|-------------|
| path | 要讀取的 JSON 檔案路徑（相對於 yaya.dll 的路徑，或絕對路徑） |
| charset | 檔案的字元編碼（可省略）。以字串（例如 `"UTF-8"`、`"Shift_JIS"`；參閱[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）或數值指定。省略時為 UTF-8 |
| key | 要擷取的鍵（可省略，可指定任意數量；Tc608-6 以後）。最上層為物件時，只傳回該鍵的值（[指定鍵讀取](#キーを指定して読む)）。僅限字串。指定時也須填寫 `charset`（例如 `"UTF-8"`） |

## Returns
- 成功時：轉換 JSON 後的值（見下方的[值的對應關係](#値の対応)）
- 失敗時：空（VOID）

## Description
讀取並解析整個 JSON 檔案，轉換為雜湊、陣列等值後傳回。不需要事先用 [FOPEN](FOPEN.md) 開啟。

JSON 解析使用 [parson](https://github.com/kgabis/parson)。

- 忽略開頭的 UTF-8 BOM
- 可以寫入 `/* */` 和 `//` 註解（雖不符合 JSON 標準，但為了讓設定檔等用途能夠使用而允許）
- 最上層不一定要是物件或陣列（也能讀取只有 `123` 或 `"abc"` 的檔案）

### 值的對應關係

| JSON | YAYA |
|------|------|
| 物件 | 雜湊 |
| 陣列 | 通用陣列（元素可包含陣列或雜湊，形成巢狀結構） |
| 字串 | 字串 |
| 數值（整數值） | 整數 |
| 數值（其他） | 實數 |
| `true` / `false` | 整數 1 / 0 |
| `null` | 空（VOID） |

- 數值在內部會以實數解析，因此即使有小數點，如 `1.0`，只要值是整數就會轉為整數。此外，超過 2^53 的整數可能含有誤差。超出整數範圍（-2^63 以上、未滿 2^63）的值會轉為實數
- 物件的鍵不會保留原有順序，而是依雜湊的鍵順序排列（數值 < 字串）（參閱 [HASH_KEYS](HASH_KEYS.md)）
- 如 `"1"` 和 `"01"` 這類在 YAYA 雜湊中不被視為相同的鍵，仍會保留為不同的鍵。像 `"1"` 這類正規形式的整數字串鍵，既可用 `h[1]` 也可用 `h["1"]` 查取
- 值為 `null` 的鍵也會保留在雜湊中。[HASH_EXIST](HASH_EXIST.md) 會傳回 1

### 指定鍵讀取
指定 `key` 時，若最上層為物件，只會將該鍵的值組成雜湊並傳回（Tc608-6 以後）。雖然會解析整個 JSON 檔案，但只需轉換指定鍵的結果（字串轉換與雜湊建立），因此只使用大型 JSON 的一部分時速度較快，結果也較小。

- 僅支援最上層的鍵。無法用 `.` 指向下層（`"a.b"` 指的是名稱中含有 `.` 的鍵）
- 檔案中不存在的鍵也不會建立於結果雜湊中。值為 `null` 的鍵則與轉換整體時相同，以 VOID 值保留
- 最上層若不是物件，則不使用 `key`，而是轉換整體
- 鍵也可以用陣列傳入（函式引數中，外層陣列會被展開）

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| path 不是字串。key 不是字串 | W0009 | 9 |
| charset 無效 | W0012 / W0009 | 12 / 9 |
| 無法開啟檔案 | W0025 | 25 |
| 無法解析為 JSON | W0026 | 26 |

## Example
data.json:
```json
{
  "name": "さくら",
  "age": 17,
  "tags": ["ghost", "shell"],
  "profile": { "height": 158.5, "visible": true, "memo": null }
}
```

```
_j = FREADJSON("data.json")
_j["name"]                  // さくら
_j["tags"][1]               // shell
_j["profile"]["height"]     // 実数の 158.5
_j["profile"]["visible"]    // 1

foreach _j["tags"]; _t {
    // _t に "ghost"、"shell" が順に入る
}

_j = FREADJSON("data.json", "UTF-8", "name", "tags")   // Tc608-6 以降。このキーだけのハッシュ
_j["name"]                  // さくら
HASH_EXIST("age", _j)       // 0（取り出していない）
```

## Compatibility
- YAYA: Tc601-1 以後
- Tc602-1: 修正小數點為 `,` 的地區設定（如德文）環境中，含小數的 JSON 解析失敗的問題
- Tc603-1: 傳入未知的字元編碼名稱時，會輸出警告 W0012 並失敗（此前不會輸出警告，而是視為 OS 預設值）
- Tc608-6: 可以在 `charset` 之後指定要擷取的鍵

## See Also
- [FREADJSONL](FREADJSONL.md)
- [PARSEJSON](PARSEJSON.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FREADXML](FREADXML.md)
- [值的巢狀結構與多維指派](../grammar/13-nesting.md)
