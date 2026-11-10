# PROCESSGLOBALDEFINE
**Category:** メタ操作・特殊関数

## Signature
```
PROCESSGLOBALDEFINE(string)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | The string to preprocess |

## Returns
- Success: The processed string after applying global definitions
- Failure: -1

## Description
Performs the same processing as the preprocessing operation (string replacement) defined by `#globaldefine`. For details about the preprocessor, see [Preprocessing](../grammar/08-preprocessor.md).

## Compatibility
- YAYA: Available since version Tc559-1

## See Also
- [Preprocessing](../grammar/08-preprocessor.md)
