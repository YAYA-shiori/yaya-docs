# FREADYAML
**Category:** ファイル操作

## Signature
```
FREADYAML( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path to the YAML file to read (a path relative to yaya.dll or an absolute path) |
| charset | File encoding (optional). Specify a string (such as `"UTF-8"` or `"Shift_JIS"`; see [Encoding Names](../grammar/11-character-encoding.md#文字コードの名前)) or a number. Defaults to UTF-8 |

## Returns
- On success: The value converted from YAML (see [Value Mapping](#値の対応) below)
- On failure: Empty (VOID)

## Description
Reads and parses an entire YAML file, then returns it as a value such as a hash or array. You do not need to open the file with [FOPEN](FOPEN.md).

YAYA parses YAML itself. It supports the subset commonly used in configuration files (see [Supported Syntax](#対応している書き方) below), but does not implement the entire YAML specification.

- A leading UTF-8 BOM is ignored. Line endings can be either CRLF or LF
- An empty file or a file containing only comments returns empty (VOID). This is not an error

### Supported Syntax

| Syntax | Example |
|--------|----|
| Block-style mappings and sequences | `key: value`, `- item`. You can also place `- item` entries at the same indentation level below `key:` |
| Flow style | `[1, 2]`, `{a: 1, b: 2}`. Nesting and multiple lines are also supported |
| Unquoted strings | Can span multiple lines (line breaks become spaces, and blank lines become line breaks) |
| Quoted strings | `'...'` (`''` represents `'`), `"..."` (escapes such as `\n` `\t` `\"` `\\` `\x41` `あ` `\U0001F600`) |
| Block scalars | `\|` (preserves line breaks), `>` (converts line breaks to spaces). Trailing line break handling `\|-` `\|+` and indentation indicators such as `\|2` are also supported |
| Comments | From `#` to the end of the line (when following a value, a space is required before `#`) |
| Anchors and aliases | Reference a value marked with `&name` using `*name` (the value is copied) |
| Merge keys | Include mappings with `<<: *name` or `<<: [*a, *b]`. Explicit keys and keys written earlier take precedence |
| Document separators | A leading `---` (and directives such as `%YAML` before it), and a trailing `...` |
| Tags | `!!str` (and `!`) makes the value a string. `!!int` `!!float` `!!bool` `!!null` determine the type even when quoted. Other tags are ignored |

The following are not supported. If present, they produce W0026.

- Multiple documents in one file (a second `---`)
- Complex keys (keys beginning with `? `, or keys written in flow style)
- Tabs used for indentation (tabs inside values are allowed)

### Value Mapping

Types are determined according to the rules of the YAML 1.2 Core Schema.

| YAML | YAYA |
|------|------|
| Mapping | Hash. Keys are always strings |
| Sequence | Generic array (nested arrays and hashes can be elements) |
| Integer (`123` `-4` `0o17` `0x1F`) | Integer. Values beyond the integer range in decimal notation are real numbers |
| Real number (`1.5` `1e3` `.5` `.inf` `-.inf` `.nan`) | Real number |
| `true` / `false` (including `True` `TRUE`, etc.) | Integer 1 / 0 |
| `null` / `~` / no value | Empty (VOID) |
| Everything else, quoted strings, and block scalars | String |

- The following differs from YAML 1.1 processors: `yes` `no` `on` `off` are strings, `017` is decimal 17, `1_000` is a string, and dates such as `2001-12-14` are also strings
- Mapping key order is not preserved. Keys are ordered as in the hash (see [HASH_KEYS](HASH_KEYS.md)). A canonical integer key such as `1` can be accessed with either `h[1]` or `h["1"]`
- If the same key is written twice, the later value is used
- Deeply nested values (more than 256 levels) and values whose aliases expand to more than 1 million elements in total cause an error (to prevent malicious files from exhausting memory)

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| path is not a string | W0009 | 9 |
| Invalid charset | W0012 / W0009 | 12 / 9 |
| Cannot open file | W0025 | 25 |
| Cannot parse as YAML or uses unsupported syntax | W0026 (also outputs the line number and cause) | 26 |

## Example
config.yaml:
```yaml
# ゴーストの設定
name: さくら
age: 17
height: 158.5
visible: true
memo: ~
tags: [ghost, shell]
talk:
  greeting: |
    こんにちは。
    今日もいい天気ですね。
  random:
    - おはよう
    - こんばんは
defaults: &defaults
  volume: 80
  speed: 2
voice:
  <<: *defaults
  speed: 3
```

```
_y = FREADYAML("config.yaml")
_y["name"]                   // さくら
_y["tags"][1]                // shell
_y["height"]                 // 実数の 158.5
_y["visible"]                // 1
_y["memo"]                   // 空（VOID）
_y["talk"]["greeting"]       // "こんにちは。" + 改行 + "今日もいい天気ですね。" + 改行
_y["talk"]["random"][0]      // おはよう
_y["voice"]["volume"]        // 80（defaults から取り込んだもの）
_y["voice"]["speed"]         // 3
```

## Compatibility
- YAYA: Available since Tc602-5
- Tc603-1: Passing an unknown encoding name now fails with warning W0012 (previously, it was treated as the OS default without a warning)

## See Also
- [PARSEYAML](PARSEYAML.md)
- [FWRITEYAML](FWRITEYAML.md)
- [FREADJSON](FREADJSON.md)
- [FREADTOML](FREADTOML.md)
- [Nested Values and Multidimensional Assignment](../grammar/13-nesting.md)
