# FUNCDECL_ERASE

**Category:** メタ操作・特殊関数

## Signature

```
FUNCDECL_ERASE(variable_name, function_name)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| variable_name | 要監視的變數名稱 |
| function_name | 刪除變數時要執行的函式名稱。指定空字串（`''` 或 `""`）即可取消註冊 |

## Returns

- 成功時：1
- 失敗時：0

變數刪除時，會自動呼叫指定的函式。被呼叫函式的引數如下：

- `_argv[0]`：變數名稱
- `_argv[1]`：變數目前的值

系統會忽略被呼叫函式的傳回值。

若變數尚不存在，會先建立空變數再註冊。

## Compatibility

- YAYA：Tc565-1 以後
- Tc574-8 / Tc603-1：改為在變數尚不存在時建立變數並註冊（在此之前不會執行任何動作，而是傳回 0）

## See Also

- FUNCDECL_WRITE
- FUNCDECL_READ
