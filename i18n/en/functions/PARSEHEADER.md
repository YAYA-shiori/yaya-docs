# PARSEHEADER
**Category:** 型取得/変換

## Signature
```
PARSEHEADER( str [, conv ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | A string in a header format, such as HTTP or SHIORI |
| conv | Optional. If nonzero, converts values to integers or real numbers using the same rules as [TOAUTOEX](TOAUTOEX.md). Defaults to 0 (no conversion) |

## Returns
- On success: a hash with the following keys
- On failure: empty (VOID)

| Key | Content |
|------|------|
| `start` | Start line (such as `GET SHIORI/3.0` or `HTTP/1.1 200 OK`). Empty string if there is no start line |
| `header` | Hash of header keys → values. If a key occurs more than once, the last value is retained |
| `key` | Array of header keys (in order of appearance, including duplicates) |
| `value` | Array of header values (in order of appearance). Contains converted values if `conv` is nonzero |
| `rawvalue` | Array of values before conversion (strings, in order of appearance) |
| `body` | String after the blank line. Empty string if there is no blank line |

## Description
Parses a string in the form “start line + `key: value` lines + blank line + body,” such as an HTTP, SHIORI, SAORI, or SSTP request or response, and returns the result as a hash and arrays. This is faster than extracting the content one line at a time with [STRSTR](STRSTR.md) or [SUBSTR](SUBSTR.md).

- Line endings can be either CRLF or LF
- The first blank line ends the headers; everything after it becomes `body`
- Each line is split into a key and value at the first `:`. One whitespace character (a space or tab) immediately after the `:` is skipped; any remaining whitespace is kept as-is (the value of `Key:  a` is ` a`)
- A line is not treated as a header line if the text before the first `:` is empty or contains whitespace. If this is the first line, it is stored in `start`; if it is a later line, it is ignored. This also allows parsing strings that contain only headers and have no start line
- Header keys are case-sensitive
- When `conv` is nonzero, conversion follows the same rules as [TOAUTOEX](TOAUTOEX.md): a value is converted only if it matches the original when converted back to a string. `12` becomes an integer, but `007` and `1.5` remain strings

The `header` hash is sorted by key, so use `key` / `value` / `rawvalue` when the order of appearance is needed.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| str is not a string | W0009 | 9 |

## Example
```
request
{
	_r = PARSEHEADER(_argv[0], 1)
	// _argv[0] が
	//   GET SHIORI/3.0
	//   Charset: UTF-8
	//   ID: OnBoot
	//   Reference0: 12
	//   Reference1: 007
	// のとき

	_r["start"]                 // GET SHIORI/3.0
	_r["header"]["ID"]          // OnBoot
	_r["header"]["Reference0"]  // 12（整数）
	_r["header"]["Reference1"]  // 007（文字列）
	_r["key"]                   // Charset,ID,Reference0,Reference1
	_r["rawvalue"][2]           // 12（文字列）
}
```

```
_nl = CHR(13) + CHR(10)
_r = PARSEHEADER('HTTP/1.1 200 OK' + _nl + 'Content-Type: text/plain' + _nl + _nl + 'hello')
_r["start"]                     // HTTP/1.1 200 OK
_r["header"]["Content-Type"]    // text/plain
_r["body"]                      // hello
```

In a dictionary shared with the 500 series, you can use `#ifdef __AYA_SYSTEM_SYSFUNC_PARSEHEADER__` to check whether this function is available and write separate code accordingly ([Preprocessing](../grammar/08-preprocessor.md#500-系と-600-系で共用する辞書)).

## Compatibility
- YAYA: Tc602-3 and later

## See Also
- [TOAUTOEX](TOAUTOEX.md)
- [HASH_SPLIT](HASH_SPLIT.md)
- [PARSEJSON](PARSEJSON.md)
- [SPLIT](SPLIT.md)
