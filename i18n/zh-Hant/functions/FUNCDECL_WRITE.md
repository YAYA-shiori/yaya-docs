# FUNCDECL_WRITE

**Category:** メタ操作・特殊関数

## Signature

```
FUNCDECL_WRITE(variable_name, function_name)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| variable_name | 要監視的變數名稱 |
| function_name | 寫入變數時要執行的函式名稱。指定空字串（`""` 或 `''`）即可解除登錄 |

## Returns

- 成功時：1
- 失敗時：0

每次對指定變數進行寫入時，都會自動呼叫已登錄的函式。被呼叫函式的引數如下：

- `_argv[0]`：變數名稱
- `_argv[1]`：要指派的新值（`=` 的右側）
- `_argv[2]`：變數先前的值

被呼叫的函式必須傳回實際寫入變數的值（也可以傳回與 `_argv[1]` 不同的值）。

值為通用陣列或雜湊時，`_argv[1]` 和 `_argv[2]` 的元素會是巢狀陣列或雜湊（`_argv` 的元素數量仍為 3）。在 Tc600-3 之前，陣列值無法正確傳遞（`_argv[1]` 和 `_argv[2]` 會是空值），若直接傳回傳回值，變數就會變成空值。

對索引的指派（`a[0] = v`）不會呼叫此函式。

變數尚未存在時，會先建立空變數再登錄（之後指派值時便會呼叫函式）。

## Compatibility

- YAYA：Tc565-1 以後
- Tc574-8 / Tc603-1：改為在變數尚未存在時建立並登錄（在此之前不會執行任何動作，而是傳回 0）
- Tc600-3：改為以巢狀形式傳遞陣列或雜湊值

## See Also

- FUNCDECL_READ
- FUNCDECL_ERASE
