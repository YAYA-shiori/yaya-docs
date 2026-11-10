# FREADJSON
**Category:** ファイル操作

## Signature
```
FREADJSON( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要讀取的 JSON 檔案路徑（相對於 yaya.dll 的路徑，或絕對路徑） |
| charset | 檔案的字元編碼（可省略）。以字串（例如 `"UTF-8"`、`"Shift_JIS"`。[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）或數值指定。省略時使用 UTF-8 |

## Returns
- 成功時：將 JSON 轉換後的值（見下方的[值的對應](#値の対応)）
- 失敗時：空（VOID）

## Description
讀取並解析整個 JSON 檔案，轉換成雜湊、陣列等值後傳回。不必先用 [FOPEN](FOPEN.md) 開啟檔案。

JSON 解析使用 [parson](https://github.com/kgabis/parson)。

- 忽略開頭的 UTF-8 BOM
- 可以使用 `/* */` 和 `//` 註解（雖然不符合 JSON 規格，但為了讓設定檔等用途也能使用而予以允許）
- 最上層不必是物件或陣列（也能讀取只有 `123` 或 `"abc"` 的檔案）

### 值的對應

| JSON | YAYA |
|------|------|
| 物件 | 雜湊 |
| 陣列 | 通用陣列（可包含陣列或雜湊，形成巢狀結構） |
| 字串 | 字串 |
| 數值（整數值） | 整數 |
| 數值（其他） | 實數 |
| `true` / `false` | 整數 1 / 0 |
| `null` | 空（VOID） |

- 數值會在內部以實數解析，因此即使有小數點，例如 `1.0`，只要值是整數就會成為整數。此外，超過 2^53 的整數可能會有誤差。超出整數範圍（大於等於 -2^63 且小於 2^63）的值會成為實數
- 不保留物件鍵的順序，而是依照雜湊鍵的順序（數值 < 字串）（參閱 [HASH_KEYS](HASH_KEYS.md)）
- `"1"` 和 `"01"` 等在 YAYA 雜湊中不會被視為相同鍵的項目，會保留為不同的鍵。像 `"1"` 這種標準形式的整數字串鍵，可用 `h[1]` 或 `h["1"]` 取得
- 鍵值為 `null` 的項目也會保留在雜湊中。[HASH_EXIST](HASH_EXIST.md) 會傳回 1

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| path 不是字串 | W0009 | 9 |
| charset 無效 | W0012 / W0009 | 12 / 9 |
| 無法開啟檔案 | W0025 | 25 |
| 無法以 JSON 格式解析 | W0026 | 26 |

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
```

## Compatibility
- YAYA：Tc601-1 以後
- Tc602-1：修正了在小數點符號為 `,` 的地區設定環境（例如德語）中，無法解析含有小數的 JSON 的問題
- Tc603-1：傳入未知的字元編碼名稱時，改為顯示警告 W0012 並以失敗告終（此前不會顯示警告，而是以 OS 預設值處理）

## See Also
- [PARSEJSON](PARSEJSON.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FREADXML](FREADXML.md)
- [巢狀值與多維指派](../grammar/13-nesting.md)
