# IHASH
**Category:** ハッシュ操作

## Signature
```
IHASH( [key1, value1, key2, value2, ...] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key*n* | 鍵 |
| value*n* | 對應於 key*n* 的值 |

## Returns
雜湊。未提供引數時會傳回空雜湊。

## Description
依序交錯排列鍵和值，以建立雜湊。

- 引數中的通用陣列會如同其他函式一樣展開。`IHASH("x", (1,2,3))` 與 `IHASH("x",1,2,3)` 相同，會成為 `x=1`、`2=3` 這兩個元素。若要將陣列放入雜湊的值中，請在建立雜湊後再指派給元素（`_h["x"] = (1,2,3)`）
- 將雜湊傳入引數時，不會展開，而會直接成為鍵或值（巢狀）
- 引數數量為奇數時，會發出警告 W0020，最後一個鍵的值會是 VOID
- 被視為相同鍵的項目出現兩次以上時，會保留最先出現的鍵和值

鍵的比對與排列順序規則，請參閱[雜湊](../grammar/12-hash.md)。

## Example
```
_h = IHASH("name", "さくら", "age", 16)
_h["name"]              // "さくら"

_e = IHASH()            // 空のハッシュ
_e["k"] = (1, 2, 3)     // 値に配列を入れる

IHASH(9, "i9", "9", "s9")   // 9 と "9" は同じキーなので 9=i9 だけ
```

## Compatibility
- YAYA: Tc600-3 以後

## See Also
- HASH_SPLIT
- HASH_KEYS
- HASH_VALUES
- HASH_EXIST
- HASH_SIZE
- IARRAY
