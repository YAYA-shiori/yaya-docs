# SERIALIZEVAR
**Category:** メタ操作・特殊関数

## Signature
```
SERIALIZEVAR( name )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 變數名稱字串。若以 `_` 開頭，則為區域變數；否則為全域變數 |

## Returns
將變數的值轉換為與存檔檔案中的值相同格式的字串。

變數不存在、值為 VOID，或變數已透過 [ERASEVAR](ERASEVAR.md) 刪除時，會發出警告 W0012 並傳回 VOID。

## Description
將指定變數的值轉換為與 [SAVEVAR](SAVEVAR.md#保存形式) 寫入存檔檔案時相同格式的字串。傳入 [DESERIALIZEVAR](DESERIALIZEVAR.md) 後，即可將相同的值還原至其他變數。

存檔檔案中的一行格式為 `變數名,値,"デリミタ",watcher|setter|destorier`，但此函式傳回的**只有值的部分**。不包含變數名稱、分隔符號、watcher / setter / destorier，也不包含字元編碼指定。

與 JSON 不同，此格式會保留整數與實數、整數鍵與字串鍵、VOID 與空字串等值之間的區別。巢狀陣列與雜湊也會以 `IARRAY{...}` / `IHASH{...}` 的形式直接輸出。

傳回的字串只有一行，換行等控制字元會經過跳脫。

## Example
```
a = 5
b = "x,y"
c = (1, "x", 2.5)
d = IHASH("k", 1)

SERIALIZEVAR("a")   // 5
SERIALIZEVAR("b")   // "x,y"（ダブルクォートを含む）
SERIALIZEVAR("c")   // 1:"x":2.5
SERIALIZEVAR("d")   // "k"=1:IHASH=IHASH
```

也可以指定區域變數。

```
_x = IARRAY
_x[0] = IHASH("k", 1)
_x[1] = "s"
_s = SERIALIZEVAR("_x")   // IHASH{"k"=1:IHASH=IHASH}:"s"
```

## Compatibility
- Tc607-3 以後

## See Also
- DESERIALIZEVAR
- SAVEVAR
- RESTOREVAR
- DUMPJSON
