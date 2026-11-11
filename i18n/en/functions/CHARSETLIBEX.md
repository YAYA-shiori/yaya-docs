# CHARSETLIBEX

**Category:** 外部ライブラリ

## Signature

```
CHARSETLIBEX(path, code)
CHARSETLIBEX(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | DLL location. Specify a relative path from the YAYA directory or an absolute path |
| code | (Optional) A character encoding ID or text identifier representing a character encoding ([character encoding names](../grammar/11-character-encoding.md#文字コードの名前)). If the name is unknown, warning W0012 is issued and the setting is left unchanged |

## Returns

If code is omitted: Returns the current character encoding setting for the specified DLL as a string
If code is specified: VOID (returns nothing)

Specify the character encoding used to communicate with an external library individually. Available from Tc530-2 onward when called before LOADLIB, and can be set during initialization. It is recommended to specify the character encoding in advance with this function during initialization. The default encoding is obtained from the charset.extension entry in the configuration file (or charset if unspecified). However, the default for SAORI-basic on POSIX environments (Tc604-1 onward) is UTF-8.

## Compatibility

- YAYA: Available since the first release. Argument omission is supported from Tc531 onward
- Tc574-8 / Tc603-1: Changed so that passing an unknown character encoding name issues warning W0012 and leaves the setting unchanged (previously, no warning was issued and the OS default was used)

## See Also

- CHARSETLIB
- CHARSETTEXTTOID
