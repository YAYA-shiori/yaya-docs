# FUNCDECL_READ

**Category:** メタ操作・特殊関数

## Signature

```
FUNCDECL_READ(variable_name, function_name)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| variable_name | 要監視的變數名稱 |
| function_name | 讀取變數時要執行的函式名稱。指定空字串（`''`）即可解除登錄 |

## Returns

- 成功時：1
- 失敗時：0

每次讀取變數時，都會自動呼叫指定的函式。被呼叫函式的引數如下：

- `_argv[0]`：變數名稱
- `_argv[1]`：變數目前的值

被呼叫的函式必須傳回實際取得的值（也可以傳回與目前值不同的值）。

值為通用陣列或雜湊時，`_argv[1]` 會是巢狀陣列或雜湊（`_argv` 的元素數量仍為 2）。在 Tc600-3 之前，只有陣列值的第一個元素會放入 `_argv[1]`。

變數尚未存在時，會先建立空變數再登錄。

## Compatibility

- YAYA：Tc565-1 以後
- Tc600-3：改為以巢狀形式傳遞陣列或雜湊值
- Tc574-8 / Tc603-1：改為在變數尚未存在時建立並登錄（在此之前不會執行任何動作，而是傳回 0）

## See Also

- FUNCDECL_WRITE
- FUNCDECL_ERASE
