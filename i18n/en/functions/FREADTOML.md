# FREADTOML
**Category:** ファイル操作

## Signature
```
FREADTOML( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path of the TOML file to read (a path relative to yaya.dll or an absolute path) |
| charset | Character encoding of the file (optional). Specify as a string (such as `"UTF-8"` or `"Shift_JIS"`. [Character encoding names](../grammar/11-character-encoding.md#文字コードの名前)) or a number. Defaults to UTF-8 (the TOML specification requires UTF-8) |

## Returns
- On success: The hash converted from TOML (see [Value mapping](#値の対応) below)
- On failure: Empty (VOID)

## Description
Reads and parses the entire TOML file, then returns it as a hash. It does not need to be opened with [FOPEN](FOPEN.md).

YAYA parses TOML itself. It supports [TOML v1.0.0](https://toml.io/ja/v1.0.0). It also accepts the newlines and trailing commas in inline tables, and the `\e` and `\xHH` escapes added in v1.1.

- A UTF-8 BOM at the beginning of the file is ignored. Line endings can be either CRLF or LF
- The top level is always a hash. An empty file or a file containing only comments produces an empty hash
- Constructs prohibited by the specification, such as defining the same key or table twice, redefining a table created with dotted keys using `[table]`, or adding to an inline table later, cause an error

### Value mapping

| TOML | YAYA |
|------|------|
| Table (`[table]`, inline table `{ }`, dotted keys `a.b = 1`) | Hash |
| Array of tables (`[[array]]`) | Generic array of hashes |
| Array | Generic array (can be nested, with arrays or hashes as elements) |
| String (`"..."` `'...'` `"""..."""` `'''...'''`) | String |
| Integer (`42` `1_000` `0xDEAD` `0o755` `0b1101`) | Integer |
| Real number (`3.14` `5e+22` `inf` `nan`) | Real number |
| `true` / `false` | Integer 1 / 0 |
| Date and time (`1979-05-27T07:32:00Z`, `1979-05-27`, `07:32:00`, etc.) | String as written |

- Integers outside the integer range (from -2^63 inclusive to 2^63 exclusive) cause an error
- The order of keys is not preserved. Keys are ordered as hash keys are (see [HASH_KEYS](HASH_KEYS.md))

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| path is not a string | W0009 | 9 |
| charset is invalid | W0012 / W0009 | 12 / 9 |
| Cannot open the file | W0025 | 25 |
| Cannot parse as TOML | W0026 (also outputs the line number and cause) | 26 |

## Example
config.toml:
```toml
# ゴーストの設定
title = "設定"
updated = 2026-09-27T12:00:00+09:00

[ghost]
name = "さくら"
age = 17
visible = true
tags = ["ghost", "shell"]
path = 'C:\ssp\ghost'

[[friends]]
name = "うにゅう"

[[friends]]
name = "まゆら"
```

```
_t = FREADTOML("config.toml")
_t["title"]                 // 設定
_t["updated"]               // 文字列の 2026-09-27T12:00:00+09:00
_t["ghost"]["name"]         // さくら
_t["ghost"]["visible"]      // 1
_t["ghost"]["tags"][1]      // shell
_t["ghost"]["path"]         // C:\ssp\ghost
_t["friends"][1]["name"]    // まゆら

foreach _t["friends"]; _f {
    // _f に {name: うにゅう}、{name: まゆら} のハッシュが順に入る
}
```

## Compatibility
- YAYA: Since Tc602-5
- Tc603-1: Passing an unknown character encoding name now causes a failure with warning W0012 (previously, no warning was issued and the OS default was used)

## See Also
- [PARSETOML](PARSETOML.md)
- [FWRITETOML](FWRITETOML.md)
- [FREADJSON](FREADJSON.md)
- [FREADYAML](FREADYAML.md)
- [Nested values and multidimensional assignment](../grammar/13-nesting.md)
