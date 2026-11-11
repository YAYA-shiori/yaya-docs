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
| code | A character encoding ID or character encoding name ([character encoding names](../grammar/11-character-encoding.md#文字コードの名前)). If omitted, an empty string, or `default`, the setting in the basic configuration file is used. If the name is unknown, warning W0012 is issued, nothing is loaded, and 1 is returned |

## Returns

- `0`: Success
- `1`: Failure

## Description

Dynamically loads the specified dictionary file.

Notes:

- If there is a problem with the dictionary, an error occurs and nothing is changed.
- The loaded dictionary does not take effect until the next request is processed, and the function currently running is protected.
- [Range-limited expansion](../grammar/06-string-embedding.md#範囲付き展開) of string embedding elements does not work after DICLOAD. Consider using EVAL, which can recognize the contents of the loaded dictionary immediately.
- A loaded dictionary can be unloaded with DICUNLOAD, subject to certain restrictions.
- While a thread started with [THREADSTART](THREADSTART.md) is running, warning W0032 is issued, nothing is loaded, and 1 is returned.

## Compatibility

- YAYA: Tc556-1 and later
- Tc608-1: Changed behavior so that loading is not possible while a worker thread is running
- Tc574-8 / Tc603-1: Fixed an issue where a character encoding ID passed as a number was ignored. Changed behavior so that passing an unknown character encoding name results in warning W0012 and a failure (previously, the dictionary was loaded using the setting in the basic configuration file)

## See Also

- DICUNLOAD
- EVAL
