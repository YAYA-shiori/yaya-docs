# GETFUNCLIST
**Category:** メタ操作・特殊関数

## Signature
```
GETFUNCLIST( [prefix] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| prefix | (Optional) Return only function names that begin with this string. If omitted, return all functions |

## Returns
- On success: A generic array of function names
- On failure: IARRAY

## Description
Returns a list of functions in the currently loaded dictionary.

If `prefix` is specified, only function names beginning with that string are returned. If omitted, all functions are returned.

## Example

Examples of functions that call all functions whose names begin with a specified string, and all functions that match a regular expression.

```
CALLALLFUNCTIONBEGINAS {
	_L= GETFUNCLIST(_argv[0])
	foreach _L;_V {
		EVAL(_V)
	}
}

CALLALLFUNCTIONINRE {
	_L= GETFUNCLIST
	foreach _L;_V {
		if RE_GREP(_V,_argv[0])
			EVAL(_V)
	}
}
```

## Compatibility
- YAYA: Available since the initial release

## See Also
- GETVARLIST
- GETSYSTEMFUNCLIST
