# RE_OPTION
**Category:** 正規表現

## Signature
```
RE_OPTION( オプション文字列 )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| Option string | Perl-compatible regular expression option string to set (i, s, m, x). If omitted, returns the current settings |

## Returns
A string indicating the currently enabled options (any combination of i, s, m, and x)

## Description
Sets Perl-compatible regular expression options.

Supported options:
- **i**: Case-insensitive matching
- **m**: Treats the input as multiple lines
- **s**: Makes the wildcard (.) match newline characters as well
- **x**: Ignores comments (#) and whitespace in the regular expression pattern

By default, no options are enabled (calling `RE_OPTION("")` also restores this state). Called with no arguments, the function returns the current options as a string.

Options can also be specified in the pattern (for example, `(?i)abc`). See [Regular expressions](../grammar/14-regular-expressions.md#オプション) for details.

## Compatibility
- YAYA: Tc534-1 onward

## See Also
- RE_MATCH
- RE_SEARCH
- RE_REPLACE
- [Regular expressions](../grammar/14-regular-expressions.md)
