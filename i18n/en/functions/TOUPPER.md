# TOUPPER
**Category:** 文字列操作

## Signature
```
TOUPPER( string [ , locale ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String to convert |
| locale | (Optional) Locale name. If omitted, uses C mode (converts only a-z to A-Z) |

## Returns
- On success: String converted to uppercase
- On failure: VOID

## Description
Converts all lowercase letters in a string to uppercase and returns the result. If locale is omitted, C mode is used (only a-z are converted to A-Z).

The format of locale is the same as the [locale strings accepted by setlocale](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/setlocale-wsetlocale). Specify a name such as `"ja-JP"`, `"tr_TR"`, or `"tr_TR.UTF-8"` for locale. Conversion follows that locale's rules and also applies to non-ASCII characters (for example, `é`→`É` and full-width Latin letters). In Turkish (`tr-TR`), `i` becomes `İ`. `"C"` and `"POSIX"` select C mode, and an empty string uses the locale configured in the OS user settings. You can also use the name returned by `coreinfo.locale` from [GETSETTING](GETSETTING.md).

- Windows: Use an OS locale name. C runtime locale names such as `"Japanese_Japan.932"` can also be used
- Linux / macOS: The locale must be installed on the OS (that is, appear in `locale -a`). If the character encoding is omitted, as in `tr_TR`, the UTF-8 version is searched for first
- This does not affect other processing or the process locale

If you specify an unavailable locale, warning W0012 is issued ([GETLASTERROR](GETLASTERROR.md) returns 12), and the result of conversion in C mode is returned.

## Example
```
_str = 'sAkuRa'
_str = TOUPPER( _str )
_str // 'SAKURA'
```

## Compatibility
- YAYA: Available since the initial version (the locale parameter is available from Tc569-5)
- Tc606-1: Changed how locale is handled. A locale can be specified by a name such as `ja-JP`, and conversion does not switch the process locale. An unavailable locale issues warning W0012 and performs conversion in C mode (previously, no warning was issued and conversion used the current locale)
- AYA: 5.8 and later

## See Also
- TOLOWER
- TRANSLATE
