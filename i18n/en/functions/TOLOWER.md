# TOLOWER
**Category:** 文字列操作

## Signature
```
TOLOWER( string [ , locale ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String to convert |
| locale | (Optional) Locale name. If omitted, uses C mode (converts only A-Z to a-z) |

## Returns
- Success: Converted lowercase string
- Failure: VOID

## Description
Converts all uppercase letters in a string to lowercase and returns the result. If locale is omitted, C mode is used (only A-Z are converted to a-z).

Specify a name such as `"ja-JP"`, `"tr_TR"`, or `"tr_TR.UTF-8"` for locale. Conversion follows that locale's rules and also applies to non-ASCII characters (such as `É`→`é` and full-width Latin letters). In Turkish (`tr-TR`), `I` becomes `ı`. `"C"` and `"POSIX"` select C mode, while an empty string uses the OS user's configured locale. You can also use the name returned by `coreinfo.locale` in [GETSETTING](GETSETTING.md).

- Windows: Uses the OS locale name. C runtime locale names such as `"Japanese_Japan.932"` can also be used
- Linux / macOS: Requires a locale installed on the OS (one listed by `locale -a`). If the character encoding is omitted, as in `tr_TR`, the UTF-8 version is searched for first
- Does not affect other operations or the process locale

If you specify an unavailable locale, warning W0012 is issued ([GETLASTERROR](GETLASTERROR.md) returns 12), and the result converted in C mode is returned.

## Example
```
_str = 'sAkuRa'
_str = TOLOWER( _str )
_str // 'sakura'
```

## Compatibility
- YAYA: Since the initial version (the locale parameter is available from Tc569-5)
- Tc606-1: Changed how locale is handled. A locale can be specified using a name such as `ja-JP`, and conversion is performed without changing the process locale. An unavailable locale issues warning W0012 and conversion is performed in C mode (previously, no warning was issued and conversion used the current locale)
- AYA: 5.8 and later

## See Also
- TOUPPER
