# RAND
**Category:** 数学関数

## Signature
```
RAND([max])
```

## Parameters
| 引數 | 說明 |
|-----------|-------------|
| max | （可省略）亂數上限。會在 0 到 (max-1) 的範圍內產生亂數。省略時預設為 100（產生 0～99 的值） |

## Returns
- 成功：指定範圍內的隨機整數
- 失敗：0

## Description
取得整數亂數。此函式不需初始化種子即可單獨運作。也可以使用 SRAND 設定種子，但基本用法並不需要。

## Compatibility
- YAYA：自初次發行起即可使用
- AYA：自版本 5.8 起即可使用

## See Also
- SRAND
