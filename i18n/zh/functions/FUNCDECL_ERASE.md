# FUNCDECL_ERASE

**Category:** メタ操作・特殊関数

## Signature

```
FUNCDECL_ERASE(variable_name, function_name)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| variable_name | 要监视的变量名 |
| function_name | 删除变量时要执行的函数名。指定空字符串（`''` 或 `""`）可取消注册 |

## Returns

- 成功时：1
- 失败时：0

变量被删除时，会自动调用指定的函数。被调用函数的参数如下：

- `_argv[0]`：变量名
- `_argv[1]`：变量当前的值

系统会忽略被调用函数的返回值。

如果变量尚不存在，则先创建一个空变量，再进行注册。

## Compatibility

- YAYA：Tc565-1 及以后
- Tc574-8 / Tc603-1：改为在变量尚不存在时创建变量并注册（此前不会执行任何操作，而是返回 0）

## See Also

- FUNCDECL_WRITE
- FUNCDECL_READ
