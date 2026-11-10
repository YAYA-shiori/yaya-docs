# GETVARLIST
**Category:** メタ操作・特殊関数

## Signature
```
GETVARLIST( [ prefix ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| prefix | (Optional) Returns only variable names that begin with the specified string. If omitted, returns all variables |

## Returns
- On success: Generic array of variable names
- On failure: IARRAY

## Description
Returns a list of the variables currently held. If `prefix` is specified, only variable names that begin with that string are returned.

## Example

Examples of a function that erases all variables whose names begin with a specified string, and a function that erases all variables matching a regular expression.

```
ERASEALLVARBEGINAS {
	_L= GETVARLIST(_argv[0])
	foreach _L;_V {
		ERASEVAR(_V)
	}
}

ERASEALLVARINRE {
	_L= GETVARLIST
	foreach _L;_V {
		if RE_GREP(_V,_argv[0])
			ERASEVAR(_V)
	}
}
```

## Compatibility
- YAYA: Available since the initial release

## See Also
- GETFUNCLIST
