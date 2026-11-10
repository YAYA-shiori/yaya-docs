# SUBSTR
**Category:** 文字列操作

## Signature
```
SUBSTR(src, pos, len)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 取得元的字串 |
| pos | 取得開始位置（從 0 開始。負值表示從末尾算起的偏移量） |
| len | 要取得的字元數 |

## Returns
- 成功時：取得的子字串
- pos 超過字串長度時：空字串 `""`
- pos + len 超過字串末尾時：取得至末尾
- 發生錯誤時：VOID

## Description
從字串中取出子字串。指定負值給 `pos` 時，會將其視為從字串末尾算起的偏移量（例如：-2 表示從末尾數來第 2 個字元）。

## Example
```
SUBSTR("HOGE", -2, 1)  // 結果: "G"（末尾から2番目の文字）
```

## Compatibility
- YAYA：從初期版本起即可使用
- AYA：5.8 以後（但不支援負值 pos）

## See Also
- STRSTR（搜尋子字串）
- STRLEN（取得字串長度）
