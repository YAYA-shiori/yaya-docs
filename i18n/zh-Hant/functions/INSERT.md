# INSERT
**Category:** 文字列操作

## Signature
```
INSERT( src , pos , insert )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 插入位置所在的原始字串 |
| pos | 插入位置（0=開頭）。指定負值時，會視為從末尾起算的偏移量（Tc574-8 / Tc603-1 以後） |
| insert | 要插入的字串 |

## Returns
- 成功時：插入後的字串
- 發生錯誤時：VOID

## Description
在字串 `src` 中，由 `pos` 指定的位置插入字串 `insert`。位置 0 代表字串開頭。

`pos` 為負值時，會在 `src` 的字元數加上該值所得的位置插入（-1 表示倒數第 1 個字元之前）。若結果仍為負值，則插入在開頭；若大於 `src` 的字元數，則插入在末尾。

```
INSERT('abc', 1, 'X')    // aXbc
INSERT('abc', -1, 'X')   // abXc
INSERT('abc', 10, 'X')   // abcX
INSERT('abc', -10, 'X')  // Xabc
```

## Compatibility
- YAYA: 從初期版本起即可使用
- AYA: 5.8 以後
- Tc574-8 / Tc603-1：改為從末尾起算負的位置，並將超出範圍的位置調整至開頭或末尾（此前會發生錯誤並中斷處理）。`insert` 傳入數值時也會插入該數值（此前不會插入任何內容）
