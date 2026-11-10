# OUTPUTNUM
**Category:** メタ操作・特殊関数

## Signature
```
OUTPUTNUM(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | Name of the function to check (string) |

## Returns
The number of selectable candidates output by the target function (integer)

## Description
Returns the number of selectable candidates output by the specified function. It gets the number of output candidates by calling the target function with an empty argument list. For information about how functions select among alternatives, see [Function selection method](../grammar/02-functions.md#選択方式).

## Compatibility
- YAYA: Available since version Tc569-1

## See Also
- [Function selection method](../grammar/02-functions.md#選択方式)
