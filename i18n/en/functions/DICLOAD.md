# DICLOAD

**Category:** メタ操作・特殊関数

## Signature

```
DICLOAD( filename [, code] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| filename | The name of the dictionary file to load |
| code | A character encoding ID or name ([character encoding names](../grammar/11-character-encoding.md#文字コードの名前)). If omitted, an empty string, or `default`, the setting in the base configuration file is used. If the name is unknown, warning W0012 is issued, nothing is loaded, and 1 is returned |

## Returns

- `0`: Success
- `1`: Failure

## Description

Dynamically loads the specified dictionary file.

Notes:

- If there is a problem with the dictionary, an error occurs and nothing is changed.
- The loaded dictionary does not take effect until the next request call; the function currently being executed is protected.
- The scope expansion syntax for string interpolation elements does not work after DICLOAD. Consider using EVAL, which can immediately recognize the contents of the loaded dictionary.
- A loaded dictionary can be unloaded with DICUNLOAD, subject to some restrictions.
- While a thread started with [THREADSTART](THREADSTART.md) is running, warning W0032 is issued, nothing is loaded, and 1 is returned.

## Compatibility

- YAYA: Tc556-1 and later
- Tc608-1: Loading is no longer possible while a worker thread is running
- Tc574-8 / Tc603-1: Fixed the issue where a character encoding ID passed as a number was ignored. Passing an unknown character encoding name now issues warning W0012 and fails (previously, the character encoding setting in the base configuration file was used)

## See Also

- DICUNLOAD
- EVAL
