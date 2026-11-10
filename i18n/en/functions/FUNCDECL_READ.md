# FUNCDECL_READ

**Category:** メタ操作・特殊関数

## Signature

```
FUNCDECL_READ(variable_name, function_name)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| variable_name | Name of the variable to monitor |
| function_name | Name of the function to execute when the variable is read. Specify an empty string (`''`) to unregister |

## Returns

- On success: 1
- On failure: 0

The specified function is automatically called whenever the variable is read. The arguments passed to the function are as follows:

- `_argv[0]`: Variable name
- `_argv[1]`: Current value of the variable

The called function must return the value to actually retrieve (it can return a value different from the current value).

When the value is a generic array or hash, `_argv[1]` contains a nested array or hash (the number of elements in `_argv` remains 2). Before Tc600-3, only the first element of an array value was placed in `_argv[1]`.

If the variable does not exist yet, an empty variable is created before registration.

## Compatibility

- YAYA: Tc565-1 and later
- Tc600-3: Changed to pass array and hash values as nested values
- Tc574-8 / Tc603-1: Changed to create and register the variable if it does not exist yet (previously, nothing was done and 0 was returned)

## See Also

- FUNCDECL_WRITE
- FUNCDECL_ERASE
