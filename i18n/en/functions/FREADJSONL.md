# FREADJSONL
**Category:** ファイル操作

## Signature
```
FREADJSONL( path [, start [, maxlines [, key ...]]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path to the JSON Lines file to read (relative to yaya.dll, or absolute) |
| start | Byte position at which to start reading (optional; defaults to 0). If it points to the middle of a line, that line is skipped and reading starts at the next line ([Reading from the middle of a line](#行の途中から読む)). Must be between 0 and 2147483647 inclusive |
| maxlines | Maximum number of lines to read (optional; defaults to 0, meaning read to the end of the file). Blank lines and lines that cannot be parsed are also counted |
| key | Key to retrieve (optional; any number can be specified). If a line's top-level value is an object, returns only the values of these keys ([Reading specified keys](#キーを指定して読む)). Strings only |

## Returns
- On success: A hash with the following keys
  - `rows`: An array of values from lines successfully parsed as JSON (using the same conversion as [FREADJSON](FREADJSON.md#値の対応))
  - `pos`: An array of byte positions at the start of the lines corresponding to the elements of `rows` (in the same order as `rows`)
  - `end`: The position where reading stopped. Pass this as `start` to continue reading
  - `skipped`: The number of lines skipped because they could not be parsed as JSON
- On failure: Empty (VOID)

## Description
Reads a JSON Lines file (text with one JSON value per line; `.jsonl`) and returns an array of values, one per line. There is no need to open it with [FOPEN](FOPEN.md).

This produces the same result as reading one line at a time with [FREAD](FREAD.md) and parsing it with [PARSEJSON](PARSEJSON.md), but is faster because it reads the file in UTF-8 in one operation and parses it line by line, without repeating function calls and string conversions for every line. It is suited to reading files such as conversation logs or histories that grow to tens of thousands of lines as data is appended.

- Only UTF-8 encoding is supported. An initial BOM is ignored
- Lines are separated by LF. A CR at the end of a line is ignored. Lines containing only whitespace are skipped
- Lines that cannot be parsed as JSON are skipped without a warning and counted in `skipped`. Lines whose top-level value is not an object or array (such as `42`) are also included in `rows` if they can be parsed
- `/* */` and `//` comments are not allowed (JSON Lines has no comments, unlike [FREADJSON](FREADJSON.md))
- Positions in `pos` are byte offsets from the start of the file, as used by [FSEEK](FSEEK.md) and [FTELL](FTELL.md)

### When the last line is incomplete
If the last line does not end with a newline, it is read if it can be parsed as JSON; otherwise, it is left unread (as another program may still be writing it). In that case, `end` is set to the start of that line. Pass `end` as the next `start` to read from that line once it has been completed.

### Reading from the middle of a line
If the byte immediately before `start` is not a newline, `start` is treated as being in the middle of a line, and the first (partial) line is discarded. To read only the end of a file, pass a position calculated by subtracting the number of bytes to read from `FSIZE`. If `start` is at the beginning of a line (0, a previous `end`, or a value from `pos`), reading starts from that line.

If `start` is greater than or equal to the file size, nothing is read, `rows` and `pos` are empty arrays, and `end` is set to `start`.

### Reading specified keys
When `key` is specified and a line's top-level value is an object, only the values of those keys are placed in a hash and added to `rows`. The entire line is parsed as JSON, but only the specified keys are converted (string conversion and hash creation), making this faster and producing a smaller result when extracting only values such as timestamps from lines containing large values such as request bodies.

- Only top-level keys can be specified. `.` cannot be used to refer to lower levels (`"a.b"` refers to a key whose name contains `.`)
- Keys absent from the line are not created in the resulting hash. Keys with `null` values remain with a VOID value, as when converting the entire value
- For lines whose top-level value is not an object, the entire value is converted without using `key`
- Keys may also be passed as an array (the outer array is expanded in function arguments). For example, use `FREADJSONL("a.jsonl", 0, 0, _keys)`

### Errors
| Condition | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| path is not a string. start or maxlines is not an integer. key is not a string | W0009 | 9 |
| start is negative or greater than 2147483647. maxlines is negative | W0012 | 12 |
| Cannot open file | W0025 | 25 |

## Example
history.jsonl:
```
{"display":"こんにちは","timestamp":1790311762291,"project":"C:\\work\\a"}
{"display":"つづき","timestamp":1790311800000,"project":"C:\\work\\b"}
```

```
_r = FREADJSONL("history.jsonl", 0, 0, "timestamp", "project")
_r["rows"][0]["project"]    // C:\work\a
_r["rows"][1]["timestamp"]  // 1790311800000
_r["pos"][1]                // 2 行目の頭のバイト位置
_r["skipped"]               // 0
```

Read only newly appended lines (save `end` and pass it as `start` in the next call):
```
if GETTYPE(lastpos) == 0 {
    lastpos = 0
}
_r = FREADJSONL("history.jsonl", lastpos, 0, "timestamp", "project")
lastpos = _r["end"]
foreach _r["rows"]; _row {
    // 新しく書き足された行だけが順に入る
}
```

## Compatibility
- Tc608-6: Added

## See Also
- [FREADJSON](FREADJSON.md)
- [PARSEJSON](PARSEJSON.md)
- [FREAD](FREAD.md)
- [FSEEK](FSEEK.md)
