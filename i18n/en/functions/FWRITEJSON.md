# FWRITEJSON
**Category:** ファイル操作

## Signature
```
FWRITEJSON( path, value [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path of the file to write (relative to yaya.dll or an absolute path) |
| value | Value to convert to JSON. Hashes and arrays, including nested ones, can be passed as a single argument |
| charset | Character encoding of the file (optional). Specify a string (such as `"UTF-8"` or `"Shift_JIS"`; [character encoding names](../grammar/11-character-encoding.md#文字コードの名前)) or a number. If omitted or an empty string, UTF-8 (without a BOM) is used |
| pretty | If 1, format the output with line breaks and indentation. Defaults to 1 (format the output) |

## Returns
- On success: 1
- On failure: 0

## Description
Converts a value to JSON and writes it to a file. If the file already exists, it is overwritten. You do not need to open it with [FOPEN](FOPEN.md).

Supported values and formatting are the same as for [DUMPJSON](DUMPJSON.md#値の対応). When formatted, a line break (LF) is added at the end of the file.

The written file can be read back with [FREADJSON](FREADJSON.md). If you wrote it using a charset other than UTF-8, specify the same charset when reading it back.

Characters that cannot be represented in the specified charset (such as emoji in Shift_JIS) are written using JSON escapes like `\uXXXX`. Characters outside the BMP are written as a pair of escapes, such as `\uD83D\uDE00`. They are restored to the original characters when read back.

Directories are not created. You cannot write to a directory that does not exist.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| Too few arguments | W0008 | 8 |
| path is not a string | W0009 | 9 |
| Invalid charset | W0012 / W0009 | 12 / 9 |
| Could not open the file | W0025 | 25 |
| Character encoding conversion itself failed | W0027 | 27 |
| Write failed | W0013 | 13 |

## Example
```
_conf = IHASH()
_conf["volume"] = 80
_conf["friends"] = ("うにゅう", "まゆら")

FWRITEJSON("config.json", _conf)
// config.json:
// {
//     "friends": [
//         "うにゅう",
//         "まゆら"
//     ],
//     "volume": 80
// }

FWRITEJSON("config.min.json", _conf, "", 0)   // UTF-8 で1行に
```

## Compatibility
- YAYA: Tc602-1 and later
- Tc603-1: Characters that cannot be represented in the specified charset are now written using format-specific escapes instead of being silently replaced with `?`. Passing an unknown character encoding name now causes the operation to fail with warning W0012 (previously, it was treated as the OS default without a warning)

## See Also
- [DUMPJSON](DUMPJSON.md)
- [FREADJSON](FREADJSON.md)
- [FWRITEXML](FWRITEXML.md)
