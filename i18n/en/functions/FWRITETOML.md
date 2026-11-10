# FWRITETOML
**Category:** ファイル操作

## Signature
```
FWRITETOML( path, value [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path of the file to write (relative to yaya.dll or an absolute path) |
| value | Hash to convert to TOML (including nested hashes) |
| charset | Character encoding of the file (optional). Specify a string (such as `"UTF-8"` or `"Shift_JIS"`; [character encoding names](../grammar/11-character-encoding.md#文字コードの名前)) or a number. If omitted or an empty string, UTF-8 (without a BOM) is used. The TOML specification requires UTF-8, so you would normally omit this argument |
| pretty | If 1, format the output using `[table]` headers; if 0, put each top-level key on its own line. Defaults to 1 |

## Returns
- On success: 1
- On failure: 0

## Description
Converts a hash to TOML and writes it to a file. If the file already exists, it is overwritten. You do not need to open it with [FOPEN](FOPEN.md).

Supported values and formatting are the same as for [DUMPTOML](DUMPTOML.md#値の対応).

The written file can be read back with [FREADTOML](FREADTOML.md).

Strings containing characters that cannot be represented in the specified charset (such as emoji in Shift_JIS) are enclosed in `"..."` (or `"""..."""` if they contain line breaks), not `'...'`, and those characters are written as `\uXXXX` (or as eight-digit escapes such as `\U0001F600` for characters outside the BMP). Keys are handled the same way. The original characters are restored when read back.

Directories are not created. You cannot write to a directory that does not exist.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| Too few arguments | W0008 | 8 |
| path is not a string | W0009 | 9 |
| Invalid charset | W0012 / W0009 | 12 / 9 |
| value is not a hash, or an array element is empty (VOID) | W0027 (the cause is also output) | 27 |
| Could not open the file | W0025 | 25 |
| Character encoding conversion itself failed | W0027 | 27 |
| Write failed | W0013 | 13 |

## Example
```
_conf = IHASH()
_conf["volume"] = 80
_conf["friends"] = ("うにゅう", "まゆら")
_conf["memo"] = "1行目" + CHR(10) + "2行目"

FWRITETOML("config.toml", _conf)
// config.toml:
// friends = ["うにゅう", "まゆら"]
// memo = """
// 1行目
// 2行目"""
// volume = 80
```

## Compatibility
- YAYA: Tc602-5 and later
- Tc603-1: Characters that cannot be represented in the specified charset are now written using format-specific escapes instead of being silently replaced with `?`. Passing an unknown character encoding name now causes the operation to fail with warning W0012 (previously, it was treated as the OS default without a warning)

## See Also
- [DUMPTOML](DUMPTOML.md)
- [FREADTOML](FREADTOML.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FWRITEYAML](FWRITEYAML.md)
