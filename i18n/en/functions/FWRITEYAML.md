# FWRITEYAML
**Category:** ファイル操作

## Signature
```
FWRITEYAML( path, value [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path of the file to write to (a path relative to yaya.dll, or an absolute path) |
| value | The value to convert to YAML. A hash or array (including nested ones) can be passed as a single argument |
| charset | The file's character encoding (optional). Specify a string (such as `"UTF-8"` or `"Shift_JIS"`; [character encoding names](../grammar/11-character-encoding.md#文字コードの名前)) or a number. Defaults to UTF-8 (without a BOM) when omitted or when an empty string is specified |
| pretty | Use block style if 1, or a single line in flow style if 0. Defaults to 1 |

## Returns
- On success: 1
- On failure: 0

## Description
Converts a value to YAML and writes it to a file. If the file already exists, it is overwritten. You do not need to open it with [FOPEN](FOPEN.md).

Value handling and formatting are the same as for [DUMPYAML](DUMPYAML.md#値の対応). In block style, a newline (LF) is added at the end of the file.

The written file can be read back with [FREADYAML](FREADYAML.md) (specify the same charset if it was written using an encoding other than UTF-8).

Strings containing characters that cannot be represented in the specified charset (such as emoji in Shift_JIS) are not written without quotes or as block scalars (`|`); instead, they are enclosed in `"..."`, and those characters are written as `\uXXXX` (or as eight digits, such as `\U0001F600`, for characters outside the BMP). The same applies to keys. The original characters are restored when the file is read back.

Directories are not created. Writing to a nonexistent directory is not possible.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| Too few arguments | W0008 | 8 |
| path is not a string | W0009 | 9 |
| Invalid charset | W0012 / W0009 | 12 / 9 |
| Cannot open the file | W0025 | 25 |
| Character encoding conversion itself failed | W0027 | 27 |
| Write failed | W0013 | 13 |

## Example
```
_conf = IHASH()
_conf["volume"] = 80
_conf["friends"] = ("うにゅう", "まゆら")
_conf["memo"] = "1行目" + CHR(10) + "2行目"

FWRITEYAML("config.yaml", _conf)
// config.yaml:
// friends:
//   - うにゅう
//   - まゆら
// memo: |-
//   1行目
//   2行目
// volume: 80

FWRITEYAML("config.flow.yaml", _conf, "", 0)
// {friends: [うにゅう, まゆら], memo: "1行目\n2行目", volume: 80}
```

## Compatibility
- YAYA: Tc602-5 and later
- Tc603-1: Characters that cannot be represented in the specified charset are now written using the format's escape sequences instead of being silently replaced with `?`. An unknown character encoding name now causes a warning W0012 and the operation to fail (previously, no warning was issued and the OS default was used)

## See Also
- [DUMPYAML](DUMPYAML.md)
- [FREADYAML](FREADYAML.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FWRITETOML](FWRITETOML.md)
