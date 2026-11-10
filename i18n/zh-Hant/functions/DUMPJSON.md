# DUMPJSON
**Category:** 型取得/変換

## Signature
```
DUMPJSON( value [, pretty] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| value | 要轉換為 JSON 的值。雜湊或陣列（包含巢狀結構）也可以作為單一引數傳入 |
| pretty | 為 1 時加入換行和縮排以美化格式。省略時為 0（輸出成單行） |

## Returns
- 成功時：JSON 字串
- 沒有引數時：空字串

## Description
將值轉換為 JSON 字串並傳回。這是 [PARSEJSON](PARSEJSON.md) 的反向轉換。

### 值的對應

| YAYA | JSON |
|------|------|
| 雜湊 | 物件。鍵會轉換為字串（`1` 會變成 `"1"`）。順序依照雜湊鍵的順序 |
| 通用陣列 | 陣列 |
| 整數 | 數值。64 位元整數也會以無誤差的方式寫入 |
| 實數 | 數值。一定會加上小數點或指數（`1.0`、`0.1`、`1e+300`） |
| 字串 | 字串 |
| 空（VOID） | `null` |

- 整數的 1 / 0 會變成數值 `1` / `0`，不會變成 `true` / `false`
- 實數會使用可讀回相同值的最短表示法。NaN 和無限大無法用 JSON 表示，因此會變成 `null`
- 字串只會跳脫 `"`、`\` 和控制字元（例如換行、定位字元）。日文等非 ASCII 字元和 `/` 會原樣寫入
- 小數點不受地區設定影響，一律使用 `.`

美化格式時，會使用 4 個空白縮排，並以 LF 換行。空陣列和空雜湊會分別合併為 `[]` / `{}`。

使用 [PARSEJSON](PARSEJSON.md) 讀回時，會還原為原本的值。但值為整數的實數（`1.0`）會變成整數。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |

## Example
```
_h = IHASH()
_h["name"] = "さくら"
_h["tags"] = ("ghost", "shell")
_h["height"] = 158.5

DUMPJSON(_h)
// {"height":158.5,"name":"さくら","tags":["ghost","shell"]}

DUMPJSON(_h, 1)
// {
//     "height": 158.5,
//     "name": "さくら",
//     "tags": [
//         "ghost",
//         "shell"
//     ]
// }

DUMPJSON(("a", 1))          // ["a",1]
DUMPJSON(未定義の変数)       // null
```

## Compatibility
- YAYA：Tc602-1 以後
- Tc602-5：修正了整數最小值（-9223372036854775808）只輸出成 `-`、造成 JSON 格式錯誤的問題

## See Also
- [FWRITEJSON](FWRITEJSON.md)
- [PARSEJSON](PARSEJSON.md)
- [DUMPXML](DUMPXML.md)
