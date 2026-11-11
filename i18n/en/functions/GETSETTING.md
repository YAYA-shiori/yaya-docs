# GETSETTING
**Category:** メタ操作・特殊関数

## Signature
```
GETSETTING( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | Identifier for the information to retrieve (one of the strings listed below or a basic settings entry name) |

## Returns
- Success: Requested information (string)
- Failure: Empty string

## Description
Returns information set for the currently running sentence.

`string` can be one of the identifiers listed below, or a number from 0 to 4 for backward compatibility. You can also specify an entry name from [basic settings](../grammar/01-basic-settings.md).

## Information Types
| Identifier | Legacy number | Data returned | Example |
|--------|--------|----------------|-----|
| `coreinfo.version` | 0 | YAYA version number | `"Tc522-1"` |
| (number 1)          | 1 | Current character encoding ID (0=Shift_JIS, 1=UTF-8, 127=OS default) | `0` |
| `coreinfo.path`    | 2 | Absolute directory path | `"c:\hogehoge\"` |
| `coreinfo.name`    | 3 | DLL name | `"YAYA"` |
| `coreinfo.author`  | 4 | DLL author | `"umeici/The Maintenance Shop"` |
| `coreinfo.savefile` | — | Save file path | `"d:/ghost/konno_yayame/..."` |
| `coreinfo.mode`    | — | Execution mode | `"normal"` or `"emergency"` |
| `coreinfo.locale`   | — | Locale for the OS user's regional settings (number and date formats) | `"ja-JP"` |
| `coreinfo.uilocale` | — | Locale for the OS user's display language | `"ja-JP"` |
| `coreinfo.timezone` | — | IANA name of the OS local time zone | `"Asia/Tokyo"` |

`coreinfo.locale` / `coreinfo.uilocale` return names in `language-region` format (BCP 47). They return an empty string if the value cannot be retrieved.

- Windows: The user's default locale name (`coreinfo.uilocale` is the display language)
- Linux / macOS: Determined from environment variables. For `coreinfo.locale`, the first variable set in this order is used: `LC_ALL` → `LC_NUMERIC` → `LANG`. For `coreinfo.uilocale`, the first variable set in this order is used: `LANGUAGE` (first language) → `LC_ALL` → `LC_MESSAGES` → `LANG`. `ja_JP.UTF-8` is converted to `ja-JP`. `C` / `POSIX` or an unset value produces an empty string
- The returned name can be passed directly as the locale argument to [TOUPPER](TOUPPER.md) / [TOLOWER](TOLOWER.md)

`coreinfo.timezone` returns an IANA time zone name such as `Asia/Tokyo`. It returns an empty string if the value cannot be retrieved.

- Windows: Converts the OS time zone name using ICU (`icu.dll`, Windows 10 1903 and later). Older versions of Windows return an empty string
- Linux / macOS: Uses the environment variable `TZ`, or, if it is not set, the target of the `/etc/localtime` link, or, if that is unavailable, `/etc/timezone`. If `TZ` is in POSIX format, such as `JST-9`, that string is returned as is
- For information including daylight saving time and offset, use [GETTIMEZONE](GETTIMEZONE.md)

## Compatibility
- YAYA: Available since the initial version. `coreinfo.mode` was added in Tc556-2, and `coreinfo.locale` / `coreinfo.uilocale` / `coreinfo.timezone` were added in Tc606-1
- AYA: Version 5.8 and later (only numeric arguments 0–4 are supported)

## See Also
- SETSETTING
- [Basic settings](../grammar/01-basic-settings.md)
