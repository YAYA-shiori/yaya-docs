# LOGGING
**Category:** デバッグ

## Signature
```
LOGGING(var)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 要寫入記錄的值。可指定任意型別 |

## Returns
VOID（沒有傳回值）

## Description
將指定的值寫入記錄檔，同時顯示在偵錯工具「玉」中。可接受任意資料型別。

簡易陣列會以逗號連接各值後輸出。

## 出力形式

有多個引數或傳入陣列時，會以逗號分隔各值並寫入同一行。字串會以 `"` 括住。

```
LOGGING('a', 1, 2.5)   // "a",1,2.500000
```

值包含陣列或雜湊時（Tc602-8 以後），陣列會以 `( )` 括住，雜湊會以 `{ }` 括住，雜湊元素會以 `鍵=值` 的形式寫入。巢狀結構也會依照相同規則輸出，因此可以辨別巢狀層級。

```
_h = PARSEJSON('{"l":[1,2],"m":{"x":"a"}}')
LOGGING(_h)                           // {"l"=(1,2),"m"={"x"="a"}}
LOGGING(PARSEJSON('[[1,[2,"s"]],3]'))  // (1,(2,"s")),3
```

最外層的陣列會展開為引數，因此不會以括號括住。

## Compatibility
- YAYA：從初始版本起可使用
- AYA：版本 5.8 以後可使用
- Tc602-8：改為以 `( )` 括住巢狀陣列、以 `{ }` 括住雜湊後輸出（在此之前，內層也會以 `,` 或 `=` 連接，雜湊的鍵和值中的字串不會以 `"` 括住）

## See Also
- GETERRORLOG
- CLEARERRORLOG
- GETLASTERROR
- SETLASTERROR
