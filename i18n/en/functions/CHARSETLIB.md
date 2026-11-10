# CHARSETLIB

**Category:** 外部ライブラリ

## Signature

```
CHARSETLIB(code)
CHARSETLIB()
CHARSETLIB
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| code | (Optional) Specify the character encoding using a character code ID or text representing a character code ([Character Code Names](../grammar/11-character-encoding.md#文字コードの名前)). If the name is unknown, warning W0012 is issued and the setting is not changed |

## Returns

If no argument is specified: Returns the current DLL character encoding setting as a string
If an argument is specified: VOID (returns nothing)

Sets the character encoding used to communicate with external libraries. Must be called before LOADLIB. The default encoding is taken from the charset.extension entry in the configuration file (or charset if unspecified).

CHARSETLIB applies globally to all external libraries, while CHARSETLIBEX lets you configure each library separately.

## Compatibility

- YAYA: Available since the first release. Omitting the argument is supported from Tc531 onward
- AYA: Version 5.8 and later
- Tc574-8 / Tc603-1: Changed so that an unknown character encoding name issues warning W0012 and leaves the setting unchanged (previously, no warning was issued and the OS default was used)

## See Also

- CHARSETLIBEX
- CHARSETIDTOTEXT
