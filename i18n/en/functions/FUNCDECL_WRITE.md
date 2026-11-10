# FUNCDECL_WRITE

**Category:** メタ操作・特殊関数

## Signature

```
FUNCDECL_WRITE(variable_name, function_name)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| variable_name | Name of the variable to monitor |
| function_name | Name of the function to execute when the variable is written. Specify an empty string (`""` or `''`) to unregister |

## Returns

- On success: 1
- On failure: 0

The registered function is automatically called whenever the specified variable is written to. The arguments passed to the function are as follows:

- `_argv[0]`: Variable name
- `_argv[1]`: New value to be assigned (the right-hand side of `=`)
- `_argv[2]`: Previous value of the variable

The called function must return the value to actually write to the variable (it can return a value different from `_argv[1]`).

When the value is a generic array or hash, the elements of `_argv[1]` and `_argv[2]` are nested arrays or hashes (the number of elements in `_argv` remains 3). Before Tc600-3, array values were not passed correctly (`_argv[1]` and `_argv[2]` were empty), so returning the value as-is left the variable empty.

This function is not called when assigning to an index (`a[0] = v`).

If the variable does not exist yet, an empty variable is created before registration (the function is called when a value is assigned later).

## Compatibility

- YAYA: Tc565-1 and later
- Tc574-8 / Tc603-1: Changed to create and register the variable if it does not exist yet (previously, nothing was done and 0 was returned)
- Tc600-3: Changed to pass array and hash values as nested values

## See Also

- FUNCDECL_READ
- FUNCDECL_ERASE
