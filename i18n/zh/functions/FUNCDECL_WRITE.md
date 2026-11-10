# FUNCDECL_WRITE

**Category:** メタ操作・特殊関数

## Signature

```
FUNCDECL_WRITE(variable_name, function_name)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| variable_name | 要监视的变量名 |
| function_name | 写入变量时要执行的函数名。指定空字符串（`""` 或 `''`）可取消注册 |

## Returns

- 成功时：1
- 失败时：0

每当向指定变量写入值时，注册的函数都会自动调用。被调用函数的参数如下：

- `_argv[0]`：变量名
- `_argv[1]`：要赋值的新值（`=` 右侧的值）
- `_argv[2]`：变量之前的值

被调用的函数必须返回实际写入变量的值（也可以返回与 `_argv[1]` 不同的值）。

值为通用数组或哈希时，`_argv[1]`、`_argv[2]` 中的元素会是嵌套的数组或哈希（`_argv` 的元素数仍为 3）。在 Tc600-3 之前，数组值无法正确传递（`_argv[1]`、`_argv[2]` 会变为空），直接返回返回值会导致变量变空。

对下标进行赋值（`a[0] = v`）时不会调用。

变量尚不存在时，会先创建一个空变量，再进行注册（之后赋值时会调用）。

## Compatibility

- YAYA：Tc565-1 及之后
- Tc574-8 / Tc603-1：改为在变量尚不存在时创建变量并进行注册（此前不会执行任何操作，而是返回 0）
- Tc600-3：改为以嵌套形式传递数组或哈希值

## See Also

- FUNCDECL_READ
- FUNCDECL_ERASE
