# DESERIALIZEVAR
**Category:** メタ操作・特殊関数

## Signature
```
DESERIALIZEVAR( name, text )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 還原目標變數名稱的字串。若以 `_` 開頭，則為區域變數；否則為全域變數。若變數不存在，則建立變數 |
| text | [SERIALIZEVAR](SERIALIZEVAR.md) 傳回格式的字串 |

## Returns
還原成功時為 1。若 `text` 無法讀取為格式，或引數無效，則為 0（不會對變數進行任何操作）。

## Description
將 `text` 解讀為 [SAVEVAR](SAVEVAR.md#保存形式) 寫入存檔檔案的值格式，並存入 `name` 指定的變數。變數原本的值會被取代，型別也會由 `text` 的內容決定（整數 / 實數 / 字串 / 陣列 / 雜湊）。

與 [LETTONAME](LETTONAME.md) 相同，不會呼叫變數所設定的 setter / watcher。分隔符以及 setter / watcher / destorier 的設定不會變更。

下列情況會發出警告並傳回 0，且不會建立或變更變數。

| 情況 | 警告 |
|------|------|
| 引數不足 | W0008 |
| `name` 或 `text` 不是字串 | W0009 |
| `name` 是空字串 | W0010 |
| `name` 不能作為變數名稱使用（包含 `,`、與系統函式或保留字同名等） | W0012 |
| `text` 無法讀取為格式（空字串、沒有雙引號的字串、沒有 `:` 的陣列、只有 `IVOID` 的值等） | W0026 |

## Example
```
a = (1, "x", 2.5)
_s = SERIALIZEVAR("a")
_r = DESERIALIZEVAR("b", _s)   // b が (1, "x", 2.5) になる。_r は 1

DESERIALIZEVAR("n", "0.5")     // n が実数 0.5 になる
DESERIALIZEVAR("m", "abc")     // 0。警告 W0026
```

還原至區域變數：

```
_x = IARRAY
_x[0] = IHASH("k", 1)
_x[1] = "s"
_r = DESERIALIZEVAR("_y", SERIALIZEVAR("_x"))
// _y は _x と同じ入れ子の配列になる
```

## Compatibility
- Tc607-3 以後

## See Also
- SERIALIZEVAR
- SAVEVAR
- RESTOREVAR
- LETTONAME
- PARSEJSON
