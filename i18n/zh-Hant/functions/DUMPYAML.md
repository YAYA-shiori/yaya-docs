# DUMPYAML
**Category:** 型取得/変換

## Signature
```
DUMPYAML( value [, pretty] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| value | 要轉換為 YAML 的值。雜湊或陣列（包含巢狀結構）也可以作為一個引數傳入 |
| pretty | 1 表示使用區塊格式（以縮排表示結構，便於閱讀和編輯），0 表示使用單行的流程格式。省略時為 1 |

## Returns
- 成功時：YAML 字串
- 沒有引數時：空字串

## Description
將值轉換為 YAML 字串並傳回。這是 [PARSEYAML](PARSEYAML.md) 的反向轉換。

與 [DUMPJSON](DUMPJSON.md) / [DUMPXML](DUMPXML.md) 不同，省略 pretty 時會進行格式化（1）。

### 值的對應方式

| YAYA | YAML |
|------|------|
| 雜湊 | 對應。鍵會轉換為字串（`1` 會變成 `"1"`）。順序依照雜湊鍵的順序 |
| 通用陣列 | 序列 |
| 整數 | 整數。64bit 整數也會精確寫入 |
| 實數 | 實數。一定會加上小數點（`1.0`、`0.1`、`1.0e+300`）。NaN 為 `.nan`，無限大為 `.inf` / `-.inf` |
| 字串 | 字串（如下所述） |
| 空值（VOID） | `null` |

- 整數的 1 / 0 會變成 `1` / `0`，不會變成 `true` / `false`
- 小數點一律使用 `.`，不受地區設定影響

字串若可直接寫入並在讀回時得到相同字串，就不會加上引號；否則會以 `"..."` 括住。以下列出的字串會以 `"..."` 括住。

- 會被讀取為數值、布林值或 null 的字串（`"123"` `"1.5"` `"true"` `"null"` `"~"`）
- 可能會被其他實作（YAML 1.1）讀取為數值或布林值的字串（`"yes"` `"no"` `"on"` `"off"` `"0x1F"` `"2001-12-14"` `"12:30"`）
- 空字串、開頭或結尾有空白的字串，以及以符號（`- ? : , [ ] { } # & * ! | > ' " % @` 和 `` ` ``）開頭的字串
- 含有 `: ` 或 ` #`，或含有控制字元（例如定位字元）的字串

在 `"..."` 中，只會跳脫 `"` `\` 和控制字元（換行會寫成 `\n`）。日文等非 ASCII 字元會照原樣寫入。

### 格式化方式（pretty 為 1）

- 使用兩個空格縮排，換行字元使用 LF。最後一行之後也會加上換行
- 序列會縮排在鍵之下，並以 `- ` 列出。序列元素若為雜湊或陣列，會接在 `- ` 之後書寫
- 空陣列和空雜湊會寫成 `[]` / `{}` 
- 含有換行的字串會使用區塊純量（`|`）。末尾沒有換行時使用 `|-`，有兩個以上換行時使用 `|+`。但若第一行以空白開頭、含有只有空白的行，或含有 CR 等控制字元，則會改用 `"..."`

pretty 為 0 時，會使用單行的流程格式（`{a: 1, b: [x, y]}`），且末尾不會加上換行。

使用 [PARSEYAML](PARSEYAML.md) 讀回時，會還原為原始值（無論使用哪種格式）。

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

DUMPYAML(_h)
// height: 158.5
// name: さくら
// tags:
//   - ghost
//   - shell

DUMPYAML(_h, 0)
// {height: 158.5, name: さくら, tags: [ghost, shell]}

DUMPYAML(("a", 1))          // "- a" + 改行 + "- 1" + 改行
DUMPYAML("123", 0)          // "123"（数値と区別するためクォートされる）
DUMPYAML(未定義の変数, 0)    // null
```

## Compatibility
- YAYA: Tc602-5 以後

## See Also
- [FWRITEYAML](FWRITEYAML.md)
- [PARSEYAML](PARSEYAML.md)
- [DUMPJSON](DUMPJSON.md)
- [DUMPTOML](DUMPTOML.md)
