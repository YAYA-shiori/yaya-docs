# GETTYPE
**Category:** 型取得/変換

## Signature
```
GETTYPE( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 要檢查型別的值、變數或運算式 |

## Returns
- 0：內部錯誤（失敗）
- 1：整數
- 2：浮點數
- 3：字串
- 4：通用陣列
- 5：雜湊（Tc600-3 以後）

## Description
取得指定值的資料型別。

為了向後相容，此函式有一項特殊行為：「元素數為 1 的通用陣列會傳回其第一個（也是唯一一個）元素的型別」。若要正確檢查元素數為 1 的通用陣列型別，建議使用 `GETTYPEEX`。

唯一元素是陣列或雜湊（[巢狀結構](../grammar/13-nesting.md)）時，也會採用相同的行為，分別傳回 4 和 5。

```
GETTYPE(PARSEJSON('[[1,2]]'))     // 4
GETTYPE(PARSEJSON('[{"a":1}]'))   // 5
```

## Compatibility
- YAYA：從初期版本起即可使用
- AYA：5.8 以後
- Tc600-3：雜湊型別改為傳回 5
- Tc602-10：修正元素數為 1 的通用陣列中，唯一元素是陣列或雜湊時會傳回 0 的問題（改為傳回 4 或 5）

## See Also
- GETTYPEEX
- IHASH
