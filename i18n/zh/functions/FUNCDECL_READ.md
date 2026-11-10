# FUNCDECL_READ

**Category:** メタ操作・特殊関数

## Signature

```
FUNCDECL_READ(variable_name, function_name)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| variable_name | 要监视的变量名 |
| function_name | 读取变量时要执行的函数名。指定空字符串（`''`）可取消注册 |

## Returns

- 成功时：1
- 失败时：0

每当读取变量时，指定的函数都会自动调用。被调用函数的参数如下：

- `_argv[0]`：变量名
- `_argv[1]`：变量的当前值

被调用的函数必须返回实际获取的值（也可以返回与当前值不同的值）。

值为通用数组或哈希时，`_argv[1]` 中会包含嵌套的数组或哈希（`_argv` 的元素数仍为 2）。在 Tc600-3 之前，数组值只有首个元素会放入 `_argv[1]`。

变量尚不存在时，会先创建一个空变量，再进行注册。

## Compatibility

- YAYA：Tc565-1 及之后
- Tc600-3：改为以嵌套形式传递数组或哈希值
- Tc574-8 / Tc603-1：改为在变量尚不存在时创建变量并进行注册（此前不会执行任何操作，而是返回 0）

## See Also

- FUNCDECL_WRITE
- FUNCDECL_ERASE
