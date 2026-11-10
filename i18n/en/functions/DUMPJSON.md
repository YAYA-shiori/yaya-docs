# DUMPJSON
**Category:** 型取得/変換

## Signature
```
DUMPJSON( value [, pretty] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| value | The value to convert to JSON. A hash or array (including nested ones) can be passed as a single argument |
| pretty | If 1, formats the output with line breaks and indentation. Defaults to 0 (single line) |

## Returns
- On success: A JSON string
- If no arguments are provided: An empty string

## Description
Converts a value to a JSON string and returns it. This is the reverse conversion of [PARSEJSON](PARSEJSON.md).

### Value mappings

| YAYA | JSON |
|------|------|
| Hash | Object. Keys are converted to strings (`1` becomes `"1"`). The order follows the hash key order |
| Generic array | Array |
| Integer | Number. 64-bit integers are written without loss of precision |
| Real | Number. A decimal point or exponent is always included (`1.0`, `0.1`, `1e+300`) |
| String | String |
| Empty (VOID) | `null` |

- Integer values 1 / 0 become the numbers `1` / `0`. They do not become `true` / `false`.
- Real numbers are written in the shortest notation that reads back as the same value. NaN and infinity cannot be represented in JSON, so they become `null`.
- For strings, only `"` `\` and control characters (such as line breaks and tabs) are escaped. Non-ASCII characters such as Japanese characters and `/` are written as-is.
- The decimal point is always `.` regardless of the locale.

When formatting output, indentation uses four spaces and line breaks use LF. Empty arrays and hashes are kept on a single line as `[]` / `{}`.

Reading the result back with [PARSEJSON](PARSEJSON.md) restores the original value. However, a real number with an integer value (such as `1.0`) becomes an integer.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |

## Example
```
_h = IHASH()
_h["name"] = "さくら"
_h["tags"] = ("ghost", "shell")
_h["height"] = 158.5

DUMPJSON(_h)
// {"height":158.5,"name":"さくら","tags":["ghost","shell"]}

DUMPJSON(_h, 1)
// {
//     "height": 158.5,
//     "name": "さくら",
//     "tags": [
//         "ghost",
//         "shell"
//     ]
// }

DUMPJSON(("a", 1))          // ["a",1]
DUMPJSON(未定義の変数)       // null
```

## Compatibility
- YAYA: Tc602-1 and later
- Tc602-5: Fixed the issue where the minimum integer (-9223372036854775808) was output as only `-`, resulting in invalid JSON

## See Also
- [FWRITEJSON](FWRITEJSON.md)
- [PARSEJSON](PARSEJSON.md)
- [DUMPXML](DUMPXML.md)
