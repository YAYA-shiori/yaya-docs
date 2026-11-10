# UNDEFGLOBALDEFINE
**Category:** メタ操作・特殊関数

## Signature
```
UNDEFGLOBALDEFINE( definename )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| definename | The directive name declared with `#globaldefine` |

## Returns
- 0: Success
- 1: Failure

## Description
Disables and deletes a directive declared with `#globaldefine`.

Text defined with `#globaldefine` cannot be inserted directly into a dictionary file. The preprocessor is applied even when the text is enclosed in quotation marks. To work around this, split the target string into parts (for example, concatenate `"TEST_" + "DEF"`).

## Compatibility
- YAYA: Tc561-1 and later

## See Also
- DICUNLOAD
- SETGLOBALDEFINE
- ISGLOBALDEFINE
- PROCESSGLOBALDEFINE
