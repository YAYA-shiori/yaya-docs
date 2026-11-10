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
| path | DLL file location. Specify a path relative to the YAYA directory or an absolute path |
| code | (Optional) Character code ID or text identifier representing a character code ([Character Code Names](../grammar/11-character-encoding.md#文字コードの名前)). If the name is unknown, warning W0012 is issued and the setting is not changed |

## Returns

If code is omitted: Returns the current character encoding setting for the specified DLL as a string
If code is specified: VOID (returns nothing)

Specifies the character encoding used to communicate with an external library individually. From Tc530-2 onward, this takes effect when called before LOADLIB and can be set during initialization. The default encoding is taken from the charset.extension entry in the configuration file (or charset if unspecified). However, the default for SAORI-basic in POSIX environments (Tc604-1 onward) is UTF-8.

## Compatibility

- YAYA: Available since the first release. Omitting the argument is supported from Tc531 onward
- Tc574-8 / Tc603-1: Changed so that an unknown character encoding name issues warning W0012 and leaves the setting unchanged (previously, no warning was issued and the OS default was used)

## See Also

- CHARSETLIB
- CHARSETTEXTTOID
