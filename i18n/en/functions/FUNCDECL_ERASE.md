# FUNCDECL_ERASE

**Category:** メタ操作・特殊関数

## Signature

```
FUNCDECL_ERASE(variable_name, function_name)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| variable_name | The name of the variable to monitor |
| function_name | The name of the function to call when the variable is deleted. Specify an empty string (`''` or `""`) to unregister it |

## Returns

- On success: 1
- On failure: 0

The specified function is called automatically when the variable is deleted. The arguments passed to the function are as follows:

- `_argv[0]`: Variable name
- `_argv[1]`: Current value of the variable

The system ignores the return value of the called function.

If the variable does not yet exist, an empty variable is created before registration.

## Compatibility

- YAYA: Tc565-1 or later
- Tc574-8 / Tc603-1: Changed to create and register the variable if it does not yet exist (previously, it did nothing and returned 0)

## See Also

- FUNCDECL_WRITE
- FUNCDECL_READ
